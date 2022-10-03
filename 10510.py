s = '1:men 2:kind 90:number 0:sun 34:book 56:mountain 87:wood 54:car 3:island 88:power 7:box 17:star 101:ice'

# a = []
# dct = {}
# dct2 = {}
# for i in s.split():
#      a.append(i.split(':'))
# for i in a:
#      dct2 = dict(a)

result = {int(k): v for k, v in [a.split(':') for a in s.split()]}
