
def hello_world():
    print("hello world")


hello_world()

def sum(num1=0, num2=0):
    
    if(type(num1) is not int or type(num2) is not int):
        return
    return num1+num2

total = sum(2, 3)
print(total)


# /*args  adalah parameter khusus yang digunakan
#  dalam definisi fungsi untuk menangani jumlah argumen yang tidak terbatas

def multiple_items(*args):
    print(args)
    print(type(args))


multiple_items("dave", "john", "sara")

# /**kwargs (keyword arguments)
def mult_named_items(**kwargs):
    print(kwargs)
    print(type(kwargs))


mult_named_items(first = "dave", last = "john")
