from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.handler_auth_url import HandlerAuthURL
from ...models.models_message import ModelsMessage
from ...types import Response


def _get_kwargs() -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/migration/trello/auth",
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> HandlerAuthURL | ModelsMessage | None:
    if response.status_code == 200:
        response_200 = HandlerAuthURL.from_dict(response.json())

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
) -> Response[HandlerAuthURL | ModelsMessage]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
) -> Response[HandlerAuthURL | ModelsMessage]:
    """Get the auth url from trello

     Returns the auth url where the user needs to get its auth code. This code can then be used to
    migrate everything from trello to Vikunja.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HandlerAuthURL | ModelsMessage]
    """

    kwargs = _get_kwargs()

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
) -> HandlerAuthURL | ModelsMessage | None:
    """Get the auth url from trello

     Returns the auth url where the user needs to get its auth code. This code can then be used to
    migrate everything from trello to Vikunja.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HandlerAuthURL | ModelsMessage
    """

    return sync_detailed(
        client=client,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
) -> Response[HandlerAuthURL | ModelsMessage]:
    """Get the auth url from trello

     Returns the auth url where the user needs to get its auth code. This code can then be used to
    migrate everything from trello to Vikunja.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HandlerAuthURL | ModelsMessage]
    """

    kwargs = _get_kwargs()

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
) -> HandlerAuthURL | ModelsMessage | None:
    """Get the auth url from trello

     Returns the auth url where the user needs to get its auth code. This code can then be used to
    migrate everything from trello to Vikunja.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HandlerAuthURL | ModelsMessage
    """

    return (
        await asyncio_detailed(
            client=client,
        )
    ).parsed
