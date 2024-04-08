import json
import os


class JSONProcessor:

    def __init__(self, directory):
        if not os.path.exists(directory):
            os.makedirs(directory)
        self._directory = directory

    def process(self, new_data, existing_file_name, new_file_name):
        # Load existing JSON data from file
        existing_file_path = os.path.join(self._directory, existing_file_name)
        new_file_path = os.path.join(self._directory, new_file_name)

        if os.path.exists(existing_file_path):
            with open(existing_file_path, 'r') as f:
                existing_data = json.loads(f.read())
        else:
            existing_data = []

        existing_data.append(json.loads(new_data))

        with open(new_file_path, 'w') as file:
            file.write(json.dumps(existing_data, indent=4))