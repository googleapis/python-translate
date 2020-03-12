# Copyright 2020 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import os
import translate_v3_create_glossary
import translate_v3_delete_glossary
import uuid

PROJECT_ID = os.environ["GCLOUD_PROJECT"]
GLOSSARY_INPUT_URI = "gs://cloud-samples-data/translation/glossary_ja.csv"


def test_create_glossary(capsys):
    glossary_id = "test-{}".format(uuid.uuid4())
    translate_v3_create_glossary.create_glossary(
        PROJECT_ID, GLOSSARY_INPUT_URI, glossary_id
    )
    out, _ = capsys.readouterr()
    # assert
    assert "Created:" in out
    assert "gs://cloud-samples-data/translation/glossary_ja.csv" in out

    # clean up after use
    try:
        translate_v3_delete_glossary.delete_glossary(PROJECT_ID, glossary_id)
    except Exception:
        pass
