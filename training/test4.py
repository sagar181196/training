message = raw_input(">")
words = message.split(' ')
emoji = {
    ':)' : '😀',
    ':(' : '😔',
    ';)' : '😉'
}
for word in words:
   print(emoji.get(word,'try another'))
