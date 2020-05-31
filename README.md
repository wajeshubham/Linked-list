**OUTPUTS**

lst = LinkedList()


lst.insert(1)

lst.insert(2)

lst.insert(3)

lst.insert(4)

lst.insert(5)

lst.insert(6)

lst.insert(7)

lst.insert(8)

lst.insert(9)

lst.insert(10)

lst.insert(11)

lst.insert(12)

"""OUTPUT --> 12 -->11 -->10 -->9 -->8 -->7 -->6 -->5 -->4 -->3 -->2 -->1 -->"""



print(lst.length())  # OUTPUT --> 12


lst.insert_at_end(13)

lst.insert_at_end(14)

lst.insert_at_end(15)

"""OUTPUT --> 12 -->11 -->10 -->9 -->8 -->7 -->6 -->5 -->4 -->3 -->2 -->1 -->13 -->14 -->15 -->"""


lst.replace_at(7, "something")

"""OUTPUT --> 12 -->11 -->10 -->9 -->8 -->7 -->6 -->something -->4 -->3 -->2 -->1 -->13 -->14 -->15 -->"""


lst.insert_at(2, "before index 3")

"""OUTPUT --> 12 -->11 -->before index 3 -->10 -->9 -->8 -->7 -->6 -->something -->4 -->3 -->2 -->1 -->13 -->14 -->15 -->
"""


lst.remove_at(2)

"""OUTPUT --> 12 -->11 -->10 -->9 -->8 -->7 -->6 -->something -->4 -->3 -->2 -->1 -->13 -->14 -->15 -->"""


print(lst.index_of(10))  # OUTPUT --> 2


lst.remove_by_value(8)

""" OUTPUT --> 12 -->11 -->10 -->9 -->7 -->6 -->something -->4 -->3 -->2 -->1 -->13 -->14 -->15 -->
"""


print(lst.value_at(6))  # OUTPUT --> something


lst.reverse()

"""OUTPUT --> 15 -->14 -->13 -->1 -->2 -->3 -->4 -->something -->6 -->7 -->9 -->10 -->11 -->12 -->
"""


lst.print()
