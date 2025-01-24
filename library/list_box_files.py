#/usr/bin/python

from ansible.module_utils.basic import AnsibleModule
from box_sdk_gen import BoxClient, BoxDeveloperTokenAuth


def run_module():
    # Define available arguments (module input)
    module_args = {
        "token": {"type": "str", "required": True, "no_log": True}
    }

    # Create the Ansible module
    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=True
    )

    # Get token from input parameters
    token = module.params["token"]

    # Business logic (modify as needed)
    # message = f"Hello, {name}!"
    try:
        
        # Authenticate with Box
        auth = BoxDeveloperTokenAuth(token=token)
        client = BoxClient(auth=auth)
        
        # Fetch items from the root folder
        folder_items = client.folders.get_folder_items('0').entries
        files = [{"name": item.name, "id": item.id} for item in folder_items]
    
    except Exception as e:
        module.fail_json(msg=f"Failed to list Box files: {str(e)}")
    

    # Return results
    module.exit_json(changed=False, files=files)

def main():
    run_module()

if __name__ == '__main__':
    main()
