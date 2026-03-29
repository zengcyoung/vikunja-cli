from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.user_user import UserUser


T = TypeVar("T", bound="ModelsReaction")


@_attrs_define
class ModelsReaction:
    """
    Attributes:
        created (str | Unset): A timestamp when this reaction was created. You cannot change this value.
        user (UserUser | Unset):
        value (str | Unset): The actual reaction. This can be any valid utf character or text, up to a length of 20.
    """

    created: str | Unset = UNSET
    user: UserUser | Unset = UNSET
    value: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        created = self.created

        user: dict[str, Any] | Unset = UNSET
        if not isinstance(self.user, Unset):
            user = self.user.to_dict()

        value = self.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if created is not UNSET:
            field_dict["created"] = created
        if user is not UNSET:
            field_dict["user"] = user
        if value is not UNSET:
            field_dict["value"] = value

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.user_user import UserUser

        d = dict(src_dict)
        created = d.pop("created", UNSET)

        _user = d.pop("user", UNSET)
        user: UserUser | Unset
        if isinstance(_user, Unset):
            user = UNSET
        else:
            user = UserUser.from_dict(_user) if _user is not None else None

        value = d.pop("value", UNSET)

        models_reaction = cls(
            created=created,
            user=user,
            value=value,
        )

        models_reaction.additional_properties = d
        return models_reaction

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
