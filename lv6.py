import sys
import libft

## create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]) # => returns "(123) 456-7890"

def debug_station(*args):
    for i in args:
        print(i)

def norminette(n):
    if len(n) == 10:
        return True

def create_phone_numbers_v1(n):
    return "({}{}{}) {}{}{}-{}{}{}{}".format(*n)

def create_phone_number_v2(n):
    str1 =  ''.join(str(x) for x in n[0:3])
    str2 =  ''.join(str(x) for x in n[3:6])
    str3 =  ''.join(str(x) for x in n[6:10])
    str4 = str1 + str2 + str3
    return str4

def create_phone_number_v3(n):
    n = ''.join(map(str,n))
    return '(%s) %s-%s'%(n[:3], n[3:6], n[6:])

ft_call_0712 = {
    'v1': create_phone_numbers_v1,
    'v2': create_phone_number_v2,
    'v3': create_phone_number_v3,
}

## reverse words if greater than 5 # => 
def spin_words_v1(sentence):
    lst = sentence.split()
    rtn = []
    for index, i in enumerate(lst):
        if len(i) <= 5:
            rtn.append(i)
        else:
            rtn.append(i[::-1])
    str1 = ' '.join(rtn)
    return str1

def spin_words_v2(sentence):
    words = sentence.split()
    rev_words = [w[::-1] if len(w) > 5 else w for w in words]
    return ' '.join(rev_words)

ft_call_0512 = {
    'v1': spin_words_v1,
    'v2': spin_words_v2,
}

## to_capitalize
def to_jaden_case(string):
    return ' '.join([word.capitalize() for word in string.split()])

## function_callers
def ft_0712(create_phone_number_v, phone_numer):
    print(ft_0712.__name__)
    try:
        ft_name = create_phone_number_v
        if ft_name in ft_call_0712 and norminette(phone_numer):
            rtn_ft_call = ft_call_0712[ft_name] 
            parsed_phone_number = rtn_ft_call(phone_numer)
            print(libft.style.GREEN + "√" + libft.style.RESET + parsed_phone_number)
        else:
            raise Exception ("[0712]: No ft_call found")
    except Exception as e:
        print(e)

def ft_0512(version, str):
    print(ft_0512.__name__)
    try:
        if version in ft_call_0512:
            rtn_ft_call = ft_call_0512[version]
            parsed_str = rtn_ft_call(str)
            print(libft.style.GREEN + "√" + libft.style.RESET + parsed_str)
    except:
        print(libft.style.RED + "[0512] could not call function" + libft.style.RESET)

ft_date = {
    '0712': ft_0712,
    '0512': ft_0512,
}

#=> take 2 arguments from the command line, one to state what function to call, the other to pass a string to that function
if __name__ == "__main__":
    if len(sys.argv) > 1:
        if sys.argv[1] in ft_date:
            try:
                ft_date[sys.argv[1]](sys.argv[2], sys.argv[3])
            except:
                print(libft.style.RED + "could not call function" + libft.style.RESET)
        else:
            print(libft.style.RED + sys.argv[1] + libft.style.RESET + " : not in ft_date_index")
    else:
        print("usage: argc1= ft_you_want_to_call, arg2+= arguments_for_given_function")
