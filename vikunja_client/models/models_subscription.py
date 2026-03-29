from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ModelsSubscription")


@_attrs_define
class ModelsSubscription:
    """
    Attributes:
        created (str | Unset): A timestamp when this subscription was created. You cannot change this value.
        entity (int | Unset):
        entity_id (int | Unset): The id of the entity to subscribe to.
        id (int | Unset): The numeric ID of the subscription
    """

    created: str | Unset = UNSET
    entity: int | Unset = UNSET
    entity_id: int | Unset = UNSET
    id: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        created = self.created

        entity = self.entity

        entity_id = self.entity_id

        id = self.id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if created is not UNSET:
            field_dict["created"] = created
        if entity is not UNSET:
            field_dict["entity"] = entity
        if entity_id is not UNSET:
            field_dict["entity_id"] = entity_id
        if id is not UNSET:
            field_dict["id"] = id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        created = d.pop("created", UNSET)

        entity = d.pop("entity", UNSET)

        entity_id = d.pop("entity_id", UNSET)

        id = d.pop("id", UNSET)

        models_subscription = cls(
            created=created,
            entity=entity,
            entity_id=entity_id,
            id=id,
        )

        models_subscription.additional_properties = d
        return models_subscription

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
