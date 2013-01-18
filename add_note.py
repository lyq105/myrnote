#!/usr/bin/python

# This script is used to creat a new note which inculde a note and bib.


import time
import os 
import os.path as osp

## generate the note list.

def note_list():

	note_data = []

	filelist = os.listdir( "notes" )
	filelist.sort()

	for filename in filelist:
		sux   = osp.splitext(filename)[1]

		if sux == '.tex':

			note_date = filename[0:4]+"-"+filename[4:6]+ "-" + filename[6:8]
			for line in open("notes/"+filename).readlines():
				if line.find("\\section") != -1:
					#print line.split("{")[1].split("}")[0].decode("utf-8").encode("gbk")
					#section_name = line.split("{")[1].split("}")[0].decode("utf-8").encode("gbk")
					section_name = line.split("{")[1].split("}")[0]
					note_data.append([filename, note_date, section_name])
					
	#print tex_file_list
	return note_data
	
def print_note_data():
	note_data = note_list()
	index = 0
	for record in note_data:
		if index < 10:
			print "["+ str(index) +"].   " + "(" + record[1] + ") " + record[2]
		else:
			print "["+ str(index) +"].  " + "(" + record[1] + ") " + record[2]
		index = index + 1


def add_note():
	# 1 determine the note title.
	note_date = time.strftime('%Y%m%d',time.localtime(time.time()))
	note_title = note_date + raw_input("Please input the note title:")

	note = open('notes/' + note_title + '.tex','w')
	note.write(
	'''
	%% setup reference database.
	'''
	+
	'\\bibliography*{' + note_title +'}'
	'''
	\\bibliographystyle*{bibstyle}     %% setup reference style.
	%% Section title
	\section{<++>}
	'''
	+
	'''
	%% list references if any.
	'''
	+
	'\putbib[' + note_title +']'
	'''
	\\newpage
	'''
	)
	note.close()
	
	bib = open('notes/' + note_title + '.bib','w')
	bib.write(
	"""
	%% If there is any bibliography, Please list it below.
	"""
	)
	bib .close()

	## use gvim to edit them.
	os.system('gvim -O ' + 'notes/' + note_title + '.tex'+' notes/' + note_title + '.bib')

def edit_note():
	print "Chose which notes should be edited:"
	print_note_data()
	index = int(raw_input("Your choice is :[]"))
	note_title = osp.splitext(note_list()[index][0])[0]

	## use gvim to edit them.
	os.system('gvim -O ' + 'notes/' + note_title + '.tex'+' notes/' + note_title + '.bib')




def main_program():
	print "0. Print note list."
	print "1. Edit existed note.  "
	print "2. Add a new note."
	print "Default optiont is [0]"
	input_option = raw_input("Please chose an option:[0]")

	if input_option == "1":
		edit_note()
	else:
		if input_option == "2":
			add_note()
		else:
			print_note_data()
			os.system("pause")
	

if __name__ == "__main__":
	main_program()
	#print_note_data()

