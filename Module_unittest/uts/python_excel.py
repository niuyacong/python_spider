""" 
python操作excel

1、 xlrd主要是用来读取excel文件 pip install xlrd

2、防止覆盖的复制 xlutils   
"""


import xlrd
from xlutils.copy import copy

def xlrd_test():
    workbook = xlrd.open_workbook(u'1.xls')

    sheet_names= workbook.sheet_names()

    for sheet_name in sheet_names:
         sheet2 = workbook.sheet_by_name(sheet_name)
         rows=sheet2.row_values(3)[0]# 获取第四行第一个内容
         print (sheet_name)
         cols = sheet2.col_values(1) # 获取第二列内容
         print(rows)
         print(cols)
         print(sheet2.cell_value(0,0))# 获取第一行第一列

# 定义个封装操作excel的类
class OperateExcel:

    # 初始化
    def __init__(self,filename='../Module_unittest/uts/1.xls',sheet_id=0):
        self.filename=filename
        self.sheet_id=sheet_id
        self.data=self.get_data()
    
    # 获取所有的数据
    def get_data(self):
        workbook = xlrd.open_workbook(self.filename)
        data= workbook.sheets()[self.sheet_id]
        return data
    # 获取总行数
    def get_lines(self):
        return self.data.nrows

    # 获取第几行第几列的内容
    def get_cell_value(self,row=0,col=0):
        return self.data.cell_value(int(row),int(col))
    
    # 写入excel
    def write_value(self,rows,col,val):
        read_data=xlrd.open_workbook(self.filename)
        write_data=copy(read_data)
        sheet_data=write_data.get_sheet(0)
        sheet_data.write(int(rows),int(col),val)
        write_data.save(self.filename)

    # 根据id 找到行的内容
    def get_rows_data(self,case_id):
        line=self.get_rows_line(case_id)
        rows_data=self.get_rows_value(line)
        return rows_data

    # 根据id  找到行号
    def get_rows_line(self,rowid):
        num=0
        data=self.get_col_value()
        for line_data in data:
            if rowid== line_data:
                return num
            num=num+1

    # 根据行号，返回行数据
    def get_rows_value(self,row):
        return self.data.row_values(row)

    # 获取某一列的内容
    def get_col_value(self,col=0):
        return self.data.col_values(col)


if __name__=="__main__":
    oper=OperateExcel('2.xls',0)
    print(oper.get_lines())# 获取总行数    
    print(oper.get_cell_value())