from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ModelsDatabaseNotifications")


@_attrs_define
class ModelsDatabaseNotifications:
    """
    Attributes:
        created (str | Unset): A timestamp when this notification was created. You cannot change this value.
        id (int | Unset): The unique, numeric id of this notification.
        name (str | Unset): The name of the notification
        notification (Any | Unset): The actual content of the notification.
        read (bool | Unset): Whether or not to mark this notification as read or unread.
            True is read, false is unread.
        read_at (str | Unset): When this notification is marked as read, this will be updated with the current
            timestamp.
    """

    created: str | Unset = UNSET
    id: int | Unset = UNSET
    name: str | Unset = UNSET
    notification: Any | Unset = UNSET
    read: bool | Unset = UNSET
    read_at: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        created = self.created

        id = self.id

        name = self.name

        notification = self.notification

        read = self.read

        read_at = self.read_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if created is not UNSET:
            field_dict["created"] = created
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if notification is not UNSET:
            field_dict["notification"] = notification
        if read is not UNSET:
            field_dict["read"] = read
        if read_at is not UNSET:
            field_dict["read_at"] = read_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        created = d.pop("created", UNSET)

        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        notification = d.pop("notification", UNSET)

        read = d.pop("read", UNSET)

        read_at = d.pop("read_at", UNSET)

        models_database_notifications = cls(
            created=created,
            id=id,
            name=name,
            notification=notification,
            read=read,
            read_at=read_at,
        )

        models_database_notifications.additional_properties = d
        return models_database_notifications

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
