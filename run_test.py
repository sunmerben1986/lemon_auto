# coding=utf-8
import unittest
import time
import os
from HTMLTestRunner import HTMLTestRunner


if __name__ == '__main__':
    now = time.strftime('%Y-%m-%d %H_%M_%S')
    Dir = os.path.abspath('./')
    print(Dir)
    nowDir = Dir.replace('\\', '/')
    print(nowDir)
    filename = nowDir + '/report/' + 'lemon' + now + 'result.html'
    print(filename)

    # fp = open(filename, 'wb')
    # runner = HTMLTestRunner(stream=fp, title='测试报告')
    # discover = unittest.defaultTestLoader.discover(nowDir+'/test_case', pattern='*_test_pre.py')
    # runner.run(discover)
    # fp.close()
