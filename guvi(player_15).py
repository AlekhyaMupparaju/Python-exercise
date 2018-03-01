import collections
s=raw_input()
results = collections.Counter(s)
print max(results,key=results.get)
