__author__ = 'Daniel'

#with open("test.txt", "a") as myfile:
#    myfile.write("appended text")
tempfilenames = ['divtoappend.html', 'http://d3js.org/d3.v2.js?2.9.1', 'https://code.jquery.com/jquery-latest.min.js', './Graph.js', './UndirectedGraph.js', './D3Graph.js', './DataTransmute.js', './d3/d3.js', './Jquery/jquery-2.1.4.min.js', './bodyscript.js' ]
tempfiles = []
for f in tempfilenames:
    tempfiles.append(open(f, "r"))

#tempfilenames

# tempfiles is a list of file handles to your temp files. Order them however you like
f = open("bigfile.js", "w")
for tempfile in tempfiles:
    f.write(tempfile.read())