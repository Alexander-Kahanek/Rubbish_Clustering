# CREATED BY: Alexander Kahanek

####### ALL LIBRARIES USED ###########
options(stringsAsFactors = FALSE)
library(dplyr)
library(lubridate)

raw <- read.csv("raw/Startup Grind Data Set - Sheet1.csv")

## number of items are combined
# using add_items function to add rows for each item

raw <- raw %>% 
  (function(data){
    # function to add rows for each item
    # loop through index in df
    
    for (k in 1:3){ # needed due to re-indexing
      for (i in 1:nrow(data)){ 
        # num items > 1
        if (data[i,'itemsTagged'] > 1){ 
          
          num_items = data[i,'itemsTagged']
          # add a row for each item
          for (n in 1:num_items){ 
            data <- data %>% 
              rbind(c(itemsTagged= as.numeric(1), street= data[i,'street'], rubbishType= data[i,'rubbishType'],
                      day= data[i,'day'], serverTimeStamp= data[i,'serverTimeStamp'],
                      city= data[i,'city'], state= data[i,'state'], lat= data[i,'lat'],
                      long= data[i,'long']))
            
          }
          # delete old row
          data <- data[-c(i),] %>% 
            mutate( # change back to character
              itemsTagged = as.numeric(itemsTagged) 
            )
        }
      }
    }
    
    return (data)
  })

## days are categorized wrong
# creating new date and time columns, also recategorizing days

raw <- raw %>% 
  mutate(
    date = as.Date(serverTimeStamp,
                   format = "%m/%d/%Y"),
    time = parse_date_time(serverTimeStamp,
                           orders = "%m/%d/%Y, %I:%M:%S %p"),
    day = wday(date, label=TRUE)
  ) %>% 
  subset(select = -c(serverTimeStamp))

## add a is_trash column to seperate object locations from litter
## change other to uncategorized, they are the same classification

litter = c("paper","tobacco","other","plastic","food","glass", "uncategorized")

raw <- raw %>% 
  mutate(
    is_litter = ifelse(rubbishType %in% litter,1,0),
    rubbishType = ifelse(rubbishType == "other", "uncategorized", rubbishType)
  )
  

raw %>% 
  write.csv("clean/clean_rubbish.csv")
