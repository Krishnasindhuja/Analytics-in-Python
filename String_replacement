#string replacement function 

def replace(test_string, replace_string):
    x=len(replace_string)
    print(x)
    replace_with = "whatever"
    loc = test_string.find(replace_string)
    print(loc)
    string1 =test_string[0:loc-1]
    string2 = test_string[loc:loc+x]
    string3 = test_string[loc+x+1:]
    print(string2) 
    y= string2
    print(y)
    y=replace_with
    #print(id(y),id(replace_with))
    z=string1 + " " + y + " " + string3
    return z
        
test_string = "hey good morning"
replace_string ="good" 
curr_string = replace(test_string,replace_string)
print(curr_string)
