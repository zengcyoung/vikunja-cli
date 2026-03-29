from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.models_permission import ModelsPermission, check_models_permission
from ..types import UNSET, Unset

T = TypeVar("T", bound="ModelsUserWithPermission")


@_attrs_define
class ModelsUserWithPermission:
    """
    Attributes:
        created (str | Unset): A timestamp when this task was created. You cannot change this value.
        email (str | Unset): The user's email address.
        id (int | Unset): The unique, numeric id of this user.
        name (str | Unset): The full name of the user.
        permission (ModelsPermission | Unset):
        updated (str | Unset): A timestamp when this task was last updated. You cannot change this value.
        username (str | Unset): The username of the user. Is always unique.
    """

    created: str | Unset = UNSET
    email: str | Unset = UNSET
    id: int | Unset = UNSET
    name: str | Unset = UNSET
    permission: ModelsPermission | Unset = UNSET
    updated: str | Unset = UNSET
    username: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        created = self.created

        email = self.email

        id = self.id

        name = self.name

        permission: int | Unset = UNSET
        if not isinstance(self.permission, Unset):
            permission = self.permission

        updated = self.updated

        username = self.username

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if created is not UNSET:
            field_dict["created"] = created
        if email is not UNSET:
            field_dict["email"] = email
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if permission is not UNSET:
            field_dict["permission"] = permission
        if updated is not UNSET:
            field_dict["updated"] = updated
        if username is not UNSET:
            field_dict["username"] = username

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        created = d.pop("created", UNSET)

        email = d.pop("email", UNSET)

        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        _permission = d.pop("permission", UNSET)
        permission: ModelsPermission | Unset
        if isinstance(_permission, Unset):
            permission = UNSET
        else:
            permission = check_models_permission(_permission)

        updated = d.pop("updated", UNSET)

        username = d.pop("username", UNSET)

        models_user_with_permission = cls(
            created=created,
            email=email,
            id=id,
            name=name,
            permission=permission,
            updated=updated,
            username=username,
        )

        models_user_with_permission.additional_properties = d
        return models_user_with_permission

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
