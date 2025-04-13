def countSymmetricIntegers(low, high):
        output = 0
        def has_even_digits(n):
            return len(str(n)) % 2 == 0
        def symmetric(num):
            n = len(str(num))
            mid = int(n/2)
            digit = []
            while num:
                rem = num % 10
                digit.append(rem)
                num = num // 10
            digit = digit[::-1]
            start_sum , end_sum = 0 , 0
            for i in range(mid):
                start_sum += int(digit[i])
            for i in range(len(digit)-1,mid-1,-1):
                end_sum += int(digit[i])
            if start_sum == end_sum:
                return True
            return False
        for i in range(low,high+1):
            if has_even_digits(i):
                if symmetric(i):
                    output += 1
        return output