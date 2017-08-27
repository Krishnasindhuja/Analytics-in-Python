#word count 

def word_distribution(string):
    string_split = []
    string_split =string.split()
    string_lower = []
    string_append = []
    print(string_split)
    for strings in string_split:
        #x = strings.lower()
        string_lower.append(strings.lower())
        for index in range(len(string_lower)):
            element = string_lower[index]
            len_element = len(element)
            last_char = element[len_element-1]
            check = element.isalpha()
            if(check):
                string_append.append(element)
            else:
                element[:-1]
                string_append.append(element)
                
                
    return string_append
    
    
    

string="Hello! How are you?"
word_distribution(string)
