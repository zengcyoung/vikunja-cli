from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.auth_token import AuthToken
from ...models.models_message import ModelsMessage
from ...models.openid_callback import OpenidCallback
from ...types import Response


def _get_kwargs(
    provider: int,
    *,
    body: OpenidCallback,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/auth/openid/{provider}/callback".format(
            provider=quote(str(provider), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> AuthToken | ModelsMessage | None:
    if response.status_code == 200:
        response_200 = AuthToken.from_dict(response.json())

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
) -> Response[AuthToken | ModelsMessage]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    provider: int,
    *,
    client: AuthenticatedClient,
    body: OpenidCallback,
) -> Response[AuthToken | ModelsMessage]:
    """Authenticate a user with OpenID Connect

     After a redirect from the OpenID Connect provider to the frontend has been made with the
    authentication `code`, this endpoint can be used to obtain a jwt token for that user and thus log
    them in.

    Args:
        provider (int):
        body (OpenidCallback):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AuthToken | ModelsMessage]
    """

    kwargs = _get_kwargs(
        provider=provider,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    provider: int,
    *,
    client: AuthenticatedClient,
    body: OpenidCallback,
) -> AuthToken | ModelsMessage | None:
    """Authenticate a user with OpenID Connect

     After a redirect from the OpenID Connect provider to the frontend has been made with the
    authentication `code`, this endpoint can be used to obtain a jwt token for that user and thus log
    them in.

    Args:
        provider (int):
        body (OpenidCallback):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AuthToken | ModelsMessage
    """

    return sync_detailed(
        provider=provider,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    provider: int,
    *,
    client: AuthenticatedClient,
    body: OpenidCallback,
) -> Response[AuthToken | ModelsMessage]:
    """Authenticate a user with OpenID Connect

     After a redirect from the OpenID Connect provider to the frontend has been made with the
    authentication `code`, this endpoint can be used to obtain a jwt token for that user and thus log
    them in.

    Args:
        provider (int):
        body (OpenidCallback):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AuthToken | ModelsMessage]
    """

    kwargs = _get_kwargs(
        provider=provider,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    provider: int,
    *,
    client: AuthenticatedClient,
    body: OpenidCallback,
) -> AuthToken | ModelsMessage | None:
    """Authenticate a user with OpenID Connect

     After a redirect from the OpenID Connect provider to the frontend has been made with the
    authentication `code`, this endpoint can be used to obtain a jwt token for that user and thus log
    them in.

    Args:
        provider (int):
        body (OpenidCallback):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AuthToken | ModelsMessage
    """

    return (
        await asyncio_detailed(
            provider=provider,
            client=client,
            body=body,
        )
    ).parsed
