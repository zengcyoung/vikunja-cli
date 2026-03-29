from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ModelsTaskCollection")


@_attrs_define
class ModelsTaskCollection:
    """
    Attributes:
        filter_ (str | Unset): The filter query to match tasks by. Check out https://vikunja.io/docs/filters for a full
            explanation.
        filter_include_nulls (bool | Unset): If set to true, the result will also include null values
        order_by (list[str] | Unset): The query parameter to order the items by. This can be either asc or desc, with
            asc being the default.
        s (str | Unset):
        sort_by (list[str] | Unset): The query parameter to sort by. This is for ex. done, priority, etc.
    """

    filter_: str | Unset = UNSET
    filter_include_nulls: bool | Unset = UNSET
    order_by: list[str] | Unset = UNSET
    s: str | Unset = UNSET
    sort_by: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        filter_ = self.filter_

        filter_include_nulls = self.filter_include_nulls

        order_by: list[str] | Unset = UNSET
        if not isinstance(self.order_by, Unset):
            order_by = self.order_by

        s = self.s

        sort_by: list[str] | Unset = UNSET
        if not isinstance(self.sort_by, Unset):
            sort_by = self.sort_by

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if filter_ is not UNSET:
            field_dict["filter"] = filter_
        if filter_include_nulls is not UNSET:
            field_dict["filter_include_nulls"] = filter_include_nulls
        if order_by is not UNSET:
            field_dict["order_by"] = order_by
        if s is not UNSET:
            field_dict["s"] = s
        if sort_by is not UNSET:
            field_dict["sort_by"] = sort_by

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        filter_ = d.pop("filter", UNSET)

        filter_include_nulls = d.pop("filter_include_nulls", UNSET)

        order_by = cast(list[str], d.pop("order_by", UNSET))

        s = d.pop("s", UNSET)

        sort_by = cast(list[str], d.pop("sort_by", UNSET))

        models_task_collection = cls(
            filter_=filter_,
            filter_include_nulls=filter_include_nulls,
            order_by=order_by,
            s=s,
            sort_by=sort_by,
        )

        models_task_collection.additional_properties = d
        return models_task_collection

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
