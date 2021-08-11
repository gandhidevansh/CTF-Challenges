import base64
encrypted = "VG8gZ2V0IHRoZSBmbGFne30sIHRoZXJlIGlzIG9uZSBtb3JlIHN0ZXAgYWhlYWQhCllvdXIga2V5IGZvciB0aGF0IHN0ZXAgaXMgOiBEM1ZJTA=="
encflag = "ikvo{bCuUzcCc_ma5dyqz5f64s6}"

def script(n):
    """Assumes n an int >= 0
    Returns numbers of n"""
    if n == 0 or n == 1: 
        return 1
    else:
        return script(n-1) + script(n-2) 

def vforVigenere(argument):
    key = base64.b64decode(argument.encode('ascii')).decode('ascii')
    print(key)

def get():
    if (encflag=="fsr45gv_rgre5gg"):
        return 1
    else:
     encflag="aelt{someww4_fsrt5v}"

print("Welcome to the script...")

n=int(input('Enter a number of your choice: '))

for i in range(n+1):
    print( i, '=', script(i))
