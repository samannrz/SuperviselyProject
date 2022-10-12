import supervisely as sly
import os
from functions import write_to_gsheet
import pandas as pd
import openpyxl


def find(s, ch):
    return [i for i, ltr in enumerate(s) if ltr == ch]


def unique(list1):
    # insert the list to the set
    list_set = set(list1)
    # convert the set to the list
    unique_list = (list(list_set))
    return unique_list

# Definition of Parameters
# Saman's Token
mytoken = 'jXCVEbySH8moyTXLihkoE1k9UX4fTMDUYkHMJgUoIzx0EnyS5outN8de6UvUCjdGfRUr8D553l8MhTLQkzDOm22bKTsJulgDiGzy2Z4yYEmFmhcsL8k37Af837qXb2UO'

# start using supervisely API
api = sly.Api(server_address="http://surgai-surgery.com", token=mytoken)

tm = api.team.get_info_by_name('Endometriosis')
ws = api.workspace.get_info_by_name(tm.id, 'Data annotation')
prs = api.project.get_list(ws.id)

nameList = []
projects = []
datasets = []

# lesions = []
lesionList = []
jj = 0

lesiondic = {
    'Adhesions.Dense':0,
    'Adhesions.Filmy':1,
    'Superficial.White':2,
    'Superficial.Black':3,
    'Superficial.Red':4,
    'Superficial.Subtle':5,
    'Ovarian.Endometrioma':6,
    'Ovarian.Chocolate Fluid':7,
    'Deep Endometriosis' :8
}
jj = 0
# get a list of supervisely video names with their corresponding project and dataset name
for pr in prs:
    if jj > 10:
        break
    dss = api.dataset.get_list(pr.id)
    for ds in dss:
        vds = api.video.get_list(ds.id)
        for vd in vds:
            nameList.append(vd.name)
            projects.append(pr.name)
            datasets.append(ds.name)
            ans = api.video.annotation.download(vd.id)
            objs = ans['objects']
            lesions = [0]*10
            for i in range(len(objs)):
                lesions[lesiondic[objs[i]['classTitle']]]=lesions[lesiondic[objs[i]['classTitle']]]+1
            lesionList.append(lesions)
            print (jj)
            jj+=1
            if jj>10:
                break







prList=projects
dsList=datasets
nameList=nameList

data_df = pd.DataFrame(
         {'Video Name': nameList, 'Project': prList, 'dataset': dsList})

lespd = pd.DataFrame(lesionList)
i =0
for les in lesiondic:
    data_df[les] = lespd.loc[:, lesiondic[les]]
    i+=1


data_df.to_excel('WP7.xlsx', 'Endometriosis')
