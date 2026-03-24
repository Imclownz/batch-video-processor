import logging
import json

class Logger:
    @staticmethod
    def setup_logging(log_file='app.log'):
        logging.basicConfig(level=logging.INFO,
            format='%(asctime)s - %(levelname)s - %(message)s',
            handlers=[
                logging.FileHandler(log_file),
                logging.StreamHandler()
            ])

class ConfigLoader:
    @staticmethod
    def load_config(config_file='config.json'):
        with open(config_file, 'r') as file:
            config = json.load(file)
        return config

class SubtitleHandler:
    @staticmethod
    def load_subtitles(sub_file):
        # Placeholder for loading subtitles
        pass

    @staticmethod
    def process_subtitles(sub_file):
        # Placeholder for processing subtitles
        pass

# Example usage
if __name__ == '__main__':
    Logger.setup_logging()
    logging.info('Logger is set up.')