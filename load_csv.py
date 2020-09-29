#------------------------------------------
#This module loads all csv to dataframes   |
#-------------------------------------------


def load_all_csv(location):
    """This function load all csv in folder specified
    Dependencies:-
    glob module
    """"

    folder_location = location
    files_list = glob.glob(folder_location+"*.csv")
# Consist all official f1 circutis info
circuits_df = pd.read_csv("F1-Data-Analysis/f1 datasets/circuits.csv") 


constructor_results_df = pd.read_csv("F1-Data-Analysis/f1 datasets/constructor_results.csv")

#Contains contstructor standings after each rounds
constructor_standings_df = pd.read_csv("F1-Data-Analysis/f1 datasets/constructor_standings.csv")

# Consist all official recognised constructors since inauguration of the constructors championship since 1958
constructors_df = pd.read_csv("F1-Data-Analysis/f1 datasets/constructors.csv") 

#Consist drivers standings after each round
driver_standings_df = pd.read_csv("F1-Data-Analysis/f1 datasets/driver_standings.csv")

#Contains Info about all the drivrs that have driven a F1 car
drivers_df = pd.read_csv("F1-Data-Analysis/f1 datasets/drivers.csv")

lap_times_df = pd.read_csv("F1-Data-Analysis/f1 datasets/lap_times.csv")
pit_stops_df = pd.read_csv("F1-Data-Analysis/f1 datasets/pit_stops.csv")
qualifying_df = pd.read_csv("F1-Data-Analysis/f1 datasets/qualifying.csv")

#Consist details of all Grand Prix since the inauguration of the sport in 1950
races_df = pd.read_csv("F1-Data-Analysis/f1 datasets/races.csv")

#Consist all results of the races organised
results_df = pd.read_csv("F1-Data-Analysis/f1 datasets/results.csv")


#Consist Seasons in f1 with wikipedia link
seasons_df = pd.read_csv("F1-Data-Analysis/f1 datasets/seasons.csv")

#Consist status codes e.g winner, brake duct failure etc.
status_df = pd.read_csv("F1-Data-Analysis/f1 datasets/status.csv")