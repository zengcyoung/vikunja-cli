from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.models_message import ModelsMessage
from ...models.user_user import UserUser
from ...models.web_http_error import WebHTTPError
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    s: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["s"] = s

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/users",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ModelsMessage | WebHTTPError | list[UserUser] | None:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = UserUser.from_dict(response_200_item_data)

            response_200.append(response_200_item)

        return response_200

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
) -> Response[ModelsMessage | WebHTTPError | list[UserUser]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    s: str | Unset = UNSET,
) -> Response[ModelsMessage | WebHTTPError | list[UserUser]]:
    """Get users

     Search for a user by its username, name or full email. Name (not username) or email require that the
    user has enabled this in their settings, unless both users share an external team (synced via
    OIDC/LDAP), in which case they can always find each other.

    Args:
        s (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ModelsMessage | WebHTTPError | list[UserUser]]
    """

    kwargs = _get_kwargs(
        s=s,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    s: str | Unset = UNSET,
) -> ModelsMessage | WebHTTPError | list[UserUser] | None:
    """Get users

     Search for a user by its username, name or full email. Name (not username) or email require that the
    user has enabled this in their settings, unless both users share an external team (synced via
    OIDC/LDAP), in which case they can always find each other.

    Args:
        s (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ModelsMessage | WebHTTPError | list[UserUser]
    """

    return sync_detailed(
        client=client,
        s=s,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    s: str | Unset = UNSET,
) -> Response[ModelsMessage | WebHTTPError | list[UserUser]]:
    """Get users

     Search for a user by its username, name or full email. Name (not username) or email require that the
    user has enabled this in their settings, unless both users share an external team (synced via
    OIDC/LDAP), in which case they can always find each other.

    Args:
        s (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ModelsMessage | WebHTTPError | list[UserUser]]
    """

    kwargs = _get_kwargs(
        s=s,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    s: str | Unset = UNSET,
) -> ModelsMessage | WebHTTPError | list[UserUser] | None:
    """Get users

     Search for a user by its username, name or full email. Name (not username) or email require that the
    user has enabled this in their settings, unless both users share an external team (synced via
    OIDC/LDAP), in which case they can always find each other.

    Args:
        s (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ModelsMessage | WebHTTPError | list[UserUser]
    """

    return (
        await asyncio_detailed(
            client=client,
            s=s,
        )
    ).parsed
