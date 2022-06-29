n = int(input('Enter a valid integer>_'))
# print(f" User entered {user_input} ")

# #create 2d array based on user input
# cols, rows =(user_input, user_input)
# col, row = 0,0
# arr = [[0 for i in range(cols)] for j in range(rows)]
# value=1

# while value<=user_input**2:
#   for i in range(col,cols):
#     arr[row][i]=value
#     value+=1
  

# for row in arr:
#   print(row)

row = 0
col = 0
rowCount = n
colCount = n
result = [ [0 for i in range(n)] for j in range(n)]
num = 1
while num<=n**2:
   for i in range(col,colCount):
      result[row][i] = num
      num+=1
   if num > n**2:
      break
   for i in range(row+1,rowCount):
      result[i][colCount-1] = num
      num+=1
   if num > n**2:
      break
   for i in range(colCount-2,col-1,-1):
      result[rowCount-1][i] = num
      num+=1
   if num > n**2:
      break
   for i in range(rowCount-2,row,-1):
      result[i][col] = num
      num+=1
   row+=1
   rowCount-=1
   col+=1
   colCount-=1

for row in result:
  print(row)