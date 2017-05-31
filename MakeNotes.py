import pyperclip,sys
text=""
while True:
	if(text!=pyperclip.paste()):
		text=pyperclip.paste()
		"""l=text.split('\n')
		if(l.__contains__('')):
			l.remove('')"""
		f=open("Note.txt","a")
		f.write('#')
		f.write(text)
		f.write('\n')
		"""for i in l:
			f.write(i)
			f.write('\n')
		f.close()
		x=input("Newtext??Wish to add it to notes? (Y/N)")
		if(x=='n' or x=='N'):
			sys.exit()"""