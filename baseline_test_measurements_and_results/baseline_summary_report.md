# Fixed-Time Baseline — Simulation Results

## Experiment

- **Model:** Four-leg signalized intersection with bidirectional trams and road vehicles in Eclipse SUMO.
- **Signal plan:** Fixed-time, 60-second cycle (25 s green, 3 s yellow, 2 s all-red for each of two phase groups).
- **Tram departures:** Every 90 s in each direction (0–810 s).
- **Traffic generation:** SUMO vehicle flows; simulation **random seed: 42**.
- **Vehicle departures:** Up to simulation time 900 s; the last recorded trip arrives at 966 s.
- **Controller:** No tram priority is active in this baseline.
- **Sources:** `baseline_tripinfo.xml` and `baseline_detector_events.csv`.

## Completed-trip performance

| Metric | Trams (all) | Road vehicles |
|---|---:|---:|
| Completed trips | 20 | 471 |
| Mean trip duration (s) | 53.00 | 50.88 |
| Mean waiting time (s) | 3.25 | 9.97 |
| Mean time loss (s) | 6.74 | 17.79 |
| Vehicles stopped at least once | 10 / 20 (50.0%) | 297 / 471 (63.1%) |

## Tram direction breakdown

| Metric | Outbound (`tramvay_gidis`) | Return (`tramvay_donus`) |
|---|---:|---:|
| Trips | 10 | 10 |
| Mean trip duration (s) | 54.50 | 51.50 |
| Mean waiting time (s) | 4.50 | 2.00 |
| Mean time loss (s) | 8.08 | 5.40 |

## Tram detector observations

- **20 unique tram detections:** 10 at `dedektor_1` and 10 at `dedektor_2`.
- `dedektor_1` on `Lane3_1`: nominal speed **11.11 m/s**, distance to J1 signal **122.19 m**, initial ETA **11.00 s**.
- `dedektor_2` on `Lane8_1`: nominal speed **11.11 m/s**, distance to J1 signal **203.92 m**, initial ETA **18.35 s**.
- At the detection instant, **10 trams** observed green (`G`) and **10** observed red (`r`) on their signal link.
- **All 10 red-detected trams stopped at least once** in the completed-trip records; the 10 green-detected trams had zero stop events in this run.

## Interpretation and limitations

- **Waiting time** measures time spent nearly stopped; **time loss** also captures slow movement relative to the ideal reference.
- Detector ETA is a **constant-speed estimate at the instant of detection**, not measured travel time or queueing delay.
- Comparisons of **tram vs. road-vehicle trip duration** are not like-for-like route comparisons; their route lengths differ.
- The 491 rows represent **completed trips** in this run, not the number of cars simultaneously in the network.
- This is **one simulation run** at one seed; statistical robustness requires additional controlled replications.
- For the eventual signal-priority comparison, preserve the same network, demand, flow parameters, simulation termination criterion, and random seed(s). Report changes in both tram and road-vehicle performance.

## Data files

- `baseline_metrics.csv`: grouped reference metrics.
- `baseline_tram_details.csv`: per-tram completed-trip measurements joined with first detection observations.
- `baseline_detector_events.csv`: raw first-detection event records.
- `baseline_tripinfo.xml`: raw SUMO completed-trip output (can be retained locally if raw outputs are not included in the repository).
