# This code is written by Senadhi

def createSeafolder():
    import os.path

    # defining the file path and name
    path = "C:/Users/Public/Weather Data Collector"

    # check whether folder already exists
    file_path = os.path.isdir("C:/Users/Public/Weather Data Collector/Sea Surface Data")

    # If foldr doesn't exist create the new folder
    if not file_path:
        os.chdir(path)
        newfolder = "Sea Surface Data"
        os.mkdir(newfolder)

