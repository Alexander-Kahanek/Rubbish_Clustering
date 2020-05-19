# Startup Grind Data Set



# clean_rubbish.csv - done by: alexander kahanek

This is a cleaned version of the above data set:

+ Items were combined into single rows
	- they were changed to one object per row

+ The weekdays had a mistake for one of the dates
	- They were changed to match.

+ Seperated system timestamp to two columns
	- date - changed to Year-month-day
	- time - changed to Year-month-day 24hour:min:sec

+ Changed rubbishType and is_litter addition
	- changed "other" category to "uncategorized".
	- added a is_litter column, 0 == not litter, 1 == is litter.
