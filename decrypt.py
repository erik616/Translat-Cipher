import math, pyperclip

def main():
    myMessage = input('Enter your encrypted message:\n') or 'Cenoonommstmme oo snnio. s s c'
    myKey = int(input('Your key:\n') or 8)

    plaintext = decryptMessage(myKey, myMessage)

    print(plaintext + '|')
    pyperclip.copy(plaintext)


def decryptMessage(key,message):
    numOfColumns = math.ceil(len(message) / key)
    numOfRows = key

    numOfShadedBoxes = (numOfColumns * numOfRows) - len(message)

    plaintext = [''] * numOfColumns

    col = 0
    row = 0

    for symbol in message:
        plaintext[col] += symbol
        col += 1

        if (col == numOfColumns) or (col == numOfColumns - 1 and row >= numOfRows - numOfShadedBoxes):
            col = 0
            row += 1

    return ''.join(plaintext)

if __name__ == '__main__':
    main()