lista = "CHS88"




s = ['chs845','chsu99']

def firstdigit(string):
    return[string.isdigit() for string in string].index(True)

for item in s:
    print (firstdigit(item))