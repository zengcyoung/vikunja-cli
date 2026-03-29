from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.models_api_token import ModelsAPIToken
from ...models.models_message import ModelsMessage
from ...models.web_http_error import WebHTTPError
from ...types import Response


def _get_kwargs(
    *,
    body: ModelsAPIToken,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/tokens",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ModelsAPIToken | ModelsMessage | WebHTTPError | None:
    if response.status_code == 200:
        response_200 = ModelsAPIToken.from_dict(response.json())

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
) -> Response[ModelsAPIToken | ModelsMessage | WebHTTPError]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: ModelsAPIToken,
) -> Response[ModelsAPIToken | ModelsMessage | WebHTTPError]:
    """Create a new api token

     Create a new api token to use on behalf of the user creating it.

    Args:
        body (ModelsAPIToken):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ModelsAPIToken | ModelsMessage | WebHTTPError]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    body: ModelsAPIToken,
) -> ModelsAPIToken | ModelsMessage | WebHTTPError | None:
    """Create a new api token

     Create a new api token to use on behalf of the user creating it.

    Args:
        body (ModelsAPIToken):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ModelsAPIToken | ModelsMessage | WebHTTPError
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: ModelsAPIToken,
) -> Response[ModelsAPIToken | ModelsMessage | WebHTTPError]:
    """Create a new api token

     Create a new api token to use on behalf of the user creating it.

    Args:
        body (ModelsAPIToken):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ModelsAPIToken | ModelsMessage | WebHTTPError]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: ModelsAPIToken,
) -> ModelsAPIToken | ModelsMessage | WebHTTPError | None:
    """Create a new api token

     Create a new api token to use on behalf of the user creating it.

    Args:
        body (ModelsAPIToken):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ModelsAPIToken | ModelsMessage | WebHTTPError
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
