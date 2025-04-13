def removeStars(s):
        stack = []
        for i in s:
            if i != "*":
                stack.append(i)
            else:
                stack.pop(-1)
        return "".join(stack)