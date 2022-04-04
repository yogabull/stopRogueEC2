import boto3

def lambda_handler(event, context):
    ec2_client = boto3.client('ec2')
    
    # Add regions to check.
    regions = ec2_client.describe_regions()['Regions']
    aws_regions = []
    for region in regions:
        aws_regions.append(region['RegionName'])

    # Loop through ec2_clients in each region.
    for region in aws_regions: 
        ec2_client = boto3.client('ec2', region_name=region)
        response = ec2_client.describe_instances()
        
        # Get a EC2 id lists.
        ec2_instances = response['Reservations'] 
        ec2_list =[]
        for instance in ec2_instances:
            ec2_list.append(instance['Instances'][0]['InstanceId'])
            
        # Stop instances in list.
        for ec2 in ec2_list:
            print(f"{region} Stopping: ", ec2)
            stop_instance(ec2, region, ec2_client)

def stop_instance(instance_id, region, ec2_client):
    response = ec2_client.stop_instances(InstanceIds=[instance_id])