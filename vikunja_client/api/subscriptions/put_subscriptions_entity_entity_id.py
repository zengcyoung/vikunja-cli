from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.models_message import ModelsMessage
from ...models.models_subscription import ModelsSubscription
from ...models.web_http_error import WebHTTPError
from ...types import Response


def _get_kwargs(
    entity: str,
    entity_id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/subscriptions/{entity}/{entity_id}".format(
            entity=quote(str(entity), safe=""),
            entity_id=quote(str(entity_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ModelsMessage | ModelsSubscription | WebHTTPError | None:
    if response.status_code == 201:
        response_201 = ModelsSubscription.from_dict(response.json())

        return response_201

    if response.status_code == 403:
        response_403 = WebHTTPError.from_dict(response.json())

        return response_403

    if response.status_code == 412:
        response_412 = WebHTTPError.from_dict(response.json())

        return response_412

    if response.status_code == 500:
        response_500 = ModelsMessage.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[ModelsMessage | ModelsSubscription | WebHTTPError]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    entity: str,
    entity_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[ModelsMessage | ModelsSubscription | WebHTTPError]:
    """Subscribes the current user to an entity.

     Subscribes the current user to an entity.

    Args:
        entity (str):
        entity_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ModelsMessage | ModelsSubscription | WebHTTPError]
    """

    kwargs = _get_kwargs(
        entity=entity,
        entity_id=entity_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    entity: str,
    entity_id: str,
    *,
    client: AuthenticatedClient,
) -> ModelsMessage | ModelsSubscription | WebHTTPError | None:
    """Subscribes the current user to an entity.

     Subscribes the current user to an entity.

    Args:
        entity (str):
        entity_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ModelsMessage | ModelsSubscription | WebHTTPError
    """

    return sync_detailed(
        entity=entity,
        entity_id=entity_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    entity: str,
    entity_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[ModelsMessage | ModelsSubscription | WebHTTPError]:
    """Subscribes the current user to an entity.

     Subscribes the current user to an entity.

    Args:
        entity (str):
        entity_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ModelsMessage | ModelsSubscription | WebHTTPError]
    """

    kwargs = _get_kwargs(
        entity=entity,
        entity_id=entity_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    entity: str,
    entity_id: str,
    *,
    client: AuthenticatedClient,
) -> ModelsMessage | ModelsSubscription | WebHTTPError | None:
    """Subscribes the current user to an entity.

     Subscribes the current user to an entity.

    Args:
        entity (str):
        entity_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ModelsMessage | ModelsSubscription | WebHTTPError
    """

    return (
        await asyncio_detailed(
            entity=entity,
            entity_id=entity_id,
            client=client,
        )
    ).parsed
