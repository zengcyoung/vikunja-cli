from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.models_message import ModelsMessage
from ...models.web_http_error import WebHTTPError
from ...types import Response


def _get_kwargs(
    task_id: int,
    user_id: int,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/tasks/{task_id}/assignees/{user_id}".format(
            task_id=quote(str(task_id), safe=""),
            user_id=quote(str(user_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ModelsMessage | WebHTTPError | None:
    if response.status_code == 200:
        response_200 = ModelsMessage.from_dict(response.json())

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
) -> Response[ModelsMessage | WebHTTPError]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    task_id: int,
    user_id: int,
    *,
    client: AuthenticatedClient,
) -> Response[ModelsMessage | WebHTTPError]:
    """Delete an assignee

     Un-assign a user from a task.

    Args:
        task_id (int):
        user_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ModelsMessage | WebHTTPError]
    """

    kwargs = _get_kwargs(
        task_id=task_id,
        user_id=user_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    task_id: int,
    user_id: int,
    *,
    client: AuthenticatedClient,
) -> ModelsMessage | WebHTTPError | None:
    """Delete an assignee

     Un-assign a user from a task.

    Args:
        task_id (int):
        user_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ModelsMessage | WebHTTPError
    """

    return sync_detailed(
        task_id=task_id,
        user_id=user_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    task_id: int,
    user_id: int,
    *,
    client: AuthenticatedClient,
) -> Response[ModelsMessage | WebHTTPError]:
    """Delete an assignee

     Un-assign a user from a task.

    Args:
        task_id (int):
        user_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ModelsMessage | WebHTTPError]
    """

    kwargs = _get_kwargs(
        task_id=task_id,
        user_id=user_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    task_id: int,
    user_id: int,
    *,
    client: AuthenticatedClient,
) -> ModelsMessage | WebHTTPError | None:
    """Delete an assignee

     Un-assign a user from a task.

    Args:
        task_id (int):
        user_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ModelsMessage | WebHTTPError
    """

    return (
        await asyncio_detailed(
            task_id=task_id,
            user_id=user_id,
            client=client,
        )
    ).parsed
