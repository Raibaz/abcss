# abcss
A tiny script to sort CSS properties in a file in alphabetical order


Sometimes coding standards enforce CSS properties in source files to be sorted alphabetically; this script can be used as a pre-commit git hook to ensure that the standard is respected without having to deal with it manually.

### Usage

`python abcss.py <file to format>`, where `<file to format>` is the full path to the file that needs to be formatted with CSS properties sorted alphabetically; it will be rewritten in-place.

### Vendor prefixes
Vendor-prefixed properties will remain grouped together, being sorted as if they all were the same property.
