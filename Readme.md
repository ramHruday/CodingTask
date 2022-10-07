# Coding task

## First challenge on python 
This repository contains the python code for the given first task, which follows the guidelines specified in the challenge.

Short description of the code
- main - calls the coffee API and reads from the stored coffee json, calls combines the results onto data.csv
- api_service - Contains the class for calling the api and handling unreachable API
- config_api - contains the configuration coffee api i.e. baseurl and endpoint
- coffee - contains **deserializer** and **read** class methods


output files
- data.csv
- [iso-date]_-_hot.csv
- 2022-10-05T23:14:06-05:00_-_iced.json 


## Second challenge on CSS query selectors using js
Below is the answer for the second task
```javascript
//  For the link
document.querySelector('#content_inner > article > ul > li:nth-child(3) > article > h3 > a').href;

// For the title
document.querySelector('#content_inner > article > ul > li:nth-child(3) > article > h3 > a').title;

```