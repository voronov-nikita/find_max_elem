a = [353, 22, 222]
if len(a) == 0:
    print(None)
elif len(a) == 1:
    print(a[0])
else:
    max_elem = None
    prev_max_elem = None
    for elem in a:
        if max_elem is None or elem > max_elem:
            prev_max_elem = max_elem
            max_elem = elem
        elif prev_max_elem is None or elem > prev_max_elem:
            prev_max_elem = elem
print(prev_max_elem)
