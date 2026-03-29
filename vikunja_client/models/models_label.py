from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.user_user import UserUser


T = TypeVar("T", bound="ModelsLabel")


@_attrs_define
class ModelsLabel:
    """
    Attributes:
        created (str | Unset): A timestamp when this label was created. You cannot change this value.
        created_by (UserUser | Unset):
        description (str | Unset): The label description.
        hex_color (str | Unset): The color this label has in hex format.
        id (int | Unset): The unique, numeric id of this label.
        title (str | Unset): The title of the label. You'll see this one on tasks associated with it.
        updated (str | Unset): A timestamp when this label was last updated. You cannot change this value.
    """

    created: str | Unset = UNSET
    created_by: UserUser | Unset = UNSET
    description: str | Unset = UNSET
    hex_color: str | Unset = UNSET
    id: int | Unset = UNSET
    title: str | Unset = UNSET
    updated: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        created = self.created

        created_by: dict[str, Any] | Unset = UNSET
        if not isinstance(self.created_by, Unset):
            created_by = self.created_by.to_dict()

        description = self.description

        hex_color = self.hex_color

        id = self.id

        title = self.title

        updated = self.updated

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if created is not UNSET:
            field_dict["created"] = created
        if created_by is not UNSET:
            field_dict["created_by"] = created_by
        if description is not UNSET:
            field_dict["description"] = description
        if hex_color is not UNSET:
            field_dict["hex_color"] = hex_color
        if id is not UNSET:
            field_dict["id"] = id
        if title is not UNSET:
            field_dict["title"] = title
        if updated is not UNSET:
            field_dict["updated"] = updated

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.user_user import UserUser

        d = dict(src_dict)
        created = d.pop("created", UNSET)

        _created_by = d.pop("created_by", UNSET)
        created_by: UserUser | Unset
        if isinstance(_created_by, Unset):
            created_by = UNSET
        else:
            created_by = UserUser.from_dict(_created_by) if _created_by is not None else None

        description = d.pop("description", UNSET)

        hex_color = d.pop("hex_color", UNSET)

        id = d.pop("id", UNSET)

        title = d.pop("title", UNSET)

        updated = d.pop("updated", UNSET)

        models_label = cls(
            created=created,
            created_by=created_by,
            description=description,
            hex_color=hex_color,
            id=id,
            title=title,
            updated=updated,
        )

        models_label.additional_properties = d
        return models_label

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
