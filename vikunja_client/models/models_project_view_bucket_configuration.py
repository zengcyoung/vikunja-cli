from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.models_task_collection import ModelsTaskCollection


T = TypeVar("T", bound="ModelsProjectViewBucketConfiguration")


@_attrs_define
class ModelsProjectViewBucketConfiguration:
    """
    Attributes:
        filter_ (ModelsTaskCollection | Unset):
        title (str | Unset):
    """

    filter_: ModelsTaskCollection | Unset = UNSET
    title: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        filter_: dict[str, Any] | Unset = UNSET
        if not isinstance(self.filter_, Unset):
            filter_ = self.filter_.to_dict()

        title = self.title

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if filter_ is not UNSET:
            field_dict["filter"] = filter_
        if title is not UNSET:
            field_dict["title"] = title

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.models_task_collection import ModelsTaskCollection

        d = dict(src_dict)
        _filter_ = d.pop("filter", UNSET)
        filter_: ModelsTaskCollection | Unset
        if isinstance(_filter_, Unset):
            filter_ = UNSET
        else:
            filter_ = ModelsTaskCollection.from_dict(_filter_) if _filter_ is not None else None

        title = d.pop("title", UNSET)

        models_project_view_bucket_configuration = cls(
            filter_=filter_,
            title=title,
        )

        models_project_view_bucket_configuration.additional_properties = d
        return models_project_view_bucket_configuration

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
