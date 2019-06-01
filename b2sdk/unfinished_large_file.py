######################################################################
#
# File: b2sdk/unfinished_large_file.py
#
# Copyright 2019 Backblaze Inc. All Rights Reserved.
#
# License https://www.backblaze.com/using_b2_code.html
#
######################################################################


class UnfinishedLargeFile(object):
    """
    A structure which represents a version of a file (in B2 cloud)

    :ivar str ~.file_id: ``fileId``
    :ivar str ~.file_name: full file name (with path)
    :ivar str ~.account_id: Account ID
    :ivar str ~.bucket_id: Bucket ID
    :ivar str ~.content_type: :rfc:`822` content type, for example ``"application/octet-stream"``
    :ivar dict ~.file_info: file info dict
    """
    def __init__(self, file_dict):
        """
        Initializes from one file returned by ``b2_start_large_file`` or ``b2_list_unfinished_large_files``
        """
        self.file_id = file_dict['fileId']
        self.file_name = file_dict['fileName']
        self.account_id = file_dict['accountId']
        self.bucket_id = file_dict['bucketId']
        self.content_type = file_dict['contentType']
        self.file_info = file_dict['fileInfo']

    def __repr__(self):
        return '<%s %s %s>' % (self.__class__.__name__, self.bucket_id, self.file_name)

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)
