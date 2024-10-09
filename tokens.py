def iota():
    iota.count+=1
    return iota.count
iota.count = -1

TOK_FUN = iota()
TOK_LPAREN = iota()
TOK_RPAREN = iota()
TOK_COLON = iota()
TOK_STR = iota()
TOK_NUM = iota()
TOK_IDENT = iota()
TOK_COMMA = iota()
TOK_LCURLY = iota()
TOK_RCURLY = iota()
TOK_RETURN = iota()
TOK_MUL = iota()
TOK_SEMI = iota()
TOK_ASSIGN = iota()
TOK_LET = iota()

def token_type2str(type):
    translator = [
        "'fun'",
        "'('",
        "')'",
        "':'",
        "a string literal",
        "a numeric literal",
        "an identifier",
        "','",
        "'{'",
        "'}'",
        "'return'",
        "'*'",
        "';'",
        "'='",
        "'let'"
    ]
    return translator[type]
