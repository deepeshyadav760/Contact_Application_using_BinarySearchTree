# Contact Application using Binary Search Tree (BST)

## Overview
This is a Python-based Contact Management System built using a Binary Search Tree (BST). It allows users to efficiently manage contacts with features like insertion, search, update, deletion, and more.

## Features
- **Add Contacts:** Insert new contacts into the system.
- **Search Contacts:** Locate a contact using a full or partial name.
- **Update Contacts:** Modify existing contact details.
- **Delete Contacts:** Remove a contact from the system.
- **Display Contacts:** View all contacts in sorted order.
- **Partial Search:** Search contacts using name prefixes.
- **Export Contacts:** Save all contacts to a CSV file.
- **Import Contacts:** Load contacts from a CSV file.

## Binary Search Tree Operations
- **Insertion:** Contacts are stored in the tree based on the lexicographical order of names.
- **Deletion:** Handles three scenarios:
  - Deleting a leaf node.
  - Deleting a node with one child.
  - Deleting a node with two children (replacing with the in-order successor).
- **Traversal:** Uses in-order traversal to display contacts in a sorted manner.

## Setup and Running Instructions
### Prerequisites
- Python 3.x installed on your system.

### Steps to Run the Application
1. Clone the repository to your local system:
   ```bash
   git clone <repository_url>
