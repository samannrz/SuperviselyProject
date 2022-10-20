from functions import *
import datetime

# This codes takes some statistics on the Workspaces
# and save the dataframe to google sheet

teamName = 'Endometriosis'
workspaceName = 'Data annotation'
sheetName = teamName + '/' + workspaceName + str(datetime.datetime.now())

#sfpath = 'C:/Users/SurgAR-User/OneDrive/Documents/Saman/mypythonfolder/supervisely-python-sdk-example/my-gpysheets-3d8d13442005.json'
sfpath = '/home/saman/PycharmProjects/SuperviselyProject/keycode/my-gpysheets-3d8d13442005.json'
sheetID = '1R_2NpRg40U08F2gl4dM0OzXcN4f0IQaW3yfXZmBWqCg'
datadf = pdStats (teamName,workspaceName)
write_to_gsheet(sfpath, sheetID, sheetName, datadf)
