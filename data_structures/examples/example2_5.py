# shows basic usage of genexps to build a tuple and an array
symbols = '$¢£¥€¤'
print(tuple(ord(symbol) for symbol in symbols))  


import array
print(array.array('I', (ord(symbol) for symbol in symbols)))
