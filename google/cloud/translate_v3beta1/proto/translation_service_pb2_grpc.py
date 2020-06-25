# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from google.cloud.translate_v3beta1.proto import (
    translation_service_pb2 as google_dot_cloud_dot_translate__v3beta1_dot_proto_dot_translation__service__pb2,
)
from google.longrunning import (
    operations_pb2 as google_dot_longrunning_dot_operations__pb2,
)


class TranslationServiceStub(object):
    """Proto file for the Cloud Translation API (v3beta1).

    Provides natural language translation operations.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.TranslateText = channel.unary_unary(
            "/google.cloud.translation.v3beta1.TranslationService/TranslateText",
            request_serializer=google_dot_cloud_dot_translate__v3beta1_dot_proto_dot_translation__service__pb2.TranslateTextRequest.SerializeToString,
            response_deserializer=google_dot_cloud_dot_translate__v3beta1_dot_proto_dot_translation__service__pb2.TranslateTextResponse.FromString,
        )
        self.DetectLanguage = channel.unary_unary(
            "/google.cloud.translation.v3beta1.TranslationService/DetectLanguage",
            request_serializer=google_dot_cloud_dot_translate__v3beta1_dot_proto_dot_translation__service__pb2.DetectLanguageRequest.SerializeToString,
            response_deserializer=google_dot_cloud_dot_translate__v3beta1_dot_proto_dot_translation__service__pb2.DetectLanguageResponse.FromString,
        )
        self.GetSupportedLanguages = channel.unary_unary(
            "/google.cloud.translation.v3beta1.TranslationService/GetSupportedLanguages",
            request_serializer=google_dot_cloud_dot_translate__v3beta1_dot_proto_dot_translation__service__pb2.GetSupportedLanguagesRequest.SerializeToString,
            response_deserializer=google_dot_cloud_dot_translate__v3beta1_dot_proto_dot_translation__service__pb2.SupportedLanguages.FromString,
        )
        self.BatchTranslateText = channel.unary_unary(
            "/google.cloud.translation.v3beta1.TranslationService/BatchTranslateText",
            request_serializer=google_dot_cloud_dot_translate__v3beta1_dot_proto_dot_translation__service__pb2.BatchTranslateTextRequest.SerializeToString,
            response_deserializer=google_dot_longrunning_dot_operations__pb2.Operation.FromString,
        )
        self.CreateGlossary = channel.unary_unary(
            "/google.cloud.translation.v3beta1.TranslationService/CreateGlossary",
            request_serializer=google_dot_cloud_dot_translate__v3beta1_dot_proto_dot_translation__service__pb2.CreateGlossaryRequest.SerializeToString,
            response_deserializer=google_dot_longrunning_dot_operations__pb2.Operation.FromString,
        )
        self.ListGlossaries = channel.unary_unary(
            "/google.cloud.translation.v3beta1.TranslationService/ListGlossaries",
            request_serializer=google_dot_cloud_dot_translate__v3beta1_dot_proto_dot_translation__service__pb2.ListGlossariesRequest.SerializeToString,
            response_deserializer=google_dot_cloud_dot_translate__v3beta1_dot_proto_dot_translation__service__pb2.ListGlossariesResponse.FromString,
        )
        self.GetGlossary = channel.unary_unary(
            "/google.cloud.translation.v3beta1.TranslationService/GetGlossary",
            request_serializer=google_dot_cloud_dot_translate__v3beta1_dot_proto_dot_translation__service__pb2.GetGlossaryRequest.SerializeToString,
            response_deserializer=google_dot_cloud_dot_translate__v3beta1_dot_proto_dot_translation__service__pb2.Glossary.FromString,
        )
        self.DeleteGlossary = channel.unary_unary(
            "/google.cloud.translation.v3beta1.TranslationService/DeleteGlossary",
            request_serializer=google_dot_cloud_dot_translate__v3beta1_dot_proto_dot_translation__service__pb2.DeleteGlossaryRequest.SerializeToString,
            response_deserializer=google_dot_longrunning_dot_operations__pb2.Operation.FromString,
        )


class TranslationServiceServicer(object):
    """Proto file for the Cloud Translation API (v3beta1).

    Provides natural language translation operations.
    """

    def TranslateText(self, request, context):
        """Translates input text and returns translated text.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def DetectLanguage(self, request, context):
        """Detects the language of text within a request.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def GetSupportedLanguages(self, request, context):
        """Returns a list of supported languages for translation.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def BatchTranslateText(self, request, context):
        """Translates a large volume of text in asynchronous batch mode.
        This function provides real-time output as the inputs are being processed.
        If caller cancels a request, the partial results (for an input file, it's
        all or nothing) may still be available on the specified output location.

        This call returns immediately and you can
        use google.longrunning.Operation.name to poll the status of the call.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def CreateGlossary(self, request, context):
        """Creates a glossary and returns the long-running operation. Returns
        NOT_FOUND, if the project doesn't exist.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def ListGlossaries(self, request, context):
        """Lists glossaries in a project. Returns NOT_FOUND, if the project doesn't
        exist.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def GetGlossary(self, request, context):
        """Gets a glossary. Returns NOT_FOUND, if the glossary doesn't
        exist.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def DeleteGlossary(self, request, context):
        """Deletes a glossary, or cancels glossary construction
        if the glossary isn't created yet.
        Returns NOT_FOUND, if the glossary doesn't exist.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")


def add_TranslationServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
        "TranslateText": grpc.unary_unary_rpc_method_handler(
            servicer.TranslateText,
            request_deserializer=google_dot_cloud_dot_translate__v3beta1_dot_proto_dot_translation__service__pb2.TranslateTextRequest.FromString,
            response_serializer=google_dot_cloud_dot_translate__v3beta1_dot_proto_dot_translation__service__pb2.TranslateTextResponse.SerializeToString,
        ),
        "DetectLanguage": grpc.unary_unary_rpc_method_handler(
            servicer.DetectLanguage,
            request_deserializer=google_dot_cloud_dot_translate__v3beta1_dot_proto_dot_translation__service__pb2.DetectLanguageRequest.FromString,
            response_serializer=google_dot_cloud_dot_translate__v3beta1_dot_proto_dot_translation__service__pb2.DetectLanguageResponse.SerializeToString,
        ),
        "GetSupportedLanguages": grpc.unary_unary_rpc_method_handler(
            servicer.GetSupportedLanguages,
            request_deserializer=google_dot_cloud_dot_translate__v3beta1_dot_proto_dot_translation__service__pb2.GetSupportedLanguagesRequest.FromString,
            response_serializer=google_dot_cloud_dot_translate__v3beta1_dot_proto_dot_translation__service__pb2.SupportedLanguages.SerializeToString,
        ),
        "BatchTranslateText": grpc.unary_unary_rpc_method_handler(
            servicer.BatchTranslateText,
            request_deserializer=google_dot_cloud_dot_translate__v3beta1_dot_proto_dot_translation__service__pb2.BatchTranslateTextRequest.FromString,
            response_serializer=google_dot_longrunning_dot_operations__pb2.Operation.SerializeToString,
        ),
        "CreateGlossary": grpc.unary_unary_rpc_method_handler(
            servicer.CreateGlossary,
            request_deserializer=google_dot_cloud_dot_translate__v3beta1_dot_proto_dot_translation__service__pb2.CreateGlossaryRequest.FromString,
            response_serializer=google_dot_longrunning_dot_operations__pb2.Operation.SerializeToString,
        ),
        "ListGlossaries": grpc.unary_unary_rpc_method_handler(
            servicer.ListGlossaries,
            request_deserializer=google_dot_cloud_dot_translate__v3beta1_dot_proto_dot_translation__service__pb2.ListGlossariesRequest.FromString,
            response_serializer=google_dot_cloud_dot_translate__v3beta1_dot_proto_dot_translation__service__pb2.ListGlossariesResponse.SerializeToString,
        ),
        "GetGlossary": grpc.unary_unary_rpc_method_handler(
            servicer.GetGlossary,
            request_deserializer=google_dot_cloud_dot_translate__v3beta1_dot_proto_dot_translation__service__pb2.GetGlossaryRequest.FromString,
            response_serializer=google_dot_cloud_dot_translate__v3beta1_dot_proto_dot_translation__service__pb2.Glossary.SerializeToString,
        ),
        "DeleteGlossary": grpc.unary_unary_rpc_method_handler(
            servicer.DeleteGlossary,
            request_deserializer=google_dot_cloud_dot_translate__v3beta1_dot_proto_dot_translation__service__pb2.DeleteGlossaryRequest.FromString,
            response_serializer=google_dot_longrunning_dot_operations__pb2.Operation.SerializeToString,
        ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
        "google.cloud.translation.v3beta1.TranslationService", rpc_method_handlers
    )
    server.add_generic_rpc_handlers((generic_handler,))


# This class is part of an EXPERIMENTAL API.
class TranslationService(object):
    """Proto file for the Cloud Translation API (v3beta1).

    Provides natural language translation operations.
    """

    @staticmethod
    def TranslateText(
        request,
        target,
        options=(),
        channel_credentials=None,
        call_credentials=None,
        compression=None,
        wait_for_ready=None,
        timeout=None,
        metadata=None,
    ):
        return grpc.experimental.unary_unary(
            request,
            target,
            "/google.cloud.translation.v3beta1.TranslationService/TranslateText",
            google_dot_cloud_dot_translate__v3beta1_dot_proto_dot_translation__service__pb2.TranslateTextRequest.SerializeToString,
            google_dot_cloud_dot_translate__v3beta1_dot_proto_dot_translation__service__pb2.TranslateTextResponse.FromString,
            options,
            channel_credentials,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )

    @staticmethod
    def DetectLanguage(
        request,
        target,
        options=(),
        channel_credentials=None,
        call_credentials=None,
        compression=None,
        wait_for_ready=None,
        timeout=None,
        metadata=None,
    ):
        return grpc.experimental.unary_unary(
            request,
            target,
            "/google.cloud.translation.v3beta1.TranslationService/DetectLanguage",
            google_dot_cloud_dot_translate__v3beta1_dot_proto_dot_translation__service__pb2.DetectLanguageRequest.SerializeToString,
            google_dot_cloud_dot_translate__v3beta1_dot_proto_dot_translation__service__pb2.DetectLanguageResponse.FromString,
            options,
            channel_credentials,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )

    @staticmethod
    def GetSupportedLanguages(
        request,
        target,
        options=(),
        channel_credentials=None,
        call_credentials=None,
        compression=None,
        wait_for_ready=None,
        timeout=None,
        metadata=None,
    ):
        return grpc.experimental.unary_unary(
            request,
            target,
            "/google.cloud.translation.v3beta1.TranslationService/GetSupportedLanguages",
            google_dot_cloud_dot_translate__v3beta1_dot_proto_dot_translation__service__pb2.GetSupportedLanguagesRequest.SerializeToString,
            google_dot_cloud_dot_translate__v3beta1_dot_proto_dot_translation__service__pb2.SupportedLanguages.FromString,
            options,
            channel_credentials,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )

    @staticmethod
    def BatchTranslateText(
        request,
        target,
        options=(),
        channel_credentials=None,
        call_credentials=None,
        compression=None,
        wait_for_ready=None,
        timeout=None,
        metadata=None,
    ):
        return grpc.experimental.unary_unary(
            request,
            target,
            "/google.cloud.translation.v3beta1.TranslationService/BatchTranslateText",
            google_dot_cloud_dot_translate__v3beta1_dot_proto_dot_translation__service__pb2.BatchTranslateTextRequest.SerializeToString,
            google_dot_longrunning_dot_operations__pb2.Operation.FromString,
            options,
            channel_credentials,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )

    @staticmethod
    def CreateGlossary(
        request,
        target,
        options=(),
        channel_credentials=None,
        call_credentials=None,
        compression=None,
        wait_for_ready=None,
        timeout=None,
        metadata=None,
    ):
        return grpc.experimental.unary_unary(
            request,
            target,
            "/google.cloud.translation.v3beta1.TranslationService/CreateGlossary",
            google_dot_cloud_dot_translate__v3beta1_dot_proto_dot_translation__service__pb2.CreateGlossaryRequest.SerializeToString,
            google_dot_longrunning_dot_operations__pb2.Operation.FromString,
            options,
            channel_credentials,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )

    @staticmethod
    def ListGlossaries(
        request,
        target,
        options=(),
        channel_credentials=None,
        call_credentials=None,
        compression=None,
        wait_for_ready=None,
        timeout=None,
        metadata=None,
    ):
        return grpc.experimental.unary_unary(
            request,
            target,
            "/google.cloud.translation.v3beta1.TranslationService/ListGlossaries",
            google_dot_cloud_dot_translate__v3beta1_dot_proto_dot_translation__service__pb2.ListGlossariesRequest.SerializeToString,
            google_dot_cloud_dot_translate__v3beta1_dot_proto_dot_translation__service__pb2.ListGlossariesResponse.FromString,
            options,
            channel_credentials,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )

    @staticmethod
    def GetGlossary(
        request,
        target,
        options=(),
        channel_credentials=None,
        call_credentials=None,
        compression=None,
        wait_for_ready=None,
        timeout=None,
        metadata=None,
    ):
        return grpc.experimental.unary_unary(
            request,
            target,
            "/google.cloud.translation.v3beta1.TranslationService/GetGlossary",
            google_dot_cloud_dot_translate__v3beta1_dot_proto_dot_translation__service__pb2.GetGlossaryRequest.SerializeToString,
            google_dot_cloud_dot_translate__v3beta1_dot_proto_dot_translation__service__pb2.Glossary.FromString,
            options,
            channel_credentials,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )

    @staticmethod
    def DeleteGlossary(
        request,
        target,
        options=(),
        channel_credentials=None,
        call_credentials=None,
        compression=None,
        wait_for_ready=None,
        timeout=None,
        metadata=None,
    ):
        return grpc.experimental.unary_unary(
            request,
            target,
            "/google.cloud.translation.v3beta1.TranslationService/DeleteGlossary",
            google_dot_cloud_dot_translate__v3beta1_dot_proto_dot_translation__service__pb2.DeleteGlossaryRequest.SerializeToString,
            google_dot_longrunning_dot_operations__pb2.Operation.FromString,
            options,
            channel_credentials,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )
