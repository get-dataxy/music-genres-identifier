# FMA: A Dataset For Music Analysis

The dataset is a dump of the [Free Music Archive (FMA)](https://freemusicarchive.org/), an interactive library of high-quality, legal audio downloads. Below the abstract from the [paper](https://arxiv.org/abs/1612.01840).

## Data

Audio data:

- [fma_small.zip](https://os.unil.cloud.switch.ch/fma/fma_small.zip): 8,000 tracks of 30s, 8 balanced genres (GTZAN-like) (7.2 GiB)
- [fma_medium.zip](https://os.unil.cloud.switch.ch/fma/fma_medium.zip): 25,000 tracks of 30s, 16 unbalanced genres (22 GiB)
- [fma_large.zip](https://os.unil.cloud.switch.ch/fma/fma_large.zip): 106,574 tracks of 30s, 161 unbalanced genres (93 GiB)
- [fma_full.zip](https://os.unil.cloud.switch.ch/fma/fma_full.zip): 106,574 untrimmed tracks, 161 unbalanced genres (879 GiB)

Metadata:

- [fma_metadata.zip](https://os.unil.cloud.switch.ch/fma/fma_metadata.zip) (342 MiB), contains

  - tracks.csv: per track metadata such as ID, title, artist, genres, tags and play counts, for all 106,574 tracks.
  - genres.csv: all 163 genre IDs with their name and parent (used to infer the genre hierarchy and top-level genres).
  - features.csv: common features extracted with librosa.
  - echonest.csv: audio features provided by Echonest (now Spotify) for a subset of 13,129 tracks.

## How to use

- Download and extract the data and metadata from the above
- The folder structure needs to be like

```cmd
music-genres-identifier\
    |--- data\
       |--- fma_small\
          |--- 000\
              |--- 0000002.mp3
              ...
       |--- fma_metadata\
          |--- features.csv
          ...
```

## Reference

[https://github.com/mdeff/fma](https://github.com/mdeff/fma)
