import pyperclip


def main():
    message = """Charles Babbage, FRS (26 December 1791 - 18 October 1871) was an English mathematician, philosopher, inventor and mechanical engineer who originated the concept of a programmable computer. Considered a "father of the computer", Babbage is credited with inventing the first mechanical computer that eventually led to more complex designs. Parts of his uncompleted mechanisms are on display in the London Science Museum. In 1991, a perfectly functioning difference engine was constructed from Babbage's original plans. Built to tolerances achievable in the 19th century, the success of the finished engine indicated that Babbage's machine would have worked. Nine years later, the Science Museum completed the printer Babbage had designed for the difference engine."""
    default = 'Common sense is not so common.'

    myMessage = input('Type your message:\n') or message
    myKey = int(input('Type a key:\n ') or 8)

    ciphertext = encryptMessage(myKey, myMessage)
    print(ciphertext + '|')
    pyperclip.copy(ciphertext)


def encryptMessage(key, message):
    ciphertext = [''] * key

    for col in range(key):
        pointer = col

        while pointer < len(message):
            ciphertext[col] += message[pointer]
            # print(message[pointer])
            pointer += key

    return ''.join(ciphertext)


if __name__ == '__main__':
    main()
