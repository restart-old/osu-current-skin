import getpass
import shutil
import os


def get_user_name():
    usr = getpass.getuser()
    return usr


class baseAPI:
    def __init__(self, osu_dir):
        self.osu_dir = osu_dir
        self.config_file = f'{osu_dir}\\osu!.{get_user_name()}.cfg'
        self.skin_dir = f'{osu_dir}\\Skins'
        self.output_dir = f'output'

    def get_skin_name(self):
        with open(self.config_file, 'r', encoding='utf-8') as config_file:
            config_file = config_file.readlines()
            for line in config_file:
                line_ = line.lower()
                line_ = line_.strip()
                if line_.rpartition(' = ')[0] == 'skin':
                    skin_name = line.strip().rpartition(' = ')[2]
        return skin_name

    def duplicate_skin_zip(self, file_path_ext=False):
        skin_name = self.get_skin_name()
        if file_path_ext is not False:
            try:
                duplicated_file = f'{self.output_dir}\\{skin_name}.{file_path_ext}'
                return duplicated_file

            except FileNotFoundError:
                print("File not found")
        try:
            output_filename = f'{self.output_dir}\\{skin_name}'
            dir_name = f'{self.skin_dir}\\{skin_name}'
            shutil.make_archive(output_filename, 'zip', dir_name)
            duplicated_file = f'{self.output_dir}\\{skin_name}.zip'
            return duplicated_file
        except FileNotFoundError:
            print('failed')

    def rename_to_osk(self):
        skin_name = self.get_skin_name()
        curr_skin = self.duplicate_skin_zip(file_path_ext='zip')
        os.rename(curr_skin, f'{self.output_dir}\\{skin_name}.osk')

    def remove_curr_skin_output(self):
        for root, dirs, files in os.walk(self.output_dir):
            for file in files:
                os.remove(f'{self.output_dir}\\{file}')
# Dev: @RestartFU
# Version: 0.1
# Credits: Nozzle's Teams
