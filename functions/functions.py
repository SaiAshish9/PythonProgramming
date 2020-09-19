
def center(*args,sep=' -- ',end='\n',file=None,flush=False):
    text=""
    for arg in args:
        text+=str(arg) + sep
    left=(80-len(text))//2
    print(" "*left,text,end=end,sep=sep,flush=flush,file=file)

center("spam, spam, spam and spam")
center("spam, spam, spam and spam",3,4,"spam",sep=":")
# sep separator between arguments
print(1,2,sep="@")