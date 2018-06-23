
_BOOKMARK_CD()
{
    local cur=${COMP_WORDS[COMP_CWORD]}
    if [ -f ../lib/bookmarks.txt ]; then
        local val=`cat .bookmarks.txt`
    else
        local val=""
    fi
    COMPREPLY=( $(compgen -W "$val" -- $cur) )
}

complete -F _BOOKMARK_CD cdb

