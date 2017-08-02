# Python_WordCount_URL
The purpose of this python program is to count the number of words on a webpage. 

This can be useful for bloggers implementing SEO (Search Engine Optimization). Having a higher word count on your webpage, allows you to rank higher in a google search result page. 

Usually I have to copy and paste the words on a webpage to a word counting application like Word.

This program has two main benefits. It speeds up the process of discovering the word count on a page. And it stores the results to a text file.

The program requests a URL and then gives back the word count on the webpage. After outputting the word count, the results are stored in a dictionary as (URL, wordcount). 

The user can type in ‘list’ to see all the results in that session. This part of the program also gives the average word count so far. This can be helpful in finding the ideal amount of words on a blog post.  

After the user types ‘quit’ they are asked if they would like to save the results. If they select no, the program exits, if they enter yes, they are asked what they want their file to be called. The program stores the results in a text file, at the location where the program is running.

It uses BeautifulSoup 4 and Pythons default urlopen to open the url.

If you have any suggestions for improvement, please let me know.  
