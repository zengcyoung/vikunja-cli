from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.models_permission import ModelsPermission, check_models_permission
from ..models.models_sharing_type import ModelsSharingType, check_models_sharing_type
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.user_user import UserUser


T = TypeVar("T", bound="ModelsLinkSharing")


@_attrs_define
class ModelsLinkSharing:
    """
    Attributes:
        created (str | Unset): A timestamp when this project was shared. You cannot change this value.
        hash_ (str | Unset): The public id to get this shared project
        id (int | Unset): The ID of the shared thing
        name (str | Unset): The name of this link share. All actions someone takes while being authenticated with that
            link will appear with that name.
        password (str | Unset): The password of this link share. You can only set it, not retrieve it after the link
            share has been created.
        permission (ModelsPermission | Unset):  Default: 0.
        shared_by (UserUser | Unset):
        sharing_type (ModelsSharingType | Unset):  Default: 0.
        updated (str | Unset): A timestamp when this share was last updated. You cannot change this value.
    """

    created: str | Unset = UNSET
    hash_: str | Unset = UNSET
    id: int | Unset = UNSET
    name: str | Unset = UNSET
    password: str | Unset = UNSET
    permission: ModelsPermission | Unset = 0
    shared_by: UserUser | Unset = UNSET
    sharing_type: ModelsSharingType | Unset = 0
    updated: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        created = self.created

        hash_ = self.hash_

        id = self.id

        name = self.name

        password = self.password

        permission: int | Unset = UNSET
        if not isinstance(self.permission, Unset):
            permission = self.permission

        shared_by: dict[str, Any] | Unset = UNSET
        if not isinstance(self.shared_by, Unset):
            shared_by = self.shared_by.to_dict()

        sharing_type: int | Unset = UNSET
        if not isinstance(self.sharing_type, Unset):
            sharing_type = self.sharing_type

        updated = self.updated

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if created is not UNSET:
            field_dict["created"] = created
        if hash_ is not UNSET:
            field_dict["hash"] = hash_
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if password is not UNSET:
            field_dict["password"] = password
        if permission is not UNSET:
            field_dict["permission"] = permission
        if shared_by is not UNSET:
            field_dict["shared_by"] = shared_by
        if sharing_type is not UNSET:
            field_dict["sharing_type"] = sharing_type
        if updated is not UNSET:
            field_dict["updated"] = updated

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.user_user import UserUser

        d = dict(src_dict)
        created = d.pop("created", UNSET)

        hash_ = d.pop("hash", UNSET)

        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        password = d.pop("password", UNSET)

        _permission = d.pop("permission", UNSET)
        permission: ModelsPermission | Unset
        if isinstance(_permission, Unset):
            permission = UNSET
        else:
            permission = check_models_permission(_permission)

        _shared_by = d.pop("shared_by", UNSET)
        shared_by: UserUser | Unset
        if isinstance(_shared_by, Unset):
            shared_by = UNSET
        else:
            shared_by = UserUser.from_dict(_shared_by) if _shared_by is not None else None

        _sharing_type = d.pop("sharing_type", UNSET)
        sharing_type: ModelsSharingType | Unset
        if isinstance(_sharing_type, Unset):
            sharing_type = UNSET
        else:
            sharing_type = check_models_sharing_type(_sharing_type)

        updated = d.pop("updated", UNSET)

        models_link_sharing = cls(
            created=created,
            hash_=hash_,
            id=id,
            name=name,
            password=password,
            permission=permission,
            shared_by=shared_by,
            sharing_type=sharing_type,
            updated=updated,
        )

        models_link_sharing.additional_properties = d
        return models_link_sharing

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
