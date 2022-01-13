ltrs={
    0:" ",
    1:"a",
    2:"b",
    3:"c",
    4:"d",
    5:"e",
    6:"f",
    7:"g",
    8:'h',
    9:'i',
    10:'j',
    11:'k',
    12:'l',
    13:'m',
    14:'n',
    15:'o',
    16:'p',
    17:'q',
    18:'r',
    19:'s',
    20:'t',
    21:'u',
    22:'v',
    23:'w',
    24:'x',
    25:'y',
    26:'z',
    27:'A',
    28:'B',
    29:'C',
    30:'D',
    31:'E',
    32:'F',
    33:'G',
    34:"H",
    35:'I',
    36:'J',
    37:'K',
    38:'L',
    39:'M',
    40:'N',
    41:'O',
    42:'P',
    43:'Q',
    44:'R',
    45:'S',
    46:'T',
    47:'U',
    48:'V',
    49:'W',
    50:'X',
    51:'Y',
    52:'Z',
    53:'`',
    54:'~',
    55:'!',
    56:'@',
    57:'#',
    58:'$',
    59:'%',
    60:'^',
    61:'&',
    62:'*',
    63:'(',
    64:')',
    65:'-',
    66:'_',
    67:'=',
    68:'+',
    69:'[',
    70:']',
    71:'\\',
    72:'|',
    73:';',
    74:':',
    75:"'",
    76:'"',
    77:',',
    78:'<',
    79:'.',
    80:'>',
    81:'/',
    82:'?',
    83:'0',
    84:'1',
    85:'2',
    86:'3',
    87:'4',
    88:'5',
    89:'6',
    90:'7',
    91:'8',
    92:'9',
    93:'{',
    94:'}'
    }

def strtodec(string,shift):
    strlen=len(string)
    c1=0
    c2=0
    ret={}
    while c1 != strlen:
        while ltrs[c2] !=  string[c1]:
            c2+=1
        c2+=shift
        ret[c1] = c2
        c2=0
        c1+=1
    return ret

def dectohex(strlen,decin):
    c1=0
    ret=''
    hold=''
    while c1 != strlen:
        if decin[c1]<16:
            hold='0'
        else:
            hold=''
        if decin[c1]==0:
            ret+='00' + ' '
        else:
            ret+=hold + hex(decin[c1]).lstrip('0x') + ' '
        c1+=1
    return ret

def hextodec(strlen,hexin):
    hexstr=hexin
    c1=0
    cmax=strlen
    rl=0
    rr=0
    ret={}
    while rr < cmax:
        rr+=3
        ret[c1]=int(hexstr[rl:rr],16)
        rl+=3
        c1+=1
    return ret

def dectostr(decin,declen,shift):
    c1=0
    c2=0
    ret=''
    while c1 != declen:
        while c2 != decin[c1]:
            c2=decin[c1]
        c2-=shift
        ret+=str(ltrs[c2])
        c2=0
        c1+=1
    return ret

def encode():
    string=input("""input string
""")
    shift=int(input("""input shift
"""))
    strlen=len(string)
    retint=strtodec(string,shift)
    rethex=dectohex(strlen,retint)
    print (rethex)

def decode():
    hexstr=input("""input hex string
""")
    shift=int(input("""input shift
"""))
    strlenhex=len(hexstr)
    retint=hextodec(strlenhex,hexstr)
    declen = len(retint) #nice, thanks David :D
    retstr=dectostr(retint,declen,shift)
    print (retstr)

def main():
    repeat='yes'
    print ("Welcome to HEXIPHER")
    while repeat == 'yes':
        mode=input("""encode or decode?
""")
        if mode == 'encode':
            encode()
        elif mode == 'decode':
            decode()
        else:
            print ("""Please check your input""")
        repeat=input("""continue?
yes or no
""")
    print("Exiting")
    quit

main()
#haha funny rite?
