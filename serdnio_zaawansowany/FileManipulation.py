class FileManipulation:

    def __init__(self, file_name) -> None:
        self.__file_name = file_name

    def add_line(self, message) -> None:
        with open(self.__file_name, 'a') as file:
            file.write(message)
            file.close()

    def get_lines_count(self) -> int:
        with open(self.__file_name, 'r') as file:
            nr_of_lines = sum(1 for line in file)
            file.close()
            return nr_of_lines

    def get_last_line(self) -> str:
        with open(self.__file_name, 'r') as file:
            lines = file.read().splitlines()
            last_line = lines[-1]
            return last_line
