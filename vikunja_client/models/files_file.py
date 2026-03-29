from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="FilesFile")


@_attrs_define
class FilesFile:
    """
    Attributes:
        created (str | Unset):
        id (int | Unset):
        mime (str | Unset):
        name (str | Unset):
        size (int | Unset):
    """

    created: str | Unset = UNSET
    id: int | Unset = UNSET
    mime: str | Unset = UNSET
    name: str | Unset = UNSET
    size: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        created = self.created

        id = self.id

        mime = self.mime

        name = self.name

        size = self.size

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if created is not UNSET:
            field_dict["created"] = created
        if id is not UNSET:
            field_dict["id"] = id
        if mime is not UNSET:
            field_dict["mime"] = mime
        if name is not UNSET:
            field_dict["name"] = name
        if size is not UNSET:
            field_dict["size"] = size

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        created = d.pop("created", UNSET)

        id = d.pop("id", UNSET)

        mime = d.pop("mime", UNSET)

        name = d.pop("name", UNSET)

        size = d.pop("size", UNSET)

        files_file = cls(
            created=created,
            id=id,
            mime=mime,
            name=name,
            size=size,
        )

        files_file.additional_properties = d
        return files_file

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
