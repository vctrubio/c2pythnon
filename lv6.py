import sys

## create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]) # => returns "(123) 456-7890"

def create_phone_numbers_v1(n):
    return "({}{}{}) {}{}{}-{}{}{}{}".format(*n)

def create_phone_number_v2(n):
  str1 =  ''.join(str(x) for x in n[0:3])
  str2 =  ''.join(str(x) for x in n[3:6])
  str3 =  ''.join(str(x) for x in n[6:10])

def create_phone_number_v3(n):
    n = ''.join(map(str,n))
    return '(%s) %s-%s'%(n[:3], n[3:6], n[6:])

#####################################################################################

ft_call = {
    'cv1' : create_phone_numbers_v1
    }

def debug_station(*args):
    for i in args:
        print(i)

#=> take 2 arguments from the command line, one to state what function to call, the other to pass a string to that function
if __name__ == "__main__":
    try:
        print(sys.argv[0])
        debug_station(sys.argv)
    except Exception:
        print("ERROR: no argv")


