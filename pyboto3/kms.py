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

def can_paginate(operation_name=None):
    """
    Check if an operation can be paginated.
    
    :type operation_name: string
    :param operation_name: The operation name. This is the same name
            as the method name on the client. For example, if the
            method name is create_foo, and you'd normally invoke the
            operation as client.create_foo(**kwargs), if the
            create_foo operation can be paginated, you can use the
            call client.get_paginator('create_foo').

    """
    pass

def cancel_key_deletion(KeyId=None):
    """
    Cancels the deletion of a customer master key (CMK). When this operation is successful, the CMK is set to the Disabled state. To enable a CMK, use  EnableKey .
    For more information about scheduling and canceling deletion of a CMK, see Deleting Customer Master Keys in the AWS Key Management Service Developer Guide .
    See also: AWS API Documentation
    
    
    :example: response = client.cancel_key_deletion(
        KeyId='string'
    )
    
    
    :type KeyId: string
    :param KeyId: [REQUIRED]
            The unique identifier for the customer master key (CMK) for which to cancel deletion.
            To specify this value, use the unique key ID or the Amazon Resource Name (ARN) of the CMK. Examples:
            Unique key ID: 1234abcd-12ab-34cd-56ef-1234567890ab
            Key ARN: arn:aws:kms:us-east-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab
            To obtain the unique key ID and key ARN for a given CMK, use ListKeys or DescribeKey .
            

    :rtype: dict
    :return: {
        'KeyId': 'string'
    }
    
    
    """
    pass

def create_alias(AliasName=None, TargetKeyId=None):
    """
    Creates a display name for a customer master key. An alias can be used to identify a key and should be unique. The console enforces a one-to-one mapping between the alias and a key. An alias name can contain only alphanumeric characters, forward slashes (/), underscores (_), and dashes (-). An alias must start with the word "alias" followed by a forward slash (alias/). An alias that begins with "aws" after the forward slash (alias/aws...) is reserved by Amazon Web Services (AWS).
    The alias and the key it is mapped to must be in the same AWS account and the same region.
    To map an alias to a different key, call  UpdateAlias .
    See also: AWS API Documentation
    
    
    :example: response = client.create_alias(
        AliasName='string',
        TargetKeyId='string'
    )
    
    
    :type AliasName: string
    :param AliasName: [REQUIRED]
            String that contains the display name. The name must start with the word 'alias' followed by a forward slash (alias/). Aliases that begin with 'alias/AWS' are reserved.
            

    :type TargetKeyId: string
    :param TargetKeyId: [REQUIRED]
            An identifier of the key for which you are creating the alias. This value cannot be another alias but can be a globally unique identifier or a fully specified ARN to a key.
            Key ARN Example - arn:aws:kms:us-east-1:123456789012:key/12345678-1234-1234-1234-123456789012
            Globally Unique Key ID Example - 12345678-1234-1234-1234-123456789012
            

    """
    pass

def create_grant(KeyId=None, GranteePrincipal=None, RetiringPrincipal=None, Operations=None, Constraints=None, GrantTokens=None, Name=None):
    """
    Adds a grant to a key to specify who can use the key and under what conditions. Grants are alternate permission mechanisms to key policies.
    For more information about grants, see Grants in the AWS Key Management Service Developer Guide .
    See also: AWS API Documentation
    
    
    :example: response = client.create_grant(
        KeyId='string',
        GranteePrincipal='string',
        RetiringPrincipal='string',
        Operations=[
            'Decrypt'|'Encrypt'|'GenerateDataKey'|'GenerateDataKeyWithoutPlaintext'|'ReEncryptFrom'|'ReEncryptTo'|'CreateGrant'|'RetireGrant'|'DescribeKey',
        ],
        Constraints={
            'EncryptionContextSubset': {
                'string': 'string'
            },
            'EncryptionContextEquals': {
                'string': 'string'
            }
        },
        GrantTokens=[
            'string',
        ],
        Name='string'
    )
    
    
    :type KeyId: string
    :param KeyId: [REQUIRED]
            The unique identifier for the customer master key (CMK) that the grant applies to.
            To specify this value, use the globally unique key ID or the Amazon Resource Name (ARN) of the key. Examples:
            Globally unique key ID: 12345678-1234-1234-1234-123456789012
            Key ARN: arn:aws:kms:us-west-2:123456789012:key/12345678-1234-1234-1234-123456789012
            

    :type GranteePrincipal: string
    :param GranteePrincipal: [REQUIRED]
            The principal that is given permission to perform the operations that the grant permits.
            To specify the principal, use the Amazon Resource Name (ARN) of an AWS principal. Valid AWS principals include AWS accounts (root), IAM users, federated users, and assumed role users. For examples of the ARN syntax to use for specifying a principal, see AWS Identity and Access Management (IAM) in the Example ARNs section of the AWS General Reference .
            

    :type RetiringPrincipal: string
    :param RetiringPrincipal: The principal that is given permission to retire the grant by using RetireGrant operation.
            To specify the principal, use the Amazon Resource Name (ARN) of an AWS principal. Valid AWS principals include AWS accounts (root), IAM users, federated users, and assumed role users. For examples of the ARN syntax to use for specifying a principal, see AWS Identity and Access Management (IAM) in the Example ARNs section of the AWS General Reference .
            

    :type Operations: list
    :param Operations: A list of operations that the grant permits.
            (string) --
            

    :type Constraints: dict
    :param Constraints: The conditions under which the operations permitted by the grant are allowed.
            You can use this value to allow the operations permitted by the grant only when a specified encryption context is present. For more information, see Encryption Context in the AWS Key Management Service Developer Guide .
            EncryptionContextSubset (dict) --Contains a list of key-value pairs, a subset of which must be present in the encryption context of a subsequent operation permitted by the grant. When a subsequent operation permitted by the grant includes an encryption context that matches this list or is a subset of this list, the grant allows the operation. Otherwise, the operation is not allowed.
            (string) --
            (string) --
            
            EncryptionContextEquals (dict) --Contains a list of key-value pairs that must be present in the encryption context of a subsequent operation permitted by the grant. When a subsequent operation permitted by the grant includes an encryption context that matches this list, the grant allows the operation. Otherwise, the operation is not allowed.
            (string) --
            (string) --
            
            

    :type GrantTokens: list
    :param GrantTokens: A list of grant tokens.
            For more information, see Grant Tokens in the AWS Key Management Service Developer Guide .
            (string) --
            

    :type Name: string
    :param Name: A friendly name for identifying the grant. Use this value to prevent unintended creation of duplicate grants when retrying this request.
            When this value is absent, all CreateGrant requests result in a new grant with a unique GrantId even if all the supplied parameters are identical. This can result in unintended duplicates when you retry the CreateGrant request.
            When this value is present, you can retry a CreateGrant request with identical parameters; if the grant already exists, the original GrantId is returned without creating a new grant. Note that the returned grant token is unique with every CreateGrant request, even when a duplicate GrantId is returned. All grant tokens obtained in this way can be used interchangeably.
            

    :rtype: dict
    :return: {
        'GrantToken': 'string',
        'GrantId': 'string'
    }
    
    
    """
    pass

def create_key(Policy=None, Description=None, KeyUsage=None, Origin=None, BypassPolicyLockoutSafetyCheck=None):
    """
    Creates a customer master key (CMK).
    You can use a CMK to encrypt small amounts of data (4 KiB or less) directly, but CMKs are more commonly used to encrypt data encryption keys (DEKs), which are used to encrypt raw data. For more information about DEKs and the difference between CMKs and DEKs, see the following:
    See also: AWS API Documentation
    
    
    :example: response = client.create_key(
        Policy='string',
        Description='string',
        KeyUsage='ENCRYPT_DECRYPT',
        Origin='AWS_KMS'|'EXTERNAL',
        BypassPolicyLockoutSafetyCheck=True|False
    )
    
    
    :type Policy: string
    :param Policy: The key policy to attach to the CMK.
            If you specify a policy and do not set BypassPolicyLockoutSafetyCheck to true, the policy must meet the following criteria:
            It must allow the principal making the CreateKey request to make a subsequent PutKeyPolicy request on the CMK. This reduces the likelihood that the CMK becomes unmanageable. For more information, refer to the scenario in the Default Key Policy section in the AWS Key Management Service Developer Guide .
            The principal(s) specified in the key policy must exist and be visible to AWS KMS. When you create a new AWS principal (for example, an IAM user or role), you might need to enforce a delay before specifying the new principal in a key policy because the new principal might not immediately be visible to AWS KMS. For more information, see Changes that I make are not always immediately visible in the IAM User Guide .
            If you do not specify a policy, AWS KMS attaches a default key policy to the CMK. For more information, see Default Key Policy in the AWS Key Management Service Developer Guide .
            The policy size limit is 32 KiB (32768 bytes).
            

    :type Description: string
    :param Description: A description of the CMK.
            Use a description that helps you decide whether the CMK is appropriate for a task.
            

    :type KeyUsage: string
    :param KeyUsage: The intended use of the CMK.
            You can use CMKs only for symmetric encryption and decryption.
            

    :type Origin: string
    :param Origin: The source of the CMK's key material.
            The default is AWS_KMS , which means AWS KMS creates the key material. When this parameter is set to EXTERNAL , the request creates a CMK without key material so that you can import key material from your existing key management infrastructure. For more information about importing key material into AWS KMS, see Importing Key Material in the AWS Key Management Service Developer Guide .
            The CMK's Origin is immutable and is set when the CMK is created.
            

    :type BypassPolicyLockoutSafetyCheck: boolean
    :param BypassPolicyLockoutSafetyCheck: A flag to indicate whether to bypass the key policy lockout safety check.
            Warning
            Setting this value to true increases the likelihood that the CMK becomes unmanageable. Do not set this value to true indiscriminately.
            For more information, refer to the scenario in the Default Key Policy section in the AWS Key Management Service Developer Guide .
            Use this parameter only when you include a policy in the request and you intend to prevent the principal making the request from making a subsequent PutKeyPolicy request on the CMK.
            The default value is false.
            

    :rtype: dict
    :return: {
        'KeyMetadata': {
            'AWSAccountId': 'string',
            'KeyId': 'string',
            'Arn': 'string',
            'CreationDate': datetime(2015, 1, 1),
            'Enabled': True|False,
            'Description': 'string',
            'KeyUsage': 'ENCRYPT_DECRYPT',
            'KeyState': 'Enabled'|'Disabled'|'PendingDeletion'|'PendingImport',
            'DeletionDate': datetime(2015, 1, 1),
            'ValidTo': datetime(2015, 1, 1),
            'Origin': 'AWS_KMS'|'EXTERNAL',
            'ExpirationModel': 'KEY_MATERIAL_EXPIRES'|'KEY_MATERIAL_DOES_NOT_EXPIRE'
        }
    }
    
    
    :returns: 
    Policy (string) -- The key policy to attach to the CMK.
    If you specify a policy and do not set BypassPolicyLockoutSafetyCheck to true, the policy must meet the following criteria:
    
    It must allow the principal making the CreateKey request to make a subsequent  PutKeyPolicy request on the CMK. This reduces the likelihood that the CMK becomes unmanageable. For more information, refer to the scenario in the Default Key Policy section in the AWS Key Management Service Developer Guide .
    The principal(s) specified in the key policy must exist and be visible to AWS KMS. When you create a new AWS principal (for example, an IAM user or role), you might need to enforce a delay before specifying the new principal in a key policy because the new principal might not immediately be visible to AWS KMS. For more information, see Changes that I make are not always immediately visible in the IAM User Guide .
    
    If you do not specify a policy, AWS KMS attaches a default key policy to the CMK. For more information, see Default Key Policy in the AWS Key Management Service Developer Guide .
    The policy size limit is 32 KiB (32768 bytes).
    
    Description (string) -- A description of the CMK.
    Use a description that helps you decide whether the CMK is appropriate for a task.
    
    KeyUsage (string) -- The intended use of the CMK.
    You can use CMKs only for symmetric encryption and decryption.
    
    Origin (string) -- The source of the CMK's key material.
    The default is AWS_KMS , which means AWS KMS creates the key material. When this parameter is set to EXTERNAL , the request creates a CMK without key material so that you can import key material from your existing key management infrastructure. For more information about importing key material into AWS KMS, see Importing Key Material in the AWS Key Management Service Developer Guide .
    The CMK's Origin is immutable and is set when the CMK is created.
    
    BypassPolicyLockoutSafetyCheck (boolean) -- A flag to indicate whether to bypass the key policy lockout safety check.
    
    Warning
    Setting this value to true increases the likelihood that the CMK becomes unmanageable. Do not set this value to true indiscriminately.
    For more information, refer to the scenario in the Default Key Policy section in the AWS Key Management Service Developer Guide .
    
    Use this parameter only when you include a policy in the request and you intend to prevent the principal making the request from making a subsequent  PutKeyPolicy request on the CMK.
    The default value is false.
    
    
    """
    pass

def decrypt(CiphertextBlob=None, EncryptionContext=None, GrantTokens=None):
    """
    Decrypts ciphertext. Ciphertext is plaintext that has been previously encrypted by using any of the following functions:
    Note that if a caller has been granted access permissions to all keys (through, for example, IAM user policies that grant Decrypt permission on all resources), then ciphertext encrypted by using keys in other accounts where the key grants access to the caller can be decrypted. To remedy this, we recommend that you do not grant Decrypt access in an IAM user policy. Instead grant Decrypt access only in key policies. If you must grant Decrypt access in an IAM user policy, you should scope the resource to specific keys or to specific trusted accounts.
    See also: AWS API Documentation
    
    
    :example: response = client.decrypt(
        CiphertextBlob=b'bytes',
        EncryptionContext={
            'string': 'string'
        },
        GrantTokens=[
            'string',
        ]
    )
    
    
    :type CiphertextBlob: bytes
    :param CiphertextBlob: [REQUIRED]
            Ciphertext to be decrypted. The blob includes metadata.
            

    :type EncryptionContext: dict
    :param EncryptionContext: The encryption context. If this was specified in the Encrypt function, it must be specified here or the decryption operation will fail. For more information, see Encryption Context .
            (string) --
            (string) --
            

    :type GrantTokens: list
    :param GrantTokens: A list of grant tokens.
            For more information, see Grant Tokens in the AWS Key Management Service Developer Guide .
            (string) --
            

    :rtype: dict
    :return: {
        'KeyId': 'string',
        'Plaintext': b'bytes'
    }
    
    
    :returns: 
    CiphertextBlob (bytes) -- [REQUIRED]
    Ciphertext to be decrypted. The blob includes metadata.
    
    EncryptionContext (dict) -- The encryption context. If this was specified in the  Encrypt function, it must be specified here or the decryption operation will fail. For more information, see Encryption Context .
    
    (string) --
    (string) --
    
    
    
    
    GrantTokens (list) -- A list of grant tokens.
    For more information, see Grant Tokens in the AWS Key Management Service Developer Guide .
    
    (string) --
    
    
    
    """
    pass

def delete_alias(AliasName=None):
    """
    Deletes the specified alias. To map an alias to a different key, call  UpdateAlias .
    See also: AWS API Documentation
    
    
    :example: response = client.delete_alias(
        AliasName='string'
    )
    
    
    :type AliasName: string
    :param AliasName: [REQUIRED]
            The alias to be deleted. The name must start with the word 'alias' followed by a forward slash (alias/). Aliases that begin with 'alias/AWS' are reserved.
            

    """
    pass

def delete_imported_key_material(KeyId=None):
    """
    Deletes key material that you previously imported and makes the specified customer master key (CMK) unusable. For more information about importing key material into AWS KMS, see Importing Key Material in the AWS Key Management Service Developer Guide .
    When the specified CMK is in the PendingDeletion state, this operation does not change the CMK's state. Otherwise, it changes the CMK's state to PendingImport .
    After you delete key material, you can use  ImportKeyMaterial to reimport the same key material into the CMK.
    See also: AWS API Documentation
    
    
    :example: response = client.delete_imported_key_material(
        KeyId='string'
    )
    
    
    :type KeyId: string
    :param KeyId: [REQUIRED]
            The identifier of the CMK whose key material to delete. The CMK's Origin must be EXTERNAL .
            A valid identifier is the unique key ID or the Amazon Resource Name (ARN) of the CMK. Examples:
            Unique key ID: 1234abcd-12ab-34cd-56ef-1234567890ab
            Key ARN: arn:aws:kms:us-east-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab
            

    """
    pass

def describe_key(KeyId=None, GrantTokens=None):
    """
    Provides detailed information about the specified customer master key.
    See also: AWS API Documentation
    
    
    :example: response = client.describe_key(
        KeyId='string',
        GrantTokens=[
            'string',
        ]
    )
    
    
    :type KeyId: string
    :param KeyId: [REQUIRED]
            A unique identifier for the customer master key. This value can be a globally unique identifier, a fully specified ARN to either an alias or a key, or an alias name prefixed by 'alias/'.
            Key ARN Example - arn:aws:kms:us-east-1:123456789012:key/12345678-1234-1234-1234-123456789012
            Alias ARN Example - arn:aws:kms:us-east-1:123456789012:alias/MyAliasName
            Globally Unique Key ID Example - 12345678-1234-1234-1234-123456789012
            Alias Name Example - alias/MyAliasName
            

    :type GrantTokens: list
    :param GrantTokens: A list of grant tokens.
            For more information, see Grant Tokens in the AWS Key Management Service Developer Guide .
            (string) --
            

    :rtype: dict
    :return: {
        'KeyMetadata': {
            'AWSAccountId': 'string',
            'KeyId': 'string',
            'Arn': 'string',
            'CreationDate': datetime(2015, 1, 1),
            'Enabled': True|False,
            'Description': 'string',
            'KeyUsage': 'ENCRYPT_DECRYPT',
            'KeyState': 'Enabled'|'Disabled'|'PendingDeletion'|'PendingImport',
            'DeletionDate': datetime(2015, 1, 1),
            'ValidTo': datetime(2015, 1, 1),
            'Origin': 'AWS_KMS'|'EXTERNAL',
            'ExpirationModel': 'KEY_MATERIAL_EXPIRES'|'KEY_MATERIAL_DOES_NOT_EXPIRE'
        }
    }
    
    
    """
    pass

def disable_key(KeyId=None):
    """
    Sets the state of a customer master key (CMK) to disabled, thereby preventing its use for cryptographic operations. For more information about how key state affects the use of a CMK, see How Key State Affects the Use of a Customer Master Key in the AWS Key Management Service Developer Guide .
    See also: AWS API Documentation
    
    
    :example: response = client.disable_key(
        KeyId='string'
    )
    
    
    :type KeyId: string
    :param KeyId: [REQUIRED]
            A unique identifier for the CMK.
            Use the CMK's unique identifier or its Amazon Resource Name (ARN). For example:
            Unique ID: 1234abcd-12ab-34cd-56ef-1234567890ab
            ARN: arn:aws:kms:us-east-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab
            

    """
    pass

def disable_key_rotation(KeyId=None):
    """
    Disables rotation of the specified key.
    See also: AWS API Documentation
    
    
    :example: response = client.disable_key_rotation(
        KeyId='string'
    )
    
    
    :type KeyId: string
    :param KeyId: [REQUIRED]
            A unique identifier for the customer master key. This value can be a globally unique identifier or the fully specified ARN to a key.
            Key ARN Example - arn:aws:kms:us-east-1:123456789012:key/12345678-1234-1234-1234-123456789012
            Globally Unique Key ID Example - 12345678-1234-1234-1234-123456789012
            

    """
    pass

def enable_key(KeyId=None):
    """
    Marks a key as enabled, thereby permitting its use.
    See also: AWS API Documentation
    
    
    :example: response = client.enable_key(
        KeyId='string'
    )
    
    
    :type KeyId: string
    :param KeyId: [REQUIRED]
            A unique identifier for the customer master key. This value can be a globally unique identifier or the fully specified ARN to a key.
            Key ARN Example - arn:aws:kms:us-east-1:123456789012:key/12345678-1234-1234-1234-123456789012
            Globally Unique Key ID Example - 12345678-1234-1234-1234-123456789012
            

    """
    pass

def enable_key_rotation(KeyId=None):
    """
    Enables rotation of the specified customer master key.
    See also: AWS API Documentation
    
    
    :example: response = client.enable_key_rotation(
        KeyId='string'
    )
    
    
    :type KeyId: string
    :param KeyId: [REQUIRED]
            A unique identifier for the customer master key. This value can be a globally unique identifier or the fully specified ARN to a key.
            Key ARN Example - arn:aws:kms:us-east-1:123456789012:key/12345678-1234-1234-1234-123456789012
            Globally Unique Key ID Example - 12345678-1234-1234-1234-123456789012
            

    """
    pass

def encrypt(KeyId=None, Plaintext=None, EncryptionContext=None, GrantTokens=None):
    """
    Encrypts plaintext into ciphertext by using a customer master key. The Encrypt function has two primary use cases:
    Unless you are moving encrypted data from one region to another, you don't use this function to encrypt a generated data key within a region. You retrieve data keys already encrypted by calling the  GenerateDataKey or  GenerateDataKeyWithoutPlaintext function. Data keys don't need to be encrypted again by calling Encrypt .
    If you want to encrypt data locally in your application, you can use the GenerateDataKey function to return a plaintext data encryption key and a copy of the key encrypted under the customer master key (CMK) of your choosing.
    See also: AWS API Documentation
    
    
    :example: response = client.encrypt(
        KeyId='string',
        Plaintext=b'bytes',
        EncryptionContext={
            'string': 'string'
        },
        GrantTokens=[
            'string',
        ]
    )
    
    
    :type KeyId: string
    :param KeyId: [REQUIRED]
            A unique identifier for the customer master key. This value can be a globally unique identifier, a fully specified ARN to either an alias or a key, or an alias name prefixed by 'alias/'.
            Key ARN Example - arn:aws:kms:us-east-1:123456789012:key/12345678-1234-1234-1234-123456789012
            Alias ARN Example - arn:aws:kms:us-east-1:123456789012:alias/MyAliasName
            Globally Unique Key ID Example - 12345678-1234-1234-1234-123456789012
            Alias Name Example - alias/MyAliasName
            

    :type Plaintext: bytes
    :param Plaintext: [REQUIRED]
            Data to be encrypted.
            

    :type EncryptionContext: dict
    :param EncryptionContext: Name-value pair that specifies the encryption context to be used for authenticated encryption. If used here, the same value must be supplied to the Decrypt API or decryption will fail. For more information, see Encryption Context .
            (string) --
            (string) --
            

    :type GrantTokens: list
    :param GrantTokens: A list of grant tokens.
            For more information, see Grant Tokens in the AWS Key Management Service Developer Guide .
            (string) --
            

    :rtype: dict
    :return: {
        'CiphertextBlob': b'bytes',
        'KeyId': 'string'
    }
    
    
    :returns: 
    KeyId (string) -- [REQUIRED]
    A unique identifier for the customer master key. This value can be a globally unique identifier, a fully specified ARN to either an alias or a key, or an alias name prefixed by "alias/".
    
    Key ARN Example - arn:aws:kms:us-east-1:123456789012:key/12345678-1234-1234-1234-123456789012
    Alias ARN Example - arn:aws:kms:us-east-1:123456789012:alias/MyAliasName
    Globally Unique Key ID Example - 12345678-1234-1234-1234-123456789012
    Alias Name Example - alias/MyAliasName
    
    
    Plaintext (bytes) -- [REQUIRED]
    Data to be encrypted.
    
    EncryptionContext (dict) -- Name-value pair that specifies the encryption context to be used for authenticated encryption. If used here, the same value must be supplied to the Decrypt API or decryption will fail. For more information, see Encryption Context .
    
    (string) --
    (string) --
    
    
    
    
    GrantTokens (list) -- A list of grant tokens.
    For more information, see Grant Tokens in the AWS Key Management Service Developer Guide .
    
    (string) --
    
    
    
    """
    pass

def generate_data_key(KeyId=None, EncryptionContext=None, NumberOfBytes=None, KeySpec=None, GrantTokens=None):
    """
    Returns a data encryption key that you can use in your application to encrypt data locally.
    You must specify the customer master key (CMK) under which to generate the data key. You must also specify the length of the data key using either the KeySpec or NumberOfBytes field. You must specify one field or the other, but not both. For common key lengths (128-bit and 256-bit symmetric keys), we recommend that you use KeySpec .
    This operation returns a plaintext copy of the data key in the Plaintext field of the response, and an encrypted copy of the data key in the CiphertextBlob field. The data key is encrypted under the CMK specified in the KeyId field of the request.
    We recommend that you use the following pattern to encrypt data locally in your application:
    To decrypt data locally:
    To return only an encrypted copy of the data key, use  GenerateDataKeyWithoutPlaintext . To return an arbitrary unpredictable byte string, use  GenerateRandom .
    If you use the optional EncryptionContext field, you must store at least enough information to be able to reconstruct the full encryption context when you later send the ciphertext to the  Decrypt operation. It is a good practice to choose an encryption context that you can reconstruct on the fly to better secure the ciphertext. For more information, see Encryption Context in the AWS Key Management Service Developer Guide .
    See also: AWS API Documentation
    
    
    :example: response = client.generate_data_key(
        KeyId='string',
        EncryptionContext={
            'string': 'string'
        },
        NumberOfBytes=123,
        KeySpec='AES_256'|'AES_128',
        GrantTokens=[
            'string',
        ]
    )
    
    
    :type KeyId: string
    :param KeyId: [REQUIRED]
            The identifier of the CMK under which to generate and encrypt the data encryption key.
            A valid identifier is the unique key ID or the Amazon Resource Name (ARN) of the CMK, or the alias name or ARN of an alias that refers to the CMK. Examples:
            Unique key ID: 1234abcd-12ab-34cd-56ef-1234567890ab
            CMK ARN: arn:aws:kms:us-east-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab
            Alias name: alias/ExampleAlias
            Alias ARN: arn:aws:kms:us-east-2:111122223333:alias/ExampleAlias
            

    :type EncryptionContext: dict
    :param EncryptionContext: A set of key-value pairs that represents additional authenticated data.
            For more information, see Encryption Context in the AWS Key Management Service Developer Guide .
            (string) --
            (string) --
            

    :type NumberOfBytes: integer
    :param NumberOfBytes: The length of the data encryption key in bytes. For example, use the value 64 to generate a 512-bit data key (64 bytes is 512 bits). For common key lengths (128-bit and 256-bit symmetric keys), we recommend that you use the KeySpec field instead of this one.

    :type KeySpec: string
    :param KeySpec: The length of the data encryption key. Use AES_128 to generate a 128-bit symmetric key, or AES_256 to generate a 256-bit symmetric key.

    :type GrantTokens: list
    :param GrantTokens: A list of grant tokens.
            For more information, see Grant Tokens in the AWS Key Management Service Developer Guide .
            (string) --
            

    :rtype: dict
    :return: {
        'CiphertextBlob': b'bytes',
        'Plaintext': b'bytes',
        'KeyId': 'string'
    }
    
    
    :returns: 
    Use the  Decrypt operation to decrypt the encrypted data key into a plaintext copy of the data key.
    Use the plaintext data key to decrypt data locally, then erase the plaintext data key from memory.
    
    """
    pass

def generate_data_key_without_plaintext(KeyId=None, EncryptionContext=None, KeySpec=None, NumberOfBytes=None, GrantTokens=None):
    """
    Returns a data encryption key encrypted under a customer master key (CMK). This operation is identical to  GenerateDataKey but returns only the encrypted copy of the data key.
    This operation is useful in a system that has multiple components with different degrees of trust. For example, consider a system that stores encrypted data in containers. Each container stores the encrypted data and an encrypted copy of the data key. One component of the system, called the control plane , creates new containers. When it creates a new container, it uses this operation (GenerateDataKeyWithoutPlaintext ) to get an encrypted data key and then stores it in the container. Later, a different component of the system, called the data plane , puts encrypted data into the containers. To do this, it passes the encrypted data key to the  Decrypt operation, then uses the returned plaintext data key to encrypt data, and finally stores the encrypted data in the container. In this system, the control plane never sees the plaintext data key.
    See also: AWS API Documentation
    
    
    :example: response = client.generate_data_key_without_plaintext(
        KeyId='string',
        EncryptionContext={
            'string': 'string'
        },
        KeySpec='AES_256'|'AES_128',
        NumberOfBytes=123,
        GrantTokens=[
            'string',
        ]
    )
    
    
    :type KeyId: string
    :param KeyId: [REQUIRED]
            The identifier of the CMK under which to generate and encrypt the data encryption key.
            A valid identifier is the unique key ID or the Amazon Resource Name (ARN) of the CMK, or the alias name or ARN of an alias that refers to the CMK. Examples:
            Unique key ID: 1234abcd-12ab-34cd-56ef-1234567890ab
            CMK ARN: arn:aws:kms:us-east-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab
            Alias name: alias/ExampleAlias
            Alias ARN: arn:aws:kms:us-east-2:111122223333:alias/ExampleAlias
            

    :type EncryptionContext: dict
    :param EncryptionContext: A set of key-value pairs that represents additional authenticated data.
            For more information, see Encryption Context in the AWS Key Management Service Developer Guide .
            (string) --
            (string) --
            

    :type KeySpec: string
    :param KeySpec: The length of the data encryption key. Use AES_128 to generate a 128-bit symmetric key, or AES_256 to generate a 256-bit symmetric key.

    :type NumberOfBytes: integer
    :param NumberOfBytes: The length of the data encryption key in bytes. For example, use the value 64 to generate a 512-bit data key (64 bytes is 512 bits). For common key lengths (128-bit and 256-bit symmetric keys), we recommend that you use the KeySpec field instead of this one.

    :type GrantTokens: list
    :param GrantTokens: A list of grant tokens.
            For more information, see Grant Tokens in the AWS Key Management Service Developer Guide .
            (string) --
            

    :rtype: dict
    :return: {
        'CiphertextBlob': b'bytes',
        'KeyId': 'string'
    }
    
    
    """
    pass

def generate_presigned_url(ClientMethod=None, Params=None, ExpiresIn=None, HttpMethod=None):
    """
    Generate a presigned url given a client, its method, and arguments
    
    :type ClientMethod: string
    :param ClientMethod: The client method to presign for

    :type Params: dict
    :param Params: The parameters normally passed to
            ClientMethod.

    :type ExpiresIn: int
    :param ExpiresIn: The number of seconds the presigned url is valid
            for. By default it expires in an hour (3600 seconds)

    :type HttpMethod: string
    :param HttpMethod: The http method to use on the generated url. By
            default, the http method is whatever is used in the method's model.

    """
    pass

def generate_random(NumberOfBytes=None):
    """
    Generates an unpredictable byte string.
    See also: AWS API Documentation
    
    
    :example: response = client.generate_random(
        NumberOfBytes=123
    )
    
    
    :type NumberOfBytes: integer
    :param NumberOfBytes: The length of the byte string.

    :rtype: dict
    :return: {
        'Plaintext': b'bytes'
    }
    
    
    """
    pass

def get_key_policy(KeyId=None, PolicyName=None):
    """
    Retrieves a policy attached to the specified key.
    See also: AWS API Documentation
    
    
    :example: response = client.get_key_policy(
        KeyId='string',
        PolicyName='string'
    )
    
    
    :type KeyId: string
    :param KeyId: [REQUIRED]
            A unique identifier for the customer master key. This value can be a globally unique identifier or the fully specified ARN to a key.
            Key ARN Example - arn:aws:kms:us-east-1:123456789012:key/12345678-1234-1234-1234-123456789012
            Globally Unique Key ID Example - 12345678-1234-1234-1234-123456789012
            

    :type PolicyName: string
    :param PolicyName: [REQUIRED]
            String that contains the name of the policy. Currently, this must be 'default'. Policy names can be discovered by calling ListKeyPolicies .
            

    :rtype: dict
    :return: {
        'Policy': 'string'
    }
    
    
    """
    pass

def get_key_rotation_status(KeyId=None):
    """
    Retrieves a Boolean value that indicates whether key rotation is enabled for the specified key.
    See also: AWS API Documentation
    
    
    :example: response = client.get_key_rotation_status(
        KeyId='string'
    )
    
    
    :type KeyId: string
    :param KeyId: [REQUIRED]
            A unique identifier for the customer master key. This value can be a globally unique identifier or the fully specified ARN to a key.
            Key ARN Example - arn:aws:kms:us-east-1:123456789012:key/12345678-1234-1234-1234-123456789012
            Globally Unique Key ID Example - 12345678-1234-1234-1234-123456789012
            

    :rtype: dict
    :return: {
        'KeyRotationEnabled': True|False
    }
    
    
    """
    pass

def get_paginator(operation_name=None):
    """
    Create a paginator for an operation.
    
    :type operation_name: string
    :param operation_name: The operation name. This is the same name
            as the method name on the client. For example, if the
            method name is create_foo, and you'd normally invoke the
            operation as client.create_foo(**kwargs), if the
            create_foo operation can be paginated, you can use the
            call client.get_paginator('create_foo').

    :rtype: L{botocore.paginate.Paginator}
    """
    pass

def get_parameters_for_import(KeyId=None, WrappingAlgorithm=None, WrappingKeySpec=None):
    """
    Returns the items you need in order to import key material into AWS KMS from your existing key management infrastructure. For more information about importing key material into AWS KMS, see Importing Key Material in the AWS Key Management Service Developer Guide .
    You must specify the key ID of the customer master key (CMK) into which you will import key material. This CMK's Origin must be EXTERNAL . You must also specify the wrapping algorithm and type of wrapping key (public key) that you will use to encrypt the key material.
    This operation returns a public key and an import token. Use the public key to encrypt the key material. Store the import token to send with a subsequent  ImportKeyMaterial request. The public key and import token from the same response must be used together. These items are valid for 24 hours, after which they cannot be used for a subsequent  ImportKeyMaterial request. To retrieve new ones, send another GetParametersForImport request.
    See also: AWS API Documentation
    
    
    :example: response = client.get_parameters_for_import(
        KeyId='string',
        WrappingAlgorithm='RSAES_PKCS1_V1_5'|'RSAES_OAEP_SHA_1'|'RSAES_OAEP_SHA_256',
        WrappingKeySpec='RSA_2048'
    )
    
    
    :type KeyId: string
    :param KeyId: [REQUIRED]
            The identifier of the CMK into which you will import key material. The CMK's Origin must be EXTERNAL .
            A valid identifier is the unique key ID or the Amazon Resource Name (ARN) of the CMK. Examples:
            Unique key ID: 1234abcd-12ab-34cd-56ef-1234567890ab
            Key ARN: arn:aws:kms:us-east-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab
            

    :type WrappingAlgorithm: string
    :param WrappingAlgorithm: [REQUIRED]
            The algorithm you will use to encrypt the key material before importing it with ImportKeyMaterial . For more information, see Encrypt the Key Material in the AWS Key Management Service Developer Guide .
            

    :type WrappingKeySpec: string
    :param WrappingKeySpec: [REQUIRED]
            The type of wrapping key (public key) to return in the response. Only 2048-bit RSA public keys are supported.
            

    :rtype: dict
    :return: {
        'KeyId': 'string',
        'ImportToken': b'bytes',
        'PublicKey': b'bytes',
        'ParametersValidTo': datetime(2015, 1, 1)
    }
    
    
    """
    pass

def get_waiter():
    """
    
    """
    pass

def import_key_material(KeyId=None, ImportToken=None, EncryptedKeyMaterial=None, ValidTo=None, ExpirationModel=None):
    """
    Imports key material into an AWS KMS customer master key (CMK) from your existing key management infrastructure. For more information about importing key material into AWS KMS, see Importing Key Material in the AWS Key Management Service Developer Guide .
    You must specify the key ID of the CMK to import the key material into. This CMK's Origin must be EXTERNAL . You must also send an import token and the encrypted key material. Send the import token that you received in the same  GetParametersForImport response that contained the public key that you used to encrypt the key material. You must also specify whether the key material expires and if so, when. When the key material expires, AWS KMS deletes the key material and the CMK becomes unusable. To use the CMK again, you can reimport the same key material. If you set an expiration date, you can change it only by reimporting the same key material and specifying a new expiration date.
    When this operation is successful, the specified CMK's key state changes to Enabled , and you can use the CMK.
    After you successfully import key material into a CMK, you can reimport the same key material into that CMK, but you cannot import different key material.
    See also: AWS API Documentation
    
    
    :example: response = client.import_key_material(
        KeyId='string',
        ImportToken=b'bytes',
        EncryptedKeyMaterial=b'bytes',
        ValidTo=datetime(2015, 1, 1),
        ExpirationModel='KEY_MATERIAL_EXPIRES'|'KEY_MATERIAL_DOES_NOT_EXPIRE'
    )
    
    
    :type KeyId: string
    :param KeyId: [REQUIRED]
            The identifier of the CMK to import the key material into. The CMK's Origin must be EXTERNAL .
            A valid identifier is the unique key ID or the Amazon Resource Name (ARN) of the CMK. Examples:
            Unique key ID: 1234abcd-12ab-34cd-56ef-1234567890ab
            Key ARN: arn:aws:kms:us-east-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab
            

    :type ImportToken: bytes
    :param ImportToken: [REQUIRED]
            The import token that you received in the response to a previous GetParametersForImport request. It must be from the same response that contained the public key that you used to encrypt the key material.
            

    :type EncryptedKeyMaterial: bytes
    :param EncryptedKeyMaterial: [REQUIRED]
            The encrypted key material to import. It must be encrypted with the public key that you received in the response to a previous GetParametersForImport request, using the wrapping algorithm that you specified in that request.
            

    :type ValidTo: datetime
    :param ValidTo: The time at which the imported key material expires. When the key material expires, AWS KMS deletes the key material and the CMK becomes unusable. You must omit this parameter when the ExpirationModel parameter is set to KEY_MATERIAL_DOES_NOT_EXPIRE . Otherwise it is required.

    :type ExpirationModel: string
    :param ExpirationModel: Specifies whether the key material expires. The default is KEY_MATERIAL_EXPIRES , in which case you must include the ValidTo parameter. When this parameter is set to KEY_MATERIAL_DOES_NOT_EXPIRE , you must omit the ValidTo parameter.

    :rtype: dict
    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def list_aliases(Limit=None, Marker=None):
    """
    Lists all of the key aliases in the account.
    See also: AWS API Documentation
    
    
    :example: response = client.list_aliases(
        Limit=123,
        Marker='string'
    )
    
    
    :type Limit: integer
    :param Limit: When paginating results, specify the maximum number of items to return in the response. If additional items exist beyond the number you specify, the Truncated element in the response is set to true.
            This value is optional. If you include a value, it must be between 1 and 100, inclusive. If you do not include a value, it defaults to 50.
            

    :type Marker: string
    :param Marker: Use this parameter only when paginating results and only in a subsequent request after you receive a response with truncated results. Set it to the value of NextMarker from the response you just received.

    :rtype: dict
    :return: {
        'Aliases': [
            {
                'AliasName': 'string',
                'AliasArn': 'string',
                'TargetKeyId': 'string'
            },
        ],
        'NextMarker': 'string',
        'Truncated': True|False
    }
    
    
    """
    pass

def list_grants(Limit=None, Marker=None, KeyId=None):
    """
    List the grants for a specified key.
    See also: AWS API Documentation
    
    
    :example: response = client.list_grants(
        Limit=123,
        Marker='string',
        KeyId='string'
    )
    
    
    :type Limit: integer
    :param Limit: When paginating results, specify the maximum number of items to return in the response. If additional items exist beyond the number you specify, the Truncated element in the response is set to true.
            This value is optional. If you include a value, it must be between 1 and 100, inclusive. If you do not include a value, it defaults to 50.
            

    :type Marker: string
    :param Marker: Use this parameter only when paginating results and only in a subsequent request after you receive a response with truncated results. Set it to the value of NextMarker from the response you just received.

    :type KeyId: string
    :param KeyId: [REQUIRED]
            A unique identifier for the customer master key. This value can be a globally unique identifier or the fully specified ARN to a key.
            Key ARN Example - arn:aws:kms:us-east-1:123456789012:key/12345678-1234-1234-1234-123456789012
            Globally Unique Key ID Example - 12345678-1234-1234-1234-123456789012
            

    :rtype: dict
    :return: {
        'Grants': [
            {
                'KeyId': 'string',
                'GrantId': 'string',
                'Name': 'string',
                'CreationDate': datetime(2015, 1, 1),
                'GranteePrincipal': 'string',
                'RetiringPrincipal': 'string',
                'IssuingAccount': 'string',
                'Operations': [
                    'Decrypt'|'Encrypt'|'GenerateDataKey'|'GenerateDataKeyWithoutPlaintext'|'ReEncryptFrom'|'ReEncryptTo'|'CreateGrant'|'RetireGrant'|'DescribeKey',
                ],
                'Constraints': {
                    'EncryptionContextSubset': {
                        'string': 'string'
                    },
                    'EncryptionContextEquals': {
                        'string': 'string'
                    }
                }
            },
        ],
        'NextMarker': 'string',
        'Truncated': True|False
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def list_key_policies(KeyId=None, Limit=None, Marker=None):
    """
    Retrieves a list of policies attached to a key.
    See also: AWS API Documentation
    
    
    :example: response = client.list_key_policies(
        KeyId='string',
        Limit=123,
        Marker='string'
    )
    
    
    :type KeyId: string
    :param KeyId: [REQUIRED]
            A unique identifier for the customer master key (CMK). You can use the unique key ID or the Amazon Resource Name (ARN) of the CMK. Examples:
            Unique key ID: 1234abcd-12ab-34cd-56ef-1234567890ab
            Key ARN: arn:aws:kms:us-east-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab
            

    :type Limit: integer
    :param Limit: When paginating results, specify the maximum number of items to return in the response. If additional items exist beyond the number you specify, the Truncated element in the response is set to true.
            This value is optional. If you include a value, it must be between 1 and 1000, inclusive. If you do not include a value, it defaults to 100.
            Currently only 1 policy can be attached to a key.
            

    :type Marker: string
    :param Marker: Use this parameter only when paginating results and only in a subsequent request after you receive a response with truncated results. Set it to the value of NextMarker from the response you just received.

    :rtype: dict
    :return: {
        'PolicyNames': [
            'string',
        ],
        'NextMarker': 'string',
        'Truncated': True|False
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def list_keys(Limit=None, Marker=None):
    """
    Lists the customer master keys.
    See also: AWS API Documentation
    
    
    :example: response = client.list_keys(
        Limit=123,
        Marker='string'
    )
    
    
    :type Limit: integer
    :param Limit: When paginating results, specify the maximum number of items to return in the response. If additional items exist beyond the number you specify, the Truncated element in the response is set to true.
            This value is optional. If you include a value, it must be between 1 and 1000, inclusive. If you do not include a value, it defaults to 100.
            

    :type Marker: string
    :param Marker: Use this parameter only when paginating results and only in a subsequent request after you receive a response with truncated results. Set it to the value of NextMarker from the response you just received.

    :rtype: dict
    :return: {
        'Keys': [
            {
                'KeyId': 'string',
                'KeyArn': 'string'
            },
        ],
        'NextMarker': 'string',
        'Truncated': True|False
    }
    
    
    """
    pass

def list_retirable_grants(Limit=None, Marker=None, RetiringPrincipal=None):
    """
    Returns a list of all grants for which the grant's RetiringPrincipal matches the one specified.
    A typical use is to list all grants that you are able to retire. To retire a grant, use  RetireGrant .
    See also: AWS API Documentation
    
    
    :example: response = client.list_retirable_grants(
        Limit=123,
        Marker='string',
        RetiringPrincipal='string'
    )
    
    
    :type Limit: integer
    :param Limit: When paginating results, specify the maximum number of items to return in the response. If additional items exist beyond the number you specify, the Truncated element in the response is set to true.
            This value is optional. If you include a value, it must be between 1 and 100, inclusive. If you do not include a value, it defaults to 50.
            

    :type Marker: string
    :param Marker: Use this parameter only when paginating results and only in a subsequent request after you receive a response with truncated results. Set it to the value of NextMarker from the response you just received.

    :type RetiringPrincipal: string
    :param RetiringPrincipal: [REQUIRED]
            The retiring principal for which to list grants.
            To specify the retiring principal, use the Amazon Resource Name (ARN) of an AWS principal. Valid AWS principals include AWS accounts (root), IAM users, federated users, and assumed role users. For examples of the ARN syntax for specifying a principal, see AWS Identity and Access Management (IAM) in the Example ARNs section of the Amazon Web Services General Reference .
            

    :rtype: dict
    :return: {
        'Grants': [
            {
                'KeyId': 'string',
                'GrantId': 'string',
                'Name': 'string',
                'CreationDate': datetime(2015, 1, 1),
                'GranteePrincipal': 'string',
                'RetiringPrincipal': 'string',
                'IssuingAccount': 'string',
                'Operations': [
                    'Decrypt'|'Encrypt'|'GenerateDataKey'|'GenerateDataKeyWithoutPlaintext'|'ReEncryptFrom'|'ReEncryptTo'|'CreateGrant'|'RetireGrant'|'DescribeKey',
                ],
                'Constraints': {
                    'EncryptionContextSubset': {
                        'string': 'string'
                    },
                    'EncryptionContextEquals': {
                        'string': 'string'
                    }
                }
            },
        ],
        'NextMarker': 'string',
        'Truncated': True|False
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def put_key_policy(KeyId=None, PolicyName=None, Policy=None, BypassPolicyLockoutSafetyCheck=None):
    """
    Attaches a key policy to the specified customer master key (CMK).
    For more information about key policies, see Key Policies in the AWS Key Management Service Developer Guide .
    See also: AWS API Documentation
    
    
    :example: response = client.put_key_policy(
        KeyId='string',
        PolicyName='string',
        Policy='string',
        BypassPolicyLockoutSafetyCheck=True|False
    )
    
    
    :type KeyId: string
    :param KeyId: [REQUIRED]
            A unique identifier for the CMK.
            Use the CMK's unique identifier or its Amazon Resource Name (ARN). For example:
            Unique ID: 1234abcd-12ab-34cd-56ef-1234567890ab
            ARN: arn:aws:kms:us-east-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab
            

    :type PolicyName: string
    :param PolicyName: [REQUIRED]
            The name of the key policy.
            This value must be default .
            

    :type Policy: string
    :param Policy: [REQUIRED]
            The key policy to attach to the CMK.
            If you do not set BypassPolicyLockoutSafetyCheck to true, the policy must meet the following criteria:
            It must allow the principal making the PutKeyPolicy request to make a subsequent PutKeyPolicy request on the CMK. This reduces the likelihood that the CMK becomes unmanageable. For more information, refer to the scenario in the Default Key Policy section in the AWS Key Management Service Developer Guide .
            The principal(s) specified in the key policy must exist and be visible to AWS KMS. When you create a new AWS principal (for example, an IAM user or role), you might need to enforce a delay before specifying the new principal in a key policy because the new principal might not immediately be visible to AWS KMS. For more information, see Changes that I make are not always immediately visible in the IAM User Guide .
            The policy size limit is 32 KiB (32768 bytes).
            

    :type BypassPolicyLockoutSafetyCheck: boolean
    :param BypassPolicyLockoutSafetyCheck: A flag to indicate whether to bypass the key policy lockout safety check.
            Warning
            Setting this value to true increases the likelihood that the CMK becomes unmanageable. Do not set this value to true indiscriminately.
            For more information, refer to the scenario in the Default Key Policy section in the AWS Key Management Service Developer Guide .
            Use this parameter only when you intend to prevent the principal making the request from making a subsequent PutKeyPolicy request on the CMK.
            The default value is false.
            

    """
    pass

def re_encrypt(CiphertextBlob=None, SourceEncryptionContext=None, DestinationKeyId=None, DestinationEncryptionContext=None, GrantTokens=None):
    """
    Encrypts data on the server side with a new customer master key (CMK) without exposing the plaintext of the data on the client side. The data is first decrypted and then reencrypted. You can also use this operation to change the encryption context of a ciphertext.
    Unlike other operations, ReEncrypt is authorized twice, once as ReEncryptFrom on the source CMK and once as ReEncryptTo on the destination CMK. We recommend that you include the "kms:ReEncrypt*" permission in your key policies to permit reencryption from or to the CMK. This permission is automatically included in the key policy when you create a CMK through the console, but you must include it manually when you create a CMK programmatically or when you set a key policy with the  PutKeyPolicy operation.
    See also: AWS API Documentation
    
    
    :example: response = client.re_encrypt(
        CiphertextBlob=b'bytes',
        SourceEncryptionContext={
            'string': 'string'
        },
        DestinationKeyId='string',
        DestinationEncryptionContext={
            'string': 'string'
        },
        GrantTokens=[
            'string',
        ]
    )
    
    
    :type CiphertextBlob: bytes
    :param CiphertextBlob: [REQUIRED]
            Ciphertext of the data to reencrypt.
            

    :type SourceEncryptionContext: dict
    :param SourceEncryptionContext: Encryption context used to encrypt and decrypt the data specified in the CiphertextBlob parameter.
            (string) --
            (string) --
            

    :type DestinationKeyId: string
    :param DestinationKeyId: [REQUIRED]
            A unique identifier for the CMK to use to reencrypt the data. This value can be a globally unique identifier, a fully specified ARN to either an alias or a key, or an alias name prefixed by 'alias/'.
            Key ARN Example - arn:aws:kms:us-east-1:123456789012:key/12345678-1234-1234-1234-123456789012
            Alias ARN Example - arn:aws:kms:us-east-1:123456789012:alias/MyAliasName
            Globally Unique Key ID Example - 12345678-1234-1234-1234-123456789012
            Alias Name Example - alias/MyAliasName
            

    :type DestinationEncryptionContext: dict
    :param DestinationEncryptionContext: Encryption context to use when the data is reencrypted.
            (string) --
            (string) --
            

    :type GrantTokens: list
    :param GrantTokens: A list of grant tokens.
            For more information, see Grant Tokens in the AWS Key Management Service Developer Guide .
            (string) --
            

    :rtype: dict
    :return: {
        'CiphertextBlob': b'bytes',
        'SourceKeyId': 'string',
        'KeyId': 'string'
    }
    
    
    """
    pass

def retire_grant(GrantToken=None, KeyId=None, GrantId=None):
    """
    Retires a grant. To clean up, you can retire a grant when you're done using it. You should revoke a grant when you intend to actively deny operations that depend on it. The following are permitted to call this API:
    You must identify the grant to retire by its grant token or by a combination of the grant ID and the Amazon Resource Name (ARN) of the customer master key (CMK). A grant token is a unique variable-length base64-encoded string. A grant ID is a 64 character unique identifier of a grant. The  CreateGrant operation returns both.
    See also: AWS API Documentation
    
    
    :example: response = client.retire_grant(
        GrantToken='string',
        KeyId='string',
        GrantId='string'
    )
    
    
    :type GrantToken: string
    :param GrantToken: Token that identifies the grant to be retired.

    :type KeyId: string
    :param KeyId: The Amazon Resource Name of the CMK associated with the grant. Example:
            arn:aws:kms:us-east-2:444455556666:key/1234abcd-12ab-34cd-56ef-1234567890ab
            

    :type GrantId: string
    :param GrantId: Unique identifier of the grant to retire. The grant ID is returned in the response to a CreateGrant operation.
            Grant ID Example - 0123456789012345678901234567890123456789012345678901234567890123
            

    :returns: 
    GrantToken (string) -- Token that identifies the grant to be retired.
    KeyId (string) -- The Amazon Resource Name of the CMK associated with the grant. Example:
    
    arn:aws:kms:us-east-2:444455556666:key/1234abcd-12ab-34cd-56ef-1234567890ab
    
    
    GrantId (string) -- Unique identifier of the grant to retire. The grant ID is returned in the response to a CreateGrant operation.
    
    Grant ID Example - 0123456789012345678901234567890123456789012345678901234567890123
    
    
    
    """
    pass

def revoke_grant(KeyId=None, GrantId=None):
    """
    Revokes a grant. You can revoke a grant to actively deny operations that depend on it.
    See also: AWS API Documentation
    
    
    :example: response = client.revoke_grant(
        KeyId='string',
        GrantId='string'
    )
    
    
    :type KeyId: string
    :param KeyId: [REQUIRED]
            A unique identifier for the customer master key associated with the grant. This value can be a globally unique identifier or the fully specified ARN to a key.
            Key ARN Example - arn:aws:kms:us-east-1:123456789012:key/12345678-1234-1234-1234-123456789012
            Globally Unique Key ID Example - 12345678-1234-1234-1234-123456789012
            

    :type GrantId: string
    :param GrantId: [REQUIRED]
            Identifier of the grant to be revoked.
            

    """
    pass

def schedule_key_deletion(KeyId=None, PendingWindowInDays=None):
    """
    Schedules the deletion of a customer master key (CMK). You may provide a waiting period, specified in days, before deletion occurs. If you do not provide a waiting period, the default period of 30 days is used. When this operation is successful, the state of the CMK changes to PendingDeletion . Before the waiting period ends, you can use  CancelKeyDeletion to cancel the deletion of the CMK. After the waiting period ends, AWS KMS deletes the CMK and all AWS KMS data associated with it, including all aliases that refer to it.
    For more information about scheduling a CMK for deletion, see Deleting Customer Master Keys in the AWS Key Management Service Developer Guide .
    See also: AWS API Documentation
    
    
    :example: response = client.schedule_key_deletion(
        KeyId='string',
        PendingWindowInDays=123
    )
    
    
    :type KeyId: string
    :param KeyId: [REQUIRED]
            The unique identifier for the customer master key (CMK) to delete.
            To specify this value, use the unique key ID or the Amazon Resource Name (ARN) of the CMK. Examples:
            Unique key ID: 1234abcd-12ab-34cd-56ef-1234567890ab
            Key ARN: arn:aws:kms:us-east-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab
            To obtain the unique key ID and key ARN for a given CMK, use ListKeys or DescribeKey .
            

    :type PendingWindowInDays: integer
    :param PendingWindowInDays: The waiting period, specified in number of days. After the waiting period ends, AWS KMS deletes the customer master key (CMK).
            This value is optional. If you include a value, it must be between 7 and 30, inclusive. If you do not include a value, it defaults to 30.
            

    :rtype: dict
    :return: {
        'KeyId': 'string',
        'DeletionDate': datetime(2015, 1, 1)
    }
    
    
    """
    pass

def update_alias(AliasName=None, TargetKeyId=None):
    """
    Updates an alias to map it to a different key.
    An alias is not a property of a key. Therefore, an alias can be mapped to and unmapped from an existing key without changing the properties of the key.
    An alias name can contain only alphanumeric characters, forward slashes (/), underscores (_), and dashes (-). An alias must start with the word "alias" followed by a forward slash (alias/). An alias that begins with "aws" after the forward slash (alias/aws...) is reserved by Amazon Web Services (AWS).
    The alias and the key it is mapped to must be in the same AWS account and the same region.
    See also: AWS API Documentation
    
    
    :example: response = client.update_alias(
        AliasName='string',
        TargetKeyId='string'
    )
    
    
    :type AliasName: string
    :param AliasName: [REQUIRED]
            String that contains the name of the alias to be modified. The name must start with the word 'alias' followed by a forward slash (alias/). Aliases that begin with 'alias/aws' are reserved.
            

    :type TargetKeyId: string
    :param TargetKeyId: [REQUIRED]
            Unique identifier of the customer master key to be mapped to the alias. This value can be a globally unique identifier or the fully specified ARN of a key.
            Key ARN Example - arn:aws:kms:us-east-1:123456789012:key/12345678-1234-1234-1234-123456789012
            Globally Unique Key ID Example - 12345678-1234-1234-1234-123456789012
            You can call ListAliases to verify that the alias is mapped to the correct TargetKeyId .
            

    """
    pass

def update_key_description(KeyId=None, Description=None):
    """
    Updates the description of a customer master key (CMK).
    See also: AWS API Documentation
    
    
    :example: response = client.update_key_description(
        KeyId='string',
        Description='string'
    )
    
    
    :type KeyId: string
    :param KeyId: [REQUIRED]
            A unique identifier for the CMK. This value can be a globally unique identifier or the fully specified ARN to a key.
            Key ARN Example - arn:aws:kms:us-east-1:123456789012:key/12345678-1234-1234-1234-123456789012
            Globally Unique Key ID Example - 12345678-1234-1234-1234-123456789012
            

    :type Description: string
    :param Description: [REQUIRED]
            New description for the CMK.
            

    """
    pass

