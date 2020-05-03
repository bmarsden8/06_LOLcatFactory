import os
import shutil
import subprocess

from pip._vendor import requests


def main():
    print_header()
    folder = get_or_create_folder_location()
    download_cats(folder)
    open_folder(folder)


def print_header():
    print('--------------------------------')
    print('   WELCOME TO LOLCAT FACTORY')
    print('--------------------------------')


def get_or_create_folder_location() -> object:
    folder = '/catphotos'
    file_path = os.path.dirname(__file__) + folder

    if not os.path.exists(file_path) or not os.path.dirname(file_path):
        print('Creating directory at {0}.......'.format(file_path))
        os.mkdir(file_path)

    print('Found or created directory at {0}'.format(file_path))
    return file_path


def download_cats(folder):
    cat_count = 8
    for i in range(1, cat_count + 1):
        name = 'lolcat_{}'.format(i)
        get_save_cat_data(folder, name)


def get_save_cat_data(folder, name):
    url = 'http://consuming-python-services-api.azurewebsites.net/cats/random'
    data = get_cat_data(url)
    save_cat_data(folder, name, data)


def get_cat_data(url):
    data = requests.get(url, stream=True)
    return data.raw


def save_cat_data(folder, name, data):
    file_name = os.path.join(folder, name + '.jpg')
    with open(file_name, 'wb') as fout:
        shutil.copyfileobj(data, fout)


def open_folder(folder):
    subprocess.call(['open', folder])


if __name__ == '__main__':
    main()
