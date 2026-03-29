from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ModelsTeamMember")


@_attrs_define
class ModelsTeamMember:
    """
    Attributes:
        admin (bool | Unset): Whether or not the member is an admin of the team. See the docs for more about what a team
            admin can do
        created (str | Unset): A timestamp when this relation was created. You cannot change this value.
        id (int | Unset): The unique, numeric id of this team member relation.
        username (str | Unset): The username of the member. We use this to prevent automated user id entering.
    """

    admin: bool | Unset = UNSET
    created: str | Unset = UNSET
    id: int | Unset = UNSET
    username: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        admin = self.admin

        created = self.created

        id = self.id

        username = self.username

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if admin is not UNSET:
            field_dict["admin"] = admin
        if created is not UNSET:
            field_dict["created"] = created
        if id is not UNSET:
            field_dict["id"] = id
        if username is not UNSET:
            field_dict["username"] = username

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        admin = d.pop("admin", UNSET)

        created = d.pop("created", UNSET)

        id = d.pop("id", UNSET)

        username = d.pop("username", UNSET)

        models_team_member = cls(
            admin=admin,
            created=created,
            id=id,
            username=username,
        )

        models_team_member.additional_properties = d
        return models_team_member

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
