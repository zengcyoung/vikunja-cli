from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.auth_token import AuthToken
from ...models.models_message import ModelsMessage
from ...models.v1_link_share_auth import V1LinkShareAuth
from ...models.web_http_error import WebHTTPError
from ...types import Response


def _get_kwargs(
    share: str,
    *,
    body: V1LinkShareAuth,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/shares/{share}/auth".format(
            share=quote(str(share), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> AuthToken | ModelsMessage | WebHTTPError | None:
    if response.status_code == 200:
        response_200 = AuthToken.from_dict(response.json())

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
) -> Response[AuthToken | ModelsMessage | WebHTTPError]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    share: str,
    *,
    client: AuthenticatedClient | Client,
    body: V1LinkShareAuth,
) -> Response[AuthToken | ModelsMessage | WebHTTPError]:
    """Get an auth token for a share

     Get a jwt auth token for a shared project from a share hash.

    Args:
        share (str):
        body (V1LinkShareAuth):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AuthToken | ModelsMessage | WebHTTPError]
    """

    kwargs = _get_kwargs(
        share=share,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    share: str,
    *,
    client: AuthenticatedClient | Client,
    body: V1LinkShareAuth,
) -> AuthToken | ModelsMessage | WebHTTPError | None:
    """Get an auth token for a share

     Get a jwt auth token for a shared project from a share hash.

    Args:
        share (str):
        body (V1LinkShareAuth):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AuthToken | ModelsMessage | WebHTTPError
    """

    return sync_detailed(
        share=share,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    share: str,
    *,
    client: AuthenticatedClient | Client,
    body: V1LinkShareAuth,
) -> Response[AuthToken | ModelsMessage | WebHTTPError]:
    """Get an auth token for a share

     Get a jwt auth token for a shared project from a share hash.

    Args:
        share (str):
        body (V1LinkShareAuth):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AuthToken | ModelsMessage | WebHTTPError]
    """

    kwargs = _get_kwargs(
        share=share,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    share: str,
    *,
    client: AuthenticatedClient | Client,
    body: V1LinkShareAuth,
) -> AuthToken | ModelsMessage | WebHTTPError | None:
    """Get an auth token for a share

     Get a jwt auth token for a shared project from a share hash.

    Args:
        share (str):
        body (V1LinkShareAuth):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AuthToken | ModelsMessage | WebHTTPError
    """

    return (
        await asyncio_detailed(
            share=share,
            client=client,
            body=body,
        )
    ).parsed
