#!/usr/bin/env python3
"""
Ansible dynamic inventory script for saltstack source
"""
import sys
import json

DOCUMENTATION = '''
---
inventory: saltstack
short_description: SaltStack minion inventory script
description:
  - Generates inventory of SaltStack managed minions
'''
try:
    import salt
    import salt.client
except ImportError:
    print("failed=True msg='`saltstack` is required for this script'")
    sys.exit(1)

def main():
    """
    generate the salt inventory for ansible
    includes detailed grain data
    """
    local = salt.client.LocalClient()

    if len(sys.argv) == 2 and sys.argv[1] == '--list':
        print(json.dumps(local.cmd('*', 'grains.items'), indent=4, sort_keys=True))
    elif len(sys.argv) == 3 and sys.argv[1] == '--host':
        print(json.dumps(local.cmd(sys.argv[2], 'grains.items'), indent=4, sort_keys=True))
    else:
        print("Need an argument, either --list or --host <host>")

if __name__ == "__main__":
    main()
