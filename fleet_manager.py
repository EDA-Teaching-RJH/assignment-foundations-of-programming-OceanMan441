VALID_RANKS = [
    "Captain",
    "Commander",
    "Lt. Commander",
    "Lieutenant",
    "Ensign"
]

VALID_DIVISIONS = [
    "Command",
    "Operations",
    "Sciences",
    "Security"
]

def init_database():
    names = ["Jean-Luc Picard", "William Riker", "Data", "Worf", "Beverly Crusher"]
    ranks = ["Captain", "Commander", "Lt. Commander", "Lieutenant", "Commander"]
    divs = ["Command","Command", "Operations", "Security", "Sciences"]
    ids = ["1001", "1002", "1003", "1004", "1005"]

    return names, ranks, divs, ids


def display_menu(user):
    print("\n====================================")
    print(f"Fleet Manager - Logged in as: {user}")
    print("====================================")
    print("1. Add Member")
    print("2. Remove Member")
    print("3. Update Rank")
    print("4. Display Roster")
    print("5. Search Crew")
    print("6. Filter by Division")
    print("7. Calculate Payroll")
    print("8. Count Officers")
    print("9. Exit")
    print("====================================")

    return input("Select option")


def add_member(names, ranks, divs, ids):
    name = input("Enter Name: ")
    rank = input("Enter Rank: ")
    division = input("Enter Division: ")
    id_ = input("Enter ID: ")
    
    if id_ in ids:
        print("Error: ID must be unique.")
    
    if rank not in VALID_RANKS:
        ("Error: Invalid Rank.")
    return
    if division not in VALID_DIVISIONS:
        print("Error: Invalid Division. ")

    names.append(name)
    ranks.append(rank)
    divs.append(division)
    ids.append(id_)

print("Crew member successfully added.")

def remove_member(names, ranks, divs, ids):
    id_ = input("Enter ID to remove: ")

    if id_ in ids:
        index = ids.index(id_)

        names.pop(index)
        ranks.pop(index)
        divs.pop(index)
        ids.pop(index)

        print("Crew member removed.")
    else:
        print("Error: ID not found.")

def update_rank(names, ranks, ids):
    id_ = input("Enter ID to update: ")

    if id_ in ids:
        idnex = ids.index(id_)
        new_rank = input("Enter new rank: ")

        if new_rank in VALID_RANKS:
            ranks[idnex] = new_rank
            print("Rank updated successfully.")
        else:
            print("Error: Invalid rank.")
    else:
        print("Error: ID not found.")

def display_roster(names, ranks, divs, ids):
     print("\n================ CREW ROSTER ================")
     print("ID     | Name                 | Rank            | Division")
     print("-----------------------------------------------------------")
     
     for i in range(len(names)):
         print(ids[i], "|", names[i], "|", ranks[i], "|", divs[i])

     print("-----------------------------------------------------------")


def search_crew(names, ranks, divs, ids):
    term = input("Enter name search term: ").lower()
    found = False
   
    for i in range(len(names)):
        if term in names[i].lower():
            print(ids[i], "|", names[i], "|", ranks[i], "|", divs[i])
        found = True

    if not found:
        print("No matching crew found.")

def filter_by_division(names, divs):
    division = input("Enter Division (Command/Operations/Sciences/Security): ")

    if division not in VALID_DIVISIONS:
        print("Invalid Disivion.")
        return
    
    print("\nCrew in", division, "Division:")

    for i in range(len(names)):
        if divs[i] == division:
            print(names[i])

def calcuate_payroll(ranks):
    total = 0

    for rank in ranks:
        if rank == "Captain":
            total += 1000
        elif rank == "Commander":
            total += 800
        elif rank == "Lt. Commander":
            total += 600
        elif rank == "Lieutenant":
            total += 400
        elif rank == "Ensign":
            total += 200

    return total

def count_officers(ranks):
    count = 0

    for rank in ranks:
        if rank == "Captain" or rank == "Commander":
            count += 1
    
    return count
