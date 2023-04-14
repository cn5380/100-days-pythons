"""
迭代工具模块
"""


import itertools

# 产生ABCD的全排列
for i in itertools.permutations("ABCD"):
    # print(i)
    pass

# 产生ABCDE的五选三组合
for i in itertools.combinations("ABCDE", 3):
    # print(i)
    pass
# 产生ABCD的123的笛卡尔积
for i in itertools.product("ABCD", "123"):
    print(i)

# 产生ABC的无限循环序列
for i in itertools.cycle(("A", "B", "C")):
    print(i)
