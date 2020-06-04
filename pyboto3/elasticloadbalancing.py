'''

The MIT License (MIT)

Copyright (c) 2016 WavyCloud

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

'''

def add_tags(LoadBalancerNames=None, Tags=None):
    """
    Adds the specified tags to the specified load balancer. Each load balancer can have a maximum of 10 tags.
    Each tag consists of a key and an optional value. If a tag with the same key is already associated with the load balancer, AddTags updates its value.
    For more information, see Tag Your Classic Load Balancer in the Classic Load Balancers Guide .
    See also: AWS API Documentation
    
    Exceptions
    Examples
    This example adds two tags to the specified load balancer.
    Expected Output:
    
    :example: response = client.add_tags(
        LoadBalancerNames=[
            'string',
        ],
        Tags=[
            {
                'Key': 'string',
                'Value': 'string'
            },
        ]
    )
    
    
    :type LoadBalancerNames: list
    :param LoadBalancerNames: [REQUIRED]\nThe name of the load balancer. You can specify one load balancer only.\n\n(string) --\n\n

    :type Tags: list
    :param Tags: [REQUIRED]\nThe tags.\n\n(dict) --Information about a tag.\n\nKey (string) -- [REQUIRED]The key of the tag.\n\nValue (string) --The value of the tag.\n\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{}


Response Structure

(dict) --
Contains the output of AddTags.





Exceptions

ElasticLoadBalancing.Client.exceptions.AccessPointNotFoundException
ElasticLoadBalancing.Client.exceptions.TooManyTagsException
ElasticLoadBalancing.Client.exceptions.DuplicateTagKeysException

Examples
This example adds two tags to the specified load balancer.
response = client.add_tags(
    LoadBalancerNames=[
        'my-load-balancer',
    ],
    Tags=[
        {
            'Key': 'project',
            'Value': 'lima',
        },
        {
            'Key': 'department',
            'Value': 'digital-media',
        },
    ],
)

print(response)


Expected Output:
{
    'ResponseMetadata': {
        '...': '...',
    },
}



    :return: {}
    
    
    :returns: 
    ElasticLoadBalancing.Client.exceptions.AccessPointNotFoundException
    ElasticLoadBalancing.Client.exceptions.TooManyTagsException
    ElasticLoadBalancing.Client.exceptions.DuplicateTagKeysException
    
    """
    pass

def apply_security_groups_to_load_balancer(LoadBalancerName=None, SecurityGroups=None):
    """
    Associates one or more security groups with your load balancer in a virtual private cloud (VPC). The specified security groups override the previously associated security groups.
    For more information, see Security Groups for Load Balancers in a VPC in the Classic Load Balancers Guide .
    See also: AWS API Documentation
    
    Exceptions
    Examples
    This example associates a security group with the specified load balancer in a VPC.
    Expected Output:
    
    :example: response = client.apply_security_groups_to_load_balancer(
        LoadBalancerName='string',
        SecurityGroups=[
            'string',
        ]
    )
    
    
    :type LoadBalancerName: string
    :param LoadBalancerName: [REQUIRED]\nThe name of the load balancer.\n

    :type SecurityGroups: list
    :param SecurityGroups: [REQUIRED]\nThe IDs of the security groups to associate with the load balancer. Note that you cannot specify the name of the security group.\n\n(string) --\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'SecurityGroups': [
        'string',
    ]
}


Response Structure

(dict) --
Contains the output of ApplySecurityGroupsToLoadBalancer.

SecurityGroups (list) --
The IDs of the security groups associated with the load balancer.

(string) --








Exceptions

ElasticLoadBalancing.Client.exceptions.AccessPointNotFoundException
ElasticLoadBalancing.Client.exceptions.InvalidConfigurationRequestException
ElasticLoadBalancing.Client.exceptions.InvalidSecurityGroupException

Examples
This example associates a security group with the specified load balancer in a VPC.
response = client.apply_security_groups_to_load_balancer(
    LoadBalancerName='my-load-balancer',
    SecurityGroups=[
        'sg-fc448899',
    ],
)

print(response)


Expected Output:
{
    'SecurityGroups': [
        'sg-fc448899',
    ],
    'ResponseMetadata': {
        '...': '...',
    },
}



    :return: {
        'SecurityGroups': [
            'string',
        ]
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def attach_load_balancer_to_subnets(LoadBalancerName=None, Subnets=None):
    """
    Adds one or more subnets to the set of configured subnets for the specified load balancer.
    The load balancer evenly distributes requests across all registered subnets. For more information, see Add or Remove Subnets for Your Load Balancer in a VPC in the Classic Load Balancers Guide .
    See also: AWS API Documentation
    
    Exceptions
    Examples
    This example adds the specified subnet to the set of configured subnets for the specified load balancer.
    Expected Output:
    
    :example: response = client.attach_load_balancer_to_subnets(
        LoadBalancerName='string',
        Subnets=[
            'string',
        ]
    )
    
    
    :type LoadBalancerName: string
    :param LoadBalancerName: [REQUIRED]\nThe name of the load balancer.\n

    :type Subnets: list
    :param Subnets: [REQUIRED]\nThe IDs of the subnets to add. You can add only one subnet per Availability Zone.\n\n(string) --\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'Subnets': [
        'string',
    ]
}


Response Structure

(dict) --
Contains the output of AttachLoadBalancerToSubnets.

Subnets (list) --
The IDs of the subnets attached to the load balancer.

(string) --








Exceptions

ElasticLoadBalancing.Client.exceptions.AccessPointNotFoundException
ElasticLoadBalancing.Client.exceptions.InvalidConfigurationRequestException
ElasticLoadBalancing.Client.exceptions.SubnetNotFoundException
ElasticLoadBalancing.Client.exceptions.InvalidSubnetException

Examples
This example adds the specified subnet to the set of configured subnets for the specified load balancer.
response = client.attach_load_balancer_to_subnets(
    LoadBalancerName='my-load-balancer',
    Subnets=[
        'subnet-0ecac448',
    ],
)

print(response)


Expected Output:
{
    'Subnets': [
        'subnet-15aaab61',
        'subnet-0ecac448',
    ],
    'ResponseMetadata': {
        '...': '...',
    },
}



    :return: {
        'Subnets': [
            'string',
        ]
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def can_paginate(operation_name=None):
    """
    Check if an operation can be paginated.
    
    :type operation_name: string
    :param operation_name: The operation name. This is the same name\nas the method name on the client. For example, if the\nmethod name is create_foo, and you\'d normally invoke the\noperation as client.create_foo(**kwargs), if the\ncreate_foo operation can be paginated, you can use the\ncall client.get_paginator('create_foo').

    """
    pass

def configure_health_check(LoadBalancerName=None, HealthCheck=None):
    """
    Specifies the health check settings to use when evaluating the health state of your EC2 instances.
    For more information, see Configure Health Checks for Your Load Balancer in the Classic Load Balancers Guide .
    See also: AWS API Documentation
    
    Exceptions
    Examples
    This example specifies the health check settings used to evaluate the health of your backend EC2 instances.
    Expected Output:
    
    :example: response = client.configure_health_check(
        LoadBalancerName='string',
        HealthCheck={
            'Target': 'string',
            'Interval': 123,
            'Timeout': 123,
            'UnhealthyThreshold': 123,
            'HealthyThreshold': 123
        }
    )
    
    
    :type LoadBalancerName: string
    :param LoadBalancerName: [REQUIRED]\nThe name of the load balancer.\n

    :type HealthCheck: dict
    :param HealthCheck: [REQUIRED]\nThe configuration information.\n\nTarget (string) -- [REQUIRED]The instance being checked. The protocol is either TCP, HTTP, HTTPS, or SSL. The range of valid ports is one (1) through 65535.\nTCP is the default, specified as a TCP: port pair, for example 'TCP:5000'. In this case, a health check simply attempts to open a TCP connection to the instance on the specified port. Failure to connect within the configured timeout is considered unhealthy.\nSSL is also specified as SSL: port pair, for example, SSL:5000.\nFor HTTP/HTTPS, you must include a ping path in the string. HTTP is specified as a HTTP:port;/;PathToPing; grouping, for example 'HTTP:80/weather/us/wa/seattle'. In this case, a HTTP GET request is issued to the instance on the given port and path. Any answer other than '200 OK' within the timeout period is considered unhealthy.\nThe total length of the HTTP ping target must be 1024 16-bit Unicode characters or less.\n\nInterval (integer) -- [REQUIRED]The approximate interval, in seconds, between health checks of an individual instance.\n\nTimeout (integer) -- [REQUIRED]The amount of time, in seconds, during which no response means a failed health check.\nThis value must be less than the Interval value.\n\nUnhealthyThreshold (integer) -- [REQUIRED]The number of consecutive health check failures required before moving the instance to the Unhealthy state.\n\nHealthyThreshold (integer) -- [REQUIRED]The number of consecutive health checks successes required before moving the instance to the Healthy state.\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'HealthCheck': {
        'Target': 'string',
        'Interval': 123,
        'Timeout': 123,
        'UnhealthyThreshold': 123,
        'HealthyThreshold': 123
    }
}


Response Structure

(dict) --
Contains the output of ConfigureHealthCheck.

HealthCheck (dict) --
The updated health check.

Target (string) --
The instance being checked. The protocol is either TCP, HTTP, HTTPS, or SSL. The range of valid ports is one (1) through 65535.
TCP is the default, specified as a TCP: port pair, for example "TCP:5000". In this case, a health check simply attempts to open a TCP connection to the instance on the specified port. Failure to connect within the configured timeout is considered unhealthy.
SSL is also specified as SSL: port pair, for example, SSL:5000.
For HTTP/HTTPS, you must include a ping path in the string. HTTP is specified as a HTTP:port;/;PathToPing; grouping, for example "HTTP:80/weather/us/wa/seattle". In this case, a HTTP GET request is issued to the instance on the given port and path. Any answer other than "200 OK" within the timeout period is considered unhealthy.
The total length of the HTTP ping target must be 1024 16-bit Unicode characters or less.

Interval (integer) --
The approximate interval, in seconds, between health checks of an individual instance.

Timeout (integer) --
The amount of time, in seconds, during which no response means a failed health check.
This value must be less than the Interval value.

UnhealthyThreshold (integer) --
The number of consecutive health check failures required before moving the instance to the Unhealthy state.

HealthyThreshold (integer) --
The number of consecutive health checks successes required before moving the instance to the Healthy state.









Exceptions

ElasticLoadBalancing.Client.exceptions.AccessPointNotFoundException

Examples
This example specifies the health check settings used to evaluate the health of your backend EC2 instances.
response = client.configure_health_check(
    HealthCheck={
        'HealthyThreshold': 2,
        'Interval': 30,
        'Target': 'HTTP:80/png',
        'Timeout': 3,
        'UnhealthyThreshold': 2,
    },
    LoadBalancerName='my-load-balancer',
)

print(response)


Expected Output:
{
    'HealthCheck': {
        'HealthyThreshold': 2,
        'Interval': 30,
        'Target': 'HTTP:80/png',
        'Timeout': 3,
        'UnhealthyThreshold': 2,
    },
    'ResponseMetadata': {
        '...': '...',
    },
}



    :return: {
        'HealthCheck': {
            'Target': 'string',
            'Interval': 123,
            'Timeout': 123,
            'UnhealthyThreshold': 123,
            'HealthyThreshold': 123
        }
    }
    
    
    :returns: 
    ElasticLoadBalancing.Client.exceptions.AccessPointNotFoundException
    
    """
    pass

def create_app_cookie_stickiness_policy(LoadBalancerName=None, PolicyName=None, CookieName=None):
    """
    Generates a stickiness policy with sticky session lifetimes that follow that of an application-generated cookie. This policy can be associated only with HTTP/HTTPS listeners.
    This policy is similar to the policy created by  CreateLBCookieStickinessPolicy , except that the lifetime of the special Elastic Load Balancing cookie, AWSELB , follows the lifetime of the application-generated cookie specified in the policy configuration. The load balancer only inserts a new stickiness cookie when the application response includes a new application cookie.
    If the application cookie is explicitly removed or expires, the session stops being sticky until a new application cookie is issued.
    For more information, see Application-Controlled Session Stickiness in the Classic Load Balancers Guide .
    See also: AWS API Documentation
    
    Exceptions
    Examples
    This example generates a stickiness policy that follows the sticky session lifetimes of the application-generated cookie.
    Expected Output:
    
    :example: response = client.create_app_cookie_stickiness_policy(
        LoadBalancerName='string',
        PolicyName='string',
        CookieName='string'
    )
    
    
    :type LoadBalancerName: string
    :param LoadBalancerName: [REQUIRED]\nThe name of the load balancer.\n

    :type PolicyName: string
    :param PolicyName: [REQUIRED]\nThe name of the policy being created. Policy names must consist of alphanumeric characters and dashes (-). This name must be unique within the set of policies for this load balancer.\n

    :type CookieName: string
    :param CookieName: [REQUIRED]\nThe name of the application cookie used for stickiness.\n

    :rtype: dict

ReturnsResponse Syntax
{}


Response Structure

(dict) --
Contains the output for CreateAppCookieStickinessPolicy.





Exceptions

ElasticLoadBalancing.Client.exceptions.AccessPointNotFoundException
ElasticLoadBalancing.Client.exceptions.DuplicatePolicyNameException
ElasticLoadBalancing.Client.exceptions.TooManyPoliciesException
ElasticLoadBalancing.Client.exceptions.InvalidConfigurationRequestException

Examples
This example generates a stickiness policy that follows the sticky session lifetimes of the application-generated cookie.
response = client.create_app_cookie_stickiness_policy(
    CookieName='my-app-cookie',
    LoadBalancerName='my-load-balancer',
    PolicyName='my-app-cookie-policy',
)

print(response)


Expected Output:
{
    'ResponseMetadata': {
        '...': '...',
    },
}



    :return: {}
    
    
    :returns: 
    ElasticLoadBalancing.Client.exceptions.AccessPointNotFoundException
    ElasticLoadBalancing.Client.exceptions.DuplicatePolicyNameException
    ElasticLoadBalancing.Client.exceptions.TooManyPoliciesException
    ElasticLoadBalancing.Client.exceptions.InvalidConfigurationRequestException
    
    """
    pass

def create_lb_cookie_stickiness_policy(LoadBalancerName=None, PolicyName=None, CookieExpirationPeriod=None):
    """
    Generates a stickiness policy with sticky session lifetimes controlled by the lifetime of the browser (user-agent) or a specified expiration period. This policy can be associated only with HTTP/HTTPS listeners.
    When a load balancer implements this policy, the load balancer uses a special cookie to track the instance for each request. When the load balancer receives a request, it first checks to see if this cookie is present in the request. If so, the load balancer sends the request to the application server specified in the cookie. If not, the load balancer sends the request to a server that is chosen based on the existing load-balancing algorithm.
    A cookie is inserted into the response for binding subsequent requests from the same user to that server. The validity of the cookie is based on the cookie expiration time, which is specified in the policy configuration.
    For more information, see Duration-Based Session Stickiness in the Classic Load Balancers Guide .
    See also: AWS API Documentation
    
    Exceptions
    Examples
    This example generates a stickiness policy with sticky session lifetimes controlled by the specified expiration period.
    Expected Output:
    
    :example: response = client.create_lb_cookie_stickiness_policy(
        LoadBalancerName='string',
        PolicyName='string',
        CookieExpirationPeriod=123
    )
    
    
    :type LoadBalancerName: string
    :param LoadBalancerName: [REQUIRED]\nThe name of the load balancer.\n

    :type PolicyName: string
    :param PolicyName: [REQUIRED]\nThe name of the policy being created. Policy names must consist of alphanumeric characters and dashes (-). This name must be unique within the set of policies for this load balancer.\n

    :type CookieExpirationPeriod: integer
    :param CookieExpirationPeriod: The time period, in seconds, after which the cookie should be considered stale. If you do not specify this parameter, the default value is 0, which indicates that the sticky session should last for the duration of the browser session.

    :rtype: dict

ReturnsResponse Syntax
{}


Response Structure

(dict) --
Contains the output for CreateLBCookieStickinessPolicy.





Exceptions

ElasticLoadBalancing.Client.exceptions.AccessPointNotFoundException
ElasticLoadBalancing.Client.exceptions.DuplicatePolicyNameException
ElasticLoadBalancing.Client.exceptions.TooManyPoliciesException
ElasticLoadBalancing.Client.exceptions.InvalidConfigurationRequestException

Examples
This example generates a stickiness policy with sticky session lifetimes controlled by the specified expiration period.
response = client.create_lb_cookie_stickiness_policy(
    CookieExpirationPeriod=60,
    LoadBalancerName='my-load-balancer',
    PolicyName='my-duration-cookie-policy',
)

print(response)


Expected Output:
{
    'ResponseMetadata': {
        '...': '...',
    },
}



    :return: {}
    
    
    :returns: 
    ElasticLoadBalancing.Client.exceptions.AccessPointNotFoundException
    ElasticLoadBalancing.Client.exceptions.DuplicatePolicyNameException
    ElasticLoadBalancing.Client.exceptions.TooManyPoliciesException
    ElasticLoadBalancing.Client.exceptions.InvalidConfigurationRequestException
    
    """
    pass

def create_load_balancer(LoadBalancerName=None, Listeners=None, AvailabilityZones=None, Subnets=None, SecurityGroups=None, Scheme=None, Tags=None):
    """
    Creates a Classic Load Balancer.
    You can add listeners, security groups, subnets, and tags when you create your load balancer, or you can add them later using  CreateLoadBalancerListeners ,  ApplySecurityGroupsToLoadBalancer ,  AttachLoadBalancerToSubnets , and  AddTags .
    To describe your current load balancers, see  DescribeLoadBalancers . When you are finished with a load balancer, you can delete it using  DeleteLoadBalancer .
    You can create up to 20 load balancers per region per account. You can request an increase for the number of load balancers for your account. For more information, see Limits for Your Classic Load Balancer in the Classic Load Balancers Guide .
    See also: AWS API Documentation
    
    Exceptions
    Examples
    This example creates a load balancer with an HTTP listener in a VPC.
    Expected Output:
    This example creates a load balancer with an HTTP listener in EC2-Classic.
    Expected Output:
    This example creates a load balancer with an HTTPS listener in a VPC.
    Expected Output:
    This example creates a load balancer with an HTTPS listener in EC2-Classic.
    Expected Output:
    This example creates an internal load balancer with an HTTP listener in a VPC.
    Expected Output:
    
    :example: response = client.create_load_balancer(
        LoadBalancerName='string',
        Listeners=[
            {
                'Protocol': 'string',
                'LoadBalancerPort': 123,
                'InstanceProtocol': 'string',
                'InstancePort': 123,
                'SSLCertificateId': 'string'
            },
        ],
        AvailabilityZones=[
            'string',
        ],
        Subnets=[
            'string',
        ],
        SecurityGroups=[
            'string',
        ],
        Scheme='string',
        Tags=[
            {
                'Key': 'string',
                'Value': 'string'
            },
        ]
    )
    
    
    :type LoadBalancerName: string
    :param LoadBalancerName: [REQUIRED]\nThe name of the load balancer.\nThis name must be unique within your set of load balancers for the region, must have a maximum of 32 characters, must contain only alphanumeric characters or hyphens, and cannot begin or end with a hyphen.\n

    :type Listeners: list
    :param Listeners: [REQUIRED]\nThe listeners.\nFor more information, see Listeners for Your Classic Load Balancer in the Classic Load Balancers Guide .\n\n(dict) --Information about a listener.\nFor information about the protocols and the ports supported by Elastic Load Balancing, see Listeners for Your Classic Load Balancer in the Classic Load Balancers Guide .\n\nProtocol (string) -- [REQUIRED]The load balancer transport protocol to use for routing: HTTP, HTTPS, TCP, or SSL.\n\nLoadBalancerPort (integer) -- [REQUIRED]The port on which the load balancer is listening. On EC2-VPC, you can specify any port from the range 1-65535. On EC2-Classic, you can specify any port from the following list: 25, 80, 443, 465, 587, 1024-65535.\n\nInstanceProtocol (string) --The protocol to use for routing traffic to instances: HTTP, HTTPS, TCP, or SSL.\nIf the front-end protocol is HTTP, HTTPS, TCP, or SSL, InstanceProtocol must be at the same protocol.\nIf there is another listener with the same InstancePort whose InstanceProtocol is secure, (HTTPS or SSL), the listener\'s InstanceProtocol must also be secure.\nIf there is another listener with the same InstancePort whose InstanceProtocol is HTTP or TCP, the listener\'s InstanceProtocol must be HTTP or TCP.\n\nInstancePort (integer) -- [REQUIRED]The port on which the instance is listening.\n\nSSLCertificateId (string) --The Amazon Resource Name (ARN) of the server certificate.\n\n\n\n\n

    :type AvailabilityZones: list
    :param AvailabilityZones: One or more Availability Zones from the same region as the load balancer.\nYou must specify at least one Availability Zone.\nYou can add more Availability Zones after you create the load balancer using EnableAvailabilityZonesForLoadBalancer .\n\n(string) --\n\n

    :type Subnets: list
    :param Subnets: The IDs of the subnets in your VPC to attach to the load balancer. Specify one subnet per Availability Zone specified in AvailabilityZones .\n\n(string) --\n\n

    :type SecurityGroups: list
    :param SecurityGroups: The IDs of the security groups to assign to the load balancer.\n\n(string) --\n\n

    :type Scheme: string
    :param Scheme: The type of a load balancer. Valid only for load balancers in a VPC.\nBy default, Elastic Load Balancing creates an Internet-facing load balancer with a DNS name that resolves to public IP addresses. For more information about Internet-facing and Internal load balancers, see Load Balancer Scheme in the Elastic Load Balancing User Guide .\nSpecify internal to create a load balancer with a DNS name that resolves to private IP addresses.\n

    :type Tags: list
    :param Tags: A list of tags to assign to the load balancer.\nFor more information about tagging your load balancer, see Tag Your Classic Load Balancer in the Classic Load Balancers Guide .\n\n(dict) --Information about a tag.\n\nKey (string) -- [REQUIRED]The key of the tag.\n\nValue (string) --The value of the tag.\n\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'DNSName': 'string'
}


Response Structure

(dict) --
Contains the output for CreateLoadBalancer.

DNSName (string) --
The DNS name of the load balancer.







Exceptions

ElasticLoadBalancing.Client.exceptions.DuplicateAccessPointNameException
ElasticLoadBalancing.Client.exceptions.TooManyAccessPointsException
ElasticLoadBalancing.Client.exceptions.CertificateNotFoundException
ElasticLoadBalancing.Client.exceptions.InvalidConfigurationRequestException
ElasticLoadBalancing.Client.exceptions.SubnetNotFoundException
ElasticLoadBalancing.Client.exceptions.InvalidSubnetException
ElasticLoadBalancing.Client.exceptions.InvalidSecurityGroupException
ElasticLoadBalancing.Client.exceptions.InvalidSchemeException
ElasticLoadBalancing.Client.exceptions.TooManyTagsException
ElasticLoadBalancing.Client.exceptions.DuplicateTagKeysException
ElasticLoadBalancing.Client.exceptions.UnsupportedProtocolException
ElasticLoadBalancing.Client.exceptions.OperationNotPermittedException

Examples
This example creates a load balancer with an HTTP listener in a VPC.
response = client.create_load_balancer(
    Listeners=[
        {
            'InstancePort': 80,
            'InstanceProtocol': 'HTTP',
            'LoadBalancerPort': 80,
            'Protocol': 'HTTP',
        },
    ],
    LoadBalancerName='my-load-balancer',
    SecurityGroups=[
        'sg-a61988c3',
    ],
    Subnets=[
        'subnet-15aaab61',
    ],
)

print(response)


Expected Output:
{
    'DNSName': 'my-load-balancer-1234567890.us-west-2.elb.amazonaws.com',
    'ResponseMetadata': {
        '...': '...',
    },
}


This example creates a load balancer with an HTTP listener in EC2-Classic.
response = client.create_load_balancer(
    AvailabilityZones=[
        'us-west-2a',
    ],
    Listeners=[
        {
            'InstancePort': 80,
            'InstanceProtocol': 'HTTP',
            'LoadBalancerPort': 80,
            'Protocol': 'HTTP',
        },
    ],
    LoadBalancerName='my-load-balancer',
)

print(response)


Expected Output:
{
    'DNSName': 'my-load-balancer-123456789.us-west-2.elb.amazonaws.com',
    'ResponseMetadata': {
        '...': '...',
    },
}


This example creates a load balancer with an HTTPS listener in a VPC.
response = client.create_load_balancer(
    Listeners=[
        {
            'InstancePort': 80,
            'InstanceProtocol': 'HTTP',
            'LoadBalancerPort': 80,
            'Protocol': 'HTTP',
        },
        {
            'InstancePort': 80,
            'InstanceProtocol': 'HTTP',
            'LoadBalancerPort': 443,
            'Protocol': 'HTTPS',
            'SSLCertificateId': 'arn:aws:iam::123456789012:server-certificate/my-server-cert',
        },
    ],
    LoadBalancerName='my-load-balancer',
    SecurityGroups=[
        'sg-a61988c3',
    ],
    Subnets=[
        'subnet-15aaab61',
    ],
)

print(response)


Expected Output:
{
    'DNSName': 'my-load-balancer-1234567890.us-west-2.elb.amazonaws.com',
    'ResponseMetadata': {
        '...': '...',
    },
}


This example creates a load balancer with an HTTPS listener in EC2-Classic.
response = client.create_load_balancer(
    AvailabilityZones=[
        'us-west-2a',
    ],
    Listeners=[
        {
            'InstancePort': 80,
            'InstanceProtocol': 'HTTP',
            'LoadBalancerPort': 80,
            'Protocol': 'HTTP',
        },
        {
            'InstancePort': 80,
            'InstanceProtocol': 'HTTP',
            'LoadBalancerPort': 443,
            'Protocol': 'HTTPS',
            'SSLCertificateId': 'arn:aws:iam::123456789012:server-certificate/my-server-cert',
        },
    ],
    LoadBalancerName='my-load-balancer',
)

print(response)


Expected Output:
{
    'DNSName': 'my-load-balancer-123456789.us-west-2.elb.amazonaws.com',
    'ResponseMetadata': {
        '...': '...',
    },
}


This example creates an internal load balancer with an HTTP listener in a VPC.
response = client.create_load_balancer(
    Listeners=[
        {
            'InstancePort': 80,
            'InstanceProtocol': 'HTTP',
            'LoadBalancerPort': 80,
            'Protocol': 'HTTP',
        },
    ],
    LoadBalancerName='my-load-balancer',
    Scheme='internal',
    SecurityGroups=[
        'sg-a61988c3',
    ],
    Subnets=[
        'subnet-15aaab61',
    ],
)

print(response)


Expected Output:
{
    'DNSName': 'internal-my-load-balancer-123456789.us-west-2.elb.amazonaws.com',
    'ResponseMetadata': {
        '...': '...',
    },
}



    :return: {
        'DNSName': 'string'
    }
    
    
    :returns: 
    ElasticLoadBalancing.Client.exceptions.DuplicateAccessPointNameException
    ElasticLoadBalancing.Client.exceptions.TooManyAccessPointsException
    ElasticLoadBalancing.Client.exceptions.CertificateNotFoundException
    ElasticLoadBalancing.Client.exceptions.InvalidConfigurationRequestException
    ElasticLoadBalancing.Client.exceptions.SubnetNotFoundException
    ElasticLoadBalancing.Client.exceptions.InvalidSubnetException
    ElasticLoadBalancing.Client.exceptions.InvalidSecurityGroupException
    ElasticLoadBalancing.Client.exceptions.InvalidSchemeException
    ElasticLoadBalancing.Client.exceptions.TooManyTagsException
    ElasticLoadBalancing.Client.exceptions.DuplicateTagKeysException
    ElasticLoadBalancing.Client.exceptions.UnsupportedProtocolException
    ElasticLoadBalancing.Client.exceptions.OperationNotPermittedException
    
    """
    pass

def create_load_balancer_listeners(LoadBalancerName=None, Listeners=None):
    """
    Creates one or more listeners for the specified load balancer. If a listener with the specified port does not already exist, it is created; otherwise, the properties of the new listener must match the properties of the existing listener.
    For more information, see Listeners for Your Classic Load Balancer in the Classic Load Balancers Guide .
    See also: AWS API Documentation
    
    Exceptions
    Examples
    This example creates a listener for your load balancer at port 80 using the HTTP protocol.
    Expected Output:
    This example creates a listener for your load balancer at port 443 using the HTTPS protocol.
    Expected Output:
    
    :example: response = client.create_load_balancer_listeners(
        LoadBalancerName='string',
        Listeners=[
            {
                'Protocol': 'string',
                'LoadBalancerPort': 123,
                'InstanceProtocol': 'string',
                'InstancePort': 123,
                'SSLCertificateId': 'string'
            },
        ]
    )
    
    
    :type LoadBalancerName: string
    :param LoadBalancerName: [REQUIRED]\nThe name of the load balancer.\n

    :type Listeners: list
    :param Listeners: [REQUIRED]\nThe listeners.\n\n(dict) --Information about a listener.\nFor information about the protocols and the ports supported by Elastic Load Balancing, see Listeners for Your Classic Load Balancer in the Classic Load Balancers Guide .\n\nProtocol (string) -- [REQUIRED]The load balancer transport protocol to use for routing: HTTP, HTTPS, TCP, or SSL.\n\nLoadBalancerPort (integer) -- [REQUIRED]The port on which the load balancer is listening. On EC2-VPC, you can specify any port from the range 1-65535. On EC2-Classic, you can specify any port from the following list: 25, 80, 443, 465, 587, 1024-65535.\n\nInstanceProtocol (string) --The protocol to use for routing traffic to instances: HTTP, HTTPS, TCP, or SSL.\nIf the front-end protocol is HTTP, HTTPS, TCP, or SSL, InstanceProtocol must be at the same protocol.\nIf there is another listener with the same InstancePort whose InstanceProtocol is secure, (HTTPS or SSL), the listener\'s InstanceProtocol must also be secure.\nIf there is another listener with the same InstancePort whose InstanceProtocol is HTTP or TCP, the listener\'s InstanceProtocol must be HTTP or TCP.\n\nInstancePort (integer) -- [REQUIRED]The port on which the instance is listening.\n\nSSLCertificateId (string) --The Amazon Resource Name (ARN) of the server certificate.\n\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{}


Response Structure

(dict) --
Contains the parameters for CreateLoadBalancerListener.





Exceptions

ElasticLoadBalancing.Client.exceptions.AccessPointNotFoundException
ElasticLoadBalancing.Client.exceptions.DuplicateListenerException
ElasticLoadBalancing.Client.exceptions.CertificateNotFoundException
ElasticLoadBalancing.Client.exceptions.InvalidConfigurationRequestException
ElasticLoadBalancing.Client.exceptions.UnsupportedProtocolException

Examples
This example creates a listener for your load balancer at port 80 using the HTTP protocol.
response = client.create_load_balancer_listeners(
    Listeners=[
        {
            'InstancePort': 80,
            'InstanceProtocol': 'HTTP',
            'LoadBalancerPort': 80,
            'Protocol': 'HTTP',
        },
    ],
    LoadBalancerName='my-load-balancer',
)

print(response)


Expected Output:
{
    'ResponseMetadata': {
        '...': '...',
    },
}


This example creates a listener for your load balancer at port 443 using the HTTPS protocol.
response = client.create_load_balancer_listeners(
    Listeners=[
        {
            'InstancePort': 80,
            'InstanceProtocol': 'HTTP',
            'LoadBalancerPort': 443,
            'Protocol': 'HTTPS',
            'SSLCertificateId': 'arn:aws:iam::123456789012:server-certificate/my-server-cert',
        },
    ],
    LoadBalancerName='my-load-balancer',
)

print(response)


Expected Output:
{
    'ResponseMetadata': {
        '...': '...',
    },
}



    :return: {}
    
    
    :returns: 
    ElasticLoadBalancing.Client.exceptions.AccessPointNotFoundException
    ElasticLoadBalancing.Client.exceptions.DuplicateListenerException
    ElasticLoadBalancing.Client.exceptions.CertificateNotFoundException
    ElasticLoadBalancing.Client.exceptions.InvalidConfigurationRequestException
    ElasticLoadBalancing.Client.exceptions.UnsupportedProtocolException
    
    """
    pass

def create_load_balancer_policy(LoadBalancerName=None, PolicyName=None, PolicyTypeName=None, PolicyAttributes=None):
    """
    Creates a policy with the specified attributes for the specified load balancer.
    Policies are settings that are saved for your load balancer and that can be applied to the listener or the application server, depending on the policy type.
    See also: AWS API Documentation
    
    Exceptions
    Examples
    This example creates a policy that enables Proxy Protocol on the specified load balancer.
    Expected Output:
    This example creates a public key policy.
    Expected Output:
    This example creates a backend server authentication policy that enables authentication on your backend instance using a public key policy.
    Expected Output:
    
    :example: response = client.create_load_balancer_policy(
        LoadBalancerName='string',
        PolicyName='string',
        PolicyTypeName='string',
        PolicyAttributes=[
            {
                'AttributeName': 'string',
                'AttributeValue': 'string'
            },
        ]
    )
    
    
    :type LoadBalancerName: string
    :param LoadBalancerName: [REQUIRED]\nThe name of the load balancer.\n

    :type PolicyName: string
    :param PolicyName: [REQUIRED]\nThe name of the load balancer policy to be created. This name must be unique within the set of policies for this load balancer.\n

    :type PolicyTypeName: string
    :param PolicyTypeName: [REQUIRED]\nThe name of the base policy type. To get the list of policy types, use DescribeLoadBalancerPolicyTypes .\n

    :type PolicyAttributes: list
    :param PolicyAttributes: The policy attributes.\n\n(dict) --Information about a policy attribute.\n\nAttributeName (string) --The name of the attribute.\n\nAttributeValue (string) --The value of the attribute.\n\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{}


Response Structure

(dict) --
Contains the output of CreateLoadBalancerPolicy.





Exceptions

ElasticLoadBalancing.Client.exceptions.AccessPointNotFoundException
ElasticLoadBalancing.Client.exceptions.PolicyTypeNotFoundException
ElasticLoadBalancing.Client.exceptions.DuplicatePolicyNameException
ElasticLoadBalancing.Client.exceptions.TooManyPoliciesException
ElasticLoadBalancing.Client.exceptions.InvalidConfigurationRequestException

Examples
This example creates a policy that enables Proxy Protocol on the specified load balancer.
response = client.create_load_balancer_policy(
    LoadBalancerName='my-load-balancer',
    PolicyAttributes=[
        {
            'AttributeName': 'ProxyProtocol',
            'AttributeValue': 'true',
        },
    ],
    PolicyName='my-ProxyProtocol-policy',
    PolicyTypeName='ProxyProtocolPolicyType',
)

print(response)


Expected Output:
{
    'ResponseMetadata': {
        '...': '...',
    },
}


This example creates a public key policy.
response = client.create_load_balancer_policy(
    LoadBalancerName='my-load-balancer',
    PolicyAttributes=[
        {
            'AttributeName': 'PublicKey',
            'AttributeValue': 'MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAwAYUjnfyEyXr1pxjhFWBpMlggUcqoi3kl+dS74kj//c6x7ROtusUaeQCTgIUkayttRDWchuqo1pHC1u+n5xxXnBBe2ejbb2WRsKIQ5rXEeixsjFpFsojpSQKkzhVGI6mJVZBJDVKSHmswnwLBdofLhzvllpovBPTHe+o4haAWvDBALJU0pkSI1FecPHcs2hwxf14zHoXy1e2k36A64nXW43wtfx5qcVSIxtCEOjnYRg7RPvybaGfQ+v6Iaxb/+7J5kEvZhTFQId+bSiJImF1FSUT1W1xwzBZPUbcUkkXDj45vC2s3Z8E+Lk7a3uZhvsQHLZnrfuWjBWGWvZ/MhZYgEXAMPLE',
        },
    ],
    PolicyName='my-PublicKey-policy',
    PolicyTypeName='PublicKeyPolicyType',
)

print(response)


Expected Output:
{
    'ResponseMetadata': {
        '...': '...',
    },
}


This example creates a backend server authentication policy that enables authentication on your backend instance using a public key policy.
response = client.create_load_balancer_policy(
    LoadBalancerName='my-load-balancer',
    PolicyAttributes=[
        {
            'AttributeName': 'PublicKeyPolicyName',
            'AttributeValue': 'my-PublicKey-policy',
        },
    ],
    PolicyName='my-authentication-policy',
    PolicyTypeName='BackendServerAuthenticationPolicyType',
)

print(response)


Expected Output:
{
    'ResponseMetadata': {
        '...': '...',
    },
}



    :return: {}
    
    
    :returns: 
    ElasticLoadBalancing.Client.exceptions.AccessPointNotFoundException
    ElasticLoadBalancing.Client.exceptions.PolicyTypeNotFoundException
    ElasticLoadBalancing.Client.exceptions.DuplicatePolicyNameException
    ElasticLoadBalancing.Client.exceptions.TooManyPoliciesException
    ElasticLoadBalancing.Client.exceptions.InvalidConfigurationRequestException
    
    """
    pass

def delete_load_balancer(LoadBalancerName=None):
    """
    Deletes the specified load balancer.
    If you are attempting to recreate a load balancer, you must reconfigure all settings. The DNS name associated with a deleted load balancer are no longer usable. The name and associated DNS record of the deleted load balancer no longer exist and traffic sent to any of its IP addresses is no longer delivered to your instances.
    If the load balancer does not exist or has already been deleted, the call to DeleteLoadBalancer still succeeds.
    See also: AWS API Documentation
    
    Examples
    This example deletes the specified load balancer.
    Expected Output:
    
    :example: response = client.delete_load_balancer(
        LoadBalancerName='string'
    )
    
    
    :type LoadBalancerName: string
    :param LoadBalancerName: [REQUIRED]\nThe name of the load balancer.\n

    :rtype: dict
ReturnsResponse Syntax{}


Response Structure

(dict) --Contains the output of DeleteLoadBalancer.




Examples
This example deletes the specified load balancer.
response = client.delete_load_balancer(
    LoadBalancerName='my-load-balancer',
)

print(response)


Expected Output:
{
    'ResponseMetadata': {
        '...': '...',
    },
}



    :return: {}
    
    
    """
    pass

def delete_load_balancer_listeners(LoadBalancerName=None, LoadBalancerPorts=None):
    """
    Deletes the specified listeners from the specified load balancer.
    See also: AWS API Documentation
    
    Exceptions
    Examples
    This example deletes the listener for the specified port from the specified load balancer.
    Expected Output:
    
    :example: response = client.delete_load_balancer_listeners(
        LoadBalancerName='string',
        LoadBalancerPorts=[
            123,
        ]
    )
    
    
    :type LoadBalancerName: string
    :param LoadBalancerName: [REQUIRED]\nThe name of the load balancer.\n

    :type LoadBalancerPorts: list
    :param LoadBalancerPorts: [REQUIRED]\nThe client port numbers of the listeners.\n\n(integer) --\n\n

    :rtype: dict

ReturnsResponse Syntax
{}


Response Structure

(dict) --
Contains the output of DeleteLoadBalancerListeners.





Exceptions

ElasticLoadBalancing.Client.exceptions.AccessPointNotFoundException

Examples
This example deletes the listener for the specified port from the specified load balancer.
response = client.delete_load_balancer_listeners(
    LoadBalancerName='my-load-balancer',
    LoadBalancerPorts=[
        80,
    ],
)

print(response)


Expected Output:
{
    'ResponseMetadata': {
        '...': '...',
    },
}



    :return: {}
    
    
    :returns: 
    ElasticLoadBalancing.Client.exceptions.AccessPointNotFoundException
    
    """
    pass

def delete_load_balancer_policy(LoadBalancerName=None, PolicyName=None):
    """
    Deletes the specified policy from the specified load balancer. This policy must not be enabled for any listeners.
    See also: AWS API Documentation
    
    Exceptions
    Examples
    This example deletes the specified policy from the specified load balancer. The policy must not be enabled on any listener.
    Expected Output:
    
    :example: response = client.delete_load_balancer_policy(
        LoadBalancerName='string',
        PolicyName='string'
    )
    
    
    :type LoadBalancerName: string
    :param LoadBalancerName: [REQUIRED]\nThe name of the load balancer.\n

    :type PolicyName: string
    :param PolicyName: [REQUIRED]\nThe name of the policy.\n

    :rtype: dict

ReturnsResponse Syntax
{}


Response Structure

(dict) --
Contains the output of DeleteLoadBalancerPolicy.





Exceptions

ElasticLoadBalancing.Client.exceptions.AccessPointNotFoundException
ElasticLoadBalancing.Client.exceptions.InvalidConfigurationRequestException

Examples
This example deletes the specified policy from the specified load balancer. The policy must not be enabled on any listener.
response = client.delete_load_balancer_policy(
    LoadBalancerName='my-load-balancer',
    PolicyName='my-duration-cookie-policy',
)

print(response)


Expected Output:
{
    'ResponseMetadata': {
        '...': '...',
    },
}



    :return: {}
    
    
    :returns: 
    ElasticLoadBalancing.Client.exceptions.AccessPointNotFoundException
    ElasticLoadBalancing.Client.exceptions.InvalidConfigurationRequestException
    
    """
    pass

def deregister_instances_from_load_balancer(LoadBalancerName=None, Instances=None):
    """
    Deregisters the specified instances from the specified load balancer. After the instance is deregistered, it no longer receives traffic from the load balancer.
    You can use  DescribeLoadBalancers to verify that the instance is deregistered from the load balancer.
    For more information, see Register or De-Register EC2 Instances in the Classic Load Balancers Guide .
    See also: AWS API Documentation
    
    Exceptions
    Examples
    This example deregisters the specified instance from the specified load balancer.
    Expected Output:
    
    :example: response = client.deregister_instances_from_load_balancer(
        LoadBalancerName='string',
        Instances=[
            {
                'InstanceId': 'string'
            },
        ]
    )
    
    
    :type LoadBalancerName: string
    :param LoadBalancerName: [REQUIRED]\nThe name of the load balancer.\n

    :type Instances: list
    :param Instances: [REQUIRED]\nThe IDs of the instances.\n\n(dict) --The ID of an EC2 instance.\n\nInstanceId (string) --The instance ID.\n\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'Instances': [
        {
            'InstanceId': 'string'
        },
    ]
}


Response Structure

(dict) --
Contains the output of DeregisterInstancesFromLoadBalancer.

Instances (list) --
The remaining instances registered with the load balancer.

(dict) --
The ID of an EC2 instance.

InstanceId (string) --
The instance ID.











Exceptions

ElasticLoadBalancing.Client.exceptions.AccessPointNotFoundException
ElasticLoadBalancing.Client.exceptions.InvalidEndPointException

Examples
This example deregisters the specified instance from the specified load balancer.
response = client.deregister_instances_from_load_balancer(
    Instances=[
        {
            'InstanceId': 'i-d6f6fae3',
        },
    ],
    LoadBalancerName='my-load-balancer',
)

print(response)


Expected Output:
{
    'Instances': [
        {
            'InstanceId': 'i-207d9717',
        },
        {
            'InstanceId': 'i-afefb49b',
        },
    ],
    'ResponseMetadata': {
        '...': '...',
    },
}



    :return: {
        'Instances': [
            {
                'InstanceId': 'string'
            },
        ]
    }
    
    
    :returns: 
    ElasticLoadBalancing.Client.exceptions.AccessPointNotFoundException
    ElasticLoadBalancing.Client.exceptions.InvalidEndPointException
    
    """
    pass

def describe_account_limits(Marker=None, PageSize=None):
    """
    Describes the current Elastic Load Balancing resource limits for your AWS account.
    For more information, see Limits for Your Classic Load Balancer in the Classic Load Balancers Guide .
    See also: AWS API Documentation
    
    
    :example: response = client.describe_account_limits(
        Marker='string',
        PageSize=123
    )
    
    
    :type Marker: string
    :param Marker: The marker for the next set of results. (You received this marker from a previous call.)

    :type PageSize: integer
    :param PageSize: The maximum number of results to return with this call.

    :rtype: dict

ReturnsResponse Syntax
{
    'Limits': [
        {
            'Name': 'string',
            'Max': 'string'
        },
    ],
    'NextMarker': 'string'
}


Response Structure

(dict) --

Limits (list) --
Information about the limits.

(dict) --
Information about an Elastic Load Balancing resource limit for your AWS account.

Name (string) --
The name of the limit. The possible values are:

classic-listeners
classic-load-balancers
classic-registered-instances


Max (string) --
The maximum value of the limit.





NextMarker (string) --
The marker to use when requesting the next set of results. If there are no additional results, the string is empty.








    :return: {
        'Limits': [
            {
                'Name': 'string',
                'Max': 'string'
            },
        ],
        'NextMarker': 'string'
    }
    
    
    :returns: 
    classic-listeners
    classic-load-balancers
    classic-registered-instances
    
    """
    pass

def describe_instance_health(LoadBalancerName=None, Instances=None):
    """
    Describes the state of the specified instances with respect to the specified load balancer. If no instances are specified, the call describes the state of all instances that are currently registered with the load balancer. If instances are specified, their state is returned even if they are no longer registered with the load balancer. The state of terminated instances is not returned.
    See also: AWS API Documentation
    
    Exceptions
    Examples
    This example describes the health of the instances for the specified load balancer.
    Expected Output:
    
    :example: response = client.describe_instance_health(
        LoadBalancerName='string',
        Instances=[
            {
                'InstanceId': 'string'
            },
        ]
    )
    
    
    :type LoadBalancerName: string
    :param LoadBalancerName: [REQUIRED]\nThe name of the load balancer.\n

    :type Instances: list
    :param Instances: The IDs of the instances.\n\n(dict) --The ID of an EC2 instance.\n\nInstanceId (string) --The instance ID.\n\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'InstanceStates': [
        {
            'InstanceId': 'string',
            'State': 'string',
            'ReasonCode': 'string',
            'Description': 'string'
        },
    ]
}


Response Structure

(dict) --
Contains the output for DescribeInstanceHealth.

InstanceStates (list) --
Information about the health of the instances.

(dict) --
Information about the state of an EC2 instance.

InstanceId (string) --
The ID of the instance.

State (string) --
The current state of the instance.
Valid values: InService | OutOfService | Unknown

ReasonCode (string) --
Information about the cause of OutOfService instances. Specifically, whether the cause is Elastic Load Balancing or the instance.
Valid values: ELB | Instance | N/A

Description (string) --
A description of the instance state. This string can contain one or more of the following messages.

N/A
A transient error occurred. Please try again later.
Instance has failed at least the UnhealthyThreshold number of health checks consecutively.
Instance has not passed the configured HealthyThreshold number of health checks consecutively.
Instance registration is still in progress.
Instance is in the EC2 Availability Zone for which LoadBalancer is not configured to route traffic to.
Instance is not currently registered with the LoadBalancer.
Instance deregistration currently in progress.
Disable Availability Zone is currently in progress.
Instance is in pending state.
Instance is in stopped state.
Instance is in terminated state.












Exceptions

ElasticLoadBalancing.Client.exceptions.AccessPointNotFoundException
ElasticLoadBalancing.Client.exceptions.InvalidEndPointException

Examples
This example describes the health of the instances for the specified load balancer.
response = client.describe_instance_health(
    LoadBalancerName='my-load-balancer',
)

print(response)


Expected Output:
{
    'InstanceStates': [
        {
            'Description': 'N/A',
            'InstanceId': 'i-207d9717',
            'ReasonCode': 'N/A',
            'State': 'InService',
        },
        {
            'Description': 'N/A',
            'InstanceId': 'i-afefb49b',
            'ReasonCode': 'N/A',
            'State': 'InService',
        },
    ],
    'ResponseMetadata': {
        '...': '...',
    },
}



    :return: {
        'InstanceStates': [
            {
                'InstanceId': 'string',
                'State': 'string',
                'ReasonCode': 'string',
                'Description': 'string'
            },
        ]
    }
    
    
    :returns: 
    N/A
    A transient error occurred. Please try again later.
    Instance has failed at least the UnhealthyThreshold number of health checks consecutively.
    Instance has not passed the configured HealthyThreshold number of health checks consecutively.
    Instance registration is still in progress.
    Instance is in the EC2 Availability Zone for which LoadBalancer is not configured to route traffic to.
    Instance is not currently registered with the LoadBalancer.
    Instance deregistration currently in progress.
    Disable Availability Zone is currently in progress.
    Instance is in pending state.
    Instance is in stopped state.
    Instance is in terminated state.
    
    """
    pass

def describe_load_balancer_attributes(LoadBalancerName=None):
    """
    Describes the attributes for the specified load balancer.
    See also: AWS API Documentation
    
    Exceptions
    Examples
    This example describes the attributes of the specified load balancer.
    Expected Output:
    
    :example: response = client.describe_load_balancer_attributes(
        LoadBalancerName='string'
    )
    
    
    :type LoadBalancerName: string
    :param LoadBalancerName: [REQUIRED]\nThe name of the load balancer.\n

    :rtype: dict
ReturnsResponse Syntax{
    'LoadBalancerAttributes': {
        'CrossZoneLoadBalancing': {
            'Enabled': True|False
        },
        'AccessLog': {
            'Enabled': True|False,
            'S3BucketName': 'string',
            'EmitInterval': 123,
            'S3BucketPrefix': 'string'
        },
        'ConnectionDraining': {
            'Enabled': True|False,
            'Timeout': 123
        },
        'ConnectionSettings': {
            'IdleTimeout': 123
        },
        'AdditionalAttributes': [
            {
                'Key': 'string',
                'Value': 'string'
            },
        ]
    }
}


Response Structure

(dict) --Contains the output of DescribeLoadBalancerAttributes.

LoadBalancerAttributes (dict) --Information about the load balancer attributes.

CrossZoneLoadBalancing (dict) --If enabled, the load balancer routes the request traffic evenly across all instances regardless of the Availability Zones.
For more information, see Configure Cross-Zone Load Balancing in the Classic Load Balancers Guide .

Enabled (boolean) --Specifies whether cross-zone load balancing is enabled for the load balancer.



AccessLog (dict) --If enabled, the load balancer captures detailed information of all requests and delivers the information to the Amazon S3 bucket that you specify.
For more information, see Enable Access Logs in the Classic Load Balancers Guide .

Enabled (boolean) --Specifies whether access logs are enabled for the load balancer.

S3BucketName (string) --The name of the Amazon S3 bucket where the access logs are stored.

EmitInterval (integer) --The interval for publishing the access logs. You can specify an interval of either 5 minutes or 60 minutes.
Default: 60 minutes

S3BucketPrefix (string) --The logical hierarchy you created for your Amazon S3 bucket, for example my-bucket-prefix/prod . If the prefix is not provided, the log is placed at the root level of the bucket.



ConnectionDraining (dict) --If enabled, the load balancer allows existing requests to complete before the load balancer shifts traffic away from a deregistered or unhealthy instance.
For more information, see Configure Connection Draining in the Classic Load Balancers Guide .

Enabled (boolean) --Specifies whether connection draining is enabled for the load balancer.

Timeout (integer) --The maximum time, in seconds, to keep the existing connections open before deregistering the instances.



ConnectionSettings (dict) --If enabled, the load balancer allows the connections to remain idle (no data is sent over the connection) for the specified duration.
By default, Elastic Load Balancing maintains a 60-second idle connection timeout for both front-end and back-end connections of your load balancer. For more information, see Configure Idle Connection Timeout in the Classic Load Balancers Guide .

IdleTimeout (integer) --The time, in seconds, that the connection is allowed to be idle (no data has been sent over the connection) before it is closed by the load balancer.



AdditionalAttributes (list) --This parameter is reserved.

(dict) --This data type is reserved.

Key (string) --This parameter is reserved.

Value (string) --This parameter is reserved.












Exceptions

ElasticLoadBalancing.Client.exceptions.AccessPointNotFoundException
ElasticLoadBalancing.Client.exceptions.LoadBalancerAttributeNotFoundException

Examples
This example describes the attributes of the specified load balancer.
response = client.describe_load_balancer_attributes(
    LoadBalancerName='my-load-balancer',
)

print(response)


Expected Output:
{
    'LoadBalancerAttributes': {
        'AccessLog': {
            'Enabled': False,
        },
        'ConnectionDraining': {
            'Enabled': False,
            'Timeout': 300,
        },
        'ConnectionSettings': {
            'IdleTimeout': 60,
        },
        'CrossZoneLoadBalancing': {
            'Enabled': False,
        },
    },
    'ResponseMetadata': {
        '...': '...',
    },
}



    :return: {
        'LoadBalancerAttributes': {
            'CrossZoneLoadBalancing': {
                'Enabled': True|False
            },
            'AccessLog': {
                'Enabled': True|False,
                'S3BucketName': 'string',
                'EmitInterval': 123,
                'S3BucketPrefix': 'string'
            },
            'ConnectionDraining': {
                'Enabled': True|False,
                'Timeout': 123
            },
            'ConnectionSettings': {
                'IdleTimeout': 123
            },
            'AdditionalAttributes': [
                {
                    'Key': 'string',
                    'Value': 'string'
                },
            ]
        }
    }
    
    
    """
    pass

def describe_load_balancer_policies(LoadBalancerName=None, PolicyNames=None):
    """
    Describes the specified policies.
    If you specify a load balancer name, the action returns the descriptions of all policies created for the load balancer. If you specify a policy name associated with your load balancer, the action returns the description of that policy. If you don\'t specify a load balancer name, the action returns descriptions of the specified sample policies, or descriptions of all sample policies. The names of the sample policies have the ELBSample- prefix.
    See also: AWS API Documentation
    
    Exceptions
    Examples
    This example describes the specified policy associated with the specified load balancer.
    Expected Output:
    
    :example: response = client.describe_load_balancer_policies(
        LoadBalancerName='string',
        PolicyNames=[
            'string',
        ]
    )
    
    
    :type LoadBalancerName: string
    :param LoadBalancerName: The name of the load balancer.

    :type PolicyNames: list
    :param PolicyNames: The names of the policies.\n\n(string) --\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'PolicyDescriptions': [
        {
            'PolicyName': 'string',
            'PolicyTypeName': 'string',
            'PolicyAttributeDescriptions': [
                {
                    'AttributeName': 'string',
                    'AttributeValue': 'string'
                },
            ]
        },
    ]
}


Response Structure

(dict) --
Contains the output of DescribeLoadBalancerPolicies.

PolicyDescriptions (list) --
Information about the policies.

(dict) --
Information about a policy.

PolicyName (string) --
The name of the policy.

PolicyTypeName (string) --
The name of the policy type.

PolicyAttributeDescriptions (list) --
The policy attributes.

(dict) --
Information about a policy attribute.

AttributeName (string) --
The name of the attribute.

AttributeValue (string) --
The value of the attribute.















Exceptions

ElasticLoadBalancing.Client.exceptions.AccessPointNotFoundException
ElasticLoadBalancing.Client.exceptions.PolicyNotFoundException

Examples
This example describes the specified policy associated with the specified load balancer.
response = client.describe_load_balancer_policies(
    LoadBalancerName='my-load-balancer',
    PolicyNames=[
        'my-authentication-policy',
    ],
)

print(response)


Expected Output:
{
    'PolicyDescriptions': [
        {
            'PolicyAttributeDescriptions': [
                {
                    'AttributeName': 'PublicKeyPolicyName',
                    'AttributeValue': 'my-PublicKey-policy',
                },
            ],
            'PolicyName': 'my-authentication-policy',
            'PolicyTypeName': 'BackendServerAuthenticationPolicyType',
        },
    ],
    'ResponseMetadata': {
        '...': '...',
    },
}



    :return: {
        'PolicyDescriptions': [
            {
                'PolicyName': 'string',
                'PolicyTypeName': 'string',
                'PolicyAttributeDescriptions': [
                    {
                        'AttributeName': 'string',
                        'AttributeValue': 'string'
                    },
                ]
            },
        ]
    }
    
    
    :returns: 
    ElasticLoadBalancing.Client.exceptions.AccessPointNotFoundException
    ElasticLoadBalancing.Client.exceptions.PolicyNotFoundException
    
    """
    pass

def describe_load_balancer_policy_types(PolicyTypeNames=None):
    """
    Describes the specified load balancer policy types or all load balancer policy types.
    The description of each type indicates how it can be used. For example, some policies can be used only with layer 7 listeners, some policies can be used only with layer 4 listeners, and some policies can be used only with your EC2 instances.
    You can use  CreateLoadBalancerPolicy to create a policy configuration for any of these policy types. Then, depending on the policy type, use either  SetLoadBalancerPoliciesOfListener or  SetLoadBalancerPoliciesForBackendServer to set the policy.
    See also: AWS API Documentation
    
    Exceptions
    Examples
    This example describes the specified load balancer policy type.
    Expected Output:
    
    :example: response = client.describe_load_balancer_policy_types(
        PolicyTypeNames=[
            'string',
        ]
    )
    
    
    :type PolicyTypeNames: list
    :param PolicyTypeNames: The names of the policy types. If no names are specified, describes all policy types defined by Elastic Load Balancing.\n\n(string) --\n\n

    :rtype: dict
ReturnsResponse Syntax{
    'PolicyTypeDescriptions': [
        {
            'PolicyTypeName': 'string',
            'Description': 'string',
            'PolicyAttributeTypeDescriptions': [
                {
                    'AttributeName': 'string',
                    'AttributeType': 'string',
                    'Description': 'string',
                    'DefaultValue': 'string',
                    'Cardinality': 'string'
                },
            ]
        },
    ]
}


Response Structure

(dict) --Contains the output of DescribeLoadBalancerPolicyTypes.

PolicyTypeDescriptions (list) --Information about the policy types.

(dict) --Information about a policy type.

PolicyTypeName (string) --The name of the policy type.

Description (string) --A description of the policy type.

PolicyAttributeTypeDescriptions (list) --The description of the policy attributes associated with the policies defined by Elastic Load Balancing.

(dict) --Information about a policy attribute type.

AttributeName (string) --The name of the attribute.

AttributeType (string) --The type of the attribute. For example, Boolean or Integer .

Description (string) --A description of the attribute.

DefaultValue (string) --The default value of the attribute, if applicable.

Cardinality (string) --The cardinality of the attribute.
Valid values:

ONE(1) : Single value required
ZERO_OR_ONE(0..1) : Up to one value is allowed
ZERO_OR_MORE(0..*) : Optional. Multiple values are allowed
ONE_OR_MORE(1..*0) : Required. Multiple values are allowed















Exceptions

ElasticLoadBalancing.Client.exceptions.PolicyTypeNotFoundException

Examples
This example describes the specified load balancer policy type.
response = client.describe_load_balancer_policy_types(
    PolicyTypeNames=[
        'ProxyProtocolPolicyType',
    ],
)

print(response)


Expected Output:
{
    'PolicyTypeDescriptions': [
        {
            'Description': 'Policy that controls whether to include the IP address and port of the originating request for TCP messages. This policy operates on TCP listeners only.',
            'PolicyAttributeTypeDescriptions': [
                {
                    'AttributeName': 'ProxyProtocol',
                    'AttributeType': 'Boolean',
                    'Cardinality': 'ONE',
                },
            ],
            'PolicyTypeName': 'ProxyProtocolPolicyType',
        },
    ],
    'ResponseMetadata': {
        '...': '...',
    },
}



    :return: {
        'PolicyTypeDescriptions': [
            {
                'PolicyTypeName': 'string',
                'Description': 'string',
                'PolicyAttributeTypeDescriptions': [
                    {
                        'AttributeName': 'string',
                        'AttributeType': 'string',
                        'Description': 'string',
                        'DefaultValue': 'string',
                        'Cardinality': 'string'
                    },
                ]
            },
        ]
    }
    
    
    :returns: 
    ONE(1) : Single value required
    ZERO_OR_ONE(0..1) : Up to one value is allowed
    ZERO_OR_MORE(0..*) : Optional. Multiple values are allowed
    ONE_OR_MORE(1..*0) : Required. Multiple values are allowed
    
    """
    pass

def describe_load_balancers(LoadBalancerNames=None, Marker=None, PageSize=None):
    """
    Describes the specified the load balancers. If no load balancers are specified, the call describes all of your load balancers.
    See also: AWS API Documentation
    
    Exceptions
    Examples
    This example describes the specified load balancer.
    Expected Output:
    
    :example: response = client.describe_load_balancers(
        LoadBalancerNames=[
            'string',
        ],
        Marker='string',
        PageSize=123
    )
    
    
    :type LoadBalancerNames: list
    :param LoadBalancerNames: The names of the load balancers.\n\n(string) --\n\n

    :type Marker: string
    :param Marker: The marker for the next set of results. (You received this marker from a previous call.)

    :type PageSize: integer
    :param PageSize: The maximum number of results to return with this call (a number from 1 to 400). The default is 400.

    :rtype: dict

ReturnsResponse Syntax
{
    'LoadBalancerDescriptions': [
        {
            'LoadBalancerName': 'string',
            'DNSName': 'string',
            'CanonicalHostedZoneName': 'string',
            'CanonicalHostedZoneNameID': 'string',
            'ListenerDescriptions': [
                {
                    'Listener': {
                        'Protocol': 'string',
                        'LoadBalancerPort': 123,
                        'InstanceProtocol': 'string',
                        'InstancePort': 123,
                        'SSLCertificateId': 'string'
                    },
                    'PolicyNames': [
                        'string',
                    ]
                },
            ],
            'Policies': {
                'AppCookieStickinessPolicies': [
                    {
                        'PolicyName': 'string',
                        'CookieName': 'string'
                    },
                ],
                'LBCookieStickinessPolicies': [
                    {
                        'PolicyName': 'string',
                        'CookieExpirationPeriod': 123
                    },
                ],
                'OtherPolicies': [
                    'string',
                ]
            },
            'BackendServerDescriptions': [
                {
                    'InstancePort': 123,
                    'PolicyNames': [
                        'string',
                    ]
                },
            ],
            'AvailabilityZones': [
                'string',
            ],
            'Subnets': [
                'string',
            ],
            'VPCId': 'string',
            'Instances': [
                {
                    'InstanceId': 'string'
                },
            ],
            'HealthCheck': {
                'Target': 'string',
                'Interval': 123,
                'Timeout': 123,
                'UnhealthyThreshold': 123,
                'HealthyThreshold': 123
            },
            'SourceSecurityGroup': {
                'OwnerAlias': 'string',
                'GroupName': 'string'
            },
            'SecurityGroups': [
                'string',
            ],
            'CreatedTime': datetime(2015, 1, 1),
            'Scheme': 'string'
        },
    ],
    'NextMarker': 'string'
}


Response Structure

(dict) --
Contains the parameters for DescribeLoadBalancers.

LoadBalancerDescriptions (list) --
Information about the load balancers.

(dict) --
Information about a load balancer.

LoadBalancerName (string) --
The name of the load balancer.

DNSName (string) --
The DNS name of the load balancer.

CanonicalHostedZoneName (string) --
The DNS name of the load balancer.
For more information, see Configure a Custom Domain Name in the Classic Load Balancers Guide .

CanonicalHostedZoneNameID (string) --
The ID of the Amazon Route 53 hosted zone for the load balancer.

ListenerDescriptions (list) --
The listeners for the load balancer.

(dict) --
The policies enabled for a listener.

Listener (dict) --
The listener.

Protocol (string) --
The load balancer transport protocol to use for routing: HTTP, HTTPS, TCP, or SSL.

LoadBalancerPort (integer) --
The port on which the load balancer is listening. On EC2-VPC, you can specify any port from the range 1-65535. On EC2-Classic, you can specify any port from the following list: 25, 80, 443, 465, 587, 1024-65535.

InstanceProtocol (string) --
The protocol to use for routing traffic to instances: HTTP, HTTPS, TCP, or SSL.
If the front-end protocol is HTTP, HTTPS, TCP, or SSL, InstanceProtocol must be at the same protocol.
If there is another listener with the same InstancePort whose InstanceProtocol is secure, (HTTPS or SSL), the listener\'s InstanceProtocol must also be secure.
If there is another listener with the same InstancePort whose InstanceProtocol is HTTP or TCP, the listener\'s InstanceProtocol must be HTTP or TCP.

InstancePort (integer) --
The port on which the instance is listening.

SSLCertificateId (string) --
The Amazon Resource Name (ARN) of the server certificate.



PolicyNames (list) --
The policies. If there are no policies enabled, the list is empty.

(string) --






Policies (dict) --
The policies defined for the load balancer.

AppCookieStickinessPolicies (list) --
The stickiness policies created using  CreateAppCookieStickinessPolicy .

(dict) --
Information about a policy for application-controlled session stickiness.

PolicyName (string) --
The mnemonic name for the policy being created. The name must be unique within a set of policies for this load balancer.

CookieName (string) --
The name of the application cookie used for stickiness.





LBCookieStickinessPolicies (list) --
The stickiness policies created using  CreateLBCookieStickinessPolicy .

(dict) --
Information about a policy for duration-based session stickiness.

PolicyName (string) --
The name of the policy. This name must be unique within the set of policies for this load balancer.

CookieExpirationPeriod (integer) --
The time period, in seconds, after which the cookie should be considered stale. If this parameter is not specified, the stickiness session lasts for the duration of the browser session.





OtherPolicies (list) --
The policies other than the stickiness policies.

(string) --




BackendServerDescriptions (list) --
Information about your EC2 instances.

(dict) --
Information about the configuration of an EC2 instance.

InstancePort (integer) --
The port on which the EC2 instance is listening.

PolicyNames (list) --
The names of the policies enabled for the EC2 instance.

(string) --






AvailabilityZones (list) --
The Availability Zones for the load balancer.

(string) --


Subnets (list) --
The IDs of the subnets for the load balancer.

(string) --


VPCId (string) --
The ID of the VPC for the load balancer.

Instances (list) --
The IDs of the instances for the load balancer.

(dict) --
The ID of an EC2 instance.

InstanceId (string) --
The instance ID.





HealthCheck (dict) --
Information about the health checks conducted on the load balancer.

Target (string) --
The instance being checked. The protocol is either TCP, HTTP, HTTPS, or SSL. The range of valid ports is one (1) through 65535.
TCP is the default, specified as a TCP: port pair, for example "TCP:5000". In this case, a health check simply attempts to open a TCP connection to the instance on the specified port. Failure to connect within the configured timeout is considered unhealthy.
SSL is also specified as SSL: port pair, for example, SSL:5000.
For HTTP/HTTPS, you must include a ping path in the string. HTTP is specified as a HTTP:port;/;PathToPing; grouping, for example "HTTP:80/weather/us/wa/seattle". In this case, a HTTP GET request is issued to the instance on the given port and path. Any answer other than "200 OK" within the timeout period is considered unhealthy.
The total length of the HTTP ping target must be 1024 16-bit Unicode characters or less.

Interval (integer) --
The approximate interval, in seconds, between health checks of an individual instance.

Timeout (integer) --
The amount of time, in seconds, during which no response means a failed health check.
This value must be less than the Interval value.

UnhealthyThreshold (integer) --
The number of consecutive health check failures required before moving the instance to the Unhealthy state.

HealthyThreshold (integer) --
The number of consecutive health checks successes required before moving the instance to the Healthy state.



SourceSecurityGroup (dict) --
The security group for the load balancer, which you can use as part of your inbound rules for your registered instances. To only allow traffic from load balancers, add a security group rule that specifies this source security group as the inbound source.

OwnerAlias (string) --
The owner of the security group.

GroupName (string) --
The name of the security group.



SecurityGroups (list) --
The security groups for the load balancer. Valid only for load balancers in a VPC.

(string) --


CreatedTime (datetime) --
The date and time the load balancer was created.

Scheme (string) --
The type of load balancer. Valid only for load balancers in a VPC.
If Scheme is internet-facing , the load balancer has a public DNS name that resolves to a public IP address.
If Scheme is internal , the load balancer has a public DNS name that resolves to a private IP address.





NextMarker (string) --
The marker to use when requesting the next set of results. If there are no additional results, the string is empty.







Exceptions

ElasticLoadBalancing.Client.exceptions.AccessPointNotFoundException
ElasticLoadBalancing.Client.exceptions.DependencyThrottleException

Examples
This example describes the specified load balancer.
response = client.describe_load_balancers(
    LoadBalancerNames=[
        'my-load-balancer',
    ],
)

print(response)


Expected Output:
{
    'LoadBalancerDescriptions': [
        {
            'AvailabilityZones': [
                'us-west-2a',
            ],
            'BackendServerDescriptions': [
                {
                    'InstancePort': 80,
                    'PolicyNames': [
                        'my-ProxyProtocol-policy',
                    ],
                },
            ],
            'CanonicalHostedZoneName': 'my-load-balancer-1234567890.us-west-2.elb.amazonaws.com',
            'CanonicalHostedZoneNameID': 'Z3DZXE0EXAMPLE',
            'CreatedTime': datetime(2015, 3, 19, 3, 24, 2, 3, 78, 0),
            'DNSName': 'my-load-balancer-1234567890.us-west-2.elb.amazonaws.com',
            'HealthCheck': {
                'HealthyThreshold': 2,
                'Interval': 30,
                'Target': 'HTTP:80/png',
                'Timeout': 3,
                'UnhealthyThreshold': 2,
            },
            'Instances': [
                {
                    'InstanceId': 'i-207d9717',
                },
                {
                    'InstanceId': 'i-afefb49b',
                },
            ],
            'ListenerDescriptions': [
                {
                    'Listener': {
                        'InstancePort': 80,
                        'InstanceProtocol': 'HTTP',
                        'LoadBalancerPort': 80,
                        'Protocol': 'HTTP',
                    },
                    'PolicyNames': [
                    ],
                },
                {
                    'Listener': {
                        'InstancePort': 443,
                        'InstanceProtocol': 'HTTPS',
                        'LoadBalancerPort': 443,
                        'Protocol': 'HTTPS',
                        'SSLCertificateId': 'arn:aws:iam::123456789012:server-certificate/my-server-cert',
                    },
                    'PolicyNames': [
                        'ELBSecurityPolicy-2015-03',
                    ],
                },
            ],
            'LoadBalancerName': 'my-load-balancer',
            'Policies': {
                'AppCookieStickinessPolicies': [
                ],
                'LBCookieStickinessPolicies': [
                    {
                        'CookieExpirationPeriod': 60,
                        'PolicyName': 'my-duration-cookie-policy',
                    },
                ],
                'OtherPolicies': [
                    'my-PublicKey-policy',
                    'my-authentication-policy',
                    'my-SSLNegotiation-policy',
                    'my-ProxyProtocol-policy',
                    'ELBSecurityPolicy-2015-03',
                ],
            },
            'Scheme': 'internet-facing',
            'SecurityGroups': [
                'sg-a61988c3',
            ],
            'SourceSecurityGroup': {
                'GroupName': 'my-elb-sg',
                'OwnerAlias': '123456789012',
            },
            'Subnets': [
                'subnet-15aaab61',
            ],
            'VPCId': 'vpc-a01106c2',
        },
    ],
    'ResponseMetadata': {
        '...': '...',
    },
}



    :return: {
        'LoadBalancerDescriptions': [
            {
                'LoadBalancerName': 'string',
                'DNSName': 'string',
                'CanonicalHostedZoneName': 'string',
                'CanonicalHostedZoneNameID': 'string',
                'ListenerDescriptions': [
                    {
                        'Listener': {
                            'Protocol': 'string',
                            'LoadBalancerPort': 123,
                            'InstanceProtocol': 'string',
                            'InstancePort': 123,
                            'SSLCertificateId': 'string'
                        },
                        'PolicyNames': [
                            'string',
                        ]
                    },
                ],
                'Policies': {
                    'AppCookieStickinessPolicies': [
                        {
                            'PolicyName': 'string',
                            'CookieName': 'string'
                        },
                    ],
                    'LBCookieStickinessPolicies': [
                        {
                            'PolicyName': 'string',
                            'CookieExpirationPeriod': 123
                        },
                    ],
                    'OtherPolicies': [
                        'string',
                    ]
                },
                'BackendServerDescriptions': [
                    {
                        'InstancePort': 123,
                        'PolicyNames': [
                            'string',
                        ]
                    },
                ],
                'AvailabilityZones': [
                    'string',
                ],
                'Subnets': [
                    'string',
                ],
                'VPCId': 'string',
                'Instances': [
                    {
                        'InstanceId': 'string'
                    },
                ],
                'HealthCheck': {
                    'Target': 'string',
                    'Interval': 123,
                    'Timeout': 123,
                    'UnhealthyThreshold': 123,
                    'HealthyThreshold': 123
                },
                'SourceSecurityGroup': {
                    'OwnerAlias': 'string',
                    'GroupName': 'string'
                },
                'SecurityGroups': [
                    'string',
                ],
                'CreatedTime': datetime(2015, 1, 1),
                'Scheme': 'string'
            },
        ],
        'NextMarker': 'string'
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def describe_tags(LoadBalancerNames=None):
    """
    Describes the tags associated with the specified load balancers.
    See also: AWS API Documentation
    
    Exceptions
    Examples
    This example describes the tags for the specified load balancer.
    Expected Output:
    
    :example: response = client.describe_tags(
        LoadBalancerNames=[
            'string',
        ]
    )
    
    
    :type LoadBalancerNames: list
    :param LoadBalancerNames: [REQUIRED]\nThe names of the load balancers.\n\n(string) --\n\n

    :rtype: dict
ReturnsResponse Syntax{
    'TagDescriptions': [
        {
            'LoadBalancerName': 'string',
            'Tags': [
                {
                    'Key': 'string',
                    'Value': 'string'
                },
            ]
        },
    ]
}


Response Structure

(dict) --Contains the output for DescribeTags.

TagDescriptions (list) --Information about the tags.

(dict) --The tags associated with a load balancer.

LoadBalancerName (string) --The name of the load balancer.

Tags (list) --The tags.

(dict) --Information about a tag.

Key (string) --The key of the tag.

Value (string) --The value of the tag.














Exceptions

ElasticLoadBalancing.Client.exceptions.AccessPointNotFoundException

Examples
This example describes the tags for the specified load balancer.
response = client.describe_tags(
    LoadBalancerNames=[
        'my-load-balancer',
    ],
)

print(response)


Expected Output:
{
    'TagDescriptions': [
        {
            'LoadBalancerName': 'my-load-balancer',
            'Tags': [
                {
                    'Key': 'project',
                    'Value': 'lima',
                },
                {
                    'Key': 'department',
                    'Value': 'digital-media',
                },
            ],
        },
    ],
    'ResponseMetadata': {
        '...': '...',
    },
}



    :return: {
        'TagDescriptions': [
            {
                'LoadBalancerName': 'string',
                'Tags': [
                    {
                        'Key': 'string',
                        'Value': 'string'
                    },
                ]
            },
        ]
    }
    
    
    :returns: 
    ElasticLoadBalancing.Client.exceptions.AccessPointNotFoundException
    
    """
    pass

def detach_load_balancer_from_subnets(LoadBalancerName=None, Subnets=None):
    """
    Removes the specified subnets from the set of configured subnets for the load balancer.
    After a subnet is removed, all EC2 instances registered with the load balancer in the removed subnet go into the OutOfService state. Then, the load balancer balances the traffic among the remaining routable subnets.
    See also: AWS API Documentation
    
    Exceptions
    Examples
    This example detaches the specified load balancer from the specified subnet.
    Expected Output:
    
    :example: response = client.detach_load_balancer_from_subnets(
        LoadBalancerName='string',
        Subnets=[
            'string',
        ]
    )
    
    
    :type LoadBalancerName: string
    :param LoadBalancerName: [REQUIRED]\nThe name of the load balancer.\n

    :type Subnets: list
    :param Subnets: [REQUIRED]\nThe IDs of the subnets.\n\n(string) --\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'Subnets': [
        'string',
    ]
}


Response Structure

(dict) --
Contains the output of DetachLoadBalancerFromSubnets.

Subnets (list) --
The IDs of the remaining subnets for the load balancer.

(string) --








Exceptions

ElasticLoadBalancing.Client.exceptions.AccessPointNotFoundException
ElasticLoadBalancing.Client.exceptions.InvalidConfigurationRequestException

Examples
This example detaches the specified load balancer from the specified subnet.
response = client.detach_load_balancer_from_subnets(
    LoadBalancerName='my-load-balancer',
    Subnets=[
        'subnet-0ecac448',
    ],
)

print(response)


Expected Output:
{
    'Subnets': [
        'subnet-15aaab61',
    ],
    'ResponseMetadata': {
        '...': '...',
    },
}



    :return: {
        'Subnets': [
            'string',
        ]
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def disable_availability_zones_for_load_balancer(LoadBalancerName=None, AvailabilityZones=None):
    """
    Removes the specified Availability Zones from the set of Availability Zones for the specified load balancer in EC2-Classic or a default VPC.
    For load balancers in a non-default VPC, use  DetachLoadBalancerFromSubnets .
    There must be at least one Availability Zone registered with a load balancer at all times. After an Availability Zone is removed, all instances registered with the load balancer that are in the removed Availability Zone go into the OutOfService state. Then, the load balancer attempts to equally balance the traffic among its remaining Availability Zones.
    For more information, see Add or Remove Availability Zones in the Classic Load Balancers Guide .
    See also: AWS API Documentation
    
    Exceptions
    Examples
    This example removes the specified Availability Zone from the set of Availability Zones for the specified load balancer.
    Expected Output:
    
    :example: response = client.disable_availability_zones_for_load_balancer(
        LoadBalancerName='string',
        AvailabilityZones=[
            'string',
        ]
    )
    
    
    :type LoadBalancerName: string
    :param LoadBalancerName: [REQUIRED]\nThe name of the load balancer.\n

    :type AvailabilityZones: list
    :param AvailabilityZones: [REQUIRED]\nThe Availability Zones.\n\n(string) --\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'AvailabilityZones': [
        'string',
    ]
}


Response Structure

(dict) --
Contains the output for DisableAvailabilityZonesForLoadBalancer.

AvailabilityZones (list) --
The remaining Availability Zones for the load balancer.

(string) --








Exceptions

ElasticLoadBalancing.Client.exceptions.AccessPointNotFoundException
ElasticLoadBalancing.Client.exceptions.InvalidConfigurationRequestException

Examples
This example removes the specified Availability Zone from the set of Availability Zones for the specified load balancer.
response = client.disable_availability_zones_for_load_balancer(
    AvailabilityZones=[
        'us-west-2a',
    ],
    LoadBalancerName='my-load-balancer',
)

print(response)


Expected Output:
{
    'AvailabilityZones': [
        'us-west-2b',
    ],
    'ResponseMetadata': {
        '...': '...',
    },
}



    :return: {
        'AvailabilityZones': [
            'string',
        ]
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def enable_availability_zones_for_load_balancer(LoadBalancerName=None, AvailabilityZones=None):
    """
    Adds the specified Availability Zones to the set of Availability Zones for the specified load balancer in EC2-Classic or a default VPC.
    For load balancers in a non-default VPC, use  AttachLoadBalancerToSubnets .
    The load balancer evenly distributes requests across all its registered Availability Zones that contain instances. For more information, see Add or Remove Availability Zones in the Classic Load Balancers Guide .
    See also: AWS API Documentation
    
    Exceptions
    Examples
    This example adds the specified Availability Zone to the specified load balancer.
    Expected Output:
    
    :example: response = client.enable_availability_zones_for_load_balancer(
        LoadBalancerName='string',
        AvailabilityZones=[
            'string',
        ]
    )
    
    
    :type LoadBalancerName: string
    :param LoadBalancerName: [REQUIRED]\nThe name of the load balancer.\n

    :type AvailabilityZones: list
    :param AvailabilityZones: [REQUIRED]\nThe Availability Zones. These must be in the same region as the load balancer.\n\n(string) --\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'AvailabilityZones': [
        'string',
    ]
}


Response Structure

(dict) --
Contains the output of EnableAvailabilityZonesForLoadBalancer.

AvailabilityZones (list) --
The updated list of Availability Zones for the load balancer.

(string) --








Exceptions

ElasticLoadBalancing.Client.exceptions.AccessPointNotFoundException

Examples
This example adds the specified Availability Zone to the specified load balancer.
response = client.enable_availability_zones_for_load_balancer(
    AvailabilityZones=[
        'us-west-2b',
    ],
    LoadBalancerName='my-load-balancer',
)

print(response)


Expected Output:
{
    'AvailabilityZones': [
        'us-west-2a',
        'us-west-2b',
    ],
    'ResponseMetadata': {
        '...': '...',
    },
}



    :return: {
        'AvailabilityZones': [
            'string',
        ]
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def generate_presigned_url(ClientMethod=None, Params=None, ExpiresIn=None, HttpMethod=None):
    """
    Generate a presigned url given a client, its method, and arguments
    
    :type ClientMethod: string
    :param ClientMethod: The client method to presign for

    :type Params: dict
    :param Params: The parameters normally passed to\nClientMethod.

    :type ExpiresIn: int
    :param ExpiresIn: The number of seconds the presigned url is valid\nfor. By default it expires in an hour (3600 seconds)

    :type HttpMethod: string
    :param HttpMethod: The http method to use on the generated url. By\ndefault, the http method is whatever is used in the method\'s model.

    """
    pass

def get_paginator(operation_name=None):
    """
    Create a paginator for an operation.
    
    :type operation_name: string
    :param operation_name: The operation name. This is the same name\nas the method name on the client. For example, if the\nmethod name is create_foo, and you\'d normally invoke the\noperation as client.create_foo(**kwargs), if the\ncreate_foo operation can be paginated, you can use the\ncall client.get_paginator('create_foo').

    :rtype: L{botocore.paginate.Paginator}
ReturnsA paginator object.


    """
    pass

def get_waiter(waiter_name=None):
    """
    Returns an object that can wait for some condition.
    
    :type waiter_name: str
    :param waiter_name: The name of the waiter to get. See the waiters\nsection of the service docs for a list of available waiters.

    :rtype: botocore.waiter.Waiter


    """
    pass

def modify_load_balancer_attributes(LoadBalancerName=None, LoadBalancerAttributes=None):
    """
    Modifies the attributes of the specified load balancer.
    You can modify the load balancer attributes, such as AccessLogs , ConnectionDraining , and CrossZoneLoadBalancing by either enabling or disabling them. Or, you can modify the load balancer attribute ConnectionSettings by specifying an idle connection timeout value for your load balancer.
    For more information, see the following in the Classic Load Balancers Guide :
    See also: AWS API Documentation
    
    Exceptions
    Examples
    This example enables cross-zone load balancing for the specified load balancer.
    Expected Output:
    This example enables connection draining for the specified load balancer.
    Expected Output:
    
    :example: response = client.modify_load_balancer_attributes(
        LoadBalancerName='string',
        LoadBalancerAttributes={
            'CrossZoneLoadBalancing': {
                'Enabled': True|False
            },
            'AccessLog': {
                'Enabled': True|False,
                'S3BucketName': 'string',
                'EmitInterval': 123,
                'S3BucketPrefix': 'string'
            },
            'ConnectionDraining': {
                'Enabled': True|False,
                'Timeout': 123
            },
            'ConnectionSettings': {
                'IdleTimeout': 123
            },
            'AdditionalAttributes': [
                {
                    'Key': 'string',
                    'Value': 'string'
                },
            ]
        }
    )
    
    
    :type LoadBalancerName: string
    :param LoadBalancerName: [REQUIRED]\nThe name of the load balancer.\n

    :type LoadBalancerAttributes: dict
    :param LoadBalancerAttributes: [REQUIRED]\nThe attributes for the load balancer.\n\nCrossZoneLoadBalancing (dict) --If enabled, the load balancer routes the request traffic evenly across all instances regardless of the Availability Zones.\nFor more information, see Configure Cross-Zone Load Balancing in the Classic Load Balancers Guide .\n\nEnabled (boolean) -- [REQUIRED]Specifies whether cross-zone load balancing is enabled for the load balancer.\n\n\n\nAccessLog (dict) --If enabled, the load balancer captures detailed information of all requests and delivers the information to the Amazon S3 bucket that you specify.\nFor more information, see Enable Access Logs in the Classic Load Balancers Guide .\n\nEnabled (boolean) -- [REQUIRED]Specifies whether access logs are enabled for the load balancer.\n\nS3BucketName (string) --The name of the Amazon S3 bucket where the access logs are stored.\n\nEmitInterval (integer) --The interval for publishing the access logs. You can specify an interval of either 5 minutes or 60 minutes.\nDefault: 60 minutes\n\nS3BucketPrefix (string) --The logical hierarchy you created for your Amazon S3 bucket, for example my-bucket-prefix/prod . If the prefix is not provided, the log is placed at the root level of the bucket.\n\n\n\nConnectionDraining (dict) --If enabled, the load balancer allows existing requests to complete before the load balancer shifts traffic away from a deregistered or unhealthy instance.\nFor more information, see Configure Connection Draining in the Classic Load Balancers Guide .\n\nEnabled (boolean) -- [REQUIRED]Specifies whether connection draining is enabled for the load balancer.\n\nTimeout (integer) --The maximum time, in seconds, to keep the existing connections open before deregistering the instances.\n\n\n\nConnectionSettings (dict) --If enabled, the load balancer allows the connections to remain idle (no data is sent over the connection) for the specified duration.\nBy default, Elastic Load Balancing maintains a 60-second idle connection timeout for both front-end and back-end connections of your load balancer. For more information, see Configure Idle Connection Timeout in the Classic Load Balancers Guide .\n\nIdleTimeout (integer) -- [REQUIRED]The time, in seconds, that the connection is allowed to be idle (no data has been sent over the connection) before it is closed by the load balancer.\n\n\n\nAdditionalAttributes (list) --This parameter is reserved.\n\n(dict) --This data type is reserved.\n\nKey (string) --This parameter is reserved.\n\nValue (string) --This parameter is reserved.\n\n\n\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'LoadBalancerName': 'string',
    'LoadBalancerAttributes': {
        'CrossZoneLoadBalancing': {
            'Enabled': True|False
        },
        'AccessLog': {
            'Enabled': True|False,
            'S3BucketName': 'string',
            'EmitInterval': 123,
            'S3BucketPrefix': 'string'
        },
        'ConnectionDraining': {
            'Enabled': True|False,
            'Timeout': 123
        },
        'ConnectionSettings': {
            'IdleTimeout': 123
        },
        'AdditionalAttributes': [
            {
                'Key': 'string',
                'Value': 'string'
            },
        ]
    }
}


Response Structure

(dict) --
Contains the output of ModifyLoadBalancerAttributes.

LoadBalancerName (string) --
The name of the load balancer.

LoadBalancerAttributes (dict) --
Information about the load balancer attributes.

CrossZoneLoadBalancing (dict) --
If enabled, the load balancer routes the request traffic evenly across all instances regardless of the Availability Zones.
For more information, see Configure Cross-Zone Load Balancing in the Classic Load Balancers Guide .

Enabled (boolean) --
Specifies whether cross-zone load balancing is enabled for the load balancer.



AccessLog (dict) --
If enabled, the load balancer captures detailed information of all requests and delivers the information to the Amazon S3 bucket that you specify.
For more information, see Enable Access Logs in the Classic Load Balancers Guide .

Enabled (boolean) --
Specifies whether access logs are enabled for the load balancer.

S3BucketName (string) --
The name of the Amazon S3 bucket where the access logs are stored.

EmitInterval (integer) --
The interval for publishing the access logs. You can specify an interval of either 5 minutes or 60 minutes.
Default: 60 minutes

S3BucketPrefix (string) --
The logical hierarchy you created for your Amazon S3 bucket, for example my-bucket-prefix/prod . If the prefix is not provided, the log is placed at the root level of the bucket.



ConnectionDraining (dict) --
If enabled, the load balancer allows existing requests to complete before the load balancer shifts traffic away from a deregistered or unhealthy instance.
For more information, see Configure Connection Draining in the Classic Load Balancers Guide .

Enabled (boolean) --
Specifies whether connection draining is enabled for the load balancer.

Timeout (integer) --
The maximum time, in seconds, to keep the existing connections open before deregistering the instances.



ConnectionSettings (dict) --
If enabled, the load balancer allows the connections to remain idle (no data is sent over the connection) for the specified duration.
By default, Elastic Load Balancing maintains a 60-second idle connection timeout for both front-end and back-end connections of your load balancer. For more information, see Configure Idle Connection Timeout in the Classic Load Balancers Guide .

IdleTimeout (integer) --
The time, in seconds, that the connection is allowed to be idle (no data has been sent over the connection) before it is closed by the load balancer.



AdditionalAttributes (list) --
This parameter is reserved.

(dict) --
This data type is reserved.

Key (string) --
This parameter is reserved.

Value (string) --
This parameter is reserved.













Exceptions

ElasticLoadBalancing.Client.exceptions.AccessPointNotFoundException
ElasticLoadBalancing.Client.exceptions.LoadBalancerAttributeNotFoundException
ElasticLoadBalancing.Client.exceptions.InvalidConfigurationRequestException

Examples
This example enables cross-zone load balancing for the specified load balancer.
response = client.modify_load_balancer_attributes(
    LoadBalancerAttributes={
        'CrossZoneLoadBalancing': {
            'Enabled': True,
        },
    },
    LoadBalancerName='my-load-balancer',
)

print(response)


Expected Output:
{
    'LoadBalancerAttributes': {
        'CrossZoneLoadBalancing': {
            'Enabled': True,
        },
    },
    'LoadBalancerName': 'my-load-balancer',
    'ResponseMetadata': {
        '...': '...',
    },
}


This example enables connection draining for the specified load balancer.
response = client.modify_load_balancer_attributes(
    LoadBalancerAttributes={
        'ConnectionDraining': {
            'Enabled': True,
            'Timeout': 300,
        },
    },
    LoadBalancerName='my-load-balancer',
)

print(response)


Expected Output:
{
    'LoadBalancerAttributes': {
        'ConnectionDraining': {
            'Enabled': True,
            'Timeout': 300,
        },
    },
    'LoadBalancerName': 'my-load-balancer',
    'ResponseMetadata': {
        '...': '...',
    },
}



    :return: {
        'LoadBalancerName': 'string',
        'LoadBalancerAttributes': {
            'CrossZoneLoadBalancing': {
                'Enabled': True|False
            },
            'AccessLog': {
                'Enabled': True|False,
                'S3BucketName': 'string',
                'EmitInterval': 123,
                'S3BucketPrefix': 'string'
            },
            'ConnectionDraining': {
                'Enabled': True|False,
                'Timeout': 123
            },
            'ConnectionSettings': {
                'IdleTimeout': 123
            },
            'AdditionalAttributes': [
                {
                    'Key': 'string',
                    'Value': 'string'
                },
            ]
        }
    }
    
    
    :returns: 
    LoadBalancerName (string) -- [REQUIRED]
    The name of the load balancer.
    
    LoadBalancerAttributes (dict) -- [REQUIRED]
    The attributes for the load balancer.
    
    CrossZoneLoadBalancing (dict) --If enabled, the load balancer routes the request traffic evenly across all instances regardless of the Availability Zones.
    For more information, see Configure Cross-Zone Load Balancing in the Classic Load Balancers Guide .
    
    Enabled (boolean) -- [REQUIRED]Specifies whether cross-zone load balancing is enabled for the load balancer.
    
    
    
    AccessLog (dict) --If enabled, the load balancer captures detailed information of all requests and delivers the information to the Amazon S3 bucket that you specify.
    For more information, see Enable Access Logs in the Classic Load Balancers Guide .
    
    Enabled (boolean) -- [REQUIRED]Specifies whether access logs are enabled for the load balancer.
    
    S3BucketName (string) --The name of the Amazon S3 bucket where the access logs are stored.
    
    EmitInterval (integer) --The interval for publishing the access logs. You can specify an interval of either 5 minutes or 60 minutes.
    Default: 60 minutes
    
    S3BucketPrefix (string) --The logical hierarchy you created for your Amazon S3 bucket, for example my-bucket-prefix/prod . If the prefix is not provided, the log is placed at the root level of the bucket.
    
    
    
    ConnectionDraining (dict) --If enabled, the load balancer allows existing requests to complete before the load balancer shifts traffic away from a deregistered or unhealthy instance.
    For more information, see Configure Connection Draining in the Classic Load Balancers Guide .
    
    Enabled (boolean) -- [REQUIRED]Specifies whether connection draining is enabled for the load balancer.
    
    Timeout (integer) --The maximum time, in seconds, to keep the existing connections open before deregistering the instances.
    
    
    
    ConnectionSettings (dict) --If enabled, the load balancer allows the connections to remain idle (no data is sent over the connection) for the specified duration.
    By default, Elastic Load Balancing maintains a 60-second idle connection timeout for both front-end and back-end connections of your load balancer. For more information, see Configure Idle Connection Timeout in the Classic Load Balancers Guide .
    
    IdleTimeout (integer) -- [REQUIRED]The time, in seconds, that the connection is allowed to be idle (no data has been sent over the connection) before it is closed by the load balancer.
    
    
    
    AdditionalAttributes (list) --This parameter is reserved.
    
    (dict) --This data type is reserved.
    
    Key (string) --This parameter is reserved.
    
    Value (string) --This parameter is reserved.
    
    
    
    
    
    
    
    
    """
    pass

def register_instances_with_load_balancer(LoadBalancerName=None, Instances=None):
    """
    Adds the specified instances to the specified load balancer.
    The instance must be a running instance in the same network as the load balancer (EC2-Classic or the same VPC). If you have EC2-Classic instances and a load balancer in a VPC with ClassicLink enabled, you can link the EC2-Classic instances to that VPC and then register the linked EC2-Classic instances with the load balancer in the VPC.
    Note that RegisterInstanceWithLoadBalancer completes when the request has been registered. Instance registration takes a little time to complete. To check the state of the registered instances, use  DescribeLoadBalancers or  DescribeInstanceHealth .
    After the instance is registered, it starts receiving traffic and requests from the load balancer. Any instance that is not in one of the Availability Zones registered for the load balancer is moved to the OutOfService state. If an Availability Zone is added to the load balancer later, any instances registered with the load balancer move to the InService state.
    To deregister instances from a load balancer, use  DeregisterInstancesFromLoadBalancer .
    For more information, see Register or De-Register EC2 Instances in the Classic Load Balancers Guide .
    See also: AWS API Documentation
    
    Exceptions
    Examples
    This example registers the specified instance with the specified load balancer.
    Expected Output:
    
    :example: response = client.register_instances_with_load_balancer(
        LoadBalancerName='string',
        Instances=[
            {
                'InstanceId': 'string'
            },
        ]
    )
    
    
    :type LoadBalancerName: string
    :param LoadBalancerName: [REQUIRED]\nThe name of the load balancer.\n

    :type Instances: list
    :param Instances: [REQUIRED]\nThe IDs of the instances.\n\n(dict) --The ID of an EC2 instance.\n\nInstanceId (string) --The instance ID.\n\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'Instances': [
        {
            'InstanceId': 'string'
        },
    ]
}


Response Structure

(dict) --
Contains the output of RegisterInstancesWithLoadBalancer.

Instances (list) --
The updated list of instances for the load balancer.

(dict) --
The ID of an EC2 instance.

InstanceId (string) --
The instance ID.











Exceptions

ElasticLoadBalancing.Client.exceptions.AccessPointNotFoundException
ElasticLoadBalancing.Client.exceptions.InvalidEndPointException

Examples
This example registers the specified instance with the specified load balancer.
response = client.register_instances_with_load_balancer(
    Instances=[
        {
            'InstanceId': 'i-d6f6fae3',
        },
    ],
    LoadBalancerName='my-load-balancer',
)

print(response)


Expected Output:
{
    'Instances': [
        {
            'InstanceId': 'i-d6f6fae3',
        },
        {
            'InstanceId': 'i-207d9717',
        },
        {
            'InstanceId': 'i-afefb49b',
        },
    ],
    'ResponseMetadata': {
        '...': '...',
    },
}



    :return: {
        'Instances': [
            {
                'InstanceId': 'string'
            },
        ]
    }
    
    
    :returns: 
    ElasticLoadBalancing.Client.exceptions.AccessPointNotFoundException
    ElasticLoadBalancing.Client.exceptions.InvalidEndPointException
    
    """
    pass

def remove_tags(LoadBalancerNames=None, Tags=None):
    """
    Removes one or more tags from the specified load balancer.
    See also: AWS API Documentation
    
    Exceptions
    Examples
    This example removes the specified tag from the specified load balancer.
    Expected Output:
    
    :example: response = client.remove_tags(
        LoadBalancerNames=[
            'string',
        ],
        Tags=[
            {
                'Key': 'string'
            },
        ]
    )
    
    
    :type LoadBalancerNames: list
    :param LoadBalancerNames: [REQUIRED]\nThe name of the load balancer. You can specify a maximum of one load balancer name.\n\n(string) --\n\n

    :type Tags: list
    :param Tags: [REQUIRED]\nThe list of tag keys to remove.\n\n(dict) --The key of a tag.\n\nKey (string) --The name of the key.\n\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{}


Response Structure

(dict) --
Contains the output of RemoveTags.





Exceptions

ElasticLoadBalancing.Client.exceptions.AccessPointNotFoundException

Examples
This example removes the specified tag from the specified load balancer.
response = client.remove_tags(
    LoadBalancerNames=[
        'my-load-balancer',
    ],
    Tags=[
        {
            'Key': 'project',
        },
    ],
)

print(response)


Expected Output:
{
    'ResponseMetadata': {
        '...': '...',
    },
}



    :return: {}
    
    
    :returns: 
    ElasticLoadBalancing.Client.exceptions.AccessPointNotFoundException
    
    """
    pass

def set_load_balancer_listener_ssl_certificate(LoadBalancerName=None, LoadBalancerPort=None, SSLCertificateId=None):
    """
    Sets the certificate that terminates the specified listener\'s SSL connections. The specified certificate replaces any prior certificate that was used on the same load balancer and port.
    For more information about updating your SSL certificate, see Replace the SSL Certificate for Your Load Balancer in the Classic Load Balancers Guide .
    See also: AWS API Documentation
    
    Exceptions
    Examples
    This example replaces the existing SSL certificate for the specified HTTPS listener.
    Expected Output:
    
    :example: response = client.set_load_balancer_listener_ssl_certificate(
        LoadBalancerName='string',
        LoadBalancerPort=123,
        SSLCertificateId='string'
    )
    
    
    :type LoadBalancerName: string
    :param LoadBalancerName: [REQUIRED]\nThe name of the load balancer.\n

    :type LoadBalancerPort: integer
    :param LoadBalancerPort: [REQUIRED]\nThe port that uses the specified SSL certificate.\n

    :type SSLCertificateId: string
    :param SSLCertificateId: [REQUIRED]\nThe Amazon Resource Name (ARN) of the SSL certificate.\n

    :rtype: dict

ReturnsResponse Syntax
{}


Response Structure

(dict) --
Contains the output of SetLoadBalancerListenerSSLCertificate.





Exceptions

ElasticLoadBalancing.Client.exceptions.CertificateNotFoundException
ElasticLoadBalancing.Client.exceptions.AccessPointNotFoundException
ElasticLoadBalancing.Client.exceptions.ListenerNotFoundException
ElasticLoadBalancing.Client.exceptions.InvalidConfigurationRequestException
ElasticLoadBalancing.Client.exceptions.UnsupportedProtocolException

Examples
This example replaces the existing SSL certificate for the specified HTTPS listener.
response = client.set_load_balancer_listener_ssl_certificate(
    LoadBalancerName='my-load-balancer',
    LoadBalancerPort=443,
    SSLCertificateId='arn:aws:iam::123456789012:server-certificate/new-server-cert',
)

print(response)


Expected Output:
{
    'ResponseMetadata': {
        '...': '...',
    },
}



    :return: {}
    
    
    :returns: 
    ElasticLoadBalancing.Client.exceptions.CertificateNotFoundException
    ElasticLoadBalancing.Client.exceptions.AccessPointNotFoundException
    ElasticLoadBalancing.Client.exceptions.ListenerNotFoundException
    ElasticLoadBalancing.Client.exceptions.InvalidConfigurationRequestException
    ElasticLoadBalancing.Client.exceptions.UnsupportedProtocolException
    
    """
    pass

def set_load_balancer_policies_for_backend_server(LoadBalancerName=None, InstancePort=None, PolicyNames=None):
    """
    Replaces the set of policies associated with the specified port on which the EC2 instance is listening with a new set of policies. At this time, only the back-end server authentication policy type can be applied to the instance ports; this policy type is composed of multiple public key policies.
    Each time you use SetLoadBalancerPoliciesForBackendServer to enable the policies, use the PolicyNames parameter to list the policies that you want to enable.
    You can use  DescribeLoadBalancers or  DescribeLoadBalancerPolicies to verify that the policy is associated with the EC2 instance.
    For more information about enabling back-end instance authentication, see Configure Back-end Instance Authentication in the Classic Load Balancers Guide . For more information about Proxy Protocol, see Configure Proxy Protocol Support in the Classic Load Balancers Guide .
    See also: AWS API Documentation
    
    Exceptions
    Examples
    This example replaces the policies that are currently associated with the specified port.
    Expected Output:
    
    :example: response = client.set_load_balancer_policies_for_backend_server(
        LoadBalancerName='string',
        InstancePort=123,
        PolicyNames=[
            'string',
        ]
    )
    
    
    :type LoadBalancerName: string
    :param LoadBalancerName: [REQUIRED]\nThe name of the load balancer.\n

    :type InstancePort: integer
    :param InstancePort: [REQUIRED]\nThe port number associated with the EC2 instance.\n

    :type PolicyNames: list
    :param PolicyNames: [REQUIRED]\nThe names of the policies. If the list is empty, then all current polices are removed from the EC2 instance.\n\n(string) --\n\n

    :rtype: dict

ReturnsResponse Syntax
{}


Response Structure

(dict) --
Contains the output of SetLoadBalancerPoliciesForBackendServer.





Exceptions

ElasticLoadBalancing.Client.exceptions.AccessPointNotFoundException
ElasticLoadBalancing.Client.exceptions.PolicyNotFoundException
ElasticLoadBalancing.Client.exceptions.InvalidConfigurationRequestException

Examples
This example replaces the policies that are currently associated with the specified port.
response = client.set_load_balancer_policies_for_backend_server(
    InstancePort=80,
    LoadBalancerName='my-load-balancer',
    PolicyNames=[
        'my-ProxyProtocol-policy',
    ],
)

print(response)


Expected Output:
{
    'ResponseMetadata': {
        '...': '...',
    },
}



    :return: {}
    
    
    :returns: 
    ElasticLoadBalancing.Client.exceptions.AccessPointNotFoundException
    ElasticLoadBalancing.Client.exceptions.PolicyNotFoundException
    ElasticLoadBalancing.Client.exceptions.InvalidConfigurationRequestException
    
    """
    pass

def set_load_balancer_policies_of_listener(LoadBalancerName=None, LoadBalancerPort=None, PolicyNames=None):
    """
    Replaces the current set of policies for the specified load balancer port with the specified set of policies.
    To enable back-end server authentication, use  SetLoadBalancerPoliciesForBackendServer .
    For more information about setting policies, see Update the SSL Negotiation Configuration , Duration-Based Session Stickiness , and Application-Controlled Session Stickiness in the Classic Load Balancers Guide .
    See also: AWS API Documentation
    
    Exceptions
    Examples
    This example replaces the policies that are currently associated with the specified listener.
    Expected Output:
    
    :example: response = client.set_load_balancer_policies_of_listener(
        LoadBalancerName='string',
        LoadBalancerPort=123,
        PolicyNames=[
            'string',
        ]
    )
    
    
    :type LoadBalancerName: string
    :param LoadBalancerName: [REQUIRED]\nThe name of the load balancer.\n

    :type LoadBalancerPort: integer
    :param LoadBalancerPort: [REQUIRED]\nThe external port of the load balancer.\n

    :type PolicyNames: list
    :param PolicyNames: [REQUIRED]\nThe names of the policies. This list must include all policies to be enabled. If you omit a policy that is currently enabled, it is disabled. If the list is empty, all current policies are disabled.\n\n(string) --\n\n

    :rtype: dict

ReturnsResponse Syntax
{}


Response Structure

(dict) --
Contains the output of SetLoadBalancePoliciesOfListener.





Exceptions

ElasticLoadBalancing.Client.exceptions.AccessPointNotFoundException
ElasticLoadBalancing.Client.exceptions.PolicyNotFoundException
ElasticLoadBalancing.Client.exceptions.ListenerNotFoundException
ElasticLoadBalancing.Client.exceptions.InvalidConfigurationRequestException

Examples
This example replaces the policies that are currently associated with the specified listener.
response = client.set_load_balancer_policies_of_listener(
    LoadBalancerName='my-load-balancer',
    LoadBalancerPort=80,
    PolicyNames=[
        'my-SSLNegotiation-policy',
    ],
)

print(response)


Expected Output:
{
    'ResponseMetadata': {
        '...': '...',
    },
}



    :return: {}
    
    
    :returns: 
    ElasticLoadBalancing.Client.exceptions.AccessPointNotFoundException
    ElasticLoadBalancing.Client.exceptions.PolicyNotFoundException
    ElasticLoadBalancing.Client.exceptions.ListenerNotFoundException
    ElasticLoadBalancing.Client.exceptions.InvalidConfigurationRequestException
    
    """
    pass

