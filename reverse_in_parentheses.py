def revers_in_par(s):    
    for i in range(len(s)):
        if s[i] == "(":
            start = i
            print (s[:start])
        if s[i] == ")":
            end = i
            print (end)
            return revers_in_par(s[:start] + s[start+1:end][::-1] + s[end+1:])
    return s