#!/usr/bin/python
# -*- coding: utf-8 -*-

ANSIBLE_METADATA = {'metadata_version': '1.1',
                    'status': ['preview'],
                    'supported_by': 'community'}

DOCUMENTATION = '''
---
module: ibm_lb_vpx
short_description: Configure IBM Cloud 'ibm_lb_vpx' resource

version_added: "2.8"

description:
    - Create, update or destroy an IBM Cloud 'ibm_lb_vpx' resource

requirements:
    - IBM-Cloud terraform-provider-ibm v1.3.0
    - Terraform v0.12.20

options:
    private_subnet:
        description:
            - None
        required: False
        type: str
    management_ip_address:
        description:
            - None
        required: False
        type: str
    tags:
        description:
            - None
        required: False
        type: list
        elements: str
    name:
        description:
            - None
        required: False
        type: str
    datacenter:
        description:
            - (Required for new resource) 
        required: False
        type: str
    ip_count:
        description:
            - (Required for new resource) 
        required: False
        type: int
    public_subnet:
        description:
            - None
        required: False
        type: str
    plan:
        description:
            - (Required for new resource) 
        required: False
        type: str
    public_vlan_id:
        description:
            - None
        required: False
        type: int
    private_vlan_id:
        description:
            - None
        required: False
        type: int
    type:
        description:
            - None
        required: False
        type: str
    speed:
        description:
            - (Required for new resource) 
        required: False
        type: int
    vip_pool:
        description:
            - None
        required: False
        type: list
        elements: str
    version:
        description:
            - (Required for new resource) 
        required: False
        type: str
    id:
        description:
            - (Required when updating or destroying existing resource) IBM Cloud Resource ID.
        required: False
        type: str
    state:
        description:
            - State of resource
        choices:
            - available
            - absent
        default: available
        required: False
    ibmcloud_api_key:
        description:
            - The API Key used for authentification. This can also be
              provided via the environment variable 'IC_API_KEY'.
        required: True
    ibmcloud_region:
        description:
            - Denotes which IBM Cloud region to connect to
        default: us-south
        required: False
    ibmcloud_zone:
        description:
            - Denotes which IBM Cloud zone to connect to in multizone
              environment. This can also be provided via the environmental
              variable 'IC_ZONE'.
        required: False

author:
    - Jay Carman (@jaywcarman)
'''

# Top level parameter keys required by Terraform module
TL_REQUIRED_PARAMETERS = [
    ('datacenter', 'str'),
    ('ip_count', 'int'),
    ('plan', 'str'),
    ('speed', 'int'),
    ('version', 'str'),
]

# All top level parameter keys supported by Terraform module
TL_ALL_PARAMETERS = [
    'private_subnet',
    'management_ip_address',
    'tags',
    'name',
    'datacenter',
    'ip_count',
    'public_subnet',
    'plan',
    'public_vlan_id',
    'private_vlan_id',
    'type',
    'speed',
    'vip_pool',
    'version',
]

# define available arguments/parameters a user can pass to the module
from ansible.module_utils.basic import env_fallback
module_args = dict(
    private_subnet=dict(
        required=False,
        type='str'),
    management_ip_address=dict(
        required=False,
        type='str'),
    tags=dict(
        required=False,
        elements='',
        type='list'),
    name=dict(
        required=False,
        type='str'),
    datacenter=dict(
        required=False,
        type='str'),
    ip_count=dict(
        required=False,
        type='int'),
    public_subnet=dict(
        required=False,
        type='str'),
    plan=dict(
        required=False,
        type='str'),
    public_vlan_id=dict(
        required=False,
        type='int'),
    private_vlan_id=dict(
        required=False,
        type='int'),
    type=dict(
        required=False,
        type='str'),
    speed=dict(
        required=False,
        type='int'),
    vip_pool=dict(
        required=False,
        elements='',
        type='list'),
    version=dict(
        required=False,
        type='str'),
    id=dict(
        required=False,
        type='str'),
    state=dict(
        type='str',
        required=False,
        default='available',
        choices=(['available', 'absent'])),
    ibmcloud_api_key=dict(
        type='str',
        no_log=True,
        fallback=(env_fallback, ['IC_API_KEY']),
        required=True),
    ibmcloud_region=dict(
        type='str',
        fallback=(env_fallback, ['IC_REGION']),
        default='us-south'),
    ibmcloud_zone=dict(
        type='str',
        fallback=(env_fallback, ['IC_ZONE']))
)


def run_module():
    from ansible.module_utils.basic import AnsibleModule
    import ansible.module_utils.ibmcloud as ibmcloud

    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=False
    )

    # New resource required arguments checks
    missing_args = []
    if module.params['id'] is None:
        for arg, _ in TL_REQUIRED_PARAMETERS:
            if module.params[arg] is None:
                missing_args.append(arg)
        if missing_args:
            module.fail_json(msg=(
                "missing required arguments: " + ", ".join(missing_args)))

    result = ibmcloud.ibmcloud_terraform(
        resource_type='ibm_lb_vpx',
        tf_type='resource',
        parameters=module.params,
        ibm_provider_version='1.3.0',
        tl_required_params=TL_REQUIRED_PARAMETERS,
        tl_all_params=TL_ALL_PARAMETERS)

    if result['rc'] > 0:
        module.fail_json(
            msg=ibmcloud.Terraform.parse_stderr(result['stderr']), **result)

    module.exit_json(**result)


def main():
    run_module()


if __name__ == '__main__':
    main()