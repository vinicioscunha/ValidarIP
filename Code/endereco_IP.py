def fn_VerifyIP(str_wordp):
    str_brokenWord = str_wordp.split('.')
    if len(str_brokenWord) != 4:
        return "Inválido"
    for int_j in str_brokenWord:
        if not int_j.isdigit():
            return "Inválido"
        int_i = int(int_j)
        if int_i < 0 or int_i > 255:
            return "Inválido"
    return "Válido"    
