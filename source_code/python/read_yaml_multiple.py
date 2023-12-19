import yaml
import sys

def check_file_supplied():
    """
    Function to check if the argument is supplied i.e. the filename is provided.
    """
    if len(sys.argv) != 2:
        raise ValueError('Please provide YAML file as an argument')
    yaml_file = sys.argv[1]
    return yaml_file


def print_yaml_file_contents(yaml_file):
    """
    Function to print YAML file contents
    """
    with open(yaml_file , 'r') as file:
        yaml_file_content = yaml.safe_load_all(file)
    
    # Iterate through all the documents
    
    for doc in yaml_file_content:
        for key, values in doc.items():
            print(f'{key} ==> {values} ==> {type(values)} ')



if __name__=="__main__":
    """Calling the functions"""
    yaml_file = check_file_supplied()
    print_yaml_file_contents(yaml_file)

    