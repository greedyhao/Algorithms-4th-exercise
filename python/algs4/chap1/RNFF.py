#!/usr/bin/python
# -*- coding: utf-8 -*-


def read_num_from_file(file):
    list_tmp = []
    for line in file:
        list_tmp.append(list(map(int, line.split(',')))[0])
    return list_tmp
