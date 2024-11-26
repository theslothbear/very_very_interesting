def perevod(n: float, base: int) -> str:
  length = len(list(str(n).split('.'))[1])
  drob = float(f"%.{length}f" % (n - int(n)))
  res, ost = '', []
  while drob:
    new = float(f"%.{length}f" % (drob*base))
    drob = new - int(new)
    res+=str(int(new))
    if drob in ost:
      return perevod_int(int(n), base) + '.' + res[:ost.index(drob)+1] + '(' + res[ost.index(drob)+1:] + ')'
    ost.append(drob)
  return perevod_int(int(n), base) + '.' + res

def perevod_int(n: int, base: int) -> str:
  res=''
  while n:
    res+=str(n % base)
    n//=base
  res+=str(n)
  return [res[-1::-1], res[-1::-1].lstrip('0')][int(len(res) > 1)]


n = float(input())
print(perevod(n, 6))
