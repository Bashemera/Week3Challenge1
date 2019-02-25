def missingNumbers(number_list):
    missing_number = []
    for i in range(number_list[0], number_list[-1]+1):
        if i not in number_list:
            missing_number.append(i)
    return missing_number

missingNumbers([1,2,4,5,6])  
