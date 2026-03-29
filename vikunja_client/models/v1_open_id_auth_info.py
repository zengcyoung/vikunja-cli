from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.code_vikunja_io_api_pkg_modules_auth_openid_provider import (
        CodeVikunjaIoApiPkgModulesAuthOpenidProvider,
    )


T = TypeVar("T", bound="V1OpenIDAuthInfo")


@_attrs_define
class V1OpenIDAuthInfo:
    """
    Attributes:
        enabled (bool | Unset):
        providers (list[CodeVikunjaIoApiPkgModulesAuthOpenidProvider] | Unset):
    """

    enabled: bool | Unset = UNSET
    providers: list[CodeVikunjaIoApiPkgModulesAuthOpenidProvider] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        enabled = self.enabled

        providers: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.providers, Unset):
            providers = []
            for providers_item_data in self.providers:
                providers_item = providers_item_data.to_dict()
                providers.append(providers_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if enabled is not UNSET:
            field_dict["enabled"] = enabled
        if providers is not UNSET:
            field_dict["providers"] = providers

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.code_vikunja_io_api_pkg_modules_auth_openid_provider import (
            CodeVikunjaIoApiPkgModulesAuthOpenidProvider,
        )

        d = dict(src_dict)
        enabled = d.pop("enabled", UNSET)

        _providers = d.pop("providers", UNSET)
        providers: list[CodeVikunjaIoApiPkgModulesAuthOpenidProvider] | Unset = UNSET
        if _providers is not UNSET:
            providers = []
            for providers_item_data in _providers:
                providers_item = CodeVikunjaIoApiPkgModulesAuthOpenidProvider.from_dict(
                    providers_item_data
                )

                providers.append(providers_item)

        v1_open_id_auth_info = cls(
            enabled=enabled,
            providers=providers,
        )

        v1_open_id_auth_info.additional_properties = d
        return v1_open_id_auth_info

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
