""" 
发送邮件
"""
import smtplib
from email.mime.text import MIMEText
class SendMail:

    user="niuya_cong@163.com"
    host="smtp.163.com"
    password="0000"
    def Send_mail(self,user_list,sub,content):
        send_user="niuya_cong<"+SendMail.user+">"
        message=MIMEText(content,_subtype="plain",_charset="utf-8")
        message['Subject']=sub
        message['From']=send_user
        message['To']=";".join(user_list)
        server=smtplib.SMTP()
        server.connect(SendMail.host)
        server.login(SendMail.user,SendMail.password)
        server.sendmail(send_user,user_list,message.as_string())
        server.close()

    def send_main(self,pass_list,fail_list):
        pass_num=float(len(pass_list))
        fail_num=float(len(fail_list))
        count_num=pass_num+fail_num
        pass_result="%.2f%%"%(pass_num/count_num*100)
        fail_result="%.2f%%"%(fail_num/count_num*100)

        userlist=['1139800084@qq.com']
        sub="接口自动化测试报告"
        content="此次运行接口%s个，通过率为%s"%(count_num,pass_result)
        self.Send_mail(userlist,sub,content)

if __name__=="__main__":
    mail=SendMail()
    userlist=['1139800084@qq.com']
    mail.Send_mail(userlist,'这是标题','这是内容')