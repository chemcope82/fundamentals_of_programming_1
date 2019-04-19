Python 3.7.2 (tags/v3.7.2:9a3ffc0492, Dec 23 2018, 22:20:52) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> txt = 'Welcome to the jungle'
>>> little = txt.lower()
>>> little
'welcome to the jungle'
>>> folded = txt.casefold()
>>> folded
'welcome to the jungle'
>>> 1 == '1'
False
>>> for letter in txt:
	print(letter + 'ee')

	
Wee
eee
lee
cee
oee
mee
eee
 ee
tee
oee
 ee
tee
hee
eee
 ee
jee
uee
nee
gee
lee
eee
>>> txt += "we've got fun and games"
>>> txt
"Welcome to the junglewe've got fun and games"
>>> txt.find("we've")
21
>>> txt.split('jungle')
['Welcome to the ', "we've got fun and games"]
>>> txt
"Welcome to the junglewe've got fun and games"
>>> txtfix = txt.split('jungle')
>>> txtfix
['Welcome to the ', "we've got fun and games"]
>>> txtfix[1] += 'jungle, '
>>> txtfix
['Welcome to the ', "we've got fun and gamesjungle, "]
>>> txtfix = txt.split('jungle')
>>> txtfix[0] += 'jungle, '
>>> txtfix
['Welcome to the jungle, ', "we've got fun and games"]
>>> txt = txtfix[0] + txtfix[1]
>>> txt
"Welcome to the jungle, we've got fun and games"
>>> 
>>> txt.endswith('games')
True
>>> txt.endswith('games') == 1
True
>>> txt.rstrip('games')
"Welcome to the jungle, we've got fun and "
>>> txt
"Welcome to the jungle, we've got fun and games"
>>> txt = txt.rstrip('games')
>>> txt
"Welcome to the jungle, we've got fun and "
>>> txt = txt.lstrip('Welcome')
>>> txt
" to the jungle, we've got fun and "
>>> txt.find("we've")
16
>>> txtslice = txt[16:21]
>>> txtslice
"we've"
>>> txt
" to the jungle, we've got fun and "
>>> txt.isalnum()
False
>>> txt.isalpha()
False
>>> txt.startswith(' ')
True
>>> txt.lstrip()
"to the jungle, we've got fun and "
>>> txt.replace(' ', '  ')
"  to  the  jungle,  we've  got  fun  and  "
>>> txt
" to the jungle, we've got fun and "
>>> txt = 'one'
>>> txt.isalhpa()
Traceback (most recent call last):
  File "<pyshell#43>", line 1, in <module>
    txt.isalhpa()
AttributeError: 'str' object has no attribute 'isalhpa'
>>> txt.isalpha()
True
>>> txt.islower()
True
>>> txt.isdigit()
False
>>> txt = '1'
>>> txt.isdigit()
True
>>> txt += ' 1 1 '
>>> txt
'1 1 1 '
>>> txt.isalnum()
False
>>> txt.find(' ')
1
>>> txt[1].isspace()
True
>>> txt = '12'
>>> txt.islower()
False
>>> txt.isupper()
False
>>> txt.lower()
'12'
>>> txt.islower()
False
>>> txt.upper()
'12'
>>> txt.isupper()
False
>>> txt = 'one'
>>> txt.join('+')
'+'
>>> txt
'one'
>>> '+'.join(txt)
'o+n+e'
>>> txt = "Where's the beef?"
>>> txt.find('*he')
-1
>>> newtxt = txt * 3
>>> newtxt
"Where's the beef?Where's the beef?Where's the beef?"
>>> newtxtlist = newtxt.split('?')
>>> newtxtlist
["Where's the beef", "Where's the beef", "Where's the beef", '']
>>> newtxtlist.pop()
''
>>> newtxtlist
["Where's the beef", "Where's the beef", "Where's the beef"]
>>> '? '.join(newtxtlist)
"Where's the beef? Where's the beef? Where's the beef"
>>> len(newtext)
Traceback (most recent call last):
  File "<pyshell#74>", line 1, in <module>
    len(newtext)
NameError: name 'newtext' is not defined
>>> len(newtxt)
51
>>> txt.replace('beef','salmon')
"Where's the salmon?"
>>> txt
"Where's the beef?"
>>> txt = txt.replace('beef', 'salmon')
>>> txt
"Where's the salmon?"
>>> txt -= 'salmon'
Traceback (most recent call last):
  File "<pyshell#80>", line 1, in <module>
    txt -= 'salmon'
TypeError: unsupported operand type(s) for -=: 'str' and 'str'
>>> txt += " I'm HUNGRY!"
>>> txt
"Where's the salmon? I'm HUNGRY!"
>>> txt = 'Do I have 200 lines yet?'
>>> len(txt)
24
>>> txt = txt.replace('200', 'two hundred')
>>> txt
'Do I have two hundred lines yet?'
>>> txt = 5*' ' + txt
>>> txt
'     Do I have two hundred lines yet?'
>>> txt += 5*' '
>>> txt
'     Do I have two hundred lines yet?     '
>>> txt.lstrip()
'Do I have two hundred lines yet?     '
>>> txt.rstrip()
'     Do I have two hundred lines yet?'
>>> txt = txt.lstrip().rstrip()
>>> txt
'Do I have two hundred lines yet?'
>>> txt = 5*' ' + txt + 5*' '
>>> txt
'     Do I have two hundred lines yet?     '
>>> txt.strip()
'Do I have two hundred lines yet?'
>>> txt
'     Do I have two hundred lines yet?     '
>>> txt = txt.strip()
>>> 
