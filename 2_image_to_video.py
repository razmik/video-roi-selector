"""
Convert all the frames into a video.
"""
from os import listdir
from os.path import isfile, join
import cv2
from tqdm import tqdm

root_folder_path = "E:\Data\Vollyball_data/all".replace('\\', '/')
out_filename = "E:\Data\Vollyball_data/vollyball.avi".replace('\\', '/')

frame_rate = 30
enable_display = False

if __name__ == '__main__':

    files = sorted([f for f in listdir(root_folder_path) if isfile(join(root_folder_path, f))])

    # Set resolution
    im = cv2.imread(join(root_folder_path, files[0]))
    height, width = im.shape[:2]
    resolution = (width, height)

    # Set video file
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    out = cv2.VideoWriter(out_filename, fourcc, frame_rate, resolution)

    for f in tqdm(files):

        f = join(root_folder_path, f)
        im = cv2.imread(f)
        im = cv2.resize(im, resolution)

        frame = im
        out.write(frame)

        if enable_display:
            cv2.imshow('Output video', frame)
            cv2.waitKey(2)

    out.release()
    cv2.destroyAllWindows()

    print('Video Saved.')
