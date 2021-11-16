import os
import json
import glob
import shutil


def load_setting():
    with open("settings.json", "r") as settings:
        return dict(json.load(settings))


class FilePathController:
    current_path = ""
    path = ""

    def start(self):
        while True:
            try:
                s = input(self.current_path + "/ ")
                if s == "exit":
                    break
                elif s.find("ls") != -1:
                    self._ls(" ".join(s.split(" ")[1:]))
                elif s.find("cd") != -1:
                    self._cd(s.split(" ")[1])
                elif s.find("rm") != -1:
                    self._delete(s.split(" ")[1])
                elif s.find("cr") != -1:
                    self._create(s.split(" ")[1], " ".join(s.split(" ")[2:]))
                elif s.find("cat") != -1:
                    self._show(s.split(" ")[1])
                elif s.find("nano") != -1:
                    self._nano(s.split(" ")[1], " ".join(s.split(" ")[2:]))
                elif s.find("rename") != -1:
                    s = s.split(" ")
                    self._rename(s[1], s[2])
                elif s.find("cp") != -1:
                    s = s.split(" ")
                    self._copy(s[1], s[2])
                elif s.find("mv") != -1:
                    s = s.split(" ")
                    self._move(s[1], s[2])
                else:
                    print(
                        "Неверная команда, список доступных команд:\n\n"
                        "ls - содержимое папки. Параметры: фильтры в виде regex\n"
                        "cd - перейти в каталог. Параметры: относительный путь или \"..\" для перехода "
                        "на каталог выше\n"
                        "rm - удалить папку/файл. Параметры: относительный путь\n"
                        "cr - создать папку/файл. Параметры: относительный путь\n"
                        "cat - просмотр содержимого файла. Параметры: относительный путь файла\n"
                        "nano - запись в файл. Параметры: относительный путь, строка для записи\n"
                        "rename - переименование папки/файла. Параметры: относительный путь, новое название\n"
                        "cp - копирование папки/файла. Параметры: относительный путь, место назначения\n"
                        "mv - перемещение папки/файла. Параметры: относительный путь, место назначения\n"
                    )
            except IndexError:
                print("Неверные параметры")
                continue
            except PermissionError:
                print("У меня нет разрешения на выполнение этого действия")
                continue

    def __init__(self):
        self.path = load_setting()["path"]
        self.current_path = self.path

    def _ls(self, filters=""):
        full_path = self.current_path
        if filters != "":
            if len(filters.split(" ")) > 1:
                self._ls(" ".join(filters.split(" ")[:-1]))
            full_path = os.path.join(full_path, filters.split(" ")[-1])
            for filename in glob.glob(full_path):
                self._getpath(os.path.basename(os.path.normpath(filename)))
        else:
            for filename in os.listdir(full_path):
                self._getpath(filename)

    def _getpath(self, filename):
        if os.path.isfile(os.path.join(self.current_path, filename)):
            print("Файл: " + filename)
        else:
            print("Папка: " + filename)

    def _cd(self, path):
        if path == "..":  # check do is up
            paths = os.path.split(self.current_path)
            self._cd_up(paths[0])  # move current_path to up dir
            return
        full_path = os.path.join(self.current_path, path)  # concatenate current_path and arg path
        if os.path.exists(full_path):  # check dir is exists
            self.current_path = full_path
        else:
            print("Папка не существует")

    def _cd_up(self, path):
        if path != os.path.split(self.path)[0]:  # check dir is not root
            self.current_path = path
        else:
            print("Вы не можете выйти за пределы корневого каталога")

    def _create(self, name, contents=""):
        full_path = os.path.join(self.current_path, name)  # concatenate current_path and arg name
        if not os.path.exists(full_path):  # check file is exists
            if name.find(".") == -1:  # check is file or not
                os.mkdir(full_path)  # create dir
            else:
                with open(full_path, "w") as file:   # create file
                    file.write(contents)  # write arg contents in file
        else:
            print("Файл/Папка уже существует")

    def _show(self, name):
        full_path = os.path.join(self.current_path, name)  # concatenate current_path and arg name
        if os.path.exists(full_path):  # check file is exists
            if os.path.isfile(full_path):  # check is file or not
                with open(full_path, "r") as file:  # read file
                    print(file.read())
            else:
                self._ls()
        else:
            print("Файл не существует")

    def _nano(self, name, contents=""):
        full_path = os.path.join(self.current_path, name)  # concatenate current_path and arg name
        if os.path.exists(full_path):  # check file is exists
            if os.path.isfile(full_path):  # check is file or not
                with open(full_path, "a+") as file:  # create file
                    file.write(contents)  # write arg contents in file
            else:
                print("Нельзя производить запись в директорию")
        else:
            print("Файл не существует")

    def _rename(self, name, new_name):
        full_path = os.path.join(self.current_path, name)  # concatenate current_path and arg name
        if os.path.exists(full_path):  # check file is exists
            os.rename(full_path, os.path.join(self.current_path, new_name))  # rename file
        else:
            print("Файл не существует")

    def _copy(self, name, to):
        full_path = os.path.join(self.current_path, name)  # concatenate current_path and arg name
        if os.path.exists(full_path):  # check file is exists
            shutil.copy(full_path, os.path.join(self.current_path, to))  # copy file
        else:
            print("Файл не существует")

    def _move(self, name, to):
        full_path = os.path.join(self.current_path, name)  # concatenate current_path and arg name
        if os.path.exists(full_path):  # check file is exists
            shutil.move(full_path, os.path.join(self.current_path, to))  # move file
        else:
            print("Файл не существует")

    def _delete(self, name):
        full_path = os.path.join(self.current_path, name)  # concatenate current_path and arg name
        if os.path.exists(full_path):   # check file is exists
            if str(name).find(".") == -1:  # check is file or not
                shutil.rmtree(full_path)  # remove dir
            else:
                os.remove(full_path)  # remove file
        else:
            print("Файл/Папка не существует")


if __name__ == '__main__':
    file_controller = FilePathController()
    file_controller.start()
