#!/usr/bin/env python

# Copyright 2018 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import os

import automl_translation_predict

project_id = os.environ["GCLOUD_PROJECT"]
compute_region = "us-central1"


def test_predict(capsys):
    model_id = "3128559826197068699"
    automl_translation_predict.predict(
        project_id, compute_region, model_id, "resources/input.txt"
    )
    out, _ = capsys.readouterr()
    assert "Translated content: " in out
