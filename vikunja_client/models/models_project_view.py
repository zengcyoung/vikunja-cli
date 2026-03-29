from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.models_project_view_bucket_configuration_mode import (
    ModelsProjectViewBucketConfigurationMode,
    check_models_project_view_bucket_configuration_mode,
)
from ..models.models_project_view_view_kind import (
    ModelsProjectViewViewKind,
    check_models_project_view_view_kind,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.models_project_view_bucket_configuration import (
        ModelsProjectViewBucketConfiguration,
    )
    from ..models.models_task_collection import ModelsTaskCollection


T = TypeVar("T", bound="ModelsProjectView")


@_attrs_define
class ModelsProjectView:
    """
    Attributes:
        bucket_configuration (list[ModelsProjectViewBucketConfiguration] | Unset): When the bucket configuration mode is
            not `manual`, this field holds the options of that configuration.
        bucket_configuration_mode (ModelsProjectViewBucketConfigurationMode | Unset): The bucket configuration mode. Can
            be `none`, `manual` or `filter`. `manual` allows to move tasks between buckets as you normally would. `filter`
            creates buckets based on a filter for each bucket.
        created (str | Unset): A timestamp when this reaction was created. You cannot change this value.
        default_bucket_id (int | Unset): The ID of the bucket where new tasks without a bucket are added to. By default,
            this is the leftmost bucket in a view.
        done_bucket_id (int | Unset): If tasks are moved to the done bucket, they are marked as done. If they are marked
            as done individually, they are moved into the done bucket.
        filter_ (ModelsTaskCollection | Unset):
        id (int | Unset): The unique numeric id of this view
        position (float | Unset): The position of this view in the list. The list of all views will be sorted by this
            parameter.
        project_id (int | Unset): The project this view belongs to
        title (str | Unset): The title of this view
        updated (str | Unset): A timestamp when this view was updated. You cannot change this value.
        view_kind (ModelsProjectViewViewKind | Unset): The kind of this view. Can be `list`, `gantt`, `table` or
            `kanban`.
    """

    bucket_configuration: list[ModelsProjectViewBucketConfiguration] | Unset = UNSET
    bucket_configuration_mode: ModelsProjectViewBucketConfigurationMode | Unset = UNSET
    created: str | Unset = UNSET
    default_bucket_id: int | Unset = UNSET
    done_bucket_id: int | Unset = UNSET
    filter_: ModelsTaskCollection | Unset = UNSET
    id: int | Unset = UNSET
    position: float | Unset = UNSET
    project_id: int | Unset = UNSET
    title: str | Unset = UNSET
    updated: str | Unset = UNSET
    view_kind: ModelsProjectViewViewKind | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        bucket_configuration: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.bucket_configuration, Unset):
            bucket_configuration = []
            for bucket_configuration_item_data in self.bucket_configuration:
                bucket_configuration_item = bucket_configuration_item_data.to_dict()
                bucket_configuration.append(bucket_configuration_item)

        bucket_configuration_mode: str | Unset = UNSET
        if not isinstance(self.bucket_configuration_mode, Unset):
            bucket_configuration_mode = self.bucket_configuration_mode

        created = self.created

        default_bucket_id = self.default_bucket_id

        done_bucket_id = self.done_bucket_id

        filter_: dict[str, Any] | Unset = UNSET
        if not isinstance(self.filter_, Unset):
            filter_ = self.filter_.to_dict()

        id = self.id

        position = self.position

        project_id = self.project_id

        title = self.title

        updated = self.updated

        view_kind: str | Unset = UNSET
        if not isinstance(self.view_kind, Unset):
            view_kind = self.view_kind

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if bucket_configuration is not UNSET:
            field_dict["bucket_configuration"] = bucket_configuration
        if bucket_configuration_mode is not UNSET:
            field_dict["bucket_configuration_mode"] = bucket_configuration_mode
        if created is not UNSET:
            field_dict["created"] = created
        if default_bucket_id is not UNSET:
            field_dict["default_bucket_id"] = default_bucket_id
        if done_bucket_id is not UNSET:
            field_dict["done_bucket_id"] = done_bucket_id
        if filter_ is not UNSET:
            field_dict["filter"] = filter_
        if id is not UNSET:
            field_dict["id"] = id
        if position is not UNSET:
            field_dict["position"] = position
        if project_id is not UNSET:
            field_dict["project_id"] = project_id
        if title is not UNSET:
            field_dict["title"] = title
        if updated is not UNSET:
            field_dict["updated"] = updated
        if view_kind is not UNSET:
            field_dict["view_kind"] = view_kind

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.models_project_view_bucket_configuration import (
            ModelsProjectViewBucketConfiguration,
        )
        from ..models.models_task_collection import ModelsTaskCollection

        d = dict(src_dict)
        _bucket_configuration = d.pop("bucket_configuration", UNSET)
        bucket_configuration: list[ModelsProjectViewBucketConfiguration] | Unset = UNSET
        if _bucket_configuration is not UNSET:
            bucket_configuration = []
            for bucket_configuration_item_data in _bucket_configuration:
                bucket_configuration_item = (
                    ModelsProjectViewBucketConfiguration.from_dict(
                        bucket_configuration_item_data
                    )
                )

                bucket_configuration.append(bucket_configuration_item)

        _bucket_configuration_mode = d.pop("bucket_configuration_mode", UNSET)
        bucket_configuration_mode: ModelsProjectViewBucketConfigurationMode | Unset
        if isinstance(_bucket_configuration_mode, Unset):
            bucket_configuration_mode = UNSET
        else:
            bucket_configuration_mode = (
                check_models_project_view_bucket_configuration_mode(
                    _bucket_configuration_mode
                )
            )

        created = d.pop("created", UNSET)

        default_bucket_id = d.pop("default_bucket_id", UNSET)

        done_bucket_id = d.pop("done_bucket_id", UNSET)

        _filter_ = d.pop("filter", UNSET)
        filter_: ModelsTaskCollection | Unset
        if isinstance(_filter_, Unset):
            filter_ = UNSET
        else:
            filter_ = ModelsTaskCollection.from_dict(_filter_) if _filter_ is not None else None

        id = d.pop("id", UNSET)

        position = d.pop("position", UNSET)

        project_id = d.pop("project_id", UNSET)

        title = d.pop("title", UNSET)

        updated = d.pop("updated", UNSET)

        _view_kind = d.pop("view_kind", UNSET)
        view_kind: ModelsProjectViewViewKind | Unset
        if isinstance(_view_kind, Unset):
            view_kind = UNSET
        else:
            view_kind = check_models_project_view_view_kind(_view_kind)

        models_project_view = cls(
            bucket_configuration=bucket_configuration,
            bucket_configuration_mode=bucket_configuration_mode,
            created=created,
            default_bucket_id=default_bucket_id,
            done_bucket_id=done_bucket_id,
            filter_=filter_,
            id=id,
            position=position,
            project_id=project_id,
            title=title,
            updated=updated,
            view_kind=view_kind,
        )

        models_project_view.additional_properties = d
        return models_project_view

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
