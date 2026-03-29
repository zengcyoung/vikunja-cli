from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.models_message import ModelsMessage
from ...models.models_task_comment import ModelsTaskComment
from ...types import UNSET, Response, Unset


def _get_kwargs(
    task_id: int,
    *,
    order_by: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["order_by"] = order_by

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/tasks/{task_id}/comments".format(
            task_id=quote(str(task_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ModelsMessage | list[ModelsTaskComment] | None:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = ModelsTaskComment.from_dict(response_200_item_data)

            response_200.append(response_200_item)

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
) -> Response[ModelsMessage | list[ModelsTaskComment]]:
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
    order_by: str | Unset = UNSET,
) -> Response[ModelsMessage | list[ModelsTaskComment]]:
    """Get all task comments

     Get all task comments. The user doing this need to have at least read access to the task.

    Args:
        task_id (int):
        order_by (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ModelsMessage | list[ModelsTaskComment]]
    """

    kwargs = _get_kwargs(
        task_id=task_id,
        order_by=order_by,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    task_id: int,
    *,
    client: AuthenticatedClient,
    order_by: str | Unset = UNSET,
) -> ModelsMessage | list[ModelsTaskComment] | None:
    """Get all task comments

     Get all task comments. The user doing this need to have at least read access to the task.

    Args:
        task_id (int):
        order_by (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ModelsMessage | list[ModelsTaskComment]
    """

    return sync_detailed(
        task_id=task_id,
        client=client,
        order_by=order_by,
    ).parsed


async def asyncio_detailed(
    task_id: int,
    *,
    client: AuthenticatedClient,
    order_by: str | Unset = UNSET,
) -> Response[ModelsMessage | list[ModelsTaskComment]]:
    """Get all task comments

     Get all task comments. The user doing this need to have at least read access to the task.

    Args:
        task_id (int):
        order_by (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ModelsMessage | list[ModelsTaskComment]]
    """

    kwargs = _get_kwargs(
        task_id=task_id,
        order_by=order_by,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    task_id: int,
    *,
    client: AuthenticatedClient,
    order_by: str | Unset = UNSET,
) -> ModelsMessage | list[ModelsTaskComment] | None:
    """Get all task comments

     Get all task comments. The user doing this need to have at least read access to the task.

    Args:
        task_id (int):
        order_by (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ModelsMessage | list[ModelsTaskComment]
    """

    return (
        await asyncio_detailed(
            task_id=task_id,
            client=client,
            order_by=order_by,
        )
    ).parsed
