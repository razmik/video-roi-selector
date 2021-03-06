"""
Display the selected ROI's for given ROI data file.
"""
from os.path import join
import cv2
import pandas as pd

data_folder_path = "E:\Data\Vollyball_data/all".replace('\\', '/')
player_roi_data_path = 'data/player_1_frames_9527_9561.csv'

bounding_box_color = (107, 244, 66)
bounding_box_thickness = 2

if __name__ == '__main__':

    df = pd.read_csv(player_roi_data_path)

    for index, row in df.iterrows():

        filename = join(data_folder_path, row['frame'])

        # Read image
        frame = cv2.imread(filename)

        # Draw ROI
        x, y, w, h = row['x'], row['y'], row['w'], row['h']
        cv2.rectangle(frame, (x, y), (x+w, y+h), bounding_box_color, bounding_box_thickness)

        # Display frames with ROI tracked
        cv2.imshow("Display", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    print('Completed.')
