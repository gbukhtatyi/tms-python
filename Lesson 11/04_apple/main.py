class RealString:
    def __init__(self, val):
        self.__val = val

    def __len__(self):
        return len(self.__val)

    def __eq__(self, other):
        return len(self.__val) == len(other)

    def __gt__(self, other):
        return len(self.__val) > len(other)

    def __lt__(self, other):
        return len(self.__val) < len(other)

    def __ge__(self, other):
        return self.__gt__(other) or self.__eq__(other)

    def __le__(self, other):
        return self.__lt__(other) or self.__eq__(other)


s1 = RealString('Apple')
s2 = RealString('Яблоко')

print(s1 == s2)
print(s1 > s2)
print(s1 >= s2)
print(s1 < s2)
print(s1 <= s2)
