from __future__ import print_function
# It can be used to use features which will appear
# in newer
# versions while having an older release of Python.


class Song:

    """
    class to represent doc string
    """
    def __init__(self, title,duration,artist):
        """
        :param title:
        :param duration:
        :param artist:
        """
        self.artist= artist
        self.title=title
        self.duration=duration

# a="is \n a string \t\t and tabbed"
# raw_string=r"this is\n a string"
# b_string="this is" +chr(10)+"a string split"
# backslash_string=r"this is a  \\raw string"
# print(backslash_string)
# if __name__=='__main__':
#     print(a)
# print(Song.__init__.__doc__)

Song.__init__.__doc__="test"
# print(Song.__init__.__doc__)


print('# of entries', len([1,2,3]))




