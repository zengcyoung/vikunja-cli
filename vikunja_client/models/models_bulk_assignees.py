from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.user_user import UserUser


T = TypeVar("T", bound="ModelsBulkAssignees")


@_attrs_define
class ModelsBulkAssignees:
    """
    Attributes:
        assignees (list[UserUser] | Unset): A project with all assignees
    """

    assignees: list[UserUser] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        assignees: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.assignees, Unset):
            assignees = []
            for assignees_item_data in self.assignees:
                assignees_item = assignees_item_data.to_dict()
                assignees.append(assignees_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if assignees is not UNSET:
            field_dict["assignees"] = assignees

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.user_user import UserUser

        d = dict(src_dict)
        _assignees = d.pop("assignees", UNSET)
        assignees: list[UserUser] | Unset = UNSET
        if _assignees is not UNSET:
            assignees = []
            for assignees_item_data in _assignees:
                assignees_item = UserUser.from_dict(assignees_item_data)

                assignees.append(assignees_item)

        models_bulk_assignees = cls(
            assignees=assignees,
        )

        models_bulk_assignees.additional_properties = d
        return models_bulk_assignees

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
