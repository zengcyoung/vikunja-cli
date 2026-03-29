from typing import Literal, cast

ModelsReminderRelation = Literal["due_date", "end_date", "start_date"]

MODELS_REMINDER_RELATION_VALUES: set[ModelsReminderRelation] = {
    "due_date",
    "end_date",
    "start_date",
}


def check_models_reminder_relation(value: str) -> ModelsReminderRelation:
    if value in MODELS_REMINDER_RELATION_VALUES:
        return cast(ModelsReminderRelation, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {MODELS_REMINDER_RELATION_VALUES!r}"
    )
