# Population_35FR
Analysis of the population of one French department (Ille-et-Vilaine - 35)

## 1.Introduction
<p align="justify">
The purpose of this study is to give some basic information about the demography of a French department (Ille-et-Vilaine - 35). The data are coming from the following French Government API https://geo.api.gouv.fr. The data used were up-to-date as of December 2018. The data have been queried for all the department and then saved as NoSQL database locally. Thus, there is no need anymore to query from the API (except to update with latest API data) and the analysis can be done offline.
</p>

## 2.Statistics

**Table 1: Basic statistics**
 
  |               | Population | Area [km<sup>2</sup>] | Density [pop/km<sup>2</sup>]|
  |-------------- | ----------:| --------------------: | ---------------------------:|
  |**Minimum**    | 107        | 0.56                  | 15                          |
  |**Median**     | 1,314      | 15.81                 | 74                          |
  |**Average**    | 2,956      | 19.82                 | 155                         |
  |**Maximum**    | 211,373    | 110.66                | 4,196                       |
  |**Department** | 1,019,923  | 6,840.54              | 149                         |

**Table 2: Top 3 and bottom 3 cities for population, area and density**

| | Top 3 | Bottom 3 | 
|-|:-------:|:----------:|
|**Population**|Rennes - 211,373 <br> Saint-Malo - 44,919 <br> Fougères - 20,170 |Bléruais - 107 <br> Lanrigan - 149 <br> La Selle-Guerchaise	 - 154|
|**Area [km<sup>2</sup>]**|Paimpont - 110.66 <br> Guipry-Messac - 92.3 <br> Val d'Anast - 76.68 |Bécherel - 0.56 <br> Châteauneuf-d'Ille-et-Vilaine - 1.39 <br> La Selle-Guerchaise - 2.17|
|**Density [pop/km<sup>2</sup>]**|Rennes - 4,196 <br> Fougères - 1,934 <br> Bécherel - 1,289 |Paimpont - 15 <br> Rannée - 21 <br> Eancé - 24|

**Comment**
<p align="justify"> 
Almost 21% of the department population lives in the biggest and most densely populated city, Rennes. The cities with the highest population have some of the highest density population (i.e. Rennes, Saint-Malo (5th highest density), Fougères). However, the third highest densely populated city (Bécherel) has only 722 inhabitants. This high density rate is due the size of its teritory, the smallest in the departement.
</p>

## 3.Data visualisation

**Number of city per population bins**

<p align="center"> 
  <img src="/Graphs/321_CityPopulation.png">
</p>

**Comment**
<p align="justify"> 
The most representated city population bins is between 1,000 to 2,000 inhabitants.
</p>

<p align="center"> 
  <img src="/Graphs/322_CityPopulationDistribution.png">
</p>

**Comment**
<p align="justify"> 
The most representated city population bins is between 1,000 to 2,000 inhabitants.
</p>


**The most populated cities are: &emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp; The least populated cities are:**
