# Simple Online Voting System in Python (CLI Version)

# In-memory databases (for demo purposes)
admins = {"admin": "admin123"}  # username: password
voters = {}  # voter_id: {"name": str, "password": str, "voted": bool}
candidates = []  # list of candidate names
votes = {}  # candidate_name: number_of_votes

def admin_login():
    username = input("Enter admin username: ")
    password = input("Enter admin password: ")
    if admins.get(username) == password:
        print(f"\nWelcome, {username} (Admin)!\n")
        admin_menu()
    else:
        print("Invalid admin credentials!\n")

def admin_menu():
    while True:
        print("1. Add Candidate")
        print("2. View Results")
        print("3. Logout")
        choice = input("Enter choice: ")

        if choice == '1':
            add_candidate()
        elif choice == '2':
            view_results()
        elif choice == '3':
            break
        else:
            print("Invalid choice!\n")

def add_candidate():
    candidate = input("Enter candidate name: ").strip()
    if candidate in candidates:
        print("Candidate already exists!\n")
    else:
        candidates.append(candidate)
        votes[candidate] = 0
        print(f"Candidate '{candidate}' added successfully!\n")

def view_results():
    if not candidates:
        print("No candidates available!\n")
        return
    print("\n--- Voting Results ---")
    for candidate in candidates:
        print(f"{candidate}: {votes[candidate]} votes")
    print()

def register_voter():
    voter_id = input("Enter Voter ID: ").strip()
    if voter_id in voters:
        print("Voter ID already registered!\n")
        return
    name = input("Enter Name: ")
    password = input("Set Password: ")
    voters[voter_id] = {"name": name, "password": password, "voted": False}
    print(f"Voter '{name}' registered successfully!\n")

def voter_login():
    voter_id = input("Enter Voter ID: ").strip()
    password = input("Enter Password: ")
    voter = voters.get(voter_id)

    if voter and voter['password'] == password:
        print(f"\nWelcome, {voter['name']}!\n")
        voter_menu(voter_id)
    else:
        print("Invalid Voter ID or Password!\n")

def voter_menu(voter_id):
    voter = voters[voter_id]
    if voter['voted']:
        print("You have already voted!\n")
        return

    if not candidates:
        print("Voting not available yet. No candidates found!\n")
        return

    print("--- Candidates ---")
    for idx, candidate in enumerate(candidates, start=1):
        print(f"{idx}. {candidate}")

    choice = input("Enter candidate number to vote: ")

    try:
        choice = int(choice)
        if 1 <= choice <= len(candidates):
            selected_candidate = candidates[choice - 1]
            votes[selected_candidate] += 1
            voters[voter_id]['voted'] = True
            print(f"You voted for {selected_candidate}!\n")
        else:
            print("Invalid candidate choice!\n")
    except ValueError:
        print("Invalid input! Please enter a number.\n")

def main():
    while True:
        print("=== Online Voting System ===")
        print("1. Admin Login")
        print("2. Register as Voter")
        print("3. Voter Login")
        print("4. Exit")
        choice = input("Enter choice: ")

        if choice == '1':
            admin_login()
        elif choice == '2':
            register_voter()
        elif choice == '3':
            voter_login()
        elif choice == '4':
            print("Thank you for using the Online Voting System!")
            break
        else:
            print("Invalid choice!\n")

if __name__ == "__main__":
    main()
