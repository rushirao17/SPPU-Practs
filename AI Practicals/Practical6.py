"""
Implement any one of the following Expert System
I. Information management
II. Hospitals and medical facilities
III. Help desks management
IV. Employee performance evaluation
V. Stock market trading
VI. Airline scheduling and cargo schedules
"""
# Airline scheduling and cargo schedules

rules = [(["cargo_available", "plane_available"], "cargo_schedule"),(["airline_available"], "airline_schedule")]
facts = set()

    
def add_fact(fact):
    facts.add(fact)

def forward_chaining():
    while True:
        new_facts = set()
        for conditions, result in rules:
            all_conditions_met = True
            for condition in conditions:
                if condition not in facts:
                    #Rushikesh Bhalerao
                    all_conditions_met = False
                    break
            if all_conditions_met and result not in facts:
                new_facts.add(result)

        if not new_facts:
            break
        facts.update(new_facts)

def is_possible(item):
    forward_chaining()
    return item in facts

print("Rules are: ",rules)

# Adding facts
add_fact("cargo_available")
add_fact("plane_available")
print("Facts are: ",facts)
print()

if is_possible("cargo_schedule"):
    print("Cargo schedule is possible!")
else:
    print("Cargo schedule is not possible.")

if is_possible("airline_schedule"):
    print("Airline schedule is possible!")
else:
    print("Airline schedule is not possible.")
