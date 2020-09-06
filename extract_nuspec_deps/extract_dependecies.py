import re
import sys
import zipfile
from pathlib import Path
# import networkx as nx

pattern = '<dependency id="(.+)" />'
compiled_pattern = re.compile(pattern)


def get_dependencies(file_path, tally, indent_level=1):

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
                        tally[dependency] += 1
                    else:
                        tally[dependency] = 1
                        get_dependencies(package_path, tally, indent_level+1)


def main():
    file_path = Path(sys.argv[1])
    # filename = 'npr_code_enhet-0.0.0.6.1.0.3.nupkg'
    tally = {}
    get_dependencies(file_path, tally)
    for dep in sorted(tally, key=tally.get):
        print(dep,":", tally[dep])


if __name__ == '__main__':
    main()
