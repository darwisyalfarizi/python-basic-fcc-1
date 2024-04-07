# Diberikan sebuah bilangan bulat, balikkan digit-digitnya.
# Contoh:
# Input: x = 123
# Output: 321


# brute force

def reverse_integer(x: int) -> int:
    # Mengubah bilangan bulat menjadi string untuk memudahkan pengelolaan digit-digitnya
    str_x = str(x)
    
    # Jika bilangan negatif, potong tanda negatif dan reverse sisa stringnya
    if str_x[0] == '-':
        reversed_str = '-' + str_x[:0:-1]
    else:
        reversed_str = str_x[::-1]
    
    # Coba konversi string menjadi integer, jika gagal (misalnya jika hasilnya melebihi batas bilangan bulat), kembalikan 0
    try:
        reversed_x = int(reversed_str)
    except ValueError:
        return 0
    
    # Periksa batas atas dan bawah
    if reversed_x < -2**31 or reversed_x > 2**31 - 1:
        return 0
    
    return reversed_x

# Contoh penggunaan
x = 1242343
print("Input:", x)
print("Output:", reverse_integer(x))
