import re
import sys
import zipfile
import collections
from pathlib import Path
from pprint import pprint


def get_dependencies(file_path, tally, indent_level=1):
    print(str(file_path))
    pattern = '<dependency id="(.+)" />'
    compiled_pattern = re.compile(pattern)
    dir_path = file_path.parent

    with zipfile.ZipFile(file_path, 'r') as zip_obj:
        nuspec_file_path = None

        for zip_file_path in zip_obj.namelist():
            if '.nuspec' in zip_file_path:
                nuspec_file_path = zip_file_path

        with zip_obj.open(nuspec_file_path) as file:
            for line in file:
                decoded_line = line.decode('cp1252').strip()
                match = compiled_pattern.match(decoded_line)
                if match:
                    dependency = match.group(1)
                    package_path = list(dir_path.glob(dependency + '*.nupkg')).pop()
                    if dependency in tally:
                        tally.append(dependency)
                    else:
                        tally.append(dependency)
                        print(indent_level * '\t' + get_dependencies(package_path, tally, indent_level+1))
#                    print(indent_level * '\t' + str(package_path))
#                    for dep in get_dependencies(package_path, indent_level+1):
#                        print(dep)
#    input("Kjør: ")
    return str(file_path)


def main():
    file_path = Path(sys.argv[1])
    # filename = 'npr_code_enhet-0.0.0.6.1.0.3.nupkg'
    tally = []
    dependencies = list(get_dependencies(file_path, tally))
    pprint(collections.Counter(tally))


if __name__ == '__main__':
    main()
