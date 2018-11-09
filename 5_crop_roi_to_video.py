"""
Display the selected ROI's for given ROI data file.
"""
from os.path import join
import cv2
import numpy as np
import pandas as pd

data_folder_path = "E:\Data\Vollyball_data/all".replace('\\', '/')
player_roi_data_path = 'data/player_2_frames_9510_10015.csv'
out_filename = player_roi_data_path.replace('.csv', '.avi')

frame_rate = 30
enable_display = False

if __name__ == '__main__':

    df = pd.read_csv(player_roi_data_path)

    # Set resolution
    im = cv2.imread(join(data_folder_path, df['frame'].iloc[0]))
    height, width = im.shape[:2]
    resolution = (width, height)

    # Set video file
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    out = cv2.VideoWriter(out_filename, fourcc, frame_rate, resolution)

    for index, row in df.iterrows():

        filename = join(data_folder_path, row['frame'])

        # Read image
        frame = cv2.imread(filename)

        black_bg = np.zeros_like(frame)

        # Capture ROI
        x, y, w, h = row['x'], row['y'], row['w'], row['h']
        roi = frame[y:y + h, x:x + w]

        # Set new frame with black background
        black_bg[y:y + h, x:x + w] = roi

        # Write to outfile
        out.write(black_bg)

        if enable_display:
            cv2.imshow('Output video', frame)
            cv2.waitKey(2)

    print('Completed.')
