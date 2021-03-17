import unittest
from paths import envPath, logPath
from dotenv import load_dotenv
load_dotenv()

# OR, the same with increased verbosity
load_dotenv(verbose=True)

load_dotenv(dotenv_path=envPath)

from minioWrapper import MinioWrapper
from utils import ridToCenterTimestamp, initLogger, myPrint
initLogger(logPath)


class MyTestCase(unittest.TestCase):

    def test_listBuckets(self):
        print("OKay")
        m = MinioWrapper()
        myPrint(m.listBuckets())
