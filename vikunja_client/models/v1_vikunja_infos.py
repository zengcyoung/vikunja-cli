from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.v1_auth_info import V1AuthInfo
    from ..models.v1_legal_info import V1LegalInfo


T = TypeVar("T", bound="V1VikunjaInfos")


@_attrs_define
class V1VikunjaInfos:
    """
    Attributes:
        auth (V1AuthInfo | Unset):
        available_migrators (list[str] | Unset):
        caldav_enabled (bool | Unset):
        demo_mode_enabled (bool | Unset):
        email_reminders_enabled (bool | Unset):
        enabled_background_providers (list[str] | Unset):
        frontend_url (str | Unset):
        legal (V1LegalInfo | Unset):
        link_sharing_enabled (bool | Unset):
        max_file_size (str | Unset):
        max_items_per_page (int | Unset):
        motd (str | Unset):
        public_teams_enabled (bool | Unset):
        task_attachments_enabled (bool | Unset):
        task_comments_enabled (bool | Unset):
        totp_enabled (bool | Unset):
        user_deletion_enabled (bool | Unset):
        version (str | Unset):
        webhooks_enabled (bool | Unset):
    """

    auth: V1AuthInfo | Unset = UNSET
    available_migrators: list[str] | Unset = UNSET
    caldav_enabled: bool | Unset = UNSET
    demo_mode_enabled: bool | Unset = UNSET
    email_reminders_enabled: bool | Unset = UNSET
    enabled_background_providers: list[str] | Unset = UNSET
    frontend_url: str | Unset = UNSET
    legal: V1LegalInfo | Unset = UNSET
    link_sharing_enabled: bool | Unset = UNSET
    max_file_size: str | Unset = UNSET
    max_items_per_page: int | Unset = UNSET
    motd: str | Unset = UNSET
    public_teams_enabled: bool | Unset = UNSET
    task_attachments_enabled: bool | Unset = UNSET
    task_comments_enabled: bool | Unset = UNSET
    totp_enabled: bool | Unset = UNSET
    user_deletion_enabled: bool | Unset = UNSET
    version: str | Unset = UNSET
    webhooks_enabled: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        auth: dict[str, Any] | Unset = UNSET
        if not isinstance(self.auth, Unset):
            auth = self.auth.to_dict()

        available_migrators: list[str] | Unset = UNSET
        if not isinstance(self.available_migrators, Unset):
            available_migrators = self.available_migrators

        caldav_enabled = self.caldav_enabled

        demo_mode_enabled = self.demo_mode_enabled

        email_reminders_enabled = self.email_reminders_enabled

        enabled_background_providers: list[str] | Unset = UNSET
        if not isinstance(self.enabled_background_providers, Unset):
            enabled_background_providers = self.enabled_background_providers

        frontend_url = self.frontend_url

        legal: dict[str, Any] | Unset = UNSET
        if not isinstance(self.legal, Unset):
            legal = self.legal.to_dict()

        link_sharing_enabled = self.link_sharing_enabled

        max_file_size = self.max_file_size

        max_items_per_page = self.max_items_per_page

        motd = self.motd

        public_teams_enabled = self.public_teams_enabled

        task_attachments_enabled = self.task_attachments_enabled

        task_comments_enabled = self.task_comments_enabled

        totp_enabled = self.totp_enabled

        user_deletion_enabled = self.user_deletion_enabled

        version = self.version

        webhooks_enabled = self.webhooks_enabled

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if auth is not UNSET:
            field_dict["auth"] = auth
        if available_migrators is not UNSET:
            field_dict["available_migrators"] = available_migrators
        if caldav_enabled is not UNSET:
            field_dict["caldav_enabled"] = caldav_enabled
        if demo_mode_enabled is not UNSET:
            field_dict["demo_mode_enabled"] = demo_mode_enabled
        if email_reminders_enabled is not UNSET:
            field_dict["email_reminders_enabled"] = email_reminders_enabled
        if enabled_background_providers is not UNSET:
            field_dict["enabled_background_providers"] = enabled_background_providers
        if frontend_url is not UNSET:
            field_dict["frontend_url"] = frontend_url
        if legal is not UNSET:
            field_dict["legal"] = legal
        if link_sharing_enabled is not UNSET:
            field_dict["link_sharing_enabled"] = link_sharing_enabled
        if max_file_size is not UNSET:
            field_dict["max_file_size"] = max_file_size
        if max_items_per_page is not UNSET:
            field_dict["max_items_per_page"] = max_items_per_page
        if motd is not UNSET:
            field_dict["motd"] = motd
        if public_teams_enabled is not UNSET:
            field_dict["public_teams_enabled"] = public_teams_enabled
        if task_attachments_enabled is not UNSET:
            field_dict["task_attachments_enabled"] = task_attachments_enabled
        if task_comments_enabled is not UNSET:
            field_dict["task_comments_enabled"] = task_comments_enabled
        if totp_enabled is not UNSET:
            field_dict["totp_enabled"] = totp_enabled
        if user_deletion_enabled is not UNSET:
            field_dict["user_deletion_enabled"] = user_deletion_enabled
        if version is not UNSET:
            field_dict["version"] = version
        if webhooks_enabled is not UNSET:
            field_dict["webhooks_enabled"] = webhooks_enabled

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.v1_auth_info import V1AuthInfo
        from ..models.v1_legal_info import V1LegalInfo

        d = dict(src_dict)
        _auth = d.pop("auth", UNSET)
        auth: V1AuthInfo | Unset
        if isinstance(_auth, Unset):
            auth = UNSET
        else:
            auth = V1AuthInfo.from_dict(_auth) if _auth is not None else None

        available_migrators = cast(list[str], d.pop("available_migrators", UNSET))

        caldav_enabled = d.pop("caldav_enabled", UNSET)

        demo_mode_enabled = d.pop("demo_mode_enabled", UNSET)

        email_reminders_enabled = d.pop("email_reminders_enabled", UNSET)

        enabled_background_providers = cast(
            list[str], d.pop("enabled_background_providers", UNSET)
        )

        frontend_url = d.pop("frontend_url", UNSET)

        _legal = d.pop("legal", UNSET)
        legal: V1LegalInfo | Unset
        if isinstance(_legal, Unset):
            legal = UNSET
        else:
            legal = V1LegalInfo.from_dict(_legal) if _legal is not None else None

        link_sharing_enabled = d.pop("link_sharing_enabled", UNSET)

        max_file_size = d.pop("max_file_size", UNSET)

        max_items_per_page = d.pop("max_items_per_page", UNSET)

        motd = d.pop("motd", UNSET)

        public_teams_enabled = d.pop("public_teams_enabled", UNSET)

        task_attachments_enabled = d.pop("task_attachments_enabled", UNSET)

        task_comments_enabled = d.pop("task_comments_enabled", UNSET)

        totp_enabled = d.pop("totp_enabled", UNSET)

        user_deletion_enabled = d.pop("user_deletion_enabled", UNSET)

        version = d.pop("version", UNSET)

        webhooks_enabled = d.pop("webhooks_enabled", UNSET)

        v1_vikunja_infos = cls(
            auth=auth,
            available_migrators=available_migrators,
            caldav_enabled=caldav_enabled,
            demo_mode_enabled=demo_mode_enabled,
            email_reminders_enabled=email_reminders_enabled,
            enabled_background_providers=enabled_background_providers,
            frontend_url=frontend_url,
            legal=legal,
            link_sharing_enabled=link_sharing_enabled,
            max_file_size=max_file_size,
            max_items_per_page=max_items_per_page,
            motd=motd,
            public_teams_enabled=public_teams_enabled,
            task_attachments_enabled=task_attachments_enabled,
            task_comments_enabled=task_comments_enabled,
            totp_enabled=totp_enabled,
            user_deletion_enabled=user_deletion_enabled,
            version=version,
            webhooks_enabled=webhooks_enabled,
        )

        v1_vikunja_infos.additional_properties = d
        return v1_vikunja_infos

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
