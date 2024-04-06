# List bersifat mutable, artinya elemen-elemen dalam list dapat diubah setelah dibuat.
#  Kita bisa menambah, menghapus, atau mengubah nilai elemen dalam list.


users = ['Dave', 'John', 'Sara']

data = ['Dave', 42, True]

emptylist = []

print("Dave" in data)

print(users[0])

#kedua dari belakang
print(users[-2])

#terakhir
print(users[-1])

#mencari no index suatu data
print(users.index('Sara'))

# [0:2] 
# angka 0 awalan dari index 
# angka 2 adalah jumlah data yg mulai dari index 0
print(users[0:2])

#jika hanya [1:] akan menampilkan semua data mulai dari index 1 
print(users[1:])

# -3 maksudnya index ke 0 karena hanya ada 3 data
# jika -2 maksudny index ke 1
print(users[-3:])

# fungsi len() menampilkan ada berapa data
print(len(data))


# menambahkan data ke list

# menggunakan append()
# menambah ke baris terakhir dan hanya bisa satu data

users.append('Elsa')
print(users)


#  menggunakan operator +=
users += ['Jason']
print(users)


# extend berfungsi memasukann banyak data dan list ,jika append hanya satu

users.extend(['Robert', 'Jimmy'])
print(users)

#dari list yg lain

#users.extend(data)
#print(users)



# insert() menambahkan data pada posisi yang kita inginkan

users.insert(0,'Bob')
print(users)

# menambahkan data di index ke 2 dan 2 data
users[2:2] = ['Eddie', 'Alex']
print(users)

# menambahkan data di index ke 2 dan akan sebelum index ke 2 data
users[1:3] = ['Robert', 'JP']
print(users)


# mengahapus sesuai isi
users.remove('Bob')
print(users)

#menghapus data paling akhir
users.pop() # data [True]
print(users)

# del berfungsi menghapus data sesuai index
del users[0]
print(users)


# del data 
# tidak bisa menghapus list menggunakan dek karena akan error
# daripada menghapus kita bisa mengosongkan saja dengan clear()

#del data
data.clear()
print(data)


# sort bisa terurutkan jika tipe datanya sama
users[1:2] = ['dave']
users.sort()
print(users)

# sort yg awal dari lowercase
users.sort(key=str.lower)
print(users)



nums =[4, 42, 78, 1, 5]

# membalikan urutan di dalam list
nums.reverse()
print(nums)

#descending
#nums.sort(reverse=True)
#print(nums)

#ascending
#nums.sort()
#print(nums)

# sorted tidak mengubah list original  dan membuar objek baru
print(sorted(nums, reverse=True))
print(nums)
print('--------------------------')

numscopy = nums.copy()
mynums = list(nums)
mycopy = nums[:]

print(numscopy)
print(mynums)
print(mycopy)
mycopy.sort()
print(mycopy)
print(nums)


print(type(nums))

mylist = list([1, 'Neil', True])
print(mylist)




