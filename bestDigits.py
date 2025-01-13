def bestDigits(number, numDigits):
    stack = []
    for digit in number:
        #edge case 1
        while numDigits > 0 and len(stack) > 0 and digit > stack[-1]:
            numDigits -= 1
            stack.pop()
        stack.append(digit)

    #edge case 2
    while numDigits > 0:
        numDigits -= 1
        stack.pop()
        
    return "".join(stack)  

number = "462839"
numDigits= 2
ans = bestDigits(number, numDigits)
print(ans)· 