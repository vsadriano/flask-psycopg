#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class Author():
    def __init__(self, first_name, last_name, email, id_=None):
        self.id = id_
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
