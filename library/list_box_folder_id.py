#/usr/bin/python

from ansible.module_utils.basic import AnsibleModule
from box_sdk_gen import BoxClient, BoxDeveloperTokenAuth


def run_module():
    # Define available arguments (module input)
    module_args = {
        "token": {"type": "str", "required": True, "no_log": True},
        "folder_id": {"type": "str", "required": True},
        "fields" : {"type": "str", "required": True}
    }

    # Create the Ansible module
    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=True
    )

    # Get token from input parameters
    token = module.params["token"]
    folder_id = module.params["folder_id"]
    fields = module.params["fields"]

    # Business logic (modify as needed)
    try:
        
        # Authenticate with Box
        auth = BoxDeveloperTokenAuth(token=token)
        client = BoxClient(auth=auth)
        
        # Fetch items from folder based on folder_id
        folder = client.folders.get_folder_by_id(folder_id=folder_id, fields=[fields])

        # Convert FolderFull object to dictionary
        folder_dict = folder.to_dict()
        
    except Exception as e:
        module.fail_json(msg=f"Failed to list folder by id: {str(e)}")
    

    # Return results
    module.exit_json(changed=False, folder=folder_dict)

def main():
    run_module()

if __name__ == '__main__':
    main()
