from fer import Video
from fer import FER
import os
import sys
import pandas as pd
import matplotlib.pyplot as plt
import cv2

def partA(location_videofile):

    face_detector = FER(mtcnn=True)
    input_video = Video(location_videofile)

    # The Analyze() function will run analysis on every frame of the input video. 
    # It will create a rectangular box around every image and show the emotion values next to that.
    # Finally, the method will publish a new video that will have a box around the face of the human with live emotion values.
    processing_data = input_video.analyze(face_detector, display=False)

    # We will now convert the analysed information into a dataframe.
    # This will help us import the data as a .CSV file to perform analysis over it later
    vid_df = input_video.to_pandas(processing_data)
    vid_df = input_video.get_first_face(vid_df)
    vid_df = input_video.get_emotions(vid_df)

    # Plotting the emotions against time in the video
    pltfig = vid_df.plot(figsize=(20, 8), fontsize=16).get_figure()


def displayPlot():
    # display plot of predicted emotion over time
    fer_df = pd.read_csv("data.csv")
    fer_df.plot()
    plt.savefig()

def partB():
    vid = cv2.VideoCapture(0)
    frame_width = int(vid.get(3))
    frame_height = int(vid.get(4))
    size = (frame_width, frame_height)
    
    result = cv2.VideoWriter('my_video.mp4', 
                         cv2.VideoWriter_fourcc(*'MJPG'),
                         10, size)
  
    while(True):
        # Capture the video frame by frame
        ret, frame = vid.read()

        # write frame to video
        result.write(frame)
            
        # Display the resulting frame
        cv2.imshow('frame', frame)
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
  
    # After the loop release the cap object
    vid.release()
    result.release()
    # Destroy all the windows
    cv2.destroyAllWindows()

    partA("videos/my_video.mp4")

def main():
    location_videofile = "videos/Video_One.mp4"
    # location_videofile = "videos/Video_Two.mp4"
    partA(location_videofile)
    displayPlot()

    partB()
    displayPlot()

main()

