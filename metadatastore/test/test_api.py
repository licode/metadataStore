# Smoketest the api

from metadatastore.api import find_events
from metadatastore.api import find_descriptors
from metadatastore.api import find_run_starts
from metadatastore.api import find_runstops
from metadatastore.api import find_last
from metadatastore.api import insert_event
from metadatastore.api import insert_descriptor
from metadatastore.api import insert_run_start
from metadatastore.api import insert_runstop
from metadatastore.api import db_connect
from metadatastore.api import db_disconnect


if __name__ == "__main__":
    import nose
    nose.runmodule(argv=['-s', '--with-doctest'], exit=False)
