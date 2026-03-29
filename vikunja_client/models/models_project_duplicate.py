from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.models_project import ModelsProject


T = TypeVar("T", bound="ModelsProjectDuplicate")


@_attrs_define
class ModelsProjectDuplicate:
    """
    Attributes:
        duplicated_project (ModelsProject | Unset):
        parent_project_id (int | Unset): The target parent project
    """

    duplicated_project: ModelsProject | Unset = UNSET
    parent_project_id: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        duplicated_project: dict[str, Any] | Unset = UNSET
        if not isinstance(self.duplicated_project, Unset):
            duplicated_project = self.duplicated_project.to_dict()

        parent_project_id = self.parent_project_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if duplicated_project is not UNSET:
            field_dict["duplicated_project"] = duplicated_project
        if parent_project_id is not UNSET:
            field_dict["parent_project_id"] = parent_project_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.models_project import ModelsProject

        d = dict(src_dict)
        _duplicated_project = d.pop("duplicated_project", UNSET)
        duplicated_project: ModelsProject | Unset
        if isinstance(_duplicated_project, Unset):
            duplicated_project = UNSET
        else:
            duplicated_project = ModelsProject.from_dict(_duplicated_project) if _duplicated_project is not None else None

        parent_project_id = d.pop("parent_project_id", UNSET)

        models_project_duplicate = cls(
            duplicated_project=duplicated_project,
            parent_project_id=parent_project_id,
        )

        models_project_duplicate.additional_properties = d
        return models_project_duplicate

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
