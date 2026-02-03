#!/usr/bin/python
from ansible.module_utils.basic import AnsibleModule

def main():
    module = AnsibleModule(argument_spec=dict(msg=dict(type='str')))
    
    # Prove we hijacked it
    module.exit_json(changed=False, result_msg=f"!!! OVERWRITTEN ECHO: {module.params['msg']} !!!")

if __name__ == '__main__':
    main()