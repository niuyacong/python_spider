""" 
获取数据
"""

import uts.python_excel as python_excel

import uts.data_config as data_config

import  uts.operate_json  as operate_json
class GetData:
    def __init__(self):
        self.exec_excel=python_excel.OperateExcel()
    
    def get_data(self):
        return self.exec_excel.get_data()
    
    def get_case_lines(self):
        return self.exec_excel.get_lines()

    def get_is_run(self,rows):
        col=data_config.get_run()
        row=self.exec_excel.get_cell_value(rows,col)
        return row=="yes"
    
    def get_is_header(self,rows):
        col=data_config.get_header()
        header=self.exec_excel.get_cell_value(rows,col)
        if header=="yes":
            return data_config.get_header_val()
        else:
            return None
    def get_request_method(self,rows):
        col=data_config.get_request_way()
        method=self.exec_excel.get_cell_value(rows,int(col))
        return method

    def get_url(self,rows):
        col=int(data_config.get_url())
        url=self.exec_excel.get_cell_value(rows,col)
        return url

    def get_request_data(self,rows):
        col=int(data_config.get_request_data())
        request_data=self.exec_excel.get_cell_value(rows,col)
        if request_data =='':
            return None
        return request_data

    def get_json_data(self,rows):
        oper=operate_json.json_data()
        data=oper.get_value(self.get_request_data(rows))
        return data

    def get_expect_data(self,rows):
        col=data_config.get_expect()
        expect_data=self.exec_excel.get_cell_value(rows,col)
        if expect_data =='':
            return None
        return expect_data