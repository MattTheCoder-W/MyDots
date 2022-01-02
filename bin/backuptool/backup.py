#!/usr/bin/env python3
import os
import json
import shutil


class Backup:
    def __init__(self):
        self.config_file = "backup_config.json"
        self.config = json.load(open(self.config_file, "r"))

    def perform(self):
        for file in os.listdir("/home/m4t1"):
            if file not in self.config['ommit']:
                if file in self.config['dots']:
                    print(file)
                    if file.config['dots'][file] == "*":
                        shutil.copytree(file, f"/home/m4t1/backup/{file}")
                else:
                    print(file)
                    shutil.copytree(file, f"/home/m4t1/backup/{file}")
                    


if __name__ == "__main__":
    backup = Backup()
    backup.perform()
    print("[*] >> END")

