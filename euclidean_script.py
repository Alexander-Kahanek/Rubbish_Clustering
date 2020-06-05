import pandas
import geopy.distance

def logical_category(OBJECT, CENTROID):
    ## function used to categorize litter objects to centroids
    # OBJECT @ pass in object type
    # CENTROID @ pass in centroid type

    if OBJECT == 'paper':
        if CENTROID == 'trashCan' or CENTROID == 'recyclingCan':
            return True

    elif OBJECT == 'tobacco':
        if CENTROID == 'trashCan' or CENTROID == 'tobaccoAshCan':
            return True

    elif OBJECT == 'plastic':
        if CENTROID == 'trashCan' or CENTROID == 'recyclingCan':
            return True

    elif OBJECT == 'glass':
        if CENTROID == 'trashCan':
            return True

    elif OBJECT == 'food':
        if CENTROID == 'trashCan':
            return True

    elif OBJECT == 'uncategorized' or OBJECT == 'other':
        if CENTROID == 'trashCan':
            return True

    else:
        return False

def get_euclidean(DF, CENTROIDS, OBJECTS, CUSTOM_CATEGORY = False):
    ## function to calculate euclidean distance
    # DF @ pass in df to be altered
    # CENTROIDS @ pass in list of types for centroids
    # OBJECTS @ pass in list of types to be objects

    DF.index = pandas.RangeIndex(len(DF.index))

    # delete rows that have latitude as null
    DF = DF[DF['lat'] != None]

    # create new columns in dataframe
    # values set to -1 as placeholders
    DF['cent_id'] = -1 # column to keep centroid id
    DF['obj_id'] = -1 # column to keep object id
    DF['closest_cent'] = -1 # column to keep closest centroid for objects
    DF['distance'] = -1 # column to keep distances from object to centroid

    centroids = [] # will store (count, lat, long)
    objects = [] # will store (count, lat, long)

    centroid_id = 1 # counter for centroid placement in dataframe
    object_id = 1 # counter for object placement in dataframe

    for i in range(len(DF)): # index in dataframe

        if DF.loc[i, 'rubbishType'] in CENTROIDS:

            # store centroid count into dataframe
            DF.loc[i, 'cent_id'] = int(centroid_id)

            # store (CENTROID count, latitude, longitude)
            centroids.append((centroid_id, DF.loc[i, 'lat'], DF.loc[i, 'long']))
            centroid_id = centroid_id + 1

        elif DF.loc[i,'rubbishType'] in OBJECTS:

            # store object count into dataframe
            DF.loc[i, 'obj_id'] = int(object_id)

            # store (OBJECTS count, latitude, longitude)
            ## convert lat / long to measurements
            objects.append((object_id, DF.loc[i, 'lat'], DF.loc[i, 'long']))
            object_id = object_id + 1

        else:
            # row is not in type passed
            DF.drop(i, inplace= True)

    for (id_o, lat_o, long_o) in objects:

        min_distance = (-1, None) # will store (centroid count, distance to centroid)

        object_type = DF.loc[DF['obj_id'] == id_o, 'rubbishType'].values[0]

        for (id_c, lat_c, long_c) in centroids:

            centroid_type = DF.loc[DF['cent_id'] == id_c, 'rubbishType'].values[0]

            if logical_category(object_type, centroid_type) or CUSTOM_CATEGORY is True:

                distance = geopy.distance.geodesic((lat_c, long_c), (lat_o, long_o))

                if min_distance[1] is None or distance.meters < min_distance[1]:
                    min_distance = (id_c, distance.meters)

        # add info to dataframe
        DF.loc[DF['obj_id'] == id_o, 'closest_cent'] = int(min_distance[0])
        DF.loc[DF['obj_id'] == id_o, 'distance'] = float(min_distance[1])

    return DF