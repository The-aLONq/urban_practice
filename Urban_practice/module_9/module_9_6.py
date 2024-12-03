def all_variants(text):
    n = len(text)
    count = 1
    while count <= n:
        index = 0
        while index <= n - count:
            yield text[index:index+count]
            index += 1
        count += 1

a = all_variants("abc")
for i in a:
    print(i)