import pyperclip,webbrowser,sys
print("sys.argv[0]= ",sys.argv[0])
if(len(sys.argv)>1):
	print("used command line")
	addr='_'.join(sys.argv[1:])
else:
	print("used clipboard")
	addr=pyperclip.paste()
print("address=",addr)
url='https://www.google.co.in/maps/search/'+addr
print("url=",url)
webbrowser.open(url)