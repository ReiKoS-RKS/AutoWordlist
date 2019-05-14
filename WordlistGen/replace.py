import re
string = open('gen.txt').read()
new_str = re.sub('[^a-zA-Z0-9\n\.]', '', string)
open('pass.txt', 'w').write(new_str)