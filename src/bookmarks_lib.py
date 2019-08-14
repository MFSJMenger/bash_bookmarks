import os
import json
from functools import wraps

if os.environ.get("BOOKMARKS_LIB", None) is None:
    filepath = os.path.abspath(__file__)
    main     = os.path.dirname(os.path.dirname(os.path.dirname(filepath)))
    main = os.path.join(main, "lib")
else:
    main = os.environ.get("BOOKMARKS_LIB")

bookmark_file   = os.path.join(main,'bookmarks.json')
bookmark_names  = os.path.join(main,'bookmarks.txt')

alias_file   = os.path.join(main,'alias.json')
alias_names  = os.path.join(main,'alias.txt')

todo_file   = os.path.join(main,'todo.json')
todo_names  = os.path.join(main,'todo.txt')

class BasicDecorator(object):

    __slots__ = ['iprint','debug','name','func','results','add_key','args','kwargs']

    def __init__(self, iprint= 0, debug=False, Name=None):
        self.debug = debug
        self.name = Name
        self.func = None
        self.results = []
        self.add_key = {}
        self.args=[]
        self.kwargs=[]
        self.iprint = iprint
        
    def __call__(self,func):
        # add func to self, so that one can use information for self.before_func
        self.func = func
        # actual wrapper_function
        @wraps(func)
        def wrapper_function(*args, **kwargs):
            self.args = args
            self.kwargs = kwargs
            self.before_func()
            self.results = func(*self.args, **self.kwargs)
            self.after_func()
            return self.results
        return wrapper_function

    def breakString(self,string,delim="\n",length=60):
        """
            divide string by delim, 
        """
        if len(string) > length:
            out="" 
            line=""
            lim=length
            for ele in string.split():
                if (len(line) + len(ele) + 1) > lim:
                    out += line + delim
                    line = ele + " "
                else:
                    line += ele + " "
            out += line 
        else:
            out = string       
        return out


    def before_func(self):
        """
            enter anything that should be executed before the function is called
        """
        pass

    def after_func(self):
        """
            enter anything that should be executed after the function is called
        """
        pass



def read_file_bookmark():
    global bookmark_file
    return read_file(bookmark_file)

def save_file_bookmark(bookmarks):
    global bookmark_file
    global bookmark_names
    save_file(bookmarks, bookmark_file, bookmark_names)


def read_file_alias():
    global alias_file
    return read_file(alias_file)

def save_file_alias(alias):
    global alias_file
    global alias_names
    save_file(alias, alias_file, alias_names)

def read_file_todo():
    global todo_file
    return read_file(todo_file)

def save_file_todo(todo):
    global todo_file
    global todo_names
    save_file(todo, todo_file, todo_names)


def read_file(json_file):

    if os.path.isfile(json_file):
        f=open(json_file, 'r')
        bookmarks = json.load(f)
        f.close()
    else:
        bookmarks = {}

    return bookmarks

def save_file(bookmarks, json_file, key_file):

    if bookmarks.keys() == []:
        os.remove(json_file)
        f=open(key_file, 'w')
        f.write('')
        f.close()
    else:
        f=open(json_file, 'w')
        json.dump(bookmarks, f, indent=4, ensure_ascii=True)
        f.close()
        f=open(key_file, 'w')
        f.write(" ".join(bookmarks.keys()))
        f.close()

class HandleBookmarkCases(BasicDecorator):
    
    __slots__ = ['save','read','func','results','args','kwargs']

    def __init__(self, save=False, read=True, Name=None):
        self.func = None
        self.results = []
        self.args=[]
        self.kwargs=[]
        self.save = save
        self.read = read

    def before_func(self):
        if self.read is True:
            if self.kwargs['typ'] == 'bookmark':
                self.kwargs['bookmarks'] = read_file_bookmark()

            elif self.kwargs['typ'] == 'alias':
                self.kwargs['bookmarks'] = read_file_alias()
            elif self.kwargs['typ'] == 'todo':
                self.kwargs['bookmarks'] = read_file_todo()
    def after_func(self):
        if self.save is True:
            if self.kwargs['typ'] == 'bookmark':
                save_file_bookmark(self.kwargs['bookmarks'])
            elif self.kwargs['typ'] == 'alias':
                save_file_alias(self.kwargs['bookmarks'])
            elif self.kwargs['typ'] == 'todo':
                save_file_todo(self.kwargs['bookmarks'])

