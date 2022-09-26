def genetate_ints(N):
    for i in range(N):
        yield i

def fuc1():
	pass

# @html_tag("h1")
# def do_some():
#     return

# def just_func():
#     print("in exec()")
#     return

if __name__ == "__main__":
    a,b,c,d = genetate_ints(4)
    print(a,b,c,d)


    # print(just_func())
