from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.models_message import ModelsMessage
from ...models.models_webhook import ModelsWebhook
from ...models.web_http_error import WebHTTPError
from ...types import Response


def _get_kwargs(
    *,
    body: ModelsWebhook,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/user/settings/webhooks",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ModelsMessage | ModelsWebhook | WebHTTPError | None:
    if response.status_code == 200:
        response_200 = ModelsWebhook.from_dict(response.json())

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
) -> Response[ModelsMessage | ModelsWebhook | WebHTTPError]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: ModelsWebhook,
) -> Response[ModelsMessage | ModelsWebhook | WebHTTPError]:
    """Create a user-level webhook target

     Create a webhook target for the current user that receives events across all projects.

    Args:
        body (ModelsWebhook):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ModelsMessage | ModelsWebhook | WebHTTPError]
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
    body: ModelsWebhook,
) -> ModelsMessage | ModelsWebhook | WebHTTPError | None:
    """Create a user-level webhook target

     Create a webhook target for the current user that receives events across all projects.

    Args:
        body (ModelsWebhook):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ModelsMessage | ModelsWebhook | WebHTTPError
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: ModelsWebhook,
) -> Response[ModelsMessage | ModelsWebhook | WebHTTPError]:
    """Create a user-level webhook target

     Create a webhook target for the current user that receives events across all projects.

    Args:
        body (ModelsWebhook):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ModelsMessage | ModelsWebhook | WebHTTPError]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: ModelsWebhook,
) -> ModelsMessage | ModelsWebhook | WebHTTPError | None:
    """Create a user-level webhook target

     Create a webhook target for the current user that receives events across all projects.

    Args:
        body (ModelsWebhook):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ModelsMessage | ModelsWebhook | WebHTTPError
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
