from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.models_team_user import ModelsTeamUser
    from ..models.user_user import UserUser


T = TypeVar("T", bound="ModelsTeam")


@_attrs_define
class ModelsTeam:
    """
    Attributes:
        created (str | Unset): A timestamp when this relation was created. You cannot change this value.
        created_by (UserUser | Unset):
        description (str | Unset): The team's description.
        external_id (str | Unset): The team's external id provided by the openid or ldap provider
        id (int | Unset): The unique, numeric id of this team.
        include_public (bool | Unset): Query parameter controlling whether to include public projects or not
        is_public (bool | Unset): Defines wether the team should be publicly discoverable when sharing a project
        members (list[ModelsTeamUser] | Unset): An array of all members in this team.
        name (str | Unset): The name of this team.
        updated (str | Unset): A timestamp when this relation was last updated. You cannot change this value.
    """

    created: str | Unset = UNSET
    created_by: UserUser | Unset = UNSET
    description: str | Unset = UNSET
    external_id: str | Unset = UNSET
    id: int | Unset = UNSET
    include_public: bool | Unset = UNSET
    is_public: bool | Unset = UNSET
    members: list[ModelsTeamUser] | Unset = UNSET
    name: str | Unset = UNSET
    updated: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        created = self.created

        created_by: dict[str, Any] | Unset = UNSET
        if not isinstance(self.created_by, Unset):
            created_by = self.created_by.to_dict()

        description = self.description

        external_id = self.external_id

        id = self.id

        include_public = self.include_public

        is_public = self.is_public

        members: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.members, Unset):
            members = []
            for members_item_data in self.members:
                members_item = members_item_data.to_dict()
                members.append(members_item)

        name = self.name

        updated = self.updated

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if created is not UNSET:
            field_dict["created"] = created
        if created_by is not UNSET:
            field_dict["created_by"] = created_by
        if description is not UNSET:
            field_dict["description"] = description
        if external_id is not UNSET:
            field_dict["external_id"] = external_id
        if id is not UNSET:
            field_dict["id"] = id
        if include_public is not UNSET:
            field_dict["include_public"] = include_public
        if is_public is not UNSET:
            field_dict["is_public"] = is_public
        if members is not UNSET:
            field_dict["members"] = members
        if name is not UNSET:
            field_dict["name"] = name
        if updated is not UNSET:
            field_dict["updated"] = updated

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.models_team_user import ModelsTeamUser
        from ..models.user_user import UserUser

        d = dict(src_dict)
        created = d.pop("created", UNSET)

        _created_by = d.pop("created_by", UNSET)
        created_by: UserUser | Unset
        if isinstance(_created_by, Unset):
            created_by = UNSET
        else:
            created_by = UserUser.from_dict(_created_by) if _created_by is not None else None

        description = d.pop("description", UNSET)

        external_id = d.pop("external_id", UNSET)

        id = d.pop("id", UNSET)

        include_public = d.pop("include_public", UNSET)

        is_public = d.pop("is_public", UNSET)

        _members = d.pop("members", UNSET)
        members: list[ModelsTeamUser] | Unset = UNSET
        if _members is not UNSET:
            members = []
            for members_item_data in _members:
                members_item = ModelsTeamUser.from_dict(members_item_data)

                members.append(members_item)

        name = d.pop("name", UNSET)

        updated = d.pop("updated", UNSET)

        models_team = cls(
            created=created,
            created_by=created_by,
            description=description,
            external_id=external_id,
            id=id,
            include_public=include_public,
            is_public=is_public,
            members=members,
            name=name,
            updated=updated,
        )

        models_team.additional_properties = d
        return models_team

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
