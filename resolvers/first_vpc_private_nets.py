"""
This custom resolver will resolve private subnets in the first VPC.
"""
from sceptre.resolvers import Resolver


class FirstVpcPrivateNets(Resolver):
    """
    Implementing class for this resolver.
    """

    def resolve(self):
        """
        Find private subnets of first VPC
        """
        response = self.connection_manager.call(
            'ec2',
            'describe_vpcs'
        )
        vpc = response['Vpcs'][0]['VpcId']
        response = self.connection_manager.call(
            'ec2',
            'describe_subnets'
        )
        private_networks = []

        for net in response['Subnets']:
            if net['VpcId'] == vpc and not net['MapPublicIpOnLaunch']:
                private_networks.append(net["SubnetId"])

        return ','.join(private_networks)
