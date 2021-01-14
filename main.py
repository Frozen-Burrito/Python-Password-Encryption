import random
import string

def gen_salt (size = 10):
  chars = string.ascii_letters + string.punctuation
  return ''.join(random.choice(chars) for x in range(size))

def hash_pwd (string, salt=None):
  msg = []

  if salt == None:
    salt = gen_salt(20)

  for i, c in enumerate(string):
    char_s = ord(salt[len(string) - i])
    char_string = ord(c)
    msg.append(chr((char_s + char_string) % 127))

  res = ''.join(msg)

  return (res + salt, salt)

if __name__ == '__main__':
  print('Password')
  message = input('> ')

  hashed_password, salt = hash_pwd(message)
  print(f'Encryption: {hashed_password}')

  print('Enter password again')
  second_password = input('> ')

  if (hash_pwd(second_password, salt)[0] == hashed_password):
    print('Passwords match! Great!')
  else: 
    print('Passwords don\'t match.')