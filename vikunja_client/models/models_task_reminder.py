from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.models_reminder_relation import (
    ModelsReminderRelation,
    check_models_reminder_relation,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="ModelsTaskReminder")


@_attrs_define
class ModelsTaskReminder:
    """
    Attributes:
        relative_period (int | Unset): A period in seconds relative to another date argument. Negative values mean the
            reminder triggers before the date. Default: 0, tiggers when RelativeTo is due.
        relative_to (ModelsReminderRelation | Unset):
        reminder (str | Unset): The absolute time when the user wants to be reminded of the task.
    """

    relative_period: int | Unset = UNSET
    relative_to: ModelsReminderRelation | Unset = UNSET
    reminder: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        relative_period = self.relative_period

        relative_to: str | Unset = UNSET
        if not isinstance(self.relative_to, Unset):
            relative_to = self.relative_to

        reminder = self.reminder

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if relative_period is not UNSET:
            field_dict["relative_period"] = relative_period
        if relative_to is not UNSET:
            field_dict["relative_to"] = relative_to
        if reminder is not UNSET:
            field_dict["reminder"] = reminder

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        relative_period = d.pop("relative_period", UNSET)

        _relative_to = d.pop("relative_to", UNSET)
        relative_to: ModelsReminderRelation | Unset
        if isinstance(_relative_to, Unset):
            relative_to = UNSET
        else:
            relative_to = check_models_reminder_relation(_relative_to)

        reminder = d.pop("reminder", UNSET)

        models_task_reminder = cls(
            relative_period=relative_period,
            relative_to=relative_to,
            reminder=reminder,
        )

        models_task_reminder.additional_properties = d
        return models_task_reminder

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
