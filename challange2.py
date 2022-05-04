import googleapiclient.discovery

compute = googleapiclient.discovery.build('compute', 'v1')

# Project Name where Resource has been created
project="sample-project"

# Zone where project is created
zone="us-central1a"

# Instance name 
instance_name="myvm"

# This will be metadata dictory
vm_metadata = compute.instances().get(project=project, zone=zone, instance=instance_name).execute()
print(vm_metadata)
    
    
# To reterive particular key eg: "id"

for key, value in vm_metadata.items():
    if key == 'id':
        print(value)