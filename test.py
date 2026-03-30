def leet_translate():
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
    magic_array = []
    for i in range(3):
        try:
            x = int(input('Enter number ' + str(i+1) + ': '))
        except ValueError:
            print("That wasn't a valid interger")
        magic_array.append(x)
        
    print('The answer is ' + str(max(magic_array)))
      
def magic_numb():
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