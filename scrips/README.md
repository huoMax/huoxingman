# 用于处理DJANGO的一些小问题

## DjangoStyleTransfer

* 当我从Bootstrap模板网站下载一套好看的模板并应用在django上时，我就要修改html文件中的href和static标签内容，使用{% url %}和{% static %}来链接静态文件，如果一项一项进行修改的话会很麻烦，所以这里使用了re库中的sub()替换

* 使用之前需要先将filespath修改为自己的存储html文件的地址

* 之后将subhref()函数中的temp = '\'blog:%s\'' % extension.group(1)中blog替换为自己的对应的app名称

* 存在的问题：
    * 将{% load staticfiles %}添加到文件首部之后，会出现一个乱码
    * 会匹配文件内定义的样式中链接css文件或者js文件的href和src标签