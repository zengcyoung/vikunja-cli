from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.models_message import ModelsMessage
from ...models.models_task_comment import ModelsTaskComment
from ...models.web_http_error import WebHTTPError
from ...types import Response


def _get_kwargs(
    task_id: int,
    comment_id: int,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/tasks/{task_id}/comments/{comment_id}".format(
            task_id=quote(str(task_id), safe=""),
            comment_id=quote(str(comment_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ModelsMessage | ModelsTaskComment | WebHTTPError | None:
    if response.status_code == 200:
        response_200 = ModelsTaskComment.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = WebHTTPError.from_dict(response.json())

        return response_400

    if response.status_code == 404:
        response_404 = WebHTTPError.from_dict(response.json())

        return response_404

    if response.status_code == 500:
        response_500 = ModelsMessage.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[ModelsMessage | ModelsTaskComment | WebHTTPError]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    task_id: int,
    comment_id: int,
    *,
    client: AuthenticatedClient,
) -> Response[ModelsMessage | ModelsTaskComment | WebHTTPError]:
    """Update an existing task comment

     Update an existing task comment. The user doing this need to have at least write access to the task
    this comment belongs to.

    Args:
        task_id (int):
        comment_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ModelsMessage | ModelsTaskComment | WebHTTPError]
    """

    kwargs = _get_kwargs(
        task_id=task_id,
        comment_id=comment_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    task_id: int,
    comment_id: int,
    *,
    client: AuthenticatedClient,
) -> ModelsMessage | ModelsTaskComment | WebHTTPError | None:
    """Update an existing task comment

     Update an existing task comment. The user doing this need to have at least write access to the task
    this comment belongs to.

    Args:
        task_id (int):
        comment_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ModelsMessage | ModelsTaskComment | WebHTTPError
    """

    return sync_detailed(
        task_id=task_id,
        comment_id=comment_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    task_id: int,
    comment_id: int,
    *,
    client: AuthenticatedClient,
) -> Response[ModelsMessage | ModelsTaskComment | WebHTTPError]:
    """Update an existing task comment

     Update an existing task comment. The user doing this need to have at least write access to the task
    this comment belongs to.

    Args:
        task_id (int):
        comment_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ModelsMessage | ModelsTaskComment | WebHTTPError]
    """

    kwargs = _get_kwargs(
        task_id=task_id,
        comment_id=comment_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    task_id: int,
    comment_id: int,
    *,
    client: AuthenticatedClient,
) -> ModelsMessage | ModelsTaskComment | WebHTTPError | None:
    """Update an existing task comment

     Update an existing task comment. The user doing this need to have at least write access to the task
    this comment belongs to.

    Args:
        task_id (int):
        comment_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ModelsMessage | ModelsTaskComment | WebHTTPError
    """

    return (
        await asyncio_detailed(
            task_id=task_id,
            comment_id=comment_id,
            client=client,
        )
    ).parsed
