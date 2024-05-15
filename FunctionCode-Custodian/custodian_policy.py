# from c7n import handler

# def run(event, context):
#     return handler.dispatch_event(event, context)

from c7n import handler
import os

def run(event, context):
    lambda_directory = os.path.dirname(os.path.abspath(__file__))
    print(lambda_directory)
    for file in os.listdir(lambda_directory):
        if file.endswith('s3_unused.json') and file != 'terminate-stopped-ec2.json' and file != 'stop-dev-ec2-offhours.json':  # Exclude config.json or any other files
            with open(os.path.join(lambda_directory, file), 'r') as f:
                # policy = json.load(f)
                # Call your Lambda execution function here, passing the policy
                print(file)
                return handler.dispatch_event(event, context, file)
