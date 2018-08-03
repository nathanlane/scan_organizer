# Readme: scan_organizer

The following is a project for organizing a mass scanning project. 

The aim of this project is to take a folder of many hi-resolution scans and organize them. This script takes an folder of raw, scanned images as input. Each image corresponds to a page of a periodcal that was shot onto microfilm. 

However, as is typical with microfilming projects, many periodicals were stored onto the microfilm. So we need to figure out which sequence of scans represents a standalone document. In other words: from a pile of images (1.tif, 2.tif,...,1000.tif) , we need to figure out where a new periodical starts and ends.

This project will utilize use a simple computer vision process to help us automate the sorting process.