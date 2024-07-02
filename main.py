import os
import sys


def main():
    file = sys.argv[1]

    extensions = ("jpeg", "jpg", "png")

    if not file.split(".")[-1] in extensions:
        raise Exception("file type not supported")

    cmd = f'ffmpeg -i {file} -vf scale=128:128 {"128px-" + file}'

    os.system(cmd)


main()
