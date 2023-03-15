from datetime import datetime
import argparse, pathlib, json, os
import module, report

parser = argparse.ArgumentParser()
parser.add_argument("--test-suite-path", help="This use if you have spesific Test Suite to be tested", default="testsuites")
args = parser.parse_args()

def get_total(list_file):
    for i in list_file:
        data = json.load(open(i, 'r'))
        for j in data:
            module.count("testcases/"+j, report.statistic)

def start():
    list_file = []
    path = pathlib.Path(args.test_suite_path)
    if not path.exists():
        raise Exception("FileNotFoundError: "+args.test_suite_path)
    if os.path.isdir(args.test_suite_path):
        
        list_file = list(path.iterdir())
    else:
        list_file.append(args.test_suite_path)
    get_total(list_file)
    for i in list_file:
        rep = {"name": str(i), "testcases": [], "start": datetime.now(), "end": None, "elapsed": None}
        data = json.load(open(i, 'r'))
        for j in data:
            module.loadModule("testcases/"+j, rep)
        rep["end"] = datetime.now()
        rep["elapsed"] = rep["end"] - rep["start"]
        report.reports.append(rep)
    with open('reports/reports.json', 'w') as f:
        json.dump(report.reports, f, indent=4, default=str)

if __name__ == '__main__':
    start()
