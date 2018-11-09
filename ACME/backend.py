"""
Func List:
    findrand
    searchbox
    movetoMyList
    AddToList - +rating&status keys
    change status
    change rating
    remove from list

    calculate total time
    calculate score deviation





    {
        ]
            film: "title"
            plot: "stuff happened"
            rating: 5
            status: "watched"
        ]
    }


"""



"""

    API URL: http://www.omdbapi.com/?i=tt3896198&apikey=2688c382
    API URL: http://www.omdbapi.com/?type=series&t=Batman&apikey=2688c382

    Parameter	  Required	    Valid Options	        Default Value	Description
    i  	          Optional*		                        <empty>	        A valid IMDb ID (e.g. tt1285016)
    t	          Optional*		                        <empty>	        Movie title to search for.
    type	      No	        movie, series, episode	<empty>	        Type of result to return.
    y	          No		                            <empty>	        Year of release.
    plot	      No	        short, full	            short	        Return short or full plot.
    r	          No	        json, xml	            json	        The data type to return.
    callback      No		                            <empty>	        JSONP callback name.


"""

# Imports
import urllib3
import json
import random
import os
from decimal import Decimal

# Variables
personallist = []
searchcontent = []
searchresult = []

# Function to make url api request
# e.g. APIReq("omdbapi", "The Matrix", "t", 0)
# e.g. APIReq("omdbapi", "", "", 1)
def APIReq(db, searchVal, searchType):
    os.system("cls")
    if db == "omdbapi":
        searchVal = searchVal.replace(" ", "%20")
        http = urllib3.PoolManager()
        r = http.request('GET', 'http://www.omdbapi.com/?'+searchType+'='+searchVal+'&apikey=2688c382')
        j = json.loads(r.data)
        j['Status'] = ""
        j['Rating'] = 0
        #print json.dumps(j, sort_keys=True, indent=4, separators=(',', ': '))
        searchcontent.append([db, searchVal, searchType])
        searchresult.append(j);
    elif db == "tmdb":
        with urllib.request.urlopen('http://www.omdbapi.com/?'+searchType+'='+searchVal+'&apikey=2688c382') as response:
            r = response.read()
    return j


def APIReqRandom(db):
    os.system("cls")
    i = 0
    response = "False"
    while response == "False":
        searchVal = 'tt' + ''.join(["%s" % random.randint(0, 9) for num in range(0, 7)])
        if db == "omdbapi":
            searchVal = searchVal.replace(" ", "%20")
            http = urllib3.PoolManager()
            r = http.request('GET', 'http://www.omdbapi.com/?i='+searchVal+'&apikey=2688c382')
            j = json.loads(r.data)
            response = j['Response']
            if response == 'True':
                #print json.dumps(j, sort_keys=True, indent=4, separators=(',', ': '))
                j['MyStatus'] = ""
                j['Rating'] = 0
                searchresult.append(j);
            i=i+1

#        elif db == "tmdb":
#            with urllib.request.urlopen('http://www.omdbapi.com/?'+searchType+'='+searchVal+'&apikey=2688c382') as response:
#                r = response.read()
    print(i)
    return j

#Read & update JSON file

def ListIO(opt):
    if opt == "load":
        with open('ls.json', 'r') as json_file:
            personallist = json.load(json_file)
    elif opt == "save":
        with open('ls.json', 'w') as json_file:
            json.dump(personallist, json_file)

    return personallist

#Copy new item to list, adding keys for "Status" and "Rating"
def ListAddition(newContent): #what type is newcontent?
    r = 0
    l = len(personallist)
    personallist.append(newContent)
    return r

#Removal of item from list
def ListRemoval(id):
    r = 0
    for k in personallist:
        if k == id:
            personallist.pop(id, None)
            r = 1
    return r

#Update rating key for individual item in list
def ChangeRating(id, rating):
    r = 0
    for k in personallist:
        if k == id:
            personallist[k]['Rating'] = rating
            r = 1
    return r

#Change status from watching->pending or pending->watching
#NOTE: the user mmay accidentally change a film. This is wwhy we need 2-way flipflop
def ChangeStatus(id, newStatus):
    #Set status of id to newstatus
    r = 0
    for k in personallist:
        if k == id:
            personallist[k]['MyStatus'] = newStatus
            r = 1
    return r


#Calculate the total time from all items in list
def CalcTime():
    rt = 0
    for k in personallist:
         tmp = personallist[k]['Runtime']
         tmp = tmp.replace("m", "")
         tmp = tmp.replace("in", "")
         rt = rt + tmp
    return rt

#Calculate the average deviation from the ratings
def CalcRating():
    summ = Decimal(0)
    personallistTEMP = personallist

    for k in personallistTEMP:
        my = k['Rating']
        their = Decimal(0)

        for j in k['Ratings']:
            #print(j)
            tmp = j['Value']
            if j['Source'] == "Internet Movie Database":
                tmp = Decimal(tmp.replace("/10", ""))
                #print(tmp)
            if j['Source'] == "Rotten Tomatoes":
                tmp = Decimal(tmp.replace("%", ""))/10
                #print(tmp)
            if j['Source'] == "Metacritic":
                tmp = Decimal(tmp.replace("/100", ""))/10
                #print(tmp)
            their += tmp
        print("===============================")
        print(their)
        print(type(len(k['Ratings'])))
        print(type(summ))
        print("-------------------------------")
        summ += Decimal(their / len(k['Ratings']))
    ret = Decimal(summ/ len(personallistTEMP))

    return ret




"""
Func List:
1    findrand
    searchbox
    movetoMyList
1    AddToList - +rating&status keys
1    change status
1    change rating
1    remove from list

1    calculate total time
    calculate score deviation
"""



# system for formatting results?
ListAddition(APIReq("omdbapi", "The Matrix", "t"))
ListAddition(APIReqRandom("omdbapi"))
ListAddition(APIReq("omdbapi", "Godzilla", "t"))

print"--------------------------------------------------------------"
print"--------------------------------------------------------------"
print"--------------------------------------------------------------"

print(CalcRating()) # This is returning 0..

#print searchcontent
#print searchresult




#APIReqRandom("omdbapi")
