# -*- coding: utf-8 -*-

import base64
def safe_base64_decode(s):
    b = base64.b64encode(s)
    bstr_tmp = str(b,'utf-8') #把byte类型的数据转换为utf-8的数据
    b_str= bstr_tmp.strip(r'=+') #用正则把 = 去掉
    return b_str

s1 = b"binarybstr\x00string"
s2 = b'YWJjZA=='
s3 = b'YWJjZA'

##safe_b = safe_base64_decode(s1)
safe_b = safe_base64_decode(s2)
##safe_b = safe_base64_decode(s3)
print (safe_b)


##使用Python编写能处理去掉=的base64解码函数
