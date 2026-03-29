from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.models_task_repeat_mode import (
    ModelsTaskRepeatMode,
    check_models_task_repeat_mode,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.models_bucket import ModelsBucket
    from ..models.models_label import ModelsLabel
    from ..models.models_reaction_map import ModelsReactionMap
    from ..models.models_related_task_map import ModelsRelatedTaskMap
    from ..models.models_subscription import ModelsSubscription
    from ..models.models_task_attachment import ModelsTaskAttachment
    from ..models.models_task_comment import ModelsTaskComment
    from ..models.models_task_reminder import ModelsTaskReminder
    from ..models.user_user import UserUser


T = TypeVar("T", bound="ModelsTask")


@_attrs_define
class ModelsTask:
    """
    Attributes:
        assignees (list[UserUser] | Unset): An array of users who are assigned to this task
        attachments (list[ModelsTaskAttachment] | Unset): All attachments this task has. This property is read-onlym,
            you must use the separate endpoint to add attachments to a task.
        bucket_id (int | Unset): The bucket id. Will only be populated when the task is accessed via a view with
            buckets.
            Can be used to move a task between buckets. In that case, the new bucket must be in the same view as the old
            one.
        buckets (list[ModelsBucket] | Unset): All buckets across all views this task is part of. Only present when
            fetching tasks with the `expand` parameter set to `buckets`.
        comment_count (int | Unset): Comment count of this task. Only present when fetching tasks with the `expand`
            parameter set to `comment_count`.
        comments (list[ModelsTaskComment] | Unset): All comments of this task. Only present when fetching tasks with the
            `expand` parameter set to `comments`.
        cover_image_attachment_id (int | Unset): If this task has a cover image, the field will return the id of the
            attachment that is the cover image.
        created (str | Unset): A timestamp when this task was created. You cannot change this value.
        created_by (UserUser | Unset):
        description (str | Unset): The task description.
        done (bool | Unset): Whether a task is done or not.
        done_at (str | Unset): The time when a task was marked as done. This field is system-controlled and cannot be
            set via API.
        due_date (str | Unset): The time when the task is due.
        end_date (str | Unset): When this task ends.
        hex_color (str | Unset): The task color in hex
        id (int | Unset): The unique, numeric id of this task.
        identifier (str | Unset): The task identifier, based on the project identifier and the task's index
        index (int | Unset): The task index, calculated per project
        is_favorite (bool | Unset): True if a task is a favorite task. Favorite tasks show up in a separate "Important"
            project. This value depends on the user making the call to the api.
        is_unread (bool | Unset):
        labels (list[ModelsLabel] | Unset): An array of labels which are associated with this task. This property is
            read-only, you must use the separate endpoint to add labels to a task.
        percent_done (float | Unset): Determines how far a task is left from being done
        position (float | Unset): The position of the task - any task project can be sorted as usual by this parameter.
            When accessing tasks via views with buckets, this is primarily used to sort them based on a range.
            Positions are always saved per view. They will automatically be set if you request the tasks through a view
            endpoint, otherwise they will always be 0. To update them, take a look at the Task Position endpoint.
        priority (int | Unset): The task priority. Can be anything you want, it is possible to sort by this later.
        project_id (int | Unset): The project this task belongs to.
        reactions (ModelsReactionMap | Unset):
        related_tasks (ModelsRelatedTaskMap | Unset):
        reminders (list[ModelsTaskReminder] | Unset): An array of reminders that are associated with this task.
        repeat_after (int | Unset): An amount in seconds this task repeats itself. If this is set, when marking the task
            as done, it will mark itself as "undone" and then increase all remindes and the due date by its amount.
        repeat_mode (ModelsTaskRepeatMode | Unset):
        start_date (str | Unset): When this task starts.
        subscription (ModelsSubscription | Unset):
        title (str | Unset): The task text. This is what you'll see in the project.
        updated (str | Unset): A timestamp when this task was last updated. You cannot change this value.
    """

    assignees: list[UserUser] | Unset = UNSET
    attachments: list[ModelsTaskAttachment] | Unset = UNSET
    bucket_id: int | Unset = UNSET
    buckets: list[ModelsBucket] | Unset = UNSET
    comment_count: int | Unset = UNSET
    comments: list[ModelsTaskComment] | Unset = UNSET
    cover_image_attachment_id: int | Unset = UNSET
    created: str | Unset = UNSET
    created_by: UserUser | Unset = UNSET
    description: str | Unset = UNSET
    done: bool | Unset = UNSET
    done_at: str | Unset = UNSET
    due_date: str | Unset = UNSET
    end_date: str | Unset = UNSET
    hex_color: str | Unset = UNSET
    id: int | Unset = UNSET
    identifier: str | Unset = UNSET
    index: int | Unset = UNSET
    is_favorite: bool | Unset = UNSET
    is_unread: bool | Unset = UNSET
    labels: list[ModelsLabel] | Unset = UNSET
    percent_done: float | Unset = UNSET
    position: float | Unset = UNSET
    priority: int | Unset = UNSET
    project_id: int | Unset = UNSET
    reactions: ModelsReactionMap | Unset = UNSET
    related_tasks: ModelsRelatedTaskMap | Unset = UNSET
    reminders: list[ModelsTaskReminder] | Unset = UNSET
    repeat_after: int | Unset = UNSET
    repeat_mode: ModelsTaskRepeatMode | Unset = UNSET
    start_date: str | Unset = UNSET
    subscription: ModelsSubscription | Unset = UNSET
    title: str | Unset = UNSET
    updated: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        assignees: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.assignees, Unset):
            assignees = []
            for assignees_item_data in self.assignees:
                assignees_item = assignees_item_data.to_dict()
                assignees.append(assignees_item)

        attachments: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.attachments, Unset):
            attachments = []
            for attachments_item_data in self.attachments:
                attachments_item = attachments_item_data.to_dict()
                attachments.append(attachments_item)

        bucket_id = self.bucket_id

        buckets: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.buckets, Unset):
            buckets = []
            for buckets_item_data in self.buckets:
                buckets_item = buckets_item_data.to_dict()
                buckets.append(buckets_item)

        comment_count = self.comment_count

        comments: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.comments, Unset):
            comments = []
            for comments_item_data in self.comments:
                comments_item = comments_item_data.to_dict()
                comments.append(comments_item)

        cover_image_attachment_id = self.cover_image_attachment_id

        created = self.created

        created_by: dict[str, Any] | Unset = UNSET
        if not isinstance(self.created_by, Unset):
            created_by = self.created_by.to_dict()

        description = self.description

        done = self.done

        done_at = self.done_at

        due_date = self.due_date

        end_date = self.end_date

        hex_color = self.hex_color

        id = self.id

        identifier = self.identifier

        index = self.index

        is_favorite = self.is_favorite

        is_unread = self.is_unread

        labels: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.labels, Unset):
            labels = []
            for labels_item_data in self.labels:
                labels_item = labels_item_data.to_dict()
                labels.append(labels_item)

        percent_done = self.percent_done

        position = self.position

        priority = self.priority

        project_id = self.project_id

        reactions: dict[str, Any] | Unset = UNSET
        if not isinstance(self.reactions, Unset):
            reactions = self.reactions.to_dict()

        related_tasks: dict[str, Any] | Unset = UNSET
        if not isinstance(self.related_tasks, Unset):
            related_tasks = self.related_tasks.to_dict()

        reminders: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.reminders, Unset):
            reminders = []
            for reminders_item_data in self.reminders:
                reminders_item = reminders_item_data.to_dict()
                reminders.append(reminders_item)

        repeat_after = self.repeat_after

        repeat_mode: int | Unset = UNSET
        if not isinstance(self.repeat_mode, Unset):
            repeat_mode = self.repeat_mode

        start_date = self.start_date

        subscription: dict[str, Any] | Unset = UNSET
        if not isinstance(self.subscription, Unset):
            subscription = self.subscription.to_dict()

        title = self.title

        updated = self.updated

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if assignees is not UNSET:
            field_dict["assignees"] = assignees
        if attachments is not UNSET:
            field_dict["attachments"] = attachments
        if bucket_id is not UNSET:
            field_dict["bucket_id"] = bucket_id
        if buckets is not UNSET:
            field_dict["buckets"] = buckets
        if comment_count is not UNSET:
            field_dict["comment_count"] = comment_count
        if comments is not UNSET:
            field_dict["comments"] = comments
        if cover_image_attachment_id is not UNSET:
            field_dict["cover_image_attachment_id"] = cover_image_attachment_id
        if created is not UNSET:
            field_dict["created"] = created
        if created_by is not UNSET:
            field_dict["created_by"] = created_by
        if description is not UNSET:
            field_dict["description"] = description
        if done is not UNSET:
            field_dict["done"] = done
        if done_at is not UNSET:
            field_dict["done_at"] = done_at
        if due_date is not UNSET:
            field_dict["due_date"] = due_date
        if end_date is not UNSET:
            field_dict["end_date"] = end_date
        if hex_color is not UNSET:
            field_dict["hex_color"] = hex_color
        if id is not UNSET:
            field_dict["id"] = id
        if identifier is not UNSET:
            field_dict["identifier"] = identifier
        if index is not UNSET:
            field_dict["index"] = index
        if is_favorite is not UNSET:
            field_dict["is_favorite"] = is_favorite
        if is_unread is not UNSET:
            field_dict["is_unread"] = is_unread
        if labels is not UNSET:
            field_dict["labels"] = labels
        if percent_done is not UNSET:
            field_dict["percent_done"] = percent_done
        if position is not UNSET:
            field_dict["position"] = position
        if priority is not UNSET:
            field_dict["priority"] = priority
        if project_id is not UNSET:
            field_dict["project_id"] = project_id
        if reactions is not UNSET:
            field_dict["reactions"] = reactions
        if related_tasks is not UNSET:
            field_dict["related_tasks"] = related_tasks
        if reminders is not UNSET:
            field_dict["reminders"] = reminders
        if repeat_after is not UNSET:
            field_dict["repeat_after"] = repeat_after
        if repeat_mode is not UNSET:
            field_dict["repeat_mode"] = repeat_mode
        if start_date is not UNSET:
            field_dict["start_date"] = start_date
        if subscription is not UNSET:
            field_dict["subscription"] = subscription
        if title is not UNSET:
            field_dict["title"] = title
        if updated is not UNSET:
            field_dict["updated"] = updated

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.models_bucket import ModelsBucket
        from ..models.models_label import ModelsLabel
        from ..models.models_reaction_map import ModelsReactionMap
        from ..models.models_related_task_map import ModelsRelatedTaskMap
        from ..models.models_subscription import ModelsSubscription
        from ..models.models_task_attachment import ModelsTaskAttachment
        from ..models.models_task_comment import ModelsTaskComment
        from ..models.models_task_reminder import ModelsTaskReminder
        from ..models.user_user import UserUser

        d = dict(src_dict)
        _assignees = d.pop("assignees", UNSET)
        assignees: list[UserUser] | Unset = UNSET
        if _assignees is not UNSET and _assignees is not None:
            assignees = []
            for assignees_item_data in _assignees:
                assignees_item = UserUser.from_dict(assignees_item_data)

                assignees.append(assignees_item)

        _attachments = d.pop("attachments", UNSET)
        attachments: list[ModelsTaskAttachment] | Unset = UNSET
        if _attachments is not UNSET and _attachments is not None:
            attachments = []
            for attachments_item_data in _attachments:
                attachments_item = ModelsTaskAttachment.from_dict(attachments_item_data)

                attachments.append(attachments_item)

        bucket_id = d.pop("bucket_id", UNSET)

        _buckets = d.pop("buckets", UNSET)
        buckets: list[ModelsBucket] | Unset = UNSET
        if _buckets is not UNSET and _buckets is not None:
            buckets = []
            for buckets_item_data in _buckets:
                buckets_item = ModelsBucket.from_dict(buckets_item_data)

                buckets.append(buckets_item)

        comment_count = d.pop("comment_count", UNSET)

        _comments = d.pop("comments", UNSET)
        comments: list[ModelsTaskComment] | Unset = UNSET
        if _comments is not UNSET and _comments is not None:
            comments = []
            for comments_item_data in _comments:
                comments_item = ModelsTaskComment.from_dict(comments_item_data)

                comments.append(comments_item)

        cover_image_attachment_id = d.pop("cover_image_attachment_id", UNSET)

        created = d.pop("created", UNSET)

        _created_by = d.pop("created_by", UNSET)
        created_by: UserUser | Unset
        if isinstance(_created_by, Unset):
            created_by = UNSET
        else:
            created_by = UserUser.from_dict(_created_by) if _created_by is not None else None

        description = d.pop("description", UNSET)

        done = d.pop("done", UNSET)

        done_at = d.pop("done_at", UNSET)

        due_date = d.pop("due_date", UNSET)

        end_date = d.pop("end_date", UNSET)

        hex_color = d.pop("hex_color", UNSET)

        id = d.pop("id", UNSET)

        identifier = d.pop("identifier", UNSET)

        index = d.pop("index", UNSET)

        is_favorite = d.pop("is_favorite", UNSET)

        is_unread = d.pop("is_unread", UNSET)

        _labels = d.pop("labels", UNSET)
        labels: list[ModelsLabel] | Unset = UNSET
        if _labels is not UNSET and _labels is not None:
            labels = []
            for labels_item_data in _labels:
                labels_item = ModelsLabel.from_dict(labels_item_data)

                labels.append(labels_item)

        percent_done = d.pop("percent_done", UNSET)

        position = d.pop("position", UNSET)

        priority = d.pop("priority", UNSET)

        project_id = d.pop("project_id", UNSET)

        _reactions = d.pop("reactions", UNSET)
        reactions: ModelsReactionMap | Unset
        if isinstance(_reactions, Unset):
            reactions = UNSET
        else:
            reactions = ModelsReactionMap.from_dict(_reactions) if _reactions is not None else None

        _related_tasks = d.pop("related_tasks", UNSET)
        related_tasks: ModelsRelatedTaskMap | Unset
        if isinstance(_related_tasks, Unset):
            related_tasks = UNSET
        else:
            related_tasks = ModelsRelatedTaskMap.from_dict(_related_tasks) if _related_tasks is not None else None

        _reminders = d.pop("reminders", UNSET)
        reminders: list[ModelsTaskReminder] | Unset = UNSET
        if _reminders is not UNSET and _reminders is not None:
            reminders = []
            for reminders_item_data in _reminders:
                reminders_item = ModelsTaskReminder.from_dict(reminders_item_data)

                reminders.append(reminders_item)

        repeat_after = d.pop("repeat_after", UNSET)

        _repeat_mode = d.pop("repeat_mode", UNSET)
        repeat_mode: ModelsTaskRepeatMode | Unset
        if isinstance(_repeat_mode, Unset):
            repeat_mode = UNSET
        else:
            repeat_mode = check_models_task_repeat_mode(_repeat_mode)

        start_date = d.pop("start_date", UNSET)

        _subscription = d.pop("subscription", UNSET)
        subscription: ModelsSubscription | Unset
        if isinstance(_subscription, Unset):
            subscription = UNSET
        else:
            subscription = ModelsSubscription.from_dict(_subscription) if _subscription is not None else None

        title = d.pop("title", UNSET)

        updated = d.pop("updated", UNSET)

        models_task = cls(
            assignees=assignees,
            attachments=attachments,
            bucket_id=bucket_id,
            buckets=buckets,
            comment_count=comment_count,
            comments=comments,
            cover_image_attachment_id=cover_image_attachment_id,
            created=created,
            created_by=created_by,
            description=description,
            done=done,
            done_at=done_at,
            due_date=due_date,
            end_date=end_date,
            hex_color=hex_color,
            id=id,
            identifier=identifier,
            index=index,
            is_favorite=is_favorite,
            is_unread=is_unread,
            labels=labels,
            percent_done=percent_done,
            position=position,
            priority=priority,
            project_id=project_id,
            reactions=reactions,
            related_tasks=related_tasks,
            reminders=reminders,
            repeat_after=repeat_after,
            repeat_mode=repeat_mode,
            start_date=start_date,
            subscription=subscription,
            title=title,
            updated=updated,
        )

        models_task.additional_properties = d
        return models_task

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
