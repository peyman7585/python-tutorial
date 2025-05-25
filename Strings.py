
import re

String1 = "Hello"
String2 = "Joliya"

greeting_message = String1 + "," + String2 + "!"
# print(greeting_message)

repeat_massage = "Python!" * 3

# print(repeat_massage)

original_string = "HeLLo wOrd"

uppercase_string = original_string.upper()
# print("Uppercase String: ", uppercase_string)
lowercase_string = original_string.lower()
# print("Lowercase String: ", lowercase_string)

sentence = "Python is a powerful language"

split_sentence = sentence.split()
# print("Split Sentence: ", split_sentence)


name = "John"
age = 23
intro = "My name is {} and im {} years old".format(name, age)
print(intro)

pi = 3.1434333524974

formatted_pi = "Pi rounded to 2 decimal places is {:.2f}".format(pi)
print(formatted_pi)

number = 43

padded_number = "The number is {:05d}".format(number)
print(padded_number)


text = "The rain is in Spain"

match = re.search(r"rain", text)

if match:
    print("Match found:", match.group())
else:
    print("Not founded")

text2 = "The rain in Spain stays mainly in the plain"
matches = re.findall(r"ain", text2)

print("Match found:", matches)

text3 = "The weather was rainy"
replaced = re.sub(r"rainy", "suny", text3)

print("Replaced text:",replaced)
