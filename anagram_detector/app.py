#!/usr/bin/env python

import os, sys, math



def detect_anagram(input1, input2):
    result = True

    def prepare_input(text):
        return sorted(''.join([char for char in text if char.isalpha()]).lower())

    input1 = prepare_input(input1)
    input2 = prepare_input(input2)

    if input1 != input2:
        return False

    return result

