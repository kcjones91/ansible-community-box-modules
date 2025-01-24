#/usr/bin/python
# Create folder on box
import os
import json
from ansible.module_utils.basic import AnsibleModule
from box_sdk_gen import BoxClient, BoxDeveloperTokenAuth



def run_module():
    # Define available arguments (module input)
    module_args = {
        "token": {"type": "str", "required": True, "no_log": True},
        "src_file_path": {"type": "str", "required": True},
        "dest_file_name": {"type": "str", "required": True},
        "parent_folder_id": {"type": "str", "required": True}
    }

    # Create the Ansible module
    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=True
    )

    # Get token from input parameters
    token = module.params["token"]
    src_file_path = module.params["src_file_path"]
    dest_file_name = module.params["dest_file_name"]
    parent_folder_id = module.params["parent_folder_id"]

    # Verify if the file exists
    if not os.path.exists(src_file_path):
        module.fail_json(msg=f"File not found: {src_file_path}")

    # Business logic (modify as needed)
    try:
        
        # Authenticate with Box
        auth = BoxDeveloperTokenAuth(token=token)
        client = BoxClient(auth=auth)
        
        # # Upload file to Box
        # with open(file_path, "rb") as file_stream:
        #     attributes = {
        #         "name": file_name,
        #         "parent": {"id": parent_folder_id }
        #     }
        
        
        attributes = {
            "name": dest_file_name,
            "parent": {"id": parent_folder_id}
        }
        
        # Upload file to Box folder
        with open(src_file_path, "rb") as file_stream:
            uploaded_file = client.uploads.upload_file(
                attributes=attributes,
                file=file_stream
            )
        # Convert new_folder to dictionary to allow ansible to parse correctly
        uploaded_file_dict = uploaded_file.to_dict()
                                        
        
    except Exception as e:
        module.fail_json(msg=f"Failed to upload file to folder: {str(e)}")
    

    # Return results
    module.exit_json(changed=False, folder=uploaded_file_dict)

def main():
    run_module()

if __name__ == '__main__':
    main()
