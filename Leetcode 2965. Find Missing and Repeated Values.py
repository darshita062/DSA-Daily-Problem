def findMissingAndRepeatedValues(grid):
        output = [0]*2
        result = []
        ht = {}
        n = len(grid)
        for i in range(n):
            result += grid[i]
        for num in result:
            if num in ht:
                ht[num] += 1
            else:
                ht[num] = 1
        for key,value in ht.items():
            if value > 1:
                output[0]=key
        for i in range(1,len(result)+1):
            if i not in result:
                output[1] = i
        return output

            
