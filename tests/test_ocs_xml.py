#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" test_ocs_xml.py - unit tests for ocs_xml functionality """

#+
# imports
#-
import glob
import os
import sys
import unittest
from ocs_xml import ocs_xml

#+
# class
#-
class TestOcs_xml(unittest.TestCase):

    def setUp(self):

        # get path to schema
        # (assumes you are in the directory where you would issue a "make test")
        self.xsdf = ''.join(os.getcwd()+'/ocs_xml/ocs.xsd')
        self.xsde = os.path.isfile(self.xsdf)
        sys.stdout.write('\nFinding schema '+self.xsdf+' ... '+('OK\n' if self.xsde else 'ERROR\n'))
        sys.stdout.flush()
        self.assertTrue(self.xsde)

        # get paths to xml test files
        # (assumes you are in the directory where you would issue a "make test")
        self.xmlf = ''.join(os.getcwd()+'/tests/*.xml')
        sys.stdout.write('\nGlobbing on '+self.xmlf+' ... '+('OK\n' if isinstance(self.xmlf,str) else 'ERROR\n'))
        sys.stdout.flush()
        self.assertIsInstance(self.xmlf,str)

        # get all xml test files in path
        self.xmll = glob.glob(self.xmlf)
        sys.stdout.write('\nGlob returns '+self.xmlf+' ... '+(str(self.xmll)+'\n' if self.xmll is not [] else 'ERROR\n'))
        sys.stdout.flush()
        self.assertNotEqual(self.xmll,[])

        # get parser based upon schema
        self.parser = ocs_xml.get_parser(self.xsdf)

    def test_ocs_xml(self):

        # loop around all xml test files for validation
        for F in self.xmll:
            sys.stdout.write('Running ocs_xml.validate('+self.xsdf+','+F+')'+'\n')
            sys.stdout.flush()
            self.assertEqual(ocs_xml.validate(self.parser,F), True)

    def tearDown(self):
        del self.xsdf
        del self.xsde
        del self.xmlf
        del self.xmll
        del self.parser

#+
# main
#-
if __name__ == '__main__':
    unittest.main()
