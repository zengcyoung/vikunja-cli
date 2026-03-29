from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="V1UserRegister")


@_attrs_define
class V1UserRegister:
    """
    Attributes:
        email (str | Unset): The user's email address
        language (str | Unset): The language of the new user. Must be a valid IETF BCP 47 language code and exist in
            Vikunja.
        password (str | Unset): The user's password in clear text. Only used when registering the user. The maximum limi
            is 72 bytes, which may be less than 72 characters. This is due to the limit in the bcrypt hashing algorithm used
            to store passwords in Vikunja.
        username (str | Unset): The user's username. Cannot contain anything that looks like an url or whitespaces.
    """

    email: str | Unset = UNSET
    language: str | Unset = UNSET
    password: str | Unset = UNSET
    username: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        email = self.email

        language = self.language

        password = self.password

        username = self.username

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if email is not UNSET:
            field_dict["email"] = email
        if language is not UNSET:
            field_dict["language"] = language
        if password is not UNSET:
            field_dict["password"] = password
        if username is not UNSET:
            field_dict["username"] = username

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        email = d.pop("email", UNSET)

        language = d.pop("language", UNSET)

        password = d.pop("password", UNSET)

        username = d.pop("username", UNSET)

        v1_user_register = cls(
            email=email,
            language=language,
            password=password,
            username=username,
        )

        v1_user_register.additional_properties = d
        return v1_user_register

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
