#!/usr/bin/env python
# -*- coding: utf-8 -*-

str1 = u'578A'
str2 = u'34578A9'

if str1 in str2:
    print u'Yes'

print str2.find(str1)