"""Shared import plumbing for the test suite.

Both comic tools live outside a package, so the modules under test are imported by
path. Keeping that in one place means the tests themselves stay readable.
"""
import os
import sys

TESTS_DIR = os.path.dirname(os.path.abspath(__file__))
GENERATOR_DIR = os.path.dirname(TESTS_DIR)
CREATOR_DIR = os.path.join(os.path.dirname(GENERATOR_DIR), 'comic_volume_creator')

LIBRARY_ROOT = '/mnt/extramedia/Comics'
BASELINE_FILE = os.path.join(TESTS_DIR, 'baseline_series_keys.json')


def load_generator():
    """Import matching_analysis_generator. Safe: it is guarded by __main__."""
    if GENERATOR_DIR not in sys.path:
        sys.path.insert(0, GENERATOR_DIR)
    import matching_analysis_generator
    return matching_analysis_generator


def load_mover():
    """Import comic_mover. Safe: it is guarded by __main__."""
    if GENERATOR_DIR not in sys.path:
        sys.path.insert(0, GENERATOR_DIR)
    import comic_mover
    return comic_mover


def load_serve_v2():
    """Import serve_v2. Safe: it is guarded by __main__, so no port is bound."""
    if GENERATOR_DIR not in sys.path:
        sys.path.insert(0, GENERATOR_DIR)
    import serve_v2
    return serve_v2


def load_release():
    """Import release — the filename parser the generator derives series names with."""
    if GENERATOR_DIR not in sys.path:
        sys.path.insert(0, GENERATOR_DIR)
    import release
    return release


def load_creator():
    """Import comic_volume_creator_server, or return None if it is not present.

    Lives in a sibling repo, so the suite must still run without it.
    """
    if CREATOR_DIR not in sys.path:
        sys.path.insert(0, CREATOR_DIR)
    try:
        import comic_volume_creator_server
        return comic_volume_creator_server
    except ImportError:
        return None


def library_items():
    """Base-level entries of the library. One level only, by design."""
    return sorted(e.name for e in os.scandir(LIBRARY_ROOT))
