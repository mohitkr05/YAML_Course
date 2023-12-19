# Data Terminology

| Terminology | Definition | 
| ---| ---|
| Collection |  A general term for a data structure that groups multiple elements. In YAML, collections can be mappings or sequences. |
| Mapping | A collection of key-value pairs, where each key uniquely identifies a corresponding value. In YAML, mappings can be represented as block or flow mappings. |
| Block Collection | A YAML data structure using indentation to define scope and starting each entry on a new line. Block collections can be sequences (lists) or mappings (dictionaries). |
| Flow Collection | A YAML data structure using explicit indicators (square brackets for sequences, curly braces for mappings) to define scope, instead of indentation. | 
| Block Mapping | A block mapping is a YAML data structure that uses indentation to denote scope and begins each entry on its own line. |
| Flow Mapping | A flow mapping is a YAML data structure that uses indentation to denote scope and begins each entry on its own line. |
| Alias | A reference to a previously defined anchor within the same YAML document. It allows reuse of complex data structures to avoid redundancy.  | 
| Anchor | A unique identifier assigned to a specific YAML data structure within the document. Used in conjunction with aliases for referencing and reusing complex data. |
| Stream | A sequence of multiple YAML documents within the same file. Each document is separated by document markers (---). | 
| Document | A single unit of information in a YAML file, consisting of a collection of data with its own structure and meaning. Documents can be separated by markers or standalone within a file. | 
| Tags | hese are special identifiers prefixed with an exclamation mark ("!") and used to explicitly inform the YAML parser about the internal data type of a scalar value. | 
| Boolean | A boolean value that can be either true or false, represented by `bool` |
| Comment | A line of text that is ignored by the YAML parser. |
| Double-quoted scalar | A scalar value that is enclosed in double quotes. |
| Dumping | The process of converting a YAML document into a human-readable format. |
| Folded scalar style | A scalar value that is folded into multiple lines. |
| Representation graph | A graphical representation of a YAML document. |
| Single-quoted scalar | A scalar value that is enclosed in single quotes. |
| Tagged scalar | A scalar value that is tagged with a tag. |




## Collections

- Collections are mappings and sequences. 
  - Mappings are like dictionaries where you have unique keys associated with values. 
  - Sequences are like lists where you have ordered entries.

### block collection

A block collection is a YAML data structure that uses indentation to denote scope and begins each entry on its own line. Block sequences indicate each entry with a dash and space (“ - ”). Mappings use a colon and space (“ : ”) to mark each key/value pair.

For example, this is a block sequence:
```yaml
- item 1
- item 2
- item 3
```

- This is a simple block mapping:

```yaml
name: John Doe
age: 30
occupation: Software engineer
```

- Mapping with nested mappings

```yaml
address:
  street: 123 Main Street
  city: New York
  state: NY
  zip: 10001
```

- Mapping with Favourite values
```yaml
favorite_fruits:
  - apple
  - banana
  - orange
```


### flow collection


- List of numbers

```yaml
[1, 2, 3, 4, 5]
```

- List of strings

```yaml
["apple", "banana", "cherry"]
```

- Key-value pair

```yaml
{name: "Alice", age: 30}
```

```yaml
{"{name: Alice, age: 30}": personal information}
```

- Mapping of mappings

```yaml
{address: {city: "New York", country: "USA"}}
```

- Mapping with Flow-style Key

```yaml
? { name: Alice, age: 30 } : information about Alice
```
