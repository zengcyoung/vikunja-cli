from typing import Literal, cast

ModelsProjectViewBucketConfigurationMode = Literal["filter", "manual", "none"]

MODELS_PROJECT_VIEW_BUCKET_CONFIGURATION_MODE_VALUES: set[
    ModelsProjectViewBucketConfigurationMode
] = {
    "filter",
    "manual",
    "none",
}


def check_models_project_view_bucket_configuration_mode(
    value: str,
) -> ModelsProjectViewBucketConfigurationMode:
    if value in MODELS_PROJECT_VIEW_BUCKET_CONFIGURATION_MODE_VALUES:
        return cast(ModelsProjectViewBucketConfigurationMode, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {MODELS_PROJECT_VIEW_BUCKET_CONFIGURATION_MODE_VALUES!r}"
    )
