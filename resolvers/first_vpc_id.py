"""
This custom resolver will resolve the VPC ID of the first VPC.
"""
from sceptre.resolvers import Resolver


class FirstVpcId(Resolver):
    """
    Implementing class for this resolver.
    """

    def resolve(self):
        """
        Find Id of first VPC
        """
        response = self.connection_manager.call(
            'ec2',
            'describe_vpcs'
        )
        return response['Vpcs'][0]['VpcId']
