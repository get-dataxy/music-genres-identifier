import os
import sys
import logging


class Mgi:
    name = "MGI"

    def __init__(self, spath, mpath, log_level=logging.INFO, log_format=None):
        self.spath = spath
        self.mpath = mpath
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

    def read_songs(self, format='wav'):
        self.logger.debug("Checking the songs path valid or not")
        if not self._is_valid_path(self.mpath):
            self.logger.error("Exiting")
            return

        self.logger.info("Reading songs using librosa")

def main(songs_path, metadata_path):
    csv_file = 'tracks.csv'
    obj = Mgi(songs_path, metadata_path, log_level=logging.DEBUG)
    obj.read_metadata(csv_file)
    obj.read_songs(format='mp3')


if __name__ == "__main__":
    spath = r'./data/fma_small'
    mpath = r'./data/fma_metadata'
    main(spath, mpath)