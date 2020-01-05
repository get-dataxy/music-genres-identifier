import os
import sys
import logging
import pandas as pd
import librosa as lb
import librosa.display
import matplotlib.pyplot as plt
import warnings

from pathlib import Path


class Mgi:
    name = "MGI"

    def __init__(self, spath, mpath, dpath='./data', use_abs=False, log_level=logging.INFO, log_format=None, warnings_suppress=True):
        self.df = None
        self.songs_pth = []
        self.format = log_format
        self.warnings_suppress = warnings_suppress
        self.logger = self._set_logger_level(log_level, warnings_suppress)
        self._set_paths(spath, mpath, dpath, use_abs)

    def _set_paths(self, spath, mpath, dpath, use_abs):
        if use_abs:
            self.spath = os.path.abspath(spath)
            self.mpath = os.path.abspath(mpath)
            self.dpath = os.path.abspath(dpath)
        else:
            self.spath = spath
            self.mpath = mpath
            self.dpath = dpath
        self.spectogram_path = '{}/{}'.format(self.dpath, 'spectogram')

    def _set_logger_level(self, log_level, warnings_suppress):
        if self.format is None:
            self.format = '[%(levelname)-8s] :: [%(name)s ] :: %(message)s'
        logging.basicConfig(stream=sys.stdout, level=log_level, format=self.format, datefmt=None)
        logger = logging.getLogger(self.name)
        logging.captureWarnings(capture=True)
        if warnings_suppress:
            warnings.filterwarnings("ignore")
        logger.setLevel(log_level)
        return logger

    def _is_valid_path(self, path):
        if not os.path.exists(path):
            self.logger.error("Invalid path: {}".format(path))
            return False
        return True

    def _isfile(self, fpath):
        if not self._is_valid_path(fpath):
            return False
        if os.path.isfile(fpath):
            return True
        self.logger.error("Invalid file path: {}".format(fpath))
        return False
    
    def _create_if_not_exist(self, dpath):
        if not self._is_valid_path(dpath):
            self.logger.debug("dpath: {} doesn't exist".format(dpath))
            Path(dpath).mkdir(parents=True, exist_ok=True)
            self.logger.debug("dpath: {} created".format(dpath))

    def read_metadata(self, filename):
        self.logger.debug("Checking the metadata path valid or not")
        if not self._is_valid_path(self.mpath):
            self.logger.error("Exiting")
            return

        self.logger.debug("Checking csv file")
        file_path = '{}/{}'.format(self.mpath, filename)
        if not self._isfile(file_path):
            self.logger.error("Exiting")
            return

        self.logger.info("Reading metadata using pandas")
        self.df = pd.read_csv(file_path, header=None, error_bad_lines=False)

    def mini_meta(self):
        # Expecting the enduser will override this method based on there need
        # TODO: need to collect the important columns from full metadata.
        pass

    def songs(self, path, songs_type='.mp3'):
        for dirpath, subdirs, files in os.walk(path):
            self.songs_pth.extend(os.path.join(dirpath, x) for x in files if x.endswith(songs_type))

    def read_songs(self, format='wav'):
        self.logger.debug("Checking the songs path valid or not")
        if not self._is_valid_path(self.mpath):
            self.logger.error("Exiting")
            return

        # creating the data folder if not exist..!
        self._create_if_not_exist(self.dpath)
        self.logger.info("Reading songs using librosa")
        self.songs(self.spath)

        # creating the spectogram if not exist..!
        self._create_if_not_exist(self.spectogram_path)

        for each_song_path in self.songs_pth:
            self.logger.debug(each_song_path)
            y, sr = lb.load(each_song_path)
            melspectrogram_ndarray = librosa.feature.melspectrogram(y=y, sr=sr, n_mels=128,fmax=8000)
            print(type(melspectrogram_ndarray))
            break
            # TODO: need to read the librosa files
            # TODO: need to store the chromagrams

def main(songs_path, metadata_path):
    csv_file = 'tracks.csv'
    obj = Mgi(songs_path, metadata_path, log_level=logging.DEBUG)
    obj.read_metadata(csv_file)
    obj.read_songs(format='mp3')


if __name__ == "__main__":
    spath = r'./data/fma_small'
    mpath = r'./data/fma_metadata'
    main(spath, mpath)