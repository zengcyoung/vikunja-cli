from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.v1_user_settings_extra_settings_links import (
        V1UserSettingsExtraSettingsLinks,
    )


T = TypeVar("T", bound="V1UserSettings")


@_attrs_define
class V1UserSettings:
    """
    Attributes:
        default_project_id (int | Unset): If a task is created without a specified project this value should be used.
            Applies
            to tasks made directly in API and from clients.
        discoverable_by_email (bool | Unset): If true, the user can be found when searching for their exact email.
        discoverable_by_name (bool | Unset): If true, this user can be found by their name or parts of it when searching
            for it.
        email_reminders_enabled (bool | Unset): If enabled, sends email reminders of tasks to the user.
        extra_settings_links (V1UserSettingsExtraSettingsLinks | Unset): Additional settings links as provided by openid
        frontend_settings (Any | Unset): Additional settings only used by the frontend
        language (str | Unset): The user's language
        name (str | Unset): The new name of the current user.
        overdue_tasks_reminders_enabled (bool | Unset): If enabled, the user will get an email for their overdue tasks
            each morning.
        overdue_tasks_reminders_time (str | Unset): The time when the daily summary of overdue tasks will be sent via
            email.
        timezone (str | Unset): The user's time zone. Used to send task reminders in the time zone of the user.
        week_start (int | Unset): The day when the week starts for this user. 0 = sunday, 1 = monday, etc.
    """

    default_project_id: int | Unset = UNSET
    discoverable_by_email: bool | Unset = UNSET
    discoverable_by_name: bool | Unset = UNSET
    email_reminders_enabled: bool | Unset = UNSET
    extra_settings_links: V1UserSettingsExtraSettingsLinks | Unset = UNSET
    frontend_settings: Any | Unset = UNSET
    language: str | Unset = UNSET
    name: str | Unset = UNSET
    overdue_tasks_reminders_enabled: bool | Unset = UNSET
    overdue_tasks_reminders_time: str | Unset = UNSET
    timezone: str | Unset = UNSET
    week_start: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        default_project_id = self.default_project_id

        discoverable_by_email = self.discoverable_by_email

        discoverable_by_name = self.discoverable_by_name

        email_reminders_enabled = self.email_reminders_enabled

        extra_settings_links: dict[str, Any] | Unset = UNSET
        if not isinstance(self.extra_settings_links, Unset):
            extra_settings_links = self.extra_settings_links.to_dict()

        frontend_settings = self.frontend_settings

        language = self.language

        name = self.name

        overdue_tasks_reminders_enabled = self.overdue_tasks_reminders_enabled

        overdue_tasks_reminders_time = self.overdue_tasks_reminders_time

        timezone = self.timezone

        week_start = self.week_start

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if default_project_id is not UNSET:
            field_dict["default_project_id"] = default_project_id
        if discoverable_by_email is not UNSET:
            field_dict["discoverable_by_email"] = discoverable_by_email
        if discoverable_by_name is not UNSET:
            field_dict["discoverable_by_name"] = discoverable_by_name
        if email_reminders_enabled is not UNSET:
            field_dict["email_reminders_enabled"] = email_reminders_enabled
        if extra_settings_links is not UNSET:
            field_dict["extra_settings_links"] = extra_settings_links
        if frontend_settings is not UNSET:
            field_dict["frontend_settings"] = frontend_settings
        if language is not UNSET:
            field_dict["language"] = language
        if name is not UNSET:
            field_dict["name"] = name
        if overdue_tasks_reminders_enabled is not UNSET:
            field_dict["overdue_tasks_reminders_enabled"] = (
                overdue_tasks_reminders_enabled
            )
        if overdue_tasks_reminders_time is not UNSET:
            field_dict["overdue_tasks_reminders_time"] = overdue_tasks_reminders_time
        if timezone is not UNSET:
            field_dict["timezone"] = timezone
        if week_start is not UNSET:
            field_dict["week_start"] = week_start

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.v1_user_settings_extra_settings_links import (
            V1UserSettingsExtraSettingsLinks,
        )

        d = dict(src_dict)
        default_project_id = d.pop("default_project_id", UNSET)

        discoverable_by_email = d.pop("discoverable_by_email", UNSET)

        discoverable_by_name = d.pop("discoverable_by_name", UNSET)

        email_reminders_enabled = d.pop("email_reminders_enabled", UNSET)

        _extra_settings_links = d.pop("extra_settings_links", UNSET)
        extra_settings_links: V1UserSettingsExtraSettingsLinks | Unset
        if isinstance(_extra_settings_links, Unset):
            extra_settings_links = UNSET
        else:
            extra_settings_links = V1UserSettingsExtraSettingsLinks.from_dict(
                _extra_settings_links
            )

        frontend_settings = d.pop("frontend_settings", UNSET)

        language = d.pop("language", UNSET)

        name = d.pop("name", UNSET)

        overdue_tasks_reminders_enabled = d.pop(
            "overdue_tasks_reminders_enabled", UNSET
        )

        overdue_tasks_reminders_time = d.pop("overdue_tasks_reminders_time", UNSET)

        timezone = d.pop("timezone", UNSET)

        week_start = d.pop("week_start", UNSET)

        v1_user_settings = cls(
            default_project_id=default_project_id,
            discoverable_by_email=discoverable_by_email,
            discoverable_by_name=discoverable_by_name,
            email_reminders_enabled=email_reminders_enabled,
            extra_settings_links=extra_settings_links,
            frontend_settings=frontend_settings,
            language=language,
            name=name,
            overdue_tasks_reminders_enabled=overdue_tasks_reminders_enabled,
            overdue_tasks_reminders_time=overdue_tasks_reminders_time,
            timezone=timezone,
            week_start=week_start,
        )

        v1_user_settings.additional_properties = d
        return v1_user_settings

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
