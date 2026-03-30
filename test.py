def leet_translate1():
    # use a dictionary to decode the leet code
    text = input('Enter the code: ')
    leet_decode = {'@': 'a', '4': 'a', '8': 'b', '3': 'e', '1': 'l', '0': 'o', '$': 's', '5': 's', '7': 't', '+': 't'}
    
    for i in text:
        if i in leet_decode:
            text = text.replace(i, leet_decode[i])
            
    print(text)

def leet_translate():
    # use case statements to decode the leet code instead of using a dictionary
    text = input('Enter the code: ')
    leet_decode = ''
    
    for i in text:
        if i == '@' or i == '4':
            leet_decode += 'a'
        elif i == '8':
            leet_decode += 'b'
        elif i == '3':
            leet_decode += 'e'
        elif i == '1':
            leet_decode += 'l'
        elif i == '0':
            leet_decode += 'o'
        elif i == '$' or i == '5':
            leet_decode += 's'
        elif i == '7' or i == '+':
            leet_decode += 't'
        else:
            leet_decode += i
            
    print(leet_decode)
  
def magic_numb1():
    # using an array to store the numbers and then using the built in max function to find the highest number
    magic_array = []
    for i in range(3):
        try:
            x = int(input('Enter number ' + str(i+1) + ': '))
        except ValueError:
            print("That wasn't a valid interger")
        magic_array.append(x)
        
    print('The answer is ' + str(max(magic_array)))
      
def magic_numb():
    # using a variable to store the highest number instead of an array
    magic_numb = 0
    for i in range(3):
        try:
            x = int(input('Enter number ' + str(i+1) + ': '))
        except ValueError:
            print("That wasn't a valid interger")
        if magic_numb < x: magic_numb = x
        
    print('The answer is ' + str(magic_numb))

def main():
    # magic_numb()
    leet_translate()

if __name__ == "__main__":
    main()