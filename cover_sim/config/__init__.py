"""Typed configuration loading and validation."""

from .loader import ConfigError, CoverConfig, load_config, pending_parameters
from .sources import SourceManifest, load_source_manifest

__all__ = ["ConfigError", "CoverConfig", "load_config", "pending_parameters",
           "SourceManifest", "load_source_manifest"]
