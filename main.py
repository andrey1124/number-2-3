lst = [2,4,6,7,1]
print(5  in [2,3,5]) #true- потому что есть
print(5 not in [2,3,5])

print([2,4] + [5,3])
print([2,3]* 3)
print([2,3,7][0])
print(len(lst))
print(max(lst))
print(min(lst))
print(sum(lst))
print(lst.index(7))
print(lst.count(7))
print(lst.append(99))

del lst[0] #удалить под индексом
print(lst)

lst.clear() #полностьью очистить
print(lst)

newlist = lst.copy()  #скопировать список
print("новый список",newlist)
print("старый список", lst)