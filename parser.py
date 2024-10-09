from tokens import *

tokens = []
cur = 0

class NodeFun:
    def __init__(self, name, args, returns):
        self.name = name
        self.args = args
        self.returns = returns

    def __str__(self):
        ret = f"Function \"{self.name}\""
        ret += f"\n  args: "
        for arg in self.args:
            ret += f"{arg}, "
        ret += f"\n  returns: {self.returns}"
        return ret

class NodeField:
    def __init__(self, name, type):
        self.name = name
        self.type = type

    def __str__(self):
        return f"Field {self.name}: {self.type}"
    
def expect(*args):
    global tokens
    global cur
    found = False
    for arg in args:
        if tokens[cur].type == arg:
            found = True

    if found == False:
        err = token_type2str(args[0])
        for i in range(1, args.count()):
            err += " or " + token_type2str(args[i])
        err += " but got " + token_type2str(tokens[cur].type)

    return tokens[cur]

def consume(*args):
    global tokens
    global cur
    found = False
    for arg in args:
        if tokens[cur].type == arg:
            found = True

    if found == False:
        err = token_type2str(args[0])
        for i in range(1, args.count()):
            err += " or " + token_type2str(args[i])
        err += " but got " + token_type2str(tokens[cur].type)

    cur+=1
    return tokens[cur-1]
        

def parse_fun():
    consume(TOK_FUN)
    name = consume(TOK_IDENT).value
    args = []
    returns = []
    consume(TOK_LPAREN)
    if expect(TOK_RPAREN, TOK_IDENT).type == TOK_IDENT:
        while(True):
            arg_name = consume(TOK_IDENT).value
            consume(TOK_COLON)
            arg_type = consume(TOK_IDENT).value
            args.append(NodeField(arg_name, arg_type))
            if expect(TOK_RPAREN, TOK_IDENT).type == TOK_RPAREN:
                break
    
    consume(TOK_RPAREN)
    node = NodeFun(name, args, returns)
    print(node)
    

def parse(ttokens):
    global tokens
    tokens = ttokens
    parse_fun()