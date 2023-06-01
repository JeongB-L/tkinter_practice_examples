def fizzBuzz(n):
        answer = []
        for num in range(1, n + 1):
            temp = ''
            if num % 3 == 0:
                temp = 'Fizz'
            if num % 5 == 0:
                temp += 'Buzz'
            if num % 3 != 0 and num % 5 != 0:
                temp = str(num)
            #if num < 3:
                #temp = str(num)
            answer.append(temp)
        return answer
    
    
n = 5
print(1 % 3 != 0 and 1 % 5 != 0)
print(fizzBuzz(n))