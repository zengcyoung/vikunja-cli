from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="BackgroundImage")


@_attrs_define
class BackgroundImage:
    """
    Attributes:
        blur_hash (str | Unset):
        id (str | Unset):
        info (Any | Unset): This can be used to supply extra information from an image provider to clients
        thumb (str | Unset):
        url (str | Unset):
    """

    blur_hash: str | Unset = UNSET
    id: str | Unset = UNSET
    info: Any | Unset = UNSET
    thumb: str | Unset = UNSET
    url: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        blur_hash = self.blur_hash

        id = self.id

        info = self.info

        thumb = self.thumb

        url = self.url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if blur_hash is not UNSET:
            field_dict["blur_hash"] = blur_hash
        if id is not UNSET:
            field_dict["id"] = id
        if info is not UNSET:
            field_dict["info"] = info
        if thumb is not UNSET:
            field_dict["thumb"] = thumb
        if url is not UNSET:
            field_dict["url"] = url

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        blur_hash = d.pop("blur_hash", UNSET)

        id = d.pop("id", UNSET)

        info = d.pop("info", UNSET)

        thumb = d.pop("thumb", UNSET)

        url = d.pop("url", UNSET)

        background_image = cls(
            blur_hash=blur_hash,
            id=id,
            info=info,
            thumb=thumb,
            url=url,
        )

        background_image.additional_properties = d
        return background_image

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
