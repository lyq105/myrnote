#!/bin/bash
## Script for build pdf files of this project.



xelatex main_file

for bufile in `ls bu*.aux`
	do
		bibtex $bufile
	done

xelatex main_file
xelatex main_file
#dvipdfmx main_file

#rm *.aux *.dvi *.out *.toc *.blg *.bbl
