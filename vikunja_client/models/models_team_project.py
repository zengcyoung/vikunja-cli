from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.models_permission import ModelsPermission, check_models_permission
from ..types import UNSET, Unset

T = TypeVar("T", bound="ModelsTeamProject")


@_attrs_define
class ModelsTeamProject:
    """
    Attributes:
        created (str | Unset): A timestamp when this relation was created. You cannot change this value.
        id (int | Unset): The unique, numeric id of this project <-> team relation.
        permission (ModelsPermission | Unset):  Default: 0.
        team_id (int | Unset): The team id.
        updated (str | Unset): A timestamp when this relation was last updated. You cannot change this value.
    """

    created: str | Unset = UNSET
    id: int | Unset = UNSET
    permission: ModelsPermission | Unset = 0
    team_id: int | Unset = UNSET
    updated: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        created = self.created

        id = self.id

        permission: int | Unset = UNSET
        if not isinstance(self.permission, Unset):
            permission = self.permission

        team_id = self.team_id

        updated = self.updated

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if created is not UNSET:
            field_dict["created"] = created
        if id is not UNSET:
            field_dict["id"] = id
        if permission is not UNSET:
            field_dict["permission"] = permission
        if team_id is not UNSET:
            field_dict["team_id"] = team_id
        if updated is not UNSET:
            field_dict["updated"] = updated

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

        team_id = d.pop("team_id", UNSET)

        updated = d.pop("updated", UNSET)

        models_team_project = cls(
            created=created,
            id=id,
            permission=permission,
            team_id=team_id,
            updated=updated,
        )

        models_team_project.additional_properties = d
        return models_team_project

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
