import supervisely as sly
import os
from functions import write_to_gsheet
import pandas as pd
import openpyxl


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
    lesionList = []
    jj = 0

    lesiondic = {
        'Adhesions.Dense': 0,
        'Adhesions.Filmy': 1,
        'Superficial.White': 2,
        'Superficial.Black': 3,
        'Superficial.Red': 4,
        'Superficial.Subtle': 5,
        'Ovarian.Endometrioma': 6,
        'Ovarian.Chocolate Fluid': 7,
        'Deep Endometriosis': 8,
        'Ovarian.Endometrioma[B]': 9
    }
    # get a list of supervisely video names with their corresponding project and dataset name
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
                lesions = [0] * 10
                for i in range(len(objs)):
                    lesions[lesiondic[objs[i]['classTitle']]] = 1

                lesionList.append(lesions)
    return projects, datasets, nameList, lesionList

def main():
    lesiondic = {
        'Adhesions.Dense': 0,
        'Adhesions.Filmy': 1,
        'Superficial.White': 2,
        'Superficial.Black': 3,
        'Superficial.Red': 4,
        'Superficial.Subtle': 5,
        'Ovarian.Endometrioma': 6,
        'Ovarian.Chocolate Fluid': 7,
        'Deep Endometriosis': 8,
        'Ovarian.Endometrioma[B]': 9
    }
    prList, dsList, nameList, lesionList = getvidlist('Endometriosis', 'Data annotation')

    data_df = pd.DataFrame(
             {'Video Name': nameList, 'Project': prList, 'dataset': dsList})

    lespd = pd.DataFrame(lesionList)
    i =0
    for les in lesiondic:
        data_df[les] = lespd.loc[:, lesiondic[les]]
        i+=1

    sfpath = 'C:/Users/SurgAR-User/OneDrive/Documents/Saman/mypythonfolder/supervisely-python-sdk-example/my-gpysheets-3d8d13442005.json'
    sheetID = '1XEX4axQ96cSP7tprdbxL6TewmICepo4fowguvG-hTwc'
    sheetName = 'Endometriosis'
    data_df.to_excel('WP7.xlsx', sheetName)
    # write_to_gsheet(sfpath, sheetID, sheetName, data_df)


if __name__== '__main__':
    main()

