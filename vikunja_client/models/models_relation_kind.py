from typing import Literal, cast

ModelsRelationKind = Literal[
    "blocked",
    "blocking",
    "copiedfrom",
    "copiedto",
    "duplicateof",
    "duplicates",
    "follows",
    "parenttask",
    "precedes",
    "related",
    "subtask",
    "unknown",
]

MODELS_RELATION_KIND_VALUES: set[ModelsRelationKind] = {
    "blocked",
    "blocking",
    "copiedfrom",
    "copiedto",
    "duplicateof",
    "duplicates",
    "follows",
    "parenttask",
    "precedes",
    "related",
    "subtask",
    "unknown",
}


def check_models_relation_kind(value: str) -> ModelsRelationKind:
    if value in MODELS_RELATION_KIND_VALUES:
        return cast(ModelsRelationKind, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {MODELS_RELATION_KIND_VALUES!r}"
    )
