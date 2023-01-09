from pathlib import Path
import os
PACKAGE_ROOT = str(Path(__package__).absolute())
def readfile(path:str) -> str:
    with open(path) as f:
        ret = f.read()
    return ret

def generate_html_pyecharts(chart, file_name) -> str:
    if chart.render is None:
        raise RuntimeError('Please pass a PyEchart chart object!')

    path = f'./templates/{file_name}'
    chart.render(path)
    html = readfile(path).replace('<body>','<center><body>').replace('</body>','</body></center>')
    os.remove(path)
    return html
