import zipfile


def extract_archive(archivepath, dest_dir): 

    with zipfile.ZipFile(archivepath, 'r') as archive:
        archive.extractall(dest_dir)

if __name__ == "__main__":
    extract_archive(
        r"D:\porgram\code\mega corse\compress_zip\compressed.zip",
        r"D:\porgram\code\mega corse\Extract"
    )
