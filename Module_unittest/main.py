""" 
主程序
"""
import sys
sys.path.append("F:\my\python_spider\Module_unittest")

from uts.runmain import RunMethod
from uts.get_data import GetData
from uts.common_utils import CommonUtils
class RunTest:
    def __init__(self):
        self.run_method=RunMethod()
        self.data=GetData()
        self.utils=CommonUtils()
    def go_on_run(self):
        res=None
        rows_count=self.data.get_case_lines()
        for i in range(1,rows_count):
            url=self.data.get_url(i)
            method=self.data.get_request_method(i)
            is_run=self.data.get_url(i)
            data=self.data.get_json_data(i)
            header=self.data.get_is_header(i)
            expect_data=self.data.get_expect_data(i)
            if is_run:
                res=self.run_method.run_method(url=url,data=data,header=header,method=method)
                print(expect_data)
                print(res)
                if self.utils.is_contains(expect_data,res):
                    print('测试成功')
                else:
                    print('测试失败')
            return res
    


if __name__=="__main__":
    run=RunTest()
    print(run.go_on_run())
