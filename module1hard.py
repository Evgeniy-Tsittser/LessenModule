grades = [[5,3,3,5,4],[2,2,2,3],[4,5,5,2],[4,4,3],[5,5,5,4,5]]
students = {'Johnny','Bilbo','Steve','Khendrik','Aaron'}
my_list = list(students)
my_list_sort = sorted(my_list)
print(my_list_sort)
a = sum(grades[0])/len(grades[0])
b = sum(grades[1])/len(grades[1])
c = sum(grades[2])/len(grades[2])
d = sum(grades[3])/len(grades[3])
e = sum(grades[4])/len(grades[4])
sred_a = [a,b,c,d,e]
print(sred_a)
gr_book = dict(zip(my_list_sort,sred_a))
print(gr_book)