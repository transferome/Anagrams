# biggest confusion with package to use is that people were using urllib, urllib2, or urllib3
# urllib2 is not in python3, and urllib3 is not standard out of the box python module
import urllib.request


def return_dictionary():
    # opens url
    fp = urllib.request.urlopen("https://inventwithpython.com/dictionary.txt")
    # reads in the lines to a list, but they are not in 'UTF-8', they are in bytearray object type
    # which means it is unreadable to us in that data type
    mbytes = fp.readlines()
    # this converts the bytearray into a 'utf8' string
    dictionary = [m.decode('utf8').rstrip('\n') for m in mbytes]
    fp.close()
    return dictionary


if __name__ == '__main__':
    pass
