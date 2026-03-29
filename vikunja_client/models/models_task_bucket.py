from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.models_bucket import ModelsBucket
    from ..models.models_task import ModelsTask


T = TypeVar("T", bound="ModelsTaskBucket")


@_attrs_define
class ModelsTaskBucket:
    """
    Attributes:
        bucket (ModelsBucket | Unset):
        bucket_id (int | Unset):
        project_view_id (int | Unset): The view this bucket belongs to. Combined with TaskID this forms a
            unique index.
        task (ModelsTask | Unset):
        task_id (int | Unset): The task which belongs to the bucket. Together with ProjectViewID
            this field is part of a unique index to prevent duplicates.
    """

    bucket: ModelsBucket | Unset = UNSET
    bucket_id: int | Unset = UNSET
    project_view_id: int | Unset = UNSET
    task: ModelsTask | Unset = UNSET
    task_id: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        bucket: dict[str, Any] | Unset = UNSET
        if not isinstance(self.bucket, Unset):
            bucket = self.bucket.to_dict()

        bucket_id = self.bucket_id

        project_view_id = self.project_view_id

        task: dict[str, Any] | Unset = UNSET
        if not isinstance(self.task, Unset):
            task = self.task.to_dict()

        task_id = self.task_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if bucket is not UNSET:
            field_dict["bucket"] = bucket
        if bucket_id is not UNSET:
            field_dict["bucket_id"] = bucket_id
        if project_view_id is not UNSET:
            field_dict["project_view_id"] = project_view_id
        if task is not UNSET:
            field_dict["task"] = task
        if task_id is not UNSET:
            field_dict["task_id"] = task_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.models_bucket import ModelsBucket
        from ..models.models_task import ModelsTask

        d = dict(src_dict)
        _bucket = d.pop("bucket", UNSET)
        bucket: ModelsBucket | Unset
        if isinstance(_bucket, Unset):
            bucket = UNSET
        else:
            bucket = ModelsBucket.from_dict(_bucket) if _bucket is not None else None

        bucket_id = d.pop("bucket_id", UNSET)

        project_view_id = d.pop("project_view_id", UNSET)

        _task = d.pop("task", UNSET)
        task: ModelsTask | Unset
        if isinstance(_task, Unset):
            task = UNSET
        else:
            task = ModelsTask.from_dict(_task) if _task is not None else None

        task_id = d.pop("task_id", UNSET)

        models_task_bucket = cls(
            bucket=bucket,
            bucket_id=bucket_id,
            project_view_id=project_view_id,
            task=task,
            task_id=task_id,
        )

        models_task_bucket.additional_properties = d
        return models_task_bucket

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
