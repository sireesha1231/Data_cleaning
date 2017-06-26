PART 2: Reformatting Data: Super Bowl Champions

README:
Solution:
1. Import BeautifulSoup Library
//How to install BeautifulSoup Library
	1.1. Download the latest version from:
		http://www.crummy.com/software/BeautifulSoup/
	1.2. Extract the files
	1.3. Open terminal and go to the location where the library is installed
	1.4. Execute the following command:
		sudo python setup.py install
	1.5. This will create the build folder in the same folder and now BeautifulSoup can be used. 

2. Read the ‘superbowl.html’ file

3. Create an array that will store all the data which is mydata[]

4. BeautifulSoup will read the html file and extract the content using ‘html.parser’

5. Do the following:
	5.1. Select the div containing the table which has an id #mw-content-text
	5.2. Find its child(table)
	5.3. Find the table’s child(rows)
	5.4. Find the row’s child(cells)

6. Each cell has a span class. Depending on the data that we wish to extract we specify the index of the span class, retrieve the text, strip off whitespaces from the end of the string.

7. Print 1 to 50 rows of this page running in a ‘for’ loop.

8. DONE!!!!