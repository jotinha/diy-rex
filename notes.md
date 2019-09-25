## TODO
* espaço no disco
* testar gravar
* levar o micro

* Remove scores or make a standard recommendations class
* ALS (https://towardsdatascience.com/prototyping-a-recommender-system-step-by-step-part-2-alternating-least-square-als-matrix-4a76c58714a1)
* multiplications as a more efficient algorithm
* content based similarity
* solving the sparsity issue
* cold start
* clean code

## Useful datasets
* github
* hacker news
* reddit
* listenbrainz


## listenbrainz

https://blog.metabrainz.org/2017/08/05/listenbrainz-data-is-live-on-bigquery/
dataset: listenbrainz:listenbrainz  
https://listenbrainz.readthedocs.io/en/production/dev/json.html
https://musicbrainz.org/doc/MusicBrainz_Database/Download
30GB



* 146914257

listened_at 	TIMESTAMP 	REQUIRED 	
user_name 	STRING 	REQUIRED 	
artist_msid 	STRING 	REQUIRED 	
artist_name 	STRING 	REQUIRED 	
artist_mbids 	STRING 	NULLABLE 	
release_msid 	STRING 	NULLABLE 	
release_name 	STRING 	NULLABLE 	
release_mbid 	STRING 	NULLABLE 	
recording_msid 	STRING 	REQUIRED 	
track_name 	STRING 	REQUIRED 	
recording_mbid 	STRING 	NULLABLE 	
tags 	STRING 	NULLABLE


## hacker news

bigquery-public-data.hacker_news

* full          -> 20982779
    title 	STRING 	NULLABLE 	Story title
    url 	STRING 	NULLABLE 	Story url
    text 	STRING 	NULLABLE 	Story or comment text
    dead 	BOOLEAN 	NULLABLE 	Is dead?
    by 	STRING 	NULLABLE 	The username of the item's author.
    score 	INTEGER 	NULLABLE 	Story score
    time 	INTEGER 	NULLABLE 	Unix time
    timestamp 	TIMESTAMP 	NULLABLE 	Timestamp for the unix time
    type 	STRING 	NULLABLE 	Type of details (comment, comment_ranking, poll, story, job, pollopt)
    id 	INTEGER 	NULLABLE 	The item's unique id.
    parent 	INTEGER 	NULLABLE 	Parent comment ID
    descendants 	INTEGER 	NULLABLE 	Number of story or poll descendants
    ranking 	INTEGER 	NULLABLE 	Comment ranking
    deleted 	BOOLEAN 	NULLABLE 	

* full_201510   -> 18778427
    by 	STRING 	NULLABLE 	Username of commenter or submitter
    score 	INTEGER 	NULLABLE 	Story score
    time 	INTEGER 	NULLABLE 	Unix time
    title 	STRING 	NULLABLE 	Story title
    type 	STRING 	NULLABLE 	Type of details (comment, comment_ranking, poll, story, job, pollopt)
    url 	STRING 	NULLABLE 	Story url
    text 	STRING 	NULLABLE 	Story or comment text
    parent 	INTEGER 	NULLABLE 	Parent comment ID
    deleted 	BOOLEAN 	NULLABLE 	Is deleted?
    dead 	BOOLEAN 	NULLABLE 	Is dead?
    descendants 	INTEGER 	NULLABLE 	Number of story or poll descendants
    id 	INTEGER 	NULLABLE 	Unique type ID
    ranking 	INTEGER 	NULLABLE 	Comment ranking


* comments      -> 8399417
    id 	INTEGER 	NULLABLE 	Unique comment ID
    by 	STRING 	NULLABLE 	Username of commenter
    author 	STRING 	NULLABLE 	Username of author
    time 	INTEGER 	NULLABLE 	Unix time
    time_ts 	TIMESTAMP 	NULLABLE 	Human readable time in UTC (format: YYYY-MM-DD hh:mm:ss)
    text 	STRING 	NULLABLE 	Comment text
    parent 	INTEGER 	NULLABLE 	Parent comment ID
    deleted 	BOOLEAN 	NULLABLE 	Is deleted?
    dead 	BOOLEAN 	NULLABLE 	Is dead?
    ranking 	INTEGER 	NULLABLE 	

* stories       -> 1959809
    id 	INTEGER 	NULLABLE 	Unique story ID
    by 	STRING 	NULLABLE 	Username of submitter
    score 	INTEGER 	NULLABLE 	Story score
    time 	INTEGER 	NULLABLE 	Unix time
    time_ts 	TIMESTAMP 	NULLABLE 	Human readable time in UTC (format: YYYY-MM-DD hh:mm:ss)
    title 	STRING 	NULLABLE 	Story title
    url 	STRING 	NULLABLE 	Story url
    text 	STRING 	NULLABLE 	Story text
    deleted 	BOOLEAN 	NULLABLE 	Is deleted?
    dead 	BOOLEAN 	NULLABLE 	Is dead?
    descendants 	INTEGER 	NULLABLE 	Number of story descendants
    author 	STRING 	NULLABLE 	Username of author 
 

