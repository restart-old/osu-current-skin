# Imports
from src.osu_skins.API.baseAPI import get_user_name
from src.osu_skins.API.baseAPI import baseAPI
from src.osu_skins.Utils.clear import clear
from src.osu_skins.Utils.dir import curr_dir
import os

# Global variables
usr_name = get_user_name()


def main():
    osu_dir = f'C:\\Users\\{usr_name}\\AppData\\Local\\osu!'
    if os.path.exists(osu_dir):
        osu_dir = osu_dir
    else:
        try:
            with open(f'{curr_dir("main.py")}\\osu!folder.txt', 'r+') as osu_folder_file:
                osu_dir = osu_folder_file.readline()
                if os.path.exists(osu_dir):
                    osu_dir = osu_dir
                else:
                    print("Could not find the osu directory!")
                    return
        except FileNotFoundError:
            print("Could not find the osu directory!")
            return
    osk = baseAPI(osu_dir=osu_dir)
    skin_name = osk.get_skin_name()
    clear()
    print(f'Current Skin: {skin_name}')
    osk.remove_curr_skin_output()
    osk.duplicate_skin_zip()
    osk.rename_to_osk()


if __name__ == '__main__':
    main()

# Dev: @RestartFU
# Version: 0.1
# Credits: Nozzle's Team
