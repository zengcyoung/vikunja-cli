from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.models_message import ModelsMessage
from ...models.models_task_unread_status import ModelsTaskUnreadStatus
from ...models.web_http_error import WebHTTPError
from ...types import Response


def _get_kwargs(
    projecttask: int,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/tasks/{projecttask}/read".format(
            projecttask=quote(str(projecttask), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ModelsMessage | ModelsTaskUnreadStatus | WebHTTPError | None:
    if response.status_code == 200:
        response_200 = ModelsTaskUnreadStatus.from_dict(response.json())

        return response_200

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
) -> Response[ModelsMessage | ModelsTaskUnreadStatus | WebHTTPError]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    projecttask: int,
    *,
    client: AuthenticatedClient,
) -> Response[ModelsMessage | ModelsTaskUnreadStatus | WebHTTPError]:
    """Mark a task as read

     Marks a task as read for the current user by removing the unread status entry.

    Args:
        projecttask (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ModelsMessage | ModelsTaskUnreadStatus | WebHTTPError]
    """

    kwargs = _get_kwargs(
        projecttask=projecttask,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    projecttask: int,
    *,
    client: AuthenticatedClient,
) -> ModelsMessage | ModelsTaskUnreadStatus | WebHTTPError | None:
    """Mark a task as read

     Marks a task as read for the current user by removing the unread status entry.

    Args:
        projecttask (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ModelsMessage | ModelsTaskUnreadStatus | WebHTTPError
    """

    return sync_detailed(
        projecttask=projecttask,
        client=client,
    ).parsed


async def asyncio_detailed(
    projecttask: int,
    *,
    client: AuthenticatedClient,
) -> Response[ModelsMessage | ModelsTaskUnreadStatus | WebHTTPError]:
    """Mark a task as read

     Marks a task as read for the current user by removing the unread status entry.

    Args:
        projecttask (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ModelsMessage | ModelsTaskUnreadStatus | WebHTTPError]
    """

    kwargs = _get_kwargs(
        projecttask=projecttask,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    projecttask: int,
    *,
    client: AuthenticatedClient,
) -> ModelsMessage | ModelsTaskUnreadStatus | WebHTTPError | None:
    """Mark a task as read

     Marks a task as read for the current user by removing the unread status entry.

    Args:
        projecttask (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ModelsMessage | ModelsTaskUnreadStatus | WebHTTPError
    """

    return (
        await asyncio_detailed(
            projecttask=projecttask,
            client=client,
        )
    ).parsed
