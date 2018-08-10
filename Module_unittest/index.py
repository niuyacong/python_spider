""" 
unittest使用
中文文档地址
http://pythonguidecn.readthedocs.io/zh/latest/writing/tests.html


HTMLTestRunner的使用
下载，HTMLTestRunner.py 放到安装目录的Lib的路径下
HTMLTestRunner.py 为python2+版本
修复可参考：
https://www.cnblogs.com/camilla/p/7243044.html



安装mock
pip install mock
"""
import unittest
import HTMLTestRunner
import mock

class Test(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print('此为类方法，只会在类开始前执行一次')

    @classmethod
    def tearDownClass(cls):
        print('此为类方法，只在类所有方法调用结束之后执行一次')

    def setUp(self):
        print('类中每个测试方法开始前都会执行')

    def tearDown(self):
        print('类中每个测试方法结束后都会执行')
    

    # 跳过这个case执行
    @unittest.skip('test_test') # 此时此case将不再执行
    def test_test(self):
        # 定义全局变量，使用globals()['userid']=123 
        # 但是每个testcase有执行顺序 按照名称顺序  在先执行的case中定义全局变量  在后面的case中才能获取到
        # 定义顺序有误，会抛出没有定义的异常
        globals()['userid']=123
        
        self.assertEqual(True,True,'值不相同')
        self.assertFalse(0,'值不为false')
        self.assertTrue(True,'此为false')
        print('每个测试用例都必须以test开头')
        

    def test_wne(self):
        # print(userid)
        print('仅以测试setup、teardown')

        # mock模拟接口返回值
        mock_data=mock.Mock(return_value={'data':'haha'})
        print(mock_data)
        # <Mock id='49657784'>

if __name__=="__main__":

    # 生成测试报告
    filepath="htmlreport.html"
    fp=open(filepath,'wb')
    # unittest.main()

    # 等同于
    suite=unittest.TestSuite()
    suite.addTest(Test('test_wne'))
    suite.addTest(Test('test_test'))
    unittest.TextTestRunner().run(suite)

    # htmltestrunner 应用
    # runner=HTMLTestRunner.HTMLTestRunner(stream=fp,title="this is a first report")
    # runner.run(suite)