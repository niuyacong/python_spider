class CommonUtils:
    def is_contains(self,str1,str2):
        return str1 in str2



if __name__=="__main__":
    a=CommonUtils()
    
    print(a.is_contains('d','abc'))