from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.v1_ldap_auth_info import V1LdapAuthInfo
    from ..models.v1_local_auth_info import V1LocalAuthInfo
    from ..models.v1_open_id_auth_info import V1OpenIDAuthInfo


T = TypeVar("T", bound="V1AuthInfo")


@_attrs_define
class V1AuthInfo:
    """
    Attributes:
        ldap (V1LdapAuthInfo | Unset):
        local (V1LocalAuthInfo | Unset):
        openid_connect (V1OpenIDAuthInfo | Unset):
    """

    ldap: V1LdapAuthInfo | Unset = UNSET
    local: V1LocalAuthInfo | Unset = UNSET
    openid_connect: V1OpenIDAuthInfo | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        ldap: dict[str, Any] | Unset = UNSET
        if not isinstance(self.ldap, Unset):
            ldap = self.ldap.to_dict()

        local: dict[str, Any] | Unset = UNSET
        if not isinstance(self.local, Unset):
            local = self.local.to_dict()

        openid_connect: dict[str, Any] | Unset = UNSET
        if not isinstance(self.openid_connect, Unset):
            openid_connect = self.openid_connect.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if ldap is not UNSET:
            field_dict["ldap"] = ldap
        if local is not UNSET:
            field_dict["local"] = local
        if openid_connect is not UNSET:
            field_dict["openid_connect"] = openid_connect

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.v1_ldap_auth_info import V1LdapAuthInfo
        from ..models.v1_local_auth_info import V1LocalAuthInfo
        from ..models.v1_open_id_auth_info import V1OpenIDAuthInfo

        d = dict(src_dict)
        _ldap = d.pop("ldap", UNSET)
        ldap: V1LdapAuthInfo | Unset
        if isinstance(_ldap, Unset):
            ldap = UNSET
        else:
            ldap = V1LdapAuthInfo.from_dict(_ldap) if _ldap is not None else None

        _local = d.pop("local", UNSET)
        local: V1LocalAuthInfo | Unset
        if isinstance(_local, Unset):
            local = UNSET
        else:
            local = V1LocalAuthInfo.from_dict(_local) if _local is not None else None

        _openid_connect = d.pop("openid_connect", UNSET)
        openid_connect: V1OpenIDAuthInfo | Unset
        if isinstance(_openid_connect, Unset):
            openid_connect = UNSET
        else:
            openid_connect = V1OpenIDAuthInfo.from_dict(_openid_connect) if _openid_connect is not None else None

        v1_auth_info = cls(
            ldap=ldap,
            local=local,
            openid_connect=openid_connect,
        )

        v1_auth_info.additional_properties = d
        return v1_auth_info

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
