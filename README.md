FontCompare
===========

To implement a tool for improving the aesthetic quality of fonts of Indic scripts

Project Abstract
----------------

There are a lot of fonts for Roman scripts but when it comes to fonts for Indic scripts like Devanagri, Bengali, Telugu, there is a dearth of good quality Open Type fonts. This tool would facilitate in providing tests enabling Font developers to contribute more to Open Type Indic fonts.

This project is part of Google Summer of Code 2013.

Student Name: Mayank Jha

Mentor: Shreyank Gupta

Melange URL: http://www.google-melange.com/gsoc/project/google/gsoc2013/mjnovice/42001

How to Install and Run the application: 

A) Installation

    1. Change into the folder containing the source. 

    2. As this is a fontforge utility so to be able to use it you need to
		install the fontforge bindings for python onto your system.
		
		Run the required command on the terminal as given below
		
		For Debian based Linux distros:

			sudo apt-get install python-fontforge
		
		For Redhat based Linux distros:

			yum install fontforge-python

    3. Run "sudo python setup.py install" from the shell prompt, supply the 
        password if prompted for.

B) Running
    From the shell prompt, type in "fontcompare" and you would be able to
    run and use the application. 

C) How to Use:
    The very basic feature of Font Compare is to compare two fonts based 
    on their glyphs, bearing, size and many other factors.
    
    Basic Usage Steps:
    i) Click on Load Test font button , which would load the font to be
       tested.
    
    ii) Click on Load Standard font Button, which would load the standard
        font against which the font would be tested.
    
    iii) Now click on the Execute button to run the various tests.
    
    You can see that the detailed glyph wise test results can be viewed 
    in the lower right corner, whereas categorised scored based on the
    degree of similarity can be seen graphically in the upper part of the 
    GUI.
