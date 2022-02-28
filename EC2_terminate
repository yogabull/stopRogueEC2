import boto3

aws_regions = [
    'us-east-1',
    'us-east-2',
    'us-west-1',
    'us-west-2',]
 
def lambda_handler(event, context):
    for region in aws_regions: # Get instances in each region.
        ec2_client = boto3.client('ec2', region_name=region)
        response = ec2_client.describe_instances()
        ec2_instances = response['Reservations']
        
        ec2_list =[]
        for instance in ec2_instances: # Get EC2 id list.
            ec2_list.append(instance['Instances'][0]['InstanceId'])
           
        print(f"{region}: ", ec2_list)
        
        
        
        
        
#       for ec2 in ec2_list:
#           print(f"Terminating:", ec2)
#           terminate_instance(ec2, region)

# def terminate_instance(instance_id, region):
#     ec2_client = boto3.client("ec2", region_name="region")
#     response = ec2_client.terminate_instances(InstanceIds=instance_id)
#     print(response)
