# check the number is palindrome or not ?

def checkPalindrome(num):
    tempNum = num
    reverseNum = ""
    for i in range(0,len(str(num))):
    # print(num % 10)
        reverseNum += str(num % 10)
        num = int(num/10)
        # print(num)

    if str(tempNum) == reverseNum:
       # print('TRUE it is a palindrome')
       return True
    else:
        return False

num = int(input('Enter Your number'))

print(checkPalindrome(num))
