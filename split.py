def email_func(valstr):
    if '@' in valstr:
        for mail in valstr.split(" "):
            if '@' in mail:
                return mail

    else:
        return False


email_func("this is first abhinav@cloudxlab.com and this is second sandeep@cloudxlab.com") 
