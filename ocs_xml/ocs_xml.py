#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" ocs_xml.py - validates XML files against the ocs.xsd schema """

#+
# imports
#-
import sys
from lxml import etree

#+
# functions
#-
def get_parser(xs):
    with open(xs, 'rb') as f:
        sroot = etree.XML(f.read())
    schema = etree.XMLSchema(sroot)
    return etree.XMLParser(schema=schema)

def validate(xs, xf):
    try:
        with open(xf, 'rb') as f:
            etree.fromstring(f.read(), xs) 
        return True
    except etree.XMLSchemaError:
        return False

def help():
    sys.stdout.write('ERROR> Invalid input (XSD schema or XML file missing)\n')
    sys.stdout.write('Use: validate.py <XSD-file> <XML_file>\n')
    sys.stdout.write('Eg:  validate.py mySchema.xsd myFile.xml\n')
    sys.exit(0)

#+
# main
#-
if __name__ == '__main__':

    # get command line parameters
    xsdf = sys.argv[1] if len(sys.argv)>1 else help()
    xmlf = sys.argv[2] if len(sys.argv)>2 else help()

    # get parser based upon schema
    xsdp = get_parser(xsdf)

    # validate xml file using parser
    if validate(xsdp, xmlf):
        sys.stdout.write('OK> '+xmlf+' validates against '+xsdf+'\n')
    else:
        sys.stdout.write('ERROR> '+xmlf+' does not validate against '+xsdf+'\n')
