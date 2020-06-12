'''
loveme

     l
    lol
   lovol
  lovevol
 lovemevol
lovememevol

'''

def tree():
	print("Enter your word")
	word = input().strip()
	arr = []

	for i in range(len(word)):	#0, 1, 2 ...
		first_pt = word[:i+1].rjust(len(word))
		sec_pt = "".join(reversed(word[:i]))
		arr.append(first_pt + sec_pt)
	
	i = len(arr) - 2
	while i >=0:
		arr.append(arr[i])
		i -= 1
	
	for i in arr:
		print(i)

if __name__ == "__main__":
	tree()



