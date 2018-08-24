"""
This custom resolver will resolve public subnets in the first VPC.
"""
from sceptre.resolvers import Resolver


class FirstVpcPublicNets(Resolver):
    """
    Implementing class for this resolver.
    """

    def resolve(self):
        """
        Find public subnets of first VPC
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
        public_networks = []

        for net in response['Subnets']:
            if net['VpcId'] == vpc and net['MapPublicIpOnLaunch']:
                public_networks.append(net)

        return ', '.join(public_networks)
