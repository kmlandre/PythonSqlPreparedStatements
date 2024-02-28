import base64
import random
import string


class CustomList(list):
    def __getitem__(self, index):
        return super(CustomList, self).__getitem__(index % len(self))


def makeCircularArray(targetArray):
    circularBytes = CustomList()
    circularBytes.extend(targetArray)

    return circularBytes


def cypher(plain, key):
    plainBytes = plain.encode("utf-8")

    keyBytes = key.encode("utf-8")
    circularBytes = makeCircularArray(keyBytes)

    cypherList = []
    output = ""

    for idx, x in enumerate(plainBytes):
        cypherChar = x * circularBytes[idx]
        cypherList.append(cypherChar)

    for x in cypherList:
        intAsBytes = x.to_bytes(2, "big")
        # print(f'{x} = {intAsBytes}')
        encoded = base64.b64encode(intAsBytes)
        output += encoded.decode("utf-8")[0:3]

    return output


def deCypher(key, cypherText):
    keyBytes = key.encode("utf-8")
    circularBytes = makeCircularArray(keyBytes)

    cypherChunkSize = 3
    cypherChunks = []

    for i in range(0, len(cypherText), cypherChunkSize):
        cypherChunk = cypherText[i: i + cypherChunkSize]
        cypherChunk += '='
        decoded = base64.b64decode(cypherChunk)
        plainInt = int.from_bytes(decoded, byteorder='big')
        # print(plainInt)
        cypherChunks.append(plainInt)

    plainText = ""

    for idx, x in enumerate(cypherChunks):
        # print(f'{x} :: {circularBytes[idx]} -- {x/circularBytes[idx]}')
        decypheredInt = int(x / circularBytes[idx])
        plainText += chr(decypheredInt)

    return plainText


def getRandomKey(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    randokey = "".join(random.choice(characters) for i in range(length))
    return randokey


def test():
    p = input("Enter plain text to Cypherize: ")
    print("")

    k = getRandomKey(16)
    tmpK = input(f"Enter key text [{k}] (press return to keep current key): ")

    if tmpK != "":
        k = tmpK

    c = cypher(p, k)
    d = deCypher(k, c)

    print(f"Cypher of [{p}] and [{k}] is:\n\t{c}")
    print("")
    print(f"DeCypher of [{k}] and [{c}] is:\n\t{d}")


##################################################

test()
