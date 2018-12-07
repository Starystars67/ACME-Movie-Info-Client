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
  console.log(val)
  APIReq('omdbapi', val, 's')
}

var input = document.getElementById("searchVal");

input.addEventListener("keydown", function(e) {
  // Number 13 is the "Enter" key on the keyboard
  if (e.keyCode === 13) {
    document.getElementById("searchButton").click();
    e.preventDefault();
  }
}, false);

$('#searchButton').click(function(e) {
  e.preventDefault();
  SearchButton();
});

$("a").click(function(e) {
  e.preventDefault();
  var page = $(this).attr('href')
  console.log(page);
  if (page == "movieSearch") {
    var searchVal = $(this).data('value')
    console.log(searchVal)
    $.getJSON('http://www.omdbapi.com/?i='+searchVal+'&apikey=2688c382', function( data ) {
      $('#ModalLabel').html(data);
    });
    return;
  } else {
    ShowPage(page);
  }
});

function HidePages() {
  $('.page').hide(); // hides
}

function ShowPage(page) {
  $('.'+page).show(); // hides
}

// Function to query api
function APIReq (db, searchVal, searchType) {
  if (db == 'omdbapi') {
    $.getJSON('http://www.omdbapi.com/?'+searchType+'='+searchVal+'&apikey=2688c382', function( data ) {
      if (DEBUG) console.log(data);
      $('#totalResults').html(data.totalResults);
      var html = ''
      for (k=0; k < data.Search.length; k++) {
        if (k %2 == 0) {
          html += '<div class="row mx-auto mt-4">'
        }
        html += '  <div class="col-md-6"> <a href="movieSearch" data-value="' + data.Search[k].imdbID + '" style="" data-toggle="modal" data-target="#movieModal">'
        html += '    <div class="media">'
        html += '      <img class="mr-3" src="'+data.Search[k].Poster+'" alt="Movie Poster Image" style="max-width: 64px;">'
        html += '      <div class="media-body">'
        html += '        <h5 class="mt-0">' + data.Search[k].Title + '</h5>' + data.Search[k].Year
        html += '      </div>'
        html += '    </div>'
        html += '  </a></div>'
        if (k %2 == 1) {
          html += '</div>'
        }
      }
      $('#SearchResults').html(html);
    });
  } else if (db == 'tmdbapi') {
    $.getJSON('https://api.themoviedb.org/3/movie/550?api_key=b820f7ca8b64556235fcf052051e01cd', function( data ) {
      if (DEBUG) console.log(data);
      $('#totalResults').html(data.totalResults);
      var html = ''
      for (k=0; k < data.Search.length; k++) {
        if (k %2 == 0) {
          html += '<div class="row mx-auto mt-4">'
        }
        html += '  <div class="col-md-6"> <a href="movieSearch" data-value="' + data.Search[k].imdbID + '" style="" data-toggle="modal" data-target="#movieModal">'
        html += '    <div class="media">'
        html += '      <img class="mr-3" src="'+data.Search[k].Poster+'" alt="Movie Poster Image" style="max-width: 64px;">'
        html += '      <div class="media-body">'
        html += '        <h5 class="mt-0">' + data.Search[k].Title + '</h5>' + data.Search[k].Year
        html += '      </div>'
        html += '    </div>'
        html += '  </a></div>'
        if (k %2 == 1) {
          html += '</div>'
        }
      }
      $('#SearchResults').html(html);
    });
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
