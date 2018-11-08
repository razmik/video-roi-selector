"""
Copy the data set into the original dataset folder (i.e., root_folder_path)
All the video frames will be copied to new folder (out_folder)
- Duplicated frames will be removed automatically.
- Frame numbering will update to universal 6-digit system.
"""

from os import listdir, makedirs
from os.path import isfile, join, isdir, exists
from shutil import copyfile
from tqdm import tqdm

root_folder_path = "E:\Data\Vollyball_data/original".replace('\\', '/')
out_folder = "E:\Data\Vollyball_data/all".replace('\\', '/')

# Create out directory if not exists
if not exists(out_folder):
    makedirs(out_folder)

if __name__ == '__main__':

    folders = [f for f in listdir(root_folder_path) if isdir(join(root_folder_path, f))]

    print('Moving files...')

    for folder_path in tqdm(folders):

        folder_path = join(root_folder_path, folder_path)
        files = [f for f in listdir(folder_path) if isfile(join(folder_path, f))]

        for f in files:

            src = join(root_folder_path, folder_path, f)
            dest = join(out_folder, '{0:06d}.jpg'.format(int(f.split('.')[0])))

            copyfile(src, dest)

    print('Completed.')
