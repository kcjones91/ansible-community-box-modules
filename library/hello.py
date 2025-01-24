#!/usr/bin/python

from ansible.module_utils.basic import AnsibleModule

def run_module():
    # Define available arguments (module input)
    module_args = {
        "name": {"type": "str", "required": True}
    }

    # Create the Ansible module
    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=True
    )

    # Get the input parameters
    name = module.params["name"]

    # Business logic (modify as needed)
    message = f"Hello, {name}!"

    # Return results
    module.exit_json(changed=False, message=message)

def main():
    run_module()

if __name__ == '__main__':
    main()
