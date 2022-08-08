# b=[]
# print(b,type(b)) # anything will be hold on squre brackets is called as "List".

# a=["hello",22.3]
# print(a,type(a))
# print(a[0],type(a[0]))
# print(a[1],type(a[1]))
# print(a[2]) # IndexError: list index out of range.

# p='hello'
# p[0]='h' # TypeError: 'str' object does not support item assignment.
# print(type(p))
# print(p[0])
# print(p[2])
# print(p[4])
# print(p[3])
# print(p[-1])
# print(p[5]) # IndexError: string index out of range

# d=None
# print(type(d))  # class is NoneType.

# b=[4,5.6,"love",None,True]
# print(b[0],type(b[0]))  # class "int"
# print(b[1],type(b[1]))  # class "float"
# print(b[2],type(b[2]))  # class "str"
# print(b[3],type(b[3]))  # class "None"
# print(b[4],type(b[4]))  # class "bool"
# print(b[5],type(b[5]))  # IndexError: list index out of range.

# f="hi"
# f[0]="H"  # TypeError: 'str' object does not support item assignment.

# a=[5,4.2,"hi"]
# a[0]=5.4
# a[1]="hello"
# a[2]=8
# a[-1]=54
# print(a)

# m=[3,32.5,"lokesh",[4,4.3]]
# print(m,type(m))
# print(m[0],type(m[0]))
# print(m[1],type(m[1]))
# print(m[2],type(m[2]))
# print(m[3],type(m[3]))
# print(m[3][0],type(m[3][0]))
# print(m[3][1],type(m[3][1]))

# n=[2,8.9,"sai",[23.4,'hi']]
# n[2]=54
# n[3][1]='lokesh'
# print(n,type(n))
# print(n[0],type(n[0]))
# print(n[1],type(n[1]))
# print(n[2],type(n[2]))
# print(n[3],type(n[3]))

# print(dir(list()))
# 11 methods :'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort'.

# a=[54,7.8,'pytho',[4,5]]
# a.append('lokesh')
# print(a)  # append is the method will add the element at end of the list.

# a=[54,7.8,'pytho',[4,5]]
# a.clear()
# print(a)  # clear is the method of list which clear all the elements in the square bracket.

# a=[54,7.8,'pytho',[4,5]]
# print(a)
# b=a.copy()
# print(b) # duplicate of "a". 

# a=[54,7.8,'pytho','']
# print(a.count(''))
# print(a.count(54))
# print(a.count(7.8))

# a=[1,3,5,7]
# b=[2,4,6,8]
# # a.extend(b)
# # print(a)
# b.extend(a)
# print(b)

# b='lokesh'
# print(b.index('e'))

# a=[54,7.8,'pytho',[4,5]]
# print(a.index(7.8))
# print(a.index(54))
# print(a.index(4))
# # print(a.index(5))
# print(a.rindex('pytho')) # AttributeError: 'list' object has no attribute 'rindex'. Did you mean: 'index'?

# c=[1,3,5,3.4,2,6,8]
# c.insert(2, 'ho')
# c.insert(1, 879)
# c.insert(0,34.43 )
# print(c)

# a=['hi','hello','python','world']
# a.pop(0)
# a.pop()
# a.pop(2)
# a.pop(1,2,3)
# print(a)

# f=[4,8,7,20,10,'hi',36]
# f.remove(20)
# print(f)

# n=[1,2,3,4,5]
# print(n[::-1])
# n.reverse()
# print(n)

# g=[122,45,983,34,55,66,77,89,100]
# g.sort()
# print(g)
# g.sort(reverse=False)
# print(g)
# g.sort(reverse=True)
# print(g)

# h=[3.4,2.6,1.8,5.7,3.8,9.6,8.3,9]
# h.sort()
# print(h)

# r=['HF','DF','EF','DC','WS','QA','FD','VO','ML','AI']
# r.sort()
# print(r)