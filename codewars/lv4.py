# Parse string number to int
def parse_int(s):
    word_to_number = {
        'zero': 0, 'and': 0,
        'one': 1, 'two': 2, 'three': 3, 'four': 4,'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9, 'ten': 10, 
        'eleven': 11, 'twelve': 12, 'thirteen': 13,'fourteen': 14, 'fifteen': 15, 'sixteen': 16, 'seventeen': 17, 'eighteen': 18, 'nineteen': 19, 'twenty': 20, 
        'thirty': 30, 'forty': 40, 'fifty': 50, 'sixty': 60, 'seventy': 70, 'eighty': 80, 'ninety': 90, 'hundred': 100, 'thousand': 1000
    }

    words = s.replace('-', ' ').split()
    total = 0
    current_number = 0

    for word in words:
        if word in word_to_number:
            if word == 'and':
                continue  # Skip "and" in the numeric value
            if word == 'hundred':
                current_number *= word_to_number[word]
            else:
                current_number += word_to_number[word]

    total += current_number
    return total


def strip_comments(strng, markers):
    rtn = []
    
    for line in strng.split('\n'):
        for marker in markers:
            index = line.find(marker)
            if index != -1:
                line = line[:index]
                break  
        print(line)
        rtn.append(line.rstrip())
    
    return '\n'.join(rtn)
