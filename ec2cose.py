import boto3

def get_ec2_instances():
    # Create an EC2 client
    ec2_client = boto3.client('ec2')
    
    # Describe instances
    response = ec2_client.describe_instances()
    
    instance_list = []
    
    # Iterate through reservations and instances
    for reservation in response['Reservations']:
        for instance in reservation['Instances']:
            instance_id = instance['InstanceId']
            instance_type = instance['InstanceType']
            
            # Get public IP if available, otherwise use private IP
            ip_address = instance.get('PublicIpAddress', instance.get('PrivateIpAddress', 'N/A'))
            
            instance_info = {
                'InstanceId': instance_id,
                'InstanceType': instance_type,
                'IPAddress': ip_address
            }
            
            instance_list.append(instance_info)
    
    return instance_list

# Call the function and print the results
instances = get_ec2_instances()

for instance in instances:
    print(f"Instance ID: {instance['InstanceId']}")
    print(f"Instance Type: {instance['InstanceType']}")
    print(f"IP Address: {instance['IPAddress']}")
    print("---")
