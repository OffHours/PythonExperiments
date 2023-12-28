import cv2
import numpy as np
import time
import glob
import os

import emailing

from threading import Thread

emailing.authentication()

#Importing the feed from camera 1, 0 is generally the built in cam on a laptop
video = cv2.VideoCapture(1)
#Waiting for the code to aquire the feed
time.sleep(1)

first_frame = None
email_sent = 0
count = 1

trig_old = False

def clean_folder():
    images = glob.glob('images/*.png')
    for image in images:
        os.remove(image)

while True:
    trig_new = False

    #Read the frame and store it i a variabe, the 'check' variable is true when a feed is aquired
    check, frame = video.read()
    #Convert to greyscale to to give us less data to process, means less processing power is needed.
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    #Gaussian blur to remove noise from the video, "(21, 21)" is the amount of blurriness, must be uneven number."0" is the standard deviation "sigmaX"
    gray_frame_gau = cv2.GaussianBlur(gray_frame, (21, 21), 0)
    
    #medianBlur_frame = cv2.medianBlur(gray_frame_gau, 15) #Commented out because it made no real difference for my application
    
    # Adjusts the brightness by adding 10 to each pixel value 
    brightness = 0 
    # Adjusts the contrast by scaling the pixel values by 2.3 
    contrast = 2.7  
    con_bri_frame = cv2.addWeighted(gray_frame_gau, contrast, np.zeros(gray_frame_gau.shape, gray_frame_gau.dtype), 0, brightness) 

    #Storing the first frame to use as master for comparison
    if first_frame is None:
        first_frame = con_bri_frame
    
    #Comparing the new frame with the master frame and storing it in the delta_frame variable
    delta_frame = cv2.absdiff(first_frame, con_bri_frame)
    
    #Converting from grayscale to, black or white, using a threshold function if>15 = 255
    #The function returns a list and we extract the second item from the list
    thresh_frame = cv2.threshold(delta_frame, 15, 255, cv2.THRESH_BINARY)[1]
    
    #Dilate the frame, expand the pixels? or something like that
    dil_frame = cv2.dilate(thresh_frame, None, iterations=2)
    
    contours, check = cv2.findContours(dil_frame, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
     
    for contour in contours:
        if cv2.contourArea(contour) < 10000:
            continue
        x, y, w, h = cv2.boundingRect(contour)
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 3)
        
        trig_new = True
        
        cv2.imwrite(f'images\camera_triggered {count}.png', frame)
        count = count + 1
    
       
    if trig_new != trig_old and trig_new == False:
        
        #print("I'm sending an email here!")
        email_sent = email_sent + 1
        print(f"I've sent {email_sent} emails")
        
        emailAdr = 'user@Example.com'
        subject = 'Someone triggered your camera'
        
        emailBody = 'This is the person!'
    
        images_all = glob.glob('images/*.png')
        
        the_image = int(len(images_all)/2)
        
        attachment = f'images\camera_triggered {the_image}.png' #This is an attached image!
        
        #Create a separate thread for handling the email and clean_folder function
        email_thread = Thread(target=emailing.gmail_send_message, args=(emailAdr, emailBody, attachment, subject))
        email_thread.daemon = True
        
        clean_thread = Thread(target=clean_folder)
        clean_thread.daemon = True
        
        email_thread.start()
        
        count = 1
        
    cv2.imshow('My Origin Video', frame)
    #cv2.imshow('My Video', dil_frame)
    #cv2.imshow('My grey', con_bri_frame)
    #cv2.imshow('My Video2', first_frame)
    #print(delta_frame)
    
    key = cv2.waitKey(1)
    
    if key == ord('q'):
        break
    
    trig_old = trig_new
    
video.release()

clean_thread.start() #Would be better if it was inside the While loop but did not get run until after the send_email thread is finished.