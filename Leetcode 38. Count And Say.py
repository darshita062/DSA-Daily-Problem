def countAndSay(n):
        def helper(var):
            temp_var = ""
            i = 0
            while i < len(var):
                count = 1
                while i + 1 < len(var) and var[i] == var[i+1]:
                        count += 1
                        i += 1
                temp_var += str(count)+var[i]
                i += 1
            return temp_var

        if n == 1:
            return "1"
        else:
            var = "1"
            for _ in range(n-1):
                var = helper(var)
        return var
