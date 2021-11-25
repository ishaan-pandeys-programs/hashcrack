# hashcrack
A python software that can be used for cracking six different types of hashes such as SHA384, SHA512, SHA224, SHA1, SHA256 and MD5 through a dictionary attack using an online txt file.

You need to have python 3 or above installed to run this progam. 

If you would like to change the online dictionary url, use CTRL+F in your text editor and search for this line:

<code>LIST_OF_WORDS = str(urlopen('https://raw.githubusercontent.com/dwyl/english-words/master/words.txt').read(), 'utf-8')</code> 

Change the url in the urlopen function and replace all instances with your version of the above line.

If you want to use a txt dictionary stored in your computer, then, well, nothing. Unless the word search fails with the online dictionary, you can't use a txt dictionary. But don't worry; you just have to store your txt on github (like the default dictionary above).
