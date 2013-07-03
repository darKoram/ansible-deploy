  

#!/usr/bin/python
# This file is part of Ansible
#
# Ansible is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Ansible is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Ansible. If not, see <http://www.gnu.org/licenses/>.

# REFERENCE MATERIAL
# eclipse p2director docs 
# http://help.eclipse.org/galileo/index.jsp?topic=/org.eclipse.platform.doc.isv/guide/p2_director.html   
# p2 tutorial
# http://blog.vogella.com/2012/04/04/installing-eclipse-features-via-the-command-line-with-the-p2-director/
# eclipse forum thread with lots of p2 related issues
# http://www.eclipse.org/forums/index.php?t=thread&frm_id=31

DOCUMENTATION = '''
---
module: eclipsep2
short_description: create a custom configured eclipse instance
description:
     - creates eclipse instances using the p2director capabilities. This module has a dependency on url downloads.
options:
  user_name:
    description:
      - user name such that /home/<user_name> gives the user's home directory (linux)
    required: false
    default: null
    aliases: ['username']
  application:
    description:
      -  the application performing p2 operations such as install or uninstall.
    required: true
    default: org.eclipse.equinox.p2.director
    aliases: []
  verifyOnly:
    description:
      -  only verify that the actions can be performed. Don't actually install or remove anything.
    required: false
    default: false
    aliases: []
  shared:
    description:
      - shared: use a shared location for the install. The path defaults to ${user.home}/.p2.
    required: false
    default: 
    aliases: []
  ps.os:
    description:
      - os where target will run
    required: false
    default: x86
    aliases: []
  bundlepool:
    description:
      - the location of where the plug-ins and features will be stored. This value is only taken \
        into account when a new profile is created. For an application where all the bundles are \
        located into the plugins/ folder of the destination, set it to <destination>.
     required: false
     default: /opt/eclipse_installs/mobile/eclipse/
  destination:
    description:
      - location of flavor/version of eclipse installation
    required: true
    default: /opt/eclipse_installs/mobile/eclipse/
    aliases: []   
  installIU:
    description:
      - a comma separated list of IUs to install. Each entry in the list is \
        in the form <id> [ '/' <version> ]. If you are looking to install a feature, \ 
        the identifier of the feature has to be suffixed with ".feature.group".
     required: false
     default: org.eclipse.sdk.ide
  metadataRepository:
    description:
      - a comma separated list of metadata repository URLs where the software to be installed can be found.
    required: false
    default: null
    aliases: []
  artifactRepository:
    description: 
      - a comma separated list of artifact repository URLs where the software artifacts can be found
    required: false
    aliases: []
  repository:
    description:
      - a comma separated list of repository URL where each entry denotes colocated \ 
        meta-data and artifact repositories.
    required: true
    default: http://download.eclipse.org/releases/juno/
    aliases: []
  profile:
    description:
      - eclipse profile
    required: true
    default: SDKProfile
    aliases: []
  profileProperties:
    description:
      - a comma separated list of <key>=<value> pair. Example: the property org.eclipse.update.install.features=true \
        will cause the update manager features to be installed.
    required: true
    default: org.eclipse.update.install.features=true
    aliases: []
  wait:
    description:
      - wait for the instance to be in state 'running' before returning
    required: false
    default: "no"
    choices: [ "yes", "no" ]
    aliases: []
  wait_timeout:
    description:
      - how long before wait gives up, in seconds
    default: 300
    aliases: []

    notes:
        - Requires java jdk to be installed.  Some packages require sun jdk.
          This can be installed using javadev module. 
          #TODO finish the javadev module.  In the mean time...
          @see http://docs.oracle.com/javase/7/docs/webnotes/install/index.html
    requirements: [java_jdk]
    author: Kesten Broughton
    '''
    
EXAMPLES = '''
# Basic task example
tasks:
- name: install a fully equiped eclipse dev suite for android
  action: cloudformation >
    stack_name="ansible-cloudformation" state=present
    region=us-east-1 disable_rollback=yes
    template=files/cloudformation-example.json
  args:
    template_parameters:
      KeyName: jmartin
      DiskType: ephemeral
      InstanceType: m1.small
      ClusterSize: 3
'''

ui_install_list = [ org.eclipse.egit.feature.group,
                    org.eclipse.jgit.feature.group
                    #groovy-eclipse 
                  ]

USER_P2 = os.path.expanduser('~/.p2')
DESTINATION_DIR = 
ECLIPSE_EXECUTABLE = "/opt/eclipse_installs/mobile/eclipse/eclipse"

def main():
    module = AnsibleModule(
        argument_spec = dict(
            state     = dict(default='present', choices=['present', 'absent']),
            name      = dict(required=True),
            enabled   = dict(required=True, choices=BOOLEANS),
            supports_check_mode = True
        )
    )
    if state == 'present':
        try:
            
        except Exception, err:

module.exit_json(changed=True, something_else=12345)

module.fail_json(msg="Eclipse mobile unable to stall.  See ansible log for details.")

if module.check_mode:
    # Check if any changes would be made by don't actually make those changes
    verifyOnly=True
    module.exit_json(changed=check_if_system_state_would_be_changed())

# include magic from lib/ansible/module_common.py
#<<INCLUDE_ANSIBLE_MODULE_COMMON>>
main()

