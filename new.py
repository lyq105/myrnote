#!/bin/python
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

def build_main_file():
	
	main_file = codecs.open ("main_file.tex","wb+","utf-8")

	head_text = codecs.open ("templates/head.tex","rb","utf-8").read()
	foot_text = codecs.open ("templates/foot.tex","rb","utf-8").read()
	#print head_text
	main_file.write(head_text)

	## Conectfile
	filelist = os.listdir( "notes" )
	for filename in filelist:
		#print osp.splitext(filename)[1] == '.tex'
		fname = osp.splitext(filename)[0]
		sux   = osp.splitext(filename)[1]
		if sux == '.tex':
			#print filename
			main_file.writelines(u"\\input{notes/" + fname + u"}\n")

	main_file.write(foot_text)
	main_file.close()

def build_pdf_file():
	sh
