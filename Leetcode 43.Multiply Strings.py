def multiply(num1, num2):
    def convert(s):
        num = 0
        sign = 1
        i = 0
        if i < len(s) and s[i] == "-":
            sign = -1
            i += 1
        for c in s[i:]:
            num = num * 10 + (ord(c)-ord('0'))
        return num*sign
    num1 = convert(num1)
    num2 = convert(num2)
    return str(num1*num2)