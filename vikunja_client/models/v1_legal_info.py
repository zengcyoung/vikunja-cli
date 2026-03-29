from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="V1LegalInfo")


@_attrs_define
class V1LegalInfo:
    """
    Attributes:
        imprint_url (str | Unset):
        privacy_policy_url (str | Unset):
    """

    imprint_url: str | Unset = UNSET
    privacy_policy_url: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        imprint_url = self.imprint_url

        privacy_policy_url = self.privacy_policy_url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if imprint_url is not UNSET:
            field_dict["imprint_url"] = imprint_url
        if privacy_policy_url is not UNSET:
            field_dict["privacy_policy_url"] = privacy_policy_url

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        imprint_url = d.pop("imprint_url", UNSET)

        privacy_policy_url = d.pop("privacy_policy_url", UNSET)

        v1_legal_info = cls(
            imprint_url=imprint_url,
            privacy_policy_url=privacy_policy_url,
        )

        v1_legal_info.additional_properties = d
        return v1_legal_info

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
