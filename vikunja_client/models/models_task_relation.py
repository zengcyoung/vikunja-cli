from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.models_relation_kind import ModelsRelationKind, check_models_relation_kind
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.user_user import UserUser


T = TypeVar("T", bound="ModelsTaskRelation")


@_attrs_define
class ModelsTaskRelation:
    """
    Attributes:
        created (str | Unset): A timestamp when this label was created. You cannot change this value.
        created_by (UserUser | Unset):
        other_task_id (int | Unset): The ID of the other task, the task which is being related.
        relation_kind (ModelsRelationKind | Unset):
        task_id (int | Unset): The ID of the "base" task, the task which has a relation to another.
    """

    created: str | Unset = UNSET
    created_by: UserUser | Unset = UNSET
    other_task_id: int | Unset = UNSET
    relation_kind: ModelsRelationKind | Unset = UNSET
    task_id: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        created = self.created

        created_by: dict[str, Any] | Unset = UNSET
        if not isinstance(self.created_by, Unset):
            created_by = self.created_by.to_dict()

        other_task_id = self.other_task_id

        relation_kind: str | Unset = UNSET
        if not isinstance(self.relation_kind, Unset):
            relation_kind = self.relation_kind

        task_id = self.task_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if created is not UNSET:
            field_dict["created"] = created
        if created_by is not UNSET:
            field_dict["created_by"] = created_by
        if other_task_id is not UNSET:
            field_dict["other_task_id"] = other_task_id
        if relation_kind is not UNSET:
            field_dict["relation_kind"] = relation_kind
        if task_id is not UNSET:
            field_dict["task_id"] = task_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.user_user import UserUser

        d = dict(src_dict)
        created = d.pop("created", UNSET)

        _created_by = d.pop("created_by", UNSET)
        created_by: UserUser | Unset
        if isinstance(_created_by, Unset):
            created_by = UNSET
        else:
            created_by = UserUser.from_dict(_created_by) if _created_by is not None else None

        other_task_id = d.pop("other_task_id", UNSET)

        _relation_kind = d.pop("relation_kind", UNSET)
        relation_kind: ModelsRelationKind | Unset
        if isinstance(_relation_kind, Unset):
            relation_kind = UNSET
        else:
            relation_kind = check_models_relation_kind(_relation_kind)

        task_id = d.pop("task_id", UNSET)

        models_task_relation = cls(
            created=created,
            created_by=created_by,
            other_task_id=other_task_id,
            relation_kind=relation_kind,
            task_id=task_id,
        )

        models_task_relation.additional_properties = d
        return models_task_relation

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
