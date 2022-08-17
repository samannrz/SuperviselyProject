import pygsheets
import supervisely as sly
import pandas as pd


# The function to write to google sheet
def write_to_gsheet(service_file_path, spreadsheet_id, sheet_name, data_df):
    """
    this function takes data_df and writes it under spreadsheet_id
    and sheet_name using your credentials under service_file_path
    """
    gc = pygsheets.authorize(service_file=service_file_path)
    sh = gc.open_by_key(spreadsheet_id)
    try:
        sh.add_worksheet(sheet_name)
    except:
        pass
    wks_write = sh.worksheet_by_title(sheet_name)
    wks_write.clear('A1', None, '*')
    wks_write.set_dataframe(data_df, (1, 1), encoding='utf-8', fit=True)
    wks_write.frozen_rows = 1

def pdStats (teamName,workspaceName):

    # Saman's Token
    mytoken = 'jXCVEbySH8moyTXLihkoE1k9UX4fTMDUYkHMJgUoIzx0EnyS5outN8de6UvUCjdGfRUr8D553l8MhTLQkzDOm22bKTsJulgDiGzy2Z4yYEmFmhcsL8k37Af837qXb2UO'
    # start using supervisely API
    api = sly.Api(server_address="http://surgai-surgery.com", token=mytoken)

    # let's test that authentication was successful and we can communicate with the platform
    my_teams = api.team.get_list()
    print(f"I'm a member of {len(my_teams)} teams")

    # Define the team name
    tm = api.team.get_info_by_name(teamName)
    ws = api.workspace.get_info_by_name(tm.id, workspaceName)


    print('Here is %s team and %s workspace' % (tm.name, ws.name))
    prs = api.project.get_list(ws.id)
    prList = []
    prTypeList = []
    dsList = []
    vdList = []
    nframesList = []
    nAnnframesList = []

    for pr in prs:
        # if pr.type == 'videos'
        dss = api.dataset.get_list(pr.id)
        print('%d datasets in %s project' % (len(dss), pr.name))
        if pr.type == 'videos':
            for ds in dss:  # going  through datasets to collect their statistics
                vds = api.video.get_list(ds.id)
                nframes = 0
                nAnnframes = 0
                for vd in vds:
                    # print('%d : Total number of frames for %s'%(len(vd.frames_to_timecodes),vd.name))
                    ans = api.video.annotation.download(vd.id)
                    nframes = ans['framesCount'] + nframes  # count Total number of frames in the dataset
                    nAnnframes = nAnnframes + len(ans['frames'])  # count n of annotatedframes in the dataset
                prList.append(pr.name)
                prTypeList.append(pr.type)
                dsList.append(ds.name)
                vdList.append(len(vds))  # total number of videos in the dataset
                nframesList.append(nframes)
                nAnnframesList.append(nAnnframes)
        elif pr.type == 'images':
            for ds in dss:  # going  through datasets to collect their statistics
                imgs = api.image.get_list(ds.id)
                nframes = 0
                nAnnframes = 0
                for im in imgs:
                    # print('%d : Total number of frames for %s'%(len(vd.frames_to_timecodes),vd.name))
                    ans = api.annotation.download(im.id)
                    anots = ans.annotation
                    if len(anots['objects']) > 0:
                        nAnnframes = nAnnframes + 1

                prList.append(pr.name)
                prTypeList.append(pr.type)
                dsList.append(ds.name)
                vdList.append(len(imgs))  # total number of images in the dataset
                nframesList.append(0)
                nAnnframesList.append(nAnnframes)  # total number of annotated images in the dataset
    prCol = 'Project'
    prTypeCol = 'Type'
    dsCol = 'Dataset'
    vdCol = 'n. Videos / Images'
    nfCol = 'n. video Frames'
    nAnnCol = 'n. Annotated Frames / Iimages'
    prList.append('Total')
    prTypeList.append('')
    dsList.append('')
    vdList.append(sum(vdList))
    nframesList.append(sum(nframesList))
    nAnnframesList.append(sum(nAnnframesList))

    data_df = pd.DataFrame(
        {prCol: prList, prTypeCol: prTypeList, dsCol: dsList, vdCol: vdList, nfCol: nframesList,
         nAnnCol: nAnnframesList})
    print(data_df)
    return data_df
