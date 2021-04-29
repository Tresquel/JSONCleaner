import json
import sys
from os.path import exists, isdir, join
from os import listdir

# Determine if it's or not a directory
def isDirectory(path):
    if (isdir(path)):
        return True
    return False

# Make the JSON file pretty
def FormatJSONFile(PathToJSONFile):
    JSONfile = json.load(open(PathToJSONFile, "r"))
    with open(PathToJSONFile, 'w') as f:
        f.write(json.dumps(JSONfile, indent=4 * ' '))
    print("Formatted %s" % (PathToJSONFile))

# Decide what to do to format the json
def formatJson(path):
    # Determine if it's directory
    is_directory=isDirectory(path)
    #
    if (is_directory):
        elements=listdir(path)
        for file in (elements):
            file_path=join(path, file)
            if (isDirectory(file_path)):
                formatJson(file_path)
            else:
                FormatJSONFile(file_path)
    else:
        FormatJSONFile(path)

# Decide what to do to deformat the json
def deformatJson(path):
    # Determine if it's directory
    is_directory=isDirectory(path)
    #
    if (is_directory):
        elements=listdir(path)
        for file in (elements):
            file_path=join(path, file)
            if (isDirectory(file_path)):
                deformatJson(file_path)
            else:
                DeFormatJSONFile(file_path)
    else:
        DeFormatJSONFile(path)

# De-Pretty the JSON file
def DeFormatJSONFile(PathToJSONFile):
    JSONfile = json.load(open(PathToJSONFile, "r"))
    with open(PathToJSONFile, 'w') as f:            
        f.write(json.dumps(JSONfile, indent=None))
    print("De-Formatted %s" % (PathToJSONFile))


if __name__ == "__main__":
    try:
        operation=str(sys.argv[1])
        path=str(sys.argv[2])
        if (not path or not exists(path)):
            raise EOFError
        if operation == "-d":
            deformatJson(path)
        elif operation == "-f":
            formatJson(path)
        else:
            raise IndexError
    except:
        print("Invalid usage!\n\nUsage: 'JSONCleaner.py -f/-d PathToJSONFile'\n'-f' is for formatting the file and '-d' is for de-formatting the file.")
