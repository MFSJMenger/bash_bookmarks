BASH_BOOKMARKS
==============

Adds basic functionallity for bookmarking
uses both bash and python to configer everything
It works with both python2 and python3

USAGE
-----

creates bash commands for bookmarking in bash.
default names are:

1. cdb bookmark - change directory to [bookmark]

2. setb bookmark - create a new bookmark of the current folder with name [bookmark]
    
3. rmb bookmark - remove the [bookmark]
    
4. listb - list all bookmarks
    
5. pb - return the name of the bookmark, useful for substitution 
         e.g. "cd `pb [bookmark]`"  is the same as cdb [bookmark]


cdb, listb and pb all have autocomplete enabled!


Configuration
~~~~~~~~~~~~~

all commands can be configured using the `bookmarks_config.ini` file. e.g.

    [bookmarks]
    
    set = set_bookmark

    cd = cd_bookmark

    lib= ~/.bookmarks

afterwards run python setup.py
will rename setb to set_bookmark and cdb to cd_bookmark


INSTALL
-------

to install just add to your bashrc

    source $BOOKMARKS_ROOT/bin/bookmarks.sh


