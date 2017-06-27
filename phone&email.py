import re
phonerg=re.compile(r'(\(?(\d){3}\)?)?(\.|-|\s|)?(\(?(\d){3}\)?)(\s|\.|-)(\(?(\d){4}\)?)(\s*(ext|x|ext.)\s*(\d{2,5}))?')
"""phonerg = re.compile(r'''(
(\d{3}|\(\d{3}\))?
(\s|-|\.)?
(\d{3})
(\s|-|\.)
(\d{4})
(\s*(ext|x|ext.)\s*(\d{2,5}))?
)''', re.VERBOSE)"""
emailrg=re.compile(r'''[A-za-z0-9.]+@[A-za-z]+\.[A-za-z.]{2,10}''')					#.something like .com/.edu.in
import pyperclip
text=str(pyperclip.paste())
#print("TEXT= ",text)
matches = []
for groups in phonerg.findall(text):
	print(groups)
	phoneNum = '-'.join([groups[0], groups[3], groups[6]])
	if groups[8] != '':
		phoneNum += ' x' + groups[8]
	matches.append(phoneNum)
for g in emailrg.findall(text):
	matches.append(g)	
if(len(matches)>0):
	pyperclip.copy('\n'.join(matches))
	print("Copied to clipboard")
	print(matches)
else:
	print('No phone numbers or email addresses found.')
