import re
import os

# 正则替换中的app名是 book,所以使用 book:

filespath = '/root/django/huoxingman/huoxingman/blog/templates/blog/'
patternhref = r'href="(?P<filename>.*?)"'
patternsrc = r'src="(?P<filename>.*?)"'
patternextension = re.compile(r'(.*)\.(.*)')

# 正则替换中提供的函数，用于处理匹配到的href标签处理
def subhref(matched):
    filename = matched.group('filename') # 根据正则分组获取文件名
    extension = patternextension.match(filename) #根据匹配到的字符串是否是文件进行处理
    if extension != None:
        # 跳转为另一个页面则使用 url
        if extension.group(2) == 'html': 
            temp = '\'blog:%s\'' % extension.group(1)
            return 'href=\"{% url ' + temp + ' %}\"'
        
        # 跳转到其他静态文件则使用 static
        temp = '\'%s\'' % extension.group(0)
        return 'href=\"{% static ' + temp + ' %}\"'
    
    # 匹配到的不带有扩展名，即不是文件，返回原字符串
    return matched.group(0)
    

 
# 正则替换中提供的函数，用于处理匹配到的src标签处理
def subsrc(matched):
    filename = matched.group('filename')
    extension = patternextension.match(filename) #根据匹配到的字符串是否是文件进行处理
    if extension != None:
        # 使用 static
        temp = '\'%s\'' % extension.group(0)
        return 'src=\"{% static ' + temp + ' %}\"'
    
    # 匹配到的不带有扩展名，即不是文件，返回原字符串
    return matched.group(0)

def modify():
    files = os.listdir(filespath)
    for htmlfile in files:
        f = open(filespath+htmlfile,'r+',encoding='utf-8')
        text = f.read()
        f.seek(0)
        f.truncate()

        headproclaim = '{% load static %}'+'\n'
        f.write(headproclaim) # 在文件最前面添加django加载静态文件声明

        text = re.sub(patternhref,subhref,text) # 正则替换href标签为django形式
        text = re.sub(patternsrc,subsrc,text) # 正则替换src标签为django形式

        f.write(text)
        f.close()

if __name__ == '__main__':
    modify()
