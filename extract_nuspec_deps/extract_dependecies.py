import re
import sys
import zipfile
from pathlib import Path
import networkx as nx
from matplotlib import pyplot as plt

from bokeh.io import output_file, show
from bokeh.models import (BoxSelectTool, BoxZoomTool, Circle, HoverTool,
                        MultiLine, NodesAndLinkedEdges, Plot, Range1d, TapTool,
                        ResetTool, WheelZoomTool, PanTool)
from bokeh.palettes import Spectral4
from bokeh.plotting import from_networkx

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
                    dependency = match.group(1).lower()
                    package_path = list(
                        dir_path.glob(dependency + '*.nupkg')).pop()
                    if package_path.name in G:
                        G.add_edge(file_path.name, package_path.name)
                    else:
                        G.add_edge(file_path.name, package_path.name)
                        get_dependencies(package_path, G)


def bokeh_plot(G, package, output_file_name, layout=nx.spectral_layout):
    plot = Plot(plot_width=1500, plot_height=1000,
                x_range=Range1d(-1.1,1.1), y_range=Range1d(-1.1,1.1))
    plot.title.text = f'Dependency network for {package.name[:-6]}'

    node_hover_tool = HoverTool(tooltips=[("index", "@index")])
    plot.add_tools(node_hover_tool, TapTool(), BoxSelectTool(), BoxZoomTool(), ResetTool(), WheelZoomTool(), PanTool())

    graph_renderer = from_networkx(G, layout, scale=1, center=(0,0))

    graph_renderer.node_renderer.glyph = Circle(size=15, fill_color=Spectral4[0])
    graph_renderer.node_renderer.selection_glyph = Circle(size=15, fill_color=Spectral4[2])
    graph_renderer.node_renderer.hover_glyph = Circle(size=15, fill_color=Spectral4[1])

    graph_renderer.edge_renderer.glyph = MultiLine(line_color="#CCCCCC", line_alpha=0.8, line_width=5)
    graph_renderer.edge_renderer.selection_glyph = MultiLine(line_color=Spectral4[2], line_width=5)
    graph_renderer.edge_renderer.hover_glyph = MultiLine(line_color=Spectral4[1], line_width=5)

    graph_renderer.selection_policy = NodesAndLinkedEdges()

    plot.renderers.append(graph_renderer)

    output_file(output_file_name)
    show(plot)


def format_centrality(G):
    centrality_list = []
    sorted_degrees = sorted(G.degree, key=lambda item: item[1], reverse=True)
    for dep, degree in sorted_degrees:
        centrality_list.append(f'{dep:<60} : {degree}')
    return centrality_list


def print_centrality(centrality_list, package_name):
    print()
    print(f'Dependencies for {package_name}'.upper())
    print('\nTop 10 dependencies: ')
    for centrality in centrality_list[:10]:
        print(centrality)
    print()


def store_centrality(centrality_list, file_name):
    with open(file_name, 'w') as file:
        for centrality in centrality_list:
            file.write(centrality + '\n')


def make_dirs(dir_list):
    p = Path('.')
    for dir_name in dir_list:
        p.joinpath(dir_name).mkdir(exist_ok=True)


def main():
    # filename = 'npr_code_enhet-0.0.0.6.1.0.3.nupkg'
    dir_list = ['figures', 'centrality']
    make_dirs(dir_list)
    file_path = Path(sys.argv[1])
    package_name = file_path.name[:-6]
    G = nx.DiGraph()
    get_dependencies(file_path, G)
    centrality_list = format_centrality(G)
    store_centrality(centrality_list, Path('centrality') / (package_name+'.txt'))
    print_centrality(centrality_list, package_name)
    print(f'\n{"Packages":<60} : {len(G.nodes)}')
    print(f'{"Dependencies":<60} : {len(G.edges)}')
    print(f'{"Cycles":60} : {len(list(nx.simple_cycles(G)))}')


    bokeh_plot(G, file_path, f"figures/{package_name}_circular_.html", nx.circular_layout)
    bokeh_plot(G, file_path, f"figures/{package_name}_spring.html", nx.spring_layout)
    bokeh_plot(G, file_path, f"figures/{package_name}_spectral.html", nx.spectral_layout)


if __name__ == '__main__':
    main()
