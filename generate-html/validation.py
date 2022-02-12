def valid_index(raw_input, length):
    try:
        index = int(raw_input)
        if index > 0 and index <= length:
            return True
        print("invalid index")
        return False
    except:
        print("that isn't a number, you goose")
        return False
