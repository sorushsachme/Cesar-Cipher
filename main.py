 
 
 
 
 

def main ():
    SYMBOL = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    translate = ''
    
    while True:
        print('Welcome to Cesar Cipher.') 
        print('What you want?!((e)ncrypt , (d)ecrypt )')
        response_ed= input('> ')

        text = input("Enter text: ").upper()

        while True:
            if response_ed.capitalize().startswith('E'):
                key = input('Enter key!(between 0 - 25) :')
                for symbol in text:
                    if symbol in SYMBOL:
                        num = SYMBOL.find(symbol)
                        num = num + int(key)
                        if num >= len(SYMBOL):
                            num = num - len(SYMBOL)
                        elif num < 0 :
                            num = num + len(SYMBOL)
                        translate += SYMBOL[num]

                break
                
            elif response_ed.capitalize().startswith('D'):
                key = input('Enter key!(between 0 - 26) :')
                for symbol in text:
                    if symbol in SYMBOL:
                        num = SYMBOL.find(symbol)
                        num = num - int(key)
                        if num >= len(SYMBOL):
                            num = num - len(SYMBOL)
                        elif num < 0 :
                            num = num + len(SYMBOL)
                        translate += SYMBOL[num]
                break
            else:
                print("enter E or D")
                continue
        print(translate)
    
        
        
if __name__ == '__main__':
    main()