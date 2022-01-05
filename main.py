#!/usr/bin/env python3

import os
import sys
import glob
from urllib.parse import urlparse, parse_qs

path = '/Users/lulu/Music/Music/Media.localized/Music/"Unknown Artist"/"Unknown Album"/'


def get_last_created():
    list_of_files = glob.glob(path.replace('"', '') + '*')
    return max(list_of_files, key = os.path.getctime).split('/')[-1]


def download(array, again):
    error = []
    for elm in array:
        link = urlparse(elm)
        link = link.scheme + '://' + link.netloc + link.path + '?v=' + parse_qs(link.query)['v'][0]
        ok = os.system('youtube-dl -x --embed-thumbnail --audio-format mp3 {}'.format(link))
        if ok == 0:
            os.system('mv *.mp3 {}'.format(path))
            os.system('open {}"{}"'.format(path, get_last_created()))
        else:
            print("Error")
            error.append(link)
    print(error)

    if len(error) != 0 and again < 5:
        download(error, again + 1)
    else:
        return


if __name__ == '__main__':
    download(sys.argv[1:], 0)

