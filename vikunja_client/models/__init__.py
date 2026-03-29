"""Contains all the data models used in inputs/outputs"""

from .auth_token import AuthToken
from .background_image import BackgroundImage
from .code_vikunja_io_api_pkg_modules_auth_openid_provider import (
    CodeVikunjaIoApiPkgModulesAuthOpenidProvider,
)
from .files_file import FilesFile
from .handler_auth_url import HandlerAuthURL
from .microsofttodo_migration import MicrosofttodoMigration
from .migration_status import MigrationStatus
from .models_api_permissions import ModelsAPIPermissions
from .models_api_token import ModelsAPIToken
from .models_api_token_route import ModelsAPITokenRoute
from .models_bucket import ModelsBucket
from .models_bulk_assignees import ModelsBulkAssignees
from .models_bulk_task import ModelsBulkTask
from .models_database_notifications import ModelsDatabaseNotifications
from .models_label import ModelsLabel
from .models_label_task import ModelsLabelTask
from .models_label_task_bulk import ModelsLabelTaskBulk
from .models_link_sharing import ModelsLinkSharing
from .models_message import ModelsMessage
from .models_permission import ModelsPermission
from .models_project import ModelsProject
from .models_project_duplicate import ModelsProjectDuplicate
from .models_project_user import ModelsProjectUser
from .models_project_view import ModelsProjectView
from .models_project_view_bucket_configuration import (
    ModelsProjectViewBucketConfiguration,
)
from .models_project_view_bucket_configuration_mode import (
    ModelsProjectViewBucketConfigurationMode,
)
from .models_project_view_view_kind import ModelsProjectViewViewKind
from .models_reaction import ModelsReaction
from .models_reaction_map import ModelsReactionMap
from .models_related_task_map import ModelsRelatedTaskMap
from .models_relation_kind import ModelsRelationKind
from .models_reminder_relation import ModelsReminderRelation
from .models_route_detail import ModelsRouteDetail
from .models_saved_filter import ModelsSavedFilter
from .models_sharing_type import ModelsSharingType
from .models_subscription import ModelsSubscription
from .models_task import ModelsTask
from .models_task_assginee import ModelsTaskAssginee
from .models_task_attachment import ModelsTaskAttachment
from .models_task_bucket import ModelsTaskBucket
from .models_task_collection import ModelsTaskCollection
from .models_task_comment import ModelsTaskComment
from .models_task_duplicate import ModelsTaskDuplicate
from .models_task_position import ModelsTaskPosition
from .models_task_relation import ModelsTaskRelation
from .models_task_reminder import ModelsTaskReminder
from .models_task_repeat_mode import ModelsTaskRepeatMode
from .models_task_unread_status import ModelsTaskUnreadStatus
from .models_team import ModelsTeam
from .models_team_member import ModelsTeamMember
from .models_team_project import ModelsTeamProject
from .models_team_user import ModelsTeamUser
from .models_team_with_permission import ModelsTeamWithPermission
from .models_user_with_permission import ModelsUserWithPermission
from .models_webhook import ModelsWebhook
from .notifications_database_notification import NotificationsDatabaseNotification
from .openid_callback import OpenidCallback
from .post_migration_ticktick_migrate_body import PostMigrationTicktickMigrateBody
from .post_migration_vikunja_file_migrate_body import (
    PostMigrationVikunjaFileMigrateBody,
)
from .put_projects_id_backgrounds_upload_body import PutProjectsIdBackgroundsUploadBody
from .put_tasks_id_attachments_body import PutTasksIdAttachmentsBody
from .put_user_settings_avatar_upload_body import PutUserSettingsAvatarUploadBody
from .todoist_migration import TodoistMigration
from .trello_migration import TrelloMigration
from .user_email_confirm import UserEmailConfirm
from .user_email_update import UserEmailUpdate
from .user_login import UserLogin
from .user_password_reset import UserPasswordReset
from .user_password_token_request import UserPasswordTokenRequest
from .user_token import UserToken
from .user_totp import UserTOTP
from .user_totp_passcode import UserTOTPPasscode
from .user_user import UserUser
from .v1_auth_info import V1AuthInfo
from .v1_ldap_auth_info import V1LdapAuthInfo
from .v1_legal_info import V1LegalInfo
from .v1_link_share_auth import V1LinkShareAuth
from .v1_local_auth_info import V1LocalAuthInfo
from .v1_open_id_auth_info import V1OpenIDAuthInfo
from .v1_user_avatar_provider import V1UserAvatarProvider
from .v1_user_deletion_request_confirm import V1UserDeletionRequestConfirm
from .v1_user_export_status import V1UserExportStatus
from .v1_user_password import V1UserPassword
from .v1_user_password_confirmation import V1UserPasswordConfirmation
from .v1_user_register import V1UserRegister
from .v1_user_settings import V1UserSettings
from .v1_user_settings_extra_settings_links import V1UserSettingsExtraSettingsLinks
from .v1_user_with_settings import V1UserWithSettings
from .v1_vikunja_infos import V1VikunjaInfos
from .web_http_error import WebHTTPError

__all__ = (
    "AuthToken",
    "BackgroundImage",
    "CodeVikunjaIoApiPkgModulesAuthOpenidProvider",
    "FilesFile",
    "HandlerAuthURL",
    "MicrosofttodoMigration",
    "MigrationStatus",
    "ModelsAPIPermissions",
    "ModelsAPIToken",
    "ModelsAPITokenRoute",
    "ModelsBucket",
    "ModelsBulkAssignees",
    "ModelsBulkTask",
    "ModelsDatabaseNotifications",
    "ModelsLabel",
    "ModelsLabelTask",
    "ModelsLabelTaskBulk",
    "ModelsLinkSharing",
    "ModelsMessage",
    "ModelsPermission",
    "ModelsProject",
    "ModelsProjectDuplicate",
    "ModelsProjectUser",
    "ModelsProjectView",
    "ModelsProjectViewBucketConfiguration",
    "ModelsProjectViewBucketConfigurationMode",
    "ModelsProjectViewViewKind",
    "ModelsReaction",
    "ModelsReactionMap",
    "ModelsRelatedTaskMap",
    "ModelsRelationKind",
    "ModelsReminderRelation",
    "ModelsRouteDetail",
    "ModelsSavedFilter",
    "ModelsSharingType",
    "ModelsSubscription",
    "ModelsTask",
    "ModelsTaskAssginee",
    "ModelsTaskAttachment",
    "ModelsTaskBucket",
    "ModelsTaskCollection",
    "ModelsTaskComment",
    "ModelsTaskDuplicate",
    "ModelsTaskPosition",
    "ModelsTaskRelation",
    "ModelsTaskReminder",
    "ModelsTaskRepeatMode",
    "ModelsTaskUnreadStatus",
    "ModelsTeam",
    "ModelsTeamMember",
    "ModelsTeamProject",
    "ModelsTeamUser",
    "ModelsTeamWithPermission",
    "ModelsUserWithPermission",
    "ModelsWebhook",
    "NotificationsDatabaseNotification",
    "OpenidCallback",
    "PostMigrationTicktickMigrateBody",
    "PostMigrationVikunjaFileMigrateBody",
    "PutProjectsIdBackgroundsUploadBody",
    "PutTasksIdAttachmentsBody",
    "PutUserSettingsAvatarUploadBody",
    "TodoistMigration",
    "TrelloMigration",
    "UserEmailConfirm",
    "UserEmailUpdate",
    "UserLogin",
    "UserPasswordReset",
    "UserPasswordTokenRequest",
    "UserToken",
    "UserTOTP",
    "UserTOTPPasscode",
    "UserUser",
    "V1AuthInfo",
    "V1LdapAuthInfo",
    "V1LegalInfo",
    "V1LinkShareAuth",
    "V1LocalAuthInfo",
    "V1OpenIDAuthInfo",
    "V1UserAvatarProvider",
    "V1UserDeletionRequestConfirm",
    "V1UserExportStatus",
    "V1UserPassword",
    "V1UserPasswordConfirmation",
    "V1UserRegister",
    "V1UserSettings",
    "V1UserSettingsExtraSettingsLinks",
    "V1UserWithSettings",
    "V1VikunjaInfos",
    "WebHTTPError",
)
