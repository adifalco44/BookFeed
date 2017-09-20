Our project desription tomorrow can be an edited version of this file. I added notes about how we can make things more clear. Please add notes 
or delete mine if you disagree -Anthony


// Day One

	// Ideas

	We determined the primary goal of the project is to create a system by which users can be inspired and drawn to literary sources of 
imformation to aid understanding of literary topics.//-insert fluffy statement about fake news/increased casual library consumption for the report-// We live
in an era where we can acess stories from around the world in an instant, but it can be difficult to find sources that verify claims made in these
areas. Our mock application, BookFeed, will attempt to create a system that sorts through stories from popular subreddits and pertinent library resources
on similiar topic so users can educate themselves appropriately. // - maybe to fluffy --> // The importance of this mission cannot be understated. 
In addition we will attempt to use user search // <-- should be library checkout history --> // history to inform the type of literary source we choose i.e. (books, scholarly 
articles, web articles, etc...). // -insert statement about relevance to information overload-->//

	//Pulling titles from Reddit

	We pulled the some of the most popular subreddits ( worldnews, politics, science, technology, Futurology, sports, books ) and we created a 
program to pull the top stories from each subreddit (ranking done by Reddit). // <-- talk about technique- // We alse developed a tool to pull keywords from these titles by 
eliminating the most common english words and useless punctuation. Our next goal is to match these keywords with the cataloged infromation on each 
book using the <title>,<creator>, and <subject>




// Work Flow Diagram

Top Level:

    BookFeed.py --> a python script that calls functions to produce linked static html pages
                --> takes in user input and generates HTML1 (TEST)
                --> Scrapes HTML one for keywords and based on articles and searches archives
                --> Pushes formatted data into linked list struct (Book/Article && KeyWordCount data)
                --> Trims list to ten
                --> generates linkes for book recommendations

Second Level:
    CreateBookList.py --> Remove common words from subreddit titles
                      --> Generate two dimensional vector of string<int>
                            --> Calls list Listify(FILE stream, vector<string>)
                            --> Requests entry information from API using keywords found in subReddit title
                            --> Calls vector <string> InterpretData(list <string>)
                                --> Returns KeyWord Count and Book Information as a string
                                --> If keywordcount > popFront(list).keywordcount --> PushFront 
                      --> Format Maybe?
    GenerateHTML.py
                    --> Push CreateBookList.py values into string formatting variables
                    --> Generate Linked HTML
    


Helper Level:


    
