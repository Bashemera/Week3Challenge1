def sort_list(list):
    evens=[]
    odds=[]
    chars=[]
    dictionary_of_list = dict()
    list_length = len(list)
    i=0
    while i<list_length:
        if i%2 ==0:
            evens.append(i)
        elif i%2 == 1:
            odds.append(i)
        else:
            chars.append(i)
        i += 1
    dictionary_of_list['evens'] =sorted(evens)
    dictionary_of_list['odds'] =sorted(odds)
    dictionary_of_list['chars'] =sorted(chars)

    print(dictionary_of_list)

if __name__ == "__main__":
    sort_list(['y','u',7,2,5,8])


    
