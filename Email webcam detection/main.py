import cv2              # Image processing library
import time             # Time library for delay
from emailing import send_email


video = cv2.VideoCapture(0)   # Initialize webcam
time.sleep(1)                 # Delay for camera warm-up

first_frame = None            # Store first frame as background
status_list = []

while True:
    status = 0
    check, frame = video.read()   # Read frame from camera
    
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)  
    # Convert to grayscale
    gray_blur = cv2.GaussianBlur(gray, (21, 21), 0)  
    # Apply blur to reduce noise

    if first_frame is None:        # If this is the first frame
        first_frame = gray_blur    # Save as background
        continue                   # Skip to next frame

    delta = cv2.absdiff(first_frame, gray_blur)  
    # Find difference from background (motion detection)
    thresh = cv2.threshold(delta, 50, 255, cv2.THRESH_BINARY)[1]  
    # Apply threshold
    dilate = cv2.dilate(thresh, None, iterations=2)  
    # Fill gaps in motion areas

    contours, _ = cv2.findContours(dilate, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)  
    # Find objects

    object_number = 1   # Object counter
    
    for contour in contours:   # For each detected object
        if cv2.contourArea(contour) < 3000:  # If area is too small
            continue            # Skip (it's noise)
        
        x, y, w, h = cv2.boundingRect(contour)  
        # Get bounding rectangle coordinates
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)  
        # Draw green rectangle

        cv2.putText(frame, f"Object {object_number}", (x, y-10),  
                    # Display object number
                    cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)
        
        object_number += 1   # Increment counter
        status = 1           # Motion detected

    status_list.append(status)
    status_list = status_list[-2:]

    if status_list[0] == 1 and status_list[1] == 0:  # If motion just stopped
        send_email()          # Send email notification

    cv2.imshow("Motion Detection", frame)  # Display video

    if cv2.waitKey(1) == ord("q"):  # If 'q' is pressed
        break                       # Exit loop

video.release()        # Release camera
cv2.destroyAllWindows()  # Close windows