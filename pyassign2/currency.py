"""__author__ = Xu Ruosen
__pkuid__ = 1700011757
__email__ = xhycentre@pku.edu.cn
"""
from urllib.request import urlopen
def exchange(x,y,z):
    n='http://cs1110.cs.cornell.edu/2016fa/a1server.php?from='+x+'&to='+y+'&amt='+z
    jstr=result(n)
    text=find(jstr,z)
    return text

def find(jstr,z):
    text=''
    for i in jstr:
        if i in "1234567890.":
            text=text+i
    length=len(z)
    text=float(text[length:])
    return text
    
def result(n):
    doc = urlopen(n)
    docstr = doc.read()
    doc.close()
    jstr = docstr.decode('ascii')
    return jstr

def main():
    currency_from=input()
    currency_to=input()
    amount_from=input()
    amount_to=exchange(currency_from, currency_to, amount_from)
    print(amount_to)

if __name__ == '__main__':
    main()


def test():
    if exchange("USD","EUR","2.5")==2.0952375:
        return True
    else:
        return False