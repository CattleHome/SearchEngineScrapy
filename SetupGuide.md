## Mac Setup Guide  to Install Web Crawler
  
Note: All `grey highlighted` lines are terminal commands. You can do this in a single shell window.

### Before Setting Up crawler  

**Step 1:**  
You need to have Homebrew (package manager for Mac) on you mac.  
You can check if it is installed by typing: `brew --version`  
If you don't have Homebrew, use below command to install it. _Otherwise, skip this step and move to Step 2._  
    
Type command:  
`/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"`  
(This installs Homebrew)  
   
**Step 2:**  
You need to install Python 2. The below command will check if system has Homebrew Python and will install it if it not present. This will ensure that System python is not touched in the process.  
`brew install python@2`  
(This installs latest Python2)  
   
**Step 3:**  
`pip` and `virtualenv` are two more things required for the crawler.  
To Install `pip`,  
use Command:  
`easy_install pip`  
(Type `pip --version` to see if it is installed correctly)  
   
To Install `virtualenv`,  
use Command:  
`pip install virtualenv`   
(Type `virtualenv --version` to see if it is installed correctly)  
  
  
### Setting up crawler  
1. Copy SearchEngineScrapy folder from location mentioned in the email (say : \\indstore\transfer\neyazee\ForAbhigyan) to any directory (Example: ~/Documents/)  
2. `cd SearchEngineScrapy`   
3. `virtualenv -p python venv`  
4. `source venv/bin/activate`  
5. `pip install -r requirements.txt`  (You need to re-run this command if this throws an error after accepting prompt to install xcode cmdline tools.)
  
  
### Running the Crawler  
1. Goto SearchEngineScrapy folder  (Example : `cd ~/Documents/SearchEngineScrapy/` : If it placed in Documents)  
2. `source venv/bin/activate` (Activate virtualenv)  
   
  
_Run commands now to crawl the results:_  
Example (To crawl 5 pages of Google search results for PDFs with keyword 'Machine Learning' and store URLs in output_filename.csv):  
   
`scrapy crawl SearchEngineScrapy -a searchQuery="Machine Learning" -a fileType="pdf" -a searchEngine="Google" -a pages=1 -o output_filename.csv`   

(output_filename will contain URLs that are of filetype: pdf and query: 'Machine Learning')
  
### Parameters of the Crawler  
| Parameter       | Prefix | Description                                  | Options                       | Required | Default |
|-----------------|--------|----------------------------------------------|-------------------------------|----------|---------|
| searchQuery     | -a     | Search Query                                 | -                             | Y        | -       |
| fileType        | -a     | Filetype that you want to search for         | pdf/csv/zip/doc/docx/jpeg/png | Y        | -       |
| searchEngine    | -a     | Search Engine you want to use                | Google/Bing                   | N        | Bing    |
| pages           | -a     | Number of pages to crawl                     | -                             | N        | 3       |
| output_filename | -o     | name of output file where results are dumped | json/jsonl/csv/xml            | N        | -       |
