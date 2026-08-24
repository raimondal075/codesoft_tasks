
contacts = []

def show_menu():
	print("\n" + "=" * 40)
	print("           CONTACT BOOK MENU")
	print("=" * 40)
	print("1. Add Contact")
	print("2. View All Contacts")
	print("3. Search Contact")
	print("4. Update Contact")
	print("5. Delete Contact")
	print("6. Exit")
	print("=" * 40)

def get_valid_choice():
	"""Ask for a menu choice and make sure it's a valid number 1-6."""
	choice = input("Enter your choice (1-6): ").strip()
	if choice.isdigit() and 1 <= int(choice) <= 6:
		return int(choice)
	else:
		print("Invalid choice! Please enter a number between 1 and 6.")
		return None

def add_contact():
	print("\n--- Add New Contact ---")
	name = input("Enter name: ").strip()

	if name == "":
		print("Name cannot be empty. Contact not added.")
		return

	phone = input("Enter phone number: ").strip()
	email = input("Enter email: ").strip()
	address = input("Enter address: ").strip()

	new_contact = {
		"name": name,
		"phone": phone,
		"email": email,
		"address": address
	}

	contacts.append(new_contact)
	print(f"Contact '{name}' added successfully!")

def view_contacts():
	print("\n--- All Contacts ---")
	if len(contacts) == 0:
		print("No contacts saved yet.")
		return

	print(f"{'No.':<5}{'Name':<20}{'Phone':<15}")
	print("-" * 40)
	for index, contact in enumerate(contacts, start=1):
		print(f"{index:<5}{contact['name']:<20}{contact['phone']:<15}")

def find_contact_indexes(search_term):
	"""Return a list of indexes of contacts matching the name or phone."""
	search_term = search_term.strip().lower()
	matches = []
	for index, contact in enumerate(contacts):
		if search_term in contact["name"].lower() or search_term in contact["phone"].lower():
			matches.append(index)
	return matches

def show_contact_details(index):
	contact = contacts[index]
	print("-" * 40)
	print(f"Name    : {contact['name']}")
	print(f"Phone   : {contact['phone']}")
	print(f"Email   : {contact['email']}")
	print(f"Address : {contact['address']}")
	print("-" * 40)

def search_contact():
	print("\n--- Search Contact ---")
	if len(contacts) == 0:
		print("No contacts saved yet.")
		return

	search_term = input("Enter name or phone number to search: ").strip()

	if search_term == "":
		print("Search term cannot be empty.")
		return

	matches = find_contact_indexes(search_term)

	if len(matches) == 0:
		print("No matching contact found.")
	else:
		print(f"\nFound {len(matches)} matching contact(s):")
		for i in matches:
			show_contact_details(i)

def update_contact():
	print("\n--- Update Contact ---")
	if len(contacts) == 0:
		print("No contacts saved yet.")
		return

	search_term = input("Enter name or phone number of the contact to update: ").strip()
	matches = find_contact_indexes(search_term)

	if len(matches) == 0:
		print("No matching contact found.")
		return

	if len(matches) > 1:
		print("\nMultiple matching contacts found:")
		for i in matches:
			show_contact_details(i)
		print("Please search with a more specific name or phone number.")
		return

	index = matches[0]
	print("\nCurrent details:")
	show_contact_details(index)

	print("\nEnter new details. Press Enter to keep the current value.")

	new_name = input(f"Name [{contacts[index]['name']}]: ").strip()
	new_phone = input(f"Phone [{contacts[index]['phone']}]: ").strip()
	new_email = input(f"Email [{contacts[index]['email']}]: ").strip()
	new_address = input(f"Address [{contacts[index]['address']}]: ").strip()

	if new_name != "":
		contacts[index]["name"] = new_name
	if new_phone != "":
		contacts[index]["phone"] = new_phone
	if new_email != "":
		contacts[index]["email"] = new_email
	if new_address != "":
		contacts[index]["address"] = new_address

	print("Contact updated successfully!")

def delete_contact():
	print("\n--- Delete Contact ---")
	if len(contacts) == 0:
		print("No contacts saved yet.")
		return

	search_term = input("Enter name or phone number of the contact to delete: ").strip()
	matches = find_contact_indexes(search_term)

	if len(matches) == 0:
		print("No matching contact found.")
		return

	if len(matches) > 1:
		print("\nMultiple matching contacts found:")
		for i in matches:
			show_contact_details(i)
		print("Please search with a more specific name or phone number.")
		return

	index = matches[0]
	print("\nContact to delete:")
	show_contact_details(index)

	confirm = input("Are you sure you want to delete this contact? (yes/no): ").strip().lower()
	while confirm not in ["yes", "no", "y", "n"]:
		confirm = input("Please enter 'yes' or 'no': ").strip().lower()

	if confirm in ["yes", "y"]:
		removed_name = contacts[index]["name"]
		del contacts[index]
		print(f"Contact '{removed_name}' deleted successfully!")
	else:
		print("Deletion cancelled.")

def main():
	print("Welcome to your Command-Line Contact Book!")

	while True:
		show_menu()
		choice = get_valid_choice()

		if choice is None:
			continue
		elif choice == 1:
			add_contact()
		elif choice == 2:
			view_contacts()
		elif choice == 3:
			search_contact()
		elif choice == 4:
			update_contact()
		elif choice == 5:
			delete_contact()
		elif choice == 6:
			print("\nThank you for using the Contact Book. Goodbye!")
			break

if __name__ == "__main__":
	main()
