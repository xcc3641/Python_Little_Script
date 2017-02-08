# coding=utf-8
from lxml import etree

'''
nodename	选取此节点的所有子节点。
/	        从根节点选取。
//	        从匹配选择的当前节点选择文档中的节点，而不考虑它们的位置。
.	        选取当前节点。
..	        选取当前节点的父节点。
@	        选取属性。

谓语（Predicates）

谓语用来查找某个特定的节点或者包含某个指定的值的节点。

谓语被嵌在方括号中。

/bookstore/book[price>35.00]/title	选取 bookstore 元素中的 book 元素的所有 title 元素，且其中的 price 元素的值须大于 35.00。

'''

text = '''
<div>
    <ul>
         <li class="item-0"><a href="link1.html">first item</a></li>
         <li class="item-1"><a href="link2.html">second item</a></li>
         <li class="item-inactive"><a href="link3.html">third item</a></li>
         <li class="item-1"><a href="link4.html">fourth item</a></li>
         <li class="item-0"><a href="link5.html">fifth item</a>
     </ul>
 </div>
'''
html = etree.HTML(text)
result = etree.tostring(html)
print(result)

result = html.xpath('//li')
print result

result = html.xpath('//li/@class')
print result

result = html.xpath('//li/a')
print result[0].text
