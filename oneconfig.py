import os
import torch

GLOBAL_CONFIG = {
            "USE_CUDE_IF_AVAILABLE": True,
            "ROUND_DIGIT": 6
        }


URL_SPM_MODEL="https://vandanresearch.sgp1.digitaloceanspaces.com/models-onemt2.5/IL2ILEN_June7_2024.model"
URL_ONEMT_MODEL="https://vandanresearch.sgp1.digitaloceanspaces.com/models-onemt2.5/checkpoint17.pt"
URL_SDIC="https://vandanresearch.sgp1.digitaloceanspaces.com/models-onemt2.5/dict.SRC.txt"
URL_TDIC="https://vandanresearch.sgp1.digitaloceanspaces.com/models-onemt2.5/dict.TGT.txt"

SUBWORD_MODEL_PATH="models/IL2ILEN_June7_2024.model"
TRANSLATION_MODEL_FOLDER="models/"
TRANSLATION_MODEL_PATH="models/checkpoint17.pt"

language_mapping = {
    "doi": "doi_Deva",
    "hin": "hin_Deva",
    "kan": "kan_Knda",
    "kas": "kas_Arab",
    "kas_deva": "kas_Deva",
    "snd": "snd_Arab",
    "snd_deva": "snd_Deva",
    "eng": "eng_Latn"
}

#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Environment specific config, or overwrite of GLOBAL_CONFIG
ENV_CONFIG = {
    "development": {
        "DEBUG": True
    },

    "staging": {
        "DEBUG": True
    },

    "production": {
        "DEBUG": False,
        "ROUND_DIGIT": 3
    }
}


def get_config() -> dict:
    """
    Get config based on running environment

    :return: dict of config
    """

    # Determine running environment
    ENV = os.environ['PYTHON_ENV'] if 'PYTHON_ENV' in os.environ else 'development'
    ENV = ENV or 'development'

    # raise error if environment is not expected
    if ENV not in ENV_CONFIG:
        raise EnvironmentError(f'Config for envirnoment {ENV} not found')

    config = GLOBAL_CONFIG.copy()
    config.update(ENV_CONFIG[ENV])

    config['ENV'] = ENV
    config['DEVICE'] = 'cuda' if torch.cuda.is_available() and config['USE_CUDE_IF_AVAILABLE'] else 'cpu'

    return config

# load config for import
CONFIG = get_config()

if __name__ == '__main__':
    # for debugging
    import json
    print(json.dumps(CONFIG, indent=4))
