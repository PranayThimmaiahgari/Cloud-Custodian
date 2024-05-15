import yaml
import json
def yaml_to_json(yaml_file_path):
    with open(yaml_file_path, 'r') as f:
        yaml_content = yaml.safe_load(f)
        json_content = json.dumps(yaml_content, indent=4)
        return json_content

# Example usage
yaml_file_path = 'S3_30days.yml'
json_content = yaml_to_json(yaml_file_path)
print(json_content)
with open('policy-new.json', 'w') as file:
    file.write(json_content)