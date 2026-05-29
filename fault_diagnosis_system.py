import random
import time
from collections import deque

# -----------------------------------
# AI-Based Fault Diagnosis System
# -----------------------------------

MAX_CYCLES = 5

# -----------------------------------
# Sensor Data Representation
# -----------------------------------

class SensorState:

    def __init__(
        self,
        cycle,
        temperature,
        pressure,
        vibration
    ):

        self.cycle = cycle
        self.temperature = temperature
        self.pressure = pressure
        self.vibration = vibration

    def is_critical(self):

        return (
            self.temperature > 100 or
            self.pressure > 130 or
            self.vibration > 80
        )

# -----------------------------------
# Knowledge Representation
# -----------------------------------

def detect_faults(state):

    faults = []

    if state.temperature > 90:
        faults.append("Overheating Fault")

    if state.pressure > 120:
        faults.append("Pressure Fault")

    if state.vibration > 75:
        faults.append("Bearing Fault")

    return faults

# -----------------------------------
# Search Algorithm
# -----------------------------------

fault_graph = {

    "Normal":
        ["Overheating Fault", "Pressure Fault"],

    "Overheating Fault":
        ["Critical Failure"],

    "Pressure Fault":
        ["Critical Failure"],

    "Bearing Fault":
        ["Critical Failure"],

    "Critical Failure":
        []
}

def bfs_search(start, goal):

    queue = deque([[start]])

    visited = set()

    while queue:

        path = queue.popleft()

        node = path[-1]

        if node == goal:
            return path

        if node not in visited:

            visited.add(node)

            for neighbor in fault_graph.get(node, []):

                new_path = list(path)

                new_path.append(neighbor)

                queue.append(new_path)

    return None

# -----------------------------------
# Constraint Satisfaction
# -----------------------------------

def validate_constraints(state):

    violations = []

    if state.temperature > 100:
        violations.append("Temperature Limit Exceeded")

    if state.pressure > 130:
        violations.append("Pressure Limit Exceeded")

    if state.vibration > 80:
        violations.append("Vibration Limit Exceeded")

    return violations

# -----------------------------------
# Utility-Based Decision Making
# -----------------------------------

def calculate_risk(state):

    risk = (
        state.temperature * 0.4 +
        state.pressure * 0.3 +
        state.vibration * 0.3
    )

    return risk

def maintenance_decision(risk):

    if risk > 100:
        return "Emergency Shutdown"

    elif risk > 80:
        return "Immediate Maintenance"

    elif risk > 60:
        return "Inspection Required"

    else:
        return "System Normal"

# -----------------------------------
# Bayesian Prediction
# -----------------------------------

def predict_failure_probability(state):

    probability = 0

    if state.temperature > 90:
        probability += 0.4

    if state.pressure > 120:
        probability += 0.3

    if state.vibration > 75:
        probability += 0.3

    return probability

# -----------------------------------
# Explainable AI
# -----------------------------------

def explain_results(
    faults,
    violations,
    probability,
    decision
):

    print("\n========== AI REPORT ==========")

    print("\nDetected Faults:")

    if faults:
        for fault in faults:
            print("-", fault)

    else:
        print("No Faults Detected")

    print("\nConstraint Violations:")

    if violations:
        for violation in violations:
            print("-", violation)

    else:
        print("No Violations")

    print("\nFailure Probability:")
    print(round(probability * 100, 2), "%")

    print("\nRecommended Action:")
    print(decision)

    print("\nReasoning:")

    if probability > 0.7:
        print("High chance of machine failure.")

    if violations:
        print("Machine operating outside safe limits.")

    print("================================")

# -----------------------------------
# Display Sensor Data
# -----------------------------------

def display_state(state):

    print("\n----------------------------")
    print("Cycle:", state.cycle)
    print("----------------------------")

    print("Temperature :", state.temperature)
    print("Pressure    :", state.pressure)
    print("Vibration   :", state.vibration)

# -----------------------------------
# Main System
# -----------------------------------

def run_system():

    print("==========================================")
    print(" AI-Based Fault Diagnosis System ")
    print("==========================================")

    for cycle in range(1, MAX_CYCLES + 1):

        state = SensorState(

            cycle,

            random.randint(50, 120),

            random.randint(70, 150),

            random.randint(20, 100)
        )

        display_state(state)

        # Fault Detection

        faults = detect_faults(state)

        print("\nDetected Faults:")
        print(faults)

        # Search Analysis

        if faults:

            print("\nFault Search Path:")

            path = bfs_search(
                faults[0],
                "Critical Failure"
            )

            print(path)

        # Constraint Checking

        violations = validate_constraints(state)

        print("\nConstraint Violations:")
        print(violations)

        # Decision Making

        risk = calculate_risk(state)

        decision = maintenance_decision(risk)

        print("\nRisk Score:")
        print(round(risk, 2))

        print("\nDecision:")
        print(decision)

        # Probabilistic Prediction

        probability = predict_failure_probability(state)

        print("\nFailure Probability:")
        print(round(probability * 100, 2), "%")

        # Explainable AI

        explain_results(
            faults,
            violations,
            probability,
            decision
        )

        if state.is_critical():

            print("\nCritical Machine State Reached")
            break

# -----------------------------------
# Run Program — Keeps Running on Render
# -----------------------------------

if __name__ == "__main__":

    run_number = 1

    while True:

        print("\n\n==========================================")
        print(f" RUN #{run_number} STARTED ")
        print("==========================================")

        run_system()

        print(f"\n✅ Run #{run_number} Complete.")
        print("Waiting 60 seconds before next run...")
        print("==========================================")

        run_number += 1

        time.sleep(60)