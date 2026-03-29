from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.files_file import FilesFile
    from ..models.user_user import UserUser


T = TypeVar("T", bound="ModelsTaskAttachment")


@_attrs_define
class ModelsTaskAttachment:
    """
    Attributes:
        created (str | Unset):
        created_by (UserUser | Unset):
        file (FilesFile | Unset):
        id (int | Unset):
        task_id (int | Unset):
    """

    created: str | Unset = UNSET
    created_by: UserUser | Unset = UNSET
    file: FilesFile | Unset = UNSET
    id: int | Unset = UNSET
    task_id: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        created = self.created

        created_by: dict[str, Any] | Unset = UNSET
        if not isinstance(self.created_by, Unset):
            created_by = self.created_by.to_dict()

        file: dict[str, Any] | Unset = UNSET
        if not isinstance(self.file, Unset):
            file = self.file.to_dict()

        id = self.id

        task_id = self.task_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if created is not UNSET:
            field_dict["created"] = created
        if created_by is not UNSET:
            field_dict["created_by"] = created_by
        if file is not UNSET:
            field_dict["file"] = file
        if id is not UNSET:
            field_dict["id"] = id
        if task_id is not UNSET:
            field_dict["task_id"] = task_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.files_file import FilesFile
        from ..models.user_user import UserUser

        d = dict(src_dict)
        created = d.pop("created", UNSET)

        _created_by = d.pop("created_by", UNSET)
        created_by: UserUser | Unset
        if isinstance(_created_by, Unset):
            created_by = UNSET
        else:
            created_by = UserUser.from_dict(_created_by) if _created_by is not None else None

        _file = d.pop("file", UNSET)
        file: FilesFile | Unset
        if isinstance(_file, Unset):
            file = UNSET
        else:
            file = FilesFile.from_dict(_file) if _file is not None else None

        id = d.pop("id", UNSET)

        task_id = d.pop("task_id", UNSET)

        models_task_attachment = cls(
            created=created,
            created_by=created_by,
            file=file,
            id=id,
            task_id=task_id,
        )

        models_task_attachment.additional_properties = d
        return models_task_attachment

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
