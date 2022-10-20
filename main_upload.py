import os
import supervisely_lib as sly
from supervisely.task import progress

mytoken = 'jXCVEbySH8moyTXLihkoE1k9UX4fTMDUYkHMJgUoIzx0EnyS5outN8de6UvUCjdGfRUr8D553l8MhTLQkzDOm22bKTsJulgDiGzy2Z4yYEmFmhcsL8k37Af837qXb2UO'
api = sly.Api(server_address="http://surgai-surgery.com", token=mytoken)

project_id  = 996 # which project you are working?
dataset = 'Saman' # the name of the dataset. It can exist or nor
#project_name = 'Smoke Annotation'

##########################
ds_info = api.dataset.get_list(project_id)
# check if the dataset exists
for i in range(len(ds_info)):
    if dataset == ds_info[i].name:
        ds_id = ds_info[i].id

# if dataset does not exist
try:
    ds_id
except NameError:
    new_ds = api.dataset.create(project_id, dataset)
    ds_id = new_ds.id

vidpath = '/home/saman/Downloads/uploadfolder/'
video_names = os.listdir(vidpath)
video_paths = [vidpath + s for s in video_names]
print(video_paths)

video_infos = api.video.upload_paths(ds_id, names=video_names, paths=video_paths)