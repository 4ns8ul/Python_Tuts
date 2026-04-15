
1. Counter: `collections.Counter()`
- A  counter is a container that stores elements as dictonary keys, and their counts are stored as dictonary values
- `{keys:values(counts)}`
2. Default Dictonary: `defaultdict(list)`
- The defaultdict tool is a container in collections class in Python. It's similar to usual dictoanry container except that a defualtdict will have a default value if the key has not been set yet. 
- Eg:

        from collections import defaultdict
        d = defaultdict(list)
        d['python'].append("awesome")
        d['something-else'].append("not relevant")
        d['python'].append("language")
        for i in d.items():
            print i