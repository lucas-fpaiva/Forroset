# Users section

In this directory are available the Forroset files, dataset visualization codes and the auxiliary code to download the MP3 files.

## Download the MP3 files
To download the mp3 files correctly, follow these instructions:

1. Download Forroset.
2. Create a empty folder to store the mp3 files.
3. Use the function `getMusics(forroset,mp3folder)`.
    1. The first parameter must be a *string* containing the path to the forroset csv file.
    2. The second parameter must be a *string* containing the path to the destination folder of the MP3 files.
4. If some files may not download automatically.
    1. A list containing their download links and their unique identifiers will be printed at the end of the code execution.
    2. Access the provided URLs and download the files manually.
    3. To avoid identification problems, rename the downloaded files to their unique identifiers provided.
5. If the download process is interrupted, just call the `getMusics()` function again with the same parameters as before.