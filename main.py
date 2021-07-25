


print('3 challenges\n1-Thousand Separators\n2-Palindrome\n3-Leap Year')
input('Press Enter to start')



def format_number(n):
    print(f"{n:,}")

print('1 - Thousand Separator')
num = int(input('Enter Number: '))
format_number(num)
print()
print('++++++++++++++++\n')

print('2 - Palindrome')
def pal(a):
  ar = a[::-1]
  if a == ar:
    print('Yep, palindrome!')
  else:
    print('Not a palindrome!')
a = input('Enter a word: ').lower()
aj = a.replace(" ", "")
# print(aj)
pal(aj)

print()
print('++++++++++++++++\n')

def leap(year):
  if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
    print('It is a leap year')
  else:
    print('It is NOT a leap year!')

print('3 - Check Leap Year')
year = int(input('Enter a year: '))
leap(year)