#!/usr/bin/python3
#
# Copyright (c) 2019 Petr Gotthard <petr.gotthard@centrum.cz>
# All rights reserved.
# Distributed under the terms of the MIT License. See the LICENSE file.
#
import xml.etree.ElementTree as etree
import io
import re

def attr(nobj, aname, aval, arg):
    nobj[arg["attr_prefix"]+aname] = aval

def add_dict(pobj, tag, tobj, arg):
    if tag not in pobj:
        pobj[tag] = tobj
    elif isinstance(pobj[tag], list):
        pobj[tag].append(tobj)
    else:
        pobj[tag] = [pobj[tag], tobj]

def add_list(pobj, tag, tobj, arg):
    if tag not in pobj:
        pobj[tag] = [tobj]
    else:
        pobj[tag].append(tobj)

def strip_namespace(text):
    match = re.match(r'{([^}]+)}(.+)', text)
    if match != None:
        return match.group(2)
    else:
        return text

def strip_text(text):
    if text == None:
        return ""
    else:
        return text.strip()

def parse(inp, schema={}, global_schema={}):
    if isinstance(inp, str):
        inp = io.StringIO(inp)

    stack = [({},{})]
    for event,elem in etree.iterparse(inp, events=('start','end')):
        tag = strip_namespace(elem.tag)
        if event == 'start':
            # load tag processing instructions
            sch = {"attr": attr, "add": add_dict, "attr_prefix": "@", "text_key": "#text"}
            sch.update(global_schema)
            for s in schema:
                if tag in s['elem']:
                    sch.update(s)
                    break
            nobj = {}
            for an,aval in elem.attrib.items():
                aname = strip_namespace(an)
                # add attribute
                sch['attr'](nobj, aname, aval, sch)
            stack.append((nobj, sch))
        elif event == 'end':
            tobj,sch = stack.pop()
            text = strip_text(elem.text) + strip_text(elem.tail)

            if len(tobj) > 0:
                if len(text) > 0:
                    tobj[sch['text_key']] = text
            elif len(text) > 0:
                # text only element
                tobj = text
            else:
                tobj = None

            # add element to the tree (or not)
            sch['add'](stack[-1][0], tag, tobj, sch)

    return stack[0][0]

# end of file
