# YAML Cheat Sheet

### File Extensions

```
.yaml
.yml
```
A simple key-value pair:

```
key: value

```

A list:
```
- item1
- item2
- item3
```

A list of key-value pairs:
```
- key1: value1
  key2: value2
- key1: value3
  key2: value4
```
A dictionary (associative array) with multiple 
keys:
```
key1: value1
key2: value2
key3: value3
```

A dictionary with nested elements:
```
key1:
  subkey1: value1
  subkey2: value2
key2:
  subkey3: value3
  subkey4: value4
```

A dictionary with lists:
```
key1:
  - item1
  - item2
key2:
  - item3
  - item4
```

A dictionary with lists of dictionaries:
```
key1:
  - subkey1: value1
    subkey2: value2
  - subkey1: value3
    subkey2: value4
key2:
  - subkey3: value5
    subkey4: value6
  - subkey3: value7
    subkey4: value8
```
A dictionary with a mix of lists and dictionaries:
```
key1:
  - item1
  - subkey1: value1
    subkey2: value2
key2:
  - item2
  - subkey3: value3
    subkey4: value4
```
    
A multi-line string:
```
key: |
  This is a string
  that spans multiple
  lines.
```
A string with special characters:
```
key: "This string contains special characters: \t, \n, \r, \', \"."
```
