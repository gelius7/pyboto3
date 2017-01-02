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

def cancel_job(Id=None):
    """
    The CancelJob operation cancels an unfinished job.
    See also: AWS API Documentation
    
    
    :example: response = client.cancel_job(
        Id='string'
    )
    
    
    :type Id: string
    :param Id: [REQUIRED]
            The identifier of the job that you want to cancel.
            To get a list of the jobs (including their jobId ) that have a status of Submitted , use the ListJobsByStatus API action.
            

    :rtype: dict
    :return: {}
    
    
    """
    pass

def create_job(PipelineId=None, Input=None, Inputs=None, Output=None, Outputs=None, OutputKeyPrefix=None, Playlists=None, UserMetadata=None):
    """
    When you create a job, Elastic Transcoder returns JSON data that includes the values that you specified plus information about the job that is created.
    If you have specified more than one output for your jobs (for example, one output for the Kindle Fire and another output for the Apple iPhone 4s), you currently must use the Elastic Transcoder API to list the jobs (as opposed to the AWS Console).
    See also: AWS API Documentation
    
    
    :example: response = client.create_job(
        PipelineId='string',
        Input={
            'Key': 'string',
            'FrameRate': 'string',
            'Resolution': 'string',
            'AspectRatio': 'string',
            'Interlaced': 'string',
            'Container': 'string',
            'Encryption': {
                'Mode': 'string',
                'Key': 'string',
                'KeyMd5': 'string',
                'InitializationVector': 'string'
            },
            'TimeSpan': {
                'StartTime': 'string',
                'Duration': 'string'
            },
            'InputCaptions': {
                'MergePolicy': 'string',
                'CaptionSources': [
                    {
                        'Key': 'string',
                        'Language': 'string',
                        'TimeOffset': 'string',
                        'Label': 'string',
                        'Encryption': {
                            'Mode': 'string',
                            'Key': 'string',
                            'KeyMd5': 'string',
                            'InitializationVector': 'string'
                        }
                    },
                ]
            },
            'DetectedProperties': {
                'Width': 123,
                'Height': 123,
                'FrameRate': 'string',
                'FileSize': 123,
                'DurationMillis': 123
            }
        },
        Inputs=[
            {
                'Key': 'string',
                'FrameRate': 'string',
                'Resolution': 'string',
                'AspectRatio': 'string',
                'Interlaced': 'string',
                'Container': 'string',
                'Encryption': {
                    'Mode': 'string',
                    'Key': 'string',
                    'KeyMd5': 'string',
                    'InitializationVector': 'string'
                },
                'TimeSpan': {
                    'StartTime': 'string',
                    'Duration': 'string'
                },
                'InputCaptions': {
                    'MergePolicy': 'string',
                    'CaptionSources': [
                        {
                            'Key': 'string',
                            'Language': 'string',
                            'TimeOffset': 'string',
                            'Label': 'string',
                            'Encryption': {
                                'Mode': 'string',
                                'Key': 'string',
                                'KeyMd5': 'string',
                                'InitializationVector': 'string'
                            }
                        },
                    ]
                },
                'DetectedProperties': {
                    'Width': 123,
                    'Height': 123,
                    'FrameRate': 'string',
                    'FileSize': 123,
                    'DurationMillis': 123
                }
            },
        ],
        Output={
            'Key': 'string',
            'ThumbnailPattern': 'string',
            'ThumbnailEncryption': {
                'Mode': 'string',
                'Key': 'string',
                'KeyMd5': 'string',
                'InitializationVector': 'string'
            },
            'Rotate': 'string',
            'PresetId': 'string',
            'SegmentDuration': 'string',
            'Watermarks': [
                {
                    'PresetWatermarkId': 'string',
                    'InputKey': 'string',
                    'Encryption': {
                        'Mode': 'string',
                        'Key': 'string',
                        'KeyMd5': 'string',
                        'InitializationVector': 'string'
                    }
                },
            ],
            'AlbumArt': {
                'MergePolicy': 'string',
                'Artwork': [
                    {
                        'InputKey': 'string',
                        'MaxWidth': 'string',
                        'MaxHeight': 'string',
                        'SizingPolicy': 'string',
                        'PaddingPolicy': 'string',
                        'AlbumArtFormat': 'string',
                        'Encryption': {
                            'Mode': 'string',
                            'Key': 'string',
                            'KeyMd5': 'string',
                            'InitializationVector': 'string'
                        }
                    },
                ]
            },
            'Composition': [
                {
                    'TimeSpan': {
                        'StartTime': 'string',
                        'Duration': 'string'
                    }
                },
            ],
            'Captions': {
                'MergePolicy': 'string',
                'CaptionSources': [
                    {
                        'Key': 'string',
                        'Language': 'string',
                        'TimeOffset': 'string',
                        'Label': 'string',
                        'Encryption': {
                            'Mode': 'string',
                            'Key': 'string',
                            'KeyMd5': 'string',
                            'InitializationVector': 'string'
                        }
                    },
                ],
                'CaptionFormats': [
                    {
                        'Format': 'string',
                        'Pattern': 'string',
                        'Encryption': {
                            'Mode': 'string',
                            'Key': 'string',
                            'KeyMd5': 'string',
                            'InitializationVector': 'string'
                        }
                    },
                ]
            },
            'Encryption': {
                'Mode': 'string',
                'Key': 'string',
                'KeyMd5': 'string',
                'InitializationVector': 'string'
            }
        },
        Outputs=[
            {
                'Key': 'string',
                'ThumbnailPattern': 'string',
                'ThumbnailEncryption': {
                    'Mode': 'string',
                    'Key': 'string',
                    'KeyMd5': 'string',
                    'InitializationVector': 'string'
                },
                'Rotate': 'string',
                'PresetId': 'string',
                'SegmentDuration': 'string',
                'Watermarks': [
                    {
                        'PresetWatermarkId': 'string',
                        'InputKey': 'string',
                        'Encryption': {
                            'Mode': 'string',
                            'Key': 'string',
                            'KeyMd5': 'string',
                            'InitializationVector': 'string'
                        }
                    },
                ],
                'AlbumArt': {
                    'MergePolicy': 'string',
                    'Artwork': [
                        {
                            'InputKey': 'string',
                            'MaxWidth': 'string',
                            'MaxHeight': 'string',
                            'SizingPolicy': 'string',
                            'PaddingPolicy': 'string',
                            'AlbumArtFormat': 'string',
                            'Encryption': {
                                'Mode': 'string',
                                'Key': 'string',
                                'KeyMd5': 'string',
                                'InitializationVector': 'string'
                            }
                        },
                    ]
                },
                'Composition': [
                    {
                        'TimeSpan': {
                            'StartTime': 'string',
                            'Duration': 'string'
                        }
                    },
                ],
                'Captions': {
                    'MergePolicy': 'string',
                    'CaptionSources': [
                        {
                            'Key': 'string',
                            'Language': 'string',
                            'TimeOffset': 'string',
                            'Label': 'string',
                            'Encryption': {
                                'Mode': 'string',
                                'Key': 'string',
                                'KeyMd5': 'string',
                                'InitializationVector': 'string'
                            }
                        },
                    ],
                    'CaptionFormats': [
                        {
                            'Format': 'string',
                            'Pattern': 'string',
                            'Encryption': {
                                'Mode': 'string',
                                'Key': 'string',
                                'KeyMd5': 'string',
                                'InitializationVector': 'string'
                            }
                        },
                    ]
                },
                'Encryption': {
                    'Mode': 'string',
                    'Key': 'string',
                    'KeyMd5': 'string',
                    'InitializationVector': 'string'
                }
            },
        ],
        OutputKeyPrefix='string',
        Playlists=[
            {
                'Name': 'string',
                'Format': 'string',
                'OutputKeys': [
                    'string',
                ],
                'HlsContentProtection': {
                    'Method': 'string',
                    'Key': 'string',
                    'KeyMd5': 'string',
                    'InitializationVector': 'string',
                    'LicenseAcquisitionUrl': 'string',
                    'KeyStoragePolicy': 'string'
                },
                'PlayReadyDrm': {
                    'Format': 'string',
                    'Key': 'string',
                    'KeyMd5': 'string',
                    'KeyId': 'string',
                    'InitializationVector': 'string',
                    'LicenseAcquisitionUrl': 'string'
                }
            },
        ],
        UserMetadata={
            'string': 'string'
        }
    )
    
    
    :type PipelineId: string
    :param PipelineId: [REQUIRED]
            The Id of the pipeline that you want Elastic Transcoder to use for transcoding. The pipeline determines several settings, including the Amazon S3 bucket from which Elastic Transcoder gets the files to transcode and the bucket into which Elastic Transcoder puts the transcoded files.
            

    :type Input: dict
    :param Input: A section of the request body that provides information about the file that is being transcoded.
            Key (string) --The name of the file to transcode. Elsewhere in the body of the JSON block is the the ID of the pipeline to use for processing the job. The InputBucket object in that pipeline tells Elastic Transcoder which Amazon S3 bucket to get the file from.
            If the file name includes a prefix, such as cooking/lasagna.mpg , include the prefix in the key. If the file isn't in the specified bucket, Elastic Transcoder returns an error.
            FrameRate (string) --The frame rate of the input file. If you want Elastic Transcoder to automatically detect the frame rate of the input file, specify auto . If you want to specify the frame rate for the input file, enter one of the following values:
            10 , 15 , 23.97 , 24 , 25 , 29.97 , 30 , 60
            If you specify a value other than auto , Elastic Transcoder disables automatic detection of the frame rate.
            Resolution (string) --This value must be auto , which causes Elastic Transcoder to automatically detect the resolution of the input file.
            AspectRatio (string) --The aspect ratio of the input file. If you want Elastic Transcoder to automatically detect the aspect ratio of the input file, specify auto . If you want to specify the aspect ratio for the output file, enter one of the following values:
            1:1 , 4:3 , 3:2 , 16:9
            If you specify a value other than auto , Elastic Transcoder disables automatic detection of the aspect ratio.
            Interlaced (string) --Whether the input file is interlaced. If you want Elastic Transcoder to automatically detect whether the input file is interlaced, specify auto . If you want to specify whether the input file is interlaced, enter one of the following values:
            true , false
            If you specify a value other than auto , Elastic Transcoder disables automatic detection of interlacing.
            Container (string) --The container type for the input file. If you want Elastic Transcoder to automatically detect the container type of the input file, specify auto . If you want to specify the container type for the input file, enter one of the following values:
            3gp , aac , asf , avi , divx , flv , m4a , mkv , mov , mp3 , mp4 , mpeg , mpeg-ps , mpeg-ts , mxf , ogg , vob , wav , webm
            Encryption (dict) --The encryption settings, if any, that are used for decrypting your input files. If your input file is encrypted, you must specify the mode that Elastic Transcoder uses to decrypt your file.
            Mode (string) --The specific server-side encryption mode that you want Elastic Transcoder to use when decrypting your input files or encrypting your output files. Elastic Transcoder supports the following options:
            S3: Amazon S3 creates and manages the keys used for encrypting your files.
            S3-AWS-KMS: Amazon S3 calls the Amazon Key Management Service, which creates and manages the keys that are used for encrypting your files. If you specify S3-AWS-KMS and you don't want to use the default key, you must add the AWS-KMS key that you want to use to your pipeline.
            AES-CBC-PKCS7: A padded cipher-block mode of operation originally used for HLS files.
            AES-CTR: AES Counter Mode.
            AES-GCM: AES Galois Counter Mode, a mode of operation that is an authenticated encryption format, meaning that a file, key, or initialization vector that has been tampered with fails the decryption process.
            For all three AES options, you must provide the following settings, which must be base64-encoded:
            Key
            Key MD5
            Initialization Vector
            Warning
            For the AES modes, your private encryption keys and your unencrypted data are never stored by AWS; therefore, it is important that you safely manage your encryption keys. If you lose them, you won't be able to unencrypt your data.
            Key (string) --The data encryption key that you want Elastic Transcoder to use to encrypt your output file, or that was used to encrypt your input file. The key must be base64-encoded and it must be one of the following bit lengths before being base64-encoded:
            128 , 192 , or 256 .
            The key must also be encrypted by using the Amazon Key Management Service.
            KeyMd5 (string) --The MD5 digest of the key that you used to encrypt your input file, or that you want Elastic Transcoder to use to encrypt your output file. Elastic Transcoder uses the key digest as a checksum to make sure your key was not corrupted in transit. The key MD5 must be base64-encoded, and it must be exactly 16 bytes long before being base64-encoded.
            InitializationVector (string) --The series of random bits created by a random bit generator, unique for every encryption operation, that you used to encrypt your input files or that you want Elastic Transcoder to use to encrypt your output files. The initialization vector must be base64-encoded, and it must be exactly 16 bytes long before being base64-encoded.
            TimeSpan (dict) --Settings for clipping an input. Each input can have different clip settings.
            StartTime (string) --The place in the input file where you want a clip to start. The format can be either HH:mm:ss.SSS (maximum value: 23:59:59.999; SSS is thousandths of a second) or sssss.SSS (maximum value: 86399.999). If you don't specify a value, Elastic Transcoder starts at the beginning of the input file.
            Duration (string) --The duration of the clip. The format can be either HH:mm:ss.SSS (maximum value: 23:59:59.999; SSS is thousandths of a second) or sssss.SSS (maximum value: 86399.999). If you don't specify a value, Elastic Transcoder creates an output file from StartTime to the end of the file.
            If you specify a value longer than the duration of the input file, Elastic Transcoder transcodes the file and returns a warning message.
            InputCaptions (dict) --You can configure Elastic Transcoder to transcode captions, or subtitles, from one format to another. All captions must be in UTF-8. Elastic Transcoder supports two types of captions:
            Embedded: Embedded captions are included in the same file as the audio and video. Elastic Transcoder supports only one embedded caption per language, to a maximum of 300 embedded captions per file. Valid input values include: CEA-608 (EIA-608 , first non-empty channel only), CEA-708 (EIA-708 , first non-empty channel only), and mov-text  Valid outputs include: mov-text  Elastic Transcoder supports a maximum of one embedded format per output.
            Sidecar: Sidecar captions are kept in a separate metadata file from the audio and video data. Sidecar captions require a player that is capable of understanding the relationship between the video file and the sidecar file. Elastic Transcoder supports only one sidecar caption per language, to a maximum of 20 sidecar captions per file. Valid input values include: dfxp (first div element only), ebu-tt , scc , smpt , srt , ttml (first div element only), and webvtt  Valid outputs include: dfxp (first div element only), scc , srt , and webvtt .
            If you want ttml or smpte-tt compatible captions, specify dfxp as your output format.
            Elastic Transcoder does not support OCR (Optical Character Recognition), does not accept pictures as a valid input for captions, and is not available for audio-only transcoding. Elastic Transcoder does not preserve text formatting (for example, italics) during the transcoding process.
            To remove captions or leave the captions empty, set Captions to null. To pass through existing captions unchanged, set the MergePolicy to MergeRetain , and pass in a null CaptionSources array.
            For more information on embedded files, see the Subtitles Wikipedia page.
            For more information on sidecar files, see the Extensible Metadata Platform and Sidecar file Wikipedia pages.
            MergePolicy (string) --A policy that determines how Elastic Transcoder handles the existence of multiple captions.
            MergeOverride: Elastic Transcoder transcodes both embedded and sidecar captions into outputs. If captions for a language are embedded in the input file and also appear in a sidecar file, Elastic Transcoder uses the sidecar captions and ignores the embedded captions for that language.
            MergeRetain: Elastic Transcoder transcodes both embedded and sidecar captions into outputs. If captions for a language are embedded in the input file and also appear in a sidecar file, Elastic Transcoder uses the embedded captions and ignores the sidecar captions for that language. If CaptionSources is empty, Elastic Transcoder omits all sidecar captions from the output files.
            Override: Elastic Transcoder transcodes only the sidecar captions that you specify in CaptionSources .
            MergePolicy cannot be null.
            CaptionSources (list) --Source files for the input sidecar captions used during the transcoding process. To omit all sidecar captions, leave CaptionSources blank.
            (dict) --A source file for the input sidecar captions used during the transcoding process.
            Key (string) --The name of the sidecar caption file that you want Elastic Transcoder to include in the output file.
            Language (string) --A string that specifies the language of the caption. If you specified multiple inputs with captions, the caption language must match in order to be included in the output. Specify this as one of:
            2-character ISO 639-1 code
            3-character ISO 639-2 code
            For more information on ISO language codes and language names, see the List of ISO 639-1 codes.
            TimeOffset (string) --For clip generation or captions that do not start at the same time as the associated video file, the TimeOffset tells Elastic Transcoder how much of the video to encode before including captions.
            Specify the TimeOffset in the form [+-]SS.sss or [+-]HH:mm:SS.ss.
            Label (string) --The label of the caption shown in the player when choosing a language. We recommend that you put the caption language name here, in the language of the captions.
            Encryption (dict) --The encryption settings, if any, that Elastic Transcoder needs to decyrpt your caption sources, or that you want Elastic Transcoder to apply to your caption sources.
            Mode (string) --The specific server-side encryption mode that you want Elastic Transcoder to use when decrypting your input files or encrypting your output files. Elastic Transcoder supports the following options:
            S3: Amazon S3 creates and manages the keys used for encrypting your files.
            S3-AWS-KMS: Amazon S3 calls the Amazon Key Management Service, which creates and manages the keys that are used for encrypting your files. If you specify S3-AWS-KMS and you don't want to use the default key, you must add the AWS-KMS key that you want to use to your pipeline.
            AES-CBC-PKCS7: A padded cipher-block mode of operation originally used for HLS files.
            AES-CTR: AES Counter Mode.
            AES-GCM: AES Galois Counter Mode, a mode of operation that is an authenticated encryption format, meaning that a file, key, or initialization vector that has been tampered with fails the decryption process.
            For all three AES options, you must provide the following settings, which must be base64-encoded:
            Key
            Key MD5
            Initialization Vector
            Warning
            For the AES modes, your private encryption keys and your unencrypted data are never stored by AWS; therefore, it is important that you safely manage your encryption keys. If you lose them, you won't be able to unencrypt your data.
            Key (string) --The data encryption key that you want Elastic Transcoder to use to encrypt your output file, or that was used to encrypt your input file. The key must be base64-encoded and it must be one of the following bit lengths before being base64-encoded:
            128 , 192 , or 256 .
            The key must also be encrypted by using the Amazon Key Management Service.
            KeyMd5 (string) --The MD5 digest of the key that you used to encrypt your input file, or that you want Elastic Transcoder to use to encrypt your output file. Elastic Transcoder uses the key digest as a checksum to make sure your key was not corrupted in transit. The key MD5 must be base64-encoded, and it must be exactly 16 bytes long before being base64-encoded.
            InitializationVector (string) --The series of random bits created by a random bit generator, unique for every encryption operation, that you used to encrypt your input files or that you want Elastic Transcoder to use to encrypt your output files. The initialization vector must be base64-encoded, and it must be exactly 16 bytes long before being base64-encoded.
            
            
            DetectedProperties (dict) --The detected properties of the input file.
            Width (integer) --The detected width of the input file, in pixels.
            Height (integer) --The detected height of the input file, in pixels.
            FrameRate (string) --The detected frame rate of the input file, in frames per second.
            FileSize (integer) --The detected file size of the input file, in bytes.
            DurationMillis (integer) --The detected duration of the input file, in milliseconds.
            
            

    :type Inputs: list
    :param Inputs: A section of the request body that provides information about the files that are being transcoded.
            (dict) --Information about the file that you're transcoding.
            Key (string) --The name of the file to transcode. Elsewhere in the body of the JSON block is the the ID of the pipeline to use for processing the job. The InputBucket object in that pipeline tells Elastic Transcoder which Amazon S3 bucket to get the file from.
            If the file name includes a prefix, such as cooking/lasagna.mpg , include the prefix in the key. If the file isn't in the specified bucket, Elastic Transcoder returns an error.
            FrameRate (string) --The frame rate of the input file. If you want Elastic Transcoder to automatically detect the frame rate of the input file, specify auto . If you want to specify the frame rate for the input file, enter one of the following values:
            10 , 15 , 23.97 , 24 , 25 , 29.97 , 30 , 60
            If you specify a value other than auto , Elastic Transcoder disables automatic detection of the frame rate.
            Resolution (string) --This value must be auto , which causes Elastic Transcoder to automatically detect the resolution of the input file.
            AspectRatio (string) --The aspect ratio of the input file. If you want Elastic Transcoder to automatically detect the aspect ratio of the input file, specify auto . If you want to specify the aspect ratio for the output file, enter one of the following values:
            1:1 , 4:3 , 3:2 , 16:9
            If you specify a value other than auto , Elastic Transcoder disables automatic detection of the aspect ratio.
            Interlaced (string) --Whether the input file is interlaced. If you want Elastic Transcoder to automatically detect whether the input file is interlaced, specify auto . If you want to specify whether the input file is interlaced, enter one of the following values:
            true , false
            If you specify a value other than auto , Elastic Transcoder disables automatic detection of interlacing.
            Container (string) --The container type for the input file. If you want Elastic Transcoder to automatically detect the container type of the input file, specify auto . If you want to specify the container type for the input file, enter one of the following values:
            3gp , aac , asf , avi , divx , flv , m4a , mkv , mov , mp3 , mp4 , mpeg , mpeg-ps , mpeg-ts , mxf , ogg , vob , wav , webm
            Encryption (dict) --The encryption settings, if any, that are used for decrypting your input files. If your input file is encrypted, you must specify the mode that Elastic Transcoder uses to decrypt your file.
            Mode (string) --The specific server-side encryption mode that you want Elastic Transcoder to use when decrypting your input files or encrypting your output files. Elastic Transcoder supports the following options:
            S3: Amazon S3 creates and manages the keys used for encrypting your files.
            S3-AWS-KMS: Amazon S3 calls the Amazon Key Management Service, which creates and manages the keys that are used for encrypting your files. If you specify S3-AWS-KMS and you don't want to use the default key, you must add the AWS-KMS key that you want to use to your pipeline.
            AES-CBC-PKCS7: A padded cipher-block mode of operation originally used for HLS files.
            AES-CTR: AES Counter Mode.
            AES-GCM: AES Galois Counter Mode, a mode of operation that is an authenticated encryption format, meaning that a file, key, or initialization vector that has been tampered with fails the decryption process.
            For all three AES options, you must provide the following settings, which must be base64-encoded:
            Key
            Key MD5
            Initialization Vector
            Warning
            For the AES modes, your private encryption keys and your unencrypted data are never stored by AWS; therefore, it is important that you safely manage your encryption keys. If you lose them, you won't be able to unencrypt your data.
            Key (string) --The data encryption key that you want Elastic Transcoder to use to encrypt your output file, or that was used to encrypt your input file. The key must be base64-encoded and it must be one of the following bit lengths before being base64-encoded:
            128 , 192 , or 256 .
            The key must also be encrypted by using the Amazon Key Management Service.
            KeyMd5 (string) --The MD5 digest of the key that you used to encrypt your input file, or that you want Elastic Transcoder to use to encrypt your output file. Elastic Transcoder uses the key digest as a checksum to make sure your key was not corrupted in transit. The key MD5 must be base64-encoded, and it must be exactly 16 bytes long before being base64-encoded.
            InitializationVector (string) --The series of random bits created by a random bit generator, unique for every encryption operation, that you used to encrypt your input files or that you want Elastic Transcoder to use to encrypt your output files. The initialization vector must be base64-encoded, and it must be exactly 16 bytes long before being base64-encoded.
            TimeSpan (dict) --Settings for clipping an input. Each input can have different clip settings.
            StartTime (string) --The place in the input file where you want a clip to start. The format can be either HH:mm:ss.SSS (maximum value: 23:59:59.999; SSS is thousandths of a second) or sssss.SSS (maximum value: 86399.999). If you don't specify a value, Elastic Transcoder starts at the beginning of the input file.
            Duration (string) --The duration of the clip. The format can be either HH:mm:ss.SSS (maximum value: 23:59:59.999; SSS is thousandths of a second) or sssss.SSS (maximum value: 86399.999). If you don't specify a value, Elastic Transcoder creates an output file from StartTime to the end of the file.
            If you specify a value longer than the duration of the input file, Elastic Transcoder transcodes the file and returns a warning message.
            InputCaptions (dict) --You can configure Elastic Transcoder to transcode captions, or subtitles, from one format to another. All captions must be in UTF-8. Elastic Transcoder supports two types of captions:
            Embedded: Embedded captions are included in the same file as the audio and video. Elastic Transcoder supports only one embedded caption per language, to a maximum of 300 embedded captions per file. Valid input values include: CEA-608 (EIA-608 , first non-empty channel only), CEA-708 (EIA-708 , first non-empty channel only), and mov-text  Valid outputs include: mov-text  Elastic Transcoder supports a maximum of one embedded format per output.
            Sidecar: Sidecar captions are kept in a separate metadata file from the audio and video data. Sidecar captions require a player that is capable of understanding the relationship between the video file and the sidecar file. Elastic Transcoder supports only one sidecar caption per language, to a maximum of 20 sidecar captions per file. Valid input values include: dfxp (first div element only), ebu-tt , scc , smpt , srt , ttml (first div element only), and webvtt  Valid outputs include: dfxp (first div element only), scc , srt , and webvtt .
            If you want ttml or smpte-tt compatible captions, specify dfxp as your output format.
            Elastic Transcoder does not support OCR (Optical Character Recognition), does not accept pictures as a valid input for captions, and is not available for audio-only transcoding. Elastic Transcoder does not preserve text formatting (for example, italics) during the transcoding process.
            To remove captions or leave the captions empty, set Captions to null. To pass through existing captions unchanged, set the MergePolicy to MergeRetain , and pass in a null CaptionSources array.
            For more information on embedded files, see the Subtitles Wikipedia page.
            For more information on sidecar files, see the Extensible Metadata Platform and Sidecar file Wikipedia pages.
            MergePolicy (string) --A policy that determines how Elastic Transcoder handles the existence of multiple captions.
            MergeOverride: Elastic Transcoder transcodes both embedded and sidecar captions into outputs. If captions for a language are embedded in the input file and also appear in a sidecar file, Elastic Transcoder uses the sidecar captions and ignores the embedded captions for that language.
            MergeRetain: Elastic Transcoder transcodes both embedded and sidecar captions into outputs. If captions for a language are embedded in the input file and also appear in a sidecar file, Elastic Transcoder uses the embedded captions and ignores the sidecar captions for that language. If CaptionSources is empty, Elastic Transcoder omits all sidecar captions from the output files.
            Override: Elastic Transcoder transcodes only the sidecar captions that you specify in CaptionSources .
            MergePolicy cannot be null.
            CaptionSources (list) --Source files for the input sidecar captions used during the transcoding process. To omit all sidecar captions, leave CaptionSources blank.
            (dict) --A source file for the input sidecar captions used during the transcoding process.
            Key (string) --The name of the sidecar caption file that you want Elastic Transcoder to include in the output file.
            Language (string) --A string that specifies the language of the caption. If you specified multiple inputs with captions, the caption language must match in order to be included in the output. Specify this as one of:
            2-character ISO 639-1 code
            3-character ISO 639-2 code
            For more information on ISO language codes and language names, see the List of ISO 639-1 codes.
            TimeOffset (string) --For clip generation or captions that do not start at the same time as the associated video file, the TimeOffset tells Elastic Transcoder how much of the video to encode before including captions.
            Specify the TimeOffset in the form [+-]SS.sss or [+-]HH:mm:SS.ss.
            Label (string) --The label of the caption shown in the player when choosing a language. We recommend that you put the caption language name here, in the language of the captions.
            Encryption (dict) --The encryption settings, if any, that Elastic Transcoder needs to decyrpt your caption sources, or that you want Elastic Transcoder to apply to your caption sources.
            Mode (string) --The specific server-side encryption mode that you want Elastic Transcoder to use when decrypting your input files or encrypting your output files. Elastic Transcoder supports the following options:
            S3: Amazon S3 creates and manages the keys used for encrypting your files.
            S3-AWS-KMS: Amazon S3 calls the Amazon Key Management Service, which creates and manages the keys that are used for encrypting your files. If you specify S3-AWS-KMS and you don't want to use the default key, you must add the AWS-KMS key that you want to use to your pipeline.
            AES-CBC-PKCS7: A padded cipher-block mode of operation originally used for HLS files.
            AES-CTR: AES Counter Mode.
            AES-GCM: AES Galois Counter Mode, a mode of operation that is an authenticated encryption format, meaning that a file, key, or initialization vector that has been tampered with fails the decryption process.
            For all three AES options, you must provide the following settings, which must be base64-encoded:
            Key
            Key MD5
            Initialization Vector
            Warning
            For the AES modes, your private encryption keys and your unencrypted data are never stored by AWS; therefore, it is important that you safely manage your encryption keys. If you lose them, you won't be able to unencrypt your data.
            Key (string) --The data encryption key that you want Elastic Transcoder to use to encrypt your output file, or that was used to encrypt your input file. The key must be base64-encoded and it must be one of the following bit lengths before being base64-encoded:
            128 , 192 , or 256 .
            The key must also be encrypted by using the Amazon Key Management Service.
            KeyMd5 (string) --The MD5 digest of the key that you used to encrypt your input file, or that you want Elastic Transcoder to use to encrypt your output file. Elastic Transcoder uses the key digest as a checksum to make sure your key was not corrupted in transit. The key MD5 must be base64-encoded, and it must be exactly 16 bytes long before being base64-encoded.
            InitializationVector (string) --The series of random bits created by a random bit generator, unique for every encryption operation, that you used to encrypt your input files or that you want Elastic Transcoder to use to encrypt your output files. The initialization vector must be base64-encoded, and it must be exactly 16 bytes long before being base64-encoded.
            
            
            DetectedProperties (dict) --The detected properties of the input file.
            Width (integer) --The detected width of the input file, in pixels.
            Height (integer) --The detected height of the input file, in pixels.
            FrameRate (string) --The detected frame rate of the input file, in frames per second.
            FileSize (integer) --The detected file size of the input file, in bytes.
            DurationMillis (integer) --The detected duration of the input file, in milliseconds.
            
            

    :type Output: dict
    :param Output: A section of the request body that provides information about the transcoded (target) file. We strongly recommend that you use the Outputs syntax instead of the Output syntax.
            Key (string) --The name to assign to the transcoded file. Elastic Transcoder saves the file in the Amazon S3 bucket specified by the OutputBucket object in the pipeline that is specified by the pipeline ID. If a file with the specified name already exists in the output bucket, the job fails.
            ThumbnailPattern (string) --Whether you want Elastic Transcoder to create thumbnails for your videos and, if so, how you want Elastic Transcoder to name the files.
            If you don't want Elastic Transcoder to create thumbnails, specify ''.
            If you do want Elastic Transcoder to create thumbnails, specify the information that you want to include in the file name for each thumbnail. You can specify the following values in any sequence:
            ``{count}`` (Required) : If you want to create thumbnails, you must include {count} in the ThumbnailPattern object. Wherever you specify {count} , Elastic Transcoder adds a five-digit sequence number (beginning with 00001 ) to thumbnail file names. The number indicates where a given thumbnail appears in the sequence of thumbnails for a transcoded file.
            Warning
            If you specify a literal value and/or {resolution} but you omit {count} , Elastic Transcoder returns a validation error and does not create the job.
            Literal values (Optional) : You can specify literal values anywhere in the ThumbnailPattern object. For example, you can include them as a file name prefix or as a delimiter between {resolution} and {count} .
            ``{resolution}`` (Optional) : If you want Elastic Transcoder to include the resolution in the file name, include {resolution} in the ThumbnailPattern object.
            When creating thumbnails, Elastic Transcoder automatically saves the files in the format (.jpg or .png) that appears in the preset that you specified in the PresetID value of CreateJobOutput . Elastic Transcoder also appends the applicable file name extension.
            ThumbnailEncryption (dict) --The encryption settings, if any, that you want Elastic Transcoder to apply to your thumbnail.
            Mode (string) --The specific server-side encryption mode that you want Elastic Transcoder to use when decrypting your input files or encrypting your output files. Elastic Transcoder supports the following options:
            S3: Amazon S3 creates and manages the keys used for encrypting your files.
            S3-AWS-KMS: Amazon S3 calls the Amazon Key Management Service, which creates and manages the keys that are used for encrypting your files. If you specify S3-AWS-KMS and you don't want to use the default key, you must add the AWS-KMS key that you want to use to your pipeline.
            AES-CBC-PKCS7: A padded cipher-block mode of operation originally used for HLS files.
            AES-CTR: AES Counter Mode.
            AES-GCM: AES Galois Counter Mode, a mode of operation that is an authenticated encryption format, meaning that a file, key, or initialization vector that has been tampered with fails the decryption process.
            For all three AES options, you must provide the following settings, which must be base64-encoded:
            Key
            Key MD5
            Initialization Vector
            Warning
            For the AES modes, your private encryption keys and your unencrypted data are never stored by AWS; therefore, it is important that you safely manage your encryption keys. If you lose them, you won't be able to unencrypt your data.
            Key (string) --The data encryption key that you want Elastic Transcoder to use to encrypt your output file, or that was used to encrypt your input file. The key must be base64-encoded and it must be one of the following bit lengths before being base64-encoded:
            128 , 192 , or 256 .
            The key must also be encrypted by using the Amazon Key Management Service.
            KeyMd5 (string) --The MD5 digest of the key that you used to encrypt your input file, or that you want Elastic Transcoder to use to encrypt your output file. Elastic Transcoder uses the key digest as a checksum to make sure your key was not corrupted in transit. The key MD5 must be base64-encoded, and it must be exactly 16 bytes long before being base64-encoded.
            InitializationVector (string) --The series of random bits created by a random bit generator, unique for every encryption operation, that you used to encrypt your input files or that you want Elastic Transcoder to use to encrypt your output files. The initialization vector must be base64-encoded, and it must be exactly 16 bytes long before being base64-encoded.
            Rotate (string) --The number of degrees clockwise by which you want Elastic Transcoder to rotate the output relative to the input. Enter one of the following values: auto , 0 , 90 , 180 , 270 . The value auto generally works only if the file that you're transcoding contains rotation metadata.
            PresetId (string) --The Id of the preset to use for this job. The preset determines the audio, video, and thumbnail settings that Elastic Transcoder uses for transcoding.
            SegmentDuration (string) --
            Warning
            (Outputs in Fragmented MP4 or MPEG-TS format only.
            If you specify a preset in PresetId for which the value of Container is fmp4 (Fragmented MP4) or ts (MPEG-TS), SegmentDuration is the target maximum duration of each segment in seconds. For HLSv3 format playlists, each media segment is stored in a separate .ts file. For HLSv4 and Smooth playlists, all media segments for an output are stored in a single file. Each segment is approximately the length of the SegmentDuration , though individual segments might be shorter or longer.
            The range of valid values is 1 to 60 seconds. If the duration of the video is not evenly divisible by SegmentDuration , the duration of the last segment is the remainder of total length/SegmentDuration.
            Elastic Transcoder creates an output-specific playlist for each output HLS output that you specify in OutputKeys. To add an output to the master playlist for this job, include it in the OutputKeys of the associated playlist.
            Watermarks (list) --Information about the watermarks that you want Elastic Transcoder to add to the video during transcoding. You can specify up to four watermarks for each output. Settings for each watermark must be defined in the preset for the current output.
            (dict) --Watermarks can be in .png or .jpg format. If you want to display a watermark that is not rectangular, use the .png format, which supports transparency.
            PresetWatermarkId (string) --The ID of the watermark settings that Elastic Transcoder uses to add watermarks to the video during transcoding. The settings are in the preset specified by Preset for the current output. In that preset, the value of Watermarks Id tells Elastic Transcoder which settings to use.
            InputKey (string) --The name of the .png or .jpg file that you want to use for the watermark. To determine which Amazon S3 bucket contains the specified file, Elastic Transcoder checks the pipeline specified by Pipeline ; the Input Bucket object in that pipeline identifies the bucket.
            If the file name includes a prefix, for example, logos/128x64.png , include the prefix in the key. If the file isn't in the specified bucket, Elastic Transcoder returns an error.
            Encryption (dict) --The encryption settings, if any, that you want Elastic Transcoder to apply to your watermarks.
            Mode (string) --The specific server-side encryption mode that you want Elastic Transcoder to use when decrypting your input files or encrypting your output files. Elastic Transcoder supports the following options:
            S3: Amazon S3 creates and manages the keys used for encrypting your files.
            S3-AWS-KMS: Amazon S3 calls the Amazon Key Management Service, which creates and manages the keys that are used for encrypting your files. If you specify S3-AWS-KMS and you don't want to use the default key, you must add the AWS-KMS key that you want to use to your pipeline.
            AES-CBC-PKCS7: A padded cipher-block mode of operation originally used for HLS files.
            AES-CTR: AES Counter Mode.
            AES-GCM: AES Galois Counter Mode, a mode of operation that is an authenticated encryption format, meaning that a file, key, or initialization vector that has been tampered with fails the decryption process.
            For all three AES options, you must provide the following settings, which must be base64-encoded:
            Key
            Key MD5
            Initialization Vector
            Warning
            For the AES modes, your private encryption keys and your unencrypted data are never stored by AWS; therefore, it is important that you safely manage your encryption keys. If you lose them, you won't be able to unencrypt your data.
            Key (string) --The data encryption key that you want Elastic Transcoder to use to encrypt your output file, or that was used to encrypt your input file. The key must be base64-encoded and it must be one of the following bit lengths before being base64-encoded:
            128 , 192 , or 256 .
            The key must also be encrypted by using the Amazon Key Management Service.
            KeyMd5 (string) --The MD5 digest of the key that you used to encrypt your input file, or that you want Elastic Transcoder to use to encrypt your output file. Elastic Transcoder uses the key digest as a checksum to make sure your key was not corrupted in transit. The key MD5 must be base64-encoded, and it must be exactly 16 bytes long before being base64-encoded.
            InitializationVector (string) --The series of random bits created by a random bit generator, unique for every encryption operation, that you used to encrypt your input files or that you want Elastic Transcoder to use to encrypt your output files. The initialization vector must be base64-encoded, and it must be exactly 16 bytes long before being base64-encoded.
            
            AlbumArt (dict) --Information about the album art that you want Elastic Transcoder to add to the file during transcoding. You can specify up to twenty album artworks for each output. Settings for each artwork must be defined in the job for the current output.
            MergePolicy (string) --A policy that determines how Elastic Transcoder handles the existence of multiple album artwork files.
            Replace: The specified album art replaces any existing album art.
            Prepend: The specified album art is placed in front of any existing album art.
            Append: The specified album art is placed after any existing album art.
            Fallback: If the original input file contains artwork, Elastic Transcoder uses that artwork for the output. If the original input does not contain artwork, Elastic Transcoder uses the specified album art file.
            Artwork (list) --The file to be used as album art. There can be multiple artworks associated with an audio file, to a maximum of 20. Valid formats are .jpg and .png
            (dict) --The file to be used as album art. There can be multiple artworks associated with an audio file, to a maximum of 20.
            To remove artwork or leave the artwork empty, you can either set Artwork to null, or set the Merge Policy to 'Replace' and use an empty Artwork array.
            To pass through existing artwork unchanged, set the Merge Policy to 'Prepend', 'Append', or 'Fallback', and use an empty Artwork array.
            InputKey (string) --The name of the file to be used as album art. To determine which Amazon S3 bucket contains the specified file, Elastic Transcoder checks the pipeline specified by PipelineId ; the InputBucket object in that pipeline identifies the bucket.
            If the file name includes a prefix, for example, cooking/pie.jpg , include the prefix in the key. If the file isn't in the specified bucket, Elastic Transcoder returns an error.
            MaxWidth (string) --The maximum width of the output album art in pixels. If you specify auto , Elastic Transcoder uses 600 as the default value. If you specify a numeric value, enter an even integer between 32 and 4096, inclusive.
            MaxHeight (string) --The maximum height of the output album art in pixels. If you specify auto , Elastic Transcoder uses 600 as the default value. If you specify a numeric value, enter an even integer between 32 and 3072, inclusive.
            SizingPolicy (string) --Specify one of the following values to control scaling of the output album art:
            Fit: Elastic Transcoder scales the output art so it matches the value that you specified in either MaxWidth or MaxHeight without exceeding the other value.
            Fill: Elastic Transcoder scales the output art so it matches the value that you specified in either MaxWidth or MaxHeight and matches or exceeds the other value. Elastic Transcoder centers the output art and then crops it in the dimension (if any) that exceeds the maximum value.
            Stretch: Elastic Transcoder stretches the output art to match the values that you specified for MaxWidth and MaxHeight . If the relative proportions of the input art and the output art are different, the output art will be distorted.
            Keep: Elastic Transcoder does not scale the output art. If either dimension of the input art exceeds the values that you specified for MaxWidth and MaxHeight , Elastic Transcoder crops the output art.
            ShrinkToFit: Elastic Transcoder scales the output art down so that its dimensions match the values that you specified for at least one of MaxWidth and MaxHeight without exceeding either value. If you specify this option, Elastic Transcoder does not scale the art up.
            ShrinkToFill Elastic Transcoder scales the output art down so that its dimensions match the values that you specified for at least one of MaxWidth and MaxHeight without dropping below either value. If you specify this option, Elastic Transcoder does not scale the art up.
            PaddingPolicy (string) --When you set PaddingPolicy to Pad , Elastic Transcoder may add white bars to the top and bottom and/or left and right sides of the output album art to make the total size of the output art match the values that you specified for MaxWidth and MaxHeight .
            AlbumArtFormat (string) --The format of album art, if any. Valid formats are .jpg and .png .
            Encryption (dict) --The encryption settings, if any, that you want Elastic Transcoder to apply to your artwork.
            Mode (string) --The specific server-side encryption mode that you want Elastic Transcoder to use when decrypting your input files or encrypting your output files. Elastic Transcoder supports the following options:
            S3: Amazon S3 creates and manages the keys used for encrypting your files.
            S3-AWS-KMS: Amazon S3 calls the Amazon Key Management Service, which creates and manages the keys that are used for encrypting your files. If you specify S3-AWS-KMS and you don't want to use the default key, you must add the AWS-KMS key that you want to use to your pipeline.
            AES-CBC-PKCS7: A padded cipher-block mode of operation originally used for HLS files.
            AES-CTR: AES Counter Mode.
            AES-GCM: AES Galois Counter Mode, a mode of operation that is an authenticated encryption format, meaning that a file, key, or initialization vector that has been tampered with fails the decryption process.
            For all three AES options, you must provide the following settings, which must be base64-encoded:
            Key
            Key MD5
            Initialization Vector
            Warning
            For the AES modes, your private encryption keys and your unencrypted data are never stored by AWS; therefore, it is important that you safely manage your encryption keys. If you lose them, you won't be able to unencrypt your data.
            Key (string) --The data encryption key that you want Elastic Transcoder to use to encrypt your output file, or that was used to encrypt your input file. The key must be base64-encoded and it must be one of the following bit lengths before being base64-encoded:
            128 , 192 , or 256 .
            The key must also be encrypted by using the Amazon Key Management Service.
            KeyMd5 (string) --The MD5 digest of the key that you used to encrypt your input file, or that you want Elastic Transcoder to use to encrypt your output file. Elastic Transcoder uses the key digest as a checksum to make sure your key was not corrupted in transit. The key MD5 must be base64-encoded, and it must be exactly 16 bytes long before being base64-encoded.
            InitializationVector (string) --The series of random bits created by a random bit generator, unique for every encryption operation, that you used to encrypt your input files or that you want Elastic Transcoder to use to encrypt your output files. The initialization vector must be base64-encoded, and it must be exactly 16 bytes long before being base64-encoded.
            
            
            Composition (list) --You can create an output file that contains an excerpt from the input file. This excerpt, called a clip, can come from the beginning, middle, or end of the file. The Composition object contains settings for the clips that make up an output file. For the current release, you can only specify settings for a single clip per output file. The Composition object cannot be null.
            (dict) --Settings for one clip in a composition. All jobs in a playlist must have the same clip settings.
            TimeSpan (dict) --Settings that determine when a clip begins and how long it lasts.
            StartTime (string) --The place in the input file where you want a clip to start. The format can be either HH:mm:ss.SSS (maximum value: 23:59:59.999; SSS is thousandths of a second) or sssss.SSS (maximum value: 86399.999). If you don't specify a value, Elastic Transcoder starts at the beginning of the input file.
            Duration (string) --The duration of the clip. The format can be either HH:mm:ss.SSS (maximum value: 23:59:59.999; SSS is thousandths of a second) or sssss.SSS (maximum value: 86399.999). If you don't specify a value, Elastic Transcoder creates an output file from StartTime to the end of the file.
            If you specify a value longer than the duration of the input file, Elastic Transcoder transcodes the file and returns a warning message.
            
            Captions (dict) --You can configure Elastic Transcoder to transcode captions, or subtitles, from one format to another. All captions must be in UTF-8. Elastic Transcoder supports two types of captions:
            Embedded: Embedded captions are included in the same file as the audio and video. Elastic Transcoder supports only one embedded caption per language, to a maximum of 300 embedded captions per file. Valid input values include: CEA-608 (EIA-608 , first non-empty channel only), CEA-708 (EIA-708 , first non-empty channel only), and mov-text  Valid outputs include: mov-text  Elastic Transcoder supports a maximum of one embedded format per output.
            Sidecar: Sidecar captions are kept in a separate metadata file from the audio and video data. Sidecar captions require a player that is capable of understanding the relationship between the video file and the sidecar file. Elastic Transcoder supports only one sidecar caption per language, to a maximum of 20 sidecar captions per file. Valid input values include: dfxp (first div element only), ebu-tt , scc , smpt , srt , ttml (first div element only), and webvtt  Valid outputs include: dfxp (first div element only), scc , srt , and webvtt .
            If you want ttml or smpte-tt compatible captions, specify dfxp as your output format.
            Elastic Transcoder does not support OCR (Optical Character Recognition), does not accept pictures as a valid input for captions, and is not available for audio-only transcoding. Elastic Transcoder does not preserve text formatting (for example, italics) during the transcoding process.
            To remove captions or leave the captions empty, set Captions to null. To pass through existing captions unchanged, set the MergePolicy to MergeRetain , and pass in a null CaptionSources array.
            For more information on embedded files, see the Subtitles Wikipedia page.
            For more information on sidecar files, see the Extensible Metadata Platform and Sidecar file Wikipedia pages.
            MergePolicy (string) --A policy that determines how Elastic Transcoder handles the existence of multiple captions.
            MergeOverride: Elastic Transcoder transcodes both embedded and sidecar captions into outputs. If captions for a language are embedded in the input file and also appear in a sidecar file, Elastic Transcoder uses the sidecar captions and ignores the embedded captions for that language.
            MergeRetain: Elastic Transcoder transcodes both embedded and sidecar captions into outputs. If captions for a language are embedded in the input file and also appear in a sidecar file, Elastic Transcoder uses the embedded captions and ignores the sidecar captions for that language. If CaptionSources is empty, Elastic Transcoder omits all sidecar captions from the output files.
            Override: Elastic Transcoder transcodes only the sidecar captions that you specify in CaptionSources .
            MergePolicy cannot be null.
            CaptionSources (list) --Source files for the input sidecar captions used during the transcoding process. To omit all sidecar captions, leave CaptionSources blank.
            (dict) --A source file for the input sidecar captions used during the transcoding process.
            Key (string) --The name of the sidecar caption file that you want Elastic Transcoder to include in the output file.
            Language (string) --A string that specifies the language of the caption. If you specified multiple inputs with captions, the caption language must match in order to be included in the output. Specify this as one of:
            2-character ISO 639-1 code
            3-character ISO 639-2 code
            For more information on ISO language codes and language names, see the List of ISO 639-1 codes.
            TimeOffset (string) --For clip generation or captions that do not start at the same time as the associated video file, the TimeOffset tells Elastic Transcoder how much of the video to encode before including captions.
            Specify the TimeOffset in the form [+-]SS.sss or [+-]HH:mm:SS.ss.
            Label (string) --The label of the caption shown in the player when choosing a language. We recommend that you put the caption language name here, in the language of the captions.
            Encryption (dict) --The encryption settings, if any, that Elastic Transcoder needs to decyrpt your caption sources, or that you want Elastic Transcoder to apply to your caption sources.
            Mode (string) --The specific server-side encryption mode that you want Elastic Transcoder to use when decrypting your input files or encrypting your output files. Elastic Transcoder supports the following options:
            S3: Amazon S3 creates and manages the keys used for encrypting your files.
            S3-AWS-KMS: Amazon S3 calls the Amazon Key Management Service, which creates and manages the keys that are used for encrypting your files. If you specify S3-AWS-KMS and you don't want to use the default key, you must add the AWS-KMS key that you want to use to your pipeline.
            AES-CBC-PKCS7: A padded cipher-block mode of operation originally used for HLS files.
            AES-CTR: AES Counter Mode.
            AES-GCM: AES Galois Counter Mode, a mode of operation that is an authenticated encryption format, meaning that a file, key, or initialization vector that has been tampered with fails the decryption process.
            For all three AES options, you must provide the following settings, which must be base64-encoded:
            Key
            Key MD5
            Initialization Vector
            Warning
            For the AES modes, your private encryption keys and your unencrypted data are never stored by AWS; therefore, it is important that you safely manage your encryption keys. If you lose them, you won't be able to unencrypt your data.
            Key (string) --The data encryption key that you want Elastic Transcoder to use to encrypt your output file, or that was used to encrypt your input file. The key must be base64-encoded and it must be one of the following bit lengths before being base64-encoded:
            128 , 192 , or 256 .
            The key must also be encrypted by using the Amazon Key Management Service.
            KeyMd5 (string) --The MD5 digest of the key that you used to encrypt your input file, or that you want Elastic Transcoder to use to encrypt your output file. Elastic Transcoder uses the key digest as a checksum to make sure your key was not corrupted in transit. The key MD5 must be base64-encoded, and it must be exactly 16 bytes long before being base64-encoded.
            InitializationVector (string) --The series of random bits created by a random bit generator, unique for every encryption operation, that you used to encrypt your input files or that you want Elastic Transcoder to use to encrypt your output files. The initialization vector must be base64-encoded, and it must be exactly 16 bytes long before being base64-encoded.
            
            CaptionFormats (list) --The array of file formats for the output captions. If you leave this value blank, Elastic Transcoder returns an error.
            (dict) --The file format of the output captions. If you leave this value blank, Elastic Transcoder returns an error.
            Format (string) --The format you specify determines whether Elastic Transcoder generates an embedded or sidecar caption for this output.
            Valid Embedded Caption Formats:
            for FLAC : None
            For MP3 : None
            For MP4 : mov-text
            For MPEG-TS : None
            For ogg : None
            For webm : None
            Valid Sidecar Caption Formats: Elastic Transcoder supports dfxp (first div element only), scc, srt, and webvtt. If you want ttml or smpte-tt compatible captions, specify dfxp as your output format.
            For FMP4 : dfxp
            Non-FMP4 outputs : All sidecar types
            
            fmp4 captions have an extension of .ismt
            Pattern (string) --The prefix for caption filenames, in the form description -{language} , where:
            description is a description of the video.
            {language} is a literal value that Elastic Transcoder replaces with the two- or three-letter code for the language of the caption in the output file names.
            If you don't include {language} in the file name pattern, Elastic Transcoder automatically appends '{language} ' to the value that you specify for the description. In addition, Elastic Transcoder automatically appends the count to the end of the segment files.
            For example, suppose you're transcoding into srt format. When you enter 'Sydney-{language}-sunrise', and the language of the captions is English (en), the name of the first caption file is be Sydney-en-sunrise00000.srt.
            Encryption (dict) --The encryption settings, if any, that you want Elastic Transcoder to apply to your caption formats.
            Mode (string) --The specific server-side encryption mode that you want Elastic Transcoder to use when decrypting your input files or encrypting your output files. Elastic Transcoder supports the following options:
            S3: Amazon S3 creates and manages the keys used for encrypting your files.
            S3-AWS-KMS: Amazon S3 calls the Amazon Key Management Service, which creates and manages the keys that are used for encrypting your files. If you specify S3-AWS-KMS and you don't want to use the default key, you must add the AWS-KMS key that you want to use to your pipeline.
            AES-CBC-PKCS7: A padded cipher-block mode of operation originally used for HLS files.
            AES-CTR: AES Counter Mode.
            AES-GCM: AES Galois Counter Mode, a mode of operation that is an authenticated encryption format, meaning that a file, key, or initialization vector that has been tampered with fails the decryption process.
            For all three AES options, you must provide the following settings, which must be base64-encoded:
            Key
            Key MD5
            Initialization Vector
            Warning
            For the AES modes, your private encryption keys and your unencrypted data are never stored by AWS; therefore, it is important that you safely manage your encryption keys. If you lose them, you won't be able to unencrypt your data.
            Key (string) --The data encryption key that you want Elastic Transcoder to use to encrypt your output file, or that was used to encrypt your input file. The key must be base64-encoded and it must be one of the following bit lengths before being base64-encoded:
            128 , 192 , or 256 .
            The key must also be encrypted by using the Amazon Key Management Service.
            KeyMd5 (string) --The MD5 digest of the key that you used to encrypt your input file, or that you want Elastic Transcoder to use to encrypt your output file. Elastic Transcoder uses the key digest as a checksum to make sure your key was not corrupted in transit. The key MD5 must be base64-encoded, and it must be exactly 16 bytes long before being base64-encoded.
            InitializationVector (string) --The series of random bits created by a random bit generator, unique for every encryption operation, that you used to encrypt your input files or that you want Elastic Transcoder to use to encrypt your output files. The initialization vector must be base64-encoded, and it must be exactly 16 bytes long before being base64-encoded.
            
            
            Encryption (dict) --You can specify encryption settings for any output files that you want to use for a transcoding job. This includes the output file and any watermarks, thumbnails, album art, or captions that you want to use. You must specify encryption settings for each file individually.
            Mode (string) --The specific server-side encryption mode that you want Elastic Transcoder to use when decrypting your input files or encrypting your output files. Elastic Transcoder supports the following options:
            S3: Amazon S3 creates and manages the keys used for encrypting your files.
            S3-AWS-KMS: Amazon S3 calls the Amazon Key Management Service, which creates and manages the keys that are used for encrypting your files. If you specify S3-AWS-KMS and you don't want to use the default key, you must add the AWS-KMS key that you want to use to your pipeline.
            AES-CBC-PKCS7: A padded cipher-block mode of operation originally used for HLS files.
            AES-CTR: AES Counter Mode.
            AES-GCM: AES Galois Counter Mode, a mode of operation that is an authenticated encryption format, meaning that a file, key, or initialization vector that has been tampered with fails the decryption process.
            For all three AES options, you must provide the following settings, which must be base64-encoded:
            Key
            Key MD5
            Initialization Vector
            Warning
            For the AES modes, your private encryption keys and your unencrypted data are never stored by AWS; therefore, it is important that you safely manage your encryption keys. If you lose them, you won't be able to unencrypt your data.
            Key (string) --The data encryption key that you want Elastic Transcoder to use to encrypt your output file, or that was used to encrypt your input file. The key must be base64-encoded and it must be one of the following bit lengths before being base64-encoded:
            128 , 192 , or 256 .
            The key must also be encrypted by using the Amazon Key Management Service.
            KeyMd5 (string) --The MD5 digest of the key that you used to encrypt your input file, or that you want Elastic Transcoder to use to encrypt your output file. Elastic Transcoder uses the key digest as a checksum to make sure your key was not corrupted in transit. The key MD5 must be base64-encoded, and it must be exactly 16 bytes long before being base64-encoded.
            InitializationVector (string) --The series of random bits created by a random bit generator, unique for every encryption operation, that you used to encrypt your input files or that you want Elastic Transcoder to use to encrypt your output files. The initialization vector must be base64-encoded, and it must be exactly 16 bytes long before being base64-encoded.
            
            

    :type Outputs: list
    :param Outputs: A section of the request body that provides information about the transcoded (target) files. We recommend that you use the Outputs syntax instead of the Output syntax.
            (dict) --The CreateJobOutput structure.
            Key (string) --The name to assign to the transcoded file. Elastic Transcoder saves the file in the Amazon S3 bucket specified by the OutputBucket object in the pipeline that is specified by the pipeline ID. If a file with the specified name already exists in the output bucket, the job fails.
            ThumbnailPattern (string) --Whether you want Elastic Transcoder to create thumbnails for your videos and, if so, how you want Elastic Transcoder to name the files.
            If you don't want Elastic Transcoder to create thumbnails, specify ''.
            If you do want Elastic Transcoder to create thumbnails, specify the information that you want to include in the file name for each thumbnail. You can specify the following values in any sequence:
            ``{count}`` (Required) : If you want to create thumbnails, you must include {count} in the ThumbnailPattern object. Wherever you specify {count} , Elastic Transcoder adds a five-digit sequence number (beginning with 00001 ) to thumbnail file names. The number indicates where a given thumbnail appears in the sequence of thumbnails for a transcoded file.
            Warning
            If you specify a literal value and/or {resolution} but you omit {count} , Elastic Transcoder returns a validation error and does not create the job.
            Literal values (Optional) : You can specify literal values anywhere in the ThumbnailPattern object. For example, you can include them as a file name prefix or as a delimiter between {resolution} and {count} .
            ``{resolution}`` (Optional) : If you want Elastic Transcoder to include the resolution in the file name, include {resolution} in the ThumbnailPattern object.
            When creating thumbnails, Elastic Transcoder automatically saves the files in the format (.jpg or .png) that appears in the preset that you specified in the PresetID value of CreateJobOutput . Elastic Transcoder also appends the applicable file name extension.
            ThumbnailEncryption (dict) --The encryption settings, if any, that you want Elastic Transcoder to apply to your thumbnail.
            Mode (string) --The specific server-side encryption mode that you want Elastic Transcoder to use when decrypting your input files or encrypting your output files. Elastic Transcoder supports the following options:
            S3: Amazon S3 creates and manages the keys used for encrypting your files.
            S3-AWS-KMS: Amazon S3 calls the Amazon Key Management Service, which creates and manages the keys that are used for encrypting your files. If you specify S3-AWS-KMS and you don't want to use the default key, you must add the AWS-KMS key that you want to use to your pipeline.
            AES-CBC-PKCS7: A padded cipher-block mode of operation originally used for HLS files.
            AES-CTR: AES Counter Mode.
            AES-GCM: AES Galois Counter Mode, a mode of operation that is an authenticated encryption format, meaning that a file, key, or initialization vector that has been tampered with fails the decryption process.
            For all three AES options, you must provide the following settings, which must be base64-encoded:
            Key
            Key MD5
            Initialization Vector
            Warning
            For the AES modes, your private encryption keys and your unencrypted data are never stored by AWS; therefore, it is important that you safely manage your encryption keys. If you lose them, you won't be able to unencrypt your data.
            Key (string) --The data encryption key that you want Elastic Transcoder to use to encrypt your output file, or that was used to encrypt your input file. The key must be base64-encoded and it must be one of the following bit lengths before being base64-encoded:
            128 , 192 , or 256 .
            The key must also be encrypted by using the Amazon Key Management Service.
            KeyMd5 (string) --The MD5 digest of the key that you used to encrypt your input file, or that you want Elastic Transcoder to use to encrypt your output file. Elastic Transcoder uses the key digest as a checksum to make sure your key was not corrupted in transit. The key MD5 must be base64-encoded, and it must be exactly 16 bytes long before being base64-encoded.
            InitializationVector (string) --The series of random bits created by a random bit generator, unique for every encryption operation, that you used to encrypt your input files or that you want Elastic Transcoder to use to encrypt your output files. The initialization vector must be base64-encoded, and it must be exactly 16 bytes long before being base64-encoded.
            Rotate (string) --The number of degrees clockwise by which you want Elastic Transcoder to rotate the output relative to the input. Enter one of the following values: auto , 0 , 90 , 180 , 270 . The value auto generally works only if the file that you're transcoding contains rotation metadata.
            PresetId (string) --The Id of the preset to use for this job. The preset determines the audio, video, and thumbnail settings that Elastic Transcoder uses for transcoding.
            SegmentDuration (string) --
            Warning
            (Outputs in Fragmented MP4 or MPEG-TS format only.
            If you specify a preset in PresetId for which the value of Container is fmp4 (Fragmented MP4) or ts (MPEG-TS), SegmentDuration is the target maximum duration of each segment in seconds. For HLSv3 format playlists, each media segment is stored in a separate .ts file. For HLSv4 and Smooth playlists, all media segments for an output are stored in a single file. Each segment is approximately the length of the SegmentDuration , though individual segments might be shorter or longer.
            The range of valid values is 1 to 60 seconds. If the duration of the video is not evenly divisible by SegmentDuration , the duration of the last segment is the remainder of total length/SegmentDuration.
            Elastic Transcoder creates an output-specific playlist for each output HLS output that you specify in OutputKeys. To add an output to the master playlist for this job, include it in the OutputKeys of the associated playlist.
            Watermarks (list) --Information about the watermarks that you want Elastic Transcoder to add to the video during transcoding. You can specify up to four watermarks for each output. Settings for each watermark must be defined in the preset for the current output.
            (dict) --Watermarks can be in .png or .jpg format. If you want to display a watermark that is not rectangular, use the .png format, which supports transparency.
            PresetWatermarkId (string) --The ID of the watermark settings that Elastic Transcoder uses to add watermarks to the video during transcoding. The settings are in the preset specified by Preset for the current output. In that preset, the value of Watermarks Id tells Elastic Transcoder which settings to use.
            InputKey (string) --The name of the .png or .jpg file that you want to use for the watermark. To determine which Amazon S3 bucket contains the specified file, Elastic Transcoder checks the pipeline specified by Pipeline ; the Input Bucket object in that pipeline identifies the bucket.
            If the file name includes a prefix, for example, logos/128x64.png , include the prefix in the key. If the file isn't in the specified bucket, Elastic Transcoder returns an error.
            Encryption (dict) --The encryption settings, if any, that you want Elastic Transcoder to apply to your watermarks.
            Mode (string) --The specific server-side encryption mode that you want Elastic Transcoder to use when decrypting your input files or encrypting your output files. Elastic Transcoder supports the following options:
            S3: Amazon S3 creates and manages the keys used for encrypting your files.
            S3-AWS-KMS: Amazon S3 calls the Amazon Key Management Service, which creates and manages the keys that are used for encrypting your files. If you specify S3-AWS-KMS and you don't want to use the default key, you must add the AWS-KMS key that you want to use to your pipeline.
            AES-CBC-PKCS7: A padded cipher-block mode of operation originally used for HLS files.
            AES-CTR: AES Counter Mode.
            AES-GCM: AES Galois Counter Mode, a mode of operation that is an authenticated encryption format, meaning that a file, key, or initialization vector that has been tampered with fails the decryption process.
            For all three AES options, you must provide the following settings, which must be base64-encoded:
            Key
            Key MD5
            Initialization Vector
            Warning
            For the AES modes, your private encryption keys and your unencrypted data are never stored by AWS; therefore, it is important that you safely manage your encryption keys. If you lose them, you won't be able to unencrypt your data.
            Key (string) --The data encryption key that you want Elastic Transcoder to use to encrypt your output file, or that was used to encrypt your input file. The key must be base64-encoded and it must be one of the following bit lengths before being base64-encoded:
            128 , 192 , or 256 .
            The key must also be encrypted by using the Amazon Key Management Service.
            KeyMd5 (string) --The MD5 digest of the key that you used to encrypt your input file, or that you want Elastic Transcoder to use to encrypt your output file. Elastic Transcoder uses the key digest as a checksum to make sure your key was not corrupted in transit. The key MD5 must be base64-encoded, and it must be exactly 16 bytes long before being base64-encoded.
            InitializationVector (string) --The series of random bits created by a random bit generator, unique for every encryption operation, that you used to encrypt your input files or that you want Elastic Transcoder to use to encrypt your output files. The initialization vector must be base64-encoded, and it must be exactly 16 bytes long before being base64-encoded.
            
            AlbumArt (dict) --Information about the album art that you want Elastic Transcoder to add to the file during transcoding. You can specify up to twenty album artworks for each output. Settings for each artwork must be defined in the job for the current output.
            MergePolicy (string) --A policy that determines how Elastic Transcoder handles the existence of multiple album artwork files.
            Replace: The specified album art replaces any existing album art.
            Prepend: The specified album art is placed in front of any existing album art.
            Append: The specified album art is placed after any existing album art.
            Fallback: If the original input file contains artwork, Elastic Transcoder uses that artwork for the output. If the original input does not contain artwork, Elastic Transcoder uses the specified album art file.
            Artwork (list) --The file to be used as album art. There can be multiple artworks associated with an audio file, to a maximum of 20. Valid formats are .jpg and .png
            (dict) --The file to be used as album art. There can be multiple artworks associated with an audio file, to a maximum of 20.
            To remove artwork or leave the artwork empty, you can either set Artwork to null, or set the Merge Policy to 'Replace' and use an empty Artwork array.
            To pass through existing artwork unchanged, set the Merge Policy to 'Prepend', 'Append', or 'Fallback', and use an empty Artwork array.
            InputKey (string) --The name of the file to be used as album art. To determine which Amazon S3 bucket contains the specified file, Elastic Transcoder checks the pipeline specified by PipelineId ; the InputBucket object in that pipeline identifies the bucket.
            If the file name includes a prefix, for example, cooking/pie.jpg , include the prefix in the key. If the file isn't in the specified bucket, Elastic Transcoder returns an error.
            MaxWidth (string) --The maximum width of the output album art in pixels. If you specify auto , Elastic Transcoder uses 600 as the default value. If you specify a numeric value, enter an even integer between 32 and 4096, inclusive.
            MaxHeight (string) --The maximum height of the output album art in pixels. If you specify auto , Elastic Transcoder uses 600 as the default value. If you specify a numeric value, enter an even integer between 32 and 3072, inclusive.
            SizingPolicy (string) --Specify one of the following values to control scaling of the output album art:
            Fit: Elastic Transcoder scales the output art so it matches the value that you specified in either MaxWidth or MaxHeight without exceeding the other value.
            Fill: Elastic Transcoder scales the output art so it matches the value that you specified in either MaxWidth or MaxHeight and matches or exceeds the other value. Elastic Transcoder centers the output art and then crops it in the dimension (if any) that exceeds the maximum value.
            Stretch: Elastic Transcoder stretches the output art to match the values that you specified for MaxWidth and MaxHeight . If the relative proportions of the input art and the output art are different, the output art will be distorted.
            Keep: Elastic Transcoder does not scale the output art. If either dimension of the input art exceeds the values that you specified for MaxWidth and MaxHeight , Elastic Transcoder crops the output art.
            ShrinkToFit: Elastic Transcoder scales the output art down so that its dimensions match the values that you specified for at least one of MaxWidth and MaxHeight without exceeding either value. If you specify this option, Elastic Transcoder does not scale the art up.
            ShrinkToFill Elastic Transcoder scales the output art down so that its dimensions match the values that you specified for at least one of MaxWidth and MaxHeight without dropping below either value. If you specify this option, Elastic Transcoder does not scale the art up.
            PaddingPolicy (string) --When you set PaddingPolicy to Pad , Elastic Transcoder may add white bars to the top and bottom and/or left and right sides of the output album art to make the total size of the output art match the values that you specified for MaxWidth and MaxHeight .
            AlbumArtFormat (string) --The format of album art, if any. Valid formats are .jpg and .png .
            Encryption (dict) --The encryption settings, if any, that you want Elastic Transcoder to apply to your artwork.
            Mode (string) --The specific server-side encryption mode that you want Elastic Transcoder to use when decrypting your input files or encrypting your output files. Elastic Transcoder supports the following options:
            S3: Amazon S3 creates and manages the keys used for encrypting your files.
            S3-AWS-KMS: Amazon S3 calls the Amazon Key Management Service, which creates and manages the keys that are used for encrypting your files. If you specify S3-AWS-KMS and you don't want to use the default key, you must add the AWS-KMS key that you want to use to your pipeline.
            AES-CBC-PKCS7: A padded cipher-block mode of operation originally used for HLS files.
            AES-CTR: AES Counter Mode.
            AES-GCM: AES Galois Counter Mode, a mode of operation that is an authenticated encryption format, meaning that a file, key, or initialization vector that has been tampered with fails the decryption process.
            For all three AES options, you must provide the following settings, which must be base64-encoded:
            Key
            Key MD5
            Initialization Vector
            Warning
            For the AES modes, your private encryption keys and your unencrypted data are never stored by AWS; therefore, it is important that you safely manage your encryption keys. If you lose them, you won't be able to unencrypt your data.
            Key (string) --The data encryption key that you want Elastic Transcoder to use to encrypt your output file, or that was used to encrypt your input file. The key must be base64-encoded and it must be one of the following bit lengths before being base64-encoded:
            128 , 192 , or 256 .
            The key must also be encrypted by using the Amazon Key Management Service.
            KeyMd5 (string) --The MD5 digest of the key that you used to encrypt your input file, or that you want Elastic Transcoder to use to encrypt your output file. Elastic Transcoder uses the key digest as a checksum to make sure your key was not corrupted in transit. The key MD5 must be base64-encoded, and it must be exactly 16 bytes long before being base64-encoded.
            InitializationVector (string) --The series of random bits created by a random bit generator, unique for every encryption operation, that you used to encrypt your input files or that you want Elastic Transcoder to use to encrypt your output files. The initialization vector must be base64-encoded, and it must be exactly 16 bytes long before being base64-encoded.
            
            
            Composition (list) --You can create an output file that contains an excerpt from the input file. This excerpt, called a clip, can come from the beginning, middle, or end of the file. The Composition object contains settings for the clips that make up an output file. For the current release, you can only specify settings for a single clip per output file. The Composition object cannot be null.
            (dict) --Settings for one clip in a composition. All jobs in a playlist must have the same clip settings.
            TimeSpan (dict) --Settings that determine when a clip begins and how long it lasts.
            StartTime (string) --The place in the input file where you want a clip to start. The format can be either HH:mm:ss.SSS (maximum value: 23:59:59.999; SSS is thousandths of a second) or sssss.SSS (maximum value: 86399.999). If you don't specify a value, Elastic Transcoder starts at the beginning of the input file.
            Duration (string) --The duration of the clip. The format can be either HH:mm:ss.SSS (maximum value: 23:59:59.999; SSS is thousandths of a second) or sssss.SSS (maximum value: 86399.999). If you don't specify a value, Elastic Transcoder creates an output file from StartTime to the end of the file.
            If you specify a value longer than the duration of the input file, Elastic Transcoder transcodes the file and returns a warning message.
            
            Captions (dict) --You can configure Elastic Transcoder to transcode captions, or subtitles, from one format to another. All captions must be in UTF-8. Elastic Transcoder supports two types of captions:
            Embedded: Embedded captions are included in the same file as the audio and video. Elastic Transcoder supports only one embedded caption per language, to a maximum of 300 embedded captions per file. Valid input values include: CEA-608 (EIA-608 , first non-empty channel only), CEA-708 (EIA-708 , first non-empty channel only), and mov-text  Valid outputs include: mov-text  Elastic Transcoder supports a maximum of one embedded format per output.
            Sidecar: Sidecar captions are kept in a separate metadata file from the audio and video data. Sidecar captions require a player that is capable of understanding the relationship between the video file and the sidecar file. Elastic Transcoder supports only one sidecar caption per language, to a maximum of 20 sidecar captions per file. Valid input values include: dfxp (first div element only), ebu-tt , scc , smpt , srt , ttml (first div element only), and webvtt  Valid outputs include: dfxp (first div element only), scc , srt , and webvtt .
            If you want ttml or smpte-tt compatible captions, specify dfxp as your output format.
            Elastic Transcoder does not support OCR (Optical Character Recognition), does not accept pictures as a valid input for captions, and is not available for audio-only transcoding. Elastic Transcoder does not preserve text formatting (for example, italics) during the transcoding process.
            To remove captions or leave the captions empty, set Captions to null. To pass through existing captions unchanged, set the MergePolicy to MergeRetain , and pass in a null CaptionSources array.
            For more information on embedded files, see the Subtitles Wikipedia page.
            For more information on sidecar files, see the Extensible Metadata Platform and Sidecar file Wikipedia pages.
            MergePolicy (string) --A policy that determines how Elastic Transcoder handles the existence of multiple captions.
            MergeOverride: Elastic Transcoder transcodes both embedded and sidecar captions into outputs. If captions for a language are embedded in the input file and also appear in a sidecar file, Elastic Transcoder uses the sidecar captions and ignores the embedded captions for that language.
            MergeRetain: Elastic Transcoder transcodes both embedded and sidecar captions into outputs. If captions for a language are embedded in the input file and also appear in a sidecar file, Elastic Transcoder uses the embedded captions and ignores the sidecar captions for that language. If CaptionSources is empty, Elastic Transcoder omits all sidecar captions from the output files.
            Override: Elastic Transcoder transcodes only the sidecar captions that you specify in CaptionSources .
            MergePolicy cannot be null.
            CaptionSources (list) --Source files for the input sidecar captions used during the transcoding process. To omit all sidecar captions, leave CaptionSources blank.
            (dict) --A source file for the input sidecar captions used during the transcoding process.
            Key (string) --The name of the sidecar caption file that you want Elastic Transcoder to include in the output file.
            Language (string) --A string that specifies the language of the caption. If you specified multiple inputs with captions, the caption language must match in order to be included in the output. Specify this as one of:
            2-character ISO 639-1 code
            3-character ISO 639-2 code
            For more information on ISO language codes and language names, see the List of ISO 639-1 codes.
            TimeOffset (string) --For clip generation or captions that do not start at the same time as the associated video file, the TimeOffset tells Elastic Transcoder how much of the video to encode before including captions.
            Specify the TimeOffset in the form [+-]SS.sss or [+-]HH:mm:SS.ss.
            Label (string) --The label of the caption shown in the player when choosing a language. We recommend that you put the caption language name here, in the language of the captions.
            Encryption (dict) --The encryption settings, if any, that Elastic Transcoder needs to decyrpt your caption sources, or that you want Elastic Transcoder to apply to your caption sources.
            Mode (string) --The specific server-side encryption mode that you want Elastic Transcoder to use when decrypting your input files or encrypting your output files. Elastic Transcoder supports the following options:
            S3: Amazon S3 creates and manages the keys used for encrypting your files.
            S3-AWS-KMS: Amazon S3 calls the Amazon Key Management Service, which creates and manages the keys that are used for encrypting your files. If you specify S3-AWS-KMS and you don't want to use the default key, you must add the AWS-KMS key that you want to use to your pipeline.
            AES-CBC-PKCS7: A padded cipher-block mode of operation originally used for HLS files.
            AES-CTR: AES Counter Mode.
            AES-GCM: AES Galois Counter Mode, a mode of operation that is an authenticated encryption format, meaning that a file, key, or initialization vector that has been tampered with fails the decryption process.
            For all three AES options, you must provide the following settings, which must be base64-encoded:
            Key
            Key MD5
            Initialization Vector
            Warning
            For the AES modes, your private encryption keys and your unencrypted data are never stored by AWS; therefore, it is important that you safely manage your encryption keys. If you lose them, you won't be able to unencrypt your data.
            Key (string) --The data encryption key that you want Elastic Transcoder to use to encrypt your output file, or that was used to encrypt your input file. The key must be base64-encoded and it must be one of the following bit lengths before being base64-encoded:
            128 , 192 , or 256 .
            The key must also be encrypted by using the Amazon Key Management Service.
            KeyMd5 (string) --The MD5 digest of the key that you used to encrypt your input file, or that you want Elastic Transcoder to use to encrypt your output file. Elastic Transcoder uses the key digest as a checksum to make sure your key was not corrupted in transit. The key MD5 must be base64-encoded, and it must be exactly 16 bytes long before being base64-encoded.
            InitializationVector (string) --The series of random bits created by a random bit generator, unique for every encryption operation, that you used to encrypt your input files or that you want Elastic Transcoder to use to encrypt your output files. The initialization vector must be base64-encoded, and it must be exactly 16 bytes long before being base64-encoded.
            
            CaptionFormats (list) --The array of file formats for the output captions. If you leave this value blank, Elastic Transcoder returns an error.
            (dict) --The file format of the output captions. If you leave this value blank, Elastic Transcoder returns an error.
            Format (string) --The format you specify determines whether Elastic Transcoder generates an embedded or sidecar caption for this output.
            Valid Embedded Caption Formats:
            for FLAC : None
            For MP3 : None
            For MP4 : mov-text
            For MPEG-TS : None
            For ogg : None
            For webm : None
            Valid Sidecar Caption Formats: Elastic Transcoder supports dfxp (first div element only), scc, srt, and webvtt. If you want ttml or smpte-tt compatible captions, specify dfxp as your output format.
            For FMP4 : dfxp
            Non-FMP4 outputs : All sidecar types
            
            fmp4 captions have an extension of .ismt
            Pattern (string) --The prefix for caption filenames, in the form description -{language} , where:
            description is a description of the video.
            {language} is a literal value that Elastic Transcoder replaces with the two- or three-letter code for the language of the caption in the output file names.
            If you don't include {language} in the file name pattern, Elastic Transcoder automatically appends '{language} ' to the value that you specify for the description. In addition, Elastic Transcoder automatically appends the count to the end of the segment files.
            For example, suppose you're transcoding into srt format. When you enter 'Sydney-{language}-sunrise', and the language of the captions is English (en), the name of the first caption file is be Sydney-en-sunrise00000.srt.
            Encryption (dict) --The encryption settings, if any, that you want Elastic Transcoder to apply to your caption formats.
            Mode (string) --The specific server-side encryption mode that you want Elastic Transcoder to use when decrypting your input files or encrypting your output files. Elastic Transcoder supports the following options:
            S3: Amazon S3 creates and manages the keys used for encrypting your files.
            S3-AWS-KMS: Amazon S3 calls the Amazon Key Management Service, which creates and manages the keys that are used for encrypting your files. If you specify S3-AWS-KMS and you don't want to use the default key, you must add the AWS-KMS key that you want to use to your pipeline.
            AES-CBC-PKCS7: A padded cipher-block mode of operation originally used for HLS files.
            AES-CTR: AES Counter Mode.
            AES-GCM: AES Galois Counter Mode, a mode of operation that is an authenticated encryption format, meaning that a file, key, or initialization vector that has been tampered with fails the decryption process.
            For all three AES options, you must provide the following settings, which must be base64-encoded:
            Key
            Key MD5
            Initialization Vector
            Warning
            For the AES modes, your private encryption keys and your unencrypted data are never stored by AWS; therefore, it is important that you safely manage your encryption keys. If you lose them, you won't be able to unencrypt your data.
            Key (string) --The data encryption key that you want Elastic Transcoder to use to encrypt your output file, or that was used to encrypt your input file. The key must be base64-encoded and it must be one of the following bit lengths before being base64-encoded:
            128 , 192 , or 256 .
            The key must also be encrypted by using the Amazon Key Management Service.
            KeyMd5 (string) --The MD5 digest of the key that you used to encrypt your input file, or that you want Elastic Transcoder to use to encrypt your output file. Elastic Transcoder uses the key digest as a checksum to make sure your key was not corrupted in transit. The key MD5 must be base64-encoded, and it must be exactly 16 bytes long before being base64-encoded.
            InitializationVector (string) --The series of random bits created by a random bit generator, unique for every encryption operation, that you used to encrypt your input files or that you want Elastic Transcoder to use to encrypt your output files. The initialization vector must be base64-encoded, and it must be exactly 16 bytes long before being base64-encoded.
            
            
            Encryption (dict) --You can specify encryption settings for any output files that you want to use for a transcoding job. This includes the output file and any watermarks, thumbnails, album art, or captions that you want to use. You must specify encryption settings for each file individually.
            Mode (string) --The specific server-side encryption mode that you want Elastic Transcoder to use when decrypting your input files or encrypting your output files. Elastic Transcoder supports the following options:
            S3: Amazon S3 creates and manages the keys used for encrypting your files.
            S3-AWS-KMS: Amazon S3 calls the Amazon Key Management Service, which creates and manages the keys that are used for encrypting your files. If you specify S3-AWS-KMS and you don't want to use the default key, you must add the AWS-KMS key that you want to use to your pipeline.
            AES-CBC-PKCS7: A padded cipher-block mode of operation originally used for HLS files.
            AES-CTR: AES Counter Mode.
            AES-GCM: AES Galois Counter Mode, a mode of operation that is an authenticated encryption format, meaning that a file, key, or initialization vector that has been tampered with fails the decryption process.
            For all three AES options, you must provide the following settings, which must be base64-encoded:
            Key
            Key MD5
            Initialization Vector
            Warning
            For the AES modes, your private encryption keys and your unencrypted data are never stored by AWS; therefore, it is important that you safely manage your encryption keys. If you lose them, you won't be able to unencrypt your data.
            Key (string) --The data encryption key that you want Elastic Transcoder to use to encrypt your output file, or that was used to encrypt your input file. The key must be base64-encoded and it must be one of the following bit lengths before being base64-encoded:
            128 , 192 , or 256 .
            The key must also be encrypted by using the Amazon Key Management Service.
            KeyMd5 (string) --The MD5 digest of the key that you used to encrypt your input file, or that you want Elastic Transcoder to use to encrypt your output file. Elastic Transcoder uses the key digest as a checksum to make sure your key was not corrupted in transit. The key MD5 must be base64-encoded, and it must be exactly 16 bytes long before being base64-encoded.
            InitializationVector (string) --The series of random bits created by a random bit generator, unique for every encryption operation, that you used to encrypt your input files or that you want Elastic Transcoder to use to encrypt your output files. The initialization vector must be base64-encoded, and it must be exactly 16 bytes long before being base64-encoded.
            
            

    :type OutputKeyPrefix: string
    :param OutputKeyPrefix: The value, if any, that you want Elastic Transcoder to prepend to the names of all files that this job creates, including output files, thumbnails, and playlists.

    :type Playlists: list
    :param Playlists: If you specify a preset in PresetId for which the value of Container is fmp4 (Fragmented MP4) or ts (MPEG-TS), Playlists contains information about the master playlists that you want Elastic Transcoder to create.
            The maximum number of master playlists in a job is 30.
            (dict) --Information about the master playlist.
            Name (string) --The name that you want Elastic Transcoder to assign to the master playlist, for example, nyc-vacation.m3u8. If the name includes a / character, the section of the name before the last / must be identical for all Name objects. If you create more than one master playlist, the values of all Name objects must be unique.
            Note
            Elastic Transcoder automatically appends the relevant file extension to the file name (.m3u8 for HLSv3 and HLSv4 playlists, and .ism and .ismc for Smooth playlists). If you include a file extension in Name , the file name will have two extensions.
            Format (string) --The format of the output playlist. Valid formats include HLSv3 , HLSv4 , and Smooth .
            OutputKeys (list) --For each output in this job that you want to include in a master playlist, the value of the Outputs:Key object.
            If your output is not HLS or does not have a segment duration set, the name of the output file is a concatenation of OutputKeyPrefix and Outputs:Key : OutputKeyPrefix``Outputs:Key``
            If your output is HLSv3 and has a segment duration set, or is not included in a playlist, Elastic Transcoder creates an output playlist file with a file extension of .m3u8 , and a series of .ts files that include a five-digit sequential counter beginning with 00000: OutputKeyPrefix``Outputs:Key`` .m3u8 OutputKeyPrefix``Outputs:Key`` 00000.ts
            If your output is HLSv4 , has a segment duration set, and is included in an HLSv4 playlist, Elastic Transcoder creates an output playlist file with a file extension of _v4.m3u8 . If the output is video, Elastic Transcoder also creates an output file with an extension of _iframe.m3u8 : OutputKeyPrefix``Outputs:Key`` _v4.m3u8 OutputKeyPrefix``Outputs:Key`` _iframe.m3u8 OutputKeyPrefix``Outputs:Key`` .ts
            Elastic Transcoder automatically appends the relevant file extension to the file name. If you include a file extension in Output Key, the file name will have two extensions.
            If you include more than one output in a playlist, any segment duration settings, clip settings, or caption settings must be the same for all outputs in the playlist. For Smooth playlists, the Audio:Profile , Video:Profile , and Video:FrameRate to Video:KeyframesMaxDist ratio must be the same for all outputs.
            (string) --
            HlsContentProtection (dict) --The HLS content protection settings, if any, that you want Elastic Transcoder to apply to the output files associated with this playlist.
            Method (string) --The content protection method for your output. The only valid value is: aes-128 .
            This value is written into the method attribute of the EXT-X-KEY metadata tag in the output playlist.
            Key (string) --If you want Elastic Transcoder to generate a key for you, leave this field blank.
            If you choose to supply your own key, you must encrypt the key by using AWS KMS. The key must be base64-encoded, and it must be one of the following bit lengths before being base64-encoded:
            128 , 192 , or 256 .
            KeyMd5 (string) --If Elastic Transcoder is generating your key for you, you must leave this field blank.
            The MD5 digest of the key that you want Elastic Transcoder to use to encrypt your output file, and that you want Elastic Transcoder to use as a checksum to make sure your key was not corrupted in transit. The key MD5 must be base64-encoded, and it must be exactly 16 bytes before being base64- encoded.
            InitializationVector (string) --If Elastic Transcoder is generating your key for you, you must leave this field blank.
            The series of random bits created by a random bit generator, unique for every encryption operation, that you want Elastic Transcoder to use to encrypt your output files. The initialization vector must be base64-encoded, and it must be exactly 16 bytes before being base64-encoded.
            LicenseAcquisitionUrl (string) --The location of the license key required to decrypt your HLS playlist. The URL must be an absolute path, and is referenced in the URI attribute of the EXT-X-KEY metadata tag in the playlist file.
            KeyStoragePolicy (string) --Specify whether you want Elastic Transcoder to write your HLS license key to an Amazon S3 bucket. If you choose WithVariantPlaylists , LicenseAcquisitionUrl must be left blank and Elastic Transcoder writes your data key into the same bucket as the associated playlist.
            PlayReadyDrm (dict) --The DRM settings, if any, that you want Elastic Transcoder to apply to the output files associated with this playlist.
            Format (string) --The type of DRM, if any, that you want Elastic Transcoder to apply to the output files associated with this playlist.
            Key (string) --The DRM key for your file, provided by your DRM license provider. The key must be base64-encoded, and it must be one of the following bit lengths before being base64-encoded:
            128 , 192 , or 256 .
            The key must also be encrypted by using AWS KMS.
            KeyMd5 (string) --The MD5 digest of the key used for DRM on your file, and that you want Elastic Transcoder to use as a checksum to make sure your key was not corrupted in transit. The key MD5 must be base64-encoded, and it must be exactly 16 bytes before being base64-encoded.
            KeyId (string) --The ID for your DRM key, so that your DRM license provider knows which key to provide.
            The key ID must be provided in big endian, and Elastic Transcoder converts it to little endian before inserting it into the PlayReady DRM headers. If you are unsure whether your license server provides your key ID in big or little endian, check with your DRM provider.
            InitializationVector (string) --The series of random bits created by a random bit generator, unique for every encryption operation, that you want Elastic Transcoder to use to encrypt your files. The initialization vector must be base64-encoded, and it must be exactly 8 bytes long before being base64-encoded. If no initialization vector is provided, Elastic Transcoder generates one for you.
            LicenseAcquisitionUrl (string) --The location of the license key required to play DRM content. The URL must be an absolute path, and is referenced by the PlayReady header. The PlayReady header is referenced in the protection header of the client manifest for Smooth Streaming outputs, and in the EXT-X-DXDRM and EXT-XDXDRMINFO metadata tags for HLS playlist outputs. An example URL looks like this: https://www.example.com/exampleKey/
            
            

    :type UserMetadata: dict
    :param UserMetadata: User-defined metadata that you want to associate with an Elastic Transcoder job. You specify metadata in key/value pairs, and you can add up to 10 key/value pairs per job. Elastic Transcoder does not guarantee that key/value pairs are returned in the same order in which you specify them.
            (string) --
            (string) --
            

    :rtype: dict
    :return: {
        'Job': {
            'Id': 'string',
            'Arn': 'string',
            'PipelineId': 'string',
            'Input': {
                'Key': 'string',
                'FrameRate': 'string',
                'Resolution': 'string',
                'AspectRatio': 'string',
                'Interlaced': 'string',
                'Container': 'string',
                'Encryption': {
                    'Mode': 'string',
                    'Key': 'string',
                    'KeyMd5': 'string',
                    'InitializationVector': 'string'
                },
                'TimeSpan': {
                    'StartTime': 'string',
                    'Duration': 'string'
                },
                'InputCaptions': {
                    'MergePolicy': 'string',
                    'CaptionSources': [
                        {
                            'Key': 'string',
                            'Language': 'string',
                            'TimeOffset': 'string',
                            'Label': 'string',
                            'Encryption': {
                                'Mode': 'string',
                                'Key': 'string',
                                'KeyMd5': 'string',
                                'InitializationVector': 'string'
                            }
                        },
                    ]
                },
                'DetectedProperties': {
                    'Width': 123,
                    'Height': 123,
                    'FrameRate': 'string',
                    'FileSize': 123,
                    'DurationMillis': 123
                }
            },
            'Inputs': [
                {
                    'Key': 'string',
                    'FrameRate': 'string',
                    'Resolution': 'string',
                    'AspectRatio': 'string',
                    'Interlaced': 'string',
                    'Container': 'string',
                    'Encryption': {
                        'Mode': 'string',
                        'Key': 'string',
                        'KeyMd5': 'string',
                        'InitializationVector': 'string'
                    },
                    'TimeSpan': {
                        'StartTime': 'string',
                        'Duration': 'string'
                    },
                    'InputCaptions': {
                        'MergePolicy': 'string',
                        'CaptionSources': [
                            {
                                'Key': 'string',
                                'Language': 'string',
                                'TimeOffset': 'string',
                                'Label': 'string',
                                'Encryption': {
                                    'Mode': 'string',
                                    'Key': 'string',
                                    'KeyMd5': 'string',
                                    'InitializationVector': 'string'
                                }
                            },
                        ]
                    },
                    'DetectedProperties': {
                        'Width': 123,
                        'Height': 123,
                        'FrameRate': 'string',
                        'FileSize': 123,
                        'DurationMillis': 123
                    }
                },
            ],
            'Output': {
                'Id': 'string',
                'Key': 'string',
                'ThumbnailPattern': 'string',
                'ThumbnailEncryption': {
                    'Mode': 'string',
                    'Key': 'string',
                    'KeyMd5': 'string',
                    'InitializationVector': 'string'
                },
                'Rotate': 'string',
                'PresetId': 'string',
                'SegmentDuration': 'string',
                'Status': 'string',
                'StatusDetail': 'string',
                'Duration': 123,
                'Width': 123,
                'Height': 123,
                'FrameRate': 'string',
                'FileSize': 123,
                'DurationMillis': 123,
                'Watermarks': [
                    {
                        'PresetWatermarkId': 'string',
                        'InputKey': 'string',
                        'Encryption': {
                            'Mode': 'string',
                            'Key': 'string',
                            'KeyMd5': 'string',
                            'InitializationVector': 'string'
                        }
                    },
                ],
                'AlbumArt': {
                    'MergePolicy': 'string',
                    'Artwork': [
                        {
                            'InputKey': 'string',
                            'MaxWidth': 'string',
                            'MaxHeight': 'string',
                            'SizingPolicy': 'string',
                            'PaddingPolicy': 'string',
                            'AlbumArtFormat': 'string',
                            'Encryption': {
                                'Mode': 'string',
                                'Key': 'string',
                                'KeyMd5': 'string',
                                'InitializationVector': 'string'
                            }
                        },
                    ]
                },
                'Composition': [
                    {
                        'TimeSpan': {
                            'StartTime': 'string',
                            'Duration': 'string'
                        }
                    },
                ],
                'Captions': {
                    'MergePolicy': 'string',
                    'CaptionSources': [
                        {
                            'Key': 'string',
                            'Language': 'string',
                            'TimeOffset': 'string',
                            'Label': 'string',
                            'Encryption': {
                                'Mode': 'string',
                                'Key': 'string',
                                'KeyMd5': 'string',
                                'InitializationVector': 'string'
                            }
                        },
                    ],
                    'CaptionFormats': [
                        {
                            'Format': 'string',
                            'Pattern': 'string',
                            'Encryption': {
                                'Mode': 'string',
                                'Key': 'string',
                                'KeyMd5': 'string',
                                'InitializationVector': 'string'
                            }
                        },
                    ]
                },
                'Encryption': {
                    'Mode': 'string',
                    'Key': 'string',
                    'KeyMd5': 'string',
                    'InitializationVector': 'string'
                },
                'AppliedColorSpaceConversion': 'string'
            },
            'Outputs': [
                {
                    'Id': 'string',
                    'Key': 'string',
                    'ThumbnailPattern': 'string',
                    'ThumbnailEncryption': {
                        'Mode': 'string',
                        'Key': 'string',
                        'KeyMd5': 'string',
                        'InitializationVector': 'string'
                    },
                    'Rotate': 'string',
                    'PresetId': 'string',
                    'SegmentDuration': 'string',
                    'Status': 'string',
                    'StatusDetail': 'string',
                    'Duration': 123,
                    'Width': 123,
                    'Height': 123,
                    'FrameRate': 'string',
                    'FileSize': 123,
                    'DurationMillis': 123,
                    'Watermarks': [
                        {
                            'PresetWatermarkId': 'string',
                            'InputKey': 'string',
                            'Encryption': {
                                'Mode': 'string',
                                'Key': 'string',
                                'KeyMd5': 'string',
                                'InitializationVector': 'string'
                            }
                        },
                    ],
                    'AlbumArt': {
                        'MergePolicy': 'string',
                        'Artwork': [
                            {
                                'InputKey': 'string',
                                'MaxWidth': 'string',
                                'MaxHeight': 'string',
                                'SizingPolicy': 'string',
                                'PaddingPolicy': 'string',
                                'AlbumArtFormat': 'string',
                                'Encryption': {
                                    'Mode': 'string',
                                    'Key': 'string',
                                    'KeyMd5': 'string',
                                    'InitializationVector': 'string'
                                }
                            },
                        ]
                    },
                    'Composition': [
                        {
                            'TimeSpan': {
                                'StartTime': 'string',
                                'Duration': 'string'
                            }
                        },
                    ],
                    'Captions': {
                        'MergePolicy': 'string',
                        'CaptionSources': [
                            {
                                'Key': 'string',
                                'Language': 'string',
                                'TimeOffset': 'string',
                                'Label': 'string',
                                'Encryption': {
                                    'Mode': 'string',
                                    'Key': 'string',
                                    'KeyMd5': 'string',
                                    'InitializationVector': 'string'
                                }
                            },
                        ],
                        'CaptionFormats': [
                            {
                                'Format': 'string',
                                'Pattern': 'string',
                                'Encryption': {
                                    'Mode': 'string',
                                    'Key': 'string',
                                    'KeyMd5': 'string',
                                    'InitializationVector': 'string'
                                }
                            },
                        ]
                    },
                    'Encryption': {
                        'Mode': 'string',
                        'Key': 'string',
                        'KeyMd5': 'string',
                        'InitializationVector': 'string'
                    },
                    'AppliedColorSpaceConversion': 'string'
                },
            ],
            'OutputKeyPrefix': 'string',
            'Playlists': [
                {
                    'Name': 'string',
                    'Format': 'string',
                    'OutputKeys': [
                        'string',
                    ],
                    'HlsContentProtection': {
                        'Method': 'string',
                        'Key': 'string',
                        'KeyMd5': 'string',
                        'InitializationVector': 'string',
                        'LicenseAcquisitionUrl': 'string',
                        'KeyStoragePolicy': 'string'
                    },
                    'PlayReadyDrm': {
                        'Format': 'string',
                        'Key': 'string',
                        'KeyMd5': 'string',
                        'KeyId': 'string',
                        'InitializationVector': 'string',
                        'LicenseAcquisitionUrl': 'string'
                    },
                    'Status': 'string',
                    'StatusDetail': 'string'
                },
            ],
            'Status': 'string',
            'UserMetadata': {
                'string': 'string'
            },
            'Timing': {
                'SubmitTimeMillis': 123,
                'StartTimeMillis': 123,
                'FinishTimeMillis': 123
            }
        }
    }
    
    
    :returns: 
    S3: Amazon S3 creates and manages the keys used for encrypting your files.
    S3-AWS-KMS: Amazon S3 calls the Amazon Key Management Service, which creates and manages the keys that are used for encrypting your files. If you specify S3-AWS-KMS and you don't want to use the default key, you must add the AWS-KMS key that you want to use to your pipeline.
    AES-CBC-PKCS7: A padded cipher-block mode of operation originally used for HLS files.
    AES-CTR: AES Counter Mode.
    AES-GCM: AES Galois Counter Mode, a mode of operation that is an authenticated encryption format, meaning that a file, key, or initialization vector that has been tampered with fails the decryption process.
    
    """
    pass

def create_pipeline(Name=None, InputBucket=None, OutputBucket=None, Role=None, AwsKmsKeyArn=None, Notifications=None, ContentConfig=None, ThumbnailConfig=None):
    """
    The CreatePipeline operation creates a pipeline with settings that you specify.
    See also: AWS API Documentation
    
    
    :example: response = client.create_pipeline(
        Name='string',
        InputBucket='string',
        OutputBucket='string',
        Role='string',
        AwsKmsKeyArn='string',
        Notifications={
            'Progressing': 'string',
            'Completed': 'string',
            'Warning': 'string',
            'Error': 'string'
        },
        ContentConfig={
            'Bucket': 'string',
            'StorageClass': 'string',
            'Permissions': [
                {
                    'GranteeType': 'string',
                    'Grantee': 'string',
                    'Access': [
                        'string',
                    ]
                },
            ]
        },
        ThumbnailConfig={
            'Bucket': 'string',
            'StorageClass': 'string',
            'Permissions': [
                {
                    'GranteeType': 'string',
                    'Grantee': 'string',
                    'Access': [
                        'string',
                    ]
                },
            ]
        }
    )
    
    
    :type Name: string
    :param Name: [REQUIRED]
            The name of the pipeline. We recommend that the name be unique within the AWS account, but uniqueness is not enforced.
            Constraints: Maximum 40 characters.
            

    :type InputBucket: string
    :param InputBucket: [REQUIRED]
            The Amazon S3 bucket in which you saved the media files that you want to transcode.
            

    :type OutputBucket: string
    :param OutputBucket: The Amazon S3 bucket in which you want Elastic Transcoder to save the transcoded files. (Use this, or use ContentConfig:Bucket plus ThumbnailConfig:Bucket.)
            Specify this value when all of the following are true:
            You want to save transcoded files, thumbnails (if any), and playlists (if any) together in one bucket.
            You do not want to specify the users or groups who have access to the transcoded files, thumbnails, and playlists.
            You do not want to specify the permissions that Elastic Transcoder grants to the files.
            Warning
            When Elastic Transcoder saves files in OutputBucket , it grants full control over the files only to the AWS account that owns the role that is specified by Role .
            You want to associate the transcoded files and thumbnails with the Amazon S3 Standard storage class.
            If you want to save transcoded files and playlists in one bucket and thumbnails in another bucket, specify which users can access the transcoded files or the permissions the users have, or change the Amazon S3 storage class, omit OutputBucket and specify values for ContentConfig and ThumbnailConfig instead.
            

    :type Role: string
    :param Role: [REQUIRED]
            The IAM Amazon Resource Name (ARN) for the role that you want Elastic Transcoder to use to create the pipeline.
            

    :type AwsKmsKeyArn: string
    :param AwsKmsKeyArn: The AWS Key Management Service (AWS KMS) key that you want to use with this pipeline.
            If you use either S3 or S3-AWS-KMS as your Encryption:Mode , you don't need to provide a key with your job because a default key, known as an AWS-KMS key, is created for you automatically. You need to provide an AWS-KMS key only if you want to use a non-default AWS-KMS key, or if you are using an Encryption:Mode of AES-PKCS7 , AES-CTR , or AES-GCM .
            

    :type Notifications: dict
    :param Notifications: The Amazon Simple Notification Service (Amazon SNS) topic that you want to notify to report job status.
            Warning
            To receive notifications, you must also subscribe to the new topic in the Amazon SNS console.
            Progressing : The topic ARN for the Amazon Simple Notification Service (Amazon SNS) topic that you want to notify when Elastic Transcoder has started to process a job in this pipeline. This is the ARN that Amazon SNS returned when you created the topic. For more information, see Create a Topic in the Amazon Simple Notification Service Developer Guide.
            Completed : The topic ARN for the Amazon SNS topic that you want to notify when Elastic Transcoder has finished processing a job in this pipeline. This is the ARN that Amazon SNS returned when you created the topic.
            Warning : The topic ARN for the Amazon SNS topic that you want to notify when Elastic Transcoder encounters a warning condition while processing a job in this pipeline. This is the ARN that Amazon SNS returned when you created the topic.
            Error : The topic ARN for the Amazon SNS topic that you want to notify when Elastic Transcoder encounters an error condition while processing a job in this pipeline. This is the ARN that Amazon SNS returned when you created the topic.
            Progressing (string) --The Amazon Simple Notification Service (Amazon SNS) topic that you want to notify when Elastic Transcoder has started to process the job.
            Completed (string) --The Amazon SNS topic that you want to notify when Elastic Transcoder has finished processing the job.
            Warning (string) --The Amazon SNS topic that you want to notify when Elastic Transcoder encounters a warning condition.
            Error (string) --The Amazon SNS topic that you want to notify when Elastic Transcoder encounters an error condition.
            

    :type ContentConfig: dict
    :param ContentConfig: The optional ContentConfig object specifies information about the Amazon S3 bucket in which you want Elastic Transcoder to save transcoded files and playlists: which bucket to use, which users you want to have access to the files, the type of access you want users to have, and the storage class that you want to assign to the files.
            If you specify values for ContentConfig , you must also specify values for ThumbnailConfig .
            If you specify values for ContentConfig and ThumbnailConfig , omit the OutputBucket object.
            Bucket : The Amazon S3 bucket in which you want Elastic Transcoder to save transcoded files and playlists.
            Permissions (Optional): The Permissions object specifies which users you want to have access to transcoded files and the type of access you want them to have. You can grant permissions to a maximum of 30 users and/or predefined Amazon S3 groups.
            Grantee Type : Specify the type of value that appears in the Grantee object:
            Canonical : The value in the Grantee object is either the canonical user ID for an AWS account or an origin access identity for an Amazon CloudFront distribution. For more information about canonical user IDs, see Access Control List (ACL) Overview in the Amazon Simple Storage Service Developer Guide. For more information about using CloudFront origin access identities to require that users use CloudFront URLs instead of Amazon S3 URLs, see Using an Origin Access Identity to Restrict Access to Your Amazon S3 Content.
            Warning
            A canonical user ID is not the same as an AWS account number.
            Email : The value in the Grantee object is the registered email address of an AWS account.
            Group : The value in the Grantee object is one of the following predefined Amazon S3 groups: AllUsers , AuthenticatedUsers , or LogDelivery .
            Grantee : The AWS user or group that you want to have access to transcoded files and playlists. To identify the user or group, you can specify the canonical user ID for an AWS account, an origin access identity for a CloudFront distribution, the registered email address of an AWS account, or a predefined Amazon S3 group
            Access : The permission that you want to give to the AWS user that you specified in Grantee . Permissions are granted on the files that Elastic Transcoder adds to the bucket, including playlists and video files. Valid values include:
            READ : The grantee can read the objects and metadata for objects that Elastic Transcoder adds to the Amazon S3 bucket.
            READ_ACP : The grantee can read the object ACL for objects that Elastic Transcoder adds to the Amazon S3 bucket.
            WRITE_ACP : The grantee can write the ACL for the objects that Elastic Transcoder adds to the Amazon S3 bucket.
            FULL_CONTROL : The grantee has READ , READ_ACP , and WRITE_ACP permissions for the objects that Elastic Transcoder adds to the Amazon S3 bucket.
            StorageClass : The Amazon S3 storage class, Standard or ReducedRedundancy , that you want Elastic Transcoder to assign to the video files and playlists that it stores in your Amazon S3 bucket.
            Bucket (string) --The Amazon S3 bucket in which you want Elastic Transcoder to save the transcoded files. Specify this value when all of the following are true:
            You want to save transcoded files, thumbnails (if any), and playlists (if any) together in one bucket.
            You do not want to specify the users or groups who have access to the transcoded files, thumbnails, and playlists.
            You do not want to specify the permissions that Elastic Transcoder grants to the files.
            You want to associate the transcoded files and thumbnails with the Amazon S3 Standard storage class.
            If you want to save transcoded files and playlists in one bucket and thumbnails in another bucket, specify which users can access the transcoded files or the permissions the users have, or change the Amazon S3 storage class, omit OutputBucket and specify values for ContentConfig and ThumbnailConfig instead.
            StorageClass (string) --The Amazon S3 storage class, Standard or ReducedRedundancy , that you want Elastic Transcoder to assign to the video files and playlists that it stores in your Amazon S3 bucket.
            Permissions (list) --Optional. The Permissions object specifies which users and/or predefined Amazon S3 groups you want to have access to transcoded files and playlists, and the type of access you want them to have. You can grant permissions to a maximum of 30 users and/or predefined Amazon S3 groups.
            If you include Permissions , Elastic Transcoder grants only the permissions that you specify. It does not grant full permissions to the owner of the role specified by Role . If you want that user to have full control, you must explicitly grant full control to the user.
            If you omit Permissions , Elastic Transcoder grants full control over the transcoded files and playlists to the owner of the role specified by Role , and grants no other permissions to any other user or group.
            (dict) --The Permission structure.
            GranteeType (string) --The type of value that appears in the Grantee object:
            Canonical : Either the canonical user ID for an AWS account or an origin access identity for an Amazon CloudFront distribution.
            Warning
            A canonical user ID is not the same as an AWS account number.
            Email : The registered email address of an AWS account.
            Group : One of the following predefined Amazon S3 groups: AllUsers , AuthenticatedUsers , or LogDelivery .
            Grantee (string) --The AWS user or group that you want to have access to transcoded files and playlists. To identify the user or group, you can specify the canonical user ID for an AWS account, an origin access identity for a CloudFront distribution, the registered email address of an AWS account, or a predefined Amazon S3 group.
            Access (list) --The permission that you want to give to the AWS user that is listed in Grantee. Valid values include:
            READ : The grantee can read the thumbnails and metadata for thumbnails that Elastic Transcoder adds to the Amazon S3 bucket.
            READ_ACP : The grantee can read the object ACL for thumbnails that Elastic Transcoder adds to the Amazon S3 bucket.
            WRITE_ACP : The grantee can write the ACL for the thumbnails that Elastic Transcoder adds to the Amazon S3 bucket.
            FULL_CONTROL : The grantee has READ, READ_ACP, and WRITE_ACP permissions for the thumbnails that Elastic Transcoder adds to the Amazon S3 bucket.
            (string) --
            
            

    :type ThumbnailConfig: dict
    :param ThumbnailConfig: The ThumbnailConfig object specifies several values, including the Amazon S3 bucket in which you want Elastic Transcoder to save thumbnail files, which users you want to have access to the files, the type of access you want users to have, and the storage class that you want to assign to the files.
            If you specify values for ContentConfig , you must also specify values for ThumbnailConfig even if you don't want to create thumbnails.
            If you specify values for ContentConfig and ThumbnailConfig , omit the OutputBucket object.
            Bucket : The Amazon S3 bucket in which you want Elastic Transcoder to save thumbnail files.
            Permissions (Optional): The Permissions object specifies which users and/or predefined Amazon S3 groups you want to have access to thumbnail files, and the type of access you want them to have. You can grant permissions to a maximum of 30 users and/or predefined Amazon S3 groups.
            GranteeType : Specify the type of value that appears in the Grantee object:
            Canonical : The value in the Grantee object is either the canonical user ID for an AWS account or an origin access identity for an Amazon CloudFront distribution.
            Warning
            A canonical user ID is not the same as an AWS account number.
            Email : The value in the Grantee object is the registered email address of an AWS account.
            Group : The value in the Grantee object is one of the following predefined Amazon S3 groups: AllUsers , AuthenticatedUsers , or LogDelivery .
            Grantee : The AWS user or group that you want to have access to thumbnail files. To identify the user or group, you can specify the canonical user ID for an AWS account, an origin access identity for a CloudFront distribution, the registered email address of an AWS account, or a predefined Amazon S3 group.
            Access : The permission that you want to give to the AWS user that you specified in Grantee . Permissions are granted on the thumbnail files that Elastic Transcoder adds to the bucket. Valid values include:
            READ : The grantee can read the thumbnails and metadata for objects that Elastic Transcoder adds to the Amazon S3 bucket.
            READ_ACP : The grantee can read the object ACL for thumbnails that Elastic Transcoder adds to the Amazon S3 bucket.
            WRITE_ACP : The grantee can write the ACL for the thumbnails that Elastic Transcoder adds to the Amazon S3 bucket.
            FULL_CONTROL : The grantee has READ , READ_ACP , and WRITE_ACP permissions for the thumbnails that Elastic Transcoder adds to the Amazon S3 bucket.
            StorageClass : The Amazon S3 storage class, Standard or ReducedRedundancy , that you want Elastic Transcoder to assign to the thumbnails that it stores in your Amazon S3 bucket.
            Bucket (string) --The Amazon S3 bucket in which you want Elastic Transcoder to save the transcoded files. Specify this value when all of the following are true:
            You want to save transcoded files, thumbnails (if any), and playlists (if any) together in one bucket.
            You do not want to specify the users or groups who have access to the transcoded files, thumbnails, and playlists.
            You do not want to specify the permissions that Elastic Transcoder grants to the files.
            You want to associate the transcoded files and thumbnails with the Amazon S3 Standard storage class.
            If you want to save transcoded files and playlists in one bucket and thumbnails in another bucket, specify which users can access the transcoded files or the permissions the users have, or change the Amazon S3 storage class, omit OutputBucket and specify values for ContentConfig and ThumbnailConfig instead.
            StorageClass (string) --The Amazon S3 storage class, Standard or ReducedRedundancy , that you want Elastic Transcoder to assign to the video files and playlists that it stores in your Amazon S3 bucket.
            Permissions (list) --Optional. The Permissions object specifies which users and/or predefined Amazon S3 groups you want to have access to transcoded files and playlists, and the type of access you want them to have. You can grant permissions to a maximum of 30 users and/or predefined Amazon S3 groups.
            If you include Permissions , Elastic Transcoder grants only the permissions that you specify. It does not grant full permissions to the owner of the role specified by Role . If you want that user to have full control, you must explicitly grant full control to the user.
            If you omit Permissions , Elastic Transcoder grants full control over the transcoded files and playlists to the owner of the role specified by Role , and grants no other permissions to any other user or group.
            (dict) --The Permission structure.
            GranteeType (string) --The type of value that appears in the Grantee object:
            Canonical : Either the canonical user ID for an AWS account or an origin access identity for an Amazon CloudFront distribution.
            Warning
            A canonical user ID is not the same as an AWS account number.
            Email : The registered email address of an AWS account.
            Group : One of the following predefined Amazon S3 groups: AllUsers , AuthenticatedUsers , or LogDelivery .
            Grantee (string) --The AWS user or group that you want to have access to transcoded files and playlists. To identify the user or group, you can specify the canonical user ID for an AWS account, an origin access identity for a CloudFront distribution, the registered email address of an AWS account, or a predefined Amazon S3 group.
            Access (list) --The permission that you want to give to the AWS user that is listed in Grantee. Valid values include:
            READ : The grantee can read the thumbnails and metadata for thumbnails that Elastic Transcoder adds to the Amazon S3 bucket.
            READ_ACP : The grantee can read the object ACL for thumbnails that Elastic Transcoder adds to the Amazon S3 bucket.
            WRITE_ACP : The grantee can write the ACL for the thumbnails that Elastic Transcoder adds to the Amazon S3 bucket.
            FULL_CONTROL : The grantee has READ, READ_ACP, and WRITE_ACP permissions for the thumbnails that Elastic Transcoder adds to the Amazon S3 bucket.
            (string) --
            
            

    :rtype: dict
    :return: {
        'Pipeline': {
            'Id': 'string',
            'Arn': 'string',
            'Name': 'string',
            'Status': 'string',
            'InputBucket': 'string',
            'OutputBucket': 'string',
            'Role': 'string',
            'AwsKmsKeyArn': 'string',
            'Notifications': {
                'Progressing': 'string',
                'Completed': 'string',
                'Warning': 'string',
                'Error': 'string'
            },
            'ContentConfig': {
                'Bucket': 'string',
                'StorageClass': 'string',
                'Permissions': [
                    {
                        'GranteeType': 'string',
                        'Grantee': 'string',
                        'Access': [
                            'string',
                        ]
                    },
                ]
            },
            'ThumbnailConfig': {
                'Bucket': 'string',
                'StorageClass': 'string',
                'Permissions': [
                    {
                        'GranteeType': 'string',
                        'Grantee': 'string',
                        'Access': [
                            'string',
                        ]
                    },
                ]
            }
        },
        'Warnings': [
            {
                'Code': 'string',
                'Message': 'string'
            },
        ]
    }
    
    
    :returns: 
    Active : The pipeline is processing jobs.
    Paused : The pipeline is not currently processing jobs.
    
    """
    pass

def create_preset(Name=None, Description=None, Container=None, Video=None, Audio=None, Thumbnails=None):
    """
    The CreatePreset operation creates a preset with settings that you specify.
    Elastic Transcoder uses the H.264 video-compression format. For more information, see the International Telecommunication Union publication Recommendation ITU-T H.264: Advanced video coding for generic audiovisual services .
    See also: AWS API Documentation
    
    
    :example: response = client.create_preset(
        Name='string',
        Description='string',
        Container='string',
        Video={
            'Codec': 'string',
            'CodecOptions': {
                'string': 'string'
            },
            'KeyframesMaxDist': 'string',
            'FixedGOP': 'string',
            'BitRate': 'string',
            'FrameRate': 'string',
            'MaxFrameRate': 'string',
            'Resolution': 'string',
            'AspectRatio': 'string',
            'MaxWidth': 'string',
            'MaxHeight': 'string',
            'DisplayAspectRatio': 'string',
            'SizingPolicy': 'string',
            'PaddingPolicy': 'string',
            'Watermarks': [
                {
                    'Id': 'string',
                    'MaxWidth': 'string',
                    'MaxHeight': 'string',
                    'SizingPolicy': 'string',
                    'HorizontalAlign': 'string',
                    'HorizontalOffset': 'string',
                    'VerticalAlign': 'string',
                    'VerticalOffset': 'string',
                    'Opacity': 'string',
                    'Target': 'string'
                },
            ]
        },
        Audio={
            'Codec': 'string',
            'SampleRate': 'string',
            'BitRate': 'string',
            'Channels': 'string',
            'AudioPackingMode': 'string',
            'CodecOptions': {
                'Profile': 'string',
                'BitDepth': 'string',
                'BitOrder': 'string',
                'Signed': 'string'
            }
        },
        Thumbnails={
            'Format': 'string',
            'Interval': 'string',
            'Resolution': 'string',
            'AspectRatio': 'string',
            'MaxWidth': 'string',
            'MaxHeight': 'string',
            'SizingPolicy': 'string',
            'PaddingPolicy': 'string'
        }
    )
    
    
    :type Name: string
    :param Name: [REQUIRED]
            The name of the preset. We recommend that the name be unique within the AWS account, but uniqueness is not enforced.
            

    :type Description: string
    :param Description: A description of the preset.

    :type Container: string
    :param Container: [REQUIRED]
            The container type for the output file. Valid values include flac , flv , fmp4 , gif , mp3 , mp4 , mpg , mxf , oga , ogg , ts , and webm .
            

    :type Video: dict
    :param Video: A section of the request body that specifies the video parameters.
            Codec (string) --The video codec for the output file. Valid values include gif , H.264 , mpeg2 , vp8 , and vp9 . You can only specify vp8 and vp9 when the container type is webm , gif when the container type is gif , and mpeg2 when the container type is mpg .
            CodecOptions (dict) --
            Profile (H.264/VP8/VP9 Only)
            The H.264 profile that you want to use for the output file. Elastic Transcoder supports the following profiles:
            baseline : The profile most commonly used for videoconferencing and for mobile applications.
            main : The profile used for standard-definition digital TV broadcasts.
            high : The profile used for high-definition digital TV broadcasts and for Blu-ray discs.
            Level (H.264 Only)
            The H.264 level that you want to use for the output file. Elastic Transcoder supports the following levels:
            1 , 1b , 1.1 , 1.2 , 1.3 , 2 , 2.1 , 2.2 , 3 , 3.1 , 3.2 , 4 , 4.1MaxReferenceFrames (H.264 Only)
            Applicable only when the value of Video:Codec is H.264. The maximum number of previously decoded frames to use as a reference for decoding future frames. Valid values are integers 0 through 16, but we recommend that you not use a value greater than the following:
            Min(Floor(Maximum decoded picture buffer in macroblocks * 256 / (Width in pixels * Height in pixels)), 16)
            where Width in pixels and Height in pixels represent either MaxWidth and MaxHeight, or Resolution. Maximum decoded picture buffer in macroblocks depends on the value of the Level object. See the list below. (A macroblock is a block of pixels measuring 16x16.)
            1 - 396
            1b - 396
            1.1 - 900
            1.2 - 2376
            1.3 - 2376
            2 - 2376
            2.1 - 4752
            2.2 - 8100
            3 - 8100
            3.1 - 18000
            3.2 - 20480
            4 - 32768
            4.1 - 32768
            MaxBitRate (Optional, H.264/MPEG2/VP8/VP9 only)
            The maximum number of bits per second in a video buffer; the size of the buffer is specified by BufferSize . Specify a value between 16 and 62,500. You can reduce the bandwidth required to stream a video by reducing the maximum bit rate, but this also reduces the quality of the video.
            BufferSize (Optional, H.264/MPEG2/VP8/VP9 only)
            The maximum number of bits in any x seconds of the output video. This window is commonly 10 seconds, the standard segment duration when you're using FMP4 or MPEG-TS for the container type of the output video. Specify an integer greater than 0. If you specify MaxBitRate and omit BufferSize , Elastic Transcoder sets BufferSize to 10 times the value of MaxBitRate .
            InterlacedMode (Optional, H.264/MPEG2 Only)
            The interlace mode for the output video.
            Interlaced video is used to double the perceived frame rate for a video by interlacing two fields (one field on every other line, the other field on the other lines) so that the human eye registers multiple pictures per frame. Interlacing reduces the bandwidth required for transmitting a video, but can result in blurred images and flickering.
            Valid values include Progressive (no interlacing, top to bottom), TopFirst (top field first), BottomFirst (bottom field first), and Auto .
            If InterlaceMode is not specified, Elastic Transcoder uses Progressive for the output. If Auto is specified, Elastic Transcoder interlaces the output.
            ColorSpaceConversionMode (Optional, H.264/MPEG2 Only)
            The color space conversion Elastic Transcoder applies to the output video. Color spaces are the algorithms used by the computer to store information about how to render color. Bt.601 is the standard for standard definition video, while Bt.709 is the standard for high definition video.
            Valid values include None , Bt709toBt601 , Bt601toBt709 , and Auto .
            If you chose Auto for ColorSpaceConversionMode and your output is interlaced, your frame rate is one of 23.97 , 24 , 25 , 29.97 , 50 , or 60 , your SegmentDuration is null, and you are using one of the resolution changes from the list below, Elastic Transcoder applies the following color space conversions:
            Standard to HD, 720x480 to 1920x1080 - Elastic Transcoder applies Bt601ToBt709
            Standard to HD, 720x576 to 1920x1080 - Elastic Transcoder applies Bt601ToBt709
            HD to Standard, 1920x1080 to 720x480 - Elastic Transcoder applies Bt709ToBt601
            HD to Standard, 1920x1080 to 720x576 - Elastic Transcoder applies Bt709ToBt601
            Note
            Elastic Transcoder may change the behavior of the ColorspaceConversionMode Auto mode in the future. All outputs in a playlist must use the same ColorSpaceConversionMode .
            If you do not specify a ColorSpaceConversionMode , Elastic Transcoder does not change the color space of a file. If you are unsure what ColorSpaceConversionMode was applied to your output file, you can check the AppliedColorSpaceConversion parameter included in your job response. If your job does not have an AppliedColorSpaceConversion in its response, no ColorSpaceConversionMode was applied.
            ChromaSubsampling
            The sampling pattern for the chroma (color) channels of the output video. Valid values include yuv420p and yuv422p .
            yuv420p samples the chroma information of every other horizontal and every other vertical line, yuv422p samples the color information of every horizontal line and every other vertical line.LoopCount (Gif Only)
            The number of times you want the output gif to loop. Valid values include Infinite and integers between 0 and 100 , inclusive.
            (string) --
            (string) --
            
            KeyframesMaxDist (string) --Applicable only when the value of Video:Codec is one of H.264 , MPEG2 , or VP8 .
            The maximum number of frames between key frames. Key frames are fully encoded frames; the frames between key frames are encoded based, in part, on the content of the key frames. The value is an integer formatted as a string; valid values are between 1 (every frame is a key frame) and 100000, inclusive. A higher value results in higher compression but may also discernibly decrease video quality.
            For Smooth outputs, the FrameRate must have a constant ratio to the KeyframesMaxDist . This allows Smooth playlists to switch between different quality levels while the file is being played.
            For example, an input file can have a FrameRate of 30 with a KeyframesMaxDist of 90. The output file then needs to have a ratio of 1:3. Valid outputs would have FrameRate of 30, 25, and 10, and KeyframesMaxDist of 90, 75, and 30, respectively.
            Alternately, this can be achieved by setting FrameRate to auto and having the same values for MaxFrameRate and KeyframesMaxDist .
            FixedGOP (string) --Applicable only when the value of Video:Codec is one of H.264 , MPEG2 , or VP8 .
            Whether to use a fixed value for FixedGOP . Valid values are true and false :
            true : Elastic Transcoder uses the value of KeyframesMaxDist for the distance between key frames (the number of frames in a group of pictures, or GOP).
            false : The distance between key frames can vary.
            Warning
            FixedGOP must be set to true for fmp4 containers.
            BitRate (string) --The bit rate of the video stream in the output file, in kilobits/second. Valid values depend on the values of Level and Profile . If you specify auto , Elastic Transcoder uses the detected bit rate of the input source. If you specify a value other than auto , we recommend that you specify a value less than or equal to the maximum H.264-compliant value listed for your level and profile:
            Level - Maximum video bit rate in kilobits/second (baseline and main Profile) : maximum video bit rate in kilobits/second (high Profile)
            1 - 64 : 80
            1b - 128 : 160
            1.1 - 192 : 240
            1.2 - 384 : 480
            1.3 - 768 : 960
            2 - 2000 : 2500
            3 - 10000 : 12500
            3.1 - 14000 : 17500
            3.2 - 20000 : 25000
            4 - 20000 : 25000
            4.1 - 50000 : 62500
            FrameRate (string) --The frames per second for the video stream in the output file. Valid values include:
            auto , 10 , 15 , 23.97 , 24 , 25 , 29.97 , 30 , 60
            If you specify auto , Elastic Transcoder uses the detected frame rate of the input source. If you specify a frame rate, we recommend that you perform the following calculation:
            Frame rate = maximum recommended decoding speed in luma samples/second / (width in pixels * height in pixels)
            where:
            width in pixels and height in pixels represent the Resolution of the output video.
            maximum recommended decoding speed in Luma samples/second is less than or equal to the maximum value listed in the following table, based on the value that you specified for Level.
            The maximum recommended decoding speed in Luma samples/second for each level is described in the following list (Level - Decoding speed ):
            1 - 380160
            1b - 380160
            1.1 - 76800
            1.2 - 1536000
            1.3 - 3041280
            2 - 3041280
            2.1 - 5068800
            2.2 - 5184000
            3 - 10368000
            3.1 - 27648000
            3.2 - 55296000
            4 - 62914560
            4.1 - 62914560
            MaxFrameRate (string) --If you specify auto for FrameRate , Elastic Transcoder uses the frame rate of the input video for the frame rate of the output video. Specify the maximum frame rate that you want Elastic Transcoder to use when the frame rate of the input video is greater than the desired maximum frame rate of the output video. Valid values include: 10 , 15 , 23.97 , 24 , 25 , 29.97 , 30 , 60 .
            Resolution (string) --
            Warning
            To better control resolution and aspect ratio of output videos, we recommend that you use the values MaxWidth , MaxHeight , SizingPolicy , PaddingPolicy , and DisplayAspectRatio instead of Resolution and AspectRatio . The two groups of settings are mutually exclusive. Do not use them together.
            The width and height of the video in the output file, in pixels. Valid values are auto and width x height :
            auto : Elastic Transcoder attempts to preserve the width and height of the input file, subject to the following rules.
            ``width x height `` : The width and height of the output video in pixels.
            Note the following about specifying the width and height:
            The width must be an even integer between 128 and 4096, inclusive.
            The height must be an even integer between 96 and 3072, inclusive.
            If you specify a resolution that is less than the resolution of the input file, Elastic Transcoder rescales the output file to the lower resolution.
            If you specify a resolution that is greater than the resolution of the input file, Elastic Transcoder rescales the output to the higher resolution.
            We recommend that you specify a resolution for which the product of width and height is less than or equal to the applicable value in the following list (List - Max width x height value ):
            1 - 25344
            1b - 25344
            1.1 - 101376
            1.2 - 101376
            1.3 - 101376
            2 - 101376
            2.1 - 202752
            2.2 - 404720
            3 - 404720
            3.1 - 921600
            3.2 - 1310720
            4 - 2097152
            4.1 - 2097152
            
            AspectRatio (string) --
            Warning
            To better control resolution and aspect ratio of output videos, we recommend that you use the values MaxWidth , MaxHeight , SizingPolicy , PaddingPolicy , and DisplayAspectRatio instead of Resolution and AspectRatio . The two groups of settings are mutually exclusive. Do not use them together.
            The display aspect ratio of the video in the output file. Valid values include:
            auto , 1:1 , 4:3 , 3:2 , 16:9
            If you specify auto , Elastic Transcoder tries to preserve the aspect ratio of the input file.
            If you specify an aspect ratio for the output file that differs from aspect ratio of the input file, Elastic Transcoder adds pillarboxing (black bars on the sides) or letterboxing (black bars on the top and bottom) to maintain the aspect ratio of the active region of the video.
            MaxWidth (string) --The maximum width of the output video in pixels. If you specify auto , Elastic Transcoder uses 1920 (Full HD) as the default value. If you specify a numeric value, enter an even integer between 128 and 4096.
            MaxHeight (string) --The maximum height of the output video in pixels. If you specify auto , Elastic Transcoder uses 1080 (Full HD) as the default value. If you specify a numeric value, enter an even integer between 96 and 3072.
            DisplayAspectRatio (string) --The value that Elastic Transcoder adds to the metadata in the output file.
            SizingPolicy (string) --Specify one of the following values to control scaling of the output video:
            Fit : Elastic Transcoder scales the output video so it matches the value that you specified in either MaxWidth or MaxHeight without exceeding the other value.
            Fill : Elastic Transcoder scales the output video so it matches the value that you specified in either MaxWidth or MaxHeight and matches or exceeds the other value. Elastic Transcoder centers the output video and then crops it in the dimension (if any) that exceeds the maximum value.
            Stretch : Elastic Transcoder stretches the output video to match the values that you specified for MaxWidth and MaxHeight . If the relative proportions of the input video and the output video are different, the output video will be distorted.
            Keep : Elastic Transcoder does not scale the output video. If either dimension of the input video exceeds the values that you specified for MaxWidth and MaxHeight , Elastic Transcoder crops the output video.
            ShrinkToFit : Elastic Transcoder scales the output video down so that its dimensions match the values that you specified for at least one of MaxWidth and MaxHeight without exceeding either value. If you specify this option, Elastic Transcoder does not scale the video up.
            ShrinkToFill : Elastic Transcoder scales the output video down so that its dimensions match the values that you specified for at least one of MaxWidth and MaxHeight without dropping below either value. If you specify this option, Elastic Transcoder does not scale the video up.
            PaddingPolicy (string) --When you set PaddingPolicy to Pad , Elastic Transcoder may add black bars to the top and bottom and/or left and right sides of the output video to make the total size of the output video match the values that you specified for MaxWidth and MaxHeight .
            Watermarks (list) --Settings for the size, location, and opacity of graphics that you want Elastic Transcoder to overlay over videos that are transcoded using this preset. You can specify settings for up to four watermarks. Watermarks appear in the specified size and location, and with the specified opacity for the duration of the transcoded video.
            Watermarks can be in .png or .jpg format. If you want to display a watermark that is not rectangular, use the .png format, which supports transparency.
            When you create a job that uses this preset, you specify the .png or .jpg graphics that you want Elastic Transcoder to include in the transcoded videos. You can specify fewer graphics in the job than you specify watermark settings in the preset, which allows you to use the same preset for up to four watermarks that have different dimensions.
            (dict) --Settings for the size, location, and opacity of graphics that you want Elastic Transcoder to overlay over videos that are transcoded using this preset. You can specify settings for up to four watermarks. Watermarks appear in the specified size and location, and with the specified opacity for the duration of the transcoded video.
            Watermarks can be in .png or .jpg format. If you want to display a watermark that is not rectangular, use the .png format, which supports transparency.
            When you create a job that uses this preset, you specify the .png or .jpg graphics that you want Elastic Transcoder to include in the transcoded videos. You can specify fewer graphics in the job than you specify watermark settings in the preset, which allows you to use the same preset for up to four watermarks that have different dimensions.
            Id (string) --A unique identifier for the settings for one watermark. The value of Id can be up to 40 characters long.
            MaxWidth (string) --The maximum width of the watermark in one of the following formats:
            number of pixels (px): The minimum value is 16 pixels, and the maximum value is the value of MaxWidth .
            integer percentage (%): The range of valid values is 0 to 100. Use the value of Target to specify whether you want Elastic Transcoder to include the black bars that are added by Elastic Transcoder, if any, in the calculation. If you specify the value in pixels, it must be less than or equal to the value of MaxWidth .
            MaxHeight (string) --The maximum height of the watermark in one of the following formats:
            number of pixels (px): The minimum value is 16 pixels, and the maximum value is the value of MaxHeight .
            integer percentage (%): The range of valid values is 0 to 100. Use the value of Target to specify whether you want Elastic Transcoder to include the black bars that are added by Elastic Transcoder, if any, in the calculation.
            If you specify the value in pixels, it must be less than or equal to the value of MaxHeight .
            SizingPolicy (string) --A value that controls scaling of the watermark:
            Fit : Elastic Transcoder scales the watermark so it matches the value that you specified in either MaxWidth or MaxHeight without exceeding the other value.
            Stretch : Elastic Transcoder stretches the watermark to match the values that you specified for MaxWidth and MaxHeight . If the relative proportions of the watermark and the values of MaxWidth and MaxHeight are different, the watermark will be distorted.
            ShrinkToFit : Elastic Transcoder scales the watermark down so that its dimensions match the values that you specified for at least one of MaxWidth and MaxHeight without exceeding either value. If you specify this option, Elastic Transcoder does not scale the watermark up.
            HorizontalAlign (string) --The horizontal position of the watermark unless you specify a non-zero value for HorizontalOffset :
            Left : The left edge of the watermark is aligned with the left border of the video.
            Right : The right edge of the watermark is aligned with the right border of the video.
            Center : The watermark is centered between the left and right borders.
            HorizontalOffset (string) --The amount by which you want the horizontal position of the watermark to be offset from the position specified by HorizontalAlign:
            number of pixels (px): The minimum value is 0 pixels, and the maximum value is the value of MaxWidth.
            integer percentage (%): The range of valid values is 0 to 100.
            For example, if you specify Left for HorizontalAlign and 5px for HorizontalOffset , the left side of the watermark appears 5 pixels from the left border of the output video.
            HorizontalOffset is only valid when the value of HorizontalAlign is Left or Right . If you specify an offset that causes the watermark to extend beyond the left or right border and Elastic Transcoder has not added black bars, the watermark is cropped. If Elastic Transcoder has added black bars, the watermark extends into the black bars. If the watermark extends beyond the black bars, it is cropped.
            Use the value of Target to specify whether you want to include the black bars that are added by Elastic Transcoder, if any, in the offset calculation.
            VerticalAlign (string) --The vertical position of the watermark unless you specify a non-zero value for VerticalOffset :
            Top : The top edge of the watermark is aligned with the top border of the video.
            Bottom : The bottom edge of the watermark is aligned with the bottom border of the video.
            Center : The watermark is centered between the top and bottom borders.
            VerticalOffset (string) --
            VerticalOffset
            The amount by which you want the vertical position of the watermark to be offset from the position specified by VerticalAlign:
            number of pixels (px): The minimum value is 0 pixels, and the maximum value is the value of MaxHeight .
            integer percentage (%): The range of valid values is 0 to 100.
            For example, if you specify Top for VerticalAlign and 5px for VerticalOffset , the top of the watermark appears 5 pixels from the top border of the output video.
            VerticalOffset is only valid when the value of VerticalAlign is Top or Bottom.
            If you specify an offset that causes the watermark to extend beyond the top or bottom border and Elastic Transcoder has not added black bars, the watermark is cropped. If Elastic Transcoder has added black bars, the watermark extends into the black bars. If the watermark extends beyond the black bars, it is cropped.
            Use the value of Target to specify whether you want Elastic Transcoder to include the black bars that are added by Elastic Transcoder, if any, in the offset calculation.
            Opacity (string) --A percentage that indicates how much you want a watermark to obscure the video in the location where it appears. Valid values are 0 (the watermark is invisible) to 100 (the watermark completely obscures the video in the specified location). The datatype of Opacity is float.
            Elastic Transcoder supports transparent .png graphics. If you use a transparent .png, the transparent portion of the video appears as if you had specified a value of 0 for Opacity . The .jpg file format doesn't support transparency.
            Target (string) --A value that determines how Elastic Transcoder interprets values that you specified for HorizontalOffset , VerticalOffset , MaxWidth , and MaxHeight :
            Content : HorizontalOffset and VerticalOffset values are calculated based on the borders of the video excluding black bars added by Elastic Transcoder, if any. In addition, MaxWidth and MaxHeight , if specified as a percentage, are calculated based on the borders of the video excluding black bars added by Elastic Transcoder, if any.
            Frame : HorizontalOffset and VerticalOffset values are calculated based on the borders of the video including black bars added by Elastic Transcoder, if any. In addition, MaxWidth and MaxHeight , if specified as a percentage, are calculated based on the borders of the video including black bars added by Elastic Transcoder, if any.
            
            

    :type Audio: dict
    :param Audio: A section of the request body that specifies the audio parameters.
            Codec (string) --The audio codec for the output file. Valid values include aac , flac , mp2 , mp3 , pcm , and vorbis .
            SampleRate (string) --The sample rate of the audio stream in the output file, in Hertz. Valid values include:
            auto , 22050 , 32000 , 44100 , 48000 , 96000
            If you specify auto , Elastic Transcoder automatically detects the sample rate.
            BitRate (string) --The bit rate of the audio stream in the output file, in kilobits/second. Enter an integer between 64 and 320, inclusive.
            Channels (string) --The number of audio channels in the output file. The following values are valid:
            auto , 0 , 1 , 2
            One channel carries the information played by a single speaker. For example, a stereo track with two channels sends one channel to the left speaker, and the other channel to the right speaker. The output channels are organized into tracks. If you want Elastic Transcoder to automatically detect the number of audio channels in the input file and use that value for the output file, select auto .
            The output of a specific channel value and inputs are as follows:
            auto channel specified, with any input: Pass through up to eight input channels.
            0 channels specified, with any input: Audio omitted from the output.
            1 channel specified, with at least one input channel: Mono sound.
            2 channels specified, with any input: Two identical mono channels or stereo. For more information about tracks, see Audio:AudioPackingMode.
            For more information about how Elastic Transcoder organizes channels and tracks, see Audio:AudioPackingMode .
            AudioPackingMode (string) --The method of organizing audio channels and tracks. Use Audio:Channels to specify the number of channels in your output, and Audio:AudioPackingMode to specify the number of tracks and their relation to the channels. If you do not specify an Audio:AudioPackingMode , Elastic Transcoder uses SingleTrack .
            The following values are valid:
            SingleTrack , OneChannelPerTrack , and OneChannelPerTrackWithMosTo8Tracks
            When you specify SingleTrack , Elastic Transcoder creates a single track for your output. The track can have up to eight channels. Use SingleTrack for all non-mxf containers.
            The outputs of SingleTrack for a specific channel value and inputs are as follows:
            0 channels with any input: Audio omitted from the output
            1, 2, or auto channels with no audio input: Audio omitted from the output
            1 channel with any input with audio: One track with one channel, downmixed if necessary
            2 channels with one track with one channel: One track with two identical channels
            2 or auto channels with two tracks with one channel each: One track with two channels
            2 or auto channels with one track with two channels: One track with two channels
            2 channels with one track with multiple channels: One track with two channels
            auto channels with one track with one channel: One track with one channel
            auto channels with one track with multiple channels: One track with multiple channels
            When you specify OneChannelPerTrack , Elastic Transcoder creates a new track for every channel in your output. Your output can have up to eight single-channel tracks.
            The outputs of OneChannelPerTrack for a specific channel value and inputs are as follows:
            0 channels with any input: Audio omitted from the output
            1, 2, or auto channels with no audio input: Audio omitted from the output
            1 channel with any input with audio: One track with one channel, downmixed if necessary
            2 channels with one track with one channel: Two tracks with one identical channel each
            2 or auto channels with two tracks with one channel each: Two tracks with one channel each
            2 or auto channels with one track with two channels: Two tracks with one channel each
            2 channels with one track with multiple channels: Two tracks with one channel each
            auto channels with one track with one channel: One track with one channel
            auto channels with one track with multiple channels: Up to eight tracks with one channel each
            When you specify OneChannelPerTrackWithMosTo8Tracks , Elastic Transcoder creates eight single-channel tracks for your output. All tracks that do not contain audio data from an input channel are MOS, or Mit Out Sound, tracks.
            The outputs of OneChannelPerTrackWithMosTo8Tracks for a specific channel value and inputs are as follows:
            0 channels with any input: Audio omitted from the output
            1, 2, or auto channels with no audio input: Audio omitted from the output
            1 channel with any input with audio: One track with one channel, downmixed if necessary, plus six MOS tracks
            2 channels with one track with one channel: Two tracks with one identical channel each, plus six MOS tracks
            2 or auto channels with two tracks with one channel each: Two tracks with one channel each, plus six MOS tracks
            2 or auto channels with one track with two channels: Two tracks with one channel each, plus six MOS tracks
            2 channels with one track with multiple channels: Two tracks with one channel each, plus six MOS tracks
            auto channels with one track with one channel: One track with one channel, plus seven MOS tracks
            auto channels with one track with multiple channels: Up to eight tracks with one channel each, plus MOS tracks until there are eight tracks in all
            CodecOptions (dict) --If you specified AAC for Audio:Codec , this is the AAC compression profile to use. Valid values include:
            auto , AAC-LC , HE-AAC , HE-AACv2
            If you specify auto , Elastic Transcoder chooses a profile based on the bit rate of the output file.
            Profile (string) --You can only choose an audio profile when you specify AAC for the value of Audio:Codec.
            Specify the AAC profile for the output file. Elastic Transcoder supports the following profiles:
            auto : If you specify auto , Elastic Transcoder selects the profile based on the bit rate selected for the output file.
            AAC-LC : The most common AAC profile. Use for bit rates larger than 64 kbps.
            HE-AAC : Not supported on some older players and devices. Use for bit rates between 40 and 80 kbps.
            HE-AACv2 : Not supported on some players and devices. Use for bit rates less than 48 kbps.
            All outputs in a Smooth playlist must have the same value for Profile .
            Note
            If you created any presets before AAC profiles were added, Elastic Transcoder automatically updated your presets to use AAC-LC. You can change the value as required.
            BitDepth (string) --You can only choose an audio bit depth when you specify flac or pcm for the value of Audio:Codec.
            The bit depth of a sample is how many bits of information are included in the audio samples. The higher the bit depth, the better the audio, but the larger the file.
            Valid values are 16 and 24 .
            The most common bit depth is 24 .
            BitOrder (string) --You can only choose an audio bit order when you specify pcm for the value of Audio:Codec.
            The order the bits of a PCM sample are stored in.
            The supported value is LittleEndian .
            Signed (string) --You can only choose whether an audio sample is signed when you specify pcm for the value of Audio:Codec.
            Whether audio samples are represented with negative and positive numbers (signed) or only positive numbers (unsigned).
            The supported value is Signed .
            
            

    :type Thumbnails: dict
    :param Thumbnails: A section of the request body that specifies the thumbnail parameters, if any.
            Format (string) --The format of thumbnails, if any. Valid values are jpg and png .
            You specify whether you want Elastic Transcoder to create thumbnails when you create a job.
            Interval (string) --The approximate number of seconds between thumbnails. Specify an integer value.
            Resolution (string) --
            Warning
            To better control resolution and aspect ratio of thumbnails, we recommend that you use the values MaxWidth , MaxHeight , SizingPolicy , and PaddingPolicy instead of Resolution and AspectRatio . The two groups of settings are mutually exclusive. Do not use them together.
            The width and height of thumbnail files in pixels. Specify a value in the format `` width `` x `` height `` where both values are even integers. The values cannot exceed the width and height that you specified in the Video:Resolution object.
            AspectRatio (string) --
            Warning
            To better control resolution and aspect ratio of thumbnails, we recommend that you use the values MaxWidth , MaxHeight , SizingPolicy , and PaddingPolicy instead of Resolution and AspectRatio . The two groups of settings are mutually exclusive. Do not use them together.
            The aspect ratio of thumbnails. Valid values include:
            auto , 1:1 , 4:3 , 3:2 , 16:9
            If you specify auto , Elastic Transcoder tries to preserve the aspect ratio of the video in the output file.
            MaxWidth (string) --The maximum width of thumbnails in pixels. If you specify auto, Elastic Transcoder uses 1920 (Full HD) as the default value. If you specify a numeric value, enter an even integer between 32 and 4096.
            MaxHeight (string) --The maximum height of thumbnails in pixels. If you specify auto, Elastic Transcoder uses 1080 (Full HD) as the default value. If you specify a numeric value, enter an even integer between 32 and 3072.
            SizingPolicy (string) --Specify one of the following values to control scaling of thumbnails:
            Fit : Elastic Transcoder scales thumbnails so they match the value that you specified in thumbnail MaxWidth or MaxHeight settings without exceeding the other value.
            Fill : Elastic Transcoder scales thumbnails so they match the value that you specified in thumbnail MaxWidth or MaxHeight settings and matches or exceeds the other value. Elastic Transcoder centers the image in thumbnails and then crops in the dimension (if any) that exceeds the maximum value.
            Stretch : Elastic Transcoder stretches thumbnails to match the values that you specified for thumbnail MaxWidth and MaxHeight settings. If the relative proportions of the input video and thumbnails are different, the thumbnails will be distorted.
            Keep : Elastic Transcoder does not scale thumbnails. If either dimension of the input video exceeds the values that you specified for thumbnail MaxWidth and MaxHeight settings, Elastic Transcoder crops the thumbnails.
            ShrinkToFit : Elastic Transcoder scales thumbnails down so that their dimensions match the values that you specified for at least one of thumbnail MaxWidth and MaxHeight without exceeding either value. If you specify this option, Elastic Transcoder does not scale thumbnails up.
            ShrinkToFill : Elastic Transcoder scales thumbnails down so that their dimensions match the values that you specified for at least one of MaxWidth and MaxHeight without dropping below either value. If you specify this option, Elastic Transcoder does not scale thumbnails up.
            PaddingPolicy (string) --When you set PaddingPolicy to Pad , Elastic Transcoder may add black bars to the top and bottom and/or left and right sides of thumbnails to make the total size of the thumbnails match the values that you specified for thumbnail MaxWidth and MaxHeight settings.
            

    :rtype: dict
    :return: {
        'Preset': {
            'Id': 'string',
            'Arn': 'string',
            'Name': 'string',
            'Description': 'string',
            'Container': 'string',
            'Audio': {
                'Codec': 'string',
                'SampleRate': 'string',
                'BitRate': 'string',
                'Channels': 'string',
                'AudioPackingMode': 'string',
                'CodecOptions': {
                    'Profile': 'string',
                    'BitDepth': 'string',
                    'BitOrder': 'string',
                    'Signed': 'string'
                }
            },
            'Video': {
                'Codec': 'string',
                'CodecOptions': {
                    'string': 'string'
                },
                'KeyframesMaxDist': 'string',
                'FixedGOP': 'string',
                'BitRate': 'string',
                'FrameRate': 'string',
                'MaxFrameRate': 'string',
                'Resolution': 'string',
                'AspectRatio': 'string',
                'MaxWidth': 'string',
                'MaxHeight': 'string',
                'DisplayAspectRatio': 'string',
                'SizingPolicy': 'string',
                'PaddingPolicy': 'string',
                'Watermarks': [
                    {
                        'Id': 'string',
                        'MaxWidth': 'string',
                        'MaxHeight': 'string',
                        'SizingPolicy': 'string',
                        'HorizontalAlign': 'string',
                        'HorizontalOffset': 'string',
                        'VerticalAlign': 'string',
                        'VerticalOffset': 'string',
                        'Opacity': 'string',
                        'Target': 'string'
                    },
                ]
            },
            'Thumbnails': {
                'Format': 'string',
                'Interval': 'string',
                'Resolution': 'string',
                'AspectRatio': 'string',
                'MaxWidth': 'string',
                'MaxHeight': 'string',
                'SizingPolicy': 'string',
                'PaddingPolicy': 'string'
            },
            'Type': 'string'
        },
        'Warning': 'string'
    }
    
    
    :returns: 
    auto channel specified, with any input: Pass through up to eight input channels.
    0 channels specified, with any input: Audio omitted from the output.
    1 channel specified, with at least one input channel: Mono sound.
    2 channels specified, with any input: Two identical mono channels or stereo. For more information about tracks, see Audio:AudioPackingMode.
    
    """
    pass

def delete_pipeline(Id=None):
    """
    The DeletePipeline operation removes a pipeline.
    You can only delete a pipeline that has never been used or that is not currently in use (doesn't contain any active jobs). If the pipeline is currently in use, DeletePipeline returns an error.
    See also: AWS API Documentation
    
    
    :example: response = client.delete_pipeline(
        Id='string'
    )
    
    
    :type Id: string
    :param Id: [REQUIRED]
            The identifier of the pipeline that you want to delete.
            

    :rtype: dict
    :return: {}
    
    
    """
    pass

def delete_preset(Id=None):
    """
    The DeletePreset operation removes a preset that you've added in an AWS region.
    See also: AWS API Documentation
    
    
    :example: response = client.delete_preset(
        Id='string'
    )
    
    
    :type Id: string
    :param Id: [REQUIRED]
            The identifier of the preset for which you want to get detailed information.
            

    :rtype: dict
    :return: {}
    
    
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

def get_waiter():
    """
    
    """
    pass

def list_jobs_by_pipeline(PipelineId=None, Ascending=None, PageToken=None):
    """
    The ListJobsByPipeline operation gets a list of the jobs currently in a pipeline.
    Elastic Transcoder returns all of the jobs currently in the specified pipeline. The response body contains one element for each job that satisfies the search criteria.
    See also: AWS API Documentation
    
    
    :example: response = client.list_jobs_by_pipeline(
        PipelineId='string',
        Ascending='string',
        PageToken='string'
    )
    
    
    :type PipelineId: string
    :param PipelineId: [REQUIRED]
            The ID of the pipeline for which you want to get job information.
            

    :type Ascending: string
    :param Ascending: To list jobs in chronological order by the date and time that they were submitted, enter true . To list jobs in reverse chronological order, enter false .

    :type PageToken: string
    :param PageToken: When Elastic Transcoder returns more than one page of results, use pageToken in subsequent GET requests to get each successive page of results.

    :rtype: dict
    :return: {
        'Jobs': [
            {
                'Id': 'string',
                'Arn': 'string',
                'PipelineId': 'string',
                'Input': {
                    'Key': 'string',
                    'FrameRate': 'string',
                    'Resolution': 'string',
                    'AspectRatio': 'string',
                    'Interlaced': 'string',
                    'Container': 'string',
                    'Encryption': {
                        'Mode': 'string',
                        'Key': 'string',
                        'KeyMd5': 'string',
                        'InitializationVector': 'string'
                    },
                    'TimeSpan': {
                        'StartTime': 'string',
                        'Duration': 'string'
                    },
                    'InputCaptions': {
                        'MergePolicy': 'string',
                        'CaptionSources': [
                            {
                                'Key': 'string',
                                'Language': 'string',
                                'TimeOffset': 'string',
                                'Label': 'string',
                                'Encryption': {
                                    'Mode': 'string',
                                    'Key': 'string',
                                    'KeyMd5': 'string',
                                    'InitializationVector': 'string'
                                }
                            },
                        ]
                    },
                    'DetectedProperties': {
                        'Width': 123,
                        'Height': 123,
                        'FrameRate': 'string',
                        'FileSize': 123,
                        'DurationMillis': 123
                    }
                },
                'Inputs': [
                    {
                        'Key': 'string',
                        'FrameRate': 'string',
                        'Resolution': 'string',
                        'AspectRatio': 'string',
                        'Interlaced': 'string',
                        'Container': 'string',
                        'Encryption': {
                            'Mode': 'string',
                            'Key': 'string',
                            'KeyMd5': 'string',
                            'InitializationVector': 'string'
                        },
                        'TimeSpan': {
                            'StartTime': 'string',
                            'Duration': 'string'
                        },
                        'InputCaptions': {
                            'MergePolicy': 'string',
                            'CaptionSources': [
                                {
                                    'Key': 'string',
                                    'Language': 'string',
                                    'TimeOffset': 'string',
                                    'Label': 'string',
                                    'Encryption': {
                                        'Mode': 'string',
                                        'Key': 'string',
                                        'KeyMd5': 'string',
                                        'InitializationVector': 'string'
                                    }
                                },
                            ]
                        },
                        'DetectedProperties': {
                            'Width': 123,
                            'Height': 123,
                            'FrameRate': 'string',
                            'FileSize': 123,
                            'DurationMillis': 123
                        }
                    },
                ],
                'Output': {
                    'Id': 'string',
                    'Key': 'string',
                    'ThumbnailPattern': 'string',
                    'ThumbnailEncryption': {
                        'Mode': 'string',
                        'Key': 'string',
                        'KeyMd5': 'string',
                        'InitializationVector': 'string'
                    },
                    'Rotate': 'string',
                    'PresetId': 'string',
                    'SegmentDuration': 'string',
                    'Status': 'string',
                    'StatusDetail': 'string',
                    'Duration': 123,
                    'Width': 123,
                    'Height': 123,
                    'FrameRate': 'string',
                    'FileSize': 123,
                    'DurationMillis': 123,
                    'Watermarks': [
                        {
                            'PresetWatermarkId': 'string',
                            'InputKey': 'string',
                            'Encryption': {
                                'Mode': 'string',
                                'Key': 'string',
                                'KeyMd5': 'string',
                                'InitializationVector': 'string'
                            }
                        },
                    ],
                    'AlbumArt': {
                        'MergePolicy': 'string',
                        'Artwork': [
                            {
                                'InputKey': 'string',
                                'MaxWidth': 'string',
                                'MaxHeight': 'string',
                                'SizingPolicy': 'string',
                                'PaddingPolicy': 'string',
                                'AlbumArtFormat': 'string',
                                'Encryption': {
                                    'Mode': 'string',
                                    'Key': 'string',
                                    'KeyMd5': 'string',
                                    'InitializationVector': 'string'
                                }
                            },
                        ]
                    },
                    'Composition': [
                        {
                            'TimeSpan': {
                                'StartTime': 'string',
                                'Duration': 'string'
                            }
                        },
                    ],
                    'Captions': {
                        'MergePolicy': 'string',
                        'CaptionSources': [
                            {
                                'Key': 'string',
                                'Language': 'string',
                                'TimeOffset': 'string',
                                'Label': 'string',
                                'Encryption': {
                                    'Mode': 'string',
                                    'Key': 'string',
                                    'KeyMd5': 'string',
                                    'InitializationVector': 'string'
                                }
                            },
                        ],
                        'CaptionFormats': [
                            {
                                'Format': 'string',
                                'Pattern': 'string',
                                'Encryption': {
                                    'Mode': 'string',
                                    'Key': 'string',
                                    'KeyMd5': 'string',
                                    'InitializationVector': 'string'
                                }
                            },
                        ]
                    },
                    'Encryption': {
                        'Mode': 'string',
                        'Key': 'string',
                        'KeyMd5': 'string',
                        'InitializationVector': 'string'
                    },
                    'AppliedColorSpaceConversion': 'string'
                },
                'Outputs': [
                    {
                        'Id': 'string',
                        'Key': 'string',
                        'ThumbnailPattern': 'string',
                        'ThumbnailEncryption': {
                            'Mode': 'string',
                            'Key': 'string',
                            'KeyMd5': 'string',
                            'InitializationVector': 'string'
                        },
                        'Rotate': 'string',
                        'PresetId': 'string',
                        'SegmentDuration': 'string',
                        'Status': 'string',
                        'StatusDetail': 'string',
                        'Duration': 123,
                        'Width': 123,
                        'Height': 123,
                        'FrameRate': 'string',
                        'FileSize': 123,
                        'DurationMillis': 123,
                        'Watermarks': [
                            {
                                'PresetWatermarkId': 'string',
                                'InputKey': 'string',
                                'Encryption': {
                                    'Mode': 'string',
                                    'Key': 'string',
                                    'KeyMd5': 'string',
                                    'InitializationVector': 'string'
                                }
                            },
                        ],
                        'AlbumArt': {
                            'MergePolicy': 'string',
                            'Artwork': [
                                {
                                    'InputKey': 'string',
                                    'MaxWidth': 'string',
                                    'MaxHeight': 'string',
                                    'SizingPolicy': 'string',
                                    'PaddingPolicy': 'string',
                                    'AlbumArtFormat': 'string',
                                    'Encryption': {
                                        'Mode': 'string',
                                        'Key': 'string',
                                        'KeyMd5': 'string',
                                        'InitializationVector': 'string'
                                    }
                                },
                            ]
                        },
                        'Composition': [
                            {
                                'TimeSpan': {
                                    'StartTime': 'string',
                                    'Duration': 'string'
                                }
                            },
                        ],
                        'Captions': {
                            'MergePolicy': 'string',
                            'CaptionSources': [
                                {
                                    'Key': 'string',
                                    'Language': 'string',
                                    'TimeOffset': 'string',
                                    'Label': 'string',
                                    'Encryption': {
                                        'Mode': 'string',
                                        'Key': 'string',
                                        'KeyMd5': 'string',
                                        'InitializationVector': 'string'
                                    }
                                },
                            ],
                            'CaptionFormats': [
                                {
                                    'Format': 'string',
                                    'Pattern': 'string',
                                    'Encryption': {
                                        'Mode': 'string',
                                        'Key': 'string',
                                        'KeyMd5': 'string',
                                        'InitializationVector': 'string'
                                    }
                                },
                            ]
                        },
                        'Encryption': {
                            'Mode': 'string',
                            'Key': 'string',
                            'KeyMd5': 'string',
                            'InitializationVector': 'string'
                        },
                        'AppliedColorSpaceConversion': 'string'
                    },
                ],
                'OutputKeyPrefix': 'string',
                'Playlists': [
                    {
                        'Name': 'string',
                        'Format': 'string',
                        'OutputKeys': [
                            'string',
                        ],
                        'HlsContentProtection': {
                            'Method': 'string',
                            'Key': 'string',
                            'KeyMd5': 'string',
                            'InitializationVector': 'string',
                            'LicenseAcquisitionUrl': 'string',
                            'KeyStoragePolicy': 'string'
                        },
                        'PlayReadyDrm': {
                            'Format': 'string',
                            'Key': 'string',
                            'KeyMd5': 'string',
                            'KeyId': 'string',
                            'InitializationVector': 'string',
                            'LicenseAcquisitionUrl': 'string'
                        },
                        'Status': 'string',
                        'StatusDetail': 'string'
                    },
                ],
                'Status': 'string',
                'UserMetadata': {
                    'string': 'string'
                },
                'Timing': {
                    'SubmitTimeMillis': 123,
                    'StartTimeMillis': 123,
                    'FinishTimeMillis': 123
                }
            },
        ],
        'NextPageToken': 'string'
    }
    
    
    :returns: 
    S3: Amazon S3 creates and manages the keys used for encrypting your files.
    S3-AWS-KMS: Amazon S3 calls the Amazon Key Management Service, which creates and manages the keys that are used for encrypting your files. If you specify S3-AWS-KMS and you don't want to use the default key, you must add the AWS-KMS key that you want to use to your pipeline.
    AES-CBC-PKCS7: A padded cipher-block mode of operation originally used for HLS files.
    AES-CTR: AES Counter Mode.
    AES-GCM: AES Galois Counter Mode, a mode of operation that is an authenticated encryption format, meaning that a file, key, or initialization vector that has been tampered with fails the decryption process.
    
    """
    pass

def list_jobs_by_status(Status=None, Ascending=None, PageToken=None):
    """
    The ListJobsByStatus operation gets a list of jobs that have a specified status. The response body contains one element for each job that satisfies the search criteria.
    See also: AWS API Documentation
    
    
    :example: response = client.list_jobs_by_status(
        Status='string',
        Ascending='string',
        PageToken='string'
    )
    
    
    :type Status: string
    :param Status: [REQUIRED]
            To get information about all of the jobs associated with the current AWS account that have a given status, specify the following status: Submitted , Progressing , Complete , Canceled , or Error .
            

    :type Ascending: string
    :param Ascending: To list jobs in chronological order by the date and time that they were submitted, enter true . To list jobs in reverse chronological order, enter false .

    :type PageToken: string
    :param PageToken: When Elastic Transcoder returns more than one page of results, use pageToken in subsequent GET requests to get each successive page of results.

    :rtype: dict
    :return: {
        'Jobs': [
            {
                'Id': 'string',
                'Arn': 'string',
                'PipelineId': 'string',
                'Input': {
                    'Key': 'string',
                    'FrameRate': 'string',
                    'Resolution': 'string',
                    'AspectRatio': 'string',
                    'Interlaced': 'string',
                    'Container': 'string',
                    'Encryption': {
                        'Mode': 'string',
                        'Key': 'string',
                        'KeyMd5': 'string',
                        'InitializationVector': 'string'
                    },
                    'TimeSpan': {
                        'StartTime': 'string',
                        'Duration': 'string'
                    },
                    'InputCaptions': {
                        'MergePolicy': 'string',
                        'CaptionSources': [
                            {
                                'Key': 'string',
                                'Language': 'string',
                                'TimeOffset': 'string',
                                'Label': 'string',
                                'Encryption': {
                                    'Mode': 'string',
                                    'Key': 'string',
                                    'KeyMd5': 'string',
                                    'InitializationVector': 'string'
                                }
                            },
                        ]
                    },
                    'DetectedProperties': {
                        'Width': 123,
                        'Height': 123,
                        'FrameRate': 'string',
                        'FileSize': 123,
                        'DurationMillis': 123
                    }
                },
                'Inputs': [
                    {
                        'Key': 'string',
                        'FrameRate': 'string',
                        'Resolution': 'string',
                        'AspectRatio': 'string',
                        'Interlaced': 'string',
                        'Container': 'string',
                        'Encryption': {
                            'Mode': 'string',
                            'Key': 'string',
                            'KeyMd5': 'string',
                            'InitializationVector': 'string'
                        },
                        'TimeSpan': {
                            'StartTime': 'string',
                            'Duration': 'string'
                        },
                        'InputCaptions': {
                            'MergePolicy': 'string',
                            'CaptionSources': [
                                {
                                    'Key': 'string',
                                    'Language': 'string',
                                    'TimeOffset': 'string',
                                    'Label': 'string',
                                    'Encryption': {
                                        'Mode': 'string',
                                        'Key': 'string',
                                        'KeyMd5': 'string',
                                        'InitializationVector': 'string'
                                    }
                                },
                            ]
                        },
                        'DetectedProperties': {
                            'Width': 123,
                            'Height': 123,
                            'FrameRate': 'string',
                            'FileSize': 123,
                            'DurationMillis': 123
                        }
                    },
                ],
                'Output': {
                    'Id': 'string',
                    'Key': 'string',
                    'ThumbnailPattern': 'string',
                    'ThumbnailEncryption': {
                        'Mode': 'string',
                        'Key': 'string',
                        'KeyMd5': 'string',
                        'InitializationVector': 'string'
                    },
                    'Rotate': 'string',
                    'PresetId': 'string',
                    'SegmentDuration': 'string',
                    'Status': 'string',
                    'StatusDetail': 'string',
                    'Duration': 123,
                    'Width': 123,
                    'Height': 123,
                    'FrameRate': 'string',
                    'FileSize': 123,
                    'DurationMillis': 123,
                    'Watermarks': [
                        {
                            'PresetWatermarkId': 'string',
                            'InputKey': 'string',
                            'Encryption': {
                                'Mode': 'string',
                                'Key': 'string',
                                'KeyMd5': 'string',
                                'InitializationVector': 'string'
                            }
                        },
                    ],
                    'AlbumArt': {
                        'MergePolicy': 'string',
                        'Artwork': [
                            {
                                'InputKey': 'string',
                                'MaxWidth': 'string',
                                'MaxHeight': 'string',
                                'SizingPolicy': 'string',
                                'PaddingPolicy': 'string',
                                'AlbumArtFormat': 'string',
                                'Encryption': {
                                    'Mode': 'string',
                                    'Key': 'string',
                                    'KeyMd5': 'string',
                                    'InitializationVector': 'string'
                                }
                            },
                        ]
                    },
                    'Composition': [
                        {
                            'TimeSpan': {
                                'StartTime': 'string',
                                'Duration': 'string'
                            }
                        },
                    ],
                    'Captions': {
                        'MergePolicy': 'string',
                        'CaptionSources': [
                            {
                                'Key': 'string',
                                'Language': 'string',
                                'TimeOffset': 'string',
                                'Label': 'string',
                                'Encryption': {
                                    'Mode': 'string',
                                    'Key': 'string',
                                    'KeyMd5': 'string',
                                    'InitializationVector': 'string'
                                }
                            },
                        ],
                        'CaptionFormats': [
                            {
                                'Format': 'string',
                                'Pattern': 'string',
                                'Encryption': {
                                    'Mode': 'string',
                                    'Key': 'string',
                                    'KeyMd5': 'string',
                                    'InitializationVector': 'string'
                                }
                            },
                        ]
                    },
                    'Encryption': {
                        'Mode': 'string',
                        'Key': 'string',
                        'KeyMd5': 'string',
                        'InitializationVector': 'string'
                    },
                    'AppliedColorSpaceConversion': 'string'
                },
                'Outputs': [
                    {
                        'Id': 'string',
                        'Key': 'string',
                        'ThumbnailPattern': 'string',
                        'ThumbnailEncryption': {
                            'Mode': 'string',
                            'Key': 'string',
                            'KeyMd5': 'string',
                            'InitializationVector': 'string'
                        },
                        'Rotate': 'string',
                        'PresetId': 'string',
                        'SegmentDuration': 'string',
                        'Status': 'string',
                        'StatusDetail': 'string',
                        'Duration': 123,
                        'Width': 123,
                        'Height': 123,
                        'FrameRate': 'string',
                        'FileSize': 123,
                        'DurationMillis': 123,
                        'Watermarks': [
                            {
                                'PresetWatermarkId': 'string',
                                'InputKey': 'string',
                                'Encryption': {
                                    'Mode': 'string',
                                    'Key': 'string',
                                    'KeyMd5': 'string',
                                    'InitializationVector': 'string'
                                }
                            },
                        ],
                        'AlbumArt': {
                            'MergePolicy': 'string',
                            'Artwork': [
                                {
                                    'InputKey': 'string',
                                    'MaxWidth': 'string',
                                    'MaxHeight': 'string',
                                    'SizingPolicy': 'string',
                                    'PaddingPolicy': 'string',
                                    'AlbumArtFormat': 'string',
                                    'Encryption': {
                                        'Mode': 'string',
                                        'Key': 'string',
                                        'KeyMd5': 'string',
                                        'InitializationVector': 'string'
                                    }
                                },
                            ]
                        },
                        'Composition': [
                            {
                                'TimeSpan': {
                                    'StartTime': 'string',
                                    'Duration': 'string'
                                }
                            },
                        ],
                        'Captions': {
                            'MergePolicy': 'string',
                            'CaptionSources': [
                                {
                                    'Key': 'string',
                                    'Language': 'string',
                                    'TimeOffset': 'string',
                                    'Label': 'string',
                                    'Encryption': {
                                        'Mode': 'string',
                                        'Key': 'string',
                                        'KeyMd5': 'string',
                                        'InitializationVector': 'string'
                                    }
                                },
                            ],
                            'CaptionFormats': [
                                {
                                    'Format': 'string',
                                    'Pattern': 'string',
                                    'Encryption': {
                                        'Mode': 'string',
                                        'Key': 'string',
                                        'KeyMd5': 'string',
                                        'InitializationVector': 'string'
                                    }
                                },
                            ]
                        },
                        'Encryption': {
                            'Mode': 'string',
                            'Key': 'string',
                            'KeyMd5': 'string',
                            'InitializationVector': 'string'
                        },
                        'AppliedColorSpaceConversion': 'string'
                    },
                ],
                'OutputKeyPrefix': 'string',
                'Playlists': [
                    {
                        'Name': 'string',
                        'Format': 'string',
                        'OutputKeys': [
                            'string',
                        ],
                        'HlsContentProtection': {
                            'Method': 'string',
                            'Key': 'string',
                            'KeyMd5': 'string',
                            'InitializationVector': 'string',
                            'LicenseAcquisitionUrl': 'string',
                            'KeyStoragePolicy': 'string'
                        },
                        'PlayReadyDrm': {
                            'Format': 'string',
                            'Key': 'string',
                            'KeyMd5': 'string',
                            'KeyId': 'string',
                            'InitializationVector': 'string',
                            'LicenseAcquisitionUrl': 'string'
                        },
                        'Status': 'string',
                        'StatusDetail': 'string'
                    },
                ],
                'Status': 'string',
                'UserMetadata': {
                    'string': 'string'
                },
                'Timing': {
                    'SubmitTimeMillis': 123,
                    'StartTimeMillis': 123,
                    'FinishTimeMillis': 123
                }
            },
        ],
        'NextPageToken': 'string'
    }
    
    
    :returns: 
    S3: Amazon S3 creates and manages the keys used for encrypting your files.
    S3-AWS-KMS: Amazon S3 calls the Amazon Key Management Service, which creates and manages the keys that are used for encrypting your files. If you specify S3-AWS-KMS and you don't want to use the default key, you must add the AWS-KMS key that you want to use to your pipeline.
    AES-CBC-PKCS7: A padded cipher-block mode of operation originally used for HLS files.
    AES-CTR: AES Counter Mode.
    AES-GCM: AES Galois Counter Mode, a mode of operation that is an authenticated encryption format, meaning that a file, key, or initialization vector that has been tampered with fails the decryption process.
    
    """
    pass

def list_pipelines(Ascending=None, PageToken=None):
    """
    The ListPipelines operation gets a list of the pipelines associated with the current AWS account.
    See also: AWS API Documentation
    
    
    :example: response = client.list_pipelines(
        Ascending='string',
        PageToken='string'
    )
    
    
    :type Ascending: string
    :param Ascending: To list pipelines in chronological order by the date and time that they were created, enter true . To list pipelines in reverse chronological order, enter false .

    :type PageToken: string
    :param PageToken: When Elastic Transcoder returns more than one page of results, use pageToken in subsequent GET requests to get each successive page of results.

    :rtype: dict
    :return: {
        'Pipelines': [
            {
                'Id': 'string',
                'Arn': 'string',
                'Name': 'string',
                'Status': 'string',
                'InputBucket': 'string',
                'OutputBucket': 'string',
                'Role': 'string',
                'AwsKmsKeyArn': 'string',
                'Notifications': {
                    'Progressing': 'string',
                    'Completed': 'string',
                    'Warning': 'string',
                    'Error': 'string'
                },
                'ContentConfig': {
                    'Bucket': 'string',
                    'StorageClass': 'string',
                    'Permissions': [
                        {
                            'GranteeType': 'string',
                            'Grantee': 'string',
                            'Access': [
                                'string',
                            ]
                        },
                    ]
                },
                'ThumbnailConfig': {
                    'Bucket': 'string',
                    'StorageClass': 'string',
                    'Permissions': [
                        {
                            'GranteeType': 'string',
                            'Grantee': 'string',
                            'Access': [
                                'string',
                            ]
                        },
                    ]
                }
            },
        ],
        'NextPageToken': 'string'
    }
    
    
    :returns: 
    Active : The pipeline is processing jobs.
    Paused : The pipeline is not currently processing jobs.
    
    """
    pass

def list_presets(Ascending=None, PageToken=None):
    """
    The ListPresets operation gets a list of the default presets included with Elastic Transcoder and the presets that you've added in an AWS region.
    See also: AWS API Documentation
    
    
    :example: response = client.list_presets(
        Ascending='string',
        PageToken='string'
    )
    
    
    :type Ascending: string
    :param Ascending: To list presets in chronological order by the date and time that they were created, enter true . To list presets in reverse chronological order, enter false .

    :type PageToken: string
    :param PageToken: When Elastic Transcoder returns more than one page of results, use pageToken in subsequent GET requests to get each successive page of results.

    :rtype: dict
    :return: {
        'Presets': [
            {
                'Id': 'string',
                'Arn': 'string',
                'Name': 'string',
                'Description': 'string',
                'Container': 'string',
                'Audio': {
                    'Codec': 'string',
                    'SampleRate': 'string',
                    'BitRate': 'string',
                    'Channels': 'string',
                    'AudioPackingMode': 'string',
                    'CodecOptions': {
                        'Profile': 'string',
                        'BitDepth': 'string',
                        'BitOrder': 'string',
                        'Signed': 'string'
                    }
                },
                'Video': {
                    'Codec': 'string',
                    'CodecOptions': {
                        'string': 'string'
                    },
                    'KeyframesMaxDist': 'string',
                    'FixedGOP': 'string',
                    'BitRate': 'string',
                    'FrameRate': 'string',
                    'MaxFrameRate': 'string',
                    'Resolution': 'string',
                    'AspectRatio': 'string',
                    'MaxWidth': 'string',
                    'MaxHeight': 'string',
                    'DisplayAspectRatio': 'string',
                    'SizingPolicy': 'string',
                    'PaddingPolicy': 'string',
                    'Watermarks': [
                        {
                            'Id': 'string',
                            'MaxWidth': 'string',
                            'MaxHeight': 'string',
                            'SizingPolicy': 'string',
                            'HorizontalAlign': 'string',
                            'HorizontalOffset': 'string',
                            'VerticalAlign': 'string',
                            'VerticalOffset': 'string',
                            'Opacity': 'string',
                            'Target': 'string'
                        },
                    ]
                },
                'Thumbnails': {
                    'Format': 'string',
                    'Interval': 'string',
                    'Resolution': 'string',
                    'AspectRatio': 'string',
                    'MaxWidth': 'string',
                    'MaxHeight': 'string',
                    'SizingPolicy': 'string',
                    'PaddingPolicy': 'string'
                },
                'Type': 'string'
            },
        ],
        'NextPageToken': 'string'
    }
    
    
    :returns: 
    auto channel specified, with any input: Pass through up to eight input channels.
    0 channels specified, with any input: Audio omitted from the output.
    1 channel specified, with at least one input channel: Mono sound.
    2 channels specified, with any input: Two identical mono channels or stereo. For more information about tracks, see Audio:AudioPackingMode.
    
    """
    pass

def read_job(Id=None):
    """
    The ReadJob operation returns detailed information about a job.
    See also: AWS API Documentation
    
    
    :example: response = client.read_job(
        Id='string'
    )
    
    
    :type Id: string
    :param Id: [REQUIRED]
            The identifier of the job for which you want to get detailed information.
            

    :rtype: dict
    :return: {
        'Job': {
            'Id': 'string',
            'Arn': 'string',
            'PipelineId': 'string',
            'Input': {
                'Key': 'string',
                'FrameRate': 'string',
                'Resolution': 'string',
                'AspectRatio': 'string',
                'Interlaced': 'string',
                'Container': 'string',
                'Encryption': {
                    'Mode': 'string',
                    'Key': 'string',
                    'KeyMd5': 'string',
                    'InitializationVector': 'string'
                },
                'TimeSpan': {
                    'StartTime': 'string',
                    'Duration': 'string'
                },
                'InputCaptions': {
                    'MergePolicy': 'string',
                    'CaptionSources': [
                        {
                            'Key': 'string',
                            'Language': 'string',
                            'TimeOffset': 'string',
                            'Label': 'string',
                            'Encryption': {
                                'Mode': 'string',
                                'Key': 'string',
                                'KeyMd5': 'string',
                                'InitializationVector': 'string'
                            }
                        },
                    ]
                },
                'DetectedProperties': {
                    'Width': 123,
                    'Height': 123,
                    'FrameRate': 'string',
                    'FileSize': 123,
                    'DurationMillis': 123
                }
            },
            'Inputs': [
                {
                    'Key': 'string',
                    'FrameRate': 'string',
                    'Resolution': 'string',
                    'AspectRatio': 'string',
                    'Interlaced': 'string',
                    'Container': 'string',
                    'Encryption': {
                        'Mode': 'string',
                        'Key': 'string',
                        'KeyMd5': 'string',
                        'InitializationVector': 'string'
                    },
                    'TimeSpan': {
                        'StartTime': 'string',
                        'Duration': 'string'
                    },
                    'InputCaptions': {
                        'MergePolicy': 'string',
                        'CaptionSources': [
                            {
                                'Key': 'string',
                                'Language': 'string',
                                'TimeOffset': 'string',
                                'Label': 'string',
                                'Encryption': {
                                    'Mode': 'string',
                                    'Key': 'string',
                                    'KeyMd5': 'string',
                                    'InitializationVector': 'string'
                                }
                            },
                        ]
                    },
                    'DetectedProperties': {
                        'Width': 123,
                        'Height': 123,
                        'FrameRate': 'string',
                        'FileSize': 123,
                        'DurationMillis': 123
                    }
                },
            ],
            'Output': {
                'Id': 'string',
                'Key': 'string',
                'ThumbnailPattern': 'string',
                'ThumbnailEncryption': {
                    'Mode': 'string',
                    'Key': 'string',
                    'KeyMd5': 'string',
                    'InitializationVector': 'string'
                },
                'Rotate': 'string',
                'PresetId': 'string',
                'SegmentDuration': 'string',
                'Status': 'string',
                'StatusDetail': 'string',
                'Duration': 123,
                'Width': 123,
                'Height': 123,
                'FrameRate': 'string',
                'FileSize': 123,
                'DurationMillis': 123,
                'Watermarks': [
                    {
                        'PresetWatermarkId': 'string',
                        'InputKey': 'string',
                        'Encryption': {
                            'Mode': 'string',
                            'Key': 'string',
                            'KeyMd5': 'string',
                            'InitializationVector': 'string'
                        }
                    },
                ],
                'AlbumArt': {
                    'MergePolicy': 'string',
                    'Artwork': [
                        {
                            'InputKey': 'string',
                            'MaxWidth': 'string',
                            'MaxHeight': 'string',
                            'SizingPolicy': 'string',
                            'PaddingPolicy': 'string',
                            'AlbumArtFormat': 'string',
                            'Encryption': {
                                'Mode': 'string',
                                'Key': 'string',
                                'KeyMd5': 'string',
                                'InitializationVector': 'string'
                            }
                        },
                    ]
                },
                'Composition': [
                    {
                        'TimeSpan': {
                            'StartTime': 'string',
                            'Duration': 'string'
                        }
                    },
                ],
                'Captions': {
                    'MergePolicy': 'string',
                    'CaptionSources': [
                        {
                            'Key': 'string',
                            'Language': 'string',
                            'TimeOffset': 'string',
                            'Label': 'string',
                            'Encryption': {
                                'Mode': 'string',
                                'Key': 'string',
                                'KeyMd5': 'string',
                                'InitializationVector': 'string'
                            }
                        },
                    ],
                    'CaptionFormats': [
                        {
                            'Format': 'string',
                            'Pattern': 'string',
                            'Encryption': {
                                'Mode': 'string',
                                'Key': 'string',
                                'KeyMd5': 'string',
                                'InitializationVector': 'string'
                            }
                        },
                    ]
                },
                'Encryption': {
                    'Mode': 'string',
                    'Key': 'string',
                    'KeyMd5': 'string',
                    'InitializationVector': 'string'
                },
                'AppliedColorSpaceConversion': 'string'
            },
            'Outputs': [
                {
                    'Id': 'string',
                    'Key': 'string',
                    'ThumbnailPattern': 'string',
                    'ThumbnailEncryption': {
                        'Mode': 'string',
                        'Key': 'string',
                        'KeyMd5': 'string',
                        'InitializationVector': 'string'
                    },
                    'Rotate': 'string',
                    'PresetId': 'string',
                    'SegmentDuration': 'string',
                    'Status': 'string',
                    'StatusDetail': 'string',
                    'Duration': 123,
                    'Width': 123,
                    'Height': 123,
                    'FrameRate': 'string',
                    'FileSize': 123,
                    'DurationMillis': 123,
                    'Watermarks': [
                        {
                            'PresetWatermarkId': 'string',
                            'InputKey': 'string',
                            'Encryption': {
                                'Mode': 'string',
                                'Key': 'string',
                                'KeyMd5': 'string',
                                'InitializationVector': 'string'
                            }
                        },
                    ],
                    'AlbumArt': {
                        'MergePolicy': 'string',
                        'Artwork': [
                            {
                                'InputKey': 'string',
                                'MaxWidth': 'string',
                                'MaxHeight': 'string',
                                'SizingPolicy': 'string',
                                'PaddingPolicy': 'string',
                                'AlbumArtFormat': 'string',
                                'Encryption': {
                                    'Mode': 'string',
                                    'Key': 'string',
                                    'KeyMd5': 'string',
                                    'InitializationVector': 'string'
                                }
                            },
                        ]
                    },
                    'Composition': [
                        {
                            'TimeSpan': {
                                'StartTime': 'string',
                                'Duration': 'string'
                            }
                        },
                    ],
                    'Captions': {
                        'MergePolicy': 'string',
                        'CaptionSources': [
                            {
                                'Key': 'string',
                                'Language': 'string',
                                'TimeOffset': 'string',
                                'Label': 'string',
                                'Encryption': {
                                    'Mode': 'string',
                                    'Key': 'string',
                                    'KeyMd5': 'string',
                                    'InitializationVector': 'string'
                                }
                            },
                        ],
                        'CaptionFormats': [
                            {
                                'Format': 'string',
                                'Pattern': 'string',
                                'Encryption': {
                                    'Mode': 'string',
                                    'Key': 'string',
                                    'KeyMd5': 'string',
                                    'InitializationVector': 'string'
                                }
                            },
                        ]
                    },
                    'Encryption': {
                        'Mode': 'string',
                        'Key': 'string',
                        'KeyMd5': 'string',
                        'InitializationVector': 'string'
                    },
                    'AppliedColorSpaceConversion': 'string'
                },
            ],
            'OutputKeyPrefix': 'string',
            'Playlists': [
                {
                    'Name': 'string',
                    'Format': 'string',
                    'OutputKeys': [
                        'string',
                    ],
                    'HlsContentProtection': {
                        'Method': 'string',
                        'Key': 'string',
                        'KeyMd5': 'string',
                        'InitializationVector': 'string',
                        'LicenseAcquisitionUrl': 'string',
                        'KeyStoragePolicy': 'string'
                    },
                    'PlayReadyDrm': {
                        'Format': 'string',
                        'Key': 'string',
                        'KeyMd5': 'string',
                        'KeyId': 'string',
                        'InitializationVector': 'string',
                        'LicenseAcquisitionUrl': 'string'
                    },
                    'Status': 'string',
                    'StatusDetail': 'string'
                },
            ],
            'Status': 'string',
            'UserMetadata': {
                'string': 'string'
            },
            'Timing': {
                'SubmitTimeMillis': 123,
                'StartTimeMillis': 123,
                'FinishTimeMillis': 123
            }
        }
    }
    
    
    :returns: 
    Key
    Key MD5
    Initialization Vector
    
    """
    pass

def read_pipeline(Id=None):
    """
    The ReadPipeline operation gets detailed information about a pipeline.
    See also: AWS API Documentation
    
    
    :example: response = client.read_pipeline(
        Id='string'
    )
    
    
    :type Id: string
    :param Id: [REQUIRED]
            The identifier of the pipeline to read.
            

    :rtype: dict
    :return: {
        'Pipeline': {
            'Id': 'string',
            'Arn': 'string',
            'Name': 'string',
            'Status': 'string',
            'InputBucket': 'string',
            'OutputBucket': 'string',
            'Role': 'string',
            'AwsKmsKeyArn': 'string',
            'Notifications': {
                'Progressing': 'string',
                'Completed': 'string',
                'Warning': 'string',
                'Error': 'string'
            },
            'ContentConfig': {
                'Bucket': 'string',
                'StorageClass': 'string',
                'Permissions': [
                    {
                        'GranteeType': 'string',
                        'Grantee': 'string',
                        'Access': [
                            'string',
                        ]
                    },
                ]
            },
            'ThumbnailConfig': {
                'Bucket': 'string',
                'StorageClass': 'string',
                'Permissions': [
                    {
                        'GranteeType': 'string',
                        'Grantee': 'string',
                        'Access': [
                            'string',
                        ]
                    },
                ]
            }
        },
        'Warnings': [
            {
                'Code': 'string',
                'Message': 'string'
            },
        ]
    }
    
    
    :returns: 
    Progressing (optional): The Amazon Simple Notification Service (Amazon SNS) topic that you want to notify when Elastic Transcoder has started to process the job.
    Completed (optional): The Amazon SNS topic that you want to notify when Elastic Transcoder has finished processing the job.
    Warning (optional): The Amazon SNS topic that you want to notify when Elastic Transcoder encounters a warning condition.
    Error (optional): The Amazon SNS topic that you want to notify when Elastic Transcoder encounters an error condition.
    
    """
    pass

def read_preset(Id=None):
    """
    The ReadPreset operation gets detailed information about a preset.
    See also: AWS API Documentation
    
    
    :example: response = client.read_preset(
        Id='string'
    )
    
    
    :type Id: string
    :param Id: [REQUIRED]
            The identifier of the preset for which you want to get detailed information.
            

    :rtype: dict
    :return: {
        'Preset': {
            'Id': 'string',
            'Arn': 'string',
            'Name': 'string',
            'Description': 'string',
            'Container': 'string',
            'Audio': {
                'Codec': 'string',
                'SampleRate': 'string',
                'BitRate': 'string',
                'Channels': 'string',
                'AudioPackingMode': 'string',
                'CodecOptions': {
                    'Profile': 'string',
                    'BitDepth': 'string',
                    'BitOrder': 'string',
                    'Signed': 'string'
                }
            },
            'Video': {
                'Codec': 'string',
                'CodecOptions': {
                    'string': 'string'
                },
                'KeyframesMaxDist': 'string',
                'FixedGOP': 'string',
                'BitRate': 'string',
                'FrameRate': 'string',
                'MaxFrameRate': 'string',
                'Resolution': 'string',
                'AspectRatio': 'string',
                'MaxWidth': 'string',
                'MaxHeight': 'string',
                'DisplayAspectRatio': 'string',
                'SizingPolicy': 'string',
                'PaddingPolicy': 'string',
                'Watermarks': [
                    {
                        'Id': 'string',
                        'MaxWidth': 'string',
                        'MaxHeight': 'string',
                        'SizingPolicy': 'string',
                        'HorizontalAlign': 'string',
                        'HorizontalOffset': 'string',
                        'VerticalAlign': 'string',
                        'VerticalOffset': 'string',
                        'Opacity': 'string',
                        'Target': 'string'
                    },
                ]
            },
            'Thumbnails': {
                'Format': 'string',
                'Interval': 'string',
                'Resolution': 'string',
                'AspectRatio': 'string',
                'MaxWidth': 'string',
                'MaxHeight': 'string',
                'SizingPolicy': 'string',
                'PaddingPolicy': 'string'
            },
            'Type': 'string'
        }
    }
    
    
    :returns: 
    0 channels with any input: Audio omitted from the output
    1, 2, or auto channels with no audio input: Audio omitted from the output
    1 channel with any input with audio: One track with one channel, downmixed if necessary
    2 channels with one track with one channel: One track with two identical channels
    2 or auto channels with two tracks with one channel each: One track with two channels
    2 or auto channels with one track with two channels: One track with two channels
    2 channels with one track with multiple channels: One track with two channels
    auto channels with one track with one channel: One track with one channel
    auto channels with one track with multiple channels: One track with multiple channels
    
    """
    pass

def test_role(Role=None, InputBucket=None, OutputBucket=None, Topics=None):
    """
    The TestRole operation tests the IAM role used to create the pipeline.
    The TestRole action lets you determine whether the IAM role you are using has sufficient permissions to let Elastic Transcoder perform tasks associated with the transcoding process. The action attempts to assume the specified IAM role, checks read access to the input and output buckets, and tries to send a test notification to Amazon SNS topics that you specify.
    See also: AWS API Documentation
    
    
    :example: response = client.test_role(
        Role='string',
        InputBucket='string',
        OutputBucket='string',
        Topics=[
            'string',
        ]
    )
    
    
    :type Role: string
    :param Role: [REQUIRED]
            The IAM Amazon Resource Name (ARN) for the role that you want Elastic Transcoder to test.
            

    :type InputBucket: string
    :param InputBucket: [REQUIRED]
            The Amazon S3 bucket that contains media files to be transcoded. The action attempts to read from this bucket.
            

    :type OutputBucket: string
    :param OutputBucket: [REQUIRED]
            The Amazon S3 bucket that Elastic Transcoder writes transcoded media files to. The action attempts to read from this bucket.
            

    :type Topics: list
    :param Topics: [REQUIRED]
            The ARNs of one or more Amazon Simple Notification Service (Amazon SNS) topics that you want the action to send a test notification to.
            (string) --
            

    :rtype: dict
    :return: {
        'Success': 'string',
        'Messages': [
            'string',
        ]
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def update_pipeline(Id=None, Name=None, InputBucket=None, Role=None, AwsKmsKeyArn=None, Notifications=None, ContentConfig=None, ThumbnailConfig=None):
    """
    Use the UpdatePipeline operation to update settings for a pipeline.
    See also: AWS API Documentation
    
    
    :example: response = client.update_pipeline(
        Id='string',
        Name='string',
        InputBucket='string',
        Role='string',
        AwsKmsKeyArn='string',
        Notifications={
            'Progressing': 'string',
            'Completed': 'string',
            'Warning': 'string',
            'Error': 'string'
        },
        ContentConfig={
            'Bucket': 'string',
            'StorageClass': 'string',
            'Permissions': [
                {
                    'GranteeType': 'string',
                    'Grantee': 'string',
                    'Access': [
                        'string',
                    ]
                },
            ]
        },
        ThumbnailConfig={
            'Bucket': 'string',
            'StorageClass': 'string',
            'Permissions': [
                {
                    'GranteeType': 'string',
                    'Grantee': 'string',
                    'Access': [
                        'string',
                    ]
                },
            ]
        }
    )
    
    
    :type Id: string
    :param Id: [REQUIRED]
            The ID of the pipeline that you want to update.
            

    :type Name: string
    :param Name: The name of the pipeline. We recommend that the name be unique within the AWS account, but uniqueness is not enforced.
            Constraints: Maximum 40 characters
            

    :type InputBucket: string
    :param InputBucket: The Amazon S3 bucket in which you saved the media files that you want to transcode and the graphics that you want to use as watermarks.

    :type Role: string
    :param Role: The IAM Amazon Resource Name (ARN) for the role that you want Elastic Transcoder to use to transcode jobs for this pipeline.

    :type AwsKmsKeyArn: string
    :param AwsKmsKeyArn: The AWS Key Management Service (AWS KMS) key that you want to use with this pipeline.
            If you use either S3 or S3-AWS-KMS as your Encryption:Mode , you don't need to provide a key with your job because a default key, known as an AWS-KMS key, is created for you automatically. You need to provide an AWS-KMS key only if you want to use a non-default AWS-KMS key, or if you are using an Encryption:Mode of AES-PKCS7 , AES-CTR , or AES-GCM .
            

    :type Notifications: dict
    :param Notifications: The topic ARN for the Amazon Simple Notification Service (Amazon SNS) topic that you want to notify to report job status.
            Warning
            To receive notifications, you must also subscribe to the new topic in the Amazon SNS console.
            Progressing : The topic ARN for the Amazon Simple Notification Service (Amazon SNS) topic that you want to notify when Elastic Transcoder has started to process jobs that are added to this pipeline. This is the ARN that Amazon SNS returned when you created the topic.
            Completed : The topic ARN for the Amazon SNS topic that you want to notify when Elastic Transcoder has finished processing a job. This is the ARN that Amazon SNS returned when you created the topic.
            Warning : The topic ARN for the Amazon SNS topic that you want to notify when Elastic Transcoder encounters a warning condition. This is the ARN that Amazon SNS returned when you created the topic.
            Error : The topic ARN for the Amazon SNS topic that you want to notify when Elastic Transcoder encounters an error condition. This is the ARN that Amazon SNS returned when you created the topic.
            Progressing (string) --The Amazon Simple Notification Service (Amazon SNS) topic that you want to notify when Elastic Transcoder has started to process the job.
            Completed (string) --The Amazon SNS topic that you want to notify when Elastic Transcoder has finished processing the job.
            Warning (string) --The Amazon SNS topic that you want to notify when Elastic Transcoder encounters a warning condition.
            Error (string) --The Amazon SNS topic that you want to notify when Elastic Transcoder encounters an error condition.
            

    :type ContentConfig: dict
    :param ContentConfig: The optional ContentConfig object specifies information about the Amazon S3 bucket in which you want Elastic Transcoder to save transcoded files and playlists: which bucket to use, which users you want to have access to the files, the type of access you want users to have, and the storage class that you want to assign to the files.
            If you specify values for ContentConfig , you must also specify values for ThumbnailConfig .
            If you specify values for ContentConfig and ThumbnailConfig , omit the OutputBucket object.
            Bucket : The Amazon S3 bucket in which you want Elastic Transcoder to save transcoded files and playlists.
            Permissions (Optional): The Permissions object specifies which users you want to have access to transcoded files and the type of access you want them to have. You can grant permissions to a maximum of 30 users and/or predefined Amazon S3 groups.
            Grantee Type : Specify the type of value that appears in the Grantee object:
            Canonical : The value in the Grantee object is either the canonical user ID for an AWS account or an origin access identity for an Amazon CloudFront distribution. For more information about canonical user IDs, see Access Control List (ACL) Overview in the Amazon Simple Storage Service Developer Guide. For more information about using CloudFront origin access identities to require that users use CloudFront URLs instead of Amazon S3 URLs, see Using an Origin Access Identity to Restrict Access to Your Amazon S3 Content.
            Warning
            A canonical user ID is not the same as an AWS account number.
            Email : The value in the Grantee object is the registered email address of an AWS account.
            Group : The value in the Grantee object is one of the following predefined Amazon S3 groups: AllUsers , AuthenticatedUsers , or LogDelivery .
            Grantee : The AWS user or group that you want to have access to transcoded files and playlists. To identify the user or group, you can specify the canonical user ID for an AWS account, an origin access identity for a CloudFront distribution, the registered email address of an AWS account, or a predefined Amazon S3 group
            Access : The permission that you want to give to the AWS user that you specified in Grantee . Permissions are granted on the files that Elastic Transcoder adds to the bucket, including playlists and video files. Valid values include:
            READ : The grantee can read the objects and metadata for objects that Elastic Transcoder adds to the Amazon S3 bucket.
            READ_ACP : The grantee can read the object ACL for objects that Elastic Transcoder adds to the Amazon S3 bucket.
            WRITE_ACP : The grantee can write the ACL for the objects that Elastic Transcoder adds to the Amazon S3 bucket.
            FULL_CONTROL : The grantee has READ , READ_ACP , and WRITE_ACP permissions for the objects that Elastic Transcoder adds to the Amazon S3 bucket.
            StorageClass : The Amazon S3 storage class, Standard or ReducedRedundancy , that you want Elastic Transcoder to assign to the video files and playlists that it stores in your Amazon S3 bucket.
            Bucket (string) --The Amazon S3 bucket in which you want Elastic Transcoder to save the transcoded files. Specify this value when all of the following are true:
            You want to save transcoded files, thumbnails (if any), and playlists (if any) together in one bucket.
            You do not want to specify the users or groups who have access to the transcoded files, thumbnails, and playlists.
            You do not want to specify the permissions that Elastic Transcoder grants to the files.
            You want to associate the transcoded files and thumbnails with the Amazon S3 Standard storage class.
            If you want to save transcoded files and playlists in one bucket and thumbnails in another bucket, specify which users can access the transcoded files or the permissions the users have, or change the Amazon S3 storage class, omit OutputBucket and specify values for ContentConfig and ThumbnailConfig instead.
            StorageClass (string) --The Amazon S3 storage class, Standard or ReducedRedundancy , that you want Elastic Transcoder to assign to the video files and playlists that it stores in your Amazon S3 bucket.
            Permissions (list) --Optional. The Permissions object specifies which users and/or predefined Amazon S3 groups you want to have access to transcoded files and playlists, and the type of access you want them to have. You can grant permissions to a maximum of 30 users and/or predefined Amazon S3 groups.
            If you include Permissions , Elastic Transcoder grants only the permissions that you specify. It does not grant full permissions to the owner of the role specified by Role . If you want that user to have full control, you must explicitly grant full control to the user.
            If you omit Permissions , Elastic Transcoder grants full control over the transcoded files and playlists to the owner of the role specified by Role , and grants no other permissions to any other user or group.
            (dict) --The Permission structure.
            GranteeType (string) --The type of value that appears in the Grantee object:
            Canonical : Either the canonical user ID for an AWS account or an origin access identity for an Amazon CloudFront distribution.
            Warning
            A canonical user ID is not the same as an AWS account number.
            Email : The registered email address of an AWS account.
            Group : One of the following predefined Amazon S3 groups: AllUsers , AuthenticatedUsers , or LogDelivery .
            Grantee (string) --The AWS user or group that you want to have access to transcoded files and playlists. To identify the user or group, you can specify the canonical user ID for an AWS account, an origin access identity for a CloudFront distribution, the registered email address of an AWS account, or a predefined Amazon S3 group.
            Access (list) --The permission that you want to give to the AWS user that is listed in Grantee. Valid values include:
            READ : The grantee can read the thumbnails and metadata for thumbnails that Elastic Transcoder adds to the Amazon S3 bucket.
            READ_ACP : The grantee can read the object ACL for thumbnails that Elastic Transcoder adds to the Amazon S3 bucket.
            WRITE_ACP : The grantee can write the ACL for the thumbnails that Elastic Transcoder adds to the Amazon S3 bucket.
            FULL_CONTROL : The grantee has READ, READ_ACP, and WRITE_ACP permissions for the thumbnails that Elastic Transcoder adds to the Amazon S3 bucket.
            (string) --
            
            

    :type ThumbnailConfig: dict
    :param ThumbnailConfig: The ThumbnailConfig object specifies several values, including the Amazon S3 bucket in which you want Elastic Transcoder to save thumbnail files, which users you want to have access to the files, the type of access you want users to have, and the storage class that you want to assign to the files.
            If you specify values for ContentConfig , you must also specify values for ThumbnailConfig even if you don't want to create thumbnails.
            If you specify values for ContentConfig and ThumbnailConfig , omit the OutputBucket object.
            Bucket : The Amazon S3 bucket in which you want Elastic Transcoder to save thumbnail files.
            Permissions (Optional): The Permissions object specifies which users and/or predefined Amazon S3 groups you want to have access to thumbnail files, and the type of access you want them to have. You can grant permissions to a maximum of 30 users and/or predefined Amazon S3 groups.
            GranteeType : Specify the type of value that appears in the Grantee object:
            Canonical : The value in the Grantee object is either the canonical user ID for an AWS account or an origin access identity for an Amazon CloudFront distribution.
            Warning
            A canonical user ID is not the same as an AWS account number.
            Email : The value in the Grantee object is the registered email address of an AWS account.
            Group : The value in the Grantee object is one of the following predefined Amazon S3 groups: AllUsers , AuthenticatedUsers , or LogDelivery .
            Grantee : The AWS user or group that you want to have access to thumbnail files. To identify the user or group, you can specify the canonical user ID for an AWS account, an origin access identity for a CloudFront distribution, the registered email address of an AWS account, or a predefined Amazon S3 group.
            Access : The permission that you want to give to the AWS user that you specified in Grantee . Permissions are granted on the thumbnail files that Elastic Transcoder adds to the bucket. Valid values include:
            READ : The grantee can read the thumbnails and metadata for objects that Elastic Transcoder adds to the Amazon S3 bucket.
            READ_ACP : The grantee can read the object ACL for thumbnails that Elastic Transcoder adds to the Amazon S3 bucket.
            WRITE_ACP : The grantee can write the ACL for the thumbnails that Elastic Transcoder adds to the Amazon S3 bucket.
            FULL_CONTROL : The grantee has READ , READ_ACP , and WRITE_ACP permissions for the thumbnails that Elastic Transcoder adds to the Amazon S3 bucket.
            StorageClass : The Amazon S3 storage class, Standard or ReducedRedundancy , that you want Elastic Transcoder to assign to the thumbnails that it stores in your Amazon S3 bucket.
            Bucket (string) --The Amazon S3 bucket in which you want Elastic Transcoder to save the transcoded files. Specify this value when all of the following are true:
            You want to save transcoded files, thumbnails (if any), and playlists (if any) together in one bucket.
            You do not want to specify the users or groups who have access to the transcoded files, thumbnails, and playlists.
            You do not want to specify the permissions that Elastic Transcoder grants to the files.
            You want to associate the transcoded files and thumbnails with the Amazon S3 Standard storage class.
            If you want to save transcoded files and playlists in one bucket and thumbnails in another bucket, specify which users can access the transcoded files or the permissions the users have, or change the Amazon S3 storage class, omit OutputBucket and specify values for ContentConfig and ThumbnailConfig instead.
            StorageClass (string) --The Amazon S3 storage class, Standard or ReducedRedundancy , that you want Elastic Transcoder to assign to the video files and playlists that it stores in your Amazon S3 bucket.
            Permissions (list) --Optional. The Permissions object specifies which users and/or predefined Amazon S3 groups you want to have access to transcoded files and playlists, and the type of access you want them to have. You can grant permissions to a maximum of 30 users and/or predefined Amazon S3 groups.
            If you include Permissions , Elastic Transcoder grants only the permissions that you specify. It does not grant full permissions to the owner of the role specified by Role . If you want that user to have full control, you must explicitly grant full control to the user.
            If you omit Permissions , Elastic Transcoder grants full control over the transcoded files and playlists to the owner of the role specified by Role , and grants no other permissions to any other user or group.
            (dict) --The Permission structure.
            GranteeType (string) --The type of value that appears in the Grantee object:
            Canonical : Either the canonical user ID for an AWS account or an origin access identity for an Amazon CloudFront distribution.
            Warning
            A canonical user ID is not the same as an AWS account number.
            Email : The registered email address of an AWS account.
            Group : One of the following predefined Amazon S3 groups: AllUsers , AuthenticatedUsers , or LogDelivery .
            Grantee (string) --The AWS user or group that you want to have access to transcoded files and playlists. To identify the user or group, you can specify the canonical user ID for an AWS account, an origin access identity for a CloudFront distribution, the registered email address of an AWS account, or a predefined Amazon S3 group.
            Access (list) --The permission that you want to give to the AWS user that is listed in Grantee. Valid values include:
            READ : The grantee can read the thumbnails and metadata for thumbnails that Elastic Transcoder adds to the Amazon S3 bucket.
            READ_ACP : The grantee can read the object ACL for thumbnails that Elastic Transcoder adds to the Amazon S3 bucket.
            WRITE_ACP : The grantee can write the ACL for the thumbnails that Elastic Transcoder adds to the Amazon S3 bucket.
            FULL_CONTROL : The grantee has READ, READ_ACP, and WRITE_ACP permissions for the thumbnails that Elastic Transcoder adds to the Amazon S3 bucket.
            (string) --
            
            

    :rtype: dict
    :return: {
        'Pipeline': {
            'Id': 'string',
            'Arn': 'string',
            'Name': 'string',
            'Status': 'string',
            'InputBucket': 'string',
            'OutputBucket': 'string',
            'Role': 'string',
            'AwsKmsKeyArn': 'string',
            'Notifications': {
                'Progressing': 'string',
                'Completed': 'string',
                'Warning': 'string',
                'Error': 'string'
            },
            'ContentConfig': {
                'Bucket': 'string',
                'StorageClass': 'string',
                'Permissions': [
                    {
                        'GranteeType': 'string',
                        'Grantee': 'string',
                        'Access': [
                            'string',
                        ]
                    },
                ]
            },
            'ThumbnailConfig': {
                'Bucket': 'string',
                'StorageClass': 'string',
                'Permissions': [
                    {
                        'GranteeType': 'string',
                        'Grantee': 'string',
                        'Access': [
                            'string',
                        ]
                    },
                ]
            }
        },
        'Warnings': [
            {
                'Code': 'string',
                'Message': 'string'
            },
        ]
    }
    
    
    :returns: 
    Active : The pipeline is processing jobs.
    Paused : The pipeline is not currently processing jobs.
    
    """
    pass

def update_pipeline_notifications(Id=None, Notifications=None):
    """
    With the UpdatePipelineNotifications operation, you can update Amazon Simple Notification Service (Amazon SNS) notifications for a pipeline.
    When you update notifications for a pipeline, Elastic Transcoder returns the values that you specified in the request.
    See also: AWS API Documentation
    
    
    :example: response = client.update_pipeline_notifications(
        Id='string',
        Notifications={
            'Progressing': 'string',
            'Completed': 'string',
            'Warning': 'string',
            'Error': 'string'
        }
    )
    
    
    :type Id: string
    :param Id: [REQUIRED]
            The identifier of the pipeline for which you want to change notification settings.
            

    :type Notifications: dict
    :param Notifications: [REQUIRED]
            The topic ARN for the Amazon Simple Notification Service (Amazon SNS) topic that you want to notify to report job status.
            Warning
            To receive notifications, you must also subscribe to the new topic in the Amazon SNS console.
            Progressing : The topic ARN for the Amazon Simple Notification Service (Amazon SNS) topic that you want to notify when Elastic Transcoder has started to process jobs that are added to this pipeline. This is the ARN that Amazon SNS returned when you created the topic.
            Completed : The topic ARN for the Amazon SNS topic that you want to notify when Elastic Transcoder has finished processing a job. This is the ARN that Amazon SNS returned when you created the topic.
            Warning : The topic ARN for the Amazon SNS topic that you want to notify when Elastic Transcoder encounters a warning condition. This is the ARN that Amazon SNS returned when you created the topic.
            Error : The topic ARN for the Amazon SNS topic that you want to notify when Elastic Transcoder encounters an error condition. This is the ARN that Amazon SNS returned when you created the topic.
            Progressing (string) --The Amazon Simple Notification Service (Amazon SNS) topic that you want to notify when Elastic Transcoder has started to process the job.
            Completed (string) --The Amazon SNS topic that you want to notify when Elastic Transcoder has finished processing the job.
            Warning (string) --The Amazon SNS topic that you want to notify when Elastic Transcoder encounters a warning condition.
            Error (string) --The Amazon SNS topic that you want to notify when Elastic Transcoder encounters an error condition.
            

    :rtype: dict
    :return: {
        'Pipeline': {
            'Id': 'string',
            'Arn': 'string',
            'Name': 'string',
            'Status': 'string',
            'InputBucket': 'string',
            'OutputBucket': 'string',
            'Role': 'string',
            'AwsKmsKeyArn': 'string',
            'Notifications': {
                'Progressing': 'string',
                'Completed': 'string',
                'Warning': 'string',
                'Error': 'string'
            },
            'ContentConfig': {
                'Bucket': 'string',
                'StorageClass': 'string',
                'Permissions': [
                    {
                        'GranteeType': 'string',
                        'Grantee': 'string',
                        'Access': [
                            'string',
                        ]
                    },
                ]
            },
            'ThumbnailConfig': {
                'Bucket': 'string',
                'StorageClass': 'string',
                'Permissions': [
                    {
                        'GranteeType': 'string',
                        'Grantee': 'string',
                        'Access': [
                            'string',
                        ]
                    },
                ]
            }
        }
    }
    
    
    :returns: 
    Active : The pipeline is processing jobs.
    Paused : The pipeline is not currently processing jobs.
    
    """
    pass

def update_pipeline_status(Id=None, Status=None):
    """
    The UpdatePipelineStatus operation pauses or reactivates a pipeline, so that the pipeline stops or restarts the processing of jobs.
    Changing the pipeline status is useful if you want to cancel one or more jobs. You can't cancel jobs after Elastic Transcoder has started processing them; if you pause the pipeline to which you submitted the jobs, you have more time to get the job IDs for the jobs that you want to cancel, and to send a  CancelJob request.
    See also: AWS API Documentation
    
    
    :example: response = client.update_pipeline_status(
        Id='string',
        Status='string'
    )
    
    
    :type Id: string
    :param Id: [REQUIRED]
            The identifier of the pipeline to update.
            

    :type Status: string
    :param Status: [REQUIRED]
            The desired status of the pipeline:
            Active : The pipeline is processing jobs.
            Paused : The pipeline is not currently processing jobs.
            

    :rtype: dict
    :return: {
        'Pipeline': {
            'Id': 'string',
            'Arn': 'string',
            'Name': 'string',
            'Status': 'string',
            'InputBucket': 'string',
            'OutputBucket': 'string',
            'Role': 'string',
            'AwsKmsKeyArn': 'string',
            'Notifications': {
                'Progressing': 'string',
                'Completed': 'string',
                'Warning': 'string',
                'Error': 'string'
            },
            'ContentConfig': {
                'Bucket': 'string',
                'StorageClass': 'string',
                'Permissions': [
                    {
                        'GranteeType': 'string',
                        'Grantee': 'string',
                        'Access': [
                            'string',
                        ]
                    },
                ]
            },
            'ThumbnailConfig': {
                'Bucket': 'string',
                'StorageClass': 'string',
                'Permissions': [
                    {
                        'GranteeType': 'string',
                        'Grantee': 'string',
                        'Access': [
                            'string',
                        ]
                    },
                ]
            }
        }
    }
    
    
    :returns: 
    Active : The pipeline is processing jobs.
    Paused : The pipeline is not currently processing jobs.
    
    """
    pass

