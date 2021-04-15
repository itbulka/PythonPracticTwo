a = 'АаБбВвГгДдЕеЖжЗзИиЙйКкЛлМмНнОоПпРрСсТтУуФфХхЦцЧчШшЩщЪъЫыЬьЭэЮюЯя'
b = '1234567890@#–—$_&-+()/*":;!?,.~`|•√π÷×¶∆£¢€¥^°={}\%©®™✓[]<> '
n, s = int(input()), str(input())
for i in range(len(s)):
    for j in range(len(a)):
        if s[i] == a[j]:
            j += n + n
            if j > 64:
                j = j - 64
                print(a[j], end='')
            else:
                print(a[j], end='')
    else:      
        if s[i] in b:
            print(s[i], end='')
