#Tuple bersifat immutable, artinya setelah dibuat, elemen-elemen dalam tuple tidak dapat diubah. 
#Kita tidak bisa menambah, menghapus, atau mengubah nilai elemen dalam tuple.

# jika mau menambhkan data tuple dengan konstruktor harus
# benar tuple(('jjj', 'aa', 'www'))
# salah tuple('jjj', 'aa', 'www')
mytuple = tuple(('Dave', 24, True))

anothertuple  = (1, 4, 2, 8, 2, 2)

print(mytuple)
print(type(mytuple))
print(type(anothertuple))


#jika ingin mengubah data tuple kita harus alihkan dahulu ke list

newlist = list(mytuple)
newlist.append('Neil')
newtuple = tuple(newlist)
print(newtuple)



#unpack tuple

(one, two, *hey) = anothertuple

print(one)
print(two)
print(hey)

print(anothertuple.count(2))