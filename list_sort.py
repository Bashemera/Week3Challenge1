def sort_list(entered_list):
    evens=[]
    odds=[]
    chars=[]
    dictionary_of_list = dict()
    list_length = len(entered_list)
    i=0
    if type(entered_list) is list:
        if(list_length!=0):
            for i  in entered_list:
                if not isinstance(i,int):
                    chars.append(i)
                elif i%2 ==0:
                    evens.append(i)
                elif i%2 == 1:
                    odds.append(i)
                else:
                    print("No more")
            dictionary_of_list['evens'] =sorted(evens)
            dictionary_of_list['odds'] =sorted(odds)
            dictionary_of_list['chars'] =sorted(chars)

            return dictionary_of_list
        else:
            return "This list is empty"
    else:
        return "This is not a list"
print(sort_list([8,90,34,2,3,'e','t','u']))

    


    
