from tsp import *

class ACO():
    # possible parameters: nAnts, Alpha=4, Beta=1, constant_q, initial_pheromones, proximity_constant, list_of_cities
    def __init__(self, nAnts=None, initial_pher=0.200, proximity_constant=1, evaporation_constant=0.35, pheromone_constant=4):
        ''' Class that implements a solution to TSP using Ant Colony Optimization
        
        initial_pher: indicates the initial amount of pheromones present on each edge
        
        
        '''
        self.nAnts = nAnts
        self.initial_pher = initial_pher
        self.C = proximity_constant
        self.evap_constant = evaporation_constant
        self.Q = pheromone_constant
        
        self.tsp = TSP(plot=False)
        self.n = self.tsp.dim 
        if (nAnts == None):
            self.nAnts = self.n + 1 # number of ants equal to number of cities. + 1 for leiden 

        self.cities = self.tsp.create_path(range(self.n))[:-1] # this creates a array of coordinates(lng, lat) of each city starting with leiden at index 0 
        self.ant_routes = np.zeros((self.nAnts, self.n))
        self.pher_prox_map = self.init_PherProxMap()
    
    def get_idx_PherProxMap(self, i, j):
        '''This is a helper method for init_PherProxMap.
        It returns one index that corresponds to indices, i and j. 
        This effectively cuts down that amount of memory needed in half.'''
        n = self.tsp.dim
        if i > j: # check i, j pairs once due to undirectedness
            i, j = j, i
        return ((i * (2 * n - i - 1)) // 2) + (j - i - 1)   
    
    def init_PherProxMap(self):
        '''Method that constructs a data structure that holds the amount of pheromones and the proximity for each city. 
        Also updates the distances of each edge and updates the number of pheromones the inital pheromones. It also creates and mapping
        of cities to integers. 
        
        Possible data structures:
         -  Dictionary of Dictionaries
         -  Compact 2D Numpy Array (most memory/time efficient)
         -  Symmetrical 3D Numpy Array (n * n * 2)
         
        Implemented: Compact 2D Numpy Array (Using helper function get_idx_PherProxMap)
    
        '''
        n = len(self.cities)
        num_pairs = (n * (n - 1))//2 # number of unique pairs
        pher_prox_map = np.zeros((num_pairs, 2)) # store 2 data values per edge
       
        for i in range(n):
            for j in range(i + 1, n): # only need to consider i < j
                haver_dist = haversine(self.cities[i, 1], self.cities[i, 0], self.cities[j, 1], self.cities[j, 0]) 
                idx = self.get_idx_PherProxMap(i, j)
                pher_prox_map[idx] = [self.initial_pher, (self.C/haver_dist)]

        return pher_prox_map
        
    def evaporation_update(self):
        """pheremone evaporation update for all edges."""
        n = self.n
        for i in range(n):
            for j in range(i + 1, n):
                index = self.get_idx_PherProxMap(i, j)
                current_pheremone = self.pher_prox_map[index][0]
                self.pher_prox_map[index][0] = (1-self.evap_constant)*current_pheremone
                
        return 
    
    def ant_pheremone_update(self):
        """updates the pheremones based on the routes of all the ants. Looks at the route of one ant and updates the pheromones left behind
        along the route based on the length of the route aka quality of route."""   
        
        for route in self.ant_routes:
            route_length = self.tsp(route)
            leiden_route = 
            for i, j in zip(route, route[1:]): # go through each edge in route and update pheremones appriopriatly
                index = self.get_idx_PherProxMap(i, j)
                current_pheremone = self.pher_prox_map[index][0]
                self.pher_prox_map[index][0] = current_pheremone + (self.Q/route_length)
        
        return
        
    def generate_ant_routes(self):
        return 
        
    def main(self):
        '''Main loop'''
        
        return 
        

#testing
aco_object = ACO()
print(len(aco_object.cities))


