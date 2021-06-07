def reverse(a):
    word = ""
    for i in a:
        temp = i + word
        word = temp
    return word

