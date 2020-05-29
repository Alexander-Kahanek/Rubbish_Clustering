# Startup Grind Data Set

Data files are not included due to company privacy, please contact to get a hold of the csv files.

# clean_script.R - done by: alexander kahanek

This is a cleaned version of the above data set:

+ Items were sesperated into single rows
	- they were changed from having counts for objects to one object per row

+ The weekdays had a mistake for one of the dates
	- They were changed to match.

+ Seperated system timestamp to two columns
	- date - changed to Year-month-day
	- time - changed to Year-month-day 24hour:min:sec

+ Changed rubbishType and is_litter addition
	- changed "other" category to "uncategorized".
	- added a is_litter column, 0 == not litter, 1 == is litter.


# euclidean_script.py - done by: alexander kahanek

This is a script made to take a pandas DataFrame object, and two lists of names: Centroid object list, and Object name list.

# analysis.rmd - done by: alexander kahanek

A work in progress rmd file. Goal is to be an analysis of clustering using python and R together.

# litter.ipynb - done by: alexander kahanek

A rudamentary analysis that was done to get a general idea of the starting data and clustering
