# import

import ctypes
import time

# info

version = 'v.24062023'
print(f'Wallpaper Manager\n{version}\n')

# options

# if this parameter prints when and what wallpaper will be installed
# example:
# At 6:00 wallpaper change on C:/Wallpapers/morning.png
print_configs = True

# if enabled, information about processing config will be printed
print_debug = False

# this is the period of time after which the program will check the time in the system
wait_time = 5  # seconds

# opening of config

try:
    config = open('config.txt', 'r')
except:
    config = open('config.txt', 'w')
    print('No any config')
    quit()
finally:
    print('Config read\n')

config_read_lines = config.readlines()

if ''.join(config_read_lines) == '':
    print('No any config')
    quit()

images_dictionary = {}

for element in config_read_lines:
    if '\n' in element:
        element = element[:-1]
    element = element.split(';')
    images_dictionary[element[0]] = element[1:]
    if print_debug:
        print(element)

if print_debug:
    print('lines at config.txt', config_read_lines)
    print('hours and dirs of images', images_dictionary, '\n')


# functions

# setting wallpaper
def set_wallpaper(path: str) -> int:
    cs = ctypes.c_buffer(path.encode())
    spi_set_desktop_wallpaper = 0x14
    return ctypes.windll.user32.SystemParametersInfoA(spi_set_desktop_wallpaper, 0, cs, 0)


# get time

def get_time():
    get_hour = time.strftime('%H')
    return int(get_hour)


# work

if print_configs:
    for x in images_dictionary:
        print(f'At {x}:00 wallpaper change on {(images_dictionary[x])[0]}')

while True:
    for hour in images_dictionary:
        if get_time() == int(hour):
            image = images_dictionary[hour]
            set_wallpaper(image[0])

        time.sleep(wait_time)
