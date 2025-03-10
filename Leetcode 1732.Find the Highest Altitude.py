def largestAltitude(gain):
        r = [0]*(len(gain)+1)
        for i in range(1,len(r)):
            r[i] = r[i-1]+gain[i-1]
        print(r)
        return max(r)