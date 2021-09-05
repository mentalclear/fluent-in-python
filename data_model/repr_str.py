# https://stackoverflow.com/questions/1436703/what-is-the-difference-between-str-and-repr

class Sic(object):
    def __repr__(object):
        return 'foo'

print(str(Sic()))
print(repr(Sic()))


class Sig(object):
    def __str__(object):
        return 'foo'

print(str(Sig()))
print(repr(Sig()))

