def validate(username, password):
    if ('||' in username or '||' in password or '//' in username or '//' in password):
        return 'Wrong username or password!'
    validator = Validator()
    return validator.login(username, password)
