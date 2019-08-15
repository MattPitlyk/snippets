def unzip_s3_obj_to_dict(s3_obj, decode='utf-8') -> Dict[str, str]:
    """Unzip the body of an S3 object into a dict of filenmae -> contents."""
    filename_to_contents = {}
    with io.BytesIO(s3_obj.get('Body').read()) as tf:
        # rewind the file
        tf.seek(0)

        # Read the file as a zipfile and process the members
        with zipfile.ZipFile(tf, mode='r') as zipf:
            for subfile in [fn for fn in zipf.namelist() if not fn.startswith('__MAC')]:
                with zipf.open(subfile) as f:
                    if decode:
                        filename_to_contents[subfile] = f.read().decode(decode)
                    else:
                        filename_to_contents[subfile] = f.read()
    return filename_to_contents
    
    
def unzip_to_dict(file, decode='utf-8') -> Dict[str, str]:
    """Unzip a file-like object into a dict of filenmae -> contents."""
    filename_to_contents = {}
    with io.BytesIO(file.read()) as tf:
        # rewind the file
        tf.seek(0)

        # Read the file as a zipfile and process the members
        with zipfile.ZipFile(tf, mode='r') as zipf:
            for subfile in [fn for fn in zipf.namelist() if not fn.startswith('__MAC')]:
                with zipf.open(subfile) as f:
                    if decode:
                        filename_to_contents[subfile] = f.read().decode(decode)
                    else:
                        filename_to_contents[subfile] = f.read()
    return filename_to_contents
