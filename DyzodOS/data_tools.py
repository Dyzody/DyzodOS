#Takes in an Input Value and either converts it to string or bytes
def GetDataType(Inp, OutputType):
    if OutputType == 'string':
        if isinstance(Inp, bytes):
            result = Inp.decode()
        elif isinstance(Inp, str):
            result = Inp
        else:
            raise ValueError("Input must be a string or bytes")
    elif OutputType == 'bytes':
        if isinstance(Inp, str):
            result = Inp.encode()
        elif isinstance(Inp, bytes):
            result = Inp
        else:
            raise ValueError("Input must be a string or bytes")
    else:
        raise ValueError("OutputType must be 'string' or 'bytes'")
    return result