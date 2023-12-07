import sys
import libft

## create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]) # => returns "(123) 456-7890"

def create_phone_numbers_v0(n):
    return n

def create_phone_numbers_v1(n):
    return "({}{}{}) {}{}{}-{}{}{}{}".format(*n)

def create_phone_number_v2(n):
  str1 =  ''.join(str(x) for x in n[0:3])
  str2 =  ''.join(str(x) for x in n[3:6])
  str3 =  ''.join(str(x) for x in n[6:10])
  return str1 + str2 + str3

def create_phone_number_v3(n):
    n = ''.join(map(str,n))
    return '(%s) %s-%s'%(n[:3], n[3:6], n[6:])

ft_call_0712 = {
    'v0': create_phone_numbers_v0,
    'v1': create_phone_numbers_v1,
    'v2': create_phone_number_v2,
    'v3': create_phone_number_v3,
}

####################

def debug_station(*args):
    for i in args:
        print(i)

def ft_0712():
    try:
        if (len(sys.argv) != 4):
            raise Exception ("!argc")
        else:
            debug_station(sys.argv)
            ft_name = sys.argv[2]
            if ft_name in ft_call_0712:
                print("found ft_call-")
                rtn_ft_call = ft_call_0712[ft_name] 
                parsed_phone_number = rtn_ft_call(sys.argv[sys.argv[3]])
                print(libft.style.GREEN + "√" + libft.style.RESET + parsed_phone_number)
            else:
                raise Exception ("No ft_call- found")
    except Exception as e:
        print(e)

ft_date = {
    '0712': ft_0712,
}

#=> take 2 arguments from the command line, one to state what function to call, the other to pass a string to that function
if __name__ == "__main__":
    if len(sys.argv) > 1:
        if sys.argv[1] in ft_date:
            print("- found in date")
            ft_date[sys.argv[1]]()
        else:
            print(libft.style.RED + sys.argv[1] + libft.style.RESET + " : not in ft_date_index")
    else:
        print("usage: argc1= ft_you_want_to_call, arg2+= arguments_for_given_function")
