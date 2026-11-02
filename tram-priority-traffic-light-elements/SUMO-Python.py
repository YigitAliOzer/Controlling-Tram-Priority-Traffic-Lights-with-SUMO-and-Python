import traci

# Starting SUMO with Python
traci.start([
    "sumo-gui",
    "-c", "Tramvay_simulasyon.sumocfg",
    "--start",
    "--delay", "100"
])

# Getting detector information
Detectors = traci.inductionloop.getIDList()

for detector in Detectors:

    lane = traci.inductionloop.getLaneID(detector)
    print("Detector is:", detector)
    print("Lane is:", lane)
    print("Position is:",traci.inductionloop.getPosition(detector))
    print("Lane length is:",traci.lane.getLength(lane))

seen_matches = set()
last_lane = None

# Simulation loops
for j in range(901):

    traci.simulationStep()

    # Tracking the first tram departed from east
    if "tramvay_donus.0" in traci.vehicle.getIDList():

        lane = traci.vehicle.getLaneID("tramvay_donus.0")

        if lane != last_lane:
            print("East tram lane is:", lane)

            if lane == "Lane8_1":
                print("Tram position is:", traci.vehicle.getLanePosition("tramvay_donus.0"))
            
            last_lane = lane

    # Reading both detectors at every simulation step
    for detector in Detectors:

        all_vehicles = traci.inductionloop.getLastStepVehicleIDs(detector)

        for vehicle in all_vehicles:

            if (detector, vehicle) not in seen_matches:

                seen_matches.add((detector, vehicle))

                print("---------------------------")
                print("Detector is:", detector)
                print("Time is:", traci.simulation.getTime())
                print("Tram is:", vehicle)

                # Getting tram speed
                speed = traci.vehicle.getSpeed(vehicle)
                print("Speed is:", round(speed, 2), "m/s")

                # Getting forthcoming traffic lights
                lights = traci.vehicle.getNextTLS(vehicle)

                for light in lights:

                    if light[0] == "J1" and light[2] >= 0:

                        distance = light[2]
                        status = light[3]

                        print("Distance is:", round(distance, 2), "meters")
                        print("Signal is:", status)

                        # Estimated time of arrival(ETA)
                        if speed > 0.1:

                            ETA = distance / speed
                            print("ETA is:", round(ETA, 2), "seconds")

                        else:
                            print("ETA cannot be calculated: tram is stopped")

                        # Current traffic signal phase
                        phase = traci.trafficlight.getPhase("J1")
                        print("Phase is:", phase)

                        break

traci.close()
