# Search address API documentation

This repository contains the documentation for [search address]() API.

#### Contents

- [Overview](#1-overview)
- [Resources](#2-resources)
  - [Search address](#21-search-address)
- [Assumptions](#3-assumptions)
- [Constraints](#4-constraints)

## 1. Overview

The Search address API provides a service for search address in our database, which including Brazil, Canada, Germany, India, Japan, South Korea, North Korea, Mexico, Spain, UK, USA.  
All requests are made to endpoints beginning:
`https://address-search.azurewebsites.net/api/`

All requests must be secure, i.e. `https`, not `http`.


## 2. Resources

The API is RESTful. All requests must be made using `https`.

### 2.1. Search address

#### Sending request body including name, street, etc, and return matched address from our database

```
POST https://address-search.azurewebsites.net/api/addresssearch
```

Example request:

```
POST /api/addresssearch HTTP/1.1
Content-Type: text/plain
User-Agent: PostmanRuntime/7.29.0
Accept: */*
Cache-Control: no-cache
Postman-Token: 4ff002a1-2f07-4d07-abcd-f23006509848
Host: address-search.azurewebsites.net
Accept-Encoding: gzip, deflate, br
Connection: keep-alive
 
{
"mode": "AddressSearch",
"searchCountries": "usa japan canada india",
"First Name": "",
"Last Name": "",
"Country": "",
"Country-ISO code": "",
"State": null,
"Province": null,
"Prefecture": "",
"City": "",
"Locality": null,
"Town": "",
"Village": null,
"Subdivision": null,
"Sector": null,
"Quadrant": null,
"Block": null,
"Neighborhood": null,
"Quarter": null,
"Street": "",
"Building/House No": "1",
"Apt/Suite": null,
"Zip": "",
"POB": null,
"address code": ""
}
```

With the following fields:

| Parameter           | Type         | Required?      | Description                                                    |
| --------------------|--------------|----------------|----------------------------------------------------------------|
| Country             | string       | required       | Country (US, UK, Japan, etc)                                   |
| Address             | string       | not required   | Address (State, City, etc)                                     |
| First Name          | string       | not required   | First Name (Jesse, Kai-Ying, etc)                              |
| Last Name           | string       | not required   | Last Name (Jordan, Chan, Chuang, etc)                          |
| State               | string       | not required   | State (WA, CA, OK, etc)                                        |
| Province            | string       | not required   | Province (MS, PA, AM, etc)                                     |
| Prefecture          | string       | not required   | Prefecture (Osaka, Kagoshima, Saga, etc)                       |
| City                | string       | not required   | City (Sao Luis, Seattle, Boston, etc)                          |
| Locality            | string       | not required   | Locality (Barkot, Chatra, Merida, etc)                         |
| Town                | string       | not required   | Town (Shingu, Togo, Teshio, etc)                               |
| Village             | string       | not required   | Village (Babilonia, Pabelo, Baca, etc)                         |
| Subdivision         | string       | not required   | Subdivision (Gyeonggi, Daegu, Jeju, etc)                       |
| Sector              | string       | not required   | Sector (one, two, five, etc)                                   |
| Quadrant            | string       | not required   | Quadrant (13, 5, 4, etc)                                       |
| Block               | string       | not required   | Block (1, 5, 3, etc)                                           |
| Neighborhood        | string       | not required   | Neighborhood (Vila do Joao, Pajucara, Praia do Gunga, etc)     |
| Quarter             | string       | not required   | Quarter (Hipodromo, Algarin, Centro, etc)                      |
| Building/House No   | string       | not required   | Building/House No (1941, 189, 974, etc)                        |
| Apt/Suite           | string       | not required   | Apt/Suite (134, 11-194, 312-214, etc)                          |
| Zip                 | string       | not required   | Zip (78240-694, 98015, 489-7663, etc)                          |
| POB                 | string       | not required   | POB (79894, 63008, 91893 CEDEX, etc)                           |


The response is JSON format. Example response body:
```
HTTP/1.1 200 OK
Transfer-Encoding: chunked
Content-Type: text/plain; charset=utf-8
Server: Kestrel
Request-Context: appId=cid-v1:4be2a3aa-a01a-42de-bdd0-a0026480daed
Date: Tue, 01 Mar 2022 02:42:30 GMT
 
[
{
"First Name": "Waylen",
"Last Name": "Cornie",
"Country": "USA",
"Country-ISO code": "3166-2:UM",
"State": "MA",
"Province": null,
"Prefecture": null,
"City": "Indianapolis",
"Locality": null,
"Town": null,
"Village": null,
"Subdivision": null,
"Sector": null,
"Quadrant": null,
"Block": null,
"Neighborhood": null,
"Quarter": null,
"Street": "5692 School Road",
"Building/House No": "1",
"Apt/Suite": "Apt 192",
"Zip": "13185",
"POB": "",
"address code": "US-033"
},
{
"First Name": "Liana",
"Last Name": "Pedro",
"Country": "USA",
"Country-ISO code": "3166-2:UM",
"State": "VT",
"Province": null,
"Prefecture": null,
"City": "Dallas",
"Locality": null,
"Town": null,
"Village": null,
"Subdivision": null,
"Sector": null,
"Quadrant": null,
"Block": null,
"Neighborhood": null,
"Quarter": null,
"Street": "506 Hanover Road",
"Building/House No": "1",
"Apt/Suite": "Apt 156",
"Zip": "47420",
"POB": "",
"address code": "US-141"
}
]
```

Possible errors:

| Error code | Description                                                                                        |
| -----------|----------------------------------------------------------------------------------------------------|
| 400        | User error, Request is incorrect or corrupt, or the server can't understand it.                    |
| 406        | Does not find any content following the criteria given by the user agent.                          |
| 422        | the request was well-formed, the server was unable to follow it, due to semantic errors.           |
| 503        | the server is currently not ready to handle the request.                                           |

## 3. Assumptions
1. The user can leave all text inputs blank except for the country.
2. Form contains all the categories of an address. Once a country is selected, will let the user enter the categories that country has. If multiple countries are selected, will show the union categories.
3. All of the data are stored in string format. No computation is needed and there are special categories that start with 0. Have to be consistent for all of the data stored.

## 4. Constraints
1. Limit countries to have a maximum of 200 addresses. Will start small and grow on top of that.