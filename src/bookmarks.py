#!/usr/bin/env python
from __future__ import print_function
import os
from bookmarks_lib import HandleBookmarkCases
from bookmarks_colors import bcolors



@HandleBookmarkCases()
def get_bookmark(bookmark,*args, **kwargs):

    bookmarks = kwargs['bookmarks']
    if bookmark in bookmarks:
        if kwargs['typ'] == 'todo':
            print(bookmarks[bookmark][0])
        else:
            print(bookmarks[bookmark])

@HandleBookmarkCases(save=True)
def set_bookmark(bookmark,*args, **kwargs):

    if kwargs['typ'] == 'bookmark':
        kwargs['bookmarks'][bookmark] = os.getcwd()
    elif kwargs['typ'] == 'alias':
        kwargs['bookmarks'][bookmark] = kwargs['dct']['alias_value']
    elif kwargs['typ'] == 'todo':
        kwargs['bookmarks'][bookmark] = [
                                          kwargs['dct']['alias_value'],
                                          kwargs['dct']['priority'],
                                        ]

@HandleBookmarkCases(save=True)
def remove_bookmark(bookmark,*args, **kwargs):

    if bookmark in kwargs['bookmarks']:
        del kwargs['bookmarks'][bookmark]

@HandleBookmarkCases()
def list_bookmarks(bookmark,*args, **kwargs):

    bookmarks = kwargs['bookmarks']
    print(bcolors.FAIL)
    print("            bookmark | path ")
    print(" ----------------------------------------------------- "+bcolors.ENDC)
    for key, value in bookmarks.items():
        if kwargs['typ'] in ['alias','bookmark']:
            key_value = value
        elif kwargs['typ'] in ['todo']:
            key_value = value[0]
        print("%s %19s %s|%s %s %s" % (
            bcolors.BOLD+bcolors.HEADER,key,bcolors.ENDC,
            bcolors.HEADER,key_value,bcolors.ENDC))

def getCommandoLine():
    """
        Get Commando line option with argpase

    """

    options = [
        'set',
        'get',
        'remove',
        'list',
        'aset',
        'aget',
        'aremove',
        'alist',
        'tset',
        'tget',
        'tremove',
        'tlist',
            ]

    import argparse

    parser = argparse.ArgumentParser("bookmarks")
    parser.add_argument("-b","--bookmark", metavar="Bookmark",type=str,default=None,
                        help="name of the bookmark, show all")

    parser.add_argument("-o","--option", metavar="Option",type=str,default='get',
                        choices=options,
                        help="What is possible")

    parser.add_argument("-v","--alias_value", metavar="VALUE",default=None,
                        help="if alias are set, use this")

    parser.add_argument("-p","--priority", metavar="PRIO",default=0,
                        help="priorities for todo list lowest 0 highest 5")

    args = parser.parse_args()

    dct = {
            'alias_value' : args.alias_value,
            'priority' : args.priority,
          }

    return args.bookmark, args.option, dct


def main():
    """
        Main Function if program is called as standalone

    """

    options = {
        'set'     : set_bookmark,
        'get'     : get_bookmark,
        'remove'  : remove_bookmark,
        'list'    : list_bookmarks,
            }

    bookmark, option, dct = getCommandoLine()


    if option in ['set','get','remove','list']:
        typ='bookmark'
    elif option in ['aset','aget','aremove','alist']:
        typ='alias'
        option = option[1:]
    elif option in ['tset','tget','tremove','tlist']:
        typ='todo'
        option = option[1:]

    options[option](bookmark,typ=typ,dct=dct)

if __name__ == "__main__":
    main()
