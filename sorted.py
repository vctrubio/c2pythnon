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

    arr.sort() # sorted(arr)
    a3 = a2.split()[::-1] # sorted(a2.split(), reverse=True)
    print(arr)
    print(a3)
    print("-- --")

    a4 = sorted(a3, key=lambda ptr: ptr[0]) # , reverse=True (can append)
    a5 = sorted(a3, key=lambda word: next(key for key, value in roman_numerals.items() if value == word))
    print(a4)
    print(a5)




if __name__ == '__main__':
    test_sort()