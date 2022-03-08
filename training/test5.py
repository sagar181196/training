def emoji(x):
    word = message.split(" ")
    dict = {':)' : '😀', ':(': '😣'}
    output=''
    for di in dict:
        output+=dict.get(di,di)
        return output


message=raw_input()
print(emoji(message))