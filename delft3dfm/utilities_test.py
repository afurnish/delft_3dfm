# -*- coding: utf-8 -*-
"""
Created on Fri May 26 15:07:25 2023
@author: aafur
"""

import os
import argparse
import re

class FileManager:
    def choose_directory(self):
        parser = argparse.ArgumentParser()
        parser.add_argument("directory", help="Specify the project directory")
        args = parser.parse_args()
        directory = args.directory

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
            int(folder.split("_")[-1]) for folder in existing_homes
        ]

        # Find the next available version number
        next_version_number = max(version_numbers) + 1 if version_numbers else 1

        return str(next_version_number).zfill(3)  # Pad with leading zeros if necessary

    def create_delft_model(self, project_name=None, version_number=None):
        if project_name:
            # Working on a specific project without prompts
            selected_directory = project_name
            os.makedirs(selected_directory, exist_ok=True)
        else:
            # Select the directory for the Delft model
            selected_directory = self.choose_directory()

        if selected_directory:
            if os.path.isdir(selected_directory):
                # Print the folders in the selected project directory
                folders = [
                    folder for folder in os.listdir(selected_directory)
                    if os.path.isdir(os.path.join(selected_directory, folder))
                ]
                print("Folders in the project directory:")
                for folder in folders:
                    print(folder)

                if version_number:
                    # Check if the specified version number exists
                    selected_folder = f"delft3dfm_proj-{project_name}-{str(version_number).zfill(3)}"
                    if selected_folder in folders:
                        print(f"Selected version: {selected_folder}")
                    else:
                        print(f"Version {version_number} does not exist in the project directory.")
                        return None

            else:
                print("Invalid project directory.")
                return None

            # Continue with the rest of the code to create the necessary directories

            if not project_name:
                # Extract the project name from the selected directory
                project_name = os.path.basename(selected_directory)

            # Get a list of existing home directories within selected_directory
            existing_homes = [
                folder for folder in folders
                if folder.startswith(f"delft3dfm_proj-{project_name}-")
            ]

            # Extract the version numbers from the existing home directories
            version_numbers = [
                int(folder.split("-")[-1]) for folder in existing_homes
            ]

            # Find the next available version number if not specified
            if not version_number:
                next_version_number = self.get_next_version_number(selected_directory, project_name)
            else:
                next_version_number = version_number

            # Create the new home directory
            model_home = os.path.join(
                selected_directory, f"delft3dfm_proj-{project_name}-{str(next_version_number).zfill(3)}"
            )
            model_setup = os.path

if __name__ == '__main__':
    file_manager = FileManager()
    project_name = None  # Example project name
    version_number = None  # Example version number

    directory_paths = file_manager.create_delft_model(project_name, version_number)

    if directory_paths:
        print("Directory paths:")
        for key, value in directory_paths.items():
            print(f"{key}: {value}")
