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

# Function to make url api request
def APIReq(db, searchVal, searchType, rand):
    os.system("cls")
    i = 0
    if rand == 0:
        if db == "omdbapi":
            #with urllib.request.urlopen('http://www.omdbapi.com/?'+searchType+'='+searchVal+'&apikey=2688c382') as response:
                #json = response.read()
            searchVal.replace(" ", "%20")
            http = urllib3.PoolManager()
            r = http.request('GET', 'http://www.omdbapi.com/?'+searchType+'='+searchVal+'&apikey=2688c382')
            print r.status
            print r.data
            j = json.loads(r.data)
            print json.dumps(j, sort_keys=True, indent=4, separators=(',', ': '))
            #print r.data
        elif db == "tmdb":
            with urllib.request.urlopen('http://www.omdbapi.com/?'+searchType+'='+searchVal+'&apikey=2688c382') as response:
                r = response.read()
    elif rand == 1:
        response = "False"
        while response == "False":
            searchType = "i"
            searchValA = ''.join(["%s" % random.randint(0, 9) for num in range(0, 7)])
            searchVal = 'tt' + searchValA
            print searchVal
            if db == "omdbapi":
                #with urllib.request.urlopen('http://www.omdbapi.com/?'+searchType+'='+searchVal+'&apikey=2688c382') as response:
                #json = response.read()
                searchVal.replace(" ", "%20")
                http = urllib3.PoolManager()
                r = http.request('GET', 'http://www.omdbapi.com/?'+searchType+'='+searchVal+'&apikey=2688c382')
                #print r.status
                #print r.data
                j = json.loads(r.data)

                response = j['Response']
                if response == 'True':
                    print json.dumps(j, sort_keys=True, indent=4, separators=(',', ': '))
                i=i+1

            elif db == "tmdb":
                with urllib.request.urlopen('http://www.omdbapi.com/?'+searchType+'='+searchVal+'&apikey=2688c382') as response:
                    r = response.read()
    print(i)
    print(type(response))

    return r

# system for formatting results?

for x in range(10):
    APIReq("omdbapi", "The Matrix", "t", 1)
