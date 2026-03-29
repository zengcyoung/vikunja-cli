from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.models_message import ModelsMessage
from ...models.models_project_duplicate import ModelsProjectDuplicate
from ...models.web_http_error import WebHTTPError
from ...types import Response


def _get_kwargs(
    project_id: int,
    *,
    body: ModelsProjectDuplicate,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/projects/{project_id}/duplicate".format(
            project_id=quote(str(project_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ModelsMessage | ModelsProjectDuplicate | WebHTTPError | None:
    if response.status_code == 201:
        response_201 = ModelsProjectDuplicate.from_dict(response.json())

        return response_201

    if response.status_code == 400:
        response_400 = WebHTTPError.from_dict(response.json())

        return response_400

    if response.status_code == 403:
        response_403 = WebHTTPError.from_dict(response.json())

        return response_403

    if response.status_code == 500:
        response_500 = ModelsMessage.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[ModelsMessage | ModelsProjectDuplicate | WebHTTPError]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    project_id: int,
    *,
    client: AuthenticatedClient,
    body: ModelsProjectDuplicate,
) -> Response[ModelsMessage | ModelsProjectDuplicate | WebHTTPError]:
    """Duplicate an existing project

     Copies the project, tasks, files, kanban data, assignees, comments, attachments, labels, relations,
    backgrounds, user/team permissions and link shares from one project to a new one. The user needs
    read access in the project and write access in the parent of the new project.

    Args:
        project_id (int):
        body (ModelsProjectDuplicate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ModelsMessage | ModelsProjectDuplicate | WebHTTPError]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    project_id: int,
    *,
    client: AuthenticatedClient,
    body: ModelsProjectDuplicate,
) -> ModelsMessage | ModelsProjectDuplicate | WebHTTPError | None:
    """Duplicate an existing project

     Copies the project, tasks, files, kanban data, assignees, comments, attachments, labels, relations,
    backgrounds, user/team permissions and link shares from one project to a new one. The user needs
    read access in the project and write access in the parent of the new project.

    Args:
        project_id (int):
        body (ModelsProjectDuplicate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ModelsMessage | ModelsProjectDuplicate | WebHTTPError
    """

    return sync_detailed(
        project_id=project_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    project_id: int,
    *,
    client: AuthenticatedClient,
    body: ModelsProjectDuplicate,
) -> Response[ModelsMessage | ModelsProjectDuplicate | WebHTTPError]:
    """Duplicate an existing project

     Copies the project, tasks, files, kanban data, assignees, comments, attachments, labels, relations,
    backgrounds, user/team permissions and link shares from one project to a new one. The user needs
    read access in the project and write access in the parent of the new project.

    Args:
        project_id (int):
        body (ModelsProjectDuplicate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ModelsMessage | ModelsProjectDuplicate | WebHTTPError]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    project_id: int,
    *,
    client: AuthenticatedClient,
    body: ModelsProjectDuplicate,
) -> ModelsMessage | ModelsProjectDuplicate | WebHTTPError | None:
    """Duplicate an existing project

     Copies the project, tasks, files, kanban data, assignees, comments, attachments, labels, relations,
    backgrounds, user/team permissions and link shares from one project to a new one. The user needs
    read access in the project and write access in the parent of the new project.

    Args:
        project_id (int):
        body (ModelsProjectDuplicate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ModelsMessage | ModelsProjectDuplicate | WebHTTPError
    """

    return (
        await asyncio_detailed(
            project_id=project_id,
            client=client,
            body=body,
        )
    ).parsed
