#!/usr/bin/python
# -*- coding: utf-8 -*-


def read_num_from_file(file):
    list_tmp = []
    for line in file:
        tmp = line.split('\n')
        del (tmp[1])
        tmp = map(int, tmp)
        list_tmp += tmp
    return list_tmp

