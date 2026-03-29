from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.models_task import ModelsTask


T = TypeVar("T", bound="ModelsBulkTask")


@_attrs_define
class ModelsBulkTask:
    """
    Attributes:
        fields (list[str] | Unset):
        task_ids (list[int] | Unset):
        tasks (list[ModelsTask] | Unset):
        values (ModelsTask | Unset):
    """

    fields: list[str] | Unset = UNSET
    task_ids: list[int] | Unset = UNSET
    tasks: list[ModelsTask] | Unset = UNSET
    values: ModelsTask | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        fields: list[str] | Unset = UNSET
        if not isinstance(self.fields, Unset):
            fields = self.fields

        task_ids: list[int] | Unset = UNSET
        if not isinstance(self.task_ids, Unset):
            task_ids = self.task_ids

        tasks: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.tasks, Unset):
            tasks = []
            for tasks_item_data in self.tasks:
                tasks_item = tasks_item_data.to_dict()
                tasks.append(tasks_item)

        values: dict[str, Any] | Unset = UNSET
        if not isinstance(self.values, Unset):
            values = self.values.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if fields is not UNSET:
            field_dict["fields"] = fields
        if task_ids is not UNSET:
            field_dict["task_ids"] = task_ids
        if tasks is not UNSET:
            field_dict["tasks"] = tasks
        if values is not UNSET:
            field_dict["values"] = values

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.models_task import ModelsTask

        d = dict(src_dict)
        fields = cast(list[str], d.pop("fields", UNSET))

        task_ids = cast(list[int], d.pop("task_ids", UNSET))

        _tasks = d.pop("tasks", UNSET)
        tasks: list[ModelsTask] | Unset = UNSET
        if _tasks is not UNSET:
            tasks = []
            for tasks_item_data in _tasks:
                tasks_item = ModelsTask.from_dict(tasks_item_data)

                tasks.append(tasks_item)

        _values = d.pop("values", UNSET)
        values: ModelsTask | Unset
        if isinstance(_values, Unset):
            values = UNSET
        else:
            values = ModelsTask.from_dict(_values) if _values is not None else None

        models_bulk_task = cls(
            fields=fields,
            task_ids=task_ids,
            tasks=tasks,
            values=values,
        )

        models_bulk_task.additional_properties = d
        return models_bulk_task

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
