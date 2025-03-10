def canPlaceFlowers(flowerbed, n):
        f = [0] + flowerbed + [0]     
        for i in range(1,len(f)-1):
            if f[i] == 0 and f[i-1] == 0 and f[i+1] == 0:
                n -= 1
                f[i] = 1
        if n <= 0:
            return True
        return False