#!/usr/bin/python
# -*- coding: utf-8 -*-

import unittest

import commons


class BaseTest(unittest.TestCase):

    def test_basic(self):
        self.assertEqual(commons.floor(88.1057268722467, 2), 88.10)
