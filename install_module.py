''' 
安装常用库
1、安装mongo key value
    首先 下载 进入官网--下载--community server --下载对应版本
    下一步，安装
    进入安装目录bin同级文件夹，新建data文件夹（存储数据），在该文件夹下新建db文件夹，复制该bin路径a
    进入bin文件夹下，shift+右键  打开命令窗口
    输入mongod --dbpath 路径a
    浏览器输入localhost:27017显示成功后
    命令行输入mongo
    db
    db.test.insert(('name','bob'))

    cmd.exe 配置为服务
    进入mongo的安装路径bin文件夹下
    在bin同级目录下新建文件夹logs，下面新建mongo.log文件，路径为b
    cmd:
    进入bin文件
    mongod --bind_ip 0.0.0.0 --logpath 路径b --logappend --dbpath 路径a
    --port 27017 --serviceName "MongoDB" --serviceDisplayName "MongoDB" --install

    配置完成  启动服务
    robomongo桌面可视化工具
    创建用户角色
    cmd进入bin文件
    db.createUser({user:"root",pwd:"123456","role":"userAdminAnyDatabase","db":"admin"})
    show users
    使用此账号密码登录可视化工具
2、安装redis 、redis desktop

3、安装mysql  下载and安装  可视化工具 mysql-font
'''