#/usr/bin/python
# Create folder on box

from ansible.module_utils.basic import AnsibleModule
from box_sdk_gen import BoxClient, BoxDeveloperTokenAuth


def run_module():
    # Define available arguments (module input)
    module_args = {
        "token": {"type": "str", "required": True, "no_log": True},
        "name": {"type": "str", "required": True},
        "parent_folder_id": {"type": "str", "required": False}
    }

    # Create the Ansible module
    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=True
    )

    # Get token from input parameters
    token = module.params["token"]
    name = module.params["name"]
    parent_folder_id = module.params["parent_folder_id"]

    # Business logic (modify as needed)
    try:
        
        # Authenticate with Box
        auth = BoxDeveloperTokenAuth(token=token)
        client = BoxClient(auth=auth)
        
        
        if (parent_folder_id and name):
            
            # Fetch items from folder based on folder_id
            new_folder = client.folders.create_folder(parent={"id": parent_folder_id}, name=name)

        else:
            
            # Fetch items from folder based on folder_id ( this might not be needed)
            new_folder = client.folders.create_folder(name=name)

        # Convert new_folder to dictionary to allow ansible to parse correctly
        new_folder_to_dict = new_folder.to_dict()
                                        
        
    except Exception as e:
        module.fail_json(msg=f"Failed to list folder by id: {str(e)}")
    

    # Return results
    module.exit_json(changed=False, folder=new_folder_to_dict)

def main():
    run_module()

if __name__ == '__main__':
    main()
