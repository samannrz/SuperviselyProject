import pandas as pd
import supervisely as sly
import pandas as pd
#tests#
# Saman's Token
mytoken = 'jXCVEbySH8moyTXLihkoE1k9UX4fTMDUYkHMJgUoIzx0EnyS5outN8de6UvUCjdGfRUr8D553l8MhTLQkzDOm22bKTsJulgDiGzy2Z4yYEmFmhcsL8k37Af837qXb2UO'

api = sly.Api(server_address="http://surgai-surgery.com", token=mytoken)

# let's test that authentication was successful and we can communicate with the platform
my_teams = api.team.get_list()
print(f"I'm a member of {len(my_teams)} teams")

# Define the team name
tm = api.team.get_info_by_name('Endometriosis')
ws = api.workspace.get_info_by_name(tm.id, 'Data annotation')
print('Here is %s team and %s workspace' % (tm.name, ws.name))
prs = api.project.get_list(ws.id)
prList = []
dsList = []
vdList = []
nframesList = []
nAnnframesList = []

for pr in prs:
    print(pr)