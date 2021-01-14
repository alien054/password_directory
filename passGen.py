import hashlib as encoder
import stdiomask as secret


special_chars = list(range(33,48)) + list(range(58,65)) + list(range(123,127))

def encrypt(site,email,key):
    hash_text = site+email+key
    
    encoded_text = encoder.sha256(hash_text.encode()).hexdigest()[:10]
    encoded_list = list(encoded_text)
    
    up   = sum(map(ord,site)) % 10
    num  = abs(sum(map(ord,email)) % 10 - up)
    
    if up == num:
        num = (num + 1)%10
    
    spc  = (sum(map(ord,site+email)) + up) % 10
    
    if spc == up:
        spc = (spc + 1) %10
    if spc == num:
        spc = (spc + 1) %10
    if spc == up:
        spc = (spc + 1) %10
        
    # print(up,num,spc)
    
    encoded_list[up]  = chr(ord(encoded_list[up])%26 + ord('A')).upper()
    encoded_list[num] = str(ord(encoded_list[num]) % 10)
    encoded_list[spc] = chr(special_chars[ord(encoded_list[spc])%26])
    
    encoded_text = "".join(encoded_list)
    
    return encoded_text



print("\n\tAll input should be in lower case\n")
print("\tEnter the name of the site you want a password for.\n\tFor www.facebook.com enter only facebook\n")
site  = input("Enter site name: ")
email = input("Enter your email: ")
print('''\n\tNow you have to enter a secrete code.\n\tThis can be same for all of your password.\n\tMost importantly you must enter the same secrete code for same site everytime.\n''')
    
while(True):    
    key   = secret.getpass("Enter a secrete code: ")
    print("\n\tPlease retype your secrete code")
    repkey   = secret.getpass("Re-type: ")

    if(key == repkey):
        print("Your Password is : {}".format(encrypt(site,email,key)))
        break
    else:
        print("\n\tSecret Code doesn't match.\n\t Try again")



