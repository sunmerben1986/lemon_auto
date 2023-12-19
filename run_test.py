# coding=utf-8
import unittest
import time
import os
from HTMLTestRunner import HTMLTestRunner


if __name__ == '__main__':
    now = time.strftime('%Y-%m-%d %H_%M_%S')
    Dir = os.path.abspath('./')
    nowDir = Dir.replace('\\', '/')
    filename = nowDir + '/report/' + 'lemon' + now + 'result.html'
    fp = open(filename, 'wb')
    runner = HTMLTestRunner(stream=fp, title='测试报告')
    discover = unittest.defaultTestLoader.discover(nowDir+'/test_case/module_event', pattern='module_event_restapi_test.py')
    runner.run(discover)
    fp.close()