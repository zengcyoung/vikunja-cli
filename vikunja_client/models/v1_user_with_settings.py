from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.v1_user_settings import V1UserSettings


T = TypeVar("T", bound="V1UserWithSettings")


@_attrs_define
class V1UserWithSettings:
    """
    Attributes:
        auth_provider (str | Unset):
        created (str | Unset): A timestamp when this task was created. You cannot change this value.
        deletion_scheduled_at (str | Unset):
        email (str | Unset): The user's email address.
        id (int | Unset): The unique, numeric id of this user.
        is_local_user (bool | Unset):
        name (str | Unset): The full name of the user.
        settings (V1UserSettings | Unset):
        updated (str | Unset): A timestamp when this task was last updated. You cannot change this value.
        username (str | Unset): The username of the user. Is always unique.
    """

    auth_provider: str | Unset = UNSET
    created: str | Unset = UNSET
    deletion_scheduled_at: str | Unset = UNSET
    email: str | Unset = UNSET
    id: int | Unset = UNSET
    is_local_user: bool | Unset = UNSET
    name: str | Unset = UNSET
    settings: V1UserSettings | Unset = UNSET
    updated: str | Unset = UNSET
    username: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        auth_provider = self.auth_provider

        created = self.created

        deletion_scheduled_at = self.deletion_scheduled_at

        email = self.email

        id = self.id

        is_local_user = self.is_local_user

        name = self.name

        settings: dict[str, Any] | Unset = UNSET
        if not isinstance(self.settings, Unset):
            settings = self.settings.to_dict()

        updated = self.updated

        username = self.username

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if auth_provider is not UNSET:
            field_dict["auth_provider"] = auth_provider
        if created is not UNSET:
            field_dict["created"] = created
        if deletion_scheduled_at is not UNSET:
            field_dict["deletion_scheduled_at"] = deletion_scheduled_at
        if email is not UNSET:
            field_dict["email"] = email
        if id is not UNSET:
            field_dict["id"] = id
        if is_local_user is not UNSET:
            field_dict["is_local_user"] = is_local_user
        if name is not UNSET:
            field_dict["name"] = name
        if settings is not UNSET:
            field_dict["settings"] = settings
        if updated is not UNSET:
            field_dict["updated"] = updated
        if username is not UNSET:
            field_dict["username"] = username

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.v1_user_settings import V1UserSettings

        d = dict(src_dict)
        auth_provider = d.pop("auth_provider", UNSET)

        created = d.pop("created", UNSET)

        deletion_scheduled_at = d.pop("deletion_scheduled_at", UNSET)

        email = d.pop("email", UNSET)

        id = d.pop("id", UNSET)

        is_local_user = d.pop("is_local_user", UNSET)

        name = d.pop("name", UNSET)

        _settings = d.pop("settings", UNSET)
        settings: V1UserSettings | Unset
        if isinstance(_settings, Unset):
            settings = UNSET
        else:
            settings = V1UserSettings.from_dict(_settings) if _settings is not None else None

        updated = d.pop("updated", UNSET)

        username = d.pop("username", UNSET)

        v1_user_with_settings = cls(
            auth_provider=auth_provider,
            created=created,
            deletion_scheduled_at=deletion_scheduled_at,
            email=email,
            id=id,
            is_local_user=is_local_user,
            name=name,
            settings=settings,
            updated=updated,
            username=username,
        )

        v1_user_with_settings.additional_properties = d
        return v1_user_with_settings

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
