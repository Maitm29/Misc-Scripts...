import sys 

def decrypt(k,cipher):
            plaintext = ''

            for each in cipher:
                        p = (ord(each)-k) % 256      //for utf-8 =256,ascii=126,text=26

                        if p < 32:
                                    p+=95

                        plaintext += chr(p)

            print plaintext

def main(argv):
            c = open("c://xxx.bin","rb")             //to read fron deasktop file (bin/txt)..
            cipher = c.read()                        //for string: cipher = raw_input("your string")

            for i in range(1,95,1):
                        decrypt(i,cipher)

if __name__ == "__main__":
            main(sys.argv[1:])
