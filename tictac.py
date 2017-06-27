import os,sys
def printing(arr,n):
	print("\n ___ ___ ___")
	for i in range(n-1,-1,-1):
		print('|',end='')
		for j in range (0,n):
			if(not arr[i][j]==0):
				print(" %s |"%arr[i][j],end=''),
			else:
				print("   |",end='')
		print("\n|___|___|___|")

def chance(arr,n):
	k=0
	l=['X','O']
	for i in range(len(arr)):
		for j in range(len(arr[i])):
			arr[i][j]=' '
	while (k<9):
		s="Player "+str(k%2+1)+" Enter your choice,1 to 9\n"
		while(True):
			ch=int(input(s))
			r=(ch-1)//3
			c=(ch-1)%3
			#print(r,c,k,(k%2))
			if(arr[r][c]==' '):
				arr[r][c]=l[k%2]
				break
			else:
				print("You can't Enter a block which is already occupied\n")
		os.system('clear')
		printing(arr,3)
		t=check_row_wise(arr)|check_col_wise(arr)|check_diagonal_wise(arr)
		print(check_col_wise(arr),check_row_wise(arr),check_diagonal_wise(arr))
		if(t==1):
			print("Congrats! Player ",(k%2+1)," wins......" )
			sys.exit()
		k+=1


def check_row_wise(arr):
	for i in arr:
		if(len(set(i))==1 and len(i)==len(arr) and i.__contains__(' ')==False):
			return 1
	return 0

def check_col_wise(arr):
	for i in range(len(arr[0])):
		l=[]
		for j in range(len(arr[i])):
			l.append(arr[j][i])
		if(len(l)==len(arr) and len(set(l))==1 and l.__contains__(' ')==False):
			return 1
	return 0

def check_diagonal_wise(arr):
	l=[]
	k=[]
	for i in range(len(arr)):
		l.append(arr[i][i])
		k.append(arr[i][len(arr)-1-i])
	if((l.__contains__(' ')==False and len(l)==len(arr) and len(set(l))==1) or (len(k)==len(arr) and len(set(k))==1 and k.__contains__(' ')==False)):
		return 1
	else:
		return 0


	"""else:
		ch=int(input("Player 2, Enter your choice,1 to 9\n"))
		arr[(ch-1)%3][(ch-1)%3]='O'
		os.system('clear')
		printing(arr,3)"""
print("The Tic Tac Toe grid is as follows.Press the respective button(1 to 9) to make your move\n")
list=[[1,2,3],[4,5,6],[7,8,9]]
printing(list,3)
chance(list,3)
#ending
#sdas
