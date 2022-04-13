#! /usr/bin/env python3

import backup
import prepare

import sys
import unittest

prepare = prepare()
backup = backup(prepare.target(), prepare.origin())

if __name__ == "__main__":

    if os.argv[1] == "b" or os.argv[1] == "backup":
        if prepare.is_first_run():
            try:
                prepare.setup()
            except:
                print("Error creating the configuration file.")
            else:
                prepare.finish_first_run()
                backup.tar_xz()

    else:
        print("Running tests...")
        



