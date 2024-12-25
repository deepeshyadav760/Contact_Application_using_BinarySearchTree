class ContactNode:
    def __init__(self, name, phone_number, email):
        self.name = name                       # Name of the contact
        self.phone_number = phone_number       # phone number of the contact
        self.email = email                     # email of the contact
        self.left = None                       # left pointer --initialised to none
        self.right = None                      # right pointer -- initialised to none

# Creating a class ContactBST with all the methods/ operations which we will perform
class ContactBST:
    def __init__(self):
        self.root = None

    # Insert method to insert the contact in the BST_conctact_application
    def insert(self, name, phone_number, email):
        """Insert a contact into the BST."""
        new_node = ContactNode(name, phone_number, email)
        if not self.root:
            self.root = new_node
            return

        current = self.root             # Right now we are at the root node
        while True: 
            if name < current.name:     # Using the < operator we are comparing the two strings (name) as names are stored in the lexicographical order
                if not current.left:
                    current.left = new_node
                    break
                current = current.left    # update current to current.left
            elif name > current.name:
                if not current.right:
                    current.right = new_node
                    break
                current = current.right    # update current to current.right
            else:
                print(f"Contact with name '{name}' already exists!")    # this will have condition if name == current.name
                break

    # This method is to search the contact from the BST by name as name are in lexicographical order
    def search_contact(self, name):
        """Search for a contact by name."""
        current = self.root                # starting from the root
        while current:
            if name == current.name:        # will return the current value/name -- means the root is the name -- search name
                return current
            elif name < current.name:       # this will go to the left subtree of the BST -- name at left node
                current = current.left
            else:
                current = current.right      # otherwise right subtree of the BST -- name at right node
        return None

    # This method is to update the contact in the application
    def update_contact(self, name, phone_number=None, email=None):  # at initial phone_number, email both are none -- need to be updated by user
        """Update an existing contact."""
        contact = self.search_contact(name)    # we will first search the contact by name 
        if contact:
            if phone_number:
                contact.phone_number = phone_number
            if email:
                contact.email = email
            print(f"Contact '{name}' updated successfully.")
        else:
            print(f"Contact '{name}' not found.")


    # This method is to delete the contact from the BST
    def delete_contact(self, name):
        """Delete a contact by name."""
        parent = None                           # Tracks the parent of the current node
        current = self.root                     # Start searching from the root

        while current and current.name != name:
            parent = current                    # Keep track of the parent
            if name < current.name:             # Move to the left subtree if the name is smaller
                current = current.left
            else:                               # Move to the right subtree if the name is larger
                current = current.right

        if not current:
            print(f"Contact '{name}' not found.")  # the contact does not exits
            return

        if not current.left or not current.right:
            child = current.left if current.left else current.right
            if not parent:
                self.root = child             # If the node to be deleted is the root, replace the root with the child
            elif current == parent.left:
                parent.left = child           # If the node to be deleted is the left child of its parent, update parent's left pointer
            else:
                parent.right = child          # If the node to be deleted is the right child of its parent, update parent's right pointer
        else:

            successor_parent = current        # Keep track of the parent of the successor
            successor = current.right         # Start looking in the right subtree
            while successor.left:
                successor_parent = successor  # Move down the tree
                successor = successor.left    # Successor is the leftmost node

            # Replace the current node's data with the successor's data
            current.name, current.phone_number, current.email = (
                successor.name,
                successor.phone_number,
                successor.email,
            )

            # Delete the successor node (it will have at most one child)
            if successor_parent.left == successor:
                successor_parent.left = successor.right            # Update left pointer of successor's parent
            else:
                successor_parent.right = successor.right           # Update right pointer of successor's parent


    # This method is to display the contacts in BST Application
    def display_contacts(self):
        """Display all contacts in sorted order."""
        stack = []                             # Creating a empty stack
        current = self.root                    # making current to root and start the traversal
        while stack or current:
            while current:                     # Traversing towards the left subtree
                stack.append(current)          # pushing the current element to the stack
                current = current.left         # Moving to the left child

            # Process the node at the top of the stack (leftmost node in the subtree)    
            current = stack.pop()              # removing the top node from the stack
            print(f"Name: {current.name}, Phone: {current.phone_number}, Email: {current.email}")
            current = current.right            # moving to the right child of the current node


    # This is to seach the contacts by using the prefix (first) characters of the name
    def search_partial(self, prefix):
        """Search for contacts starting with a given prefix."""
        result = []                             # Creating an empty list to store the matched contacts
        stack = [self.root]                     # start with the root node on the stack

        while stack:
            node = stack.pop()                     # Pop the top node from the stack
            if node:                               # If the node exists
                if node.name.startswith(prefix):   # Check if the node's name starts with the given prefix
                    result.append(node)             # Add the matching node to the result list
                stack.append(node.right)            # add the right child in the stack
                stack.append(node.left)             # add the left child in the stack
        return result

    # This is to export the contacts into csv file--storing contacts
    def export_to_file(self, file_path):
        """Export all contacts to a file in CSV format."""
        with open(file_path, 'w') as file:                  # opeining file with write (w) mode
            stack = []
            current = self.root
            while stack or current:
                while current:
                    stack.append(current)
                    current = current.left
                current = stack.pop()
                file.write(f"{current.name},{current.phone_number},{current.email}\n")
                current = current.right
        print(f"Contacts exported to {file_path}.")


    # This is to import the csv  file of the contacts
    def import_from_file(self, file_path):
        """Import contacts from a CSV file."""
        with open(file_path, 'r') as file:                             # Opening file with read (r) mode
            for line in file:                                          # Reading each line from the file
                name, phone_number, email = line.strip().split(',')    # Striping any leading or trailing white spaces, and spliting the line into name, phone_number, email
                self.insert(name, phone_number, email)                 # Insert the contact into the binary search tree (BST)
        print(f"Contacts imported from {file_path}.") 