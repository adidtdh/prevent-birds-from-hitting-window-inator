import cv2, time, base64
import numpy as np
import requests
import datetime
import os
import playsound

url = "http://admin:a@192.168.29.179/IMAGE.JPG" #replace this url with your url for an image
#the next two lines are the login headers. Replace it with your login. If you dont know it, it probebly is what is put down right there
user = "admin"
password = "password"
first_frame = None
dir_path = os.path.dirname(os.path.realpath(__file__))
while True:
    switch = False
    url_response = requests.get(url, auth=(user, password)) #goes to the camera and grabs the current frame from the url
    img_array = np.array(bytearray(url_response.content), dtype=np.uint8)
    img = cv2.imdecode(img_array, -1)
    frame = img
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray,(21,21), 0)

    if first_frame is None:
        first_frame = gray
        continue

    delta_frame = cv2.absdiff(first_frame,gray)
    thresh_frame = cv2.threshold(delta_frame, 30, 255, cv2.THRESH_BINARY)[1]
    thresh_frame = cv2.dilate(thresh_frame, None, iterations=2)

    (cnts,_) = cv2.findContours(thresh_frame.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    for contour in cnts:
        if cv2.contourArea(contour) < 50:
            switch = True
            continue

    #these show what the camera sees it is not nessessary for the program so you can comment it out
    cv2.imshow("Threshold Frame", thresh_frame)
    cv2.imshow("orgiginal", delta_frame)
    cv2.imshow("unedited", frame)

    key=cv2.waitKey(1)

    nowd = datetime.datetime.now()
    #every 3 seconds it takes a new picture. Lower this if your envirnment has really heavy lighting changes.
    if nowd.second % 3 == 0:
        first_frame = None

    if switch:
        # takes a picture becasue birds are cool and saves it to a directory with the date and time. This also isnt nessessary
        filename = "{0},{1},{2},{3},{4},{5}.png".format(nowd.year,nowd.month,nowd.day,nowd.hour,nowd.minute,nowd.second )
        print(f"bird detected at {nowd}")
        cv2.imwrite(os.path.join(f"{dir_path}/birdpics" , filename), frame)
        #plays a loud sound to scare the bird away so that it doesnt hit the window
        playsound.playsound('eren.mp3', True) #
    #press q to end program
    if cv2.waitKey(1) == ord('q'):
        break

video.release()
cv2.destroyAllWindows