import os


def find_files_only_in_first_folder(folder1, folder2):
    # Get a list of all base file names in the first folder
    files_in_folder1 = {os.path.splitext(file)[0] for file in os.listdir(folder1)}

    # Get a list of all base file names in the second folder
    files_in_folder2 = {os.path.splitext(file)[0] for file in os.listdir(folder2)}

    # Find base file names that are in the first folder but not in the second folder
    files_only_in_folder1 = files_in_folder1 - files_in_folder2

    return files_only_in_folder1


if __name__ == "__main__":
    folder1 = "data/box_downloads"
    folder2 = "data/peak_normalized_box_downloads"

    if os.path.exists(folder1) and os.path.exists(folder2):
        files_only_in_folder1 = find_files_only_in_first_folder(folder1, folder2)

        if files_only_in_folder1:
            print("Files found only in the first folder:")
            for file in files_only_in_folder1:
                print(file)
        else:
            print("No files found only in the first folder.")
    else:
        print("One or both folders do not exist.")
