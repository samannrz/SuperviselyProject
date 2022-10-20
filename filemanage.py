import supervisely as sly

mytoken = 'jXCVEbySH8moyTXLihkoE1k9UX4fTMDUYkHMJgUoIzx0EnyS5outN8de6UvUCjdGfRUr8D553l8MhTLQkzDOm22bKTsJulgDiGzy2Z4yYEmFmhcsL8k37Af837qXb2UO'
path = "C://Users/SurgAR-User/OneDrive/Documents/Surgar/Female/Rigas first Results/BAD2/BAD"
teamName = 'Endometriosis'
workspaceName = 'Data annotation'

# start using supervisely API
api = sly.Api(server_address="http://surgai-surgery.com", token=mytoken)

tm = api.team.get_info_by_name(teamName)
files = api.file.list(tm.id, '/Endometriosis_WS3/Semmelweis')
vds = api.video.get_list(1551)

for vd in vds:
    print(vd.name)

# ws = api.workspace.get_info_by_name(tm.id, workspaceName)
# prs = api.project.get_list(ws.id)
