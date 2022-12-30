# This script is to download videos from a workspace to a local path

import os
import supervisely_lib as sly

# Define the parameters
#src_project_name = 'Endometriosis_WS1'
project_id = 760
WORKSPACE_ID = 33

##########################
mytoken = 'jXCVEbySH8moyTXLihkoE1k9UX4fTMDUYkHMJgUoIzx0EnyS5outN8de6UvUCjdGfRUr8D553l8MhTLQkzDOm22bKTsJulgDiGzy2Z4yYEmFmhcsL8k37Af837qXb2UO'
api = sly.Api(server_address="http://surgai-surgery.com", token=mytoken)
try:
    src_project_name
except NameError:
    src_project_name = api.project.get_info_by_id(project_id).name

#### End settings. ####

project = api.project.get_info_by_name(WORKSPACE_ID, src_project_name)
if project is None:
    raise RuntimeError('Project {!r} not found'.format(src_project_name))

if project.type != str(sly.ProjectType.VIDEOS):
    raise RuntimeError('Project {!r} has type {!r}. This script works only with video projects'
                       .format(src_project_name, project.type))

dest_dir  = os.path.join(os.getcwd(),src_project_name)
sly.fs.mkdir(dest_dir)
print(dest_dir)
sly.download_video_project(api, project.id, dest_dir, dataset_ids=None, log_progress=True)
sly.logger.info('Project {!r} has been successfully downloaded'.format(src_project_name))
