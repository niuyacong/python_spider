""" 
操作json文件中的json数据
"""

import json


class json_data:
    def __init__(self,filename="../Module_unittest/uts/json.json"):
        self.filename=filename
        self.data=self.load_data()

    def load_data(self):
        with open(self.filename) as files:
            data=json.load(files)
            return data
    
    def get_value(self,keys):
        return self.data[keys]
    

if __name__=="__main__":
    j=json_data()
    print(j.get_value('login'))