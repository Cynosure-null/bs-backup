#!/usr/bin/env python3

import tarfile
import os

class Backup:
    def __init__(self, target, origin):
        self.target = target
        self.origin = origin

        def tar_xz():
            # Taken from https://clay-atlas.com/us/blog/2021/08/16/python-en-tarfile-compress-decompress/

            target_tar = tarfile.open(self.target, 'w:xz')
            origin_tar = tarfile.open(self.target, 'w:xz')

            for root, dirs, files in os.walk(self.origin):
                for file_name in files:
                    target_tar.add(self.origin(root, filename))

            tar.close()

