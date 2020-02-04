# Copyright 2020 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# [START translate_v3_get_supported_languages]
from google.cloud import translate


def sample_get_supported_languages(project_id="YOUR_PROJECT_ID"):
    """Getting a list of supported language codes."""

    client = translate.TranslationServiceClient()

    parent = client.location_path(project_id, "global")

    response = client.get_supported_languages(parent=parent)

    # List language codes of supported languages.
    print("Supported Languages:")
    for language in response.languages:
        print(u"Language Code: {}".format(language.language_code))


# [END translate_v3_get_supported_languages]
