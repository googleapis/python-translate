# Copyright 2020 Google LLC
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


# [START translate_v3_batch_translate_text_with_model]
from google.cloud import translate


def batch_translate_text_with_model(
    input_uri="gs://YOUR_BUCKET_ID/path/to/your/file.txt",
    output_uri="gs://YOUR_BUCKET_ID/path/to/save/results/",
    project_id="YOUR_PROJECT_ID",
    model_id="YOUR_MODEL_ID",
):
    """Batch translate text using Translation model.
     Model can be AutoML or General[built-in] model. """

    client = translate.TranslationServiceClient()

    # Supported file types: https://cloud.google.com/translate/docs/supported-formats
    gcs_source = {"input_uri": input_uri}
    location = "us-central1"

    input_configs_element = {
        "gcs_source": gcs_source,
        "mime_type": "text/plain"  # Can be "text/plain" or "text/html".
    }
    gcs_destination = {"output_uri_prefix": output_uri}
    output_config = {"gcs_destination": gcs_destination}
    parent = client.location_path(project_id, location)

    model_path = "projects/{}/locations/{}/models/{}".format(
        project_id, location, model_id  # The location of AutoML model.
    )

    # Supported language codes: https://cloud.google.com/translate/docs/languages
    models = {"ja": model_path}  # takes a target lang as key.

    operation = client.batch_translate_text(
        parent=parent,
        source_language_code="en",
        target_language_codes=["ja"],  # Up to 10 language codes here.
        input_configs=[input_configs_element],
        output_config=output_config,
        models=models,
    )

    print(u"Waiting for operation to complete...")
    response = operation.result()

    # Display the translation for each input text provided.
    print(u"Total Characters: {}".format(response.total_characters))
    print(u"Translated Characters: {}".format(response.translated_characters))


# [END translate_v3_batch_translate_text_with_model]
