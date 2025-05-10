import sys

def file_extensions(filename):
    no_extension = []
    extensions = {}

    with open(filename, 'r') as f:
        for line in f:
            file = line.strip()
            if '.' not in file or file.endswith('.'):
                no_extension.append(file)
            else:
                parts = file.split('.')
                ext = parts[-1]
                if ext not in extensions:
                    extensions[ext] = []
                extensions[ext].append(file)

    return no_extension, extensions

def main():
    no_ext_files, ext_dict = file_extensions("./src/filenames.txt")

    print(f"{len(no_ext_files)} files with no extension")
    
    for ext in sorted(ext_dict):
        print(f"{ext} {len(ext_dict[ext])}")

if __name__ == "__main__":
    main()
