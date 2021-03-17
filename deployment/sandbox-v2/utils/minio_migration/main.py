import argparse
import hashlib
import json
import sys
import traceback

from minioWrapper import MinioWrapper
from paths import envPath, logPath
from dotenv import load_dotenv
load_dotenv()

# OR, the same with increased verbosity
load_dotenv(verbose=True)

load_dotenv(dotenv_path=envPath)

from utils import initLogger, myPrint, writeJsonFile, getJsonFile, ridToCenterTimestamp, getTimeInSec, timeDiff
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
    myPrint(conf.minio_endpoint)
    try:
        prev_time = start_time
        if args.action == 'get_packets' or args.action == 'all':
            myPrint("Action: get_vids", 1)
            m = MinioWrapper()
            myPrint(m.listBuckets())
            prev_time, prstr = timeDiff(prev_time)
            myPrint("Time taken by Action get_vids: " + prstr, 11)
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
