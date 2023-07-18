# -*- coding: utf-8 -*-
""" File Generation Handling for Delft 3d FM suite

Created on Fri May 26 15:05:33 2023
@author: aafur
"""
class FileGenerator:
    def __init__(self, file_name):
        self.file_name = file_name
        
    def generate_file(self):
        header = self._generate_header()
        body = self._generate_body()

        with open(self.file_name, 'w') as file:
            file.write(header)
            file.write(body)

    def _generate_header(self):
        # Implement header generation logic here
        pass

    def _generate_body(self):
        # Implement body generation logic here
        pass
