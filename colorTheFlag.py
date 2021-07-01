"""
Your job is to colour the blank cells red or white so that every red cell only has white neighbours (and no red ones) and every white cell only has red neighbours (and no white ones). You are not allowed to recolour already coloured cells.

Input:
The first line contains t (1≤t≤100), the number of test cases.
In each test case, the first line will contain n (1≤n≤50) and m (1≤m≤50), the height and width of the grid respectively.
The next n lines will contain the grid. Each character of the grid is either 'R', 'W', or '.'.

Output:
For each test case, output "YES" if there is a valid grid or "NO" if there is not.

# Example:
Input -->
3
4 6
.R....
......
......
.W....
4 4
.R.W
....
....
....
5 1
R
W
R
W
R

Output -->
YES
WRWRWR
RWRWRW
WRWRWR
RWRWRW
NO
YES
R
W
R
W
R

"""

t = int(input())
for _ in range(t):
	row, col = map(int, input().split())
	matrix = []
	r_matrix = []
	w_matrix = []
	line1 = ['R', 'W']
	line2 = ['W', 'R']
	if col % 2 == 0:
		line1 = line1*(col//2)
		line2 = line2*(col//2)
	else:
		line1 = line1*((col-1)//2)
		line2 = line2*((col-1)//2)
		line1.append('R')
		line2.append('W')

	flag = True
	for x in range(row):
		if flag:
			r_matrix.append(line1)
			w_matrix.append(line2)
		else:
			r_matrix.append(line2)
			w_matrix.append(line1)

		flag = not flag

	for i in range(row):
		r = input()
		rlist = []
		for x in r:
			rlist.append(x)

		matrix.append(rlist)

	#checking 
	check1 = True
	check2 = True
	flag = False
	for i in range(row):
		for j in range(col):
			if(matrix[i][j] != "."):
				if(matrix[i][j] != r_matrix[i][j]):
					flag = True
					check1 = False
					break
		if flag:
			break

	flag = False
	for i in range(row):
		for j in range(col):
			if(matrix[i][j] != "."):
				if(matrix[i][j] != w_matrix[i][j]):
					flag = True
					check2 = False
					break
		if flag:
			break

	if check1 or check2:
		print("YES")
		if check1:
			for x in r_matrix:
				for y in x:
					print(y, end="")

				print()

		else:
			for x in w_matrix:
				for y in x:
					print(y, end="")

				print()

	else:
		print("NO")
