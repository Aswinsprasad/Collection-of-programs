# check if a number is prime

num = 11
 

if num > 1:
 

    for i in range(2, int(num/2)+1):
 
      
        if (num % i) == 0:
            print(num, " not a prime number")
            break
    else:
        print(num, " prime number")
 
else:
    print(num, "not a prime number")
