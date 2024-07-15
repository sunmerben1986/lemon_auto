# coding=utf-8
import unittest
import time
import os
from HTMLTestRunner import HTMLTestRunner


if __name__ == '__main__':
    now = time.strftime('%Y-%m-%d %H_%M_%S')
    Dir = os.path.abspath('./')
    nowDir = Dir.replace('\\', '/')
    filename = nowDir + '/lemon_auto/report/' + 'lemon' + now + 'result.html'
    fp = open(filename, 'wb')
    runner = HTMLTestRunner(stream=fp, title='测试报告')
    discover = unittest.defaultTestLoader.discover(nowDir+'/lemon_auto/test_case/module_event', pattern='module_*')
    runner.run(discover)
    fp.close()