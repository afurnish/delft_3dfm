# -*- coding: utf-8 -*-
"""
Created on Tue Jun  6 16:26:17 2023

@author: aafur
"""
from o_functions.start import opsys2; start_path = opsys2()
#store all vid_preparation functions here as functions. 
#%% Path Structure
def folder_maker():
    mother_folder = r'/5.Final/1.friction'
    fn, number = scw_nc_choice(start_path,mother_folder)

    beg_path = start_path + r'modelling_DATA/kent_estuary_project' ; end_path = r'\FlowFM\DFM_OUTPUT_FlowFM'
    
    
    #change mother_folder when you change when you save delft files to diff locations.
    home_folder = r'/' + number + '_kent_validation_delft_2019.dsproj_data'  # change this
    fig_output_folder = r'/' + number + '_SCW' # change this
    # name of folders that hold respective pngs from file processing
    n = r'/kent_'+ number +'_water_depth(m)' # name of the water depth pngs
    n2 = r'/kent_'+ number +'_surface_height(m)' # name of the water surface height pngs
    n3 = r'/kent_'+ number +'_salinity(ppt)' # name of the salinity profile ppt pngs
    # variables folders 
    wd_png_folder = r'/water_depth_png'
    sh_png_folder = r'/mesh2d_S1_png'
    sa_png_folder = r'/mesh2d_sa1_png'
    val_folder = r'/val_folder_png'
    stats_folder = r'/stats_data'
    stats_figures = r'/stats_figures'
    
    #
    out = r'/outputs'
    main_path = beg_path + mother_folder + out + fig_output_folder
    water_depth_figurepath = main_path + wd_png_folder
    mesh2d_s1_figurepath =  main_path + sh_png_folder
    mesh2d_sa1_figurepath = main_path + sa_png_folder
    val_figurepath = main_path + val_folder
    videopath = beg_path + mother_folder + out + fig_output_folder + r'/giffs'
    folder_path = beg_path + mother_folder + out + fig_output_folder
    path = beg_path + mother_folder + home_folder + end_path
    output_folder = beg_path + mother_folder + out
    stats_path = folder_path + stats_folder
    
    
    # Path to mask layer
    UKWEST_loc = start_path + r'modelling_DATA/kent_estuary_project/land_boundary/QGIS_Shapefiles/UK_WEST_POLYGON_NEGATIVE.shp'
    UKWEST = gpd.read_file(UKWEST_loc)
    
    
    
    
    return folder_paths
