from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.models_message import ModelsMessage
from ...models.models_reaction_map import ModelsReactionMap
from ...models.web_http_error import WebHTTPError
from ...types import Response


def _get_kwargs(
    kind: int,
    id: int,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/{kind}/{id}/reactions".format(
            kind=quote(str(kind), safe=""),
            id=quote(str(id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ModelsMessage | WebHTTPError | list[ModelsReactionMap] | None:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = ModelsReactionMap.from_dict(response_200_item_data)

            response_200.append(response_200_item)

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
) -> Response[ModelsMessage | WebHTTPError | list[ModelsReactionMap]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    kind: int,
    id: int,
    *,
    client: AuthenticatedClient,
) -> Response[ModelsMessage | WebHTTPError | list[ModelsReactionMap]]:
    """Get all reactions for an entity

     Returns all reactions for an entity

    Args:
        kind (int):
        id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ModelsMessage | WebHTTPError | list[ModelsReactionMap]]
    """

    kwargs = _get_kwargs(
        kind=kind,
        id=id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    kind: int,
    id: int,
    *,
    client: AuthenticatedClient,
) -> ModelsMessage | WebHTTPError | list[ModelsReactionMap] | None:
    """Get all reactions for an entity

     Returns all reactions for an entity

    Args:
        kind (int):
        id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ModelsMessage | WebHTTPError | list[ModelsReactionMap]
    """

    return sync_detailed(
        kind=kind,
        id=id,
        client=client,
    ).parsed


async def asyncio_detailed(
    kind: int,
    id: int,
    *,
    client: AuthenticatedClient,
) -> Response[ModelsMessage | WebHTTPError | list[ModelsReactionMap]]:
    """Get all reactions for an entity

     Returns all reactions for an entity

    Args:
        kind (int):
        id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ModelsMessage | WebHTTPError | list[ModelsReactionMap]]
    """

    kwargs = _get_kwargs(
        kind=kind,
        id=id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    kind: int,
    id: int,
    *,
    client: AuthenticatedClient,
) -> ModelsMessage | WebHTTPError | list[ModelsReactionMap] | None:
    """Get all reactions for an entity

     Returns all reactions for an entity

    Args:
        kind (int):
        id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ModelsMessage | WebHTTPError | list[ModelsReactionMap]
    """

    return (
        await asyncio_detailed(
            kind=kind,
            id=id,
            client=client,
        )
    ).parsed
