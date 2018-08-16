""" 
主程序
"""
import sys
sys.path.append("F:\my\python_spider\Module_unittest")
from  jsonpath_rw import jsonpath,parse
from uts.runmain import RunMethod
from uts.get_data import GetData
from uts.common_utils import CommonUtils
from uts.depended_data import DependdentData
from uts.send_email import SendMail
class RunTest:
    def __init__(self):
        self.run_method=RunMethod()
        self.data=GetData()
        self.utils=CommonUtils()
    def go_on_run(self):
        res=None
        pass_count=[]
        fail_count=[]
        rows_count=self.data.get_case_lines()
        for i in range(1,rows_count):
            url=self.data.get_url(i)
            method=self.data.get_request_method(i)
            is_run=self.data.get_url(i)
            data=self.data.get_json_data(i)
            header=self.data.get_is_header(i)
            expect_data=self.data.get_expect_data(i)
            caseid=self.data.get_case_id(i)
            case_field=self.data.get_case_data(i)
            if is_run:
                if caseid:
                    depent=self.dependent=DependdentData(caseid)
                    depent_data=depent.get_data_for_key(i)
                    data[case_field]=depent_data
                res=self.run_method.run_method(url=url,data=data,header=header,method=method)
                print(res)
                if self.utils.is_contains(expect_data,res):
                    self.data.insert_data(i,'测试成功')
                    pass_count.append(i)
                    print('测试成功')
                else:
                    self.data.insert_data(i,'测试失败')
                    fail_count.append(i)
                    print('测试失败')
            # return res
            mail=SendMail()
            mail.send_main(pass_count,fail_count)

            print(pass_count)
            print(fail_count)
    


if __name__=="__main__":
    run=RunTest()
    run.go_on_run()

# if __name__=="__main__":
#         depend_data="data[0].username"
#         resonse_data={'data': [{'username': 'nyc123'}]}
#         # 返回数据的层级关系  需要用到 pip  install jsonpath_rw
#         json_exe=parse(depend_data) # 类似正则的规则定义
#         madle=json_exe.find(resonse_data)
#         print([math.value for math in madle][0])
