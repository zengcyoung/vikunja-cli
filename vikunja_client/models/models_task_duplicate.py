from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.models_task import ModelsTask


T = TypeVar("T", bound="ModelsTaskDuplicate")


@_attrs_define
class ModelsTaskDuplicate:
    """
    Attributes:
        duplicated_task (ModelsTask | Unset):
    """

    duplicated_task: ModelsTask | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        duplicated_task: dict[str, Any] | Unset = UNSET
        if not isinstance(self.duplicated_task, Unset):
            duplicated_task = self.duplicated_task.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if duplicated_task is not UNSET:
            field_dict["duplicated_task"] = duplicated_task

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.models_task import ModelsTask

        d = dict(src_dict)
        _duplicated_task = d.pop("duplicated_task", UNSET)
        duplicated_task: ModelsTask | Unset
        if isinstance(_duplicated_task, Unset):
            duplicated_task = UNSET
        else:
            duplicated_task = ModelsTask.from_dict(_duplicated_task) if _duplicated_task is not None else None

        models_task_duplicate = cls(
            duplicated_task=duplicated_task,
        )

        models_task_duplicate.additional_properties = d
        return models_task_duplicate

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
