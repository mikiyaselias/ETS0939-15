# section-B
# string : 
it is a sequence of characters enclosed within quotes. It is one of the most commonly used data types and used to represent textual data.
strings can be enclosed in single quotes (''),double quote ("") or triple quote
conclusion : strings are versatile and essential for handling textual data in python program.
# string method 
there are many built in methods that are used to manipulate strings in python.
# str.lower() method
it is used to convert all uppercase letters in string to lowercase.it does not modify or change the form of the original stting but returns anew string with all characters in lowercase. this method only affects uppercase letters. lowercase letters and non alphabetic characters remain unchanged. 
# str .upper() method 
it is used to convert all lowercase letters in string to uppercase. this method also dose not modify the orginal string but returns a new string with all characters in uppercase. it only affects lowercase letters other characters remain the same. 
# str . title()
it is used to convert a string so that each word starts with an uppercase letter and the rest of the letters are in lowercase. simply it is used to capitallize the first letter of each word. it makes all other letters lower case even if the original text had a mixing casing.
# str.capitalize()
this string method is used for changing the first character of the string to uppercase and the rest to lowercase. here if the string starts with non alphabetic character it remains the same . this string method can be used for formatting names anad titles.
# str.swapcase()
this string method is used for swapping the case of all characters in the string . it changes the uppercase to lowercase and the lowecase to uppercase. here also the non alphabetic caharacters remains the same and it does not modify th original string.
# str.isupper()
this string method is used to check if the alphabets inside the string are all in uppercase.
it has a true and false return value.this method also ignors non alphabetic characters. when the alphabets inside the string are uppercase it returns true value .otherwise if the alphabets are lowercase it returns false value .
# str.islower()
this string method is used to check if the alphabets inside the string are all in lowercase. it has a true and false return value . this method also ignores non alphabetic characters. when the alphabets inside the string are lowercase it returns true value otherwise it returns false value.
# str.strip()
this string type is used for removing leading and trailing whitespaces or specified characters from the string. the whitespace refers to the invisible characters that creates empty space in the text. this method also does not modify the orginal characters.
# str.lstrip()
used for removing the leading whitespace or specified character from the string.
# str.rstrip()
used for removing the trailing whitespace or specified chracter fom the string.
# str.replace()
this method is used for replacing occurrance of a substring with another substring inside the string .  this string method is different from the others because it modifies the original string . this method is also case sensetive .
# str.split()
this method is used for dividing string into a list of substring based on a specified separator.
# str.join()
this method is the inverse of str.split(). it is used for making the list strings or iterable strings into single string by combininf them.
 # str.find() 
 this method is used for searching for a substring within a string and returns a lowest index where it is found . this string method is also case sensetive . if it does not found the substring it returns -1.
 # str.index()
 thid method is the same with str.find(). but it raises a value error when substring is not found rather than returning -1.