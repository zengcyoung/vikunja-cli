from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CodeVikunjaIoApiPkgModulesAuthOpenidProvider")


@_attrs_define
class CodeVikunjaIoApiPkgModulesAuthOpenidProvider:
    """
    Attributes:
        auth_url (str | Unset):
        client_id (str | Unset):
        email_fallback (bool | Unset):
        force_user_info (bool | Unset):
        key (str | Unset):
        logout_url (str | Unset):
        name (str | Unset):
        scope (str | Unset):
        username_fallback (bool | Unset):
    """

    auth_url: str | Unset = UNSET
    client_id: str | Unset = UNSET
    email_fallback: bool | Unset = UNSET
    force_user_info: bool | Unset = UNSET
    key: str | Unset = UNSET
    logout_url: str | Unset = UNSET
    name: str | Unset = UNSET
    scope: str | Unset = UNSET
    username_fallback: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        auth_url = self.auth_url

        client_id = self.client_id

        email_fallback = self.email_fallback

        force_user_info = self.force_user_info

        key = self.key

        logout_url = self.logout_url

        name = self.name

        scope = self.scope

        username_fallback = self.username_fallback

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if auth_url is not UNSET:
            field_dict["auth_url"] = auth_url
        if client_id is not UNSET:
            field_dict["client_id"] = client_id
        if email_fallback is not UNSET:
            field_dict["email_fallback"] = email_fallback
        if force_user_info is not UNSET:
            field_dict["force_user_info"] = force_user_info
        if key is not UNSET:
            field_dict["key"] = key
        if logout_url is not UNSET:
            field_dict["logout_url"] = logout_url
        if name is not UNSET:
            field_dict["name"] = name
        if scope is not UNSET:
            field_dict["scope"] = scope
        if username_fallback is not UNSET:
            field_dict["username_fallback"] = username_fallback

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        auth_url = d.pop("auth_url", UNSET)

        client_id = d.pop("client_id", UNSET)

        email_fallback = d.pop("email_fallback", UNSET)

        force_user_info = d.pop("force_user_info", UNSET)

        key = d.pop("key", UNSET)

        logout_url = d.pop("logout_url", UNSET)

        name = d.pop("name", UNSET)

        scope = d.pop("scope", UNSET)

        username_fallback = d.pop("username_fallback", UNSET)

        code_vikunja_io_api_pkg_modules_auth_openid_provider = cls(
            auth_url=auth_url,
            client_id=client_id,
            email_fallback=email_fallback,
            force_user_info=force_user_info,
            key=key,
            logout_url=logout_url,
            name=name,
            scope=scope,
            username_fallback=username_fallback,
        )

        code_vikunja_io_api_pkg_modules_auth_openid_provider.additional_properties = d
        return code_vikunja_io_api_pkg_modules_auth_openid_provider

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
