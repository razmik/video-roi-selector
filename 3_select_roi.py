"""
Select start and end frames, and run the algorithm.
You will prompt each frame within the selected range, for ROI (region of interest) selection.
All the selected ROI's will be recorded in 'data' folder with the respective frame name.
# https://www.learnopencv.com/how-to-select-a-bounding-box-roi-in-opencv-cpp-python/
"""
from os import listdir
from os.path import isfile, join
from tqdm import tqdm
import cv2
import pandas as pd

root_folder_path = "E:\Data\Vollyball_data/all".replace('\\', '/')
out_folder = 'data/'

player_id = 1
start_frame = 9527
end_frame = 9561

allowed_range = list(range(start_frame, end_frame+1))


if __name__ == '__main__':

    files = sorted([f for f in listdir(root_folder_path) if isfile(join(root_folder_path, f)) if int(f.split('.')[0]) in allowed_range])

    boxes = []
    for f in tqdm(files):

        file_path = join(root_folder_path, f)

        # Read image
        frame = cv2.imread(file_path)

        # Select ROI
        roi = cv2.selectROI("Frame Grabber", frame, fromCenter=False, showCrosshair=True)

        # Set roi
        boxes.append([f, roi[0], roi[1], roi[2], roi[3]])

    # Save ROIs.
    cols = ['frame', 'x', 'y', 'w', 'h']
    pd.DataFrame(boxes, columns=cols).to_csv(join(out_folder, 'player_{}_frames_{}_{}.csv'.format(player_id, start_frame, end_frame)), index=None)

    print('Completed.')
