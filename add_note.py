#!/usr/bin/python

# This script is used to creat a new note which inculde a note and bib.


import time
import os 

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

