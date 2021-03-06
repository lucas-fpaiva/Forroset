# -*- coding: utf-8 -*-

## Importing Required Libraries
import requests
import urllib.request
import re
from bs4 import BeautifulSoup
import pandas as pd
from time import sleep
import os

def getMusics(forroset, mp3folder):
  """ Downloads the mp3 files provided by Spotify
      * forroset: path to the location of the forroset file(string)
      * mp3folder: destination folder path for downloaded files(string)
  """
  ## Accessing dataset
  forroset = pd.read_csv(forroset)
  ## Listing identifiers
  ids = forroset['track_id']
  ## Checking if there are songs in the directory
  mp3_files = os.listdir(mp3folder)
  downloaded_musics = []
  undownloaded = []
  for element in mp3_files:
    downloaded_musics.append(element.split(".")[0])
  for music in ids:
    if music not in downloaded_musics:
      undownloaded.append(music)
  ## Downloading songs
  for i in range(len(undownloaded)):
    try:
      r = requests.get(forroset.loc[ids == undownloaded[i]].preview_url.tolist()[0])
      sleep(0.5)
      soup = BeautifulSoup(r.content, 'html.parser')
      with open((mp3folder+'/{}.mp3').format(undownloaded[i]), 'wb') as f:
          f.write(r.content)
    except:
      pass
  ## Checking which songs have not been downloaded
  undownloaded_dict ={}
  mp3_files = os.listdir(mp3folder)
  for element in mp3_files:
    downloaded_musics.append(element.split(".")[0])
  for music in ids:
    if music not in downloaded_musics:
      undownloaded_dict[music] = forroset.loc[ids == music].preview_url.tolist()[0]
  keys = undownloaded_dict.keys()
  ## Print music list to be downloaded manually
  print("List of not downloaded songs")
  c = 0
  for key in undownloaded_dict.keys():
    c+=1
    print("{} --- Link: {} --- Identifier: {}".format(c, undownloaded_dict[key], key))
