from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.user_user import UserUser


T = TypeVar("T", bound="ModelsWebhook")


@_attrs_define
class ModelsWebhook:
    """
    Attributes:
        basic_auth_password (str | Unset):
        basic_auth_user (str | Unset): If provided, webhook requests will be sent with a Basic Auth header.
        created (str | Unset): A timestamp when this webhook target was created. You cannot change this value.
        created_by (UserUser | Unset):
        events (list[str] | Unset): The webhook events which should fire this webhook target
        id (int | Unset): The generated ID of this webhook target
        project_id (int | Unset): The project ID of the project this webhook target belongs to
        secret (str | Unset): If provided, webhook requests will be signed using HMAC. Check out the docs about how to
            use this: https://vikunja.io/docs/webhooks/#signing
        target_url (str | Unset): The target URL where the POST request with the webhook payload will be made
        updated (str | Unset): A timestamp when this webhook target was last updated. You cannot change this value.
        user_id (int | Unset): The user ID if this is a user-level webhook (mutually exclusive with ProjectID)
    """

    basic_auth_password: str | Unset = UNSET
    basic_auth_user: str | Unset = UNSET
    created: str | Unset = UNSET
    created_by: UserUser | Unset = UNSET
    events: list[str] | Unset = UNSET
    id: int | Unset = UNSET
    project_id: int | Unset = UNSET
    secret: str | Unset = UNSET
    target_url: str | Unset = UNSET
    updated: str | Unset = UNSET
    user_id: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        basic_auth_password = self.basic_auth_password

        basic_auth_user = self.basic_auth_user

        created = self.created

        created_by: dict[str, Any] | Unset = UNSET
        if not isinstance(self.created_by, Unset):
            created_by = self.created_by.to_dict()

        events: list[str] | Unset = UNSET
        if not isinstance(self.events, Unset):
            events = self.events

        id = self.id

        project_id = self.project_id

        secret = self.secret

        target_url = self.target_url

        updated = self.updated

        user_id = self.user_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if basic_auth_password is not UNSET:
            field_dict["basic_auth_password"] = basic_auth_password
        if basic_auth_user is not UNSET:
            field_dict["basic_auth_user"] = basic_auth_user
        if created is not UNSET:
            field_dict["created"] = created
        if created_by is not UNSET:
            field_dict["created_by"] = created_by
        if events is not UNSET:
            field_dict["events"] = events
        if id is not UNSET:
            field_dict["id"] = id
        if project_id is not UNSET:
            field_dict["project_id"] = project_id
        if secret is not UNSET:
            field_dict["secret"] = secret
        if target_url is not UNSET:
            field_dict["target_url"] = target_url
        if updated is not UNSET:
            field_dict["updated"] = updated
        if user_id is not UNSET:
            field_dict["user_id"] = user_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.user_user import UserUser

        d = dict(src_dict)
        basic_auth_password = d.pop("basic_auth_password", UNSET)

        basic_auth_user = d.pop("basic_auth_user", UNSET)

        created = d.pop("created", UNSET)

        _created_by = d.pop("created_by", UNSET)
        created_by: UserUser | Unset
        if isinstance(_created_by, Unset):
            created_by = UNSET
        else:
            created_by = UserUser.from_dict(_created_by) if _created_by is not None else None

        events = cast(list[str], d.pop("events", UNSET))

        id = d.pop("id", UNSET)

        project_id = d.pop("project_id", UNSET)

        secret = d.pop("secret", UNSET)

        target_url = d.pop("target_url", UNSET)

        updated = d.pop("updated", UNSET)

        user_id = d.pop("user_id", UNSET)

        models_webhook = cls(
            basic_auth_password=basic_auth_password,
            basic_auth_user=basic_auth_user,
            created=created,
            created_by=created_by,
            events=events,
            id=id,
            project_id=project_id,
            secret=secret,
            target_url=target_url,
            updated=updated,
            user_id=user_id,
        )

        models_webhook.additional_properties = d
        return models_webhook

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
