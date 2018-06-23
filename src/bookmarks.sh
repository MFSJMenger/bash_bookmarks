# $BOOKMARKS_ROOT must be set in bashrc!
export LAST_BOOKMARK_ENTRY=""
export LAST_ALIAS_ENTRY=""

BOOKMARK_SET(){

    $BOOKMARKS_ROOT/src/bookmarks.py -o set -b "$1"

}

BOOKMARK_CD(){

    bookmark=${1:-$LAST_BOOKMARK_ENTRY}
    path=`$BOOKMARKS_ROOT/src/bookmarks.py -o get -b "$bookmark"`
    if [ ! -z "$path" ]; then
    cd $path
    export LAST_BOOKMARK_ENTRY="$bookmark"
    fi
    pwd

}

BOOKMARK_PATH(){

    bookmark=${1}
    path=`$BOOKMARKS_ROOT/src/bookmarks.py -o get -b "$bookmark"`
    if [ ! -z "$path" ]; then
    echo $path
    fi

}

BOOKMARK_LIST(){

    $BOOKMARKS_ROOT/src/bookmarks.py -o list

}

BOOKMARK_REMOVE(){

    $BOOKMARKS_ROOT/src/bookmarks.py -o remove -b "$1"
}



ALIAS_SET(){

    $BOOKMARKS_ROOT/src/bookmarks.py -o aset -b "$1" -v "$2"

}


ALIAS_GET(){

    bookmark=${1}
    path=`$BOOKMARKS_ROOT/src/bookmarks.py -o aget -b "$bookmark"`
    if [ ! -z "$path" ]; then
    echo $path
    fi

}

ALIAS_LIST(){

    $BOOKMARKS_ROOT/src/bookmarks.py -o alist

}

ALIAS_REMOVE(){

    $BOOKMARKS_ROOT/src/bookmarks.py -o aremove -b "$1"
}


TODO_SET(){

    $BOOKMARKS_ROOT/src/bookmarks.py -o tset -b "$1" -v "$2" -p "$3"

}


TODO_GET(){

    bookmark=${1}
    path=`$BOOKMARKS_ROOT/src/bookmarks.py -o tget -b "$bookmark"`
    if [ ! -z "$path" ]; then
    echo $path
    fi

}

TODO_LIST(){

    $BOOKMARKS_ROOT/src/bookmarks.py -o tlist

}

TODO_REMOVE(){

    $BOOKMARKS_ROOT/src/bookmarks.py -o tremove -b "$1"
}
