The two json files contain the results from the Hadoop YARN load simulator.
They are given to the python file yarnsimulator.py which
takes in a json file, parses through the keys and creates dataframes.

These dataframes are then joined (inner) to create dataframe
objects that are used to plot graphs (using matplotlib). 

These graphs give the user an idea of how Scheduler choice affects
other performance factors.