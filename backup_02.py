name=input("请输入文件名")
old=open(name,'r',encoding='UTF-8')  # 打开name文件，只读模式，utf-8解码
if old:                              # 若文件存在
    suf=name.rfind('.')              # ’ . ‘的索引 
    if suf>0:                        # ’ . ‘若存在
        copy=name[:suf]+'[copy]'+name[suf:]  # 新文件的名字
    new=open(copy,'w',encoding='UTF-8')      # 新建文件
    for i in old.readlines():                # 读取每行的数据
        new.write(i)                         # 写入数据
print("%s成功备份为%s"%(name,copy))
new.close()                           # 关闭备份文件
old.close()                           # 关闭原文件
