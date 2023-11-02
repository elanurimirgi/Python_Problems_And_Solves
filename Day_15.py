#Homework1
class Notebook:
    def __init__(self):
        self.notes = {}  # We will store the notes in a dictionary.

    def add_note(self, title, content):
        self.notes[title] = content
        print(f"Note added: {title}")

    def update_note(self, title, new_content):
        if title in self.notes:
            self.notes[title] = new_content
            print(f"Note updated: {title}")
        else:
            print("Note not found.")

    def delete_note(self, title):
        if title in self.notes:
            del self.notes[title]
            print(f"Note deleted: {title}")
        else:
            print("Note not found.")

    def list_notes(self):
        print("Your notes:")
        for title, content in self.notes.items():
            print(f"{title}: {content}")

    def save_notes(self, file_name):
        with open(file_name, "w") as file:
            for title, content in self.notes.items():
                file.write(f"{title}: {content}\n")
        print("Notes saved to a file.")

    def load_notes(self, file_name):
        try:
            with open(file_name, "r") as file:
                lines = file.readlines()
            for line in lines:
                title, content = line.strip().split(": ", 1)
                self.notes[title] = content
            print("Notes loaded from a file.")
        except FileNotFoundError:
            print("Notes file not found.")

def main():
    notebook = Notebook()
    while True:
        print("\nAvailable actions:")
        print("1. Add a Note")
        print("2. Update a Note")
        print("3. Delete a Note")
        print("4. List Notes")
        print("5. Save Notes")
        print("6. Load Notes")
        print("7. Exit")
        choice = input("Please select an action (1/2/3/4/5/6/7): ")

        if choice == "1":
            title = input("Enter the note title: ")
            content = input("Enter the note content: ")
            notebook.add_note(title, content)
        elif choice == "2":
            title = input("Enter the title of the note to update: ")
            new_content = input("Enter the new content: ")
            notebook.update_note(title, new_content)
        elif choice == "3":
            title = input("Enter the title of the note to delete: ")
            notebook.delete_note(title)
        elif choice == "4":
            notebook.list_notes()
        elif choice == "5":
            file_name = input("Enter the file name to save the notes: ")
            notebook.save_notes(file_name)
        elif choice == "6":
            file_name = input("Enter the file name to load the notes: ")
            notebook.load_notes(file_name)
        elif choice == "7":
            print("Notebook application is closing.")
            break
        else:
            print("You made an invalid choice. Please try again.")

if __name__ == "__main__":
    main()
