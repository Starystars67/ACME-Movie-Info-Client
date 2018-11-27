// Backend Functionality but will be loaded into the client side UI.

/*

    API URL: http://www.omdbapi.com/?i=tt3896198&apikey=2688c382
    API URL: http://www.omdbapi.com/?type=series&t=Batman&apikey=2688c382

    Parameter	  Required	    Valid Options	        Default Value	  Description
    i  	        Optional*		                        <empty>	        A valid IMDb ID (e.g. tt1285016)
    t	          Optional*		                        <empty>	        Movie title to search for.
    type	      No	        movie, series, episode	<empty>	        Type of result to return.
    y	          No		                              <empty>	        Year of release.
    plot	      No	        short, full	            short	          Return short or full plot.
    r	          No	        json, xml	              json	          The data type to return.
    callback    No		                              <empty>	        JSONP callback name.

*/


//var personallist;// = [];
//var searchcontent;// = [];
//var searchresult;// = [];


const DEBUG = true;

function SearchButton() {
  HidePages();
  var val = $('#searchVal').val();
  $('#searchcriteria').html(val);
  $('.search').show();
  APIReq('omdbapi', val, 's')
}

$('#searchButton').click(function() {
  alert( "Handler for .click() called." );
  SearchButton();
});

function HidePages() {
  $('.page').hide(); // hides
}

// Function to query debug
function APIReq (db, searchVal, searchType) {
  if (db == 'omdbapi') {
    $.getJSON('http://www.omdbapi.com/?'+searchType+'='+searchVal+'&apikey=2688c382', function( data ) {
      if (DEBUG) console.log(data);

    });
  } else if (db == 'tmdbapi') {

  }

}

/*function APIReqRandom(db) {
  //var i = 0;
  var response = "False";
  while (response == "False") {
      //var searchVal = 'tt' + ''.join(["%s" % random.randint(0, 9) for num in range(0, 7)]);
      if (db == "omdbapi") {
          var searchVal = searchVal.replace(" ", "%20");
          var http = urllib3.PoolManager();

          var r = http.request('GET', 'http://www.omdbapi.com/?i='+searchVal+'&apikey=2688c382');
          var j = json.loads(r.data);

          var response = j['Response'];
          if (response == 'True') {
              j['MyStatus'] = "";
              j['Rating'] = 0;
              searchresult.push(j);
            }
          //i++;
        }
      }
  return j
}

function ListIO(opt) {
  if (opt == "load") {
    with open('ls.json', 'r') as json_file:
    personallist = json.load(json_file)
  }
  else if (opt == "save") {
    with open('ls.json', 'w') as json_file:
    json.dump(personallist, json_file)
  }
  return (personallist);
}

function ListAddition(newContent) {
  var r = 0;
  var l = personallist.length();
  personallist.push(newContent);
  return (r);
}

function ListRemoval(id) {
  var r = 0;
  for (k=0; k < personallist; k++) {
    if (k == id){
      personallist.pop(id);
      r = 1;
    }
  }
  return (r);
}

function ChangeRating(id, rating) {
  var r = 0;
  for (k=0; k < personallist; k++) {
    if (k == id){
      personallist[k]['Rating'] = rating;
      r = 1;
    }
  }
  return (r);
}

function ChangeStatus(id, newStatus) {
  var r = 0;
  for (k=0; k < personallist; k++) {
    if (k == id) {
      personallist[k]['MyStatus'] = newStatus;
      r = 1;
    }
  }
  return (r);
}

function CalcTime() {
  var rt = 0
  for (k=0; k < personallist; k++) {
    var tmp = personallist[k]['Runtime'];
    tmp = tmp.replace("m", "");
    tmp = tmp.replace("in", "");
    rt = rt + tmp;
  }
  return (rt);
}

function CalcRating() {
  var summ = 0;
  var personallistTEMP = personallist;
  for (k=0; k < personallistTEMP; k++) {
    var my = k['Rating'];
    var their = 0;
    for (j=0; j < k['Ratings']; j++) {
      var tmp = j['Value'];
      if (j['Source'] == "Internet Movie Database") {
        tmp = tmp.replace("/10", "");
      }
      if (j['Source'] == "Rotten Tomatoes") {
        tmp = tmp.replace("%", "")/10;
      }
      if (j['Source'] == "Metacritic") {
        tmp = tmp.replace("/100", "")/10;
      }
      their += tmp;
    }
    summ += their / k['Ratings'].length();
  }
  var ret = summ/ personallistTEMP.length();
  return (ret);
}
*/
