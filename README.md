Data Science Assignment 5
README file
Methedology:

We first scraped https://www.ebay.com/globaldeals/tech and collected the following info: Timestamp, Title, Price, Original_price,Shipping, Item_url

Then after collecting thet data it was pushed to github for automation. The website was scraped every 3 hours using Github Actions. It was scraped from 2025-03-19 17:19:23 to 2025-03-23 12:26:28 (approx. 5 days). 
The csv file that was cleaned had 3419 rows of data (anything new was because I didn't stop the automation before cleaning, the analysis doesn't include the data after 1pm )

After that, data cleaning took place. 
    - I removed the US $, $ and , from Price and Original_price.
    - We notice that the Original_price is not filled in all columns thus meaning that the price was not discounted, so we replaced the empty Original_price cell with its respective Price column. 
    - Shipping column was cleaned by replacing missing or invalid values with "Shipping info unavailable".
    - Price and Original_price were converted to numeric values.
    - Then Discount_percentage was computed

Then the data was visualized for analysis:
- Time Series Analysis:
    Analyzed the number of deals posted per hour.

- Price and Discount Analysis:
    Visualized the distribution of product prices and discounts.
    Compared Original_price and Price using a scatter plot.

-Shipping Information Analysis:
    Analyzed the frequency of different shipping options.

-Text Analysis on Product Titles:
    Counted the frequency of the following keywords "Apple", "Samsung", "Laptop", "iPhone", "Tablet", "Gimbal"

-Price Difference Analysis:
    Computed the absolute discount (Original_price - Price) and analyzed its distribution.

-Discount Analysis:
    Identified the top 5 unique deals with the highest discounts.

Key Findings:


1. Time Series Analysis
Deals are posted less frequently after 12 and before 18 (not all hours are shown in the graph since these are only the hours when deals were posted on eBay.)

2. Price and Discount Analysis
The majority of products are priced between 20 and 510 approximately with ome outlies (max peice is 2500)

The distribution of the product prices isn't normally distributed (shape of the curve is not of a normally distributed graph). Meaning that there is a vairety of prices but most of them are consentrated between 20 and 200 approx.

The scratter plot shows:
- The points generally follow an upward trend, indicating that as the Original Price increases, the Discounted Price also increases.
-More points are clustered in the lower range (0–1000), meaning that most of the items are priced lower

Discounts typically range from 20% to 60-65%.

3. Shipping Information Analysis

Approxinately 1/3 of the products offer Free shipping while the rest 2/3 have unavailable shipping info


4. Text Analysis on Product Titles

The most frequent keywords in product titles are:

"Apple" (aaprox 700 count) > "Iphone" (approx 430 count)> "Samsung" > "Laptop"> "Tablet" > "Gimbal" (nearly negligible)


5. Price Difference Analysis

The price difference isn't ussually huge between the original and discounted price

6. Discount Analysis

It showed the top 5 unique deals with the highest discounts which have 4 Samsung products

Challenges Faced

Making sure all data was properly cleaned and scraped while being automated

Debating whether to remove duplicate productes with different timestamps only but decided on keeping them since this indicates that the product is still not sold which is important information

Potential Improvements: 

- Perform advanced time series analysis to identify trends over days, weeks, or months.
- Compare how long a product is taking to be sold with and without any discounts