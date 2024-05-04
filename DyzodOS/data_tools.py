def GetDataType(Inp, OutputType):
    """
    Converts input to the specified output type.

    Parameters:
    - Inp: Input string or bytes to be converted.
    - OutputType: Type of output desired ('string' or 'bytes').

    Returns:
    - Converted input of the specified output type.
    """
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