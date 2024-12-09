from tsp import *

class ACO():
    # possible parameters: nAnts, Alpha=4, Beta=1, constant_q, initial_pheromones, proximity_constant, list_of_cities
    def __init__(self, nAnts=None, initial_pher=0.200, proximity_constant=1, evaporation_constant=0.35, pheromone_constant=4, alpha=1, beta=1):
        ''' Class that implements a solution to TSP using Ant Colony Optimization
        
        initial_pher: indicates the initial amount of pheromones present on each edge
        
        
        '''
        self.nAnts = nAnts
        self.initial_pher = initial_pher
        self.C = proximity_constant
        self.evap_constant = evaporation_constant
        self.Q = pheromone_constant
        self.alpha = alpha
        self.beta = beta
        
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
            leiden_route = self.tsp.create_path(route)[:-1]
            for i, j in zip(leiden_route, leiden_route[1:]): # go through each edge in route and update pheremones appriopriatly
                index = self.get_idx_PherProxMap(i, j)
                current_pheremone = self.pher_prox_map[index][0]
                self.pher_prox_map[index][0] = current_pheremone + (self.Q/route_length)
        
        return
    
    def calculate_desire(self, i, j):
        '''Calculate the desire to go from city i to city j. Returns the desire as a float. 
        Helper method for generete_ant_routes'''
        index = self.get_idx_PherProxMap(i, j)
        pher, prox = self.pher_prox_map[index]
        return (pher**self.alpha)*(prox**self.beta)
    
    def prob_to_go_to_cities(self, ant_location: int, allowed_cities: list):
        """Calculates the probability of going to each city that is still allowed in a dictionary, where the length of
        the dict is equal to the allowed_cities.
        ant_location(int): current city ant is located in"""
        
        probs = {}
        desires = []
        # first getting each indivdual desire from current ant location to every available city
        for city in allowed_cities:
            desires.append(self.calculate_desire(ant_location, city))
        
        # then taking each city and calculating probability. prob = (desire to specific city/sum of desires for all cities)
        for index, city in enumerate(allowed_cities):
            probs[city] = ((desires[index])/sum(desires))
        
        return probs
    
    def generate_ant_routes(self):
        
        cities_without_leiden = range(1, len(self.cities))
        start_city = 1
        ant_number = 0
        
        
        
        return 
        
    def main(self):
        '''Main loop'''
        
        return 
        

#testing
aco_object = ACO()
print(aco_object.prob_to_go_to_cities(2, [3, 4, 5, 6]))


