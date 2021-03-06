# -*- coding: utf-8 -*-
"""
hash_table.py
~~~~~~
The Hash Table allows you to store multiple Hash Map, 
each of which has an Name Map and an Hash useful to 
write the content for use on the web site.

:copyright: (c) 2013 by Leonardo Zizzamia
:license: BSD (See LICENSE for details)
""" 
# Imports outside Bombolone
from flask import Blueprint, request, g, render_template, url_for, redirect
from pymongo.objectid import ObjectId
from pymongo.errors import InvalidId, PyMongoError

# Imports inside Bombolone
from decorators import check_rank, get_hash

MODULE_DIR = 'admin/hash_table'
hash_table = Blueprint('hash_table', __name__)

@hash_table.route('/admin/hash_table/')
@check_rank(30) 
@get_hash('hash_table')
def overview():
    """ 
    List all the documents, each has a name 
    that identifies it, and an hash map. 
    """
    return render_template('{}/index.html'.format(MODULE_DIR), **locals())


@hash_table.route('/admin/hash_table/new/')
@hash_table.route('/admin/hash_table/update/<_id>/')
@check_rank(30)
@get_hash('hash_table')
def upsert(_id=None):
    """ """
    view = False
    return render_template('{}/upsert.html'.format(MODULE_DIR), **locals())


@hash_table.route('/admin/hash_table/view/<_id>/')
@check_rank(40)
@get_hash('hash_table')
def view(_id=None):
    """ """
    view = True
    return render_template('{}/upsert.html'.format(MODULE_DIR), **locals())