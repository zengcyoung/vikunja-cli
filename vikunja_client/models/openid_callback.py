from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="OpenidCallback")


@_attrs_define
class OpenidCallback:
    """
    Attributes:
        code (str | Unset):
        redirect_url (str | Unset):
        scope (str | Unset):
    """

    code: str | Unset = UNSET
    redirect_url: str | Unset = UNSET
    scope: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        code = self.code

        redirect_url = self.redirect_url

        scope = self.scope

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if code is not UNSET:
            field_dict["code"] = code
        if redirect_url is not UNSET:
            field_dict["redirect_url"] = redirect_url
        if scope is not UNSET:
            field_dict["scope"] = scope

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        code = d.pop("code", UNSET)

        redirect_url = d.pop("redirect_url", UNSET)

        scope = d.pop("scope", UNSET)

        openid_callback = cls(
            code=code,
            redirect_url=redirect_url,
            scope=scope,
        )

        openid_callback.additional_properties = d
        return openid_callback

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
