def uniqueOccurrences(arr):
        hash_set = {}
        for i in arr:
            if i in hash_set:
                hash_set[i] += 1
            else:
                hash_set[i] = 1
        distinct = []
        for value in hash_set.values():
            if value in distinct:
                return False
            else:
                distinct.append(value)
        return True