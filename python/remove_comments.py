import re
import sys

def remove_comments(text):

    # Regular expression
    pattern = r'(--.*)|(((\/\*)+?[\w\W]+?(\*\/)+))'

    # Compile and substitute
    result = re.sub(pattern,'',f, flags=re.MULTILINE)

    return result

if __name__ == '__main__':
    filen = sys.argv[1]
    f = open(filen).read()
    nf = remove_comments(f)
    fh = open(filen+".nocomments","w")
    fh.write(nf)
    fh.close()
