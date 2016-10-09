#!/usr/bin/env python

import os, sys, math



def reverse_factorial(input):
    print "*** %s ***" % input
    result = None

    if input == 0:
        return result

    n = input
    i = 2
    while n % i == 0:
        n /= i
        i += 1

    print n
    print i
    if n == 1:
        result = i-1

    print "result: %s" % result

    return result

