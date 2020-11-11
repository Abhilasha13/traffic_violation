# MIS531
# Enterprise Data Management

# Executive Summary

After conducting a geospatial analysis on the frequency of speeding violations, it is recommended to increase the number of 2-way cameras in the Harju-Maakond county (Tallinn City). Other areas that have a high number of cameras have witnessed fewer speeding violations. Further, it is recommended to reduce the speed limit in Tallinn from 70km/h to 50km/h during weekends, as this is when the highest number of violations occur. Additionally, it is advised to implement a community policing program in the city of Tallinn due to its high population and significant DUI offenses. Other counties such as Polva have seen a positive impact after implementing such a community program as the number of DUI offenses decreased in these areas over time.

## Dataset Summary
The dataset used in this analysis is the Republic of Estonia’s traffic violation data. In total, the dataset contained 468,350 records with 27 distinct attributes. These attributes provide significant information with respect to each violation that was conducted and recorded. Some examples include the date/timings, violations, respective laws, locations, type of vehicles and generic information regarding the violator. in total, there are 75 different types of violations ranging from high frequency violations such as speeding to low frequency violations such as illegal tachograph usage. An interesting finding within this dataset is that the maximum number of violations were caused by males aged between 26-34. Additionally, a decreasing trend in the number of violations were observed between 2014-2018 and this was mostly due to the active number of policies and enforcement measures that have been implemented over the years.

## Other Sources
Other sources that were used within this analysis included the Republic of Estonia’s traffic laws1. An English translation was available and this was used to determine the relevant laws and thoroughly understand them to further analyze our findings and provide recommendations. Additionally, further information was found through the Republic of Estonaia’s Road Administration website. This included more information on speed cameras (their locations and speed measurement methods) that assisted with our analysis and information regarding the country’s overall road network2. Further an online storymap describing Estonia’s traffic system visually was used to reaffirm our findings through the original dataset3. To further obtain more information regarding alcohol violations, an article was used that highlighted the extent of alcohol violations and proactive measures taken across different cities to reduce the number of DUI drivers4. The article summarizes the proceedings that were taken by local police across different cities in Estonia to reduce the number of DUI violations.

## Analysis Methods
The analysis methods that were used for this project included a combination of **SQL queries, Python scripts and Tableau Desktop** for the original dataset and creating inferences based on the secondary sources aforementioned. Several different types of queries were used to understand the dataset (i.e. identifying the number of violations per Section and locating the areas where the maximum number of violations occurred). After identifying Section 227 (Overspeeding) was the most common violation, the dataset was converged to perform a geographical analysis. This included creating a centroid for LEST_X and LEST_Y and converting them into Longitude and Latitude through a script written in Python. LEST refers to an Estonian coordinate system. The Lest_X and Y coordinate pairs give the left and right (western, eastern) longitude boundary and the lower and upper (southern, northern) latitude boundary respectively. This data was then used to plot the geospatial visualization through Tableau.

## Recommendations
The first recommendation is to increase the number of 2-way speeding cameras in the city of Tallinn (Harju Maakond County). Figure 2 illustrates that there are only around two to three cameras within this area, despite the highly dense population and number of speeding violations as shown in Figure 1. A majority of 2-way speeding cameras are currently placed towards the center of the country and this defines a negative correlation with the heat map, as not many speeding violations stretch across that area. 

A second recommendation that can be made with regards to improving the number of speed violations is to reduce the speed limit in the Tallinn area on Fridays and Saturdays between 3PM to 7PM. Currently, this is the prime time of when most violations occur as represented in the dataset and reaffirmed in the online Estonia story-map traffic system. As a result, due to the large population within this specific area, it would be feasible to reduce the speed limit from 70km/h to 40-50km/h.

The third recommendation pertains to the 8% of violations related to DUI where measures can be taken to further increase community policing. According to an article, a number of different counties across Estonia (Valga, Polva, Voru) implemented a method for individuals to report on suspicious DUI drivers. This inadvertently showcased that these areas reported the least number of DUI violations. However, looking at the the Harju and Ida-Viru counties that are highly populated, no such measure has been implemented. It is therefore recommended to extend community policing to these areas. To make the community policing initiative more effective, the government can start rewarding its citizens if they succeed in playing the role of a vigilante and complement it with hefty fines on violators.

## Visualizations

### Figure 1: Speed Violation in Estonia
![Speed Violation in Estonia](https://github.com/Abhilasha13/MIS531/blob/master/speed_violation_in_estonia.png)

### Figure 2: Speeding Camera Location
![Speeding Camera Location](https://github.com/Abhilasha13/MIS531/blob/master/speed_camera_location.png)

### Figure 3: Total Count of Traffic Violation Graph
![Total_Count of Traffic Violation Graph](https://github.com/Abhilasha13/MIS531/blob/master/total_traffic_violation_count.png)

## SQL Query to take the average of LEST_X and LEST_Y:

### Speeding LATITUDES and lONGITUDES

```
SELECT AVG(regexp_substr(LEST_Y, '[^-]+', 1, 1)+regexp_substr(LEST_Y, '[^-]+', 7, 1))/2 as LEST_Y, 
            AVG(regexp_substr(LEST_X, '[^-]+', 1, 1)+regexp_substr(LEST_X, '[^-]+', 9, 1))/2 as LEST_X 
FROM est.casedetails 
WHERE --COUNTY = 'Harju maakond' AND 
            (LEST_Y IS NOT NULL AND LEST_X IS NOT NULL) AND 
            SECTION in ('§ 227. Mootorsõidukijuhi poolt lubatud sõidukiiruse ületamine') 
GROUP BY LEST_Y,LEST_X 
ORDER BY LEST_Y DESC,LEST_X DESC;
```

### More about Python code:

```
from pyproj import Proj, transform
inProj = Proj(init='epsg:3301')
outProj = Proj(init='epsg:4326')
x1,y1 = -11705274.6374,4826473.6922
x2,y2 = transform(inProj,outProj,x1,y1) 
print x2,y2
```

LEST is an Estonian coordinate. LEST is a planar rectangular coordinate system founded on LAMBERT-EST. x-axes is collinear with LAMBERT-EST central meridian. The Lest_X and Y
coordinate pairs give the lower and upper boundary of each corner of each grid-square polygon: - Lest_X: left and right (western, eastern) longitude boundary - Lest_Y: lower and
upper (southern, northern) latitude boundary.

So, to find the latitude and longitude of the region we need to convert the L-EST to WGS84 (in order to plot the Geographical map for visualization).
So, we use espg:3301.

### Usage Instructions:

```
python assignment1.py -i <inputfile> -o <outputfile>
```
inputfile = input.csv
outputfile = output.csv

## References:

[Traffic Act – Riigi Teataja". Riigiteataja.Ee, 2019](https://www.riigiteataja.ee/en/compare_original?id=507012014005)

[“Estonian Road Network.” Maanteeamet, 28 Jan. 2019](https://www.mnt.ee/eng/roads/estonian-road-network)

[“Estonia Traffic Story Map.” StoryMapJS](https://uploads.knightlab.com/storymapjs/b5a9580f9a353c90b89c740926b0761d/kiiruskaamerad-eestis/index.html)

[Err. “Over 600 Drunk Drivers Caught in South Estonia in 2017 Thanks to Callers.” ERR, 23 Dec. 2017](https://news.err.ee/650539/over-600-drunk-drivers-caught-insouth-estonia-in-2017-thanks-to-callers)
