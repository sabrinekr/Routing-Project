from vrp import create_routes
from cvrp import create_routes_cvrp
from vrptw import create_routes_vrptw
import sys

if __name__ == '__main__':
    
    print("we will use this algorithm", sys.argv[1])
    routing = sys.argv[1]
    if routing == 'vrp':
        create_routes()
    elif routing == 'cvrp':
        create_routes_cvrp()
    elif routing == 'vrptw':
        create_routes_cvrp()
    else:
        print("this algorithm doesn't exist")