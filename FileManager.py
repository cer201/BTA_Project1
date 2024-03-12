import json

class FileManager:
    def load_data(self, filename):
        with open(filename, 'r') as file:
            return file.read()

    def save_data(self, filename, data):
        with open(filename, 'w') as file:
            file.write(data)

    def read_json(self, json_file_path):
        try:
            with open(json_file_path, 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            print(f"File {json_file_path} not found.")
            return []
        except json.JSONDecodeError as e:
            print(f"Error decoding JSON from file {json_file_path}: {e}")
            return []
        
    def write_json(self, data, json_file_path):
        with open(json_file_path, 'w') as file:
            json.dump(data, file)
    
    def add_to_json(self, data, json_file_path):
        current_data = self.read_json(json_file_path)
        current_data.append(data)
        self.write_json(current_data, json_file_path)
