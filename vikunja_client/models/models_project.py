from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.models_permission import ModelsPermission, check_models_permission
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.models_project_view import ModelsProjectView
    from ..models.models_subscription import ModelsSubscription
    from ..models.user_user import UserUser


T = TypeVar("T", bound="ModelsProject")


@_attrs_define
class ModelsProject:
    """
    Attributes:
        background_blur_hash (str | Unset): Contains a very small version of the project background to use as a blurry
            preview until the actual background is loaded. Check out https://blurha.sh/ to learn how it works.
        background_information (Any | Unset): Holds extra information about the background set since some background
            providers require attribution or similar. If not null, the background can be accessed at
            /projects/{projectID}/background
        created (str | Unset): A timestamp when this project was created. You cannot change this value.
        description (str | Unset): The description of the project.
        hex_color (str | Unset): The hex color of this project
        id (int | Unset): The unique, numeric id of this project.
        identifier (str | Unset): The unique project short identifier. Used to build task identifiers.
        is_archived (bool | Unset): Whether a project is archived.
        is_favorite (bool | Unset): True if a project is a favorite. Favorite projects show up in a separate parent
            project. This value depends on the user making the call to the api.
        max_permission (ModelsPermission | Unset):
        owner (UserUser | Unset):
        parent_project_id (int | Unset):
        position (float | Unset): The position this project has when querying all projects. See the tasks.position
            property on how to use this.
        subscription (ModelsSubscription | Unset):
        title (str | Unset): The title of the project. You'll see this in the overview.
        updated (str | Unset): A timestamp when this project was last updated. You cannot change this value.
        views (list[ModelsProjectView] | Unset):
    """

    background_blur_hash: str | Unset = UNSET
    background_information: Any | Unset = UNSET
    created: str | Unset = UNSET
    description: str | Unset = UNSET
    hex_color: str | Unset = UNSET
    id: int | Unset = UNSET
    identifier: str | Unset = UNSET
    is_archived: bool | Unset = UNSET
    is_favorite: bool | Unset = UNSET
    max_permission: ModelsPermission | Unset = UNSET
    owner: UserUser | Unset = UNSET
    parent_project_id: int | Unset = UNSET
    position: float | Unset = UNSET
    subscription: ModelsSubscription | Unset = UNSET
    title: str | Unset = UNSET
    updated: str | Unset = UNSET
    views: list[ModelsProjectView] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        background_blur_hash = self.background_blur_hash

        background_information = self.background_information

        created = self.created

        description = self.description

        hex_color = self.hex_color

        id = self.id

        identifier = self.identifier

        is_archived = self.is_archived

        is_favorite = self.is_favorite

        max_permission: int | Unset = UNSET
        if not isinstance(self.max_permission, Unset):
            max_permission = self.max_permission

        owner: dict[str, Any] | Unset = UNSET
        if not isinstance(self.owner, Unset):
            owner = self.owner.to_dict()

        parent_project_id = self.parent_project_id

        position = self.position

        subscription: dict[str, Any] | Unset = UNSET
        if not isinstance(self.subscription, Unset):
            subscription = self.subscription.to_dict()

        title = self.title

        updated = self.updated

        views: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.views, Unset):
            views = []
            for views_item_data in self.views:
                views_item = views_item_data.to_dict()
                views.append(views_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if background_blur_hash is not UNSET:
            field_dict["background_blur_hash"] = background_blur_hash
        if background_information is not UNSET:
            field_dict["background_information"] = background_information
        if created is not UNSET:
            field_dict["created"] = created
        if description is not UNSET:
            field_dict["description"] = description
        if hex_color is not UNSET:
            field_dict["hex_color"] = hex_color
        if id is not UNSET:
            field_dict["id"] = id
        if identifier is not UNSET:
            field_dict["identifier"] = identifier
        if is_archived is not UNSET:
            field_dict["is_archived"] = is_archived
        if is_favorite is not UNSET:
            field_dict["is_favorite"] = is_favorite
        if max_permission is not UNSET:
            field_dict["max_permission"] = max_permission
        if owner is not UNSET:
            field_dict["owner"] = owner
        if parent_project_id is not UNSET:
            field_dict["parent_project_id"] = parent_project_id
        if position is not UNSET:
            field_dict["position"] = position
        if subscription is not UNSET:
            field_dict["subscription"] = subscription
        if title is not UNSET:
            field_dict["title"] = title
        if updated is not UNSET:
            field_dict["updated"] = updated
        if views is not UNSET:
            field_dict["views"] = views

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.models_project_view import ModelsProjectView
        from ..models.models_subscription import ModelsSubscription
        from ..models.user_user import UserUser

        d = dict(src_dict)
        background_blur_hash = d.pop("background_blur_hash", UNSET)

        background_information = d.pop("background_information", UNSET)

        created = d.pop("created", UNSET)

        description = d.pop("description", UNSET)

        hex_color = d.pop("hex_color", UNSET)

        id = d.pop("id", UNSET)

        identifier = d.pop("identifier", UNSET)

        is_archived = d.pop("is_archived", UNSET)

        is_favorite = d.pop("is_favorite", UNSET)

        _max_permission = d.pop("max_permission", UNSET)
        max_permission: ModelsPermission | Unset
        if isinstance(_max_permission, Unset):
            max_permission = UNSET
        else:
            max_permission = check_models_permission(_max_permission)

        _owner = d.pop("owner", UNSET)
        owner: UserUser | Unset
        if isinstance(_owner, Unset):
            owner = UNSET
        else:
            owner = UserUser.from_dict(_owner) if _owner is not None else None

        parent_project_id = d.pop("parent_project_id", UNSET)

        position = d.pop("position", UNSET)

        _subscription = d.pop("subscription", UNSET)
        subscription: ModelsSubscription | Unset
        if isinstance(_subscription, Unset):
            subscription = UNSET
        else:
            subscription = ModelsSubscription.from_dict(_subscription) if _subscription is not None else None

        title = d.pop("title", UNSET)

        updated = d.pop("updated", UNSET)

        _views = d.pop("views", UNSET)
        views: list[ModelsProjectView] | Unset = UNSET
        if _views is not UNSET:
            views = []
            for views_item_data in _views:
                views_item = ModelsProjectView.from_dict(views_item_data)

                views.append(views_item)

        models_project = cls(
            background_blur_hash=background_blur_hash,
            background_information=background_information,
            created=created,
            description=description,
            hex_color=hex_color,
            id=id,
            identifier=identifier,
            is_archived=is_archived,
            is_favorite=is_favorite,
            max_permission=max_permission,
            owner=owner,
            parent_project_id=parent_project_id,
            position=position,
            subscription=subscription,
            title=title,
            updated=updated,
            views=views,
        )

        models_project.additional_properties = d
        return models_project

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
