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

def abort_multipart_upload(accountId=None, vaultName=None, uploadId=None):
    """
    This operation aborts a multipart upload identified by the upload ID.
    After the Abort Multipart Upload request succeeds, you cannot upload any more parts to the multipart upload or complete the multipart upload. Aborting a completed upload fails. However, aborting an already-aborted upload will succeed, for a short time. For more information about uploading a part and completing a multipart upload, see  UploadMultipartPart and  CompleteMultipartUpload .
    This operation is idempotent.
    An AWS account has full permission to perform all operations (actions). However, AWS Identity and Access Management (IAM) users don\'t have any permissions by default. You must grant them explicit permission to perform specific actions. For more information, see Access Control Using AWS Identity and Access Management (IAM) .
    For conceptual information and underlying REST API, see Working with Archives in Amazon S3 Glacier and Abort Multipart Upload in the Amazon Glacier Developer Guide .
    See also: AWS API Documentation
    
    Exceptions
    Examples
    The example deletes an in-progress multipart upload to a vault named my-vault:
    Expected Output:
    
    :example: response = client.abort_multipart_upload(
        vaultName='string',
        uploadId='string'
    )
    
    
    :type accountId: string
    :param accountId: The AccountId value is the AWS account ID of the account that owns the vault. You can either specify an AWS account ID or optionally a single \'- \' (hyphen), in which case Amazon S3 Glacier uses the AWS account ID associated with the credentials used to sign the request. If you use an account ID, do not include any hyphens (\'-\') in the ID.\n\nNote: this parameter is set to '-' bydefault if no value is not specified.\n

    :type vaultName: string
    :param vaultName: [REQUIRED]\nThe name of the vault.\n

    :type uploadId: string
    :param uploadId: [REQUIRED]\nThe upload ID of the multipart upload to delete.\n

    :return: response = client.abort_multipart_upload(
        accountId='-',
        uploadId='19gaRezEXAMPLES6Ry5YYdqthHOC_kGRCT03L9yetr220UmPtBYKk-OssZtLqyFu7sY1_lR7vgFuJV6NtcV5zpsJ',
        vaultName='my-vault',
    )
    
    print(response)
    
    
    :returns: 
    Glacier.Client.exceptions.ResourceNotFoundException
    Glacier.Client.exceptions.InvalidParameterValueException
    Glacier.Client.exceptions.MissingParameterValueException
    Glacier.Client.exceptions.ServiceUnavailableException
    
    """
    pass

def abort_vault_lock(accountId=None, vaultName=None):
    """
    This operation aborts the vault locking process if the vault lock is not in the Locked state. If the vault lock is in the Locked state when this operation is requested, the operation returns an AccessDeniedException error. Aborting the vault locking process removes the vault lock policy from the specified vault.
    A vault lock is put into the InProgress state by calling  InitiateVaultLock . A vault lock is put into the Locked state by calling  CompleteVaultLock . You can get the state of a vault lock by calling  GetVaultLock . For more information about the vault locking process, see Amazon Glacier Vault Lock . For more information about vault lock policies, see Amazon Glacier Access Control with Vault Lock Policies .
    This operation is idempotent. You can successfully invoke this operation multiple times, if the vault lock is in the InProgress state or if there is no policy associated with the vault.
    See also: AWS API Documentation
    
    Exceptions
    Examples
    The example aborts the vault locking process if the vault lock is not in the Locked state for the vault named examplevault.
    Expected Output:
    
    :example: response = client.abort_vault_lock(
        vaultName='string'
    )
    
    
    :type accountId: string
    :param accountId: The AccountId value is the AWS account ID. This value must match the AWS account ID associated with the credentials used to sign the request. You can either specify an AWS account ID or optionally a single \'- \' (hyphen), in which case Amazon Glacier uses the AWS account ID associated with the credentials used to sign the request. If you specify your account ID, do not include any hyphens (\'-\') in the ID.\n\nNote: this parameter is set to '-' bydefault if no value is not specified.\n

    :type vaultName: string
    :param vaultName: [REQUIRED]\nThe name of the vault.\n

    :return: response = client.abort_vault_lock(
        accountId='-',
        vaultName='examplevault',
    )
    
    print(response)
    
    
    :returns: 
    Glacier.Client.exceptions.ResourceNotFoundException
    Glacier.Client.exceptions.InvalidParameterValueException
    Glacier.Client.exceptions.MissingParameterValueException
    Glacier.Client.exceptions.ServiceUnavailableException
    
    """
    pass

def add_tags_to_vault(accountId=None, vaultName=None, Tags=None):
    """
    This operation adds the specified tags to a vault. Each tag is composed of a key and a value. Each vault can have up to 10 tags. If your request would cause the tag limit for the vault to be exceeded, the operation throws the LimitExceededException error. If a tag already exists on the vault under a specified key, the existing key value will be overwritten. For more information about tags, see Tagging Amazon S3 Glacier Resources .
    See also: AWS API Documentation
    
    Exceptions
    Examples
    The example adds two tags to a my-vault.
    Expected Output:
    
    :example: response = client.add_tags_to_vault(
        vaultName='string',
        Tags={
            'string': 'string'
        }
    )
    
    
    :type accountId: string
    :param accountId: The AccountId value is the AWS account ID of the account that owns the vault. You can either specify an AWS account ID or optionally a single \'- \' (hyphen), in which case Amazon S3 Glacier uses the AWS account ID associated with the credentials used to sign the request. If you use an account ID, do not include any hyphens (\'-\') in the ID.\n\nNote: this parameter is set to '-' bydefault if no value is not specified.\n

    :type vaultName: string
    :param vaultName: [REQUIRED]\nThe name of the vault.\n

    :type Tags: dict
    :param Tags: The tags to add to the vault. Each tag is composed of a key and a value. The value can be an empty string.\n\n(string) --\n(string) --\n\n\n\n

    :return: response = client.add_tags_to_vault(
        Tags={
            'examplekey1': 'examplevalue1',
            'examplekey2': 'examplevalue2',
        },
        accountId='-',
        vaultName='my-vault',
    )
    
    print(response)
    
    
    :returns: 
    Glacier.Client.exceptions.InvalidParameterValueException
    Glacier.Client.exceptions.MissingParameterValueException
    Glacier.Client.exceptions.ResourceNotFoundException
    Glacier.Client.exceptions.LimitExceededException
    Glacier.Client.exceptions.ServiceUnavailableException
    
    """
    pass

def can_paginate(operation_name=None):
    """
    Check if an operation can be paginated.
    
    :type operation_name: string
    :param operation_name: The operation name. This is the same name\nas the method name on the client. For example, if the\nmethod name is create_foo, and you\'d normally invoke the\noperation as client.create_foo(**kwargs), if the\ncreate_foo operation can be paginated, you can use the\ncall client.get_paginator('create_foo').

    """
    pass

def complete_multipart_upload(accountId=None, vaultName=None, uploadId=None, archiveSize=None, checksum=None):
    """
    You call this operation to inform Amazon S3 Glacier (Glacier) that all the archive parts have been uploaded and that Glacier can now assemble the archive from the uploaded parts. After assembling and saving the archive to the vault, Glacier returns the URI path of the newly created archive resource. Using the URI path, you can then access the archive. After you upload an archive, you should save the archive ID returned to retrieve the archive at a later point. You can also get the vault inventory to obtain a list of archive IDs in a vault. For more information, see  InitiateJob .
    In the request, you must include the computed SHA256 tree hash of the entire archive you have uploaded. For information about computing a SHA256 tree hash, see Computing Checksums . On the server side, Glacier also constructs the SHA256 tree hash of the assembled archive. If the values match, Glacier saves the archive to the vault; otherwise, it returns an error, and the operation fails. The  ListParts operation returns a list of parts uploaded for a specific multipart upload. It includes checksum information for each uploaded part that can be used to debug a bad checksum issue.
    Additionally, Glacier also checks for any missing content ranges when assembling the archive, if missing content ranges are found, Glacier returns an error and the operation fails.
    Complete Multipart Upload is an idempotent operation. After your first successful complete multipart upload, if you call the operation again within a short period, the operation will succeed and return the same archive ID. This is useful in the event you experience a network issue that causes an aborted connection or receive a 500 server error, in which case you can repeat your Complete Multipart Upload request and get the same archive ID without creating duplicate archives. Note, however, that after the multipart upload completes, you cannot call the List Parts operation and the multipart upload will not appear in List Multipart Uploads response, even if idempotent complete is possible.
    An AWS account has full permission to perform all operations (actions). However, AWS Identity and Access Management (IAM) users don\'t have any permissions by default. You must grant them explicit permission to perform specific actions. For more information, see Access Control Using AWS Identity and Access Management (IAM) .
    For conceptual information and underlying REST API, see Uploading Large Archives in Parts (Multipart Upload) and Complete Multipart Upload in the Amazon Glacier Developer Guide .
    See also: AWS API Documentation
    
    Exceptions
    Examples
    The example completes a multipart upload for a 3 MiB archive.
    Expected Output:
    
    :example: response = client.complete_multipart_upload(
        vaultName='string',
        uploadId='string',
        archiveSize='string',
        checksum='string'
    )
    
    
    :type accountId: string
    :param accountId: The AccountId value is the AWS account ID of the account that owns the vault. You can either specify an AWS account ID or optionally a single \'- \' (hyphen), in which case Amazon S3 Glacier uses the AWS account ID associated with the credentials used to sign the request. If you use an account ID, do not include any hyphens (\'-\') in the ID.\n\nNote: this parameter is set to '-' bydefault if no value is not specified.\n

    :type vaultName: string
    :param vaultName: [REQUIRED]\nThe name of the vault.\n

    :type uploadId: string
    :param uploadId: [REQUIRED]\nThe upload ID of the multipart upload.\n

    :type archiveSize: string
    :param archiveSize: The total size, in bytes, of the entire archive. This value should be the sum of all the sizes of the individual parts that you uploaded.

    :type checksum: string
    :param checksum: The SHA256 tree hash of the entire archive. It is the tree hash of SHA256 tree hash of the individual parts. If the value you specify in the request does not match the SHA256 tree hash of the final assembled archive as computed by Amazon S3 Glacier (Glacier), Glacier returns an error and the request fails.\n\nThis is a required field.Ideally you will want to compute this value with checksums from\nprevious uploaded parts, using the algorithm described in\nGlacier documentation.\nBut if you prefer, you can also use botocore.utils.calculate_tree_hash()\nto compute it from raw file by:\nchecksum = calculate_tree_hash(open('your_file.txt', 'rb'))\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'location': 'string',
    'checksum': 'string',
    'archiveId': 'string'
}


Response Structure

(dict) --
Contains the Amazon S3 Glacier response to your request.
For information about the underlying REST API, see Upload Archive . For conceptual information, see Working with Archives in Amazon S3 Glacier .

location (string) --
The relative URI path of the newly added archive resource.

checksum (string) --
The checksum of the archive computed by Amazon S3 Glacier.

archiveId (string) --
The ID of the archive. This value is also included as part of the location.







Exceptions

Glacier.Client.exceptions.ResourceNotFoundException
Glacier.Client.exceptions.InvalidParameterValueException
Glacier.Client.exceptions.MissingParameterValueException
Glacier.Client.exceptions.ServiceUnavailableException

Examples
The example completes a multipart upload for a 3 MiB archive.
response = client.complete_multipart_upload(
    accountId='-',
    archiveSize='3145728',
    checksum='9628195fcdbcbbe76cdde456d4646fa7de5f219fb39823836d81f0cc0e18aa67',
    uploadId='19gaRezEXAMPLES6Ry5YYdqthHOC_kGRCT03L9yetr220UmPtBYKk-OssZtLqyFu7sY1_lR7vgFuJV6NtcV5zpsJ',
    vaultName='my-vault',
)

print(response)


Expected Output:
{
    'archiveId': 'NkbByEejwEggmBz2fTHgJrg0XBoDfjP4q6iu87-TjhqG6eGoOY9Z8i1_AUyUsuhPAdTqLHy8pTl5nfCFJmDl2yEZONi5L26Omw12vcs01MNGntHEQL8MBfGlqrEXAMPLEArchiveId',
    'checksum': '9628195fcdbcbbe76cdde456d4646fa7de5f219fb39823836d81f0cc0e18aa67',
    'location': '/111122223333/vaults/my-vault/archives/NkbByEejwEggmBz2fTHgJrg0XBoDfjP4q6iu87-TjhqG6eGoOY9Z8i1_AUyUsuhPAdTqLHy8pTl5nfCFJmDl2yEZONi5L26Omw12vcs01MNGntHEQL8MBfGlqrEXAMPLEArchiveId',
    'ResponseMetadata': {
        '...': '...',
    },
}



    :return: checksum = calculate_tree_hash(open('your_file.txt', 'rb'))
    
    
    :returns: 
    Glacier.Client.exceptions.ResourceNotFoundException
    Glacier.Client.exceptions.InvalidParameterValueException
    Glacier.Client.exceptions.MissingParameterValueException
    Glacier.Client.exceptions.ServiceUnavailableException
    
    """
    pass

def complete_vault_lock(accountId=None, vaultName=None, lockId=None):
    """
    This operation completes the vault locking process by transitioning the vault lock from the InProgress state to the Locked state, which causes the vault lock policy to become unchangeable. A vault lock is put into the InProgress state by calling  InitiateVaultLock . You can obtain the state of the vault lock by calling  GetVaultLock . For more information about the vault locking process, Amazon Glacier Vault Lock .
    This operation is idempotent. This request is always successful if the vault lock is in the Locked state and the provided lock ID matches the lock ID originally used to lock the vault.
    If an invalid lock ID is passed in the request when the vault lock is in the Locked state, the operation returns an AccessDeniedException error. If an invalid lock ID is passed in the request when the vault lock is in the InProgress state, the operation throws an InvalidParameter error.
    See also: AWS API Documentation
    
    Exceptions
    Examples
    The example completes the vault locking process by transitioning the vault lock from the InProgress state to the Locked state.
    Expected Output:
    
    :example: response = client.complete_vault_lock(
        vaultName='string',
        lockId='string'
    )
    
    
    :type accountId: string
    :param accountId: The AccountId value is the AWS account ID. This value must match the AWS account ID associated with the credentials used to sign the request. You can either specify an AWS account ID or optionally a single \'- \' (hyphen), in which case Amazon Glacier uses the AWS account ID associated with the credentials used to sign the request. If you specify your account ID, do not include any hyphens (\'-\') in the ID.\n\nNote: this parameter is set to '-' bydefault if no value is not specified.\n

    :type vaultName: string
    :param vaultName: [REQUIRED]\nThe name of the vault.\n

    :type lockId: string
    :param lockId: [REQUIRED]\nThe lockId value is the lock ID obtained from a InitiateVaultLock request.\n

    :return: response = client.complete_vault_lock(
        accountId='-',
        lockId='AE863rKkWZU53SLW5be4DUcW',
        vaultName='example-vault',
    )
    
    print(response)
    
    
    :returns: 
    Glacier.Client.exceptions.ResourceNotFoundException
    Glacier.Client.exceptions.InvalidParameterValueException
    Glacier.Client.exceptions.MissingParameterValueException
    Glacier.Client.exceptions.ServiceUnavailableException
    
    """
    pass

def create_vault(accountId=None, vaultName=None):
    """
    This operation creates a new vault with the specified name. The name of the vault must be unique within a region for an AWS account. You can create up to 1,000 vaults per account. If you need to create more vaults, contact Amazon S3 Glacier.
    You must use the following guidelines when naming a vault.
    This operation is idempotent.
    An AWS account has full permission to perform all operations (actions). However, AWS Identity and Access Management (IAM) users don\'t have any permissions by default. You must grant them explicit permission to perform specific actions. For more information, see Access Control Using AWS Identity and Access Management (IAM) .
    For conceptual information and underlying REST API, see Creating a Vault in Amazon Glacier and Create Vault in the Amazon Glacier Developer Guide .
    See also: AWS API Documentation
    
    Exceptions
    Examples
    The following example creates a new vault named my-vault.
    Expected Output:
    
    :example: response = client.create_vault(
        vaultName='string'
    )
    
    
    :type accountId: string
    :param accountId: The AccountId value is the AWS account ID. This value must match the AWS account ID associated with the credentials used to sign the request. You can either specify an AWS account ID or optionally a single \'- \' (hyphen), in which case Amazon S3 Glacier uses the AWS account ID associated with the credentials used to sign the request. If you specify your account ID, do not include any hyphens (\'-\') in the ID.\n\nNote: this parameter is set to '-' bydefault if no value is not specified.\n

    :type vaultName: string
    :param vaultName: [REQUIRED]\nThe name of the vault.\n

    :rtype: dict

ReturnsResponse Syntax
{
    'location': 'string'
}


Response Structure

(dict) --
Contains the Amazon S3 Glacier response to your request.

location (string) --
The URI of the vault that was created.







Exceptions

Glacier.Client.exceptions.InvalidParameterValueException
Glacier.Client.exceptions.MissingParameterValueException
Glacier.Client.exceptions.ServiceUnavailableException
Glacier.Client.exceptions.LimitExceededException

Examples
The following example creates a new vault named my-vault.
response = client.create_vault(
    accountId='-',
    vaultName='my-vault',
)

print(response)


Expected Output:
{
    'location': '/111122223333/vaults/my-vault',
    'ResponseMetadata': {
        '...': '...',
    },
}



    :return: {
        'location': 'string'
    }
    
    
    :returns: 
    accountId (string) -- The AccountId value is the AWS account ID. This value must match the AWS account ID associated with the credentials used to sign the request. You can either specify an AWS account ID or optionally a single \'- \' (hyphen), in which case Amazon S3 Glacier uses the AWS account ID associated with the credentials used to sign the request. If you specify your account ID, do not include any hyphens (\'-\') in the ID.
    
    Note: this parameter is set to "-" bydefault if no value is not specified.
    
    vaultName (string) -- [REQUIRED]
    The name of the vault.
    
    
    """
    pass

def delete_archive(accountId=None, vaultName=None, archiveId=None):
    """
    This operation deletes an archive from a vault. Subsequent requests to initiate a retrieval of this archive will fail. Archive retrievals that are in progress for this archive ID may or may not succeed according to the following scenarios:
    This operation is idempotent. Attempting to delete an already-deleted archive does not result in an error.
    An AWS account has full permission to perform all operations (actions). However, AWS Identity and Access Management (IAM) users don\'t have any permissions by default. You must grant them explicit permission to perform specific actions. For more information, see Access Control Using AWS Identity and Access Management (IAM) .
    For conceptual information and underlying REST API, see Deleting an Archive in Amazon Glacier and Delete Archive in the Amazon Glacier Developer Guide .
    See also: AWS API Documentation
    
    Exceptions
    Examples
    The example deletes the archive specified by the archive ID.
    Expected Output:
    
    :example: response = client.delete_archive(
        vaultName='string',
        archiveId='string'
    )
    
    
    :type accountId: string
    :param accountId: The AccountId value is the AWS account ID of the account that owns the vault. You can either specify an AWS account ID or optionally a single \'- \' (hyphen), in which case Amazon S3 Glacier uses the AWS account ID associated with the credentials used to sign the request. If you use an account ID, do not include any hyphens (\'-\') in the ID.\n\nNote: this parameter is set to '-' bydefault if no value is not specified.\n

    :type vaultName: string
    :param vaultName: [REQUIRED]\nThe name of the vault.\n

    :type archiveId: string
    :param archiveId: [REQUIRED]\nThe ID of the archive to delete.\n

    :return: response = client.delete_archive(
        accountId='-',
        archiveId='NkbByEejwEggmBz2fTHgJrg0XBoDfjP4q6iu87-TjhqG6eGoOY9Z8i1_AUyUsuhPAdTqLHy8pTl5nfCFJmDl2yEZONi5L26Omw12vcs01MNGntHEQL8MBfGlqrEXAMPLEArchiveId',
        vaultName='examplevault',
    )
    
    print(response)
    
    
    :returns: 
    accountId (string) -- The AccountId value is the AWS account ID of the account that owns the vault. You can either specify an AWS account ID or optionally a single \'- \' (hyphen), in which case Amazon S3 Glacier uses the AWS account ID associated with the credentials used to sign the request. If you use an account ID, do not include any hyphens (\'-\') in the ID.
    
    Note: this parameter is set to "-" bydefault if no value is not specified.
    
    vaultName (string) -- [REQUIRED]
    The name of the vault.
    
    archiveId (string) -- [REQUIRED]
    The ID of the archive to delete.
    
    
    """
    pass

def delete_vault(accountId=None, vaultName=None):
    """
    This operation deletes a vault. Amazon S3 Glacier will delete a vault only if there are no archives in the vault as of the last inventory and there have been no writes to the vault since the last inventory. If either of these conditions is not satisfied, the vault deletion fails (that is, the vault is not removed) and Amazon S3 Glacier returns an error. You can use  DescribeVault to return the number of archives in a vault, and you can use Initiate a Job (POST jobs) to initiate a new inventory retrieval for a vault. The inventory contains the archive IDs you use to delete archives using Delete Archive (DELETE archive) .
    This operation is idempotent.
    An AWS account has full permission to perform all operations (actions). However, AWS Identity and Access Management (IAM) users don\'t have any permissions by default. You must grant them explicit permission to perform specific actions. For more information, see Access Control Using AWS Identity and Access Management (IAM) .
    For conceptual information and underlying REST API, see Deleting a Vault in Amazon Glacier and Delete Vault in the Amazon S3 Glacier Developer Guide .
    See also: AWS API Documentation
    
    Exceptions
    Examples
    The example deletes a vault named my-vault:
    Expected Output:
    
    :example: response = client.delete_vault(
        vaultName='string'
    )
    
    
    :type accountId: string
    :param accountId: The AccountId value is the AWS account ID of the account that owns the vault. You can either specify an AWS account ID or optionally a single \'- \' (hyphen), in which case Amazon S3 Glacier uses the AWS account ID associated with the credentials used to sign the request. If you use an account ID, do not include any hyphens (\'-\') in the ID.\n\nNote: this parameter is set to '-' bydefault if no value is not specified.\n

    :type vaultName: string
    :param vaultName: [REQUIRED]\nThe name of the vault.\n

    :return: response = client.delete_vault(
        accountId='-',
        vaultName='my-vault',
    )
    
    print(response)
    
    
    :returns: 
    Glacier.Client.exceptions.ResourceNotFoundException
    Glacier.Client.exceptions.InvalidParameterValueException
    Glacier.Client.exceptions.MissingParameterValueException
    Glacier.Client.exceptions.ServiceUnavailableException
    
    """
    pass

def delete_vault_access_policy(accountId=None, vaultName=None):
    """
    This operation deletes the access policy associated with the specified vault. The operation is eventually consistent; that is, it might take some time for Amazon S3 Glacier to completely remove the access policy, and you might still see the effect of the policy for a short time after you send the delete request.
    This operation is idempotent. You can invoke delete multiple times, even if there is no policy associated with the vault. For more information about vault access policies, see Amazon Glacier Access Control with Vault Access Policies .
    See also: AWS API Documentation
    
    Exceptions
    Examples
    The example deletes the access policy associated with the vault named examplevault.
    Expected Output:
    
    :example: response = client.delete_vault_access_policy(
        vaultName='string'
    )
    
    
    :type accountId: string
    :param accountId: The AccountId value is the AWS account ID of the account that owns the vault. You can either specify an AWS account ID or optionally a single \'- \' (hyphen), in which case Amazon S3 Glacier uses the AWS account ID associated with the credentials used to sign the request. If you use an account ID, do not include any hyphens (\'-\') in the ID.\n\nNote: this parameter is set to '-' bydefault if no value is not specified.\n

    :type vaultName: string
    :param vaultName: [REQUIRED]\nThe name of the vault.\n

    :return: response = client.delete_vault_access_policy(
        accountId='-',
        vaultName='examplevault',
    )
    
    print(response)
    
    
    :returns: 
    Glacier.Client.exceptions.ResourceNotFoundException
    Glacier.Client.exceptions.InvalidParameterValueException
    Glacier.Client.exceptions.MissingParameterValueException
    Glacier.Client.exceptions.ServiceUnavailableException
    
    """
    pass

def delete_vault_notifications(accountId=None, vaultName=None):
    """
    This operation deletes the notification configuration set for a vault. The operation is eventually consistent; that is, it might take some time for Amazon S3 Glacier to completely disable the notifications and you might still receive some notifications for a short time after you send the delete request.
    An AWS account has full permission to perform all operations (actions). However, AWS Identity and Access Management (IAM) users don\'t have any permissions by default. You must grant them explicit permission to perform specific actions. For more information, see Access Control Using AWS Identity and Access Management (IAM) .
    For conceptual information and underlying REST API, see Configuring Vault Notifications in Amazon S3 Glacier and Delete Vault Notification Configuration in the Amazon S3 Glacier Developer Guide.
    See also: AWS API Documentation
    
    Exceptions
    Examples
    The example deletes the notification configuration set for the vault named examplevault.
    Expected Output:
    
    :example: response = client.delete_vault_notifications(
        vaultName='string'
    )
    
    
    :type accountId: string
    :param accountId: The AccountId value is the AWS account ID of the account that owns the vault. You can either specify an AWS account ID or optionally a single \'- \' (hyphen), in which case Amazon S3 Glacier uses the AWS account ID associated with the credentials used to sign the request. If you use an account ID, do not include any hyphens (\'-\') in the ID.\n\nNote: this parameter is set to '-' bydefault if no value is not specified.\n

    :type vaultName: string
    :param vaultName: [REQUIRED]\nThe name of the vault.\n

    :return: response = client.delete_vault_notifications(
        accountId='-',
        vaultName='examplevault',
    )
    
    print(response)
    
    
    :returns: 
    Glacier.Client.exceptions.ResourceNotFoundException
    Glacier.Client.exceptions.InvalidParameterValueException
    Glacier.Client.exceptions.MissingParameterValueException
    Glacier.Client.exceptions.ServiceUnavailableException
    
    """
    pass

def describe_job(accountId=None, vaultName=None, jobId=None):
    """
    This operation returns information about a job you previously initiated, including the job initiation date, the user who initiated the job, the job status code/message and the Amazon SNS topic to notify after Amazon S3 Glacier (Glacier) completes the job. For more information about initiating a job, see  InitiateJob .
    A job ID will not expire for at least 24 hours after Glacier completes the job.
    An AWS account has full permission to perform all operations (actions). However, AWS Identity and Access Management (IAM) users don\'t have any permissions by default. You must grant them explicit permission to perform specific actions. For more information, see Access Control Using AWS Identity and Access Management (IAM) .
    For more information about using this operation, see the documentation for the underlying REST API Describe Job in the Amazon Glacier Developer Guide .
    See also: AWS API Documentation
    
    Exceptions
    Examples
    The example returns information about the previously initiated job specified by the job ID.
    Expected Output:
    
    :example: response = client.describe_job(
        vaultName='string',
        jobId='string'
    )
    
    
    :type accountId: string
    :param accountId: The AccountId value is the AWS account ID of the account that owns the vault. You can either specify an AWS account ID or optionally a single \'- \' (hyphen), in which case Amazon S3 Glacier uses the AWS account ID associated with the credentials used to sign the request. If you use an account ID, do not include any hyphens (\'-\') in the ID.\n\nNote: this parameter is set to '-' bydefault if no value is not specified.\n

    :type vaultName: string
    :param vaultName: [REQUIRED]\nThe name of the vault.\n

    :type jobId: string
    :param jobId: [REQUIRED]\nThe ID of the job to describe.\n

    :rtype: dict

ReturnsResponse Syntax
{
    'JobId': 'string',
    'JobDescription': 'string',
    'Action': 'ArchiveRetrieval'|'InventoryRetrieval'|'Select',
    'ArchiveId': 'string',
    'VaultARN': 'string',
    'CreationDate': 'string',
    'Completed': True|False,
    'StatusCode': 'InProgress'|'Succeeded'|'Failed',
    'StatusMessage': 'string',
    'ArchiveSizeInBytes': 123,
    'InventorySizeInBytes': 123,
    'SNSTopic': 'string',
    'CompletionDate': 'string',
    'SHA256TreeHash': 'string',
    'ArchiveSHA256TreeHash': 'string',
    'RetrievalByteRange': 'string',
    'Tier': 'string',
    'InventoryRetrievalParameters': {
        'Format': 'string',
        'StartDate': 'string',
        'EndDate': 'string',
        'Limit': 'string',
        'Marker': 'string'
    },
    'JobOutputPath': 'string',
    'SelectParameters': {
        'InputSerialization': {
            'csv': {
                'FileHeaderInfo': 'USE'|'IGNORE'|'NONE',
                'Comments': 'string',
                'QuoteEscapeCharacter': 'string',
                'RecordDelimiter': 'string',
                'FieldDelimiter': 'string',
                'QuoteCharacter': 'string'
            }
        },
        'ExpressionType': 'SQL',
        'Expression': 'string',
        'OutputSerialization': {
            'csv': {
                'QuoteFields': 'ALWAYS'|'ASNEEDED',
                'QuoteEscapeCharacter': 'string',
                'RecordDelimiter': 'string',
                'FieldDelimiter': 'string',
                'QuoteCharacter': 'string'
            }
        }
    },
    'OutputLocation': {
        'S3': {
            'BucketName': 'string',
            'Prefix': 'string',
            'Encryption': {
                'EncryptionType': 'aws:kms'|'AES256',
                'KMSKeyId': 'string',
                'KMSContext': 'string'
            },
            'CannedACL': 'private'|'public-read'|'public-read-write'|'aws-exec-read'|'authenticated-read'|'bucket-owner-read'|'bucket-owner-full-control',
            'AccessControlList': [
                {
                    'Grantee': {
                        'Type': 'AmazonCustomerByEmail'|'CanonicalUser'|'Group',
                        'DisplayName': 'string',
                        'URI': 'string',
                        'ID': 'string',
                        'EmailAddress': 'string'
                    },
                    'Permission': 'FULL_CONTROL'|'WRITE'|'WRITE_ACP'|'READ'|'READ_ACP'
                },
            ],
            'Tagging': {
                'string': 'string'
            },
            'UserMetadata': {
                'string': 'string'
            },
            'StorageClass': 'STANDARD'|'REDUCED_REDUNDANCY'|'STANDARD_IA'
        }
    }
}


Response Structure

(dict) --
Contains the description of an Amazon S3 Glacier job.

JobId (string) --
An opaque string that identifies an Amazon S3 Glacier job.

JobDescription (string) --
The job description provided when initiating the job.

Action (string) --
The job type. This value is either ArchiveRetrieval , InventoryRetrieval , or Select .

ArchiveId (string) --
The archive ID requested for a select job or archive retrieval. Otherwise, this field is null.

VaultARN (string) --
The Amazon Resource Name (ARN) of the vault from which an archive retrieval was requested.

CreationDate (string) --
The UTC date when the job was created. This value is a string representation of ISO 8601 date format, for example "2012-03-20T17:03:43.221Z" .

Completed (boolean) --
The job status. When a job is completed, you get the job\'s output using Get Job Output (GET output).

StatusCode (string) --
The status code can be InProgress , Succeeded , or Failed , and indicates the status of the job.

StatusMessage (string) --
A friendly message that describes the job status.

ArchiveSizeInBytes (integer) --
For an archive retrieval job, this value is the size in bytes of the archive being requested for download. For an inventory retrieval or select job, this value is null.

InventorySizeInBytes (integer) --
For an inventory retrieval job, this value is the size in bytes of the inventory requested for download. For an archive retrieval or select job, this value is null.

SNSTopic (string) --
An Amazon SNS topic that receives notification.

CompletionDate (string) --
The UTC time that the job request completed. While the job is in progress, the value is null.

SHA256TreeHash (string) --
For an archive retrieval job, this value is the checksum of the archive. Otherwise, this value is null.
The SHA256 tree hash value for the requested range of an archive. If the InitiateJob request for an archive specified a tree-hash aligned range, then this field returns a value.
If the whole archive is retrieved, this value is the same as the ArchiveSHA256TreeHash value.
This field is null for the following:

Archive retrieval jobs that specify a range that is not tree-hash aligned
Archival jobs that specify a range that is equal to the whole archive, when the job status is InProgress
Inventory jobs
Select jobs


ArchiveSHA256TreeHash (string) --
The SHA256 tree hash of the entire archive for an archive retrieval. For inventory retrieval or select jobs, this field is null.

RetrievalByteRange (string) --
The retrieved byte range for archive retrieval jobs in the form StartByteValue -EndByteValue . If no range was specified in the archive retrieval, then the whole archive is retrieved. In this case, StartByteValue equals 0 and EndByteValue equals the size of the archive minus 1. For inventory retrieval or select jobs, this field is null.

Tier (string) --
The tier to use for a select or an archive retrieval. Valid values are Expedited , Standard , or Bulk . Standard is the default.

InventoryRetrievalParameters (dict) --
Parameters used for range inventory retrieval.

Format (string) --
The output format for the vault inventory list, which is set by the InitiateJob request when initiating a job to retrieve a vault inventory. Valid values are CSV and JSON .

StartDate (string) --
The start of the date range in Universal Coordinated Time (UTC) for vault inventory retrieval that includes archives created on or after this date. This value should be a string in the ISO 8601 date format, for example 2013-03-20T17:03:43Z .

EndDate (string) --
The end of the date range in UTC for vault inventory retrieval that includes archives created before this date. This value should be a string in the ISO 8601 date format, for example 2013-03-20T17:03:43Z .

Limit (string) --
The maximum number of inventory items returned per vault inventory retrieval request. This limit is set when initiating the job with the a InitiateJob request.

Marker (string) --
An opaque string that represents where to continue pagination of the vault inventory retrieval results. You use the marker in a new InitiateJob request to obtain additional inventory items. If there are no more inventory items, this value is null . For more information, see Range Inventory Retrieval .



JobOutputPath (string) --
Contains the job output location.

SelectParameters (dict) --
Contains the parameters used for a select.

InputSerialization (dict) --
Describes the serialization format of the object.

csv (dict) --
Describes the serialization of a CSV-encoded object.

FileHeaderInfo (string) --
Describes the first line of input. Valid values are None , Ignore , and Use .

Comments (string) --
A single character used to indicate that a row should be ignored when the character is present at the start of that row.

QuoteEscapeCharacter (string) --
A single character used for escaping the quotation-mark character inside an already escaped value.

RecordDelimiter (string) --
A value used to separate individual records from each other.

FieldDelimiter (string) --
A value used to separate individual fields from each other within a record.

QuoteCharacter (string) --
A value used as an escape character where the field delimiter is part of the value.





ExpressionType (string) --
The type of the provided expression, for example SQL .

Expression (string) --
The expression that is used to select the object.

OutputSerialization (dict) --
Describes how the results of the select job are serialized.

csv (dict) --
Describes the serialization of CSV-encoded query results.

QuoteFields (string) --
A value that indicates whether all output fields should be contained within quotation marks.

QuoteEscapeCharacter (string) --
A single character used for escaping the quotation-mark character inside an already escaped value.

RecordDelimiter (string) --
A value used to separate individual records from each other.

FieldDelimiter (string) --
A value used to separate individual fields from each other within a record.

QuoteCharacter (string) --
A value used as an escape character where the field delimiter is part of the value.







OutputLocation (dict) --
Contains the location where the data from the select job is stored.

S3 (dict) --
Describes an S3 location that will receive the results of the job request.

BucketName (string) --
The name of the Amazon S3 bucket where the job results are stored.

Prefix (string) --
The prefix that is prepended to the results for this request.

Encryption (dict) --
Contains information about the encryption used to store the job results in Amazon S3.

EncryptionType (string) --
The server-side encryption algorithm used when storing job results in Amazon S3, for example AES256 or aws:kms .

KMSKeyId (string) --
The AWS KMS key ID to use for object encryption. All GET and PUT requests for an object protected by AWS KMS fail if not made by using Secure Sockets Layer (SSL) or Signature Version 4.

KMSContext (string) --
Optional. If the encryption type is aws:kms , you can use this value to specify the encryption context for the job results.



CannedACL (string) --
The canned access control list (ACL) to apply to the job results.

AccessControlList (list) --
A list of grants that control access to the staged results.

(dict) --
Contains information about a grant.

Grantee (dict) --
The grantee.

Type (string) --
Type of grantee

DisplayName (string) --
Screen name of the grantee.

URI (string) --
URI of the grantee group.

ID (string) --
The canonical user ID of the grantee.

EmailAddress (string) --
Email address of the grantee.



Permission (string) --
Specifies the permission given to the grantee.





Tagging (dict) --
The tag-set that is applied to the job results.

(string) --
(string) --




UserMetadata (dict) --
A map of metadata to store with the job results in Amazon S3.

(string) --
(string) --




StorageClass (string) --
The storage class used to store the job results.











Exceptions

Glacier.Client.exceptions.ResourceNotFoundException
Glacier.Client.exceptions.InvalidParameterValueException
Glacier.Client.exceptions.MissingParameterValueException
Glacier.Client.exceptions.ServiceUnavailableException

Examples
The example returns information about the previously initiated job specified by the job ID.
response = client.describe_job(
    accountId='-',
    jobId='zbxcm3Z_3z5UkoroF7SuZKrxgGoDc3RloGduS7Eg-RO47Yc6FxsdGBgf_Q2DK5Ejh18CnTS5XW4_XqlNHS61dsO4Cn',
    vaultName='my-vault',
)

print(response)


Expected Output:
{
    'Action': 'InventoryRetrieval',
    'Completed': False,
    'CreationDate': '2015-07-17T20:23:41.616Z',
    'InventoryRetrievalParameters': {
        'Format': 'JSON',
    },
    'JobId': 'zbxcm3Z_3z5UkoroF7SuZKrxgGoDc3RloGduS7Eg-RO47Yc6FxsdGBgf_Q2DK5Ejh18CnTS5XW4_XqlNHS61dsO4CnMW',
    'StatusCode': 'InProgress',
    'VaultARN': 'arn:aws:glacier:us-west-2:0123456789012:vaults/my-vault',
    'ResponseMetadata': {
        '...': '...',
    },
}



    :return: {
        'JobId': 'string',
        'JobDescription': 'string',
        'Action': 'ArchiveRetrieval'|'InventoryRetrieval'|'Select',
        'ArchiveId': 'string',
        'VaultARN': 'string',
        'CreationDate': 'string',
        'Completed': True|False,
        'StatusCode': 'InProgress'|'Succeeded'|'Failed',
        'StatusMessage': 'string',
        'ArchiveSizeInBytes': 123,
        'InventorySizeInBytes': 123,
        'SNSTopic': 'string',
        'CompletionDate': 'string',
        'SHA256TreeHash': 'string',
        'ArchiveSHA256TreeHash': 'string',
        'RetrievalByteRange': 'string',
        'Tier': 'string',
        'InventoryRetrievalParameters': {
            'Format': 'string',
            'StartDate': 'string',
            'EndDate': 'string',
            'Limit': 'string',
            'Marker': 'string'
        },
        'JobOutputPath': 'string',
        'SelectParameters': {
            'InputSerialization': {
                'csv': {
                    'FileHeaderInfo': 'USE'|'IGNORE'|'NONE',
                    'Comments': 'string',
                    'QuoteEscapeCharacter': 'string',
                    'RecordDelimiter': 'string',
                    'FieldDelimiter': 'string',
                    'QuoteCharacter': 'string'
                }
            },
            'ExpressionType': 'SQL',
            'Expression': 'string',
            'OutputSerialization': {
                'csv': {
                    'QuoteFields': 'ALWAYS'|'ASNEEDED',
                    'QuoteEscapeCharacter': 'string',
                    'RecordDelimiter': 'string',
                    'FieldDelimiter': 'string',
                    'QuoteCharacter': 'string'
                }
            }
        },
        'OutputLocation': {
            'S3': {
                'BucketName': 'string',
                'Prefix': 'string',
                'Encryption': {
                    'EncryptionType': 'aws:kms'|'AES256',
                    'KMSKeyId': 'string',
                    'KMSContext': 'string'
                },
                'CannedACL': 'private'|'public-read'|'public-read-write'|'aws-exec-read'|'authenticated-read'|'bucket-owner-read'|'bucket-owner-full-control',
                'AccessControlList': [
                    {
                        'Grantee': {
                            'Type': 'AmazonCustomerByEmail'|'CanonicalUser'|'Group',
                            'DisplayName': 'string',
                            'URI': 'string',
                            'ID': 'string',
                            'EmailAddress': 'string'
                        },
                        'Permission': 'FULL_CONTROL'|'WRITE'|'WRITE_ACP'|'READ'|'READ_ACP'
                    },
                ],
                'Tagging': {
                    'string': 'string'
                },
                'UserMetadata': {
                    'string': 'string'
                },
                'StorageClass': 'STANDARD'|'REDUCED_REDUNDANCY'|'STANDARD_IA'
            }
        }
    }
    
    
    :returns: 
    Archive retrieval jobs that specify a range that is not tree-hash aligned
    Archival jobs that specify a range that is equal to the whole archive, when the job status is InProgress
    Inventory jobs
    Select jobs
    
    """
    pass

def describe_vault(accountId=None, vaultName=None):
    """
    This operation returns information about a vault, including the vault\'s Amazon Resource Name (ARN), the date the vault was created, the number of archives it contains, and the total size of all the archives in the vault. The number of archives and their total size are as of the last inventory generation. This means that if you add or remove an archive from a vault, and then immediately use Describe Vault, the change in contents will not be immediately reflected. If you want to retrieve the latest inventory of the vault, use  InitiateJob . Amazon S3 Glacier generates vault inventories approximately daily. For more information, see Downloading a Vault Inventory in Amazon S3 Glacier .
    An AWS account has full permission to perform all operations (actions). However, AWS Identity and Access Management (IAM) users don\'t have any permissions by default. You must grant them explicit permission to perform specific actions. For more information, see Access Control Using AWS Identity and Access Management (IAM) .
    For conceptual information and underlying REST API, see Retrieving Vault Metadata in Amazon S3 Glacier and Describe Vault in the Amazon Glacier Developer Guide .
    See also: AWS API Documentation
    
    Exceptions
    Examples
    The example retrieves data about a vault named my-vault.
    Expected Output:
    
    :example: response = client.describe_vault(
        vaultName='string'
    )
    
    
    :type accountId: string
    :param accountId: The AccountId value is the AWS account ID of the account that owns the vault. You can either specify an AWS account ID or optionally a single \'- \' (hyphen), in which case Amazon S3 Glacier uses the AWS account ID associated with the credentials used to sign the request. If you use an account ID, do not include any hyphens (\'-\') in the ID.\n\nNote: this parameter is set to '-' bydefault if no value is not specified.\n

    :type vaultName: string
    :param vaultName: [REQUIRED]\nThe name of the vault.\n

    :rtype: dict

ReturnsResponse Syntax
{
    'VaultARN': 'string',
    'VaultName': 'string',
    'CreationDate': 'string',
    'LastInventoryDate': 'string',
    'NumberOfArchives': 123,
    'SizeInBytes': 123
}


Response Structure

(dict) --
Contains the Amazon S3 Glacier response to your request.

VaultARN (string) --
The Amazon Resource Name (ARN) of the vault.

VaultName (string) --
The name of the vault.

CreationDate (string) --
The Universal Coordinated Time (UTC) date when the vault was created. This value should be a string in the ISO 8601 date format, for example 2012-03-20T17:03:43.221Z .

LastInventoryDate (string) --
The Universal Coordinated Time (UTC) date when Amazon S3 Glacier completed the last vault inventory. This value should be a string in the ISO 8601 date format, for example 2012-03-20T17:03:43.221Z .

NumberOfArchives (integer) --
The number of archives in the vault as of the last inventory date. This field will return null if an inventory has not yet run on the vault, for example if you just created the vault.

SizeInBytes (integer) --
Total size, in bytes, of the archives in the vault as of the last inventory date. This field will return null if an inventory has not yet run on the vault, for example if you just created the vault.







Exceptions

Glacier.Client.exceptions.ResourceNotFoundException
Glacier.Client.exceptions.InvalidParameterValueException
Glacier.Client.exceptions.MissingParameterValueException
Glacier.Client.exceptions.ServiceUnavailableException

Examples
The example retrieves data about a vault named my-vault.
response = client.describe_vault(
    accountId='-',
    vaultName='my-vault',
)

print(response)


Expected Output:
{
    'CreationDate': '2016-09-23T19:27:18.665Z',
    'NumberOfArchives': 0,
    'SizeInBytes': 0,
    'VaultARN': 'arn:aws:glacier:us-west-2:111122223333:vaults/my-vault',
    'VaultName': 'my-vault',
    'ResponseMetadata': {
        '...': '...',
    },
}



    :return: {
        'VaultARN': 'string',
        'VaultName': 'string',
        'CreationDate': 'string',
        'LastInventoryDate': 'string',
        'NumberOfArchives': 123,
        'SizeInBytes': 123
    }
    
    
    :returns: 
    Glacier.Client.exceptions.ResourceNotFoundException
    Glacier.Client.exceptions.InvalidParameterValueException
    Glacier.Client.exceptions.MissingParameterValueException
    Glacier.Client.exceptions.ServiceUnavailableException
    
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

def get_data_retrieval_policy(accountId=None):
    """
    This operation returns the current data retrieval policy for the account and region specified in the GET request. For more information about data retrieval policies, see Amazon Glacier Data Retrieval Policies .
    See also: AWS API Documentation
    
    Exceptions
    Examples
    The example returns the current data retrieval policy for the account.
    Expected Output:
    
    :example: response = client.get_data_retrieval_policy(
    
    )
    
    
    :type accountId: string
    :param accountId: The AccountId value is the AWS account ID. This value must match the AWS account ID associated with the credentials used to sign the request. You can either specify an AWS account ID or optionally a single \'- \' (hyphen), in which case Amazon Glacier uses the AWS account ID associated with the credentials used to sign the request. If you specify your account ID, do not include any hyphens (\'-\') in the ID.\n\nNote: this parameter is set to '-' bydefault if no value is not specified.\n

    :rtype: dict
ReturnsResponse Syntax{
    'Policy': {
        'Rules': [
            {
                'Strategy': 'string',
                'BytesPerHour': 123
            },
        ]
    }
}


Response Structure

(dict) --Contains the Amazon S3 Glacier response to the GetDataRetrievalPolicy request.

Policy (dict) --Contains the returned data retrieval policy in JSON format.

Rules (list) --The policy rule. Although this is a list type, currently there must be only one rule, which contains a Strategy field and optionally a BytesPerHour field.

(dict) --Data retrieval policy rule.

Strategy (string) --The type of data retrieval policy to set.
Valid values: BytesPerHour|FreeTier|None

BytesPerHour (integer) --The maximum number of bytes that can be retrieved in an hour.
This field is required only if the value of the Strategy field is BytesPerHour . Your PUT operation will be rejected if the Strategy field is not set to BytesPerHour and you set this field.












Exceptions

Glacier.Client.exceptions.InvalidParameterValueException
Glacier.Client.exceptions.MissingParameterValueException
Glacier.Client.exceptions.ServiceUnavailableException

Examples
The example returns the current data retrieval policy for the account.
response = client.get_data_retrieval_policy(
    accountId='-',
)

print(response)


Expected Output:
{
    'Policy': {
        'Rules': [
            {
                'BytesPerHour': 10737418240,
                'Strategy': 'BytesPerHour',
            },
        ],
    },
    'ResponseMetadata': {
        '...': '...',
    },
}



    :return: {
        'Policy': {
            'Rules': [
                {
                    'Strategy': 'string',
                    'BytesPerHour': 123
                },
            ]
        }
    }
    
    
    """
    pass

def get_job_output(accountId=None, vaultName=None, jobId=None, range=None):
    """
    This operation downloads the output of the job you initiated using  InitiateJob . Depending on the job type you specified when you initiated the job, the output will be either the content of an archive or a vault inventory.
    You can download all the job output or download a portion of the output by specifying a byte range. In the case of an archive retrieval job, depending on the byte range you specify, Amazon S3 Glacier (Glacier) returns the checksum for the portion of the data. You can compute the checksum on the client and verify that the values match to ensure the portion you downloaded is the correct data.
    A job ID will not expire for at least 24 hours after Glacier completes the job. That a byte range. For both archive and inventory retrieval jobs, you should verify the downloaded size against the size returned in the headers from the Get Job Output response.
    For archive retrieval jobs, you should also verify that the size is what you expected. If you download a portion of the output, the expected size is based on the range of bytes you specified. For example, if you specify a range of bytes=0-1048575 , you should verify your download size is 1,048,576 bytes. If you download an entire archive, the expected size is the size of the archive when you uploaded it to Amazon S3 Glacier The expected size is also returned in the headers from the Get Job Output response.
    In the case of an archive retrieval job, depending on the byte range you specify, Glacier returns the checksum for the portion of the data. To ensure the portion you downloaded is the correct data, compute the checksum on the client, verify that the values match, and verify that the size is what you expected.
    A job ID does not expire for at least 24 hours after Glacier completes the job. That is, you can download the job output within the 24 hours period after Amazon Glacier completes the job.
    An AWS account has full permission to perform all operations (actions). However, AWS Identity and Access Management (IAM) users don\'t have any permissions by default. You must grant them explicit permission to perform specific actions. For more information, see Access Control Using AWS Identity and Access Management (IAM) .
    For conceptual information and the underlying REST API, see Downloading a Vault Inventory , Downloading an Archive , and Get Job Output
    See also: AWS API Documentation
    
    Exceptions
    Examples
    The example downloads the output of a previously initiated inventory retrieval job that is identified by the job ID.
    Expected Output:
    
    :example: response = client.get_job_output(
        vaultName='string',
        jobId='string',
        range='string'
    )
    
    
    :type accountId: string
    :param accountId: The AccountId value is the AWS account ID of the account that owns the vault. You can either specify an AWS account ID or optionally a single \'- \' (hyphen), in which case Amazon S3 Glacier uses the AWS account ID associated with the credentials used to sign the request. If you use an account ID, do not include any hyphens (\'-\') in the ID.\n\nNote: this parameter is set to '-' bydefault if no value is not specified.\n

    :type vaultName: string
    :param vaultName: [REQUIRED]\nThe name of the vault.\n

    :type jobId: string
    :param jobId: [REQUIRED]\nThe job ID whose data is downloaded.\n

    :type range: string
    :param range: The range of bytes to retrieve from the output. For example, if you want to download the first 1,048,576 bytes, specify the range as bytes=0-1048575 . By default, this operation downloads the entire output.\nIf the job output is large, then you can use a range to retrieve a portion of the output. This allows you to download the entire output in smaller chunks of bytes. For example, suppose you have 1 GB of job output you want to download and you decide to download 128 MB chunks of data at a time, which is a total of eight Get Job Output requests. You use the following process to download the job output:\n\nDownload a 128 MB chunk of output by specifying the appropriate byte range. Verify that all 128 MB of data was received.\nAlong with the data, the response includes a SHA256 tree hash of the payload. You compute the checksum of the payload on the client and compare it with the checksum you received in the response to ensure you received all the expected data.\nRepeat steps 1 and 2 for all the eight 128 MB chunks of output data, each time specifying the appropriate byte range.\nAfter downloading all the parts of the job output, you have a list of eight checksum values. Compute the tree hash of these values to find the checksum of the entire output. Using the DescribeJob API, obtain job information of the job that provided you the output. The response includes the checksum of the entire archive stored in Amazon S3 Glacier. You compare this value with the checksum you computed to ensure you have downloaded the entire archive content with no errors.\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'body': StreamingBody(),
    'checksum': 'string',
    'status': 123,
    'contentRange': 'string',
    'acceptRanges': 'string',
    'contentType': 'string',
    'archiveDescription': 'string'
}


Response Structure

(dict) --
Contains the Amazon S3 Glacier response to your request.

body (StreamingBody) --
The job data, either archive data or inventory data.

checksum (string) --
The checksum of the data in the response. This header is returned only when retrieving the output for an archive retrieval job. Furthermore, this header appears only under the following conditions:

You get the entire range of the archive.
You request a range to return of the archive that starts and ends on a multiple of 1 MB. For example, if you have an 3.1 MB archive and you specify a range to return that starts at 1 MB and ends at 2 MB, then the x-amz-sha256-tree-hash is returned as a response header.
You request a range of the archive to return that starts on a multiple of 1 MB and goes to the end of the archive. For example, if you have a 3.1 MB archive and you specify a range that starts at 2 MB and ends at 3.1 MB (the end of the archive), then the x-amz-sha256-tree-hash is returned as a response header.


status (integer) --
The HTTP response code for a job output request. The value depends on whether a range was specified in the request.

contentRange (string) --
The range of bytes returned by Amazon S3 Glacier. If only partial output is downloaded, the response provides the range of bytes Amazon S3 Glacier returned. For example, bytes 0-1048575/8388608 returns the first 1 MB from 8 MB.

acceptRanges (string) --
Indicates the range units accepted. For more information, see RFC2616 .

contentType (string) --
The Content-Type depends on whether the job output is an archive or a vault inventory. For archive data, the Content-Type is application/octet-stream. For vault inventory, if you requested CSV format when you initiated the job, the Content-Type is text/csv. Otherwise, by default, vault inventory is returned as JSON, and the Content-Type is application/json.

archiveDescription (string) --
The description of an archive.







Exceptions

Glacier.Client.exceptions.ResourceNotFoundException
Glacier.Client.exceptions.InvalidParameterValueException
Glacier.Client.exceptions.MissingParameterValueException
Glacier.Client.exceptions.ServiceUnavailableException

Examples
The example downloads the output of a previously initiated inventory retrieval job that is identified by the job ID.
response = client.get_job_output(
    accountId='-',
    jobId='zbxcm3Z_3z5UkoroF7SuZKrxgGoDc3RloGduS7Eg-RO47Yc6FxsdGBgf_Q2DK5Ejh18CnTS5XW4_XqlNHS61dsO4CnMW',
    range='',
    vaultName='my-vaul',
)

print(response)


Expected Output:
{
    'acceptRanges': 'bytes',
    'body': 'inventory-data',
    'contentType': 'application/json',
    'status': 200,
    'ResponseMetadata': {
        '...': '...',
    },
}



    :return: {
        'body': StreamingBody(),
        'checksum': 'string',
        'status': 123,
        'contentRange': 'string',
        'acceptRanges': 'string',
        'contentType': 'string',
        'archiveDescription': 'string'
    }
    
    
    :returns: 
    You get the entire range of the archive.
    You request a range to return of the archive that starts and ends on a multiple of 1 MB. For example, if you have an 3.1 MB archive and you specify a range to return that starts at 1 MB and ends at 2 MB, then the x-amz-sha256-tree-hash is returned as a response header.
    You request a range of the archive to return that starts on a multiple of 1 MB and goes to the end of the archive. For example, if you have a 3.1 MB archive and you specify a range that starts at 2 MB and ends at 3.1 MB (the end of the archive), then the x-amz-sha256-tree-hash is returned as a response header.
    
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

def get_vault_access_policy(accountId=None, vaultName=None):
    """
    This operation retrieves the access-policy subresource set on the vault; for more information on setting this subresource, see Set Vault Access Policy (PUT access-policy) . If there is no access policy set on the vault, the operation returns a 404 Not found error. For more information about vault access policies, see Amazon Glacier Access Control with Vault Access Policies .
    See also: AWS API Documentation
    
    Exceptions
    Examples
    The example retrieves the access-policy set on the vault named example-vault.
    Expected Output:
    
    :example: response = client.get_vault_access_policy(
        vaultName='string'
    )
    
    
    :type accountId: string
    :param accountId: The AccountId value is the AWS account ID of the account that owns the vault. You can either specify an AWS account ID or optionally a single \'- \' (hyphen), in which case Amazon S3 Glacier uses the AWS account ID associated with the credentials used to sign the request. If you use an account ID, do not include any hyphens (\'-\') in the ID.\n\nNote: this parameter is set to '-' bydefault if no value is not specified.\n

    :type vaultName: string
    :param vaultName: [REQUIRED]\nThe name of the vault.\n

    :rtype: dict

ReturnsResponse Syntax
{
    'policy': {
        'Policy': 'string'
    }
}


Response Structure

(dict) --
Output for GetVaultAccessPolicy.

policy (dict) --
Contains the returned vault access policy as a JSON string.

Policy (string) --
The vault access policy.









Exceptions

Glacier.Client.exceptions.ResourceNotFoundException
Glacier.Client.exceptions.InvalidParameterValueException
Glacier.Client.exceptions.MissingParameterValueException
Glacier.Client.exceptions.ServiceUnavailableException

Examples
The example retrieves the access-policy set on the vault named example-vault.
response = client.get_vault_access_policy(
    accountId='-',
    vaultName='example-vault',
)

print(response)


Expected Output:
{
    'policy': {
        'Policy': '{"Version":"2012-10-17","Statement":[{"Sid":"Define-owner-access-rights","Effect":"Allow","Principal":{"AWS":"arn:aws:iam::999999999999:root"},"Action":"glacier:DeleteArchive","Resource":"arn:aws:glacier:us-west-2:999999999999:vaults/examplevault"}]}',
    },
    'ResponseMetadata': {
        '...': '...',
    },
}



    :return: {
        'policy': {
            'Policy': 'string'
        }
    }
    
    
    :returns: 
    Glacier.Client.exceptions.ResourceNotFoundException
    Glacier.Client.exceptions.InvalidParameterValueException
    Glacier.Client.exceptions.MissingParameterValueException
    Glacier.Client.exceptions.ServiceUnavailableException
    
    """
    pass

def get_vault_lock(accountId=None, vaultName=None):
    """
    This operation retrieves the following attributes from the lock-policy subresource set on the specified vault:
    A vault lock is put into the InProgress state by calling  InitiateVaultLock . A vault lock is put into the Locked state by calling  CompleteVaultLock . You can abort the vault locking process by calling  AbortVaultLock . For more information about the vault locking process, Amazon Glacier Vault Lock .
    If there is no vault lock policy set on the vault, the operation returns a 404 Not found error. For more information about vault lock policies, Amazon Glacier Access Control with Vault Lock Policies .
    See also: AWS API Documentation
    
    Exceptions
    Examples
    The example retrieves the attributes from the lock-policy subresource set on the vault named examplevault.
    Expected Output:
    
    :example: response = client.get_vault_lock(
        vaultName='string'
    )
    
    
    :type accountId: string
    :param accountId: The AccountId value is the AWS account ID of the account that owns the vault. You can either specify an AWS account ID or optionally a single \'- \' (hyphen), in which case Amazon S3 Glacier uses the AWS account ID associated with the credentials used to sign the request. If you use an account ID, do not include any hyphens (\'-\') in the ID.\n\nNote: this parameter is set to '-' bydefault if no value is not specified.\n

    :type vaultName: string
    :param vaultName: [REQUIRED]\nThe name of the vault.\n

    :rtype: dict

ReturnsResponse Syntax
{
    'Policy': 'string',
    'State': 'string',
    'ExpirationDate': 'string',
    'CreationDate': 'string'
}


Response Structure

(dict) --
Contains the Amazon S3 Glacier response to your request.

Policy (string) --
The vault lock policy as a JSON string, which uses "" as an escape character.

State (string) --
The state of the vault lock. InProgress or Locked .

ExpirationDate (string) --
The UTC date and time at which the lock ID expires. This value can be null if the vault lock is in a Locked state.

CreationDate (string) --
The UTC date and time at which the vault lock was put into the InProgress state.







Exceptions

Glacier.Client.exceptions.ResourceNotFoundException
Glacier.Client.exceptions.InvalidParameterValueException
Glacier.Client.exceptions.MissingParameterValueException
Glacier.Client.exceptions.ServiceUnavailableException

Examples
The example retrieves the attributes from the lock-policy subresource set on the vault named examplevault.
response = client.get_vault_lock(
    accountId='-',
    vaultName='examplevault',
)

print(response)


Expected Output:
{
    'CreationDate': 'exampledate',
    'ExpirationDate': 'exampledate',
    'Policy': '{"Version":"2012-10-17","Statement":[{"Sid":"Define-vault-lock","Effect":"Deny","Principal":{"AWS":"arn:aws:iam::999999999999:root"},"Action":"glacier:DeleteArchive","Resource":"arn:aws:glacier:us-west-2:999999999999:vaults/examplevault","Condition":{"NumericLessThanEquals":{"glacier:ArchiveAgeinDays":"365"}}}]}',
    'State': 'InProgress',
    'ResponseMetadata': {
        '...': '...',
    },
}



    :return: {
        'Policy': 'string',
        'State': 'string',
        'ExpirationDate': 'string',
        'CreationDate': 'string'
    }
    
    
    :returns: 
    accountId (string) -- The AccountId value is the AWS account ID of the account that owns the vault. You can either specify an AWS account ID or optionally a single \'- \' (hyphen), in which case Amazon S3 Glacier uses the AWS account ID associated with the credentials used to sign the request. If you use an account ID, do not include any hyphens (\'-\') in the ID.
    
    Note: this parameter is set to "-" bydefault if no value is not specified.
    
    vaultName (string) -- [REQUIRED]
    The name of the vault.
    
    
    """
    pass

def get_vault_notifications(accountId=None, vaultName=None):
    """
    This operation retrieves the notification-configuration subresource of the specified vault.
    For information about setting a notification configuration on a vault, see  SetVaultNotifications . If a notification configuration for a vault is not set, the operation returns a 404 Not Found error. For more information about vault notifications, see Configuring Vault Notifications in Amazon S3 Glacier .
    An AWS account has full permission to perform all operations (actions). However, AWS Identity and Access Management (IAM) users don\'t have any permissions by default. You must grant them explicit permission to perform specific actions. For more information, see Access Control Using AWS Identity and Access Management (IAM) .
    For conceptual information and underlying REST API, see Configuring Vault Notifications in Amazon S3 Glacier and Get Vault Notification Configuration in the Amazon Glacier Developer Guide .
    See also: AWS API Documentation
    
    Exceptions
    Examples
    The example retrieves the notification-configuration for the vault named my-vault.
    Expected Output:
    
    :example: response = client.get_vault_notifications(
        vaultName='string'
    )
    
    
    :type accountId: string
    :param accountId: The AccountId value is the AWS account ID of the account that owns the vault. You can either specify an AWS account ID or optionally a single \'- \' (hyphen), in which case Amazon S3 Glacier uses the AWS account ID associated with the credentials used to sign the request. If you use an account ID, do not include any hyphens (\'-\') in the ID.\n\nNote: this parameter is set to '-' bydefault if no value is not specified.\n

    :type vaultName: string
    :param vaultName: [REQUIRED]\nThe name of the vault.\n

    :rtype: dict

ReturnsResponse Syntax
{
    'vaultNotificationConfig': {
        'SNSTopic': 'string',
        'Events': [
            'string',
        ]
    }
}


Response Structure

(dict) --
Contains the Amazon S3 Glacier response to your request.

vaultNotificationConfig (dict) --
Returns the notification configuration set on the vault.

SNSTopic (string) --
The Amazon Simple Notification Service (Amazon SNS) topic Amazon Resource Name (ARN).

Events (list) --
A list of one or more events for which Amazon S3 Glacier will send a notification to the specified Amazon SNS topic.

(string) --










Exceptions

Glacier.Client.exceptions.ResourceNotFoundException
Glacier.Client.exceptions.InvalidParameterValueException
Glacier.Client.exceptions.MissingParameterValueException
Glacier.Client.exceptions.ServiceUnavailableException

Examples
The example retrieves the notification-configuration for the vault named my-vault.
response = client.get_vault_notifications(
    accountId='-',
    vaultName='my-vault',
)

print(response)


Expected Output:
{
    'vaultNotificationConfig': {
        'Events': [
            'InventoryRetrievalCompleted',
            'ArchiveRetrievalCompleted',
        ],
        'SNSTopic': 'arn:aws:sns:us-west-2:0123456789012:my-vault',
    },
    'ResponseMetadata': {
        '...': '...',
    },
}



    :return: {
        'vaultNotificationConfig': {
            'SNSTopic': 'string',
            'Events': [
                'string',
            ]
        }
    }
    
    
    :returns: 
    (string) --
    
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

def initiate_job(accountId=None, vaultName=None, jobParameters=None):
    """
    This operation initiates a job of the specified type, which can be a select, an archival retrieval, or a vault retrieval. For more information about using this operation, see the documentation for the underlying REST API Initiate a Job .
    See also: AWS API Documentation
    
    Exceptions
    Examples
    The example initiates an inventory-retrieval job for the vault named examplevault.
    Expected Output:
    
    :example: response = client.initiate_job(
        vaultName='string',
        jobParameters={
            'Format': 'string',
            'Type': 'string',
            'ArchiveId': 'string',
            'Description': 'string',
            'SNSTopic': 'string',
            'RetrievalByteRange': 'string',
            'Tier': 'string',
            'InventoryRetrievalParameters': {
                'StartDate': 'string',
                'EndDate': 'string',
                'Limit': 'string',
                'Marker': 'string'
            },
            'SelectParameters': {
                'InputSerialization': {
                    'csv': {
                        'FileHeaderInfo': 'USE'|'IGNORE'|'NONE',
                        'Comments': 'string',
                        'QuoteEscapeCharacter': 'string',
                        'RecordDelimiter': 'string',
                        'FieldDelimiter': 'string',
                        'QuoteCharacter': 'string'
                    }
                },
                'ExpressionType': 'SQL',
                'Expression': 'string',
                'OutputSerialization': {
                    'csv': {
                        'QuoteFields': 'ALWAYS'|'ASNEEDED',
                        'QuoteEscapeCharacter': 'string',
                        'RecordDelimiter': 'string',
                        'FieldDelimiter': 'string',
                        'QuoteCharacter': 'string'
                    }
                }
            },
            'OutputLocation': {
                'S3': {
                    'BucketName': 'string',
                    'Prefix': 'string',
                    'Encryption': {
                        'EncryptionType': 'aws:kms'|'AES256',
                        'KMSKeyId': 'string',
                        'KMSContext': 'string'
                    },
                    'CannedACL': 'private'|'public-read'|'public-read-write'|'aws-exec-read'|'authenticated-read'|'bucket-owner-read'|'bucket-owner-full-control',
                    'AccessControlList': [
                        {
                            'Grantee': {
                                'Type': 'AmazonCustomerByEmail'|'CanonicalUser'|'Group',
                                'DisplayName': 'string',
                                'URI': 'string',
                                'ID': 'string',
                                'EmailAddress': 'string'
                            },
                            'Permission': 'FULL_CONTROL'|'WRITE'|'WRITE_ACP'|'READ'|'READ_ACP'
                        },
                    ],
                    'Tagging': {
                        'string': 'string'
                    },
                    'UserMetadata': {
                        'string': 'string'
                    },
                    'StorageClass': 'STANDARD'|'REDUCED_REDUNDANCY'|'STANDARD_IA'
                }
            }
        }
    )
    
    
    :type accountId: string
    :param accountId: The AccountId value is the AWS account ID of the account that owns the vault. You can either specify an AWS account ID or optionally a single \'- \' (hyphen), in which case Amazon S3 Glacier uses the AWS account ID associated with the credentials used to sign the request. If you use an account ID, do not include any hyphens (\'-\') in the ID.\n\nNote: this parameter is set to '-' bydefault if no value is not specified.\n

    :type vaultName: string
    :param vaultName: [REQUIRED]\nThe name of the vault.\n

    :type jobParameters: dict
    :param jobParameters: Provides options for specifying job information.\n\nFormat (string) --When initiating a job to retrieve a vault inventory, you can optionally add this parameter to your request to specify the output format. If you are initiating an inventory job and do not specify a Format field, JSON is the default format. Valid values are 'CSV' and 'JSON'.\n\nType (string) --The job type. You can initiate a job to perform a select query on an archive, retrieve an archive, or get an inventory of a vault. Valid values are 'select', 'archive-retrieval' and 'inventory-retrieval'.\n\nArchiveId (string) --The ID of the archive that you want to retrieve. This field is required only if Type is set to select or archive-retrieval code>. An error occurs if you specify this request parameter for an inventory retrieval job request.\n\nDescription (string) --The optional description for the job. The description must be less than or equal to 1,024 bytes. The allowable characters are 7-bit ASCII without control codes-specifically, ASCII values 32-126 decimal or 0x20-0x7E hexadecimal.\n\nSNSTopic (string) --The Amazon SNS topic ARN to which Amazon S3 Glacier sends a notification when the job is completed and the output is ready for you to download. The specified topic publishes the notification to its subscribers. The SNS topic must exist.\n\nRetrievalByteRange (string) --The byte range to retrieve for an archive retrieval. in the form 'StartByteValue -EndByteValue ' If not specified, the whole archive is retrieved. If specified, the byte range must be megabyte (1024*1024) aligned which means that StartByteValue must be divisible by 1 MB and EndByteValue plus 1 must be divisible by 1 MB or be the end of the archive specified as the archive byte size value minus 1. If RetrievalByteRange is not megabyte aligned, this operation returns a 400 response.\nAn error occurs if you specify this field for an inventory retrieval job request.\n\nTier (string) --The tier to use for a select or an archive retrieval job. Valid values are Expedited , Standard , or Bulk . Standard is the default.\n\nInventoryRetrievalParameters (dict) --Input parameters used for range inventory retrieval.\n\nStartDate (string) --The start of the date range in UTC for vault inventory retrieval that includes archives created on or after this date. This value should be a string in the ISO 8601 date format, for example 2013-03-20T17:03:43Z .\n\nEndDate (string) --The end of the date range in UTC for vault inventory retrieval that includes archives created before this date. This value should be a string in the ISO 8601 date format, for example 2013-03-20T17:03:43Z .\n\nLimit (string) --Specifies the maximum number of inventory items returned per vault inventory retrieval request. Valid values are greater than or equal to 1.\n\nMarker (string) --An opaque string that represents where to continue pagination of the vault inventory retrieval results. You use the marker in a new InitiateJob request to obtain additional inventory items. If there are no more inventory items, this value is null .\n\n\n\nSelectParameters (dict) --Contains the parameters that define a job.\n\nInputSerialization (dict) --Describes the serialization format of the object.\n\ncsv (dict) --Describes the serialization of a CSV-encoded object.\n\nFileHeaderInfo (string) --Describes the first line of input. Valid values are None , Ignore , and Use .\n\nComments (string) --A single character used to indicate that a row should be ignored when the character is present at the start of that row.\n\nQuoteEscapeCharacter (string) --A single character used for escaping the quotation-mark character inside an already escaped value.\n\nRecordDelimiter (string) --A value used to separate individual records from each other.\n\nFieldDelimiter (string) --A value used to separate individual fields from each other within a record.\n\nQuoteCharacter (string) --A value used as an escape character where the field delimiter is part of the value.\n\n\n\n\n\nExpressionType (string) --The type of the provided expression, for example SQL .\n\nExpression (string) --The expression that is used to select the object.\n\nOutputSerialization (dict) --Describes how the results of the select job are serialized.\n\ncsv (dict) --Describes the serialization of CSV-encoded query results.\n\nQuoteFields (string) --A value that indicates whether all output fields should be contained within quotation marks.\n\nQuoteEscapeCharacter (string) --A single character used for escaping the quotation-mark character inside an already escaped value.\n\nRecordDelimiter (string) --A value used to separate individual records from each other.\n\nFieldDelimiter (string) --A value used to separate individual fields from each other within a record.\n\nQuoteCharacter (string) --A value used as an escape character where the field delimiter is part of the value.\n\n\n\n\n\n\n\nOutputLocation (dict) --Contains information about the location where the select job results are stored.\n\nS3 (dict) --Describes an S3 location that will receive the results of the job request.\n\nBucketName (string) --The name of the Amazon S3 bucket where the job results are stored.\n\nPrefix (string) --The prefix that is prepended to the results for this request.\n\nEncryption (dict) --Contains information about the encryption used to store the job results in Amazon S3.\n\nEncryptionType (string) --The server-side encryption algorithm used when storing job results in Amazon S3, for example AES256 or aws:kms .\n\nKMSKeyId (string) --The AWS KMS key ID to use for object encryption. All GET and PUT requests for an object protected by AWS KMS fail if not made by using Secure Sockets Layer (SSL) or Signature Version 4.\n\nKMSContext (string) --Optional. If the encryption type is aws:kms , you can use this value to specify the encryption context for the job results.\n\n\n\nCannedACL (string) --The canned access control list (ACL) to apply to the job results.\n\nAccessControlList (list) --A list of grants that control access to the staged results.\n\n(dict) --Contains information about a grant.\n\nGrantee (dict) --The grantee.\n\nType (string) -- [REQUIRED]Type of grantee\n\nDisplayName (string) --Screen name of the grantee.\n\nURI (string) --URI of the grantee group.\n\nID (string) --The canonical user ID of the grantee.\n\nEmailAddress (string) --Email address of the grantee.\n\n\n\nPermission (string) --Specifies the permission given to the grantee.\n\n\n\n\n\nTagging (dict) --The tag-set that is applied to the job results.\n\n(string) --\n(string) --\n\n\n\n\nUserMetadata (dict) --A map of metadata to store with the job results in Amazon S3.\n\n(string) --\n(string) --\n\n\n\n\nStorageClass (string) --The storage class used to store the job results.\n\n\n\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'location': 'string',
    'jobId': 'string',
    'jobOutputPath': 'string'
}


Response Structure

(dict) --
Contains the Amazon S3 Glacier response to your request.

location (string) --
The relative URI path of the job.

jobId (string) --
The ID of the job.

jobOutputPath (string) --
The path to the location of where the select results are stored.







Exceptions

Glacier.Client.exceptions.ResourceNotFoundException
Glacier.Client.exceptions.PolicyEnforcedException
Glacier.Client.exceptions.InvalidParameterValueException
Glacier.Client.exceptions.MissingParameterValueException
Glacier.Client.exceptions.InsufficientCapacityException
Glacier.Client.exceptions.ServiceUnavailableException

Examples
The example initiates an inventory-retrieval job for the vault named examplevault.
response = client.initiate_job(
    accountId='-',
    jobParameters={
        'Description': 'My inventory job',
        'Format': 'CSV',
        'SNSTopic': 'arn:aws:sns:us-west-2:111111111111:Glacier-InventoryRetrieval-topic-Example',
        'Type': 'inventory-retrieval',
    },
    vaultName='examplevault',
)

print(response)


Expected Output:
{
    'jobId': ' HkF9p6o7yjhFx-K3CGl6fuSm6VzW9T7esGQfco8nUXVYwS0jlb5gq1JZ55yHgt5vP54ZShjoQzQVVh7vEXAMPLEjobID',
    'location': '/111122223333/vaults/examplevault/jobs/HkF9p6o7yjhFx-K3CGl6fuSm6VzW9T7esGQfco8nUXVYwS0jlb5gq1JZ55yHgt5vP54ZShjoQzQVVh7vEXAMPLEjobID',
    'ResponseMetadata': {
        '...': '...',
    },
}



    :return: {
        'location': 'string',
        'jobId': 'string',
        'jobOutputPath': 'string'
    }
    
    
    :returns: 
    Glacier.Client.exceptions.ResourceNotFoundException
    Glacier.Client.exceptions.PolicyEnforcedException
    Glacier.Client.exceptions.InvalidParameterValueException
    Glacier.Client.exceptions.MissingParameterValueException
    Glacier.Client.exceptions.InsufficientCapacityException
    Glacier.Client.exceptions.ServiceUnavailableException
    
    """
    pass

def initiate_multipart_upload(accountId=None, vaultName=None, archiveDescription=None, partSize=None):
    """
    This operation initiates a multipart upload. Amazon S3 Glacier creates a multipart upload resource and returns its ID in the response. The multipart upload ID is used in subsequent requests to upload parts of an archive (see  UploadMultipartPart ).
    When you initiate a multipart upload, you specify the part size in number of bytes. The part size must be a megabyte (1024 KB) multiplied by a power of 2-for example, 1048576 (1 MB), 2097152 (2 MB), 4194304 (4 MB), 8388608 (8 MB), and so on. The minimum allowable part size is 1 MB, and the maximum is 4 GB.
    Every part you upload to this resource (see  UploadMultipartPart ), except the last one, must have the same size. The last one can be the same size or smaller. For example, suppose you want to upload a 16.2 MB file. If you initiate the multipart upload with a part size of 4 MB, you will upload four parts of 4 MB each and one part of 0.2 MB.
    After you complete the multipart upload, Amazon S3 Glacier (Glacier) removes the multipart upload resource referenced by the ID. Glacier also removes the multipart upload resource if you cancel the multipart upload or it may be removed if there is no activity for a period of 24 hours.
    An AWS account has full permission to perform all operations (actions). However, AWS Identity and Access Management (IAM) users don\'t have any permissions by default. You must grant them explicit permission to perform specific actions. For more information, see Access Control Using AWS Identity and Access Management (IAM) .
    For conceptual information and underlying REST API, see Uploading Large Archives in Parts (Multipart Upload) and Initiate Multipart Upload in the Amazon Glacier Developer Guide .
    See also: AWS API Documentation
    
    Exceptions
    Examples
    The example initiates a multipart upload to a vault named my-vault with a part size of 1 MiB (1024 x 1024 bytes) per file.
    Expected Output:
    
    :example: response = client.initiate_multipart_upload(
        vaultName='string',
        archiveDescription='string',
        partSize='string'
    )
    
    
    :type accountId: string
    :param accountId: The AccountId value is the AWS account ID of the account that owns the vault. You can either specify an AWS account ID or optionally a single \'- \' (hyphen), in which case Amazon S3 Glacier uses the AWS account ID associated with the credentials used to sign the request. If you use an account ID, do not include any hyphens (\'-\') in the ID.\n\nNote: this parameter is set to '-' bydefault if no value is not specified.\n

    :type vaultName: string
    :param vaultName: [REQUIRED]\nThe name of the vault.\n

    :type archiveDescription: string
    :param archiveDescription: The archive description that you are uploading in parts.\nThe part size must be a megabyte (1024 KB) multiplied by a power of 2, for example 1048576 (1 MB), 2097152 (2 MB), 4194304 (4 MB), 8388608 (8 MB), and so on. The minimum allowable part size is 1 MB, and the maximum is 4 GB (4096 MB).\n

    :type partSize: string
    :param partSize: The size of each part except the last, in bytes. The last part can be smaller than this part size.

    :rtype: dict

ReturnsResponse Syntax
{
    'location': 'string',
    'uploadId': 'string'
}


Response Structure

(dict) --
The Amazon S3 Glacier response to your request.

location (string) --
The relative URI path of the multipart upload ID Amazon S3 Glacier created.

uploadId (string) --
The ID of the multipart upload. This value is also included as part of the location.







Exceptions

Glacier.Client.exceptions.ResourceNotFoundException
Glacier.Client.exceptions.InvalidParameterValueException
Glacier.Client.exceptions.MissingParameterValueException
Glacier.Client.exceptions.ServiceUnavailableException

Examples
The example initiates a multipart upload to a vault named my-vault with a part size of 1 MiB (1024 x 1024 bytes) per file.
response = client.initiate_multipart_upload(
    accountId='-',
    partSize='1048576',
    vaultName='my-vault',
)

print(response)


Expected Output:
{
    'location': '/111122223333/vaults/my-vault/multipart-uploads/19gaRezEXAMPLES6Ry5YYdqthHOC_kGRCT03L9yetr220UmPtBYKk-OssZtLqyFu7sY1_lR7vgFuJV6NtcV5zpsJ',
    'uploadId': '19gaRezEXAMPLES6Ry5YYdqthHOC_kGRCT03L9yetr220UmPtBYKk-OssZtLqyFu7sY1_lR7vgFuJV6NtcV5zpsJ',
    'ResponseMetadata': {
        '...': '...',
    },
}



    :return: {
        'location': 'string',
        'uploadId': 'string'
    }
    
    
    :returns: 
    Glacier.Client.exceptions.ResourceNotFoundException
    Glacier.Client.exceptions.InvalidParameterValueException
    Glacier.Client.exceptions.MissingParameterValueException
    Glacier.Client.exceptions.ServiceUnavailableException
    
    """
    pass

def initiate_vault_lock(accountId=None, vaultName=None, policy=None):
    """
    This operation initiates the vault locking process by doing the following:
    You can set one vault lock policy for each vault and this policy can be up to 20 KB in size. For more information about vault lock policies, see Amazon Glacier Access Control with Vault Lock Policies .
    You must complete the vault locking process within 24 hours after the vault lock enters the InProgress state. After the 24 hour window ends, the lock ID expires, the vault automatically exits the InProgress state, and the vault lock policy is removed from the vault. You call  CompleteVaultLock to complete the vault locking process by setting the state of the vault lock to Locked .
    After a vault lock is in the Locked state, you cannot initiate a new vault lock for the vault.
    You can abort the vault locking process by calling  AbortVaultLock . You can get the state of the vault lock by calling  GetVaultLock . For more information about the vault locking process, Amazon Glacier Vault Lock .
    If this operation is called when the vault lock is in the InProgress state, the operation returns an AccessDeniedException error. When the vault lock is in the InProgress state you must call  AbortVaultLock before you can initiate a new vault lock policy.
    See also: AWS API Documentation
    
    Exceptions
    Examples
    The example initiates the vault locking process for the vault named my-vault.
    Expected Output:
    
    :example: response = client.initiate_vault_lock(
        vaultName='string',
        policy={
            'Policy': 'string'
        }
    )
    
    
    :type accountId: string
    :param accountId: The AccountId value is the AWS account ID. This value must match the AWS account ID associated with the credentials used to sign the request. You can either specify an AWS account ID or optionally a single \'- \' (hyphen), in which case Amazon Glacier uses the AWS account ID associated with the credentials used to sign the request. If you specify your account ID, do not include any hyphens (\'-\') in the ID.\n\nNote: this parameter is set to '-' bydefault if no value is not specified.\n

    :type vaultName: string
    :param vaultName: [REQUIRED]\nThe name of the vault.\n

    :type policy: dict
    :param policy: The vault lock policy as a JSON string, which uses '' as an escape character.\n\nPolicy (string) --The vault lock policy.\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'lockId': 'string'
}


Response Structure

(dict) --
Contains the Amazon S3 Glacier response to your request.

lockId (string) --
The lock ID, which is used to complete the vault locking process.







Exceptions

Glacier.Client.exceptions.ResourceNotFoundException
Glacier.Client.exceptions.InvalidParameterValueException
Glacier.Client.exceptions.MissingParameterValueException
Glacier.Client.exceptions.ServiceUnavailableException

Examples
The example initiates the vault locking process for the vault named my-vault.
response = client.initiate_vault_lock(
    accountId='-',
    policy={
        'Policy': '{"Version":"2012-10-17","Statement":[{"Sid":"Define-vault-lock","Effect":"Deny","Principal":{"AWS":"arn:aws:iam::999999999999:root"},"Action":"glacier:DeleteArchive","Resource":"arn:aws:glacier:us-west-2:999999999999:vaults/examplevault","Condition":{"NumericLessThanEquals":{"glacier:ArchiveAgeinDays":"365"}}}]}',
    },
    vaultName='my-vault',
)

print(response)


Expected Output:
{
    'lockId': 'AE863rKkWZU53SLW5be4DUcW',
    'ResponseMetadata': {
        '...': '...',
    },
}



    :return: {
        'lockId': 'string'
    }
    
    
    :returns: 
    accountId (string) -- The AccountId value is the AWS account ID. This value must match the AWS account ID associated with the credentials used to sign the request. You can either specify an AWS account ID or optionally a single \'- \' (hyphen), in which case Amazon Glacier uses the AWS account ID associated with the credentials used to sign the request. If you specify your account ID, do not include any hyphens (\'-\') in the ID.
    
    Note: this parameter is set to "-" bydefault if no value is not specified.
    
    vaultName (string) -- [REQUIRED]
    The name of the vault.
    
    policy (dict) -- The vault lock policy as a JSON string, which uses "" as an escape character.
    
    Policy (string) --The vault lock policy.
    
    
    
    
    """
    pass

def list_jobs(accountId=None, vaultName=None, limit=None, marker=None, statuscode=None, completed=None):
    """
    This operation lists jobs for a vault, including jobs that are in-progress and jobs that have recently finished. The List Job operation returns a list of these jobs sorted by job initiation time.
    The List Jobs operation supports pagination. You should always check the response Marker field. If there are no more jobs to list, the Marker field is set to null . If there are more jobs to list, the Marker field is set to a non-null value, which you can use to continue the pagination of the list. To return a list of jobs that begins at a specific job, set the marker request parameter to the Marker value for that job that you obtained from a previous List Jobs request.
    You can set a maximum limit for the number of jobs returned in the response by specifying the limit parameter in the request. The default limit is 50. The number of jobs returned might be fewer than the limit, but the number of returned jobs never exceeds the limit.
    Additionally, you can filter the jobs list returned by specifying the optional statuscode parameter or completed parameter, or both. Using the statuscode parameter, you can specify to return only jobs that match either the InProgress , Succeeded , or Failed status. Using the completed parameter, you can specify to return only jobs that were completed (true ) or jobs that were not completed (false ).
    For more information about using this operation, see the documentation for the underlying REST API List Jobs .
    See also: AWS API Documentation
    
    Exceptions
    Examples
    The example lists jobs for the vault named my-vault.
    Expected Output:
    
    :example: response = client.list_jobs(
        vaultName='string',
        limit='string',
        marker='string',
        statuscode='string',
        completed='string'
    )
    
    
    :type accountId: string
    :param accountId: The AccountId value is the AWS account ID of the account that owns the vault. You can either specify an AWS account ID or optionally a single \'- \' (hyphen), in which case Amazon S3 Glacier uses the AWS account ID associated with the credentials used to sign the request. If you use an account ID, do not include any hyphens (\'-\') in the ID.\n\nNote: this parameter is set to '-' bydefault if no value is not specified.\n

    :type vaultName: string
    :param vaultName: [REQUIRED]\nThe name of the vault.\n

    :type limit: string
    :param limit: The maximum number of jobs to be returned. The default limit is 50. The number of jobs returned might be fewer than the specified limit, but the number of returned jobs never exceeds the limit.

    :type marker: string
    :param marker: An opaque string used for pagination. This value specifies the job at which the listing of jobs should begin. Get the marker value from a previous List Jobs response. You only need to include the marker if you are continuing the pagination of results started in a previous List Jobs request.

    :type statuscode: string
    :param statuscode: The type of job status to return. You can specify the following values: InProgress , Succeeded , or Failed .

    :type completed: string
    :param completed: The state of the jobs to return. You can specify true or false .

    :rtype: dict

ReturnsResponse Syntax
{
    'JobList': [
        {
            'JobId': 'string',
            'JobDescription': 'string',
            'Action': 'ArchiveRetrieval'|'InventoryRetrieval'|'Select',
            'ArchiveId': 'string',
            'VaultARN': 'string',
            'CreationDate': 'string',
            'Completed': True|False,
            'StatusCode': 'InProgress'|'Succeeded'|'Failed',
            'StatusMessage': 'string',
            'ArchiveSizeInBytes': 123,
            'InventorySizeInBytes': 123,
            'SNSTopic': 'string',
            'CompletionDate': 'string',
            'SHA256TreeHash': 'string',
            'ArchiveSHA256TreeHash': 'string',
            'RetrievalByteRange': 'string',
            'Tier': 'string',
            'InventoryRetrievalParameters': {
                'Format': 'string',
                'StartDate': 'string',
                'EndDate': 'string',
                'Limit': 'string',
                'Marker': 'string'
            },
            'JobOutputPath': 'string',
            'SelectParameters': {
                'InputSerialization': {
                    'csv': {
                        'FileHeaderInfo': 'USE'|'IGNORE'|'NONE',
                        'Comments': 'string',
                        'QuoteEscapeCharacter': 'string',
                        'RecordDelimiter': 'string',
                        'FieldDelimiter': 'string',
                        'QuoteCharacter': 'string'
                    }
                },
                'ExpressionType': 'SQL',
                'Expression': 'string',
                'OutputSerialization': {
                    'csv': {
                        'QuoteFields': 'ALWAYS'|'ASNEEDED',
                        'QuoteEscapeCharacter': 'string',
                        'RecordDelimiter': 'string',
                        'FieldDelimiter': 'string',
                        'QuoteCharacter': 'string'
                    }
                }
            },
            'OutputLocation': {
                'S3': {
                    'BucketName': 'string',
                    'Prefix': 'string',
                    'Encryption': {
                        'EncryptionType': 'aws:kms'|'AES256',
                        'KMSKeyId': 'string',
                        'KMSContext': 'string'
                    },
                    'CannedACL': 'private'|'public-read'|'public-read-write'|'aws-exec-read'|'authenticated-read'|'bucket-owner-read'|'bucket-owner-full-control',
                    'AccessControlList': [
                        {
                            'Grantee': {
                                'Type': 'AmazonCustomerByEmail'|'CanonicalUser'|'Group',
                                'DisplayName': 'string',
                                'URI': 'string',
                                'ID': 'string',
                                'EmailAddress': 'string'
                            },
                            'Permission': 'FULL_CONTROL'|'WRITE'|'WRITE_ACP'|'READ'|'READ_ACP'
                        },
                    ],
                    'Tagging': {
                        'string': 'string'
                    },
                    'UserMetadata': {
                        'string': 'string'
                    },
                    'StorageClass': 'STANDARD'|'REDUCED_REDUNDANCY'|'STANDARD_IA'
                }
            }
        },
    ],
    'Marker': 'string'
}


Response Structure

(dict) --
Contains the Amazon S3 Glacier response to your request.

JobList (list) --
A list of job objects. Each job object contains metadata describing the job.

(dict) --
Contains the description of an Amazon S3 Glacier job.

JobId (string) --
An opaque string that identifies an Amazon S3 Glacier job.

JobDescription (string) --
The job description provided when initiating the job.

Action (string) --
The job type. This value is either ArchiveRetrieval , InventoryRetrieval , or Select .

ArchiveId (string) --
The archive ID requested for a select job or archive retrieval. Otherwise, this field is null.

VaultARN (string) --
The Amazon Resource Name (ARN) of the vault from which an archive retrieval was requested.

CreationDate (string) --
The UTC date when the job was created. This value is a string representation of ISO 8601 date format, for example "2012-03-20T17:03:43.221Z" .

Completed (boolean) --
The job status. When a job is completed, you get the job\'s output using Get Job Output (GET output).

StatusCode (string) --
The status code can be InProgress , Succeeded , or Failed , and indicates the status of the job.

StatusMessage (string) --
A friendly message that describes the job status.

ArchiveSizeInBytes (integer) --
For an archive retrieval job, this value is the size in bytes of the archive being requested for download. For an inventory retrieval or select job, this value is null.

InventorySizeInBytes (integer) --
For an inventory retrieval job, this value is the size in bytes of the inventory requested for download. For an archive retrieval or select job, this value is null.

SNSTopic (string) --
An Amazon SNS topic that receives notification.

CompletionDate (string) --
The UTC time that the job request completed. While the job is in progress, the value is null.

SHA256TreeHash (string) --
For an archive retrieval job, this value is the checksum of the archive. Otherwise, this value is null.
The SHA256 tree hash value for the requested range of an archive. If the InitiateJob request for an archive specified a tree-hash aligned range, then this field returns a value.
If the whole archive is retrieved, this value is the same as the ArchiveSHA256TreeHash value.
This field is null for the following:

Archive retrieval jobs that specify a range that is not tree-hash aligned
Archival jobs that specify a range that is equal to the whole archive, when the job status is InProgress
Inventory jobs
Select jobs


ArchiveSHA256TreeHash (string) --
The SHA256 tree hash of the entire archive for an archive retrieval. For inventory retrieval or select jobs, this field is null.

RetrievalByteRange (string) --
The retrieved byte range for archive retrieval jobs in the form StartByteValue -EndByteValue . If no range was specified in the archive retrieval, then the whole archive is retrieved. In this case, StartByteValue equals 0 and EndByteValue equals the size of the archive minus 1. For inventory retrieval or select jobs, this field is null.

Tier (string) --
The tier to use for a select or an archive retrieval. Valid values are Expedited , Standard , or Bulk . Standard is the default.

InventoryRetrievalParameters (dict) --
Parameters used for range inventory retrieval.

Format (string) --
The output format for the vault inventory list, which is set by the InitiateJob request when initiating a job to retrieve a vault inventory. Valid values are CSV and JSON .

StartDate (string) --
The start of the date range in Universal Coordinated Time (UTC) for vault inventory retrieval that includes archives created on or after this date. This value should be a string in the ISO 8601 date format, for example 2013-03-20T17:03:43Z .

EndDate (string) --
The end of the date range in UTC for vault inventory retrieval that includes archives created before this date. This value should be a string in the ISO 8601 date format, for example 2013-03-20T17:03:43Z .

Limit (string) --
The maximum number of inventory items returned per vault inventory retrieval request. This limit is set when initiating the job with the a InitiateJob request.

Marker (string) --
An opaque string that represents where to continue pagination of the vault inventory retrieval results. You use the marker in a new InitiateJob request to obtain additional inventory items. If there are no more inventory items, this value is null . For more information, see Range Inventory Retrieval .



JobOutputPath (string) --
Contains the job output location.

SelectParameters (dict) --
Contains the parameters used for a select.

InputSerialization (dict) --
Describes the serialization format of the object.

csv (dict) --
Describes the serialization of a CSV-encoded object.

FileHeaderInfo (string) --
Describes the first line of input. Valid values are None , Ignore , and Use .

Comments (string) --
A single character used to indicate that a row should be ignored when the character is present at the start of that row.

QuoteEscapeCharacter (string) --
A single character used for escaping the quotation-mark character inside an already escaped value.

RecordDelimiter (string) --
A value used to separate individual records from each other.

FieldDelimiter (string) --
A value used to separate individual fields from each other within a record.

QuoteCharacter (string) --
A value used as an escape character where the field delimiter is part of the value.





ExpressionType (string) --
The type of the provided expression, for example SQL .

Expression (string) --
The expression that is used to select the object.

OutputSerialization (dict) --
Describes how the results of the select job are serialized.

csv (dict) --
Describes the serialization of CSV-encoded query results.

QuoteFields (string) --
A value that indicates whether all output fields should be contained within quotation marks.

QuoteEscapeCharacter (string) --
A single character used for escaping the quotation-mark character inside an already escaped value.

RecordDelimiter (string) --
A value used to separate individual records from each other.

FieldDelimiter (string) --
A value used to separate individual fields from each other within a record.

QuoteCharacter (string) --
A value used as an escape character where the field delimiter is part of the value.







OutputLocation (dict) --
Contains the location where the data from the select job is stored.

S3 (dict) --
Describes an S3 location that will receive the results of the job request.

BucketName (string) --
The name of the Amazon S3 bucket where the job results are stored.

Prefix (string) --
The prefix that is prepended to the results for this request.

Encryption (dict) --
Contains information about the encryption used to store the job results in Amazon S3.

EncryptionType (string) --
The server-side encryption algorithm used when storing job results in Amazon S3, for example AES256 or aws:kms .

KMSKeyId (string) --
The AWS KMS key ID to use for object encryption. All GET and PUT requests for an object protected by AWS KMS fail if not made by using Secure Sockets Layer (SSL) or Signature Version 4.

KMSContext (string) --
Optional. If the encryption type is aws:kms , you can use this value to specify the encryption context for the job results.



CannedACL (string) --
The canned access control list (ACL) to apply to the job results.

AccessControlList (list) --
A list of grants that control access to the staged results.

(dict) --
Contains information about a grant.

Grantee (dict) --
The grantee.

Type (string) --
Type of grantee

DisplayName (string) --
Screen name of the grantee.

URI (string) --
URI of the grantee group.

ID (string) --
The canonical user ID of the grantee.

EmailAddress (string) --
Email address of the grantee.



Permission (string) --
Specifies the permission given to the grantee.





Tagging (dict) --
The tag-set that is applied to the job results.

(string) --
(string) --




UserMetadata (dict) --
A map of metadata to store with the job results in Amazon S3.

(string) --
(string) --




StorageClass (string) --
The storage class used to store the job results.









Marker (string) --
An opaque string used for pagination that specifies the job at which the listing of jobs should begin. You get the marker value from a previous List Jobs response. You only need to include the marker if you are continuing the pagination of the results started in a previous List Jobs request.







Exceptions

Glacier.Client.exceptions.ResourceNotFoundException
Glacier.Client.exceptions.InvalidParameterValueException
Glacier.Client.exceptions.MissingParameterValueException
Glacier.Client.exceptions.ServiceUnavailableException

Examples
The example lists jobs for the vault named my-vault.
response = client.list_jobs(
    accountId='-',
    vaultName='my-vault',
)

print(response)


Expected Output:
{
    'JobList': [
        {
            'Action': 'ArchiveRetrieval',
            'ArchiveId': 'kKB7ymWJVpPSwhGP6ycSOAekp9ZYe_--zM_mw6k76ZFGEIWQX-ybtRDvc2VkPSDtfKmQrj0IRQLSGsNuDp-AJVlu2ccmDSyDUmZwKbwbpAdGATGDiB3hHO0bjbGehXTcApVud_wyDw',
            'ArchiveSHA256TreeHash': '9628195fcdbcbbe76cdde932d4646fa7de5f219fb39823836d81f0cc0e18aa67',
            'ArchiveSizeInBytes': 3145728,
            'Completed': False,
            'CreationDate': '2015-07-17T21:16:13.840Z',
            'JobDescription': 'Retrieve archive on 2015-07-17',
            'JobId': 'l7IL5-EkXyEY9Ws95fClzIbk2O5uLYaFdAYOi-azsX_Z8V6NH4yERHzars8wTKYQMX6nBDI9cMNHzyZJO59-8N9aHWav',
            'RetrievalByteRange': '0-3145727',
            'SHA256TreeHash': '9628195fcdbcbbe76cdde932d4646fa7de5f219fb39823836d81f0cc0e18aa67',
            'SNSTopic': 'arn:aws:sns:us-west-2:0123456789012:my-vault',
            'StatusCode': 'InProgress',
            'VaultARN': 'arn:aws:glacier:us-west-2:0123456789012:vaults/my-vault',
        },
        {
            'Action': 'InventoryRetrieval',
            'Completed': False,
            'CreationDate': '2015-07-17T20:23:41.616Z',
            'InventoryRetrievalParameters': {
                'Format': 'JSON',
            },
            'JobId': 'zbxcm3Z_3z5UkoroF7SuZKrxgGoDc3RloGduS7Eg-RO47Yc6FxsdGBgf_Q2DK5Ejh18CnTS5XW4_XqlNHS61dsO4CnMW',
            'StatusCode': 'InProgress',
            'VaultARN': 'arn:aws:glacier:us-west-2:0123456789012:vaults/my-vault',
        },
    ],
    'ResponseMetadata': {
        '...': '...',
    },
}



    :return: {
        'JobList': [
            {
                'JobId': 'string',
                'JobDescription': 'string',
                'Action': 'ArchiveRetrieval'|'InventoryRetrieval'|'Select',
                'ArchiveId': 'string',
                'VaultARN': 'string',
                'CreationDate': 'string',
                'Completed': True|False,
                'StatusCode': 'InProgress'|'Succeeded'|'Failed',
                'StatusMessage': 'string',
                'ArchiveSizeInBytes': 123,
                'InventorySizeInBytes': 123,
                'SNSTopic': 'string',
                'CompletionDate': 'string',
                'SHA256TreeHash': 'string',
                'ArchiveSHA256TreeHash': 'string',
                'RetrievalByteRange': 'string',
                'Tier': 'string',
                'InventoryRetrievalParameters': {
                    'Format': 'string',
                    'StartDate': 'string',
                    'EndDate': 'string',
                    'Limit': 'string',
                    'Marker': 'string'
                },
                'JobOutputPath': 'string',
                'SelectParameters': {
                    'InputSerialization': {
                        'csv': {
                            'FileHeaderInfo': 'USE'|'IGNORE'|'NONE',
                            'Comments': 'string',
                            'QuoteEscapeCharacter': 'string',
                            'RecordDelimiter': 'string',
                            'FieldDelimiter': 'string',
                            'QuoteCharacter': 'string'
                        }
                    },
                    'ExpressionType': 'SQL',
                    'Expression': 'string',
                    'OutputSerialization': {
                        'csv': {
                            'QuoteFields': 'ALWAYS'|'ASNEEDED',
                            'QuoteEscapeCharacter': 'string',
                            'RecordDelimiter': 'string',
                            'FieldDelimiter': 'string',
                            'QuoteCharacter': 'string'
                        }
                    }
                },
                'OutputLocation': {
                    'S3': {
                        'BucketName': 'string',
                        'Prefix': 'string',
                        'Encryption': {
                            'EncryptionType': 'aws:kms'|'AES256',
                            'KMSKeyId': 'string',
                            'KMSContext': 'string'
                        },
                        'CannedACL': 'private'|'public-read'|'public-read-write'|'aws-exec-read'|'authenticated-read'|'bucket-owner-read'|'bucket-owner-full-control',
                        'AccessControlList': [
                            {
                                'Grantee': {
                                    'Type': 'AmazonCustomerByEmail'|'CanonicalUser'|'Group',
                                    'DisplayName': 'string',
                                    'URI': 'string',
                                    'ID': 'string',
                                    'EmailAddress': 'string'
                                },
                                'Permission': 'FULL_CONTROL'|'WRITE'|'WRITE_ACP'|'READ'|'READ_ACP'
                            },
                        ],
                        'Tagging': {
                            'string': 'string'
                        },
                        'UserMetadata': {
                            'string': 'string'
                        },
                        'StorageClass': 'STANDARD'|'REDUCED_REDUNDANCY'|'STANDARD_IA'
                    }
                }
            },
        ],
        'Marker': 'string'
    }
    
    
    :returns: 
    Archive retrieval jobs that specify a range that is not tree-hash aligned
    Archival jobs that specify a range that is equal to the whole archive, when the job status is InProgress
    Inventory jobs
    Select jobs
    
    """
    pass

def list_multipart_uploads(accountId=None, vaultName=None, marker=None, limit=None):
    """
    This operation lists in-progress multipart uploads for the specified vault. An in-progress multipart upload is a multipart upload that has been initiated by an  InitiateMultipartUpload request, but has not yet been completed or aborted. The list returned in the List Multipart Upload response has no guaranteed order.
    The List Multipart Uploads operation supports pagination. By default, this operation returns up to 50 multipart uploads in the response. You should always check the response for a marker at which to continue the list; if there are no more items the marker is null . To return a list of multipart uploads that begins at a specific upload, set the marker request parameter to the value you obtained from a previous List Multipart Upload request. You can also limit the number of uploads returned in the response by specifying the limit parameter in the request.
    Note the difference between this operation and listing parts ( ListParts ). The List Multipart Uploads operation lists all multipart uploads for a vault and does not require a multipart upload ID. The List Parts operation requires a multipart upload ID since parts are associated with a single upload.
    An AWS account has full permission to perform all operations (actions). However, AWS Identity and Access Management (IAM) users don\'t have any permissions by default. You must grant them explicit permission to perform specific actions. For more information, see Access Control Using AWS Identity and Access Management (IAM) .
    For conceptual information and the underlying REST API, see Working with Archives in Amazon S3 Glacier and List Multipart Uploads in the Amazon Glacier Developer Guide .
    See also: AWS API Documentation
    
    Exceptions
    Examples
    The example lists all the in-progress multipart uploads for the vault named examplevault.
    Expected Output:
    
    :example: response = client.list_multipart_uploads(
        vaultName='string',
        marker='string',
        limit='string'
    )
    
    
    :type accountId: string
    :param accountId: The AccountId value is the AWS account ID of the account that owns the vault. You can either specify an AWS account ID or optionally a single \'- \' (hyphen), in which case Amazon S3 Glacier uses the AWS account ID associated with the credentials used to sign the request. If you use an account ID, do not include any hyphens (\'-\') in the ID.\n\nNote: this parameter is set to '-' bydefault if no value is not specified.\n

    :type vaultName: string
    :param vaultName: [REQUIRED]\nThe name of the vault.\n

    :type marker: string
    :param marker: An opaque string used for pagination. This value specifies the upload at which the listing of uploads should begin. Get the marker value from a previous List Uploads response. You need only include the marker if you are continuing the pagination of results started in a previous List Uploads request.

    :type limit: string
    :param limit: Specifies the maximum number of uploads returned in the response body. If this value is not specified, the List Uploads operation returns up to 50 uploads.

    :rtype: dict

ReturnsResponse Syntax
{
    'UploadsList': [
        {
            'MultipartUploadId': 'string',
            'VaultARN': 'string',
            'ArchiveDescription': 'string',
            'PartSizeInBytes': 123,
            'CreationDate': 'string'
        },
    ],
    'Marker': 'string'
}


Response Structure

(dict) --
Contains the Amazon S3 Glacier response to your request.

UploadsList (list) --
A list of in-progress multipart uploads.

(dict) --
A list of in-progress multipart uploads for a vault.

MultipartUploadId (string) --
The ID of a multipart upload.

VaultARN (string) --
The Amazon Resource Name (ARN) of the vault that contains the archive.

ArchiveDescription (string) --
The description of the archive that was specified in the Initiate Multipart Upload request.

PartSizeInBytes (integer) --
The part size, in bytes, specified in the Initiate Multipart Upload request. This is the size of all the parts in the upload except the last part, which may be smaller than this size.

CreationDate (string) --
The UTC time at which the multipart upload was initiated.





Marker (string) --
An opaque string that represents where to continue pagination of the results. You use the marker in a new List Multipart Uploads request to obtain more uploads in the list. If there are no more uploads, this value is null .







Exceptions

Glacier.Client.exceptions.ResourceNotFoundException
Glacier.Client.exceptions.InvalidParameterValueException
Glacier.Client.exceptions.MissingParameterValueException
Glacier.Client.exceptions.ServiceUnavailableException

Examples
The example lists all the in-progress multipart uploads for the vault named examplevault.
response = client.list_multipart_uploads(
    accountId='-',
    vaultName='examplevault',
)

print(response)


Expected Output:
{
    'Marker': 'null',
    'UploadsList': [
        {
            'ArchiveDescription': 'archive 1',
            'CreationDate': '2012-03-19T23:20:59.130Z',
            'MultipartUploadId': 'xsQdFIRsfJr20CW2AbZBKpRZAFTZSJIMtL2hYf8mvp8dM0m4RUzlaqoEye6g3h3ecqB_zqwB7zLDMeSWhwo65re4C4Ev',
            'PartSizeInBytes': 4194304,
            'VaultARN': 'arn:aws:glacier:us-west-2:012345678901:vaults/examplevault',
        },
        {
            'ArchiveDescription': 'archive 2',
            'CreationDate': '2012-04-01T15:00:00.000Z',
            'MultipartUploadId': 'nPyGOnyFcx67qqX7E-0tSGiRi88hHMOwOxR-_jNyM6RjVMFfV29lFqZ3rNsSaWBugg6OP92pRtufeHdQH7ClIpSF6uJc',
            'PartSizeInBytes': 4194304,
            'VaultARN': 'arn:aws:glacier:us-west-2:012345678901:vaults/examplevault',
        },
        {
            'ArchiveDescription': 'archive 3',
            'CreationDate': '2012-03-20T17:03:43.221Z',
            'MultipartUploadId': 'qt-RBst_7yO8gVIonIBsAxr2t-db0pE4s8MNeGjKjGdNpuU-cdSAcqG62guwV9r5jh5mLyFPzFEitTpNE7iQfHiu1XoV',
            'PartSizeInBytes': 4194304,
            'VaultARN': 'arn:aws:glacier:us-west-2:012345678901:vaults/examplevault',
        },
    ],
    'ResponseMetadata': {
        '...': '...',
    },
}



    :return: {
        'UploadsList': [
            {
                'MultipartUploadId': 'string',
                'VaultARN': 'string',
                'ArchiveDescription': 'string',
                'PartSizeInBytes': 123,
                'CreationDate': 'string'
            },
        ],
        'Marker': 'string'
    }
    
    
    :returns: 
    Glacier.Client.exceptions.ResourceNotFoundException
    Glacier.Client.exceptions.InvalidParameterValueException
    Glacier.Client.exceptions.MissingParameterValueException
    Glacier.Client.exceptions.ServiceUnavailableException
    
    """
    pass

def list_parts(accountId=None, vaultName=None, uploadId=None, marker=None, limit=None):
    """
    This operation lists the parts of an archive that have been uploaded in a specific multipart upload. You can make this request at any time during an in-progress multipart upload before you complete the upload (see  CompleteMultipartUpload . List Parts returns an error for completed uploads. The list returned in the List Parts response is sorted by part range.
    The List Parts operation supports pagination. By default, this operation returns up to 50 uploaded parts in the response. You should always check the response for a marker at which to continue the list; if there are no more items the marker is null . To return a list of parts that begins at a specific part, set the marker request parameter to the value you obtained from a previous List Parts request. You can also limit the number of parts returned in the response by specifying the limit parameter in the request.
    An AWS account has full permission to perform all operations (actions). However, AWS Identity and Access Management (IAM) users don\'t have any permissions by default. You must grant them explicit permission to perform specific actions. For more information, see Access Control Using AWS Identity and Access Management (IAM) .
    For conceptual information and the underlying REST API, see Working with Archives in Amazon S3 Glacier and List Parts in the Amazon Glacier Developer Guide .
    See also: AWS API Documentation
    
    Exceptions
    Examples
    The example lists all the parts of a multipart upload.
    Expected Output:
    
    :example: response = client.list_parts(
        vaultName='string',
        uploadId='string',
        marker='string',
        limit='string'
    )
    
    
    :type accountId: string
    :param accountId: The AccountId value is the AWS account ID of the account that owns the vault. You can either specify an AWS account ID or optionally a single \'- \' (hyphen), in which case Amazon S3 Glacier uses the AWS account ID associated with the credentials used to sign the request. If you use an account ID, do not include any hyphens (\'-\') in the ID.\n\nNote: this parameter is set to '-' bydefault if no value is not specified.\n

    :type vaultName: string
    :param vaultName: [REQUIRED]\nThe name of the vault.\n

    :type uploadId: string
    :param uploadId: [REQUIRED]\nThe upload ID of the multipart upload.\n

    :type marker: string
    :param marker: An opaque string used for pagination. This value specifies the part at which the listing of parts should begin. Get the marker value from the response of a previous List Parts response. You need only include the marker if you are continuing the pagination of results started in a previous List Parts request.

    :type limit: string
    :param limit: The maximum number of parts to be returned. The default limit is 50. The number of parts returned might be fewer than the specified limit, but the number of returned parts never exceeds the limit.

    :rtype: dict

ReturnsResponse Syntax
{
    'MultipartUploadId': 'string',
    'VaultARN': 'string',
    'ArchiveDescription': 'string',
    'PartSizeInBytes': 123,
    'CreationDate': 'string',
    'Parts': [
        {
            'RangeInBytes': 'string',
            'SHA256TreeHash': 'string'
        },
    ],
    'Marker': 'string'
}


Response Structure

(dict) --
Contains the Amazon S3 Glacier response to your request.

MultipartUploadId (string) --
The ID of the upload to which the parts are associated.

VaultARN (string) --
The Amazon Resource Name (ARN) of the vault to which the multipart upload was initiated.

ArchiveDescription (string) --
The description of the archive that was specified in the Initiate Multipart Upload request.

PartSizeInBytes (integer) --
The part size in bytes. This is the same value that you specified in the Initiate Multipart Upload request.

CreationDate (string) --
The UTC time at which the multipart upload was initiated.

Parts (list) --
A list of the part sizes of the multipart upload. Each object in the array contains a RangeBytes and sha256-tree-hash name/value pair.

(dict) --
A list of the part sizes of the multipart upload.

RangeInBytes (string) --
The byte range of a part, inclusive of the upper value of the range.

SHA256TreeHash (string) --
The SHA256 tree hash value that Amazon S3 Glacier calculated for the part. This field is never null .





Marker (string) --
An opaque string that represents where to continue pagination of the results. You use the marker in a new List Parts request to obtain more jobs in the list. If there are no more parts, this value is null .







Exceptions

Glacier.Client.exceptions.ResourceNotFoundException
Glacier.Client.exceptions.InvalidParameterValueException
Glacier.Client.exceptions.MissingParameterValueException
Glacier.Client.exceptions.ServiceUnavailableException

Examples
The example lists all the parts of a multipart upload.
response = client.list_parts(
    accountId='-',
    uploadId='OW2fM5iVylEpFEMM9_HpKowRapC3vn5sSL39_396UW9zLFUWVrnRHaPjUJddQ5OxSHVXjYtrN47NBZ-khxOjyEXAMPLE',
    vaultName='examplevault',
)

print(response)


Expected Output:
{
    'ArchiveDescription': 'archive description',
    'CreationDate': '2012-03-20T17:03:43.221Z',
    'Marker': 'null',
    'MultipartUploadId': 'OW2fM5iVylEpFEMM9_HpKowRapC3vn5sSL39_396UW9zLFUWVrnRHaPjUJddQ5OxSHVXjYtrN47NBZ-khxOjyEXAMPLE',
    'PartSizeInBytes': 4194304,
    'Parts': [
        {
            'RangeInBytes': '0-4194303',
            'SHA256TreeHash': '01d34dabf7be316472c93b1ef80721f5d4',
        },
        {
            'RangeInBytes': '4194304-8388607',
            'SHA256TreeHash': '0195875365afda349fc21c84c099987164',
        },
    ],
    'VaultARN': 'arn:aws:glacier:us-west-2:012345678901:vaults/demo1-vault',
    'ResponseMetadata': {
        '...': '...',
    },
}



    :return: {
        'MultipartUploadId': 'string',
        'VaultARN': 'string',
        'ArchiveDescription': 'string',
        'PartSizeInBytes': 123,
        'CreationDate': 'string',
        'Parts': [
            {
                'RangeInBytes': 'string',
                'SHA256TreeHash': 'string'
            },
        ],
        'Marker': 'string'
    }
    
    
    :returns: 
    Glacier.Client.exceptions.ResourceNotFoundException
    Glacier.Client.exceptions.InvalidParameterValueException
    Glacier.Client.exceptions.MissingParameterValueException
    Glacier.Client.exceptions.ServiceUnavailableException
    
    """
    pass

def list_provisioned_capacity(accountId=None):
    """
    This operation lists the provisioned capacity units for the specified AWS account.
    See also: AWS API Documentation
    
    Exceptions
    Examples
    The example lists the provisioned capacity units for an account.
    Expected Output:
    
    :example: response = client.list_provisioned_capacity(
    
    )
    
    
    :type accountId: string
    :param accountId: The AWS account ID of the account that owns the vault. You can either specify an AWS account ID or optionally a single \'-\' (hyphen), in which case Amazon S3 Glacier uses the AWS account ID associated with the credentials used to sign the request. If you use an account ID, don\'t include any hyphens (\'-\') in the ID.\n\nNote: this parameter is set to '-' bydefault if no value is not specified.\n

    :rtype: dict
ReturnsResponse Syntax{
    'ProvisionedCapacityList': [
        {
            'CapacityId': 'string',
            'StartDate': 'string',
            'ExpirationDate': 'string'
        },
    ]
}


Response Structure

(dict) --
ProvisionedCapacityList (list) --The response body contains the following JSON fields.

(dict) --The definition for a provisioned capacity unit.

CapacityId (string) --The ID that identifies the provisioned capacity unit.

StartDate (string) --The date that the provisioned capacity unit was purchased, in Universal Coordinated Time (UTC).

ExpirationDate (string) --The date that the provisioned capacity unit expires, in Universal Coordinated Time (UTC).










Exceptions

Glacier.Client.exceptions.InvalidParameterValueException
Glacier.Client.exceptions.MissingParameterValueException
Glacier.Client.exceptions.ServiceUnavailableException

Examples
The example lists the provisioned capacity units for an account.
response = client.list_provisioned_capacity(
    accountId='-',
)

print(response)


Expected Output:
{
    'ProvisionedCapacityList': [
        {
            'CapacityId': 'zSaq7NzHFQDANTfQkDen4V7z',
            'ExpirationDate': '2016-12-12T00:00:00.000Z',
            'StartDate': '2016-11-11T20:11:51.095Z',
        },
        {
            'CapacityId': 'yXaq7NzHFQNADTfQkDen4V7z',
            'ExpirationDate': '2017-01-15T00:00:00.000Z',
            'StartDate': '2016-12-13T20:11:51.095Z',
        },
    ],
    'ResponseMetadata': {
        '...': '...',
    },
}



    :return: {
        'ProvisionedCapacityList': [
            {
                'CapacityId': 'string',
                'StartDate': 'string',
                'ExpirationDate': 'string'
            },
        ]
    }
    
    
    """
    pass

def list_tags_for_vault(accountId=None, vaultName=None):
    """
    This operation lists all the tags attached to a vault. The operation returns an empty map if there are no tags. For more information about tags, see Tagging Amazon S3 Glacier Resources .
    See also: AWS API Documentation
    
    Exceptions
    Examples
    The example lists all the tags attached to the vault examplevault.
    Expected Output:
    
    :example: response = client.list_tags_for_vault(
        vaultName='string'
    )
    
    
    :type accountId: string
    :param accountId: The AccountId value is the AWS account ID of the account that owns the vault. You can either specify an AWS account ID or optionally a single \'- \' (hyphen), in which case Amazon S3 Glacier uses the AWS account ID associated with the credentials used to sign the request. If you use an account ID, do not include any hyphens (\'-\') in the ID.\n\nNote: this parameter is set to '-' bydefault if no value is not specified.\n

    :type vaultName: string
    :param vaultName: [REQUIRED]\nThe name of the vault.\n

    :rtype: dict

ReturnsResponse Syntax
{
    'Tags': {
        'string': 'string'
    }
}


Response Structure

(dict) --
Contains the Amazon S3 Glacier response to your request.

Tags (dict) --
The tags attached to the vault. Each tag is composed of a key and a value.

(string) --
(string) --










Exceptions

Glacier.Client.exceptions.InvalidParameterValueException
Glacier.Client.exceptions.MissingParameterValueException
Glacier.Client.exceptions.ResourceNotFoundException
Glacier.Client.exceptions.ServiceUnavailableException

Examples
The example lists all the tags attached to the vault examplevault.
response = client.list_tags_for_vault(
    accountId='-',
    vaultName='examplevault',
)

print(response)


Expected Output:
{
    'Tags': {
        'date': 'july2015',
        'id': '1234',
    },
    'ResponseMetadata': {
        '...': '...',
    },
}



    :return: {
        'Tags': {
            'string': 'string'
        }
    }
    
    
    :returns: 
    (string) --
    (string) --
    
    
    
    """
    pass

def list_vaults(accountId=None, marker=None, limit=None):
    """
    This operation lists all vaults owned by the calling user\'s account. The list returned in the response is ASCII-sorted by vault name.
    By default, this operation returns up to 10 items. If there are more vaults to list, the response marker field contains the vault Amazon Resource Name (ARN) at which to continue the list with a new List Vaults request; otherwise, the marker field is null . To return a list of vaults that begins at a specific vault, set the marker request parameter to the vault ARN you obtained from a previous List Vaults request. You can also limit the number of vaults returned in the response by specifying the limit parameter in the request.
    An AWS account has full permission to perform all operations (actions). However, AWS Identity and Access Management (IAM) users don\'t have any permissions by default. You must grant them explicit permission to perform specific actions. For more information, see Access Control Using AWS Identity and Access Management (IAM) .
    For conceptual information and underlying REST API, see Retrieving Vault Metadata in Amazon S3 Glacier and List Vaults in the Amazon Glacier Developer Guide .
    See also: AWS API Documentation
    
    Exceptions
    Examples
    The example lists all vaults owned by the specified AWS account.
    Expected Output:
    
    :example: response = client.list_vaults(
        marker='string',
        limit='string'
    )
    
    
    :type accountId: string
    :param accountId: The AccountId value is the AWS account ID. This value must match the AWS account ID associated with the credentials used to sign the request. You can either specify an AWS account ID or optionally a single \'- \' (hyphen), in which case Amazon Glacier uses the AWS account ID associated with the credentials used to sign the request. If you specify your account ID, do not include any hyphens (\'-\') in the ID.\n\nNote: this parameter is set to '-' bydefault if no value is not specified.\n

    :type marker: string
    :param marker: A string used for pagination. The marker specifies the vault ARN after which the listing of vaults should begin.

    :type limit: string
    :param limit: The maximum number of vaults to be returned. The default limit is 10. The number of vaults returned might be fewer than the specified limit, but the number of returned vaults never exceeds the limit.

    :rtype: dict

ReturnsResponse Syntax
{
    'VaultList': [
        {
            'VaultARN': 'string',
            'VaultName': 'string',
            'CreationDate': 'string',
            'LastInventoryDate': 'string',
            'NumberOfArchives': 123,
            'SizeInBytes': 123
        },
    ],
    'Marker': 'string'
}


Response Structure

(dict) --
Contains the Amazon S3 Glacier response to your request.

VaultList (list) --
List of vaults.

(dict) --
Contains the Amazon S3 Glacier response to your request.

VaultARN (string) --
The Amazon Resource Name (ARN) of the vault.

VaultName (string) --
The name of the vault.

CreationDate (string) --
The Universal Coordinated Time (UTC) date when the vault was created. This value should be a string in the ISO 8601 date format, for example 2012-03-20T17:03:43.221Z .

LastInventoryDate (string) --
The Universal Coordinated Time (UTC) date when Amazon S3 Glacier completed the last vault inventory. This value should be a string in the ISO 8601 date format, for example 2012-03-20T17:03:43.221Z .

NumberOfArchives (integer) --
The number of archives in the vault as of the last inventory date. This field will return null if an inventory has not yet run on the vault, for example if you just created the vault.

SizeInBytes (integer) --
Total size, in bytes, of the archives in the vault as of the last inventory date. This field will return null if an inventory has not yet run on the vault, for example if you just created the vault.





Marker (string) --
The vault ARN at which to continue pagination of the results. You use the marker in another List Vaults request to obtain more vaults in the list.







Exceptions

Glacier.Client.exceptions.ResourceNotFoundException
Glacier.Client.exceptions.InvalidParameterValueException
Glacier.Client.exceptions.MissingParameterValueException
Glacier.Client.exceptions.ServiceUnavailableException

Examples
The example lists all vaults owned by the specified AWS account.
response = client.list_vaults(
    accountId='-',
    limit='',
    marker='',
)

print(response)


Expected Output:
{
    'VaultList': [
        {
            'CreationDate': '2015-04-06T21:23:45.708Z',
            'LastInventoryDate': '2015-04-07T00:26:19.028Z',
            'NumberOfArchives': 1,
            'SizeInBytes': 3178496,
            'VaultARN': 'arn:aws:glacier:us-west-2:0123456789012:vaults/my-vault',
            'VaultName': 'my-vault',
        },
    ],
    'ResponseMetadata': {
        '...': '...',
    },
}



    :return: {
        'VaultList': [
            {
                'VaultARN': 'string',
                'VaultName': 'string',
                'CreationDate': 'string',
                'LastInventoryDate': 'string',
                'NumberOfArchives': 123,
                'SizeInBytes': 123
            },
        ],
        'Marker': 'string'
    }
    
    
    :returns: 
    Glacier.Client.exceptions.ResourceNotFoundException
    Glacier.Client.exceptions.InvalidParameterValueException
    Glacier.Client.exceptions.MissingParameterValueException
    Glacier.Client.exceptions.ServiceUnavailableException
    
    """
    pass

def purchase_provisioned_capacity(accountId=None):
    """
    This operation purchases a provisioned capacity unit for an AWS account.
    See also: AWS API Documentation
    
    Exceptions
    Examples
    The example purchases provisioned capacity unit for an AWS account.
    Expected Output:
    
    :example: response = client.purchase_provisioned_capacity(
    
    )
    
    
    :type accountId: string
    :param accountId: The AWS account ID of the account that owns the vault. You can either specify an AWS account ID or optionally a single \'-\' (hyphen), in which case Amazon S3 Glacier uses the AWS account ID associated with the credentials used to sign the request. If you use an account ID, don\'t include any hyphens (\'-\') in the ID.\n\nNote: this parameter is set to '-' bydefault if no value is not specified.\n

    :rtype: dict
ReturnsResponse Syntax{
    'capacityId': 'string'
}


Response Structure

(dict) --
capacityId (string) --The ID that identifies the provisioned capacity unit.






Exceptions

Glacier.Client.exceptions.InvalidParameterValueException
Glacier.Client.exceptions.MissingParameterValueException
Glacier.Client.exceptions.LimitExceededException
Glacier.Client.exceptions.ServiceUnavailableException

Examples
The example purchases provisioned capacity unit for an AWS account.
response = client.purchase_provisioned_capacity(
    accountId='-',
)

print(response)


Expected Output:
{
    'capacityId': 'zSaq7NzHFQDANTfQkDen4V7z',
    'ResponseMetadata': {
        '...': '...',
    },
}



    :return: {
        'capacityId': 'string'
    }
    
    
    """
    pass

def remove_tags_from_vault(accountId=None, vaultName=None, TagKeys=None):
    """
    This operation removes one or more tags from the set of tags attached to a vault. For more information about tags, see Tagging Amazon S3 Glacier Resources . This operation is idempotent. The operation will be successful, even if there are no tags attached to the vault.
    See also: AWS API Documentation
    
    Exceptions
    Examples
    The example removes two tags from the vault named examplevault.
    Expected Output:
    
    :example: response = client.remove_tags_from_vault(
        vaultName='string',
        TagKeys=[
            'string',
        ]
    )
    
    
    :type accountId: string
    :param accountId: The AccountId value is the AWS account ID of the account that owns the vault. You can either specify an AWS account ID or optionally a single \'- \' (hyphen), in which case Amazon S3 Glacier uses the AWS account ID associated with the credentials used to sign the request. If you use an account ID, do not include any hyphens (\'-\') in the ID.\n\nNote: this parameter is set to '-' bydefault if no value is not specified.\n

    :type vaultName: string
    :param vaultName: [REQUIRED]\nThe name of the vault.\n

    :type TagKeys: list
    :param TagKeys: A list of tag keys. Each corresponding tag is removed from the vault.\n\n(string) --\n\n

    :return: response = client.remove_tags_from_vault(
        TagKeys=[
            'examplekey1',
            'examplekey2',
        ],
        accountId='-',
        vaultName='examplevault',
    )
    
    print(response)
    
    
    :returns: 
    Glacier.Client.exceptions.InvalidParameterValueException
    Glacier.Client.exceptions.MissingParameterValueException
    Glacier.Client.exceptions.ResourceNotFoundException
    Glacier.Client.exceptions.ServiceUnavailableException
    
    """
    pass

def set_data_retrieval_policy(accountId=None, Policy=None):
    """
    This operation sets and then enacts a data retrieval policy in the region specified in the PUT request. You can set one policy per region for an AWS account. The policy is enacted within a few minutes of a successful PUT operation.
    The set policy operation does not affect retrieval jobs that were in progress before the policy was enacted. For more information about data retrieval policies, see Amazon Glacier Data Retrieval Policies .
    See also: AWS API Documentation
    
    Exceptions
    Examples
    The example sets and then enacts a data retrieval policy.
    Expected Output:
    
    :example: response = client.set_data_retrieval_policy(
        Policy={
            'Rules': [
                {
                    'Strategy': 'string',
                    'BytesPerHour': 123
                },
            ]
        }
    )
    
    
    :type accountId: string
    :param accountId: The AccountId value is the AWS account ID. This value must match the AWS account ID associated with the credentials used to sign the request. You can either specify an AWS account ID or optionally a single \'- \' (hyphen), in which case Amazon Glacier uses the AWS account ID associated with the credentials used to sign the request. If you specify your account ID, do not include any hyphens (\'-\') in the ID.\n\nNote: this parameter is set to '-' bydefault if no value is not specified.\n

    :type Policy: dict
    :param Policy: The data retrieval policy in JSON format.\n\nRules (list) --The policy rule. Although this is a list type, currently there must be only one rule, which contains a Strategy field and optionally a BytesPerHour field.\n\n(dict) --Data retrieval policy rule.\n\nStrategy (string) --The type of data retrieval policy to set.\nValid values: BytesPerHour|FreeTier|None\n\nBytesPerHour (integer) --The maximum number of bytes that can be retrieved in an hour.\nThis field is required only if the value of the Strategy field is BytesPerHour . Your PUT operation will be rejected if the Strategy field is not set to BytesPerHour and you set this field.\n\n\n\n\n\n\n

    :return: response = client.set_data_retrieval_policy(
        Policy={
            'Rules': [
                {
                    'BytesPerHour': 10737418240,
                    'Strategy': 'BytesPerHour',
                },
            ],
        },
        accountId='-',
    )
    
    print(response)
    
    
    :returns: 
    Glacier.Client.exceptions.InvalidParameterValueException
    Glacier.Client.exceptions.MissingParameterValueException
    Glacier.Client.exceptions.ServiceUnavailableException
    
    """
    pass

def set_vault_access_policy(accountId=None, vaultName=None, policy=None):
    """
    This operation configures an access policy for a vault and will overwrite an existing policy. To configure a vault access policy, send a PUT request to the access-policy subresource of the vault. An access policy is specific to a vault and is also called a vault subresource. You can set one access policy per vault and the policy can be up to 20 KB in size. For more information about vault access policies, see Amazon Glacier Access Control with Vault Access Policies .
    See also: AWS API Documentation
    
    Exceptions
    Examples
    The example configures an access policy for the vault named examplevault.
    Expected Output:
    
    :example: response = client.set_vault_access_policy(
        vaultName='string',
        policy={
            'Policy': 'string'
        }
    )
    
    
    :type accountId: string
    :param accountId: The AccountId value is the AWS account ID of the account that owns the vault. You can either specify an AWS account ID or optionally a single \'- \' (hyphen), in which case Amazon S3 Glacier uses the AWS account ID associated with the credentials used to sign the request. If you use an account ID, do not include any hyphens (\'-\') in the ID.\n\nNote: this parameter is set to '-' bydefault if no value is not specified.\n

    :type vaultName: string
    :param vaultName: [REQUIRED]\nThe name of the vault.\n

    :type policy: dict
    :param policy: The vault access policy as a JSON string.\n\nPolicy (string) --The vault access policy.\n\n\n

    :return: response = client.set_vault_access_policy(
        accountId='-',
        policy={
            'Policy': '{"Version":"2012-10-17","Statement":[{"Sid":"Define-owner-access-rights","Effect":"Allow","Principal":{"AWS":"arn:aws:iam::999999999999:root"},"Action":"glacier:DeleteArchive","Resource":"arn:aws:glacier:us-west-2:999999999999:vaults/examplevault"}]}',
        },
        vaultName='examplevault',
    )
    
    print(response)
    
    
    :returns: 
    Glacier.Client.exceptions.ResourceNotFoundException
    Glacier.Client.exceptions.InvalidParameterValueException
    Glacier.Client.exceptions.MissingParameterValueException
    Glacier.Client.exceptions.ServiceUnavailableException
    
    """
    pass

def set_vault_notifications(accountId=None, vaultName=None, vaultNotificationConfig=None):
    """
    This operation configures notifications that will be sent when specific events happen to a vault. By default, you don\'t get any notifications.
    To configure vault notifications, send a PUT request to the notification-configuration subresource of the vault. The request should include a JSON document that provides an Amazon SNS topic and specific events for which you want Amazon S3 Glacier to send notifications to the topic.
    Amazon SNS topics must grant permission to the vault to be allowed to publish notifications to the topic. You can configure a vault to publish a notification for the following vault events:
    An AWS account has full permission to perform all operations (actions). However, AWS Identity and Access Management (IAM) users don\'t have any permissions by default. You must grant them explicit permission to perform specific actions. For more information, see Access Control Using AWS Identity and Access Management (IAM) .
    For conceptual information and underlying REST API, see Configuring Vault Notifications in Amazon S3 Glacier and Set Vault Notification Configuration in the Amazon Glacier Developer Guide .
    See also: AWS API Documentation
    
    Exceptions
    Examples
    The example sets the examplevault notification configuration.
    Expected Output:
    
    :example: response = client.set_vault_notifications(
        vaultName='string',
        vaultNotificationConfig={
            'SNSTopic': 'string',
            'Events': [
                'string',
            ]
        }
    )
    
    
    :type accountId: string
    :param accountId: The AccountId value is the AWS account ID of the account that owns the vault. You can either specify an AWS account ID or optionally a single \'- \' (hyphen), in which case Amazon S3 Glacier uses the AWS account ID associated with the credentials used to sign the request. If you use an account ID, do not include any hyphens (\'-\') in the ID.\n\nNote: this parameter is set to '-' bydefault if no value is not specified.\n

    :type vaultName: string
    :param vaultName: [REQUIRED]\nThe name of the vault.\n

    :type vaultNotificationConfig: dict
    :param vaultNotificationConfig: Provides options for specifying notification configuration.\n\nSNSTopic (string) --The Amazon Simple Notification Service (Amazon SNS) topic Amazon Resource Name (ARN).\n\nEvents (list) --A list of one or more events for which Amazon S3 Glacier will send a notification to the specified Amazon SNS topic.\n\n(string) --\n\n\n\n

    :return: response = client.set_vault_notifications(
        accountId='-',
        vaultName='examplevault',
        vaultNotificationConfig={
            'Events': [
                'ArchiveRetrievalCompleted',
                'InventoryRetrievalCompleted',
            ],
            'SNSTopic': 'arn:aws:sns:us-west-2:012345678901:mytopic',
        },
    )
    
    print(response)
    
    
    :returns: 
    accountId (string) -- The AccountId value is the AWS account ID of the account that owns the vault. You can either specify an AWS account ID or optionally a single \'- \' (hyphen), in which case Amazon S3 Glacier uses the AWS account ID associated with the credentials used to sign the request. If you use an account ID, do not include any hyphens (\'-\') in the ID.
    
    Note: this parameter is set to "-" bydefault if no value is not specified.
    
    vaultName (string) -- [REQUIRED]
    The name of the vault.
    
    vaultNotificationConfig (dict) -- Provides options for specifying notification configuration.
    
    SNSTopic (string) --The Amazon Simple Notification Service (Amazon SNS) topic Amazon Resource Name (ARN).
    
    Events (list) --A list of one or more events for which Amazon S3 Glacier will send a notification to the specified Amazon SNS topic.
    
    (string) --
    
    
    
    
    
    """
    pass

def upload_archive(vaultName=None, accountId=None, archiveDescription=None, checksum=None, body=None):
    """
    This operation adds an archive to a vault. This is a synchronous operation, and for a successful upload, your data is durably persisted. Amazon S3 Glacier returns the archive ID in the x-amz-archive-id header of the response.
    You must use the archive ID to access your data in Amazon S3 Glacier. After you upload an archive, you should save the archive ID returned so that you can retrieve or delete the archive later. Besides saving the archive ID, you can also index it and give it a friendly name to allow for better searching. You can also use the optional archive description field to specify how the archive is referred to in an external index of archives, such as you might create in Amazon DynamoDB. You can also get the vault inventory to obtain a list of archive IDs in a vault. For more information, see  InitiateJob .
    You must provide a SHA256 tree hash of the data you are uploading. For information about computing a SHA256 tree hash, see Computing Checksums .
    You can optionally specify an archive description of up to 1,024 printable ASCII characters. You can get the archive description when you either retrieve the archive or get the vault inventory. For more information, see  InitiateJob . Amazon Glacier does not interpret the description in any way. An archive description does not need to be unique. You cannot use the description to retrieve or sort the archive list.
    Archives are immutable. After you upload an archive, you cannot edit the archive or its description.
    An AWS account has full permission to perform all operations (actions). However, AWS Identity and Access Management (IAM) users don\'t have any permissions by default. You must grant them explicit permission to perform specific actions. For more information, see Access Control Using AWS Identity and Access Management (IAM) .
    For conceptual information and underlying REST API, see Uploading an Archive in Amazon Glacier and Upload Archive in the Amazon Glacier Developer Guide .
    See also: AWS API Documentation
    
    Exceptions
    Examples
    The example adds an archive to a vault.
    Expected Output:
    
    :example: response = client.upload_archive(
        vaultName='string',
        archiveDescription='string',
        body=b'bytes'|file
    )
    
    
    :type vaultName: string
    :param vaultName: [REQUIRED]\nThe name of the vault.\n

    :type accountId: string
    :param accountId: The AccountId value is the AWS account ID of the account that owns the vault. You can either specify an AWS account ID or optionally a single \'- \' (hyphen), in which case Amazon S3 Glacier uses the AWS account ID associated with the credentials used to sign the request. If you use an account ID, do not include any hyphens (\'-\') in the ID.\n\nNote: this parameter is set to '-' bydefault if no value is not specified.\n

    :type archiveDescription: string
    :param archiveDescription: The optional description of the archive you are uploading.

    :type checksum: string
    :param checksum: The SHA256 tree hash of the data being uploaded.\n\nPlease note that this parameter is automatically populated if it is not provided. Including this parameter is not required\n

    :type body: bytes or seekable file-like object
    :param body: The data to upload.

    :rtype: dict

ReturnsResponse Syntax
{
    'location': 'string',
    'checksum': 'string',
    'archiveId': 'string'
}


Response Structure

(dict) --
Contains the Amazon S3 Glacier response to your request.
For information about the underlying REST API, see Upload Archive . For conceptual information, see Working with Archives in Amazon S3 Glacier .

location (string) --
The relative URI path of the newly added archive resource.

checksum (string) --
The checksum of the archive computed by Amazon S3 Glacier.

archiveId (string) --
The ID of the archive. This value is also included as part of the location.







Exceptions

Glacier.Client.exceptions.ResourceNotFoundException
Glacier.Client.exceptions.InvalidParameterValueException
Glacier.Client.exceptions.MissingParameterValueException
Glacier.Client.exceptions.RequestTimeoutException
Glacier.Client.exceptions.ServiceUnavailableException

Examples
The example adds an archive to a vault.
response = client.upload_archive(
    accountId='-',
    archiveDescription='',
    body='example-data-to-upload',
    checksum='',
    vaultName='my-vault',
)

print(response)


Expected Output:
{
    'archiveId': 'kKB7ymWJVpPSwhGP6ycSOAekp9ZYe_--zM_mw6k76ZFGEIWQX-ybtRDvc2VkPSDtfKmQrj0IRQLSGsNuDp-AJVlu2ccmDSyDUmZwKbwbpAdGATGDiB3hHO0bjbGehXTcApVud_wyDw',
    'checksum': '969fb39823836d81f0cc028195fcdbcbbe76cdde932d4646fa7de5f21e18aa67',
    'location': '/0123456789012/vaults/my-vault/archives/kKB7ymWJVpPSwhGP6ycSOAekp9ZYe_--zM_mw6k76ZFGEIWQX-ybtRDvc2VkPSDtfKmQrj0IRQLSGsNuDp-AJVlu2ccmDSyDUmZwKbwbpAdGATGDiB3hHO0bjbGehXTcApVud_wyDw',
    'ResponseMetadata': {
        '...': '...',
    },
}



    :return: {
        'location': 'string',
        'checksum': 'string',
        'archiveId': 'string'
    }
    
    
    :returns: 
    Glacier.Client.exceptions.ResourceNotFoundException
    Glacier.Client.exceptions.InvalidParameterValueException
    Glacier.Client.exceptions.MissingParameterValueException
    Glacier.Client.exceptions.RequestTimeoutException
    Glacier.Client.exceptions.ServiceUnavailableException
    
    """
    pass

def upload_multipart_part(accountId=None, vaultName=None, uploadId=None, checksum=None, range=None, body=None):
    """
    This operation uploads a part of an archive. You can upload archive parts in any order. You can also upload them in parallel. You can upload up to 10,000 parts for a multipart upload.
    Amazon Glacier rejects your upload part request if any of the following conditions is true:
    This operation is idempotent. If you upload the same part multiple times, the data included in the most recent request overwrites the previously uploaded data.
    An AWS account has full permission to perform all operations (actions). However, AWS Identity and Access Management (IAM) users don\'t have any permissions by default. You must grant them explicit permission to perform specific actions. For more information, see Access Control Using AWS Identity and Access Management (IAM) .
    For conceptual information and underlying REST API, see Uploading Large Archives in Parts (Multipart Upload) and Upload Part in the Amazon Glacier Developer Guide .
    See also: AWS API Documentation
    
    Exceptions
    Examples
    The example uploads the first 1 MiB (1024 x 1024 bytes) part of an archive.
    Expected Output:
    
    :example: response = client.upload_multipart_part(
        vaultName='string',
        uploadId='string',
        range='string',
        body=b'bytes'|file
    )
    
    
    :type accountId: string
    :param accountId: The AccountId value is the AWS account ID of the account that owns the vault. You can either specify an AWS account ID or optionally a single \'- \' (hyphen), in which case Amazon S3 Glacier uses the AWS account ID associated with the credentials used to sign the request. If you use an account ID, do not include any hyphens (\'-\') in the ID.\n\nNote: this parameter is set to '-' bydefault if no value is not specified.\n

    :type vaultName: string
    :param vaultName: [REQUIRED]\nThe name of the vault.\n

    :type uploadId: string
    :param uploadId: [REQUIRED]\nThe upload ID of the multipart upload.\n

    :type checksum: string
    :param checksum: The SHA256 tree hash of the data being uploaded.\n\nPlease note that this parameter is automatically populated if it is not provided. Including this parameter is not required\n

    :type range: string
    :param range: Identifies the range of bytes in the assembled archive that will be uploaded in this part. Amazon S3 Glacier uses this information to assemble the archive in the proper sequence. The format of this header follows RFC 2616. An example header is Content-Range:bytes 0-4194303/*.

    :type body: bytes or seekable file-like object
    :param body: The data to upload.

    :rtype: dict

ReturnsResponse Syntax
{
    'checksum': 'string'
}


Response Structure

(dict) --
Contains the Amazon S3 Glacier response to your request.

checksum (string) --
The SHA256 tree hash that Amazon S3 Glacier computed for the uploaded part.







Exceptions

Glacier.Client.exceptions.ResourceNotFoundException
Glacier.Client.exceptions.InvalidParameterValueException
Glacier.Client.exceptions.MissingParameterValueException
Glacier.Client.exceptions.RequestTimeoutException
Glacier.Client.exceptions.ServiceUnavailableException

Examples
The example uploads the first 1 MiB (1024 x 1024 bytes) part of an archive.
response = client.upload_multipart_part(
    accountId='-',
    body='part1',
    checksum='c06f7cd4baacb087002a99a5f48bf953',
    range='bytes 0-1048575/*',
    uploadId='19gaRezEXAMPLES6Ry5YYdqthHOC_kGRCT03L9yetr220UmPtBYKk-OssZtLqyFu7sY1_lR7vgFuJV6NtcV5zpsJ',
    vaultName='examplevault',
)

print(response)


Expected Output:
{
    'checksum': 'c06f7cd4baacb087002a99a5f48bf953',
    'ResponseMetadata': {
        '...': '...',
    },
}



    :return: {
        'checksum': 'string'
    }
    
    
    :returns: 
    Range does not align The byte range value in the request does not align with the part size specified in the corresponding initiate request. For example, if you specify a part size of 4194304 bytes (4 MB), then 0 to 4194303 bytes (4 MB - 1) and 4194304 (4 MB) to 8388607 (8 MB - 1) are valid part ranges. However, if you set a range value of 2 MB to 6 MB, the range does not align with the part size and the upload will fail.
    
    """
    pass

