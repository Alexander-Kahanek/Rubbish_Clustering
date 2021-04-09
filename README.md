# Startup Grind Data Set

Two data files are included in this Repository:

+ The raw dataset, provided by Rubbish, co.
	- https://www.rubbish.love/

+ The cleaned dataset,

# clean_script.R
done by: alexander kahanek

This is a script used to clean the original raw data set, the hyperparameters can be modified at the top of the script. The script will output a csv file with the following changes:

+ Items were separated into single rows,
	- they were changed from having counts for objects to one object per row.

+ The weekdays had a mistake for one of the dates,
	- they were changed to match.

+ Seperated system timestamp to two columns
	- date - changed to Year-month-day
	- time - changed to Year-month-day 24hour:min:sec

+ Changed rubbishType and is_litter addition
	- changed "other" and "uncategorized" categories to "unknown".
	- added a is_litter column, 0 == not litter, 1 == is litter.


# euclidean_script.py
done by: alexander kahanek

This script is made to take a Pandas DataFrame object, and two lists of centroid and object names. It leaves an option to use the logical classifier, or to ignore this. The script performs the following:

+ Gives ID numbers to litter and collection objects.

+ Finds closest collection object for each litter object.
	- Adjusts the distance for the curvature of the earth.

+ Adds columns to DataFrame object, then returns.
	- obj_id is the object id, -1 signifies it was not tagged as a litter object.
	- cent_id is the centroid id, -1 signifies it was not tagged as a collection object.
	- closest_cent is the closest centroid for a litter object, -1 signifies there is no centroid or object is a centroid.
	- cent_type is the centroid type associated to the closest centroid. None signifies the same as -1 above.
	- distance is the distance from the litter object to the closest centroid, -1 signifies there is no distance.
	

# rubbish_analysis.rmd
done by: alexander kahanek

A work in progress rmd file. Goal is to be an analysis of clustering using R for vizualization and the Data Analysis, while Python is used for scripting.
