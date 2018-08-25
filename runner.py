import json
from datetime import datetime, timedelta
from subprocess import Popen, PIPE

CMD = '--source=ohlcv --from=2018-08-23 --proxy_type=rotate --period=1HRS --filetype=csv --timeout=20'


def run(command):
    print(command)
    process = Popen(command, stdout=PIPE, shell=True)
    while True:
        line = process.stdout.readline().rstrip()
        if not line:
            continue
        elif 'DONE' in str(line):
            break
        yield line


if __name__ == "__main__":
    start_exec = datetime.now()
    symbol_ids = []
    with open("symbol_ids.json", "r") as f:
        symbol_ids = json.load(f)

    print('symbols: ', symbol_ids)

    while len(symbol_ids) > 0:
        for path in run('python run.py --symbol=' + symbol_ids[0] + ' ' + CMD):
            print(path)

        with open("symbol_ids.json", "w") as f:
            symbol_ids.pop(0)
            json.dump(symbol_ids, f)

    print('DONE, Took: ', timedelta(seconds=(datetime.now() - start_exec).total_seconds()))
