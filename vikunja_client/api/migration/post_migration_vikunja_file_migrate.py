from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.models_message import ModelsMessage
from ...models.post_migration_vikunja_file_migrate_body import (
    PostMigrationVikunjaFileMigrateBody,
)
from ...types import Response


def _get_kwargs(
    *,
    body: PostMigrationVikunjaFileMigrateBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/migration/vikunja-file/migrate",
    }

    _kwargs["data"] = body.to_dict()

    headers["Content-Type"] = "application/x-www-form-urlencoded"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ModelsMessage | None:
    if response.status_code == 200:
        response_200 = ModelsMessage.from_dict(response.json())

        return response_200

    if response.status_code == 500:
        response_500 = ModelsMessage.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[ModelsMessage]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: PostMigrationVikunjaFileMigrateBody,
) -> Response[ModelsMessage]:
    """Import all projects, tasks etc. from a Vikunja data export

     Imports all projects, tasks, notes, reminders, subtasks and files from a Vikunjda data export into
    Vikunja.

    Args:
        body (PostMigrationVikunjaFileMigrateBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ModelsMessage]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    body: PostMigrationVikunjaFileMigrateBody,
) -> ModelsMessage | None:
    """Import all projects, tasks etc. from a Vikunja data export

     Imports all projects, tasks, notes, reminders, subtasks and files from a Vikunjda data export into
    Vikunja.

    Args:
        body (PostMigrationVikunjaFileMigrateBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ModelsMessage
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: PostMigrationVikunjaFileMigrateBody,
) -> Response[ModelsMessage]:
    """Import all projects, tasks etc. from a Vikunja data export

     Imports all projects, tasks, notes, reminders, subtasks and files from a Vikunjda data export into
    Vikunja.

    Args:
        body (PostMigrationVikunjaFileMigrateBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ModelsMessage]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: PostMigrationVikunjaFileMigrateBody,
) -> ModelsMessage | None:
    """Import all projects, tasks etc. from a Vikunja data export

     Imports all projects, tasks, notes, reminders, subtasks and files from a Vikunjda data export into
    Vikunja.

    Args:
        body (PostMigrationVikunjaFileMigrateBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ModelsMessage
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
