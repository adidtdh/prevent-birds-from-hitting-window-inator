# Prevent Birds From Hitting Window Inator
Plays a loud sound that prevents birds from hitting the window (made for wifi camera)

 It is really quite simple. It just plays a short and loud audio clip which plays when movement is detected near the window. I put the camera on a stool and pointed it at the window so that birds would stop flying right into it. Eventually this wasreplaced with a net but this was a nice temporary solution. 
 
 The camera that I used was an old camera from 2004 or something like that and it was literally made before I was born. I think that the resolution is 320:240. Chances are that your camera is better than that so change line 34 so that the number is higher
 
 
 ```python
for contour in cnts:
        if cv2.contourArea(contour) < 50: #THIS LINE
            switch = True
            continue
 ```
 
 This also takes a picture of the bird because brids are cool. And the audio clip is from Attack On Titan because thats cool too. You can change the audio to anything you want just name the file eren.mp3. That is all :D.

![Heres a bird](https://raw.githubusercontent.com/adidtdh/prevent-birds-from-hitting-window-inator/master/camera/birdpics/2020%2C4%2C26%2C17%2C25%2C15.png)

Heres the picture of the bird I got. It is in the bottom right corner. 
