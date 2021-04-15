lst = list(input().split(':'))
lt = []
while lst != ['']:
    lt.append(lst)
    lst = list(input().split(':'))
c = list(input().split(';'))
for i in range(len(lt)):
    if c.count(lt[i][1]) != 0:
        print('To:', lt[i][0])
        m = lt[i][4].split(',')
        print(m[0] + ',' + ' ваш пароль слишком простой, смените его.')
