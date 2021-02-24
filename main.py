import random


def generateTitle():
    fa = open('adjectives.txt', 'r')
    fn = open('nouns.txt', 'r')
    linea = fa.readlines()
    linen = fn.readlines()

    # 5749 lines of adjectives
    # 6801 lines of nouns

    print(str(linea[random.randint(0,5749)])[:-1] + ' ' + str(linen[random.randint(0,6801)]))

    fa.close()
    fn.close()