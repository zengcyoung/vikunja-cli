from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.models_message import ModelsMessage
from ...models.user_token import UserToken
from ...models.web_http_error import WebHTTPError
from ...types import Response


def _get_kwargs() -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/user/settings/token/caldav",
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ModelsMessage | UserToken | WebHTTPError | None:
    if response.status_code == 200:
        response_200 = UserToken.from_dict(response.json())

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
) -> Response[ModelsMessage | UserToken | WebHTTPError]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
) -> Response[ModelsMessage | UserToken | WebHTTPError]:
    """Generate a caldav token

     Generates a caldav token which can be used for the caldav api. It is not possible to see the token
    again after it was generated.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ModelsMessage | UserToken | WebHTTPError]
    """

    kwargs = _get_kwargs()

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
) -> ModelsMessage | UserToken | WebHTTPError | None:
    """Generate a caldav token

     Generates a caldav token which can be used for the caldav api. It is not possible to see the token
    again after it was generated.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ModelsMessage | UserToken | WebHTTPError
    """

    return sync_detailed(
        client=client,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
) -> Response[ModelsMessage | UserToken | WebHTTPError]:
    """Generate a caldav token

     Generates a caldav token which can be used for the caldav api. It is not possible to see the token
    again after it was generated.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ModelsMessage | UserToken | WebHTTPError]
    """

    kwargs = _get_kwargs()

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
) -> ModelsMessage | UserToken | WebHTTPError | None:
    """Generate a caldav token

     Generates a caldav token which can be used for the caldav api. It is not possible to see the token
    again after it was generated.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ModelsMessage | UserToken | WebHTTPError
    """

    return (
        await asyncio_detailed(
            client=client,
        )
    ).parsed
