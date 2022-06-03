email = input("Enter Your email:").strip()
username = email[:email.index('@')]
domain_name = email[email.index("@")+1:]
format_=f"your username is {username} and your domain name is {domain_name}"
print(format_)