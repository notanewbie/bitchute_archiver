#
#
#  notanewbie made this.
#  ____________________
# |  ________________  |
# | |________________| |
# |                    |
# |  ________________  |
# | |                | |
# | |   __________   | |
# | |  |          |  | |
# | |__|          |__| |
# |____________________|
#
#
#

import urllib2;
import time;
def GetURL2(link):
    req = urllib2.Request(link, None, {'User-agent' : 'Mozilla/5.0 (Windows; U; Windows NT 5.1; de; rv:1.9.1.5) Gecko/20091102 Firefox/3.5.5'})
    response = urllib2.urlopen(req).read()
    return response;
def main():
    vid = raw_input("Which video would you like to archive?\n")
    vid = GetURL2(vid).split("tracker.openwebtorrent.com&as=")[1].split("&xs")[0];
    print "URL found: " + vid;
    GetURL2("http://web.archive.org/save/" + vid);
    print "Video saved."
    main();
main();
