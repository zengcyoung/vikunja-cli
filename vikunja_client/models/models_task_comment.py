from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.models_reaction_map import ModelsReactionMap
    from ..models.user_user import UserUser


T = TypeVar("T", bound="ModelsTaskComment")


@_attrs_define
class ModelsTaskComment:
    """
    Attributes:
        author (UserUser | Unset):
        comment (str | Unset):
        created (str | Unset):
        id (int | Unset):
        reactions (ModelsReactionMap | Unset):
        updated (str | Unset):
    """

    author: UserUser | Unset = UNSET
    comment: str | Unset = UNSET
    created: str | Unset = UNSET
    id: int | Unset = UNSET
    reactions: ModelsReactionMap | Unset = UNSET
    updated: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        author: dict[str, Any] | Unset = UNSET
        if not isinstance(self.author, Unset):
            author = self.author.to_dict()

        comment = self.comment

        created = self.created

        id = self.id

        reactions: dict[str, Any] | Unset = UNSET
        if not isinstance(self.reactions, Unset):
            reactions = self.reactions.to_dict()

        updated = self.updated

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if author is not UNSET:
            field_dict["author"] = author
        if comment is not UNSET:
            field_dict["comment"] = comment
        if created is not UNSET:
            field_dict["created"] = created
        if id is not UNSET:
            field_dict["id"] = id
        if reactions is not UNSET:
            field_dict["reactions"] = reactions
        if updated is not UNSET:
            field_dict["updated"] = updated

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.models_reaction_map import ModelsReactionMap
        from ..models.user_user import UserUser

        d = dict(src_dict)
        _author = d.pop("author", UNSET)
        author: UserUser | Unset
        if isinstance(_author, Unset):
            author = UNSET
        else:
            author = UserUser.from_dict(_author) if _author is not None else None

        comment = d.pop("comment", UNSET)

        created = d.pop("created", UNSET)

        id = d.pop("id", UNSET)

        _reactions = d.pop("reactions", UNSET)
        reactions: ModelsReactionMap | Unset
        if isinstance(_reactions, Unset):
            reactions = UNSET
        else:
            reactions = ModelsReactionMap.from_dict(_reactions) if _reactions is not None else None

        updated = d.pop("updated", UNSET)

        models_task_comment = cls(
            author=author,
            comment=comment,
            created=created,
            id=id,
            reactions=reactions,
            updated=updated,
        )

        models_task_comment.additional_properties = d
        return models_task_comment

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
