import argparse
import sys
import traceback

from paths import envPath, logPath
from dotenv import load_dotenv

load_dotenv()

# OR, the same with increased verbosity
load_dotenv(verbose=True)

load_dotenv(dotenv_path=envPath)

from actions.table_migration import TableMigration
from utils import initLogger, myPrint, getTimeInSec, timeDiff
import config as conf


def args_parse():
    parser = argparse.ArgumentParser()
    parser.add_argument('action', help='get_vids|fetch_info|reprint|all')
    args = parser.parse_args()
    return args, parser


def main():
    args, parser = args_parse()
    initLogger(logPath)
    start_time = getTimeInSec()

    try:
        prev_time = start_time
        if args.action == 'migrate' or args.action == 'all':
            myPrint("Action: migrate", 1)
            TableMigration().run()
            prev_time, prstr = timeDiff(prev_time)
            myPrint("Time taken by Action migrate: " + prstr, 11)
    except:
        prev_time, prstr = timeDiff(start_time)
        myPrint("Total time taken by the script: " + prstr, 11)
        formatted_lines = traceback.format_exc()
        myPrint(formatted_lines, 13)
        sys.exit(1)
    prev_time, prstr = timeDiff(start_time)
    myPrint("Total time taken by the script: " + prstr, 11)
    return sys.exit(0)


if __name__ == "__main__":
    main()
