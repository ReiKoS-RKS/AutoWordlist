import re
import time
import os
import sys
import random
print("Este é o meu primeiro script, para criar a wordlist digite o número de palavras a gerar e de enter".upper())
time.sleep(3)
print("Depois e so aguardar enquanto as palavras são geradas".upper())
time.sleep(3)
print("A PASTA QUE CONTEM A WORDLIST É (pass.txt), E PARA LIMPAR AS WORDLISTS EXECUTE o python3 clearWordlist.py")
time.sleep(4.5)
print("""



































































""")
c = int(input("Quantas Palavras Deseja Criar?: "))
a = 0
while a != c:
    wordlist = ("a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z")
    WordlistTXT = ()
    wordlistGen = random.choice(wordlist)
    wordlistGen2 = random.choice(wordlist)
    wordlistGen3 = random.choice(wordlist)
    wordlistGen4 = random.choice(wordlist)
    wordlistGen5 = random.choice(wordlist)
    wordlistGen6 = random.choice(wordlist)
#------------Separador_______________
    wordlistTXT = wordlist.index(wordlistGen)
    wordlistTXT = wordlist.index(wordlistGen2)
    wordlistTXT = wordlist.index(wordlistGen3)
    wordlistTXT = wordlist.index(wordlistGen4)
    wordlistTXT = wordlist.index(wordlistGen5)
    wordlistTXT = wordlist.index(wordlistGen6)
#------------Separador_______________
    print(wordlistGen+wordlistGen2+wordlistGen3+wordlistGen4+wordlistGen5+wordlistGen6)
    f = open( 'gen.txt', 'a' )
    f.write(repr(wordlistGen+wordlistGen2+wordlistGen3+wordlistGen4+wordlistGen5+wordlistGen6+wordlistGen2) + '\n' )
    a = a + 1
    f.close()
os.system('python replace.py')
print("""\033[91m=-=-=-=-THANK YOU FOR \033[1mUSING MY SCRIPT-=-=-=-=

\033[91m=-=-=-=-YOUR FILE IS  \033[1mcd pass.txt-=-=-=-=
\033[92m                  _    _  _____                 _____  
\033[92m    /\           | |  | |/ ____|               |  __ \ 
\033[1m   /  \   ___ ___| |__| | |  __ _ __ ___  _   _| |__) |
\033[1m  / /\ \ / __/ _ \  __  | | |_ | '__/ _ \| | | |  ___/ 
\033[1m / ____ \ (_|  __/ |  | | |__| | | | (_) | |_| | |     
\033[92m/_/    \_\___\___|_|  |_|\_____|_|  \___/ \__,_|_|     
                                                       
\033[93mSupport me on Instagram: \033[94m@aceh_owner""")