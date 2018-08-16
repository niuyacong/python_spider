""" 
处理依赖数据的请求
"""
from uts.python_excel import OperateExcel
from uts.runmain import RunMethod
from uts.get_data import GetData
from  jsonpath_rw import jsonpath,parse
import json
class DependdentData:

    def __init__(self,case_id):
        self.opera_excel=OperateExcel()
        self.case_id=case_id
        self.data=GetData()
    # 根据case_id 返回整行内容
    def get_case_line_data(self):
        return self.opera_excel.get_rows_data(self.case_id)

    # 执行依赖测试  获取结果
    def run_dependent(self):
        run_method=RunMethod()
        rows=self.opera_excel.get_rows_line(self.case_id)
        url=self.data.get_url(rows)
        header=self.data.get_is_header(rows)
        data=self.data.get_json_data(rows)
        method=self.data.get_request_method(rows)
        return json.loads(run_method.run_method(method,url,data,header))

    # 返回依赖数据
    def get_data_for_key(self,rows):
        depend_data=self.data.get_case_field(rows)
        resonse_data=self.run_dependent()
        # 返回数据的层级关系  需要用到 pip  install jsonpath_rw
        json_exe=parse(depend_data) # 类似正则的规则定义
        madle=json_exe.find(resonse_data)
        return [math.value for math in madle][0]



       