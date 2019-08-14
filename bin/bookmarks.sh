
export BOOKMARKS_LIB=~/.bookmarks

BOOKMARKS_ROOT=$(dirname "$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )")
export BOOKMARKS_ROOT

source $BOOKMARKS_ROOT/src/bookmarks.sh
source $BOOKMARKS_ROOT/complete/bookmarks.sh

alias setb="BOOKMARK_SET"     # set bookmark
alias cdb="BOOKMARK_CD"       # cd bookmark
alias listb="BOOKMARK_LIST"   # list bookmarks
alias rmb="BOOKMARK_REMOVE"   # remove bookmark
alias pb="BOOKMARK_PATH"   # show path bookmark

