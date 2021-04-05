# sy402_lab08
Software that will detect changes across the filesystem by hashing all files across the VM.

I stored the data in the hash data file by sha256 encrypting all the files through os.walk. Following this, I hashed each file and wrote it to the output file.
