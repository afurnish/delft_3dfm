# -*- coding: utf-8 -*-
"""
Created on Fri May 26 15:07:25 2023

@author: aafur
"""
#%% Dependencies 
import os
import easygui
import re
#%%
class FileManager:
    def choose_directory(self):
        directory = easygui.diropenbox(title="Select Directory")
        return directory

    
    def get_next_version_number(self, selected_directory, name):
        # Get a list of existing home directories for the given name
        existing_homes = [
            folder for folder in os.listdir(selected_directory)
            if os.path.isdir(os.path.join(selected_directory, folder))
            and folder.endswith("_delft3dfm_home")
            and folder.split("_", 2)[2].startswith(name)
        ]
    
        # Extract the version numbers from the existing home directories
        version_numbers = [
            int(folder.split("_")[0]) for folder in existing_homes
        ]
    
        # Find the next available version number
        next_version_number = max(version_numbers) + 1 if version_numbers else 1
    
        return str(next_version_number).zfill(3)  # Pad with leading zeros if necessary


    def create_delft_model(self, name):
        # Select the directory for the Delft model
        selected_directory = self.choose_directory()

        if selected_directory:
            # Check if the selected directory is already a home directory
            if "delft3dfm_home" in os.path.basename(selected_directory):
                # Retrieve the existing directory paths and return them
                model_home = selected_directory
                model_setup = os.path.join(model_home, "FlowFM_model_setup")
                model_outputs = os.path.join(model_home, "FlowFM_outputs")

                directory_paths = {
                    'model_home': model_home,
                    'model_setup': model_setup,
                    'model_outputs': model_outputs
                }
                return directory_paths

            else:
                # Get a list of existing home directories within selected_directory
                existing_homes = [
                    folder for folder in os.listdir(selected_directory)
                    if os.path.isdir(os.path.join(selected_directory, folder))
                    and folder.startswith("delft3dfm_home")
                ]

                # Extract the version numbers from the existing home directories
                version_numbers = [
                    int(folder.split("_")[2]) for folder in existing_homes
                ]

                # Find the next available version number
                next_version_number = max(version_numbers) + 1 if version_numbers else 1

                # Create the new home directory
                model_home = os.path.join(
                    selected_directory, f"delft3dfm_home_{str(next_version_number).zfill(3)}_{name}"
                )
                model_setup = os.path.join(model_home, "FlowFM_model_setup")
                model_outputs = os.path.join(model_home, "FlowFM_outputs")

                # Create the directory structure
                os.makedirs(model_setup, exist_ok=True)
                os.makedirs(model_outputs, exist_ok=True)

                directory_paths = {
                    'model_home': model_home,
                    'model_setup': model_setup,
                    'model_outputs': model_outputs
                }
                return directory_paths

        return None

    
if __name__ == '__main__':
    
   
    
#%% File Manager processes that dont work as cant get easygui
    file_manager = FileManager()
    model_name = 'kent_estuary3'  # Example model name
    directory_paths = file_manager.create_delft_model(model_name)
    
    directory_paths = directory_paths if directory_paths else {}

