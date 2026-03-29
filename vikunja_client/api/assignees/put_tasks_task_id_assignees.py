from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.models_message import ModelsMessage
from ...models.models_task_assginee import ModelsTaskAssginee
from ...models.web_http_error import WebHTTPError
from ...types import Response


def _get_kwargs(
    task_id: int,
    *,
    body: ModelsTaskAssginee,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/tasks/{task_id}/assignees".format(
            task_id=quote(str(task_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ModelsMessage | ModelsTaskAssginee | WebHTTPError | None:
    if response.status_code == 201:
        response_201 = ModelsTaskAssginee.from_dict(response.json())

        return response_201

    if response.status_code == 400:
        response_400 = WebHTTPError.from_dict(response.json())

        return response_400

    if response.status_code == 500:
        response_500 = ModelsMessage.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[ModelsMessage | ModelsTaskAssginee | WebHTTPError]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    task_id: int,
    *,
    client: AuthenticatedClient,
    body: ModelsTaskAssginee,
) -> Response[ModelsMessage | ModelsTaskAssginee | WebHTTPError]:
    """Add a new assignee to a task

     Adds a new assignee to a task. The assignee needs to have access to the project, the doer must be
    able to edit this task.

    Args:
        task_id (int):
        body (ModelsTaskAssginee):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ModelsMessage | ModelsTaskAssginee | WebHTTPError]
    """

    kwargs = _get_kwargs(
        task_id=task_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    task_id: int,
    *,
    client: AuthenticatedClient,
    body: ModelsTaskAssginee,
) -> ModelsMessage | ModelsTaskAssginee | WebHTTPError | None:
    """Add a new assignee to a task

     Adds a new assignee to a task. The assignee needs to have access to the project, the doer must be
    able to edit this task.

    Args:
        task_id (int):
        body (ModelsTaskAssginee):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ModelsMessage | ModelsTaskAssginee | WebHTTPError
    """

    return sync_detailed(
        task_id=task_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    task_id: int,
    *,
    client: AuthenticatedClient,
    body: ModelsTaskAssginee,
) -> Response[ModelsMessage | ModelsTaskAssginee | WebHTTPError]:
    """Add a new assignee to a task

     Adds a new assignee to a task. The assignee needs to have access to the project, the doer must be
    able to edit this task.

    Args:
        task_id (int):
        body (ModelsTaskAssginee):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ModelsMessage | ModelsTaskAssginee | WebHTTPError]
    """

    kwargs = _get_kwargs(
        task_id=task_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    task_id: int,
    *,
    client: AuthenticatedClient,
    body: ModelsTaskAssginee,
) -> ModelsMessage | ModelsTaskAssginee | WebHTTPError | None:
    """Add a new assignee to a task

     Adds a new assignee to a task. The assignee needs to have access to the project, the doer must be
    able to edit this task.

    Args:
        task_id (int):
        body (ModelsTaskAssginee):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ModelsMessage | ModelsTaskAssginee | WebHTTPError
    """

    return (
        await asyncio_detailed(
            task_id=task_id,
            client=client,
            body=body,
        )
    ).parsed
