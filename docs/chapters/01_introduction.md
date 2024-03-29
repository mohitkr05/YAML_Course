# Introduction

## What is YAML

YAML (YAML Ain't Markup Language) is a human-readable data serialization language. It is often used for configuration files and in applications where data is being stored or transmitted.

### References

- [Official website](https://yaml.org/)
- [YAML Specifications](https://github.com/yaml/yaml-spec)
- [YAML Grammar](https://github.com/yaml/yaml-grammar)
- [YAML test suite](https://github.com/yaml/yaml-test-suite)

## What is a data serialization language?

A data serialization language is a way of encoding data structures and objects so that they can be stored or transmitted efficiently. Serialization involves converting the data into a format that can be easily stored or transmitted, such as a text or binary file.

Serialization is often used when data needs to be persisted to a file or database, or when it needs to be transmitted over a network connection. Serialization languages provide a way to represent the data in a structured way that can be easily interpreted by other systems or applications.

There are many different data serialization languages, including JSON, XML, YAML, and Protocol Buffers. Each language has its own syntax and set of rules for encoding data, and different languages may be better suited for different use cases.


## YAML Goals

The design goals for YAML are, in decreasing priority:

 - YAML should be easily readable by humans.
 - YAML data should be portable between programming languages.
 - YAML should match the native data structures of dynamic languages.
 - YAML should have a consistent model to support generic tools.
 - YAML should support one-pass processing.
 - YAML should be expressive and extensible.
 - YAML should be easy to implement and use.


## Difference between YAML/JSON & XML

XML, JSON, and YAML are all data serialization languages, which means they are used to translate complex data structures into a format that can be easily stored and transmitted. Here are some key differences between these formats:

- Syntax: XML uses a tag-based syntax, with elements nested inside each other using start and end tags. JSON uses a key-value syntax, with keys and values separated by a colon and nested elements indicated using curly braces. YAML uses a combination of key-value pairs and lists, with a minimal syntax that relies on indentation to indicate nesting.

- Data types: XML and JSON support a similar set of data types, including strings, numbers, booleans, and null. YAML supports these types as well, but also includes additional types like dates and binary data.

- Compatibility: JSON is widely supported and is natively supported by many programming languages. XML is also widely supported, but may require additional libraries or tools to parse and generate documents. YAML has good support in some languages, but may have limited support in others.

- Readability: JSON and YAML are generally considered to be more readable than XML, as they use a more concise syntax and do not require the use of start and end tags.

- Use cases: XML is often used for storing and transmitting structured data, such as in web services and application configurations. JSON is commonly used for storing and transmitting data in web applications. YAML is often used for configuration files, as well as for storing and transmitting data in applications.

## Benefits of using YAML

- Easy to read and write: YAML is designed to be human-readable, so it is easy to write and understand. This is especially useful when working with configuration files.

- Supports multiple data types: YAML supports a variety of data types, including strings, numbers, boolean values, and null. This makes it a flexible choice for storing data.

- Supports nesting: YAML allows you to nest elements, which can be useful for organizing complex data structures.

- Language-agnostic: YAML is not tied to any particular programming language, so it can be used with a wide range of languages and tools.

- Compact syntax: YAML uses a minimal syntax, which means that it can be used to represent complex data structures in a compact and concise way.

- Portable: Since YAML is a text-based format, it is easy to share and transport data stored in YAML files.


## Challenges with YAML

- Syntax errors: YAML has a strict syntax, and any errors in the syntax can cause the document to be invalid. This can make it difficult to debug YAML documents, especially if they are large or complex.

- Limited support for certain data types: While YAML supports a wide range of data types, it does not support all data types that are available in programming languages. For example, YAML does not support functions or objects.

- Limited tooling: There are fewer tools available for working with YAML compared to other data serialization languages like JSON or XML. This can make it more difficult to find libraries or utilities to work with YAML in certain programming languages.

- Limited support for comments: YAML does not have a native syntax for adding comments to documents. While some YAML parsers support comments using the # character, this is not part of the official YAML specification and may not be supported by all parsers.

-  Poor performance: In some cases, YAML may not be as efficient as other data serialization languages in terms of performance. For example, parsing and serializing large YAML documents may be slower compared to other formats.


## Development timeline

| Year | Description |
| ---- | ----------- |
| 2001 | YAML was first released in Perl. |
| 2003 | The first YAML framework was written in Ruby. |
| 2004 | The YAML 1.0 specification was published.   By Clark Evans, Oren Ben-Kiki, and Ingy döt Net after 3 years of collaborative design work through the yaml-core mailing list. |
| 2005 | The YAML 1.1 specification was published | 
| 2006 | Kyrylo Simonov produced PyYAML and LibYAML | 
| 2009 | The YAML 1.2 specification was published, it's primary focus was making YAML a strict superset of JSON | 
| 2020 | New YAML language design team formed to work on YAML improvements | 
| 2021 | This YAML 1.2.2 specification was published | 


