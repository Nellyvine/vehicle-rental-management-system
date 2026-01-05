
import os


class FileManager:
    def __init__(self, file_name):
        self.fileName = file_name

        # Create file if it does not exist
        if not os.path.exists(file_name):
            try:
                with open(file_name, 'w'):
                    pass
            except IOError as e:
                print(f"Error creating file {file_name}: {e}")

    def write_to_file(self, data):

        try:
            with open(self.fileName, 'a') as file:

                file.write(data + '\n')
            return True
        except IOError as e:
            print(f"Error writing to file: {e}")
            return False

    def read_from_file(self):
        try:
            with open(self.fileName, 'r') as file:
                lines = file.readlines()
            return [line.strip() for line in lines if line.strip()]

        except FileNotFoundError:

            print(f"File {self.fileName} not found")
            return []
        except IOError as e:
            print(f"Error reading file: {e}")
            return []
