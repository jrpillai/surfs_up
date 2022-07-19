# Surfs Up: Year Round Sustainability of a Surf and Ice Cream Shop in Oahu

## Overview
In this analysis, using a SQLite Weather Database and Python, I extract temperature observations for the month of June and December in the years 2010-2017 to determine if the weather in Oahu is conducive to running a Surf and Ice Cream shop.

## Results
June and December temperatures were extract using a filter, and loaded into a datafram for analysis. You can see the descriptive statistics and histograms for each month below:

![Summary Statistics for June Temperatures](Images/june_desc_stat.png) ![Summary Statistics for December Temperatures](Images/dec_desc_stat.png)

![June Temperatures Histogram](Images/june_hist.png) ![December Temperatures Histogram](Images/dec_hist.png)

### Key Differences
  * June has a mean temperature of about 71° F, four degrees less than December mean temperature of 75° F.
  * June has a minimum temperature of about 56° F, significantly higher than the December mean temperature of 64° F.
  * June has less spread, or variability in temperature, with a standard deviation of 3.26° F compared to the December standard deviation of 3.75° F

### Key Similarities
  * Overall, the air temperatures in Oahu in December and June are mild and temperate, with little difference between summer and winter. 
  * Although December has slightly more variability, there is still predictably temperate weather the majority of the time.

## Summary
Based on temperature data alone, it appears that the weather in Oahu is conducive to running a Surf and Ice Cream Shop in Oahu. However, I performed a few additional queries to determine if there is a difference in rainfall between these months.

```
# Write a query that filters the Measurement table to retrieve the precipitation for the month of December and June.
prcp_dec = session.query(Measurement.prcp).filter(extract('month', Measurement.date)=='12').all()
prcp_june = session.query(Measurement.prcp).filter(extract('month', Measurement.date)=='06').all()
```

The code above extracted the daily rainfall over the last month for 2010-2017. The resulting analysis showed a mean daily rainfall of 






