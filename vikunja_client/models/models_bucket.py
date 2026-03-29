from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.models_task import ModelsTask
    from ..models.user_user import UserUser


T = TypeVar("T", bound="ModelsBucket")


@_attrs_define
class ModelsBucket:
    """
    Attributes:
        count (int | Unset): The number of tasks currently in this bucket
        created (str | Unset): A timestamp when this bucket was created. You cannot change this value.
        created_by (UserUser | Unset):
        id (int | Unset): The unique, numeric id of this bucket.
        limit (int | Unset): How many tasks can be at the same time on this board max
        position (float | Unset): The position this bucket has when querying all buckets. See the tasks.position
            property on how to use this.
        project_view_id (int | Unset): The project view this bucket belongs to.
        tasks (list[ModelsTask] | Unset): All tasks which belong to this bucket.
        title (str | Unset): The title of this bucket.
        updated (str | Unset): A timestamp when this bucket was last updated. You cannot change this value.
    """

    count: int | Unset = UNSET
    created: str | Unset = UNSET
    created_by: UserUser | Unset = UNSET
    id: int | Unset = UNSET
    limit: int | Unset = UNSET
    position: float | Unset = UNSET
    project_view_id: int | Unset = UNSET
    tasks: list[ModelsTask] | Unset = UNSET
    title: str | Unset = UNSET
    updated: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        count = self.count

        created = self.created

        created_by: dict[str, Any] | Unset = UNSET
        if not isinstance(self.created_by, Unset):
            created_by = self.created_by.to_dict()

        id = self.id

        limit = self.limit

        position = self.position

        project_view_id = self.project_view_id

        tasks: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.tasks, Unset):
            tasks = []
            for tasks_item_data in self.tasks:
                tasks_item = tasks_item_data.to_dict()
                tasks.append(tasks_item)

        title = self.title

        updated = self.updated

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if count is not UNSET:
            field_dict["count"] = count
        if created is not UNSET:
            field_dict["created"] = created
        if created_by is not UNSET:
            field_dict["created_by"] = created_by
        if id is not UNSET:
            field_dict["id"] = id
        if limit is not UNSET:
            field_dict["limit"] = limit
        if position is not UNSET:
            field_dict["position"] = position
        if project_view_id is not UNSET:
            field_dict["project_view_id"] = project_view_id
        if tasks is not UNSET:
            field_dict["tasks"] = tasks
        if title is not UNSET:
            field_dict["title"] = title
        if updated is not UNSET:
            field_dict["updated"] = updated

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.models_task import ModelsTask
        from ..models.user_user import UserUser

        d = dict(src_dict)
        count = d.pop("count", UNSET)

        created = d.pop("created", UNSET)

        _created_by = d.pop("created_by", UNSET)
        created_by: UserUser | Unset
        if isinstance(_created_by, Unset):
            created_by = UNSET
        else:
            created_by = UserUser.from_dict(_created_by) if _created_by is not None else None

        id = d.pop("id", UNSET)

        limit = d.pop("limit", UNSET)

        position = d.pop("position", UNSET)

        project_view_id = d.pop("project_view_id", UNSET)

        _tasks = d.pop("tasks", UNSET)
        tasks: list[ModelsTask] | Unset = UNSET
        if _tasks is not UNSET:
            tasks = []
            for tasks_item_data in _tasks:
                tasks_item = ModelsTask.from_dict(tasks_item_data)

                tasks.append(tasks_item)

        title = d.pop("title", UNSET)

        updated = d.pop("updated", UNSET)

        models_bucket = cls(
            count=count,
            created=created,
            created_by=created_by,
            id=id,
            limit=limit,
            position=position,
            project_view_id=project_view_id,
            tasks=tasks,
            title=title,
            updated=updated,
        )

        models_bucket.additional_properties = d
        return models_bucket

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
