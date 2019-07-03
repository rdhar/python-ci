import os
import shutil


def ignore_files(dir, files):
    return [f for f in files if os.path.isfile(os.path.join(dir, f))]


def copyDirectory(src, dest):
    try:
        shutil.copytree(src, dest, ignore=ignore_files)
    # Directories are the same
    except shutil.Error as e:
        print('Directory not copied. Error: %s' % e)
    # Any error saying that the directory doesn't exist
    except OSError as e:
        print('Directory not copied. Error: %s' % e)


copyDirectory("dirin", "dirout")
