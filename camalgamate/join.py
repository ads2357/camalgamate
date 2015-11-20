import glob, re, os, sys
import toposort

class Header:
    include_pat = '#include\s+"([^"]+)"'

    def __init__(self, dependencies, name):
        self.dependencies = dependencies
        self.name = name

    @classmethod
    def from_file(clazz, header_file_name):
        """Generates a Header from a header file."""
        header_deps = set()
        with open(header_file_name, "r") as hfile:
            for line in hfile:
                match = re.match(clazz.include_pat, line)
                if match:
                    header_deps.add(match.group(1))
        return clazz(header_deps, header_file_name)

def order_headers(header_file_name_collection):
    """Reorders the list of header files, dependencies first"""
    header_set = set(header_file_name_collection)
    if len(header_set) != len(header_file_name_collection):
        raise ValueError("Duplicate header file names")
    
    header_objs = [ Header.from_file(name) for name in header_set ]
    dep_graph = { head.name : head.dependencies for head in header_objs }

    return toposort.toposort_flatten(dep_graph)

def commentify(string):
    if '/*' in string or '*/' in string:
        raise ValueError("String " + string + " already looks like a comment")
    return '/* ' + string + '*/'

def cat_files(ordered_file_name_list, output_io):
    """Concatenates the files, in order, omitting local includes"""
    for fname in ordered_file_name_list:
        output_io.writelines([commentify(fname)])
        with open(fname, "r") as sourcefile:
            for line in sourcefile:
                if not re.match(Header.include_pat, line):
                    output_io.write(line)
