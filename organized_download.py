import os
import shutil

# Путь к папке загрузки
download_folder = 'C:/Users/user/Downloads/'

# Получение списка файлов в папке загрузки
files = os.listdir(download_folder)

# Создание словаря для хранения файлов по расширениям
file_extensions = {}

# Проход по всем файлам в папке загрузки
for file in files:

    # Определение расширения файла
    filename_parts = file.rsplit('.', 1)
    if len(filename_parts) > 1:
        file_extension = '.' + filename_parts[1].lower()
    else:
        file_extension = ''

    # Добавление файла в словарь
    if file_extension not in file_extensions:
        # Создание подпапки для расширения, если ее нет
        if not os.path.exists(download_folder + file_extension.lstrip('.')):
            os.mkdir(download_folder + file_extension[1:])
        file_extensions[file_extension] = [file]
    else:
        file_extensions[file_extension].append(file)

# Перемещение файлов в соответствующие подпапки
for extension, files in file_extensions.items():
    # Имя подпапки
    folder_name = download_folder + extension[1:]
    print(f"Moving {len(files)} files with extension '{extension}' to folder '{folder_name}' ")

    for file in files:
        # Исходный путь файла
        scr_path = download_folder + file

        # Путь для перемещения файла
        dest_path = folder_name + '/' + file

        #Перемещение файла
        try:
            shutil.move(scr_path, dest_path)
            print(f"Moved file '{file}' to folder '{folder_name}'")
        except Exception as e:
            print(f"Failed to move file '{file}' to folder '{folder_name}': {e}")
