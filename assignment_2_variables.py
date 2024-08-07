# 1. Simple Message
msg = "I am Ali"
print(msg)

# 2. Simple Messages
msg = "I am Ali"
print(msg)
msg = 'I am Ali Hassan Malik'
print('Updated Message:',msg)

# 3. Personal Message
msg_to = 'Eric'
print("Hello",msg_to,", would you like to learn some Python today?")

# 4. Name Case
name = "ali"
print('This is lower case:',name.lower())
print('This is upper case:',name.upper())
print('This is title:',name.title())

# 5. Famous Quote
qoute = '''"Think a hundred times before you take a decision, but once that decision is taken, stand by it as one man."'''
print('Muhammad Ali Jinnah once said,',qoute)

qoute = "I do not believe in taking the right decision, I take a decision and make it right."
print(f'Muhammad Ali Jinnah once said, "{qoute}"')

# 6. Famous Quote 2
famous_person = 'Muhammad Ali Jinnah'
message       = 'With faith, discipline and selfless devotion to duty, there is nothing worthwhile that you cannot achieve.'
print(famous_person,'said:',message)

#7. Stripping Names
person_name = '\t\n        Imran \t           Khan               \n'
print('Simple Text:',person_name)
print('lstrip:',person_name.lstrip())
print('rstrip:',person_name.rstrip())
print('strip:',person_name.strip())

#8. Variable Sum
x = 5
y = 10 
z = 15
print ("----------Variable Sum----------")
print('Sum of three variables:',x+y+z)

#9.Variable Swap
x=50
y=100
print ("----------Before Swapping----------")
print('value of x:',x)
print('value of y:',y)

temp = x
x = y
y = temp
print("----------After Swapping----------")
print('value of x:',x)
print('value of y:',y)

#10. Favorite Color
fav_col = 'Black'
print("----------Favorite Color----------")
print(fav_col)
new_col = fav_col
print(new_col)

#11. Changing Pet Name
pet_name = 'Buddy'
pet_name = 'Max'
print("----------Pet Name----------")
print(pet_name)

# 12. Observing Name Error
Sunshine = "here"
print("----------Observing Name Error----------")
print(Sunshine)
#print(Sunsine) This is error

#13. Reassigning Score
score = 100
print("----------Reassigning Score----------")
print(score)
score = 125
print('Reassiging:',score)

#14. City Name
city_name:str = 'Lahore'
print("----------City Name----------")
print(city_name)
 
#15. Title Case Text
text = "python programming"
print("----------15. Title Case Text----------")
print(text.title())

#16. Lowercase Conversion
sample_text = 'HeLLo I aM HeRE'
print("----------16. Lowercase Conversion----------")
print(sample_text.lower())

# 17. Uppercase Conversion
print("---------- 17. Uppercase Conversion----------")
print(sample_text.upper())

# 18. Current Temperature
temperature = 25
print("---------- 18. Current Temperature ----------")
print(f"The current temperature is {temperature} degrees.")

#19. Printing a Poem
poem = '''Nature's first green is gold,
Her hardest hue to hold.
Her early leaf's a flower;
But only so an hour.'''
print("---------- 19. Printing a Poem ----------")
print(poem)
