
import os
import time


directory = 'C:/Users/user/Desktop/Python/os/hw65.py'  


for dirpath, dirnames, filenames in os.walk(directory):
    for filename in filenames:
        full_path = os.path.join(dirpath, filename)
        mtime = os.path.getmtime(full_path)
        last_modified_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(mtime))
        size = os.path.getsize(full_path)
        parent_directory = os.path.dirname(full_path)
        print(f"Файл: {filename}")
        print(f"Полный путь: {full_path}")
        print(f"Время последнего изменения: {last_modified_time}")
        print(f"Размер файла: {size} байт")
        print(f"Родительская директория: {parent_directory}")
        print('-' * 40)
