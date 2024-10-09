from parser import parse
from tokens import *

KEYWORD_TABLE = [
    {"type": TOK_FUN, "word": "fun"},
    {"type": TOK_LPAREN, "word": "("},
    {"type": TOK_RPAREN, "word": ")"},
    {"type": TOK_COLON, "word": ":"},
    {"type": TOK_COMMA, "word": ","},
    {"type": TOK_LCURLY, "word": "{"},
    {"type": TOK_RCURLY, "word": "}"},
    {"type": TOK_RETURN, "word": "return"},
    {"type": TOK_MUL, "word": "*"},
    {"type": TOK_ASSIGN, "word": "="},
    {"type": TOK_SEMI, "word": ";"},
    {"type": TOK_LET, "word": "let"},
]

def strncmp(a: str, b, len):
    return a[:len] == b[:len]

def keyword_check(src, cur, tokens):
    for keyword in KEYWORD_TABLE:
        length = len(keyword["word"])
        if(strncmp(keyword["word"], src[cur:], length)):
            tokens.append(Token(keyword["type"], ""))
            return length

    return 0 

class Token:
    def __init__(self, type, value):
        self.type = type
        self.value = value

    def __str__(self):
        return f"{token_type2str(self.type)}        {self.value}"

def lex(src):
    num_lines = 0
    num_cols = 0
    cur = 0
    src += '\0'
    tokens = []
    while(src[cur] != '\0'):
        num_cols+=1
        if(src[cur] == '\n'):
            num_lines += 1
            num_cols = 0
            cur+=1
            continue
        if(src[cur] == ' '):
            cur+=1
            continue
        if(src[cur] == '/' and src[cur+1] == '/'):
            cur+=1
            while(src[cur] != '\0' and src[cur] != "\n"):
                cur+=1
            continue

        off = keyword_check(src, cur, tokens)
        if(off > 0):
            cur += off
            continue

        if(src[cur] == '"'):
            str = ""
            cur+=1
            while(src[cur] != '\0' and src[cur] != '"'):
                str += src[cur]
                cur+=1
            if(src[cur] == '\0'):
                raise Exception("Unterminated string literal at end of file")
            tokens.append(Token(TOK_STR, str))
            cur+=1
            continue

        if(src[cur].isdigit()):
            str = ""
            while(src[cur] != '\0' and src[cur].isdigit()):
                str += src[cur]
                cur+=1
            tokens.append(Token(TOK_NUM, str))
            continue
        
        if(src[cur].isidentifier()):
            str = ""
            while(src[cur] != '\0' and (src[cur].isidentifier() or src[cur].isdigit())):
                str += src[cur]
                cur+=1
            tokens.append(Token(TOK_IDENT, str))
            continue

        print("[Lexer] Fell trough all token checks " + src[cur])
        cur+=1
        continue

    return tokens
        
with open("main.w", "r") as fd:
    tokens = lex(fd.read())
    parse(tokens)

with open("out.wasm", "w") as fd:
    fd.write("yas")