
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
