import os

from autowebcompat import utils


def test_labels():
    labels = utils.read_labels()
    for label in labels:
        for browser in ['firefox', 'chrome']:
            assert os.path.join('data', '{}_{}.png'.format(label, browser))


def test_validate_labels():
    labels = utils.read_labels()
    for label in labels.values():
        assert label in ['y', 'n', 'd']
