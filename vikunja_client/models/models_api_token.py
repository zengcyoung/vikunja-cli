from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.models_api_permissions import ModelsAPIPermissions


T = TypeVar("T", bound="ModelsAPIToken")


@_attrs_define
class ModelsAPIToken:
    """
    Attributes:
        created (str | Unset): A timestamp when this api key was created. You cannot change this value.
        expires_at (str | Unset): The date when this key expires.
        id (int | Unset): The unique, numeric id of this api key.
        permissions (ModelsAPIPermissions | Unset):
        title (str | Unset): A human-readable name for this token
        token (str | Unset): The actual api key. Only visible after creation.
    """

    created: str | Unset = UNSET
    expires_at: str | Unset = UNSET
    id: int | Unset = UNSET
    permissions: ModelsAPIPermissions | Unset = UNSET
    title: str | Unset = UNSET
    token: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        created = self.created

        expires_at = self.expires_at

        id = self.id

        permissions: dict[str, Any] | Unset = UNSET
        if not isinstance(self.permissions, Unset):
            permissions = self.permissions.to_dict()

        title = self.title

        token = self.token

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if created is not UNSET:
            field_dict["created"] = created
        if expires_at is not UNSET:
            field_dict["expires_at"] = expires_at
        if id is not UNSET:
            field_dict["id"] = id
        if permissions is not UNSET:
            field_dict["permissions"] = permissions
        if title is not UNSET:
            field_dict["title"] = title
        if token is not UNSET:
            field_dict["token"] = token

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.models_api_permissions import ModelsAPIPermissions

        d = dict(src_dict)
        created = d.pop("created", UNSET)

        expires_at = d.pop("expires_at", UNSET)

        id = d.pop("id", UNSET)

        _permissions = d.pop("permissions", UNSET)
        permissions: ModelsAPIPermissions | Unset
        if isinstance(_permissions, Unset):
            permissions = UNSET
        else:
            permissions = ModelsAPIPermissions.from_dict(_permissions) if _permissions is not None else None

        title = d.pop("title", UNSET)

        token = d.pop("token", UNSET)

        models_api_token = cls(
            created=created,
            expires_at=expires_at,
            id=id,
            permissions=permissions,
            title=title,
            token=token,
        )

        models_api_token.additional_properties = d
        return models_api_token

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
