from typing import Literal, cast

ModelsProjectViewViewKind = Literal["gantt", "kanban", "list", "table"]

MODELS_PROJECT_VIEW_VIEW_KIND_VALUES: set[ModelsProjectViewViewKind] = {
    "gantt",
    "kanban",
    "list",
    "table",
}


def check_models_project_view_view_kind(value: str) -> ModelsProjectViewViewKind:
    if value in MODELS_PROJECT_VIEW_VIEW_KIND_VALUES:
        return cast(ModelsProjectViewViewKind, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {MODELS_PROJECT_VIEW_VIEW_KIND_VALUES!r}"
    )
