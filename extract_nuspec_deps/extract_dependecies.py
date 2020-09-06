import re
import sys
import zipfile
from pathlib import Path
import networkx as nx
from matplotlib import pyplot as plt

pattern = '<dependency id="(.+)" />'
compiled_pattern = re.compile(pattern)


def get_dependencies(file_path, G):

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
                    package_path = list(
                        dir_path.glob(dependency + '*.nupkg')).pop()
                    if package_path.name in G:
                        G.add_edge(file_path.name, package_path.name)
                    else:
                        G.add_edge(file_path.name, package_path.name)
                        get_dependencies(package_path, G)


def main():
    file_path = Path(sys.argv[1])
    # filename = 'npr_code_enhet-0.0.0.6.1.0.3.nupkg'
    G = nx.Graph()
    get_dependencies(file_path, G)
    for dep, degree in sorted(G.degree, key=lambda item: item[1])[-10:]:
        print(dep, degree)
    print('Packages:     ', len(G.nodes))
    print('Dependencies: ', len(G.edges))

    plt.figure()
    nx.draw_circular(G)
    plt.savefig("circular.png")
    plt.show()

    plt.figure()
    nx.draw_spring(G)
    plt.savefig("spring.png")
    plt.show()

    plt.figure()
    nx.draw_spectral(G)
    plt.savefig("spectral.png")
    plt.show()


if __name__ == '__main__':
    main()
