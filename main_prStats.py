from functions import *
import datetime

import datetime
from functions import *

# surgai-surgery (This is Saman's token)
mytoken = 'jXCVEbySH8moyTXLihkoE1k9UX4fTMDUYkHMJgUoIzx0EnyS5outN8de6UvUCjdGfRUr8D553l8MhTLQkzDOm22bKTsJulgDiGzy2Z4yYEmFmhcsL8k37Af837qXb2UO'

# Free supervisely (This is Saman's token)
mytoken = '0OmEfZ2wTF8j1oq6Tx6Y16mcGXRm1zToFB2gXTpkGqsEQIOXflIILpXjrBz6CpzJaiC0uP5gOgxo4XEJBfX4lMAu8DSaguK4XYD7eIt3eP50ZmXy64RqDwQ5KMDla7lY'

teamName = 'sabrinamadad'
workspaceName = 'First Workspace'

teamName = 'Endometriosis'
workspaceName = 'Data Annotation'
sfpath = 'keycode/my-gpysheets-3d8d13442005.json'
sheetID = '1nf_MApxQjGKhriQOsApIZNtDIuDJEC0cK2FjTqZjquU'
datadf = pdStats(mytoken, teamName, workspaceName)
sheetName = teamName + '/' + workspaceName + str(datetime.date.today())
write_to_gsheet(sfpath, sheetID, sheetName, datadf)
