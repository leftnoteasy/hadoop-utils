import sys

if __name__ == "__main__":
  last = None
  count = 0
  arr = []
  max = 0
  for line in sys.stdin:
    time = line[:line.rindex(":")]
    if last != time:
      if None != last:
        arr.append((last, count))
        if count > max:
          max = count
      last = time
      count = 0
    else:
      count = count + 1

  for (time, count) in arr:
    num = count * 50 / max
    print time,"=","+"*num,"|",count