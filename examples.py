#!/usr/bin/python3
import xml2dict
import json

# idential to https://github.com/martinblech/xmltodict
print(json.dumps(xml2dict.parse('''
    <mydocument has="an attribute">
        <and>
            <many>elements</many>
            <many>more elements</many>
        </and>
        <plus a="complex">
            element as well
        </plus>
    </mydocument>
'''), indent=4))

# default functionality
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

# put items with unique keys to a dict
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

# print (skip, store elsewhere) certain items
# return the remainder only
def print_item(obj, tag, val, arg):
    print("ITEM", tag, val)

schema = [
    {"elem": ["item"], "add": print_item}
]

print(json.dumps(xml2dict.parse(xml, schema), indent=4))

# end of file
