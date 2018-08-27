"""
This custom resolver will resolve the ACM certificate ARN of a domain name.
"""
from sceptre.resolvers import Resolver


class CertificateArn(Resolver):
    """
    Implementing class for this resolver.
    """

    def resolve(self):
        """
        Find certificate ARN for domain name
        """
        response = self.connection_manager.call(
            'acm',
            'list_certificates'
        )
        for cert in response['CertificateSummaryList']:
            if cert['DomainName'] == self.argument:
                return cert['CertificateArn']

        return "not found"
