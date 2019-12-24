# Flexible XML to dict Converter

```bash
pip install python-xml2dict
```

```python
import xml2dict
```

## Default Behaviour

The `parse` function takes a string or a file as a parameter. All other
parameters are optional.

```python
xml = '''
    <list>
        <items>
            <item id="1">A</item>
            <item id="2">B</item>
            <item id="3">C</item>
            <item id="4">D</item>
        </items>
        <date>1.1.2019</date>
    </list>
'''
print(json.dumps(xml2dict.parse(xml), indent=4))
```

```python
{
    "list": {
        "items": {
            "item": [
                {
                    "@id": "1",
                    "#text": "A"
                },
                {
                    "@id": "2",
                    "#text": "B"
                },
                {
                    "@id": "3",
                    "#text": "C"
                },
                {
                    "@id": "4",
                    "#text": "D"
                }
            ]
        },
        "date": "1.1.2019"
    }
}
```

## Customized Behaviour

Behaviour can be modified by defining custom processing functions, which may be
applicable to one, more or all XML elements.

### Put items with unique keys to a dict

```python
def get_key(obj, name, val, arg):
    if name == 'id':
        arg['key'] = val
    else:
        obj[tag] = val

def add_item(obj, tag, val, arg):
    if tag not in obj:
        obj[tag] = {arg['key']: val}
    else:
        obj[tag][arg['key']] = val

schema = [
    {"elem": ["item"], "attr": get_key, "add": add_item}
]

print(json.dumps(xml2dict.parse(xml, schema), indent=4))
```

```python
{
    "list": {
        "items": {
            "item": {
                "1": "A",
                "2": "B",
                "3": "C",
                "4": "D"
            }
        },
        "date": "1.1.2019"
    }
}
```

### Use different processing for certain items

If the processing function does not store the value into a dict, only the
remaining items will be returned.

```python
def print_item(obj, tag, val, arg):
    print("ITEM", tag, val)

schema = [
    {"elem": ["item"], "add": print_item}
]

print(json.dumps(xml2dict.parse(xml, schema), indent=4))
```

```python
ITEM item {'@id': '1', '#text': 'A'}
ITEM item {'@id': '2', '#text': 'B'}
ITEM item {'@id': '3', '#text': 'C'}
ITEM item {'@id': '4', '#text': 'D'}
{
    "list": {
        "items": null,
        "date": "1.1.2019"
    }
}
```
