## Create the below pattern using nested for loop in Python.
"""
*
* *
* * *
* * * *
* * * * *
* * * *
* * *
* *
*
"""

n=int(input("Please enter a number with maximum * you wish to see at the middle of the picture: "))
for i in range(1,n+1):
	out="* "*i
	print (out)
	if i==n:
		for j in range(n-1,0,-1):
			out1="* "*j
			print (out1)
