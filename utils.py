def getDriverRouteListFromSolution(data, manager, routing, solution):
    driverRoutes = []
    driverRouteDistances = []
    for vehicle_id in range(data['num_vehicles']):
        routes = []
        route_distance = 0

        index = routing.Start(vehicle_id)

        while not routing.IsEnd(index):
            routes.append(manager.IndexToNode(index))
            previous_index = index
            index = solution.Value(routing.NextVar(index))
            route_distance += routing.GetArcCostForVehicle(
                previous_index, index, vehicle_id)

        driverRouteDistances.append(route_distance)
        driverRoutes.append(routes)
    return driverRoutes, driverRouteDistances