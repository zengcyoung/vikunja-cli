from typing import Literal, cast

ModelsTaskRepeatMode = Literal[0, 1, 2]

MODELS_TASK_REPEAT_MODE_VALUES: set[ModelsTaskRepeatMode] = {
    0,
    1,
    2,
}


def check_models_task_repeat_mode(value: int) -> ModelsTaskRepeatMode:
    if value in MODELS_TASK_REPEAT_MODE_VALUES:
        return cast(ModelsTaskRepeatMode, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {MODELS_TASK_REPEAT_MODE_VALUES!r}"
    )
