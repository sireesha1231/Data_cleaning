PART 1: Entity Resolution: UIC Courses


README:
Solution:
1. Import the Regular Expression module

2. Import the spell checker library i.e. ‘Autocorrect’.
	//How to install autocorrect
	2.1. Download the tar ball from the following link:
		https://pypi.python.org/pypi/autocorrect/0.2.0
	2.2. Extract the files
	2.3. Open terminal and go to the location where the library is installed
	2.4. Execute the following command:
		sudo python setup.py install
	2.5. This will create the build folder in the same folder and now autocorrect can be used. 
(ex: 
>>spell(‘Hellllo’) 
>>’Hello’
)

3. Name Clean Function:
	3.1. Find the comma in the name string and partition at the comma.
	3.2. Flip the first name and last name and capitalize both the words.
	3.3. Strip off any whitespaces if any.
	3.4. If there are any dots in the name, replace them with a whitespace.
	3.5. Split the string by cutting off the first name using split()[-1] and capitalize the last name.

4. Course Clean Function:
	4.1. Using regular expressions, run a spell check using the autocorrect library on all the courses.
	4.2. Using regular expressions, replace all intro, intro. and Intro with Introduction.
	4.3. Simply replace ‘&’ with ‘and’.
	4.4. Capitalize all the course names and remove whitespaces using strip()

5. Read Data Function:
	5.1. Open the file.
	5.2. Create an array ‘mydata’ that will store all the data that needs to be manipulated.
	5.3. Create a list called ‘row’.
	5.4. Partition each line at ‘-‘ as professor name on the left and courses on the right.
	5.5. Split the courses at ‘|’.
	5.6. Apply the name and course cleaning functions on prof_name and course.
	5.7. Finally append the cleaned row to mydata array.

6. Write Data Function:
	6.1. Open the output file i.e. ‘cleaned.txt’ in writable format.
	6.2. Print the data in the same format as the input file.

  