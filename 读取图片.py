#读取文件
with open(r'E:\study\python_study\wenjian\tupian.jpg','rb')as f:
    img=f.read()
    
#写入文件
with open(r'E:\study\python_study\wenjian\tupian2.jpg','wb')as f1:
    f1.write(img)