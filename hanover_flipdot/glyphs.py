#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np

five = {}

five[' '] = [[0],
             [0],
             [0],
             [0],
             [0]]

five['A'] = [[0, 1, 1, 0],
             [1, 0, 0, 1],
             [1, 1, 1, 1],
             [1, 0, 0, 1],
             [1, 0, 0, 1]]

five['B'] = [[1, 1, 1, 0],
             [1, 0, 0, 1],
             [1, 1, 1, 1],
             [1, 0, 0, 1],
             [1, 1, 1, 0]]

five['C'] = [[0, 1, 1, 0],
             [1, 0, 0, 1],
             [1, 0, 0, 0],
             [1, 0, 0, 1],
             [0, 1, 1, 0]]

five['D'] = [[1, 1, 1, 0],
             [1, 0, 0, 1],
             [1, 0, 0, 1],
             [1, 0, 0, 1],
             [1, 1, 1, 0]]

five['E'] = [[1, 1, 1, 1],
             [1, 0, 0, 0],
             [1, 1, 1, 0],
             [1, 0, 0, 0],
             [1, 1, 1, 1]]

five['F'] = [[1, 1, 1, 1],
             [1, 0, 0, 0],
             [1, 1, 1, 0],
             [1, 0, 0, 0],
             [1, 0, 0, 0]]

five['G'] = [[0, 1, 1, 1],
             [1, 0, 0, 0],
             [1, 0, 1, 1],
             [1, 0, 0, 1],
             [1, 1, 1, 0]]

five['H'] = [[1, 0, 0, 1],
             [1, 0, 0, 1],
             [1, 1, 1, 1],
             [1, 0, 0, 1],
             [1, 0, 0, 1]]

five['I'] = [[1, 1, 1],
             [0, 1, 0],
             [0, 1, 0],
             [0, 1, 0],
             [1, 1, 1]]

five['J'] = [[1, 1, 1],
             [0, 0, 1],
             [0, 0, 1],
             [0, 0, 1],
             [1, 1, 0]]

five['K'] = [[1, 0, 0, 1],
             [1, 0, 1, 0],
             [1, 1, 0, 0],
             [1, 0, 1, 0],
             [1, 0, 0, 1]]

five['L'] = [[1, 0, 0, 0],
             [1, 0, 0, 0],
             [1, 0, 0, 0],
             [1, 0, 0, 0],
             [1, 1, 1, 1]]

five['M'] = [[1, 0, 0, 0, 1],
             [1, 1, 0, 0, 1],
             [1, 0, 1, 0, 1],
             [1, 0, 0, 0, 1],
             [1, 0, 0, 0, 1]]

five['N'] = [[1, 0, 0, 1],
             [1, 1, 0, 1],
             [1, 0, 1, 1],
             [1, 0, 0, 1],
             [1, 0, 0, 1]]

five['O'] = [[0, 1, 1, 0],
             [1, 0, 0, 1],
             [1, 0, 0, 1],
             [1, 0, 0, 1],
             [0, 1, 1, 0]]

five['P'] = [[1, 1, 1, 0],
             [1, 0, 0, 1],
             [1, 1, 1, 0],
             [1, 0, 0, 0],
             [1, 0, 0, 0]]

five['Q'] = [[0, 1, 1, 0],
             [1, 0, 0, 1],
             [1, 0, 0, 1],
             [1, 0, 1, 0],
             [0, 1, 0, 1]]

five['R'] = [[1, 1, 1, 0],
             [1, 0, 0, 1],
             [1, 1, 1, 0],
             [1, 0, 0, 1],
             [1, 0, 0, 1]]

five['S'] = [[0, 1, 1, 0],
             [1, 0, 0, 1],
             [0, 1, 1, 0],
             [0, 0, 0, 1],
             [1, 1, 1, 0]]

five['T'] = [[1, 1, 1],
             [0, 1, 0],
             [0, 1, 0],
             [0, 1, 0],
             [0, 1, 0]]

five['U'] = [[1, 0, 0, 1],
             [1, 0, 0, 1],
             [1, 0, 0, 1],
             [1, 0, 0, 1],
             [0, 1, 1, 0]]

five['V'] = [[1, 0, 0, 0, 1],
             [1, 0, 0, 0, 1],
             [1, 0, 0, 0, 1],
             [0, 1, 0, 1, 0],
             [0, 0, 1, 0, 0]]

five['W'] = [[1, 0, 0, 0, 1],
             [1, 0, 0, 0, 1],
             [1, 0, 1, 0, 1],
             [1, 1, 0, 1, 1],
             [1, 0, 0, 0, 1]]

five['X'] = [[1, 0, 1],
             [1, 0, 1],
             [0, 1, 0],
             [1, 0, 1],
             [1, 0, 1]]

five['Y'] = [[1, 0, 1],
             [1, 0, 1],
             [0, 1, 1],
             [0, 0, 1],
             [1, 1, 1]]

five['Z'] = [[1, 1, 1, 1],
             [0, 0, 0, 1],
             [0, 1, 1, 0],
             [1, 0, 0, 0],
             [1, 1, 1, 1]]

five['0'] = [[1, 1, 1],
             [1, 0, 1],
             [1, 0, 1],
             [1, 0, 1],
             [1, 1, 1]]

five['1'] = [[1],
             [1],
             [1],
             [1]]

five['2'] = [[1, 1, 1],
             [0, 0, 1],
             [1, 1, 1],
             [1, 0, 0],
             [1, 1, 1]]

five['3'] = [[1, 1, 1],
             [0, 0, 1],
             [1, 1, 1],
             [0, 0, 1],
             [1, 1, 1]]

five['4'] = [[0, 0, 1],
             [0, 1, 1],
             [1, 0, 1],
             [1, 1, 1],
             [0, 0, 1]]

five['5'] = [[1, 1, 1],
             [1, 0, 0],
             [1, 1, 1],
             [0, 0, 1],
             [1, 1, 1]]

five['6'] = [[1, 1, 1],
             [1, 0, 0],
             [1, 1, 1],
             [1, 0, 1],
             [1, 1, 1]]

five['7'] = [[1, 1, 1],
             [0, 0, 1],
             [0, 1, 0],
             [1, 0, 0],
             [1, 0, 0]]

five['8'] = [[1, 1, 1],
             [1, 0, 1],
             [1, 1, 1],
             [1, 0, 1],
             [1, 1, 1]]

five['9'] = [[1, 1, 1],
             [1, 0, 1],
             [1, 1, 1],
             [0, 0, 1],
             [1, 1, 1]]

five['/'] = [[0, 0, 1],
             [0, 0, 1],
             [0, 1, 0],
             [1, 0, 0],
             [1, 0, 0]]

five['\\'] = [[1, 0, 0],
              [1, 0, 0],
              [0, 1, 0],
              [0, 0, 1],
              [0, 0, 1]]

five['('] = [[0, 1],
             [1, 0],
             [1, 0],
             [1, 0],
             [0, 1]]

five[')'] = [[1, 0],
             [0, 1],
             [0, 1],
             [0, 1],
             [1, 0]]

five[']'] = [[1, 1],
             [0, 1],
             [0, 1],
             [0, 1],
             [1, 1]]

five['['] = [[1, 1],
             [1, 0],
             [1, 0],
             [1, 0],
             [1, 1]]

five['{'] = [[0, 1, 1],
             [0, 1, 0],
             [1, 0, 0],
             [0, 1, 0],
             [0, 1, 1]]

five['}'] = [[1, 1, 0],
             [0, 1, 0],
             [0, 0, 1],
             [0, 1, 0],
             [1, 1, 0]]

five['>'] = [[1, 0, 0],
             [0, 1, 0],
             [0, 0, 1],
             [0, 1, 0],
             [1, 0, 0]]

five['<'] = [[0, 0, 1],
             [0, 1, 0],
             [1, 0, 0],
             [0, 1, 0],
             [0, 0, 1]]

five['+'] = [[0, 0, 0],
             [0, 1, 0],
             [1, 1, 1],
             [0, 1, 0],
             [0, 0, 0]]

five['&'] = [[0, 0, 0],
             [0, 1, 0],
             [1, 1, 1],
             [0, 1, 0],
             [0, 0, 0]]

five['-'] = [[0, 0, 0],
             [0, 0, 0],
             [1, 1, 1],
             [0, 0, 0],
             [0, 0, 0]]

five['@'] = [[0, 1, 1, 1],
             [1, 0, 0, 1],
             [1, 0, 0, 1],
             [1, 0, 1, 1],
             [1, 0, 1, 1]]

five['!'] = [[1],
             [1],
             [1],
             [0],
             [1]]

five['?'] = [[1, 1, 1],
             [0, 0, 1],
             [0, 1, 1],
             [0, 0, 0],
             [0, 1, 0]]

five['£'] = [[0, 1, 1],
             [1, 0, 0],
             [1, 1, 0],
             [1, 0, 0],
             [1, 1, 1]]

five['$'] = [[0, 1, 1],
             [1, 0, 0],
             [1, 1, 0],
             [1, 0, 0],
             [1, 1, 1]]

five['%'] = [[1, 0, 1],
             [0, 0, 1],
             [0, 1, 0],
             [1, 0, 0],
             [1, 0, 1]]

five['.'] = [[0],
             [0],
             [0],
             [0],
             [1]]

five[':'] = [[0],
             [1],
             [0],
             [0],
             [1]]

five[','] = [[0],
             [0],
             [0],
             [1],
             [1]]

five[';'] = [[0],
             [1],
             [0],
             [1],
             [1]]

five['='] = [[0, 0, 0],
             [1, 1, 1],
             [0, 0, 0],
             [1, 1, 1],
             [0, 0, 0]]

five['\''] =[[1],
             [1],
             [0],
             [0],
             [0]]

five['"'] = [[1, 0, 1],
             [1, 0, 1],
             [0, 0, 0],
             [0, 0, 0],
             [0, 0, 0]]

five['#'] = [[0, 1, 0, 1, 0],
             [1, 1, 1, 1, 1],
             [0, 1, 0, 1, 0],
             [1, 1, 1, 1, 1],
             [0, 1, 0, 1, 0]]

five['*'] = [[0, 1, 0],
             [1, 1, 1],
             [0, 1, 0],
             [0, 0, 0],
             [0, 0, 0]]


""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

ten = {}

ten[' '] = [[0],
            [0],
            [0],
            [0],
            [0]]

ten['A'] = [[0, 1, 1, 1, 1, 0],
            [1, 1, 1, 1, 1, 1],
            [1, 1, 0, 0, 1, 1],
            [1, 1, 0, 0, 1, 1],
            [1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1],
            [1, 1, 0, 0, 1, 1],
            [1, 1, 0, 0, 1, 1],
            [1, 1, 0, 0, 1, 1],
            [1, 1, 0, 0, 1, 1]]

ten['B'] = [[1, 1, 1, 1, 1, 0],
            [1, 1, 1, 0, 1, 1],
            [1, 1, 0, 0, 1, 1],
            [1, 1, 0, 0, 1, 1],
            [1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1],
            [1, 1, 0, 0, 1, 1],
            [1, 1, 0, 0, 1, 1],
            [1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 0]]


ten['C'] = [[0, 1, 1, 1, 1, 0],
            [1, 1, 1, 1, 1, 1],
            [1, 1, 0, 0, 1, 1],
            [1, 1, 0, 0, 0, 0],
            [1, 1, 0, 0, 0, 0],
            [1, 1, 0, 0, 0, 0],
            [1, 1, 0, 0, 0, 0],
            [1, 1, 0, 0, 1, 1],
            [1, 1, 1, 1, 1, 1],
            [0, 1, 1, 1, 1, 0]]

ten['D'] = [[1, 1, 1, 1, 1, 0],
            [1, 1, 1, 1, 1, 1],
            [1, 1, 0, 0, 1, 1],
            [1, 1, 0, 0, 1, 1],
            [1, 1, 0, 0, 1, 1],
            [1, 1, 0, 0, 1, 1],
            [1, 1, 0, 0, 1, 1],
            [1, 1, 0, 0, 1, 1],
            [1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 0]]

ten['E'] = [[1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1],
            [1, 1, 0, 0, 0, 0],
            [1, 1, 0, 0, 0, 0],
            [1, 1, 1, 1, 1, 0],
            [1, 1, 1, 1, 1, 0],
            [1, 1, 0, 0, 0, 0],
            [1, 1, 0, 0, 0, 0],
            [1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1]]

ten['F'] = [[1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1],
            [1, 1, 0, 0, 0, 0],
            [1, 1, 0, 0, 0, 0],
            [1, 1, 1, 1, 1, 0],
            [1, 1, 1, 1, 1, 0],
            [1, 1, 0, 0, 0, 0],
            [1, 1, 0, 0, 0, 0],
            [1, 1, 0, 0, 0, 0],
            [1, 1, 0, 0, 0, 0]]

ten['G'] = [[0, 1, 1, 1, 1, 0],
            [1, 1, 1, 1, 1, 1],
            [1, 1, 0, 0, 1, 1],
            [1, 1, 0, 0, 0, 0],
            [1, 1, 0, 1, 1, 1],
            [1, 1, 0, 1, 1, 1],
            [1, 1, 0, 0, 1, 1],
            [1, 1, 0, 0, 1, 1],
            [1, 1, 1, 1, 1, 1],
            [0, 1, 1, 1, 1, 0]]

ten['H'] = [[1, 1, 0, 0, 1, 1],
            [1, 1, 0, 0, 1, 1],
            [1, 1, 0, 0, 1, 1],
            [1, 1, 0, 0, 1, 1],
            [1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1],
            [1, 1, 0, 0, 1, 1],
            [1, 1, 0, 0, 1, 1],
            [1, 1, 0, 0, 1, 1],
            [1, 1, 0, 0, 1, 1]]

ten['I'] = [[1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1],
            [0, 0, 1, 1, 0, 0],
            [0, 0, 1, 1, 0, 0],
            [0, 0, 1, 1, 0, 0],
            [0, 0, 1, 1, 0, 0],
            [0, 0, 1, 1, 0, 0],
            [0, 0, 1, 1, 0, 0],
            [1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1]]

ten['J'] = [[1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1],
            [0, 0, 0, 0, 1, 1],
            [0, 0, 0, 0, 1, 1],
            [0, 0, 0, 0, 1, 1],
            [0, 0, 0, 0, 1, 1],
            [0, 0, 0, 0, 1, 1],
            [1, 1, 0, 0, 1, 1],
            [1, 1, 1, 1, 1, 1],
            [0, 1, 1, 1, 1, 0]]

ten['K'] = [[1, 1, 0, 0, 1, 1],
            [1, 1, 0, 0, 1, 1],
            [1, 1, 0, 0, 1, 1],
            [1, 1, 0, 0, 1, 1],
            [1, 1, 1, 1, 0, 0],
            [1, 1, 1, 1, 1, 0],
            [1, 1, 0, 1, 1, 1],
            [1, 1, 0, 0, 1, 1],
            [1, 1, 0, 0, 1, 1],
            [1, 1, 0, 0, 1, 1]]

ten['L'] = [[1, 1, 0, 0, 0, 0],
            [1, 1, 0, 0, 0, 0],
            [1, 1, 0, 0, 0, 0],
            [1, 1, 0, 0, 0, 0],
            [1, 1, 0, 0, 0, 0],
            [1, 1, 0, 0, 0, 0],
            [1, 1, 0, 0, 0, 0],
            [1, 1, 0, 0, 0, 0],
            [1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1]]

ten['M'] = [[1, 1, 0, 0, 0, 0, 0, 1, 1],
            [1, 1, 1, 0, 0, 0, 1, 1, 1],
            [1, 1, 1, 1, 0, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 0, 1, 1, 1, 0, 1, 1],
            [1, 1, 0, 0, 1, 0, 0, 1, 1],
            [1, 1, 0, 0, 0, 0, 0, 1, 1],
            [1, 1, 0, 0, 0, 0, 0, 1, 1],
            [1, 1, 0, 0, 0, 0, 0, 1, 1],
            [1, 1, 0, 0, 0, 0, 0, 1, 1]]

ten['N'] = [[1, 1, 0, 0, 0, 0, 1, 1],
            [1, 1, 1, 0, 0, 0, 1, 1],
            [1, 1, 1, 1, 0, 0, 1, 1],
            [1, 1, 0, 1, 1, 0, 1, 1],
            [1, 1, 0, 0, 1, 1, 1, 1],
            [1, 1, 0, 0, 0, 1, 1, 1],
            [1, 1, 0, 0, 0, 0, 1, 1],
            [1, 1, 0, 0, 0, 0, 1, 1],
            [1, 1, 0, 0, 0, 0, 1, 1],
            [1, 1, 0, 0, 0, 0, 1, 1]]

ten['O'] = [[0, 1, 1, 1, 1, 0],
            [1, 1, 1, 1, 1, 1],
            [1, 1, 0, 0, 1, 1],
            [1, 1, 0, 0, 1, 1],
            [1, 1, 0, 0, 1, 1],
            [1, 1, 0, 0, 1, 1],
            [1, 1, 0, 0, 1, 1],
            [1, 1, 0, 0, 1, 1],
            [1, 1, 1, 1, 1, 1],
            [0, 1, 1, 1, 1, 0]]

ten['P'] = [[1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1],
            [1, 1, 0, 0, 1, 1],
            [1, 1, 0, 0, 1, 1],
            [1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 0],
            [1, 1, 0, 0, 0, 0],
            [1, 1, 0, 0, 0, 0],
            [1, 1, 0, 0, 0, 0],
            [1, 1, 0, 0, 0, 0]]

ten['Q'] = [[0, 1, 1, 1, 1, 0],
            [1, 1, 1, 1, 1, 1],
            [1, 1, 0, 0, 1, 1],
            [1, 1, 0, 0, 1, 1],
            [1, 1, 0, 0, 1, 1],
            [1, 1, 0, 0, 1, 1],
            [1, 1, 0, 0, 0, 1],
            [1, 1, 0, 1, 1, 0],
            [1, 1, 0, 1, 1, 1],
            [0, 1, 1, 0, 1, 1]]

ten['R'] = [[1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1],
            [1, 1, 0, 0, 1, 1],
            [1, 1, 0, 0, 1, 1],
            [1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 0],
            [1, 1, 0, 1, 1, 1],
            [1, 1, 0, 0, 1, 1],
            [1, 1, 0, 0, 1, 1],
            [1, 1, 0, 0, 1, 1]]

ten['S'] = [[0, 1, 1, 1, 1, 0],
            [1, 1, 1, 1, 1, 1],
            [1, 1, 0, 0, 1, 1],
            [1, 1, 0, 0, 0, 0],
            [1, 1, 1, 1, 1, 1],
            [0, 1, 1, 1, 1, 1],
            [0, 0, 0, 0, 1, 1],
            [1, 1, 0, 0, 1, 1],
            [1, 1, 1, 1, 1, 1],
            [0, 1, 1, 1, 1, 0]]

ten['T'] = [[1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1],
            [0, 0, 1, 1, 0, 0],
            [0, 0, 1, 1, 0, 0],
            [0, 0, 1, 1, 0, 0],
            [0, 0, 1, 1, 0, 0],
            [0, 0, 1, 1, 0, 0],
            [0, 0, 1, 1, 0, 0],
            [0, 0, 1, 1, 0, 0],
            [0, 0, 1, 1, 0, 0]]

ten['U'] = [[1, 1, 0, 0, 1, 1],
            [1, 1, 0, 0, 1, 1],
            [1, 1, 0, 0, 1, 1],
            [1, 1, 0, 0, 1, 1],
            [1, 1, 0, 0, 1, 1],
            [1, 1, 0, 0, 1, 1],
            [1, 1, 0, 0, 1, 1],
            [1, 1, 0, 0, 1, 1],
            [1, 1, 1, 1, 1, 1],
            [0, 1, 1, 1, 1, 0]]

ten['V'] = [[1, 1, 0, 0, 0, 1, 1],
            [1, 1, 0, 0, 0, 1, 1],
            [1, 1, 0, 0, 0, 1, 1],
            [1, 1, 0, 0, 0, 1, 1],
            [1, 1, 0, 0, 0, 1, 1],
            [1, 1, 0, 0, 0, 1, 1],
            [1, 1, 1, 0, 1, 1, 1],
            [0, 1, 1, 1, 1, 1, 0],
            [0, 0, 1, 1, 1, 0, 0],
            [0, 0, 0, 1, 0, 0, 0]]

ten['W'] = [[1, 1, 0, 0, 0, 0, 0, 1, 1],
            [1, 1, 0, 0, 0, 0, 0, 1, 1],
            [1, 1, 0, 0, 0, 0, 0, 1, 1],
            [1, 1, 0, 0, 0, 0, 0, 1, 1],
            [1, 1, 0, 0, 1, 0, 0, 1, 1],
            [1, 1, 0, 1, 1, 1, 0, 1, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 0, 1, 1, 1, 1],
            [1, 1, 1, 0, 0, 0, 1, 1, 1],
            [1, 1, 0, 0, 0, 0, 0, 1, 1]]

ten['X'] = [[1, 1, 0, 0, 0, 1, 1],
            [1, 1, 0, 0, 0, 1, 1],
            [1, 1, 1, 0, 1, 1, 1],
            [0, 1, 1, 1, 1, 1, 0],
            [0, 0, 1, 1, 1, 0, 0],
            [0, 1, 1, 1, 1, 1, 0],
            [1, 1, 1, 0, 1, 1, 1],
            [1, 1, 0, 0, 0, 1, 1],
            [1, 1, 0, 0, 0, 1, 1],
            [1, 1, 0, 0, 0, 1, 1]]

ten['Y'] = [[1, 1, 0, 0, 1, 1],
            [1, 1, 0, 0, 1, 1],
            [1, 1, 1, 0, 1, 1],
            [0, 1, 1, 1, 1, 1],
            [0, 0, 1, 1, 1, 1],
            [0, 0, 1, 1, 1, 1],
            [0, 0, 0, 0, 1, 1],
            [1, 1, 0, 0, 1, 1],
            [1, 1, 1, 1, 1, 1],
            [0, 1, 1, 1, 1, 1]]

ten['Z'] = [[1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1],
            [0, 0, 0, 0, 1, 1],
            [0, 0, 0, 1, 1, 1],
            [0, 0, 1, 1, 1, 1],
            [0, 1, 1, 1, 0, 0],
            [1, 1, 0, 0, 0, 0],
            [1, 0, 0, 0, 0, 0],
            [1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1]]

ten['0'] = [[0, 1, 1, 1, 1, 0],
            [1, 1, 1, 1, 1, 1],
            [1, 1, 0, 0, 1, 1],
            [1, 1, 0, 0, 1, 1],
            [1, 1, 0, 0, 1, 1],
            [1, 1, 0, 0, 1, 1],
            [1, 1, 0, 0, 1, 1],
            [1, 1, 0, 0, 1, 1],
            [1, 1, 1, 1, 1, 1],
            [0, 1, 1, 1, 1, 0]]

ten['1'] = [[1, 1],
            [1, 1],
            [1, 1],
            [1, 1],
            [1, 1],
            [1, 1],
            [1, 1],
            [1, 1],
            [1, 1],
            [1, 1]]

ten['2'] = [[0, 1, 1, 1, 1, 0],
            [1, 1, 1, 1, 1, 1],
            [1, 1, 0, 0, 1, 1],
            [1, 1, 0, 0, 1, 1],
            [0, 0, 0, 0, 1, 1],
            [0, 0, 0, 1, 1, 1],
            [0, 0, 1, 1, 1, 0],
            [0, 1, 1, 1, 0, 0],
            [1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1]]

ten['3'] = [[0, 1, 1, 1, 1, 0],
            [1, 1, 1, 1, 1, 1],
            [1, 1, 0, 0, 1, 1],
            [0, 0, 0, 0, 1, 1],
            [0, 0, 1, 1, 1, 1],
            [0, 0, 1, 1, 1, 1],
            [0, 0, 0, 0, 1, 1],
            [1, 1, 0, 0, 1, 1],
            [1, 1, 1, 1, 1, 1],
            [0, 1, 1, 1, 1, 1]]

ten['4'] = [[0, 0, 0, 0, 1, 1],
            [0, 0, 0, 1, 1, 1],
            [0, 0, 1, 1, 1, 1],
            [0, 1, 1, 1, 1, 1],
            [1, 1, 1, 0, 1, 1],
            [1, 1, 0, 0, 1, 1],
            [1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1],
            [0, 0, 0, 0, 1, 1],
            [0, 0, 0, 0, 1, 1]]

ten['5'] = [[1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1],
            [1, 0, 0, 0, 0, 0],
            [1, 1, 1, 1, 0, 0],
            [1, 1, 1, 1, 1, 0],
            [0, 0, 0, 0, 1, 1],
            [0, 0, 0, 0, 1, 1],
            [1, 1, 0, 0, 1, 1],
            [1, 1, 1, 1, 1, 1],
            [0, 1, 1, 1, 1, 0]]

ten['6'] = [[0, 1, 1, 1, 1, 0],
            [1, 1, 1, 1, 1, 1],
            [1, 1, 0, 0, 1, 1],
            [1, 1, 0, 0, 0, 0],
            [1, 1, 1, 1, 1, 0],
            [1, 1, 1, 1, 1, 1],
            [1, 1, 0, 0, 1, 1],
            [1, 1, 0, 0, 1, 1],
            [1, 1, 1, 1, 1, 1],
            [0, 1, 1, 1, 1, 0]]

ten['7'] = [[1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1],
            [0, 0, 0, 0, 1, 1],
            [0, 0, 0, 1, 1, 1],
            [0, 0, 1, 1, 1, 0],
            [0, 1, 1, 1, 0, 0],
            [1, 1, 1, 0, 0, 0],
            [1, 1, 0, 0, 0, 0],
            [1, 1, 0, 0, 0, 0],
            [1, 1, 0, 0, 0, 0]]

ten['8'] = [[0, 1, 1, 1, 1, 0],
            [1, 1, 1, 1, 1, 1],
            [1, 1, 0, 0, 1, 1],
            [1, 1, 0, 0, 1, 1],
            [1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1],
            [1, 1, 0, 0, 1, 1],
            [1, 1, 0, 0, 1, 1],
            [1, 1, 1, 1, 1, 1],
            [0, 1, 1, 1, 1, 0]]

ten['9'] = [[0, 1, 1, 1, 1, 0],
            [1, 1, 1, 1, 1, 1],
            [1, 1, 0, 0, 1, 1],
            [1, 1, 0, 0, 1, 1],
            [1, 1, 1, 1, 1, 1],
            [0, 1, 1, 1, 1, 1],
            [0, 0, 0, 0, 1, 1],
            [1, 1, 0, 0, 1, 1],
            [1, 1, 1, 1, 1, 1],
            [0, 1, 1, 1, 1, 0]]

ten['/'] = [[0, 0, 1, 1],
            [0, 0, 1, 1],
            [0, 0, 1, 1],
            [0, 1, 1, 0],
            [0, 1, 1, 0],
            [0, 1, 1, 0],
            [1, 1, 0, 0],
            [1, 1, 0, 0],
            [1, 1, 0, 0],
            [1, 1, 0, 0]]

ten['\\'] = [[1, 1, 0, 0],
             [1, 1, 0, 0],
             [1, 1, 0, 0],
             [1, 1, 1, 0],
             [0, 1, 1, 0],
             [0, 1, 1, 0],
             [0, 1, 1, 1],
             [0, 0, 1, 1],
             [0, 0, 1, 1],
             [0, 0, 1, 1]]

ten['('] = [[0, 0, 1, 1],
            [1, 1, 1, 1],
            [1, 1, 0, 0],
            [1, 1, 0, 0],
            [1, 1, 0, 0],
            [1, 1, 0, 0],
            [1, 1, 0, 0],
            [1, 1, 0, 0],
            [1, 1, 1, 1],
            [0, 0, 1, 1]]

ten[')'] = [[1, 1, 0, 0],
            [1, 1, 1, 1],
            [0, 0, 1, 1],
            [0, 0, 1, 1],
            [0, 0, 1, 1],
            [0, 0, 1, 1],
            [0, 0, 1, 1],
            [0, 0, 1, 1],
            [1, 1, 1, 1],
            [1, 1, 0, 0]]

ten['['] = [[1, 1, 1, 1],
            [1, 1, 1, 1],
            [1, 1, 0, 0],
            [1, 1, 0, 0],
            [1, 1, 0, 0],
            [1, 1, 0, 0],
            [1, 1, 0, 0],
            [1, 1, 0, 0],
            [1, 1, 1, 1],
            [1, 1, 1, 1]]

ten[']'] = [[1, 1, 1, 1],
            [1, 1, 1, 1],
            [0, 0, 1, 1],
            [0, 0, 1, 1],
            [0, 0, 1, 1],
            [0, 0, 1, 1],
            [0, 0, 1, 1],
            [0, 0, 1, 1],
            [1, 1, 1, 1],
            [1, 1, 1, 1]]

ten['{'] = [[0, 0, 1, 1],
            [0, 1, 1, 1],
            [0, 1, 1, 0],
            [0, 1, 1, 0],
            [1, 1, 0, 0],
            [1, 1, 0, 0],
            [0, 1, 1, 0],
            [0, 1, 1, 0],
            [0, 1, 1, 1],
            [0, 0, 1, 1]]

ten['}'] = [[1, 1, 0, 0],
            [1, 1, 1, 0],
            [0, 1, 1, 0],
            [0, 1, 1, 0],
            [0, 0, 1, 1],
            [0, 0, 1, 1],
            [0, 1, 1, 0],
            [0, 1, 1, 0],
            [1, 1, 1, 0],
            [1, 1, 0, 0]]

ten['>'] = [[0, 0, 0, 0, 1, 0],
            [0, 0, 0, 1, 1, 1],
            [0, 0, 1, 1, 1, 0],
            [0, 1, 1, 1, 0, 0],
            [0, 1, 1, 0, 0, 0],
            [1, 1, 1, 0, 0, 0],
            [0, 1, 1, 1, 0, 0],
            [0, 0, 1, 1, 1, 0],
            [0, 0, 0, 1, 1, 1],
            [0, 0, 0, 0, 1, 0]]

ten['<'] = [[0, 1, 0, 0, 0, 0],
            [1, 1, 1, 0, 0, 0],
            [0, 1, 1, 1, 0, 0],
            [0, 0, 1, 1, 0, 0],
            [0, 0, 0, 1, 1, 0],
            [0, 0, 0, 1, 1, 1],
            [0, 0, 1, 1, 1, 0],
            [0, 1, 1, 1, 0, 0],
            [1, 1, 1, 0, 0, 0],
            [0, 1, 0, 0, 0, 0]]

ten['+'] = [[0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 1, 1, 0, 0],
            [0, 0, 1, 1, 0, 0],
            [1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1],
            [0, 0, 1, 1, 0, 0],
            [0, 0, 1, 1, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0]]

ten['&'] = [[0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 1, 1, 0, 0],
            [0, 0, 1, 1, 0, 0],
            [1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1],
            [0, 0, 1, 1, 0, 0],
            [0, 0, 1, 1, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0]]

ten['-'] = [[0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0]]

ten['@'] = [[0, 1, 1, 1, 1, 1, 0],
            [1, 1, 1, 1, 1, 1, 1],
            [1, 1, 0, 0, 0, 1, 1],
            [1, 1, 0, 1, 1, 1, 1],
            [1, 1, 0, 1, 0, 1, 1],
            [1, 1, 0, 1, 0, 1, 1],
            [1, 1, 0, 1, 1, 1, 0],
            [1, 1, 0, 0, 0, 0, 0],
            [1, 1, 1, 1, 1, 0, 0],
            [0, 1, 1, 1, 1, 0, 0]]

ten['!'] = [[1, 1],
            [1, 1],
            [1, 1],
            [1, 1],
            [1, 1],
            [1, 1],
            [1, 1],
            [0, 0],
            [1, 1],
            [1, 1]]

ten['?'] = [[0, 1, 1, 1, 1, 0],
            [1, 1, 1, 1, 1, 1],
            [1, 1, 0, 0, 1, 1],
            [0, 0, 0, 0, 1, 1],
            [0, 0, 0, 1, 1, 0],
            [0, 0, 1, 1, 0, 0],
            [0, 0, 1, 1, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 1, 1, 0, 0],
            [0, 0, 1, 1, 0, 0]]

ten['£'] = [[0, 0, 1, 1, 0, 0],
            [1, 1, 1, 1, 1, 1],
            [1, 1, 0, 0, 1, 1],
            [1, 1, 0, 0, 0, 0],
            [1, 1, 1, 1, 0, 0],
            [1, 1, 1, 1, 0, 0],
            [1, 1, 0, 0, 0, 0],
            [1, 1, 0, 0, 0, 0],
            [1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1]]

ten['$'] = [[0, 0, 1, 1, 0, 0],
            [1, 1, 1, 1, 1, 1],
            [1, 1, 0, 0, 1, 1],
            [1, 1, 0, 0, 0, 0],
            [1, 1, 1, 1, 0, 0],
            [1, 1, 1, 1, 0, 0],
            [1, 1, 0, 0, 0, 0],
            [1, 1, 0, 0, 0, 0],
            [1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1]]

ten['%'] = [[1, 1, 0, 0, 1, 1],
            [1, 1, 0, 0, 1, 1],
            [1, 1, 0, 0, 1, 1],
            [0, 0, 0, 1, 1, 1],
            [0, 0, 1, 1, 1, 0],
            [0, 1, 1, 1, 0, 0],
            [1, 1, 1, 0, 0, 0],
            [1, 1, 0, 0, 1, 1],
            [1, 1, 0, 0, 1, 1],
            [1, 1, 0, 0, 1, 1]]

ten['.'] = [[0, 0],
            [0, 0],
            [0, 0],
            [0, 0],
            [0, 0],
            [0, 0],
            [0, 0],
            [0, 0],
            [1, 1],
            [1, 1]]

ten[':'] = [[0, 0],
            [0, 0],
            [0, 0],
            [0, 0],
            [1, 1],
            [1, 1],
            [0, 0],
            [0, 0],
            [1, 1],
            [1, 1]]

ten[','] = [[0, 0],
            [0, 0],
            [0, 0],
            [0, 0],
            [0, 0],
            [0, 0],
            [0, 0],
            [0, 0],
            [1, 1],
            [0, 1]]

ten[';'] = [[0, 0],
            [0, 0],
            [0, 0],
            [0, 0],
            [1, 1],
            [1, 1],
            [0, 0],
            [0, 0],
            [1, 1],
            [0, 1]]

ten['='] = [[0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0]]

ten['\''] =[[1],
            [1],
            [1],
            [0],
            [0],
            [0],
            [0],
            [0],
            [0],
            [0]]

ten['"'] = [[1, 0, 1],
            [1, 0, 1],
            [1, 0, 1],
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0]]

ten['#'] = [[0, 1, 1, 0, 1, 1, 0],
            [0, 1, 1, 0, 1, 1, 0],
            [1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1],
            [0, 1, 1, 0, 1, 1, 0],
            [0, 1, 1, 0, 1, 1, 0],
            [1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1],
            [0, 1, 1, 0, 1, 1, 0],
            [0, 1, 1, 0, 1, 1, 0]]

ten['*'] = [[0, 0, 1, 0, 0],
            [0, 1, 1, 1, 0],
            [1, 1, 1, 1, 1],
            [0, 1, 1, 1, 0],
            [0, 0, 1, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0]]


def glify(text, font=five, debug=False):

    if font == five:
        output = ([[], [], [], [], []])
    else:
        output = ([[], [], [], [], [], [], [], [], [], []])

    for char in text:
        a = np.array(font[char])
        output = np.concatenate((output, a), axis=1)
        a = np.array(font[' '])
        output = np.concatenate((output, a), axis=1)

    if debug:
        print(output)

    return output


container = list()
for row in glify('ABCDE'):
    tmp = list()
    for item in row:
        tmp.append(str(int(item)))
    
    tmp = ''.join(tmp).zfill(96)
    tmp += '\n'
    container.append(''.join(tmp))

while len(container) < 16:
    container.append(('0'*96) + '\n')

container = ''.join(container)
container = container.replace('0', '-')
container = container.replace('1', '#')
