import os
import sys
import logging
import pandas as pd


class Mgi:
    name = "MGI"

    def __init__(self, spath, mpath, dpath='./data', log_level=logging.INFO, log_format=None):
        self.spath = spath
        self.mpath = mpath
        self.dpath = dpath
        self.df = None
        self.songs_pth = []
        self.format = log_format
        self.logger = self.set_logger_level(log_level)

    def set_logger_level(self, log_level):
        if self.format is None:
            self.format = '[ %(levelname)s ] :: [ %(name)s ] :: %(message)s'
        logging.basicConfig(stream=sys.stdout, level=log_level, format=self.format, datefmt=None)
        logger = logging.getLogger(self.name)
        logger.setLevel(log_level)
        return logger

    def _is_valid_path(self, path):
        if not os.path.exists(self.mpath):
            self.logger.error("Invalid path: {}".format(self.mpath))
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
            # TODO: create the dpath
            pass

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

    def songs(self, path, songs_type='.mp3'):
        for dirpath, subdirs, files in os.walk(path):
            self.songs_pth.extend(os.path.join(dirpath, x) for x in files if x.endswith(songs_type))

    def read_songs(self, format='wav'):
        self.logger.debug("Checking the songs path valid or not")
        if not self._is_valid_path(self.mpath):
            self.logger.error("Exiting")
            return

        self._create_if_not_exist(self.dpath)
        self.logger.info("Reading songs using librosa")
        self.songs(self.spath)
        for each in self.songs_pth:
            print(each)
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