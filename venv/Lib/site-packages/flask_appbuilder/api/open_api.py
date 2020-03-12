from typing import Dict, Optional
import logging
import yaml


log = logging.getLogger(__name__)


class OpenApiDocManager:

    def __init__(self, filename: str):
        self._filename = filename
        with open(self._filename, 'r') as stream:
            try:
                self._docs = yaml.safe_load(stream)
            except yaml.YAMLError as exc:
                log.error("Invalid OpenAPI spec file: {exc}")

    def get_method(self, name: str, method: str) -> Optional[Dict]:
        try:
            return self._docs[name][method]
        except KeyError:
            return None
