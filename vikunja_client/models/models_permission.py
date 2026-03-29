from typing import Literal, cast

ModelsPermission = Literal[0, 1, 2]

MODELS_PERMISSION_VALUES: set[ModelsPermission] = {
    0,
    1,
    2,
}


def check_models_permission(value: int) -> ModelsPermission:
    if value in MODELS_PERMISSION_VALUES:
        return cast(ModelsPermission, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {MODELS_PERMISSION_VALUES!r}"
    )
