__author__ = 'Rinisha'
__date__ = '11/23/2015'

def max(a, b):

    if a > b: # Check is the first argument is bigger then return the first argument
        return a
    else: # else return the second argument
        return b

def max_of_three(a, b, c):
    return max(max(a, b), c)

def find_length_of_string(str):
    sum = 0
    for c in str:
        sum = sum + 1
    return sum

def isVowel(a):
    vowels = ['A', 'E', 'I', 'O', 'U']

    if a.upper() in vowels:
        return True
    else:
        return False

def isConsonant(a):
    consonants = ['q','w','r','t','y','p','s','d','f','g','h','j','k','l','z','x','c','v','b','n','m']
    if a.lower() in consonants:
        return True
    else:
        return False

def translate(string):
    result=""
    for c in string:
        if isConsonant(c):
            result = result + c + 'o' + c
        else:
            result = result + c
    return result

def sum_of_list(list):
    sum=0
    if not list:
        excep = Exception()
        excep.message = "Sum Does not support an empty list"
        raise  excep
    for c in list:
        sum= sum+ c
    return sum

def product_of_list(list):
    #If an empty list raise an exception
    if not list:
        # time to raise that exception
       exception = Exception()
        # set a good message
       exception.message = "Multiplication does not support empty list."
       raise exception

    product=1

    for c in list:
        product= product * c
    return product

def reverse (string):
     #If an empty list raise an exception
    if not string:
        # time to raise that exception
       exception = Exception()
        # set a good message
       exception.message = "reverse does not support empty list."
       raise exception
    return string [::-1]

def isPalindrome(string):
     #If an empty list raise an exception
    if not string:
        # time to raise that exception
       exception = Exception()
        # set a good message
       exception.message = "isPalindrome does not support empty string."
       raise exception
    string1=string.lower()
    if string1 [::-1 ] != string1:
        return False
    else:
        return True

def isMember(list1, x):
     #If an empty list raise an exception
    if not list1:
        # time to raise that exception
       exception = Exception()
        # set a good message
       exception.message = "isMember does not support empty list."
       raise exception
    for c in list1:
        if x == c:
            return True
    return False

def isOverlapping(list1, list2):
     #If an empty list raise an exception
    if not list1:
        # time to raise that exception
       exception = Exception()
        # set a good message
       exception.message = "isOverlapping does not support empty list."
       raise exception
      #If an empty list raise an exception
    if not list2:
        # time to raise that exception
       exception = Exception()
        # set a good message
       exception.message = "isOverlapping does not support empty list."
       raise exception
    for c in list1:
        for i in list2:
            if c == i:
                return True
        else:
            print False

def generate_n_chars (int, character ):
    result = ''
    for i in range(0,int,):
        result= result + character
    return result

def histogram(list ):
    for c in list:
        print generate_n_chars(c, '*')

'''

START OF TEST FUNCTIONS

'''

def test_max():
    # test 2 same positive intgers
    if (max(2, 2) != 2):
        print "max Failed when when calling for same positive numbers"

    # test 2 same 0 intgers
    if (max(0, 0) != 0):
        print "max Failed when when calling for 0s "
    # test 2 same negative intgers
    if (max(-10, -10) != -10):
        print "max Failed when when calling for same negative numbers"
    # test 2 one positive one negative integers
    if (max(530, -250) != 530):
        print "max Failed when when calling for first positive and second negative numbers"

def test_max_of_three():
    # test 3 same positive intgers
    if (max_of_three(2, 2, 2) != 2):
        print "max Failed when when calling for same positive numbers"
    # test 3 same 0 intgers
    if (max_of_three(0, 0, 0) != 0):
        print "max Failed when when calling for 0s"
    # test 3 same negative intgers
    if (max_of_three(-10, -10, -10) != -10):
        print "max Failed when when calling for same negative numbers"
    # test 1 positive 2 negative integers
    if (max_of_three(530, -250, -246) != 530):
        print "max Failed when when calling for 1 positive 2 negative integers"
    if (max_of_three(530, -250, 246) != 530):
        print "max Failed when when calling for 2 positive 1 negative integers"

def test_find_length_of_string():
    if find_length_of_string("Aanya") != 5:
        print 'failed when trying to find length Aanya'
    if find_length_of_string("Pratyush") != 8:
        print 'failed when trying to find length Pratyush'
    if find_length_of_string("Mi hir") != 6:
        print 'failed when trying to find length Mihir space in middle'
    if find_length_of_string("Ana") != 3:
        print 'failed when trying to find length Ana'
    if find_length_of_string(" Neel") != 5:
        print 'failed when trying to find length Neel, space in front'
    if find_length_of_string("Rinisha  ") != 9:
        print 'failed when trying to find length Rinisha, 2 spaces in the end'
    if find_length_of_string("") != 0:
        print 'failed when trying to find length a blank string'
    if find_length_of_string(" ") != 1:
        print 'failed when trying to find length a blank space'

def test_vowel_or_consonant():
    vowels = ['A', 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u']
    not_vowels = ['Q', 'W', 'r', 'T', 'y', 'P','C','c']

    for c in vowels:
        if isVowel(c)== False:
            print "Failed for Vowel: %s" % c

    for c in not_vowels:
        if isVowel(c):
            print "Failed for Consonant: %s" % c

def test_translate():
    if translate("Shruthi") != 'SoShohrorutothohi' :
        print "fail when trying to print Shruthi"
    if translate("Aanya") != 'Aanonyoya':
        print "fail when printing Aanya"
    if translate("Divya") != 'DoDivovyoya':
        print "fail when printing Divya"
    if translate("Mihir") != 'MoMihohiror':
        print "fail when printing Mihir"
    if translate("Rinisha") != 'RoRinonisoshoha':
        print "fail when printing Rinisha"
    if translate("") != "":
        print "fail for blank"
    if translate(" ") != " ":
        print "fail for space"

def test_sum_of_list():
    list1 = [1,2,3,4,5]
    list2 = [0,0,0,0,]
    list3 = []
    list4 = [-1, -2, -3, -4]
    list5 = [-1, 2, -3, 4]

    if (sum_of_list(list1)) != 15:
        print "sum of list failed for 4 positive numbers"
    if (sum_of_list(list2)) != 0:
        print "sum of list failed for 4 zeroes"

    if (sum_of_list(list4)) != -10:
        print "sum of list failed for 4 negative numbers"
    if (sum_of_list(list5)) != 2:
        print "sum of list failed for 2 negative and 2 positive numbers"

    try:
        sum_of_list(list3)
        print "Sum of list Failed for a Null list"
    except Exception as e:
        if e.message != "Sum Does not support an empty list":
            print 'Failed for summing the empty list '

def test_product_of_list():
    list1 = [1,2,3,4,5]
    list2 = [0,0,0,0,]
    list3 = []
    list4 = [-1, -2, -3, -4]
    list5 = [-1, 2, -3, 4]

    if (product_of_list(list1)) != 120:
        print "product of list failed for 4 positive numbers"
    if (product_of_list(list2)) != 0:
        print "product of list failed for 4 zeroes"
    if (product_of_list(list4)) != 24:
        print "product of list failed for 4 negative numbers"
    if (product_of_list(list5)) != 24:
        print "product of list failed for 2 negative and 2 positive numbers"

    try:
        product_of_list(list3)
        print "Failed: Multiplication Did not throw exception foran empty list"
    except Exception as ex:
        if "Multiplication does not support empty list." != ex.message:
            print "Failed: Multiplecation - Bad exception thrown"

def test_isPalindrome():
    if isPalindrome('radar') != True:
        print "Failed for the palindrome radar"
    if isPalindrome ('Rinisha') != False:
        print " Failed for a not palindrome string : Rinisha"
    if isPalindrome("Radar") != True :
        print "failed for a palindrome with an uppercase letter"
    if isPalindrome("") != "isPalindrome does not support empty string.":
        print "Failed: incorrect "



def test_reverse():
    if reverse('radar') != 'radar':
        print " reverse Failed for the string radar"
    if reverse ('Rinisha') != 'ahsiniR':
        print " reversee Failed for a string : Rinisha"
    if reverse("Radar") != "radaR" :
        print " revers failed for Radar uppercase r"
    if reverse(" ") != "":
        print " reverse failed for an empty string"

def test_member():
    list1 = [2,4,1,6]
    list2 = [2,6, 1,7]
    list3 = []
    if isMember(list1,9) != False:
        print " member failed for a false statement"
    if isMember(list2, 7) != True:
        print " member failed for a true statement"
    if isMember(list3, 7) != "isMember does not support empty list." :
        print " member failed for an empty statement"


def test_overlapping():
    if isOverlapping([8,1,8,2,4,7],[3,1,5,71, 4]) != True:
        print"  Overlapping failed for a rue statement"
    if isOverlapping([8,1,8,2,4,7], [24,63,28]) != False:
        print "Overlapping failed for a false statement"
    if isOverlapping([], []) != False:
        print " Overlapping failed for empty statements "
    if isOverlapping([], [24,63,28]) != False:
        print "Overlapping failed for one empty statement"

def test_generate_n_cars():
    if generate_n_chars(7,'9') != '9999999':
        print " generating Chars Failed where character is an integer"
    if generate_n_chars(7,'x') != 'xxxxxxx':
        print "generating chars failed when x was the character"
    if generate_n_chars(0,0) != '':
        print "generating chars failed for zeroes"

def all_tests():
    test_max()
    test_max_of_three()
    test_find_length_of_string()
    test_vowel_or_consonant()
    test_translate()
    test_sum_of_list()
    test_product_of_list()
    test_isPalindrome()
    test_reverse()
    test_member()
    test_overlapping()
    test_generate_n_cars()



all_tests()