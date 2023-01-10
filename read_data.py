import json


def fromJson(file_path: str)->dict:
    """
    This function will read the json file and return the data as a dictionary.
    
    Parameters:
        file_path (str): Path of the file to be read
    Returns:
        dict: Dictionary containing the data of the json file.
    
    """
    return data
f = open('data/result.json', 'r', encoding='UTF8').read()
data = json.loads(f)
print(fromJson(data))