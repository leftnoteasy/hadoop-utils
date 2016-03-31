import sys

if __name__ == "__main__":
  failed_tasks = set()
  for line in open(sys.argv[1]):
	failed_tasks.add(line.strip())

  for line in sys.stdin:
     if line.__contains__("using containerId"):
        idx = line.find("attempt_")
	task_id = line[idx:line.find("]", idx)]
        if failed_tasks.__contains__(task_id):
          print line
