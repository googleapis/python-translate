import os
import pathlib
import sys
import collections
from timeit import default_timer as timer


import pytest

os.environ['GOOGLE_CLOUD_PROJECT'] = 'python-docs-samples-tests'

def flaky_test_diagnostic(file_name, test_name, N=20):

  timing_dict = collections.defaultdict(list)
  for ri in range(N):
    start = timer()
    result = pytest.main(['-s', f'{file_name}::{test_name}'])
    end = timer()
    delta = end-start
    if result == pytest.ExitCode.OK:
      timing_dict['SUCCESS'].append(delta)
    else:
      timing_dict['FAILURE'].append(delta)

  return timing_dict

# Run test in snippets directory:
dir_of_curr_file = os.path.dirname(__file__)
helper_filepath = pathlib.Path(dir_of_curr_file)#.parent / 'samples' / 'snippets'
sys.path.append(helper_filepath.resolve().as_posix())
os.chdir(helper_filepath.resolve())


# Settings:
file_name = 'hybrid_tutorial_test.py'
test_name = 'test_translate_glossary'
timing_dict = flaky_test_diagnostic(file_name, test_name, N=5)

for key, delta_list in timing_dict.items():
  mean_time = sum(delta_list)/len(delta_list)
  max_time = max(delta_list)
  min_time = min(delta_list)
  report_string = f'Result: {key}, mean={mean_time:3.2f}, min={min_time:3.2f}, max={max_time:3.2f}, count={len(delta_list)}'
  print(report_string)