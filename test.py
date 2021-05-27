# -*- coding:utf-8 -*-
# @Author : Dummerfu
# @Contact : https://github.com/dummerchen 
# @Time : 2021/4/24 11:17
import re

str='image_codes/734d420f-688b-41de-9d24-04450b306580/'
pattern=r"(?P<image_codes>.+)/$"
mc=re.match(pattern,str)

print(mc)
print(mc.group('image_codes'))
