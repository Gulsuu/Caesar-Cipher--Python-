def caesar(text, shift, direction):
  if direction=="encode":
    finaltext=""
    for i in text:
      if i in alphabet: #alphabet de olmayan boşluk,sembol olduğu gibi yazdır.
        indexno=alphabet.index(i) #list.index() bi listedeki itemin index nosunu buldurur.
        indexno+=shift
        newindexno=indexno
        newletter=alphabet[newindexno]
        finaltext+=newletter
      else:
        finaltext+=i
  elif direction=="decode":
    finaltext=""
    for i in text:
      if i in alphabet:
        indexno=alphabet.index(i)
        indexno-=shift
        newindexno=indexno
        newletter=alphabet[newindexno]
        finaltext+=newletter
      else:
        finaltext+=i
  print(f"The {direction}d text is {finaltext}.") 

#program okumaya buradan başlar fonksiyon çağırılınca gelir. 
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
from cipherart import logo
print(logo)
endgame=False
while endgame==False:
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))
  shift=shift%26 #list index out of range vermemesi için büyük sayıda
  caesar(text,shift,direction)#fonksiyon çağırıldı def kısmını okur bilgisayar.
  again=input("Do you want to restart the game?Yes or No.\n").lower()
  if again=="no":
    endgame=True
    print("The end.")
