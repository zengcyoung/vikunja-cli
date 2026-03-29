from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="UserLogin")


@_attrs_define
class UserLogin:
    """
    Attributes:
        long_token (bool | Unset): If true, the token returned will be valid a lot longer than default. Useful for
            "remember me" style logins.
        password (str | Unset): The password for the user.
        totp_passcode (str | Unset): The totp passcode of a user. Only needs to be provided when enabled.
        username (str | Unset): The username used to log in.
    """

    long_token: bool | Unset = UNSET
    password: str | Unset = UNSET
    totp_passcode: str | Unset = UNSET
    username: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        long_token = self.long_token

        password = self.password

        totp_passcode = self.totp_passcode

        username = self.username

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if long_token is not UNSET:
            field_dict["long_token"] = long_token
        if password is not UNSET:
            field_dict["password"] = password
        if totp_passcode is not UNSET:
            field_dict["totp_passcode"] = totp_passcode
        if username is not UNSET:
            field_dict["username"] = username

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        long_token = d.pop("long_token", UNSET)

        password = d.pop("password", UNSET)

        totp_passcode = d.pop("totp_passcode", UNSET)

        username = d.pop("username", UNSET)

        user_login = cls(
            long_token=long_token,
            password=password,
            totp_passcode=totp_passcode,
            username=username,
        )

        user_login.additional_properties = d
        return user_login

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
