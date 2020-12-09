# Heaps algorithm using loops
def HeapsLoop(a):
  size = len(a)
  c = [0] * size

  i = 0
  print(a)
  while i < size:
    if c[i] < i:
      if i & 1:
        a[c[i]], a[i] = a[i], a[c[i]]
      else:
        a[0],a[i] = a[i],a[0]
      print(a,end='')
      print(" i = ", i, c)
      c[i] += 1
      i = 0
    else:
      c[i] = 0
      i += 1

# Heaps Algorithm using recursion
def HeapsRecursion(a, size):
    # base case
    if size == 1:
        # this is a permutation d       o something
        print(a)
        return
    # looping the indices of a over size
    for i in range(size):
        HeapsRecursion(a, size-1)
        # swap i and size-1 element if odd
        if size&1:
            a[i],a[size-1] = a[size-1],a[i]
        # swap 0 and size-1 if even
        else:
            a[0],a[size-1] = a[size-1],a[0]

print("Recursion")
HeapsRecursion([0,1,2,3],4)
print("Loop")
HeapsLoop([0,1,2,3])
