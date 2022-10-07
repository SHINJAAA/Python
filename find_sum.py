def find_sum(num):
    if num == 0:
       return 0
    else:
      return num + find_sum(num-1)

num=int(input("Enter a number: "))

print("The sum of first "+str(num)+ " is",find_sum(num))