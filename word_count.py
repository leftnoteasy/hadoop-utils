import sys

if __name__=="__main__":
  d = {}
  for line in sys.stdin:
    line = line[:len(line)-1]
    if not d.__contains__(line):
      d[line] = 1
    else:
      d[line] = d[line] + 1

  for (k,v) in d.items():
    print k,"=",v
		
