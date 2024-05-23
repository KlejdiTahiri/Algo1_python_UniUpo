import base64
mystr = 'Ymxle3NIZCBiZSBGaGUgsW1w2XJmZWNOLCBmb31gdChleSBzaGFsbCBlbWVy22UgdmljdG9yaW91cwo--'

# Encode
mystr_encoded = base64.b64encode(mystr.encode('utf-8'))
#print(mystr_encoded)
# b'TyBKb8OjbyBtb3JkZXUgbyBjw6NvIQ=='

# Decode
mystr_encoded = base64.b64decode(mystr_encoded).decode('utf-8')
print(mystr)
# 'O João mordeu o cão!'