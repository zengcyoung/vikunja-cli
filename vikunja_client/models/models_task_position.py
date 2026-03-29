from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ModelsTaskPosition")


@_attrs_define
class ModelsTaskPosition:
    """
    Attributes:
        position (float | Unset): The position of the task - any task project can be sorted as usual by this parameter.
            When accessing tasks via kanban buckets, this is primarily used to sort them based on a range
            We're using a float64 here to make it possible to put any task within any two other tasks (by changing the
            number).
            You would calculate the new position between two tasks with something like task3.position = (task2.position -
            task1.position) / 2.
            A 64-Bit float leaves plenty of room to initially give tasks a position with 2^16 difference to the previous
            task
            which also leaves a lot of room for rearranging and sorting later.
            Positions are always saved per view. They will automatically be set if you request the tasks through a view
            endpoint, otherwise they will always be 0. To update them, take a look at the Task Position endpoint.
        project_view_id (int | Unset): The project view this task is related to
        task_id (int | Unset): The ID of the task this position is for
    """

    position: float | Unset = UNSET
    project_view_id: int | Unset = UNSET
    task_id: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        position = self.position

        project_view_id = self.project_view_id

        task_id = self.task_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if position is not UNSET:
            field_dict["position"] = position
        if project_view_id is not UNSET:
            field_dict["project_view_id"] = project_view_id
        if task_id is not UNSET:
            field_dict["task_id"] = task_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        position = d.pop("position", UNSET)

        project_view_id = d.pop("project_view_id", UNSET)

        task_id = d.pop("task_id", UNSET)

        models_task_position = cls(
            position=position,
            project_view_id=project_view_id,
            task_id=task_id,
        )

        models_task_position.additional_properties = d
        return models_task_position

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
