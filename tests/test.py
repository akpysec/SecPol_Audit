import os

path = ""
path_to_files = []

if len(path) >= 2:
    path_to_files.append(path)

    # Iterate over .csv files in a path
    files = [x for x in os.listdir(path=path_to_files[0]) if x.lower().endswith(".inf")]
    for file in files:
        print(path_to_files[0] + file)
