import supervisely as sly
import pandas as pd

# import os
from functions import write_to_gsheet
# import openpyxl
import datetime



def find(s, ch):
    return [i for i, ltr in enumerate(s) if ltr == ch]


def getvidlist(teamName,workspaceName):
    # Definition of Parameters
    # Saman's Token
    mytoken = 'jXCVEbySH8moyTXLihkoE1k9UX4fTMDUYkHMJgUoIzx0EnyS5outN8de6UvUCjdGfRUr8D553l8MhTLQkzDOm22bKTsJulgDiGzy2Z4yYEmFmhcsL8k37Af837qXb2UO'

    # start using supervisely API
    api = sly.Api(server_address="http://surgai-surgery.com", token=mytoken)

    tm = api.team.get_info_by_name(teamName)
    ws = api.workspace.get_info_by_name(tm.id, workspaceName)
    prs = api.project.get_list(ws.id)

    nameList = []
    projects = []
    datasets = []

    # lesions = []
    annot = []
    jj = 0

      # get a list of workspace video names with their corresponding project and dataset name
    for pr in prs:
        dss = api.dataset.get_list(pr.id)
        for ds in dss:
            vds = api.video.get_list(ds.id)
            for vd in vds:
                nameList.append(vd.name)
                projects.append(pr.name)
                datasets.append(ds.name)
                ans = api.video.annotation.download(vd.id)
                objs = ans['objects']

                if len(objs):
                    annot.append(1)
                else:
                    annot.append(0)




    return projects, datasets, nameList, annot

def main():
    teamName = 'Endometriosis'
    workspaceName = 'Incision annotation'
    prList, dsList, nameList, lesionList = getvidlist(teamName, workspaceName)

    data_df = pd.DataFrame(
             {'Video Name': nameList, 'Project': prList, 'dataset': dsList , 'annotated': lesionList})


    sfpath = 'keycode/my-gpysheets-3d8d13442005.json'
    sheetID = '10nt-qCCI6KUOd-dE-Iq1e3xXd7gkFV-f776dp25oGmQ'
    sheetName = teamName + '_' + workspaceName + str(datetime.date.today())
    data_df.to_excel('incision.xlsx', sheetName) #locally saves to the current path
    write_to_gsheet(sfpath, sheetID, sheetName, data_df)


if __name__== '__main__':
    main()
