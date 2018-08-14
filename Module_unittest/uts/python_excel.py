""" 
python操作excel

1、 xlrd主要是用来读取excel文件 pip install xlrd

"""


import xlrd
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
    

if __name__=="__main__":
    oper=OperateExcel('2.xls',0)
    print(oper.get_lines())# 获取总行数    
    print(oper.get_cell_value())