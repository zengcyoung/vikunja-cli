from typing import Literal, cast

ModelsSharingType = Literal[0, 1, 2]

MODELS_SHARING_TYPE_VALUES: set[ModelsSharingType] = {
    0,
    1,
    2,
}


def check_models_sharing_type(value: int) -> ModelsSharingType:
    if value in MODELS_SHARING_TYPE_VALUES:
        return cast(ModelsSharingType, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {MODELS_SHARING_TYPE_VALUES!r}"
    )
