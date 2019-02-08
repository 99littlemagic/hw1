#!/usr/bin/python

import sys
import re

def extract_names(filename):
  """
  Given a file name for baby<year>.html,
  returns a list starting with the year string
  followed by the name-rank strings in alphabetical order.
  
  ['2006', 'Aaliyah 91', Aaron 57', 'Abagail 895', ' ...]

  If this seems too daunting, return

  ['2006', (male_name,rank), (female_name,rank), ....]

  The names and ranks are pairs rather than strings and they
  do not have to be sorted. For example the list might begin

  ['2006', ('Jacob','1'), ('Emma','1'), ...]
  
  """
  #a = open('baby1990.html').read()
  a=open(filename).read()


  ## 1. Extract all the text from the file and print it

  # <td>1</td><td>Michael</td><td>Jessica</td>
  # <td>(.*?)</td> is the regular expression to locate the target lines
  pattern = re.compile(r'<td>(.*?)</td>',re.S)
  items = re.findall(pattern, a)
  # modify the first item
  items[0]='1'
  print(items)


  # 2. Find and extract the year and print it

  # <h3 align="center">Popularity in 1990</h3>
  # <h3 align="center">(.*?)</h3> is the regular expression to locate the target lines
  pattern2 = re.compile(r'<h3 align="center">(.*?)</h3>',re.S)
  year = re.findall(pattern2, a)
  m=str(year)
  # extract the year
  m=m[16:20]
  print(m)


  # 3. Extract the names and rank numbers and print them

  # create the new list
  name_list=[]
  i=0
  while i <=(len (items) -3):
   name_list.append(str(items[i+1]+' '+items[i]))
   name_list.append(str(items[i+2]+' '+items[i]))
   i=i+3
  
  print(name_list)


  # 4. Get the names data into a dict and print it
  # choose whichever number is smaller for a name appears more than once
  tuples = re.findall(r'<td>(\d+)</td><td>(\w+)</td>\<td>(\w+)</td>', a)

  # creat a dict to store name and number
  # each name is a key
  # so if a name is already stored, it will not be added
  
  name_rank =  {}
  for rank_tuple in tuples:
   (rank, boyname, girlname) = rank_tuple  # unpack the tuple into 3 vars
   if boyname not in name_rank:
      name_rank[boyname] = rank
   if girlname not in name_rank:
      name_rank[girlname] = rank
  # print the dict
  print(name_rank)

  # 4. Build the [year, 'name rank', ... ] list and print it

  # sort the dict based on key
  sorted_name = sorted(name_rank.keys())

  # creat the result list
  name_result_list=[m]
  for name in sorted_name:
   name_result_list.append(name + " " + name_rank[name])
    
  # print the new list
  #print(name_result_list)


  

  return name_result_list



    
def main():
  # This command-line parsing code is provided.
  # Make a list of command line arguments, omitting the [0] element
  # which is the script itself.

  if len(sys.argv) == 2:
    arg = sys.argv[1]
    
    
  else:
    print("usage: ", sys.argv[0], "filename")
    sys.exit(1)

  mylist=extract_names(arg)
  text = '\n'.join(mylist) + '\n'
  print(text)
   

  # For each filename, get the names, then print the text output
  
 

  print('Yes, you are running the script correctly!')
 
if __name__ == '__main__':
  main()






