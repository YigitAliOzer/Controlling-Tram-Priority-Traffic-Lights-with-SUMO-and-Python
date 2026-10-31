# Controlling-Tram-Priority-Traffic-Lights-with-SUMO-and-Python
Development of tram priority signalized traffic light control system using SUMO and several Python libraries.

This student study aims to provide signal priority with traffic lights at an intersection described as a four-way junction.
The goal is to reduce tram delays and waiting times through feedback based on parameters such as traffic density and road demand.

Simulation Inventory
1- Four-way intersection
2- Tram flow with defined routes (90-second intervals) and Poisson-distributed car flow (Poisson=0.08333)
3- Fixed-time 60-second traffic light cycle (25-3-2-25-3-2)
4- Detectors for tram detection

Control Strategy
Tram data from the detector will be evaluated by the controller to predict arrival time at the intersection, and signal priority will be provided using strategies such as early green light and green light extension.

Study Status: In Progress

Software Tools
SUMO(Simulation of Urban MObility)
Python->TraCI Library
Python->NumPy,MatPlotLib,Pandas Libraries(For planned analyzes)

Artificial Intelligence (AI) Assistance and Integrity
Artificial Intelligence (AI) tools were used for conceptual explanations, troubleshooting assistance, and documentation support.

How to Run
1. Install Eclipse SUMO.
2. Download or clone this repository.
3. Open `Tramvay_simulasyon.sumocfg` in SUMO-GUI.
4. Run `SUMO-Python.py` to test the TraCI-based detection system.(When planned phases being finished)



