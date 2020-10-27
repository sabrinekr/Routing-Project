from vrp import create_routes
from cvrp import create_routes_cvrp
from vrptw import create_routes_vrptw
import sys

if __name__ == '__main__':
    
    routing = 'cvrp'
    if routing == 'vrp':
        create_routes()
    if routing == 'cvrp':
        create_routes_cvrp()
    if routing == 'vrptw':
        create_routes_cvrp()