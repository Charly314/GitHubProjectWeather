# This code is written by Senadhi

def createIcefolder():
    import os.path

    # defining the file path and name
    path = "C:/Users/Public/Weather Data Collector"

    # check whether folder already exists
    file_path = os.path.isdir("C:/Users/Public/Weather Data Collector/Ice Thickness Data")

    # If foldr doesn't exist create the new folder
    if not file_path:
        os.chdir(path)
        newfolder = "Ice Thickness Data"
        os.mkdir(newfolder)

