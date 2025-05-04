def numEquivDominoPairs(dominoes):
        """
        # Brute Force Method
        n = len(dominoes)
        count = 0
        for i in range(n):
            for j in range(i+1,n):
                if (dominoes[i][0]==dominoes[j][1] and dominoes[i][1]==dominoes[j][0]) or (dominoes[i][0]==dominoes[j][0] and dominoes[i][1]==dominoes[j][1]):
                    count += 1
        return count
        """
        # Optimized Method
        count = 0
        freq = {}

        for a, b in dominoes:
            key = (min(a, b), max(a, b))  # ensures [a,b] and [b,a] are treated the same
            count += freq.get(key, 0)
            freq[key] = freq.get(key, 0) + 1

        return count