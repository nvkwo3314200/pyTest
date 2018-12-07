'使用__all__来限定哪些属性会被导入'
#__all__ = ['Error', 'encode', 'decode']

def encode(args):
    print("encode ", args)
    
def decode(args):
    print("decode ", args)
    
Error = 'This is a Error'

'使用_来防止变量被导入'
_hide = 'HELLO'

X = 'X'

Y = 'Y'

Z = 'Z'