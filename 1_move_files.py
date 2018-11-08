from os import listdir
from os.path import isfile, join, isdir
from shutil import copyfile
from tqdm import tqdm

root_folder_path = "E:\Data\Vollyball_data/original".replace('\\', '/')
out_folder = "E:\Data\Vollyball_data/all".replace('\\', '/')


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
