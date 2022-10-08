from __future__ import annotations

import os
import pytest

from jupyter_nb_double_quote_to_single_quote._main import main


THIS_FILE_DIR = os.path.abspath(os.path.dirname(__file__))
RESOURCE_DIR = os.path.join(THIS_FILE_DIR, 'resources')


TESTS = (
    ('jupyter_case_1_before.ipynb', 'jupyter_case_1_after.ipynb', 1),
    # the file in Case 2 is not altered, so we reload the same file
    ('jupyter_case_2.ipynb', 'jupyter_case_2.ipynb', 0),
)


@pytest.mark.parametrize(('input_file', 'output_file', 'expected_retv'), TESTS)
def test_rewrite(input_file, output_file, expected_retv, tmpdir):
    with open(os.path.join(RESOURCE_DIR, input_file)) as fp:
        before_contents = fp.read()

    with open(os.path.join(RESOURCE_DIR, output_file)) as fp:
        after_contents = fp.read()

    path = tmpdir.join('file.ipynb')
    path.write(before_contents)
    retval = main([str(path)])
    assert path.read() == after_contents
    assert retval == expected_retv
