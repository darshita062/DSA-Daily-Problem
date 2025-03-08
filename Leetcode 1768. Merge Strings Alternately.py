def mergeAlternately(word1, word2):
        list1 = []
        list2 = []
        for i in word1:
            list1.append(i)
        for j in word2:
            list2.append(j)
        string = ""
        if (len(word1) > len(word2)):
            for i in range(len(word2)):
                string += word1[i] + word2[i]
            print(string)
            string += word1[len(word2):]
        elif (len(word1) < len(word2)):
            for i in range(len(word1)):
                string += word1[i] + word2[i]
            print(string)
            string += word2[len(word1):] 
        else:
            for i in range(len(word1)):
                string += word1[i] + word2[i]
            print(string)
        return string