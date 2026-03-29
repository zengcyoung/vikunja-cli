from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="V1UserAvatarProvider")


@_attrs_define
class V1UserAvatarProvider:
    """
    Attributes:
        avatar_provider (str | Unset): The avatar provider. Valid types are `gravatar` (uses the user email), `upload`,
            `initials`, `marble` (generates a random avatar for each user), `ldap` (synced from LDAP server), `openid`
            (synced from OpenID provider), `default`.
    """

    avatar_provider: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        avatar_provider = self.avatar_provider

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if avatar_provider is not UNSET:
            field_dict["avatar_provider"] = avatar_provider

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        avatar_provider = d.pop("avatar_provider", UNSET)

        v1_user_avatar_provider = cls(
            avatar_provider=avatar_provider,
        )

        v1_user_avatar_provider.additional_properties = d
        return v1_user_avatar_provider

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
