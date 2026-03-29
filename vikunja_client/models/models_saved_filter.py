from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.models_task_collection import ModelsTaskCollection
    from ..models.user_user import UserUser


T = TypeVar("T", bound="ModelsSavedFilter")


@_attrs_define
class ModelsSavedFilter:
    """
    Attributes:
        created (str | Unset): A timestamp when this filter was created. You cannot change this value.
        description (str | Unset): The description of the filter
        filters (ModelsTaskCollection | Unset):
        id (int | Unset): The unique numeric id of this saved filter
        is_favorite (bool | Unset): True if the filter is a favorite. Favorite filters show up in a separate parent
            project together with favorite projects.
        owner (UserUser | Unset):
        title (str | Unset): The title of the filter.
        updated (str | Unset): A timestamp when this filter was last updated. You cannot change this value.
    """

    created: str | Unset = UNSET
    description: str | Unset = UNSET
    filters: ModelsTaskCollection | Unset = UNSET
    id: int | Unset = UNSET
    is_favorite: bool | Unset = UNSET
    owner: UserUser | Unset = UNSET
    title: str | Unset = UNSET
    updated: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        created = self.created

        description = self.description

        filters: dict[str, Any] | Unset = UNSET
        if not isinstance(self.filters, Unset):
            filters = self.filters.to_dict()

        id = self.id

        is_favorite = self.is_favorite

        owner: dict[str, Any] | Unset = UNSET
        if not isinstance(self.owner, Unset):
            owner = self.owner.to_dict()

        title = self.title

        updated = self.updated

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if created is not UNSET:
            field_dict["created"] = created
        if description is not UNSET:
            field_dict["description"] = description
        if filters is not UNSET:
            field_dict["filters"] = filters
        if id is not UNSET:
            field_dict["id"] = id
        if is_favorite is not UNSET:
            field_dict["is_favorite"] = is_favorite
        if owner is not UNSET:
            field_dict["owner"] = owner
        if title is not UNSET:
            field_dict["title"] = title
        if updated is not UNSET:
            field_dict["updated"] = updated

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.models_task_collection import ModelsTaskCollection
        from ..models.user_user import UserUser

        d = dict(src_dict)
        created = d.pop("created", UNSET)

        description = d.pop("description", UNSET)

        _filters = d.pop("filters", UNSET)
        filters: ModelsTaskCollection | Unset
        if isinstance(_filters, Unset):
            filters = UNSET
        else:
            filters = ModelsTaskCollection.from_dict(_filters) if _filters is not None else None

        id = d.pop("id", UNSET)

        is_favorite = d.pop("is_favorite", UNSET)

        _owner = d.pop("owner", UNSET)
        owner: UserUser | Unset
        if isinstance(_owner, Unset):
            owner = UNSET
        else:
            owner = UserUser.from_dict(_owner) if _owner is not None else None

        title = d.pop("title", UNSET)

        updated = d.pop("updated", UNSET)

        models_saved_filter = cls(
            created=created,
            description=description,
            filters=filters,
            id=id,
            is_favorite=is_favorite,
            owner=owner,
            title=title,
            updated=updated,
        )

        models_saved_filter.additional_properties = d
        return models_saved_filter

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
