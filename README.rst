BASH_BOOKMARKS
==============

Adds basic functionallity for bookmarking
uses both bash and python to configer everything
It works with both python2 and python3

USAGE
-----

creates bash commands for bookmarking in bash.
default names are:
    cdb bookmark - change directory to [bookmark]

    setb bookmark - create a new bookmark of the current folder with name [bookmark]
    
    rmb bookmark - remove the [bookmark]
    
    listb - list all bookmarks
    
    pb - return the name of the bookmark, useful for substitution 
         e.g. cd `pb [bookmark]`  is the same as cdb [bookmark]

Configuration
~~~~~~~~~~~~~

all commands can be configured using the `bookmarks_config.ini` file. e.g.

    [bookmarks]
    
    set = set_bookmark
    
    cd = cd_bookmark

afterwards run python setup.py

will rename setb to set_bookmark and cdb to cd_bookmark


INSTALL
-------

to install just add to your bashrc


    export $BOOKMARKS_ROOT=path_to_this_folder
    
    source $BOOKMARKS_ROOT/bin/bookmarks.sh


