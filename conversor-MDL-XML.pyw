import matlab.engine
import sys

# Call matlab engine on background and convert to XML
def mdl2xml(fileName):
    myengine = matlab.engine.start_matlab() #start engine background=true

    myengine.load_system(fileName) #put MDL/SLX on memory

    partialFilename = fileName.split(".") #create xml filename
    xmlCompleteFilename = partialFilename[0] + '.xml'

    myengine.save_system(fileName, xmlCompleteFilename, 'ExportToXML', True) #mdl2xmler

    myengine.quit() #stop engine

fileName = sys.argv[1] #call function
mdl2xml(fileName)
