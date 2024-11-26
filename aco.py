from tsp import *

class ACO():
    # possible parameters: nAnts, Alpha=4, Beta=1, constant_q, initial_pheromones, proximity_constant, list_of_cities
    def __init__(self, initial_pher=0.200):
        ''' initial_pher: indicates the initial amount of pheromones present on each edge'''
        # need to create a universal mapping of cities to integers
        self.initial_pher = initial_pher
        self.tsp = TSP()
        #self.cities_mapped = {city: idx for idx, city in enumerate(self.tsp.data['capital'])} # map cities to integers
        self.pher_prox_map = None
    
    def get_idx_PherProxMap(self, i, j):
        '''This is a helper method for init_PherProxMap to get the one index of 2D array from two indixes, i and j'''
        n = len(self.tsp.dim)
        if i > j: # check i, j pairs once due to undirectedness
            i, j = j, i
        return ((i * (2 * n - i - 1)) // 2) + (j - i - 1)   
    
    def init_PherProxMap(self):
        '''Method that constructs a data structure that holds the amount of pheromones 
        between each city and the proximity from each city. 
        Also updates the distances of each edge and updates the number of pheromones the inital pheromones
        
        Possible data structures:
         -  Dictionary of Dictionaries
         -  Compact 2D Numpy Array (most memory/time efficient)
         -  Symmetrical 3D Numpy Array (n * n * 2)
         
        Implemented: Compact 2D Numpy Array
        
        Input: 
         -  List of cities
    
        '''
        data = self.tsp.data
        
        data.iloc[i, 2]
        
        # need to create a universal mapping of cities to integers
        n = len(self.tsp.dim) #number of cities
        num_pairs = (n * (n - 1))//2 #number of unique pairs
        self.pher_prox_map = np.zeros((num_pairs, 2)) #store 2 data values per edge
        
        for i in range(n):
            for j in range(i + 1, n): #only need to consider i < j
                haver_dist = haversine(data.iloc[i, 2], data.iloc[i, 3], data.iloc[j, 2], data.iloc[j, 3]) 
                idx = self.get_idx_PherProxMap(i, j)
                self.pher_prox_map[idx] = [self.initial_pher, haver_dist]
        
        return self.pher_prox_map

#testing
aco_object = ACO()
#aco_object.init_pher_prox_map()
#print(aco_object.pher_prox_map)
