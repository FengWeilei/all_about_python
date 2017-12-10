# -*- coding: utf-8 -*-

import re

def is_valid_email(addr):
    regex = r'(\w+\.)?\w+@\w+\.com'
    print(re.match(regex, addr) != None)
    
##is_valid_email('someone@gmail.com')
is_valid_email('someone@gmail.com')
is_valid_email('bill.gates@microsoft.com')
is_valid_email('bob#example.com')
is_valid_email('mr-bob@example.com')
print('ok')

print('-'*20)

def name_of_email(addr):
    regex = r'\<(\w+\s\w+)\>\s\w+@\w+\.org|(\w+)@\w+\.org'
    result = re.match(regex, addr).group(2)
    print(result)
    return result
print(name_of_email('<Tom Paris> tom@voyager.org') == 'Tom Paris')
print(name_of_email('tom@voyager.org') == 'tom')
