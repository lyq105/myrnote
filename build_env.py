#!/usr/bin/python
##=============================================================================
#   Project name:  Project name
#       Filename:  Filename
#   Descriptions:  Descriptions
#                  to generate the main contral file of latex.
#         Author:  liyiqiang(lyq105@163.com)
#         Create:  2011-06-22 21:11:10
#      Last edit:  2011-06-22 21:11:10
##=============================================================================


## there are steps for generate the main contral file.
## 1. read the head file.
## 2. scan the note directory to generate the content of notes.
## 3. add foot content.

## Notice: 
##   file encoding should be utf8.

import os
import os.path as osp
import shutil as sh
import codecs


## construct the document build env
def build_env():
	
	main_file = codecs.open ("main_file.tex","wb+","utf-8")

	head_text = codecs.open ("templates/head.tex","rb","utf-8").read()
	foot_text = codecs.open ("templates/foot.tex","rb","utf-8").read()
	#print head_text
	main_file.write(head_text)

	## Conectfile
	filelist = os.listdir( "notes" )
	filelist.sort()

	for filename in filelist:
		fname = osp.splitext(filename)[0]
		sux   = osp.splitext(filename)[1]

		if sux == '.tex':
			main_file.write(u"\\include{notes/" + fname + u"}\n")

		if sux == '.bib':
			sh.copy('notes/' + filename,'./')

	sh.copy('templates/bibstyle.bst', './')

	main_file.write(foot_text)
	main_file.close()

## compile rules for generate the main doc
def build_doc():
	main_file = "main_file"

	os.system("xelatex -quiet " + main_file)
	
	filelist = os.listdir( "./" )

	for filename in filelist:
		if osp.isfile(filename):
			fname = osp.splitext(filename)[0][0:2]
			#print fname
			sux   = osp.splitext(filename)[1]
			if fname == "bu" and sux == ".aux":
					os.system("bibtex " + filename)
					print filename


	os.system("xelatex " + main_file)
	os.system("xelatex " + main_file)
#os.system("xelatex -quiet " + main_file)
	#os.system("xelatex -quiet " + main_file)
	#os.system("dvipdfmx " + main_file)

	
## clean usless files
def clean_env():
	filelist = os.listdir( "./" )

	for filename in filelist:
		if osp.isfile(filename):
			sux   = osp.splitext(filename)[1]
			if sux != ".pdf" and sux != ".py" and sux != '.swp':
				print filename
				os.remove(filename)
	filelist = os.listdir( "notes/" )
	#print filelist
	for filename in filelist:
		#print filename
		if osp.isfile('notes/' + filename):
			#print filename
			sux   = osp.splitext(filename)[1]
			print sux
			if sux == ".aux":
				print filename
				os.remove('notes/'+filename)


if __name__ == "__main__":
	build_env();
	build_doc();
	print "Start clean docs!!"
	os.system("pause")
	clean_env();
