
# ansible-community-box-modules

This is a personal project to convert most of the code from the [Box Python SDK](https://github.com/box/box-python-sdk) into custom Ansible modules. The purpose is to explore Python even more and dive deeper into the Ansible framework.

## Overview
This project provides custom Ansible modules to interact with the Box API using Ansible playbooks. Currently, it includes modules for:
- Listing files in a Box folder (`list_box_files.py`)
- Listing folders within a given parent folder (`list_box_folders.py`)
- Creating new folders in Box (`create_box_folder.py`)

---

## Installation & Setup
### 1. Prerequisites
Before using these modules, ensure you have:
- Python 3.x installed
- Ansible installed (`pip install ansible`)
- Box Python SDK (`pip install box-python-sdk`)
- A Box Developer Token from [Box Developer Console](https://app.box.com/developers/console)

### 2. Clone the Repository
```bash
git clone https://github.com/YOUR_USERNAME/ansible-community-box-modules.git
cd ansible-community-box-modules
```

### 3. Configure Ansible
Ensure the `library/` directory is in your Ansible module path:
```ini
[defaults]
library = ./library
```
Or set it dynamically in your playbooks.

---

## Usage Examples
### 1. List Files in a Box Folder
```yaml
- name: List files in Box folder
  hosts: localhost
  tasks:
    - name: Fetch file list
      list_box_files:
        token: "YOUR_BOX_TOKEN"
      register: box_files

    - debug:
        var: box_files
```

### 2. List Folders in a Box Parent Folder
```yaml
- name: List folders in Box
  hosts: localhost
  tasks:
    - name: Fetch folder list
      list_box_folders:
        token: "YOUR_BOX_TOKEN"
        parent_folder_id: "0"
      register: box_folders

    - debug:
        var: box_folders
```

### 3. Create a New Folder in Box
```yaml
- name: Create a new folder in Box
  hosts: localhost
  tasks:
    - name: Create folder
      create_box_folder:
        token: "YOUR_BOX_TOKEN"
        name: "My_New_Folder"
        parent_folder_id: "0"
      register: new_folder

    - debug:
        var: new_folder
```

---

## Available Modules
| Module Name           | Description                                          |
|-----------------------|------------------------------------------------------|
| `list_box_files.py`   | Lists all files in the specified Box folder.        |
| `list_box_folders.py` | Lists all folders inside a given parent folder.     |
| `create_box_folder.py`| Creates a new folder inside a specified parent ID.  |

---

## Future Enhancements
- More Box API integrations (File Uploads, Metadata, Sharing)
- Better error handling & logging
- Exploring support for OAuth 2.0 instead of developer tokens
- Ansible Galaxy publishing (We will see)

---

## Contributing
This is a personal learning project, but contributions are welcome! Feel free to submit pull requests or open issues.

---

## License
This project is licensed under the MIT License.

---

## Contact
For any questions or feedback, reach out via GitHub Issues.
