import supervisely as sly
import os
from functions import write_to_gsheet
import pandas as pd
import openpyxl


def find(s, ch):
    return [i for i, ltr in enumerate(s) if ltr == ch]


## Definition of Parameters
# Saman's Token
mytoken = 'jXCVEbySH8moyTXLihkoE1k9UX4fTMDUYkHMJgUoIzx0EnyS5outN8de6UvUCjdGfRUr8D553l8MhTLQkzDOm22bKTsJulgDiGzy2Z4yYEmFmhcsL8k37Af837qXb2UO'
path = "C://Users/SurgAR-User/OneDrive/Documents/Surgar/Female/Rigas first Results/BAD"
teamName = 'Endometriosis'
workspaceName = 'Data annotation'

# start using supervisely API
api = sly.Api(server_address="http://surgai-surgery.com", token=mytoken)

tm = api.team.get_info_by_name(teamName)
ws = api.workspace.get_info_by_name(tm.id, workspaceName)
prs = api.project.get_list(ws.id)

videos = []
projects = []
datasets = []
file_names = []
frames = []

# get a list of supervisely video names with their corresponding project and dataset name
for pr in prs:
    dss = api.dataset.get_list(pr.id)
    for ds in dss:
        vds = api.video.get_list(ds.id)
        for vd in vds:
            videos.append(vd.name)
            projects.append(pr.name)
            datasets.append(ds.name)

# list of video names and the frames
dir_list = os.listdir(path)
myfiles = []
for file in dir_list:
    points = find(file, '.')
    myfiles.append({'name': file[:points[-2]], 'framenum': int(file[points[-2] + 1:points[-1]])})

nameList = []
prList = []
dsList = []
frList = []
for fl in myfiles:
    fn = fl['name']
    indv = videos.index(fn)
    nameList.append(videos[indv])
    prList.append(projects[indv])
    dsList.append(datasets[indv])
    frList.append(fl['framenum'])

data_df = pd.DataFrame(
    {'Project': prList, 'dataset': dsList, 'Video Name': nameList, 'Frame': frList})
sfpath = 'C:/Users/SurgAR-User/OneDrive/Documents/Saman/mypythonfolder/supervisely-python-sdk-example/my-gpysheets-3d8d13442005.json'
sheetID = '1XEX4axQ96cSP7tprdbxL6TewmICepo4fowguvG-hTwc'
sheetName = teamName  + workspaceName
data_df.to_excel('Corrections.xlsx', sheetName)
write_to_gsheet(sfpath, sheetID, sheetName, data_df)
