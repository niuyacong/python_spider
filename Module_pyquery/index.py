""" 
PyQuery库
和jquery用法一样
pip3 install pyquery
"""

html_doc ='''
<html><head><title>The Dormouse's story</title></head>
<body>
<ul>
<li>1</li>
<li>2</li>
<li>3</li>
<li>4</li>
</ul>
<p class="story">...</p>
</body>
</html>
'''

from pyquery import PyQuery as pq

# 载入的三种方式
doc=pq(html_doc)
doc=pq(url="http://www.baidu.com")
# doc=pq(filename='demo.html')

print(doc("li")) # 可标签 可 css 可id


print(doc('#id .css ')) # 层级关系用空格分割

# 查找子元素
print(doc.find("a")) # 可标签 可 css 可id 可嵌套

# 查找直接子元素
doc.children('a')    # 可标签 可 css 可id 可嵌套

# 查找直接父元素
doc.parent()         # 可标签 可 css 可id 可嵌套

# 查找所以父元素
doc.parents()        # 可标签 可 css 可id 可嵌套

# 所有兄弟元素
doc.siblings()       # 可标签 可 css 可id 可嵌套





