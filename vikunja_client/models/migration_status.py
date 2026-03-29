from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="MigrationStatus")


@_attrs_define
class MigrationStatus:
    """
    Attributes:
        finished_at (str | Unset):
        id (int | Unset):
        migrator_name (str | Unset):
        started_at (str | Unset):
    """

    finished_at: str | Unset = UNSET
    id: int | Unset = UNSET
    migrator_name: str | Unset = UNSET
    started_at: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        finished_at = self.finished_at

        id = self.id

        migrator_name = self.migrator_name

        started_at = self.started_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if finished_at is not UNSET:
            field_dict["finished_at"] = finished_at
        if id is not UNSET:
            field_dict["id"] = id
        if migrator_name is not UNSET:
            field_dict["migrator_name"] = migrator_name
        if started_at is not UNSET:
            field_dict["started_at"] = started_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        finished_at = d.pop("finished_at", UNSET)

        id = d.pop("id", UNSET)

        migrator_name = d.pop("migrator_name", UNSET)

        started_at = d.pop("started_at", UNSET)

        migration_status = cls(
            finished_at=finished_at,
            id=id,
            migrator_name=migrator_name,
            started_at=started_at,
        )

        migration_status.additional_properties = d
        return migration_status

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
