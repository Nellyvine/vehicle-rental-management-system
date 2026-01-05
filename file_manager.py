
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

    def update_file(self, record_id, updated_data):
        try:
            lines = self.read_from_file()
            record_found = False

            for i in range(len(lines)):
                if lines[i].startswith(record_id + '|'):
                    lines[i] = updated_data
                    record_found = True
                    break

            if record_found:
                with open(self.fileName, 'w') as file:
                    for line in lines:
                        file.write(line + '\n')
                return True
            else:
                print(f"Record with ID {record_id} not found")
                return False

        except IOError as e:
            print(f"Error updating file: {e}")
            return False
