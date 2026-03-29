from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.models_permission import ModelsPermission, check_models_permission
from ..types import UNSET, Unset

T = TypeVar("T", bound="ModelsProjectUser")


@_attrs_define
class ModelsProjectUser:
    """
    Attributes:
        created (str | Unset): A timestamp when this relation was created. You cannot change this value.
        id (int | Unset): The unique, numeric id of this project <-> user relation.
        permission (ModelsPermission | Unset):  Default: 0.
        updated (str | Unset): A timestamp when this relation was last updated. You cannot change this value.
        username (str | Unset): The username.
    """

    created: str | Unset = UNSET
    id: int | Unset = UNSET
    permission: ModelsPermission | Unset = 0
    updated: str | Unset = UNSET
    username: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        created = self.created

        id = self.id

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
        if id is not UNSET:
            field_dict["id"] = id
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

        id = d.pop("id", UNSET)

        _permission = d.pop("permission", UNSET)
        permission: ModelsPermission | Unset
        if isinstance(_permission, Unset):
            permission = UNSET
        else:
            permission = check_models_permission(_permission)

        updated = d.pop("updated", UNSET)

        username = d.pop("username", UNSET)

        models_project_user = cls(
            created=created,
            id=id,
            permission=permission,
            updated=updated,
            username=username,
        )

        models_project_user.additional_properties = d
        return models_project_user

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
