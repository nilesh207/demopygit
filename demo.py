pos = 0
def search(list, n):
  l = 0
  u = len(list)-1
  while l <= u:
    mid = (l + u)//2
    if list[mid] == n:
      globals()['pos'] = mid
      return True
    else:
        if list[mid] < n:
             l = mid + 1
        else:
             u = mid - 1
             
list = [11,22,33,44,55,66,77,88,99]
n = 77
if search(list, n):
  print("Found at ", pos)
else:
  print("Not Found")
