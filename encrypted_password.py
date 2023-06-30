username=input("Please enter your username: ")
password=input("Please enter your password: ")

password_length=len(password)
count=print (type(password_length))
encrypted_password_length='*' * password_length


print(f'Hi {username} your password {password} is {password_length} characters long and the encrypted value is: {encrypted_password_length} ')