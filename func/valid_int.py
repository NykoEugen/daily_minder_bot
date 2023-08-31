def valid_int(*args):
    for item in args:
        try:
            valid_val = int(item)
            return valid_val
        except TypeError as e:
            print(f"Incorrect data")
            return False
