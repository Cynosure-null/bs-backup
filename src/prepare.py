#!/usr/bin/env python

import os
import toml

class Prepare:
    def __init__(self, config_path = os.path.expanduser("~/.config/bs-backup.conf")):
        self.config_path = config_path;
        self.config_load = toml.load(self.config_path);
        self.config_dump = toml.dump(self.config_path);

        def is_first_run():
            is_first_run = self.config_load['is_first_run'];

            if is_first_run == 'true' or is_first_run == True:
                return False;
            else:
                return True;

        def origin():
            return self.config_load['origin_directory'];

        def target():
            return self.config_load['target_directory'];

        def setup():
            config_file = open(self.config_path, 'w');
            default_config = """
            title = \"bs-backup configuration\"

            # Checks if this is the first time bs-backup has ran
            is_first_run

            #The directory you wish to backup. /home/username/ is default
            origin_directory = \" /home/{} \"

            # The directory you wish to save your backups to
            # The default is /mnt/
            # CHANGE THIS VALUE. Leaving as is will back up the hard drive on itself.

            target_directory = \" /mnt/ \"

            """
            default_config = default_config.format(os.getlogin())
            config_file.write(default_config)
            config_file.close()

        def finish_first_run():
            # The same as prepare.setup(), just a differnt value for is_first_run
            config_file = open(self.config_path, 'w');
            default_config = """
            title = \"bs-backup configuration\"

            # Checks if this is the first time bs-backup has ran
            is_first_run = \" false \"

            #The directory you wish to backup. /home/username/ is default
            origin_directory = \" /home/{} \"

            # The directory you wish to save your backups to
            # The default is /mnt/
            # CHANGE THIS VALUE. Leaving as is will back up the hard drive on itself.

            target_directory = \" /mnt/ \"

            """
            default_config = default_config.format(os.getlogin())
            config_file.write(default_config)
            config_file.close()
