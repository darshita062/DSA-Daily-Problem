def minimumRecolors(blocks, k):
        min_op = float("infinity")
        n = len(blocks)
        def W_to_B(substr):
            count = 0
            ind = 0
            lst = list(substr)
            for i in lst:
                ind += 1
                if i == "W":
                    lst[ind-1] = "B"
                    count += 1
            return count
        for i in range(n-k+1):
            wd = blocks[i:i+k]
            min_op = min(min_op,W_to_B(wd))
        return min_op
            