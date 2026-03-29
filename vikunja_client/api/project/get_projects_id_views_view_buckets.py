from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.models_bucket import ModelsBucket
from ...models.models_message import ModelsMessage
from ...types import Response


def _get_kwargs(
    id: int,
    view: int,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/projects/{id}/views/{view}/buckets".format(
            id=quote(str(id), safe=""),
            view=quote(str(view), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ModelsMessage | list[ModelsBucket] | None:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = ModelsBucket.from_dict(response_200_item_data)

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
) -> Response[ModelsMessage | list[ModelsBucket]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    id: int,
    view: int,
    *,
    client: AuthenticatedClient,
) -> Response[ModelsMessage | list[ModelsBucket]]:
    """Get all kanban buckets of a project

     Returns all kanban buckets which belong to that project. Buckets are always sorted by their
    `position` in ascending order. To get all buckets with their tasks, use the tasks endpoint with a
    kanban view.

    Args:
        id (int):
        view (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ModelsMessage | list[ModelsBucket]]
    """

    kwargs = _get_kwargs(
        id=id,
        view=view,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    id: int,
    view: int,
    *,
    client: AuthenticatedClient,
) -> ModelsMessage | list[ModelsBucket] | None:
    """Get all kanban buckets of a project

     Returns all kanban buckets which belong to that project. Buckets are always sorted by their
    `position` in ascending order. To get all buckets with their tasks, use the tasks endpoint with a
    kanban view.

    Args:
        id (int):
        view (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ModelsMessage | list[ModelsBucket]
    """

    return sync_detailed(
        id=id,
        view=view,
        client=client,
    ).parsed


async def asyncio_detailed(
    id: int,
    view: int,
    *,
    client: AuthenticatedClient,
) -> Response[ModelsMessage | list[ModelsBucket]]:
    """Get all kanban buckets of a project

     Returns all kanban buckets which belong to that project. Buckets are always sorted by their
    `position` in ascending order. To get all buckets with their tasks, use the tasks endpoint with a
    kanban view.

    Args:
        id (int):
        view (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ModelsMessage | list[ModelsBucket]]
    """

    kwargs = _get_kwargs(
        id=id,
        view=view,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: int,
    view: int,
    *,
    client: AuthenticatedClient,
) -> ModelsMessage | list[ModelsBucket] | None:
    """Get all kanban buckets of a project

     Returns all kanban buckets which belong to that project. Buckets are always sorted by their
    `position` in ascending order. To get all buckets with their tasks, use the tasks endpoint with a
    kanban view.

    Args:
        id (int):
        view (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ModelsMessage | list[ModelsBucket]
    """

    return (
        await asyncio_detailed(
            id=id,
            view=view,
            client=client,
        )
    ).parsed
