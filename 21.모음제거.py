def solution(my_string):
    li = ["a","e","i","o","u"]
    for str in li :
        my_string = my_string.replace(str,"")
    return my_string