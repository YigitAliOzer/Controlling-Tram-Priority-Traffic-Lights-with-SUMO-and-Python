import traci #Calling TraCI Library

traci.start(["sumo-gui","-c","Tramvay_simulasyon.sumocfg","--start", "--delay","300"]) #Starting SUMO With Python

Detectors = traci.inductionloop.getIDList() 

for detector in Detectors:
    print("Detector is:", detector)
    print("Lane is:", traci.inductionloop.getLaneID(detector))

seen_matches = set()

# Our Detection Step With Loops

for j in range(901):

    traci.simulationStep()

    for vehicle in traci.simulation.getDepartedIDList():
        if vehicle.startswith("tramvay_donus"):
            print("Tram is:", vehicle)
            print("Time is:", traci.simulation.getTime())

    for detector in Detectors:

        all_vehicles = traci.inductionloop.getLastStepVehicleIDs(detector)

        for vehicle in all_vehicles:
            if(detector, vehicle) not in seen_matches:
        
                seen_matches.add((detector,vehicle))
            
            print("Detector is:",detector)
            print("Time is:",traci.simulation.getTime())
            print("Tram is:",vehicle)

traci.close()
