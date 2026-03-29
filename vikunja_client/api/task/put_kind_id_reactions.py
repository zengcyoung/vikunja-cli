from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.models_message import ModelsMessage
from ...models.models_reaction import ModelsReaction
from ...models.web_http_error import WebHTTPError
from ...types import Response


def _get_kwargs(
    kind: int,
    id: int,
    *,
    body: ModelsReaction,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/{kind}/{id}/reactions".format(
            kind=quote(str(kind), safe=""),
            id=quote(str(id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ModelsMessage | ModelsReaction | WebHTTPError | None:
    if response.status_code == 200:
        response_200 = ModelsReaction.from_dict(response.json())

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
) -> Response[ModelsMessage | ModelsReaction | WebHTTPError]:
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
    body: ModelsReaction,
) -> Response[ModelsMessage | ModelsReaction | WebHTTPError]:
    """Add a reaction to an entity

     Add a reaction to an entity. Will do nothing if the reaction already exists.

    Args:
        kind (int):
        id (int):
        body (ModelsReaction):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ModelsMessage | ModelsReaction | WebHTTPError]
    """

    kwargs = _get_kwargs(
        kind=kind,
        id=id,
        body=body,
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
    body: ModelsReaction,
) -> ModelsMessage | ModelsReaction | WebHTTPError | None:
    """Add a reaction to an entity

     Add a reaction to an entity. Will do nothing if the reaction already exists.

    Args:
        kind (int):
        id (int):
        body (ModelsReaction):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ModelsMessage | ModelsReaction | WebHTTPError
    """

    return sync_detailed(
        kind=kind,
        id=id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    kind: int,
    id: int,
    *,
    client: AuthenticatedClient,
    body: ModelsReaction,
) -> Response[ModelsMessage | ModelsReaction | WebHTTPError]:
    """Add a reaction to an entity

     Add a reaction to an entity. Will do nothing if the reaction already exists.

    Args:
        kind (int):
        id (int):
        body (ModelsReaction):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ModelsMessage | ModelsReaction | WebHTTPError]
    """

    kwargs = _get_kwargs(
        kind=kind,
        id=id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    kind: int,
    id: int,
    *,
    client: AuthenticatedClient,
    body: ModelsReaction,
) -> ModelsMessage | ModelsReaction | WebHTTPError | None:
    """Add a reaction to an entity

     Add a reaction to an entity. Will do nothing if the reaction already exists.

    Args:
        kind (int):
        id (int):
        body (ModelsReaction):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ModelsMessage | ModelsReaction | WebHTTPError
    """

    return (
        await asyncio_detailed(
            kind=kind,
            id=id,
            client=client,
            body=body,
        )
    ).parsed
