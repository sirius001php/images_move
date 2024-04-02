import keyboard
import shutil

import os
import time

folder_path = "D:/Downloads"  # Замініть "your_folder_path" на шлях до вашої папки
parent_dir = "D:/Work3D/1CCM"
parent_dir2 = "D:/Work3D/2ZakExpress"
parent_dir3 = "D:/Work3D/others"


class Colors:
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    END = '\033[0m'
def get_last_added_file(folder_path):
    # Створюємо словник для зберігання інформації про файли та їх час останньої модифікації
    file_info = {}


    while True:
        # Переглядаємо вміст папки
        for root, dirs, files in os.walk(folder_path):
            for file_name in files:
                file_path = os.path.join(root, file_name)
                # Запам'ятовуємо час останньої модифікації
                file_info[file_path] = os.path.getmtime(file_path)


        # Знову переглядаємо папку та шукаємо останній доданий файл
        last_added_file = max(file_info, key=file_info.get)

        # Отримуємо інформацію про назву та тип останнього доданого файлу
        _, file_extension = os.path.splitext(last_added_file)
        file_type = file_extension[1:] if file_extension else "No extension"
        file_name = os.path.basename(last_added_file)

        print(f"Останній доданий файл: {file_name}, Тип: {file_type}")
        return file_name

class Q:
    name_remove = 'asd'
    def get_path(self):
        return self.name_remove

    def set_path(self, path):
        self.name_remove = path


class T:

    t = time.time()

    def get_time(self):
        return (time.time() - self.t) * 0.0166

    def set_time(self):
        self.t = time.time()

def resize_and_overlay(image_path):
    # Відкриваємо зображення
    original_image = Image.open(image_path)

    # Отримуємо розміри оригінального зображення
    width, height = original_image.size

    # Знаходимо максимальний розмір
    max_size = max(width, height)

    # Створюємо чорне зображення з квадратним розширенням
    black_image = Image.new("RGB", (max_size, max_size), color="black")

    # Обчислюємо положення оригінального зображення на чорному зображенні
    x_offset = (max_size - width) // 2
    y_offset = (max_size - height) // 2

    # Вставляємо оригінальне зображення на чорне зображення
    black_image.paste(original_image, (x_offset, y_offset))

    black_image.save(image_path)

def move_file(folder_path, parent_dir, q, t):
    try:
        file_name = get_last_added_file(folder_path)

        if file_name[0] == 'R' and file_name[1] == 'e':

            source_path = folder_path + '/' + file_name
            destination_path = parent_dir + '/' + q.get_path().split('.')[0]
            shutil.move(source_path, destination_path)
            print(f"Файл без фона переміщено до {destination_path}")
            os.replace(destination_path + '/' + file_name, destination_path + '/' + q.get_path().split('.')[0] + '(1).jpg')
        else:
            source_path = folder_path + '/' + file_name
            destination_path = parent_dir + '/' + file_name.split('.')[0]
            os.mkdir(destination_path)
            shutil.move(source_path, destination_path)
            resize_and_overlay(destination_path + '/' + file_name)

            print(Colors.GREEN + f"Час викон: {t.get_time():.2f} хвилин" + Colors.END)
            t.set_time()
            print(Colors.BLUE +f"Файл переміщено до {destination_path}" + Colors.END)

        q.set_path(file_name)
    except Exception as e:
        print(f"Помилка переміщення файлу.  Можливо вже є така папка. : {e}")

def assign_hotkey(hotkey, hotkey2, hotkey3, q, t):

    print(f"Очікування натискання хоткея {hotkey} для переміщення файлу.")
    keyboard.add_hotkey(hotkey, move_file, args=(folder_path, parent_dir, q, t), suppress=True)
    keyboard.add_hotkey(hotkey2, move_file, args=(folder_path, parent_dir2, q, t), suppress=True)
    keyboard.add_hotkey(hotkey3, move_file, args=(folder_path, parent_dir3, q, t), suppress=True)
    keyboard.wait()  # Очікуємо на натискання клавіші Esc для завершення програми

from PIL import Image, ImageOps



if __name__ == "__main__":
    t = T()
    q = Q()
    hotkey = "F1"  # Замініть на бажаний хоткей
    hotkey2 = "F2"  # Замініть на бажаний хоткей
    hotkey3 = "F3"  # Замініть на бажаний хоткей

    assign_hotkey(hotkey, hotkey2, hotkey3, q, t)


