from __future__ import print_function
import sys
from string import Template

from src.bookmarks_tools import appendText, writeFile

try:
    import configparser
except:
    import ConfigParser as configparser

bin_bookmarks = Template("""
export BOOKMARKS_LIB=$bookmarks_lib

BOOKMARKS_ROOT=$$(dirname "$$( cd "$$( dirname "$${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )")
export BOOKMARKS_ROOT

source $$BOOKMARKS_ROOT/src/bookmarks.sh
source $$BOOKMARKS_ROOT/complete/bookmarks.sh

alias $bookmarks_set="BOOKMARK_SET"     # set bookmark
alias $bookmarks_cd="BOOKMARK_CD"       # cd bookmark
alias $bookmarks_list="BOOKMARK_LIST"   # list bookmarks
alias $bookmarks_rm="BOOKMARK_REMOVE"   # remove bookmark
alias $bookmarks_path="BOOKMARK_PATH"   # show path bookmark

""")

complete_bookmarks = Template("""
_BOOKMARK_PATH()
{
    local cur=$${COMP_WORDS[COMP_CWORD]}
    if [ -f $$BOOKMARKS_LIB/bookmarks.txt ]; then
        local val=`cat $$BOOKMARKS_LIB/bookmarks.txt`
    else
        local val=""
    fi
    COMPREPLY=( $$(compgen -W "$$val" -- $$cur) )
}

complete -F _BOOKMARK_PATH $bookmarks_cd
complete -F _BOOKMARK_PATH $bookmarks_path
complete -F _BOOKMARK_PATH $bookmarks_rm
""")

src_bookmarks_colors = Template("""
class bcolors:
    HEADER = '$color_header'
    OKBLUE = '$color_okblue'
    OKGREEN = '$color_okgreen'
    WARNING = '$color_warning'
    FAIL = '$color_fail'
    ENDC = '$color_endc'
    BOLD = '$color_bold'
    UNDERLINE = '$color_underline'
""")



def read_bookmark_config(fileName):

    configs = {
            'bookmarks' : {
                'set' : 'setb',
                'cd'  : 'cdb',
                'list' : 'listb',
                'rm' : 'rmb',
                'path' : 'pb',
                'lib' : '~/.bookmarks',
                },
            'color' : {
                'header' : '\\033[95m',
                'okblue' : '\\033[94m',
                'okgreen' : '\\033[92m',
                'warning' : '\\033[93m',
                'fail' : '\\033[91m',
                'endc' : '\\033[0m',
                'bold' : '\\033[1m',
                'underline' : '\\033[4m',
                },
            }
    config = configparser.ConfigParser()
    config.read(fileName)

    for section in config.sections():
        main = section.lower()
        if main not in configs:
            pass
        for key in config[section]:
            if key.lower() in configs[main]:
                configs[main][key.lower()] = config[section][key]
    
    return configs

def configer_bookmarks_dct(dct):

    outdct = {}
    for entry in dct:
        for key in dct[entry]:
            outdct[entry + "_" + key] = dct[entry][key]

    return outdct

def config_bookmarks(config_file):
    dct = configer_bookmarks_dct(read_bookmark_config(config_file))
    writeFile('bin/bookmarks.sh', bin_bookmarks.substitute(dct))
    writeFile('complete/bookmarks.sh', complete_bookmarks.substitute(dct))
    writeFile('src/bookmarks_colors.py', src_bookmarks_colors.substitute(dct))

config_bookmarks('bookmarks_config.ini')
