from operator import itemgetter

roman_numerals = {1000: 'M',
                  900: 'CM',
                  500: 'D',
                  400: 'CD',
                  100: 'C',
                  90: 'XC',
                  50: 'L',
                  40: 'XL',
                  10: 'X',
                  9: 'IX',
                  5: 'V',
                  4: 'IV',
                  1: 'I'
                  }

def test_sort():
    global roman_numerals
    arr = []
    a2 = ''
    for key in roman_numerals:
        a2 += roman_numerals[key] + ' '
        arr.append(key)

    print(arr)
    print(a2)
    print("-- --")

    arr.sort()  # sorted(arr)
    a3 = a2.split()[::-1]  # sorted(a2.split(), reverse=True)
    print(arr)
    print(a3)
    print("-- --")

    a4 = sorted(a3, key=lambda ptr: ptr[0])  # , reverse=True (can append)
    a4 = sorted(a3, key=itemgetter(0))  # ^ same as above
    a5 = sorted(a3, key=lambda word: next(
        key for key, value in roman_numerals.items() if value == word))
    print(a4)
    print(a5)


# sort by int in word: to sort a given string. Each word in the string will contain a single number. This number is the position the word should have in the result.

def order_v1(words):
  return ' '.join(sorted(words.split(), key=lambda w:sorted(w)))

def order_v2(sentence):
    result = []
    split_up = sentence.split() #the original sentence turned into a list
    for i in range(1,10):
        for item in split_up:
            if str(i) in item:
                 result.append(item)    #adds them in numerical order since it cycles through i first
    return " ".join(result)

def extract_number(word):
    for l in word: 
        if l.isdigit(): return int(l)
    return None
def order_v3(sentence):
    return ' '.join(sorted(sentence.split(), key=extract_number))

def order_v4(sentence):
  return " ".join(sorted(sentence.split(), key=min))

if __name__ == '__main__':
    test_sort()
