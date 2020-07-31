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

# [START translate_v3_get_supported_languages_for_target]
from google.cloud import translate


def get_supported_languages_with_target(project_id="YOUR_PROJECT_ID"):
    """Listing supported languages with target language name."""

    client = translate.TranslationServiceClient()
    parent = client.location_path(project_id, "global")

    # Supported language codes: https://cloud.google.com/translate/docs/languages
    response = client.get_supported_languages(
        display_language_code="is",  # target language code
        parent=parent
    )
    # List language codes of supported languages
    for language in response.languages:
        print(u"Language Code: {}".format(language.language_code))
        print(u"Display Name: {}".format(language.display_name))

# [END translate_v3_get_supported_languages_for_target]
