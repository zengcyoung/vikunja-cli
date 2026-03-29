from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ModelsTeamUser")


@_attrs_define
class ModelsTeamUser:
    """
    Attributes:
        admin (bool | Unset): Whether the member is an admin of the team. See the docs for more about what a team admin
            can do
        created (str | Unset): A timestamp when this task was created. You cannot change this value.
        email (str | Unset): The user's email address.
        id (int | Unset): The unique, numeric id of this user.
        name (str | Unset): The full name of the user.
        updated (str | Unset): A timestamp when this task was last updated. You cannot change this value.
        username (str | Unset): The username of the user. Is always unique.
    """

    admin: bool | Unset = UNSET
    created: str | Unset = UNSET
    email: str | Unset = UNSET
    id: int | Unset = UNSET
    name: str | Unset = UNSET
    updated: str | Unset = UNSET
    username: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        admin = self.admin

        created = self.created

        email = self.email

        id = self.id

        name = self.name

        updated = self.updated

        username = self.username

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if admin is not UNSET:
            field_dict["admin"] = admin
        if created is not UNSET:
            field_dict["created"] = created
        if email is not UNSET:
            field_dict["email"] = email
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if updated is not UNSET:
            field_dict["updated"] = updated
        if username is not UNSET:
            field_dict["username"] = username

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        admin = d.pop("admin", UNSET)

        created = d.pop("created", UNSET)

        email = d.pop("email", UNSET)

        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        updated = d.pop("updated", UNSET)

        username = d.pop("username", UNSET)

        models_team_user = cls(
            admin=admin,
            created=created,
            email=email,
            id=id,
            name=name,
            updated=updated,
            username=username,
        )

        models_team_user.additional_properties = d
        return models_team_user

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
