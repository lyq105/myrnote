#!/bin/bash
## Script for build pdf files of this project.



latex main_file

for bufile in `ls bu*.aux`
	do
		bibtex $bufile
	done

latex main_file
latex main_file
dvipdfmx main_file

#rm *.aux *.dvi *.out *.toc *.blg *.bbl
