#Concatenation: Combining two or more strings into one.
greeting = "Hello"
name = "Alice"
print(greeting + " " + name)  

#Repetition: Repeating a string multiple times.
print("Hello! " * 3) 

#Slicing: Extracting a portion of a string.
print("Hello, World!"[7:12])  

#Escape Characters: Using special characters like newline (\n) and tab (\t).
print("Line 1\nLine 2\n\tIndented Line")

#String Length: Using the len() function to find the length of a string.
print(len("Hello, Alice!"))  

#Indexing: Accessing individual characters in a string (starting from 0).
print("Hello"[0])  

#Negative Indexing: Accessing characters from the end of the string.
print("Hello"[-1]) 

#String Comparison: Comparing strings using comparison operators.
print("apple" == "apple")  

#upper(): Converts all characters to uppercase.
message = "hello, world"
print(message.upper())  

#lower(): Converts all characters to lowercase.
message = "HELLO, WORLD"
print(message.lower())  

#strip(): Removes leading and trailing whitespace.
message = "   Hello, World!   "
print(message.strip())  
#replace(): Replaces one substring with another.
message = "Hello, World!"
print(message.replace("World", "Alice"))  

#find(): Finds the index of the first occurrence of a substring.
message = "Hello, World!"
print(message.find("World"))  

#split(): Splits a string into a list(Array) based on a delimiter.
message = "apple,banana,cherry"
print(message.split(","))  

