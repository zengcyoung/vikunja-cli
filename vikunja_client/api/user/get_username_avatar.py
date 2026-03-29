from http import HTTPStatus
from io import BytesIO
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.models_message import ModelsMessage
from ...types import UNSET, File, Response, Unset


def _get_kwargs(
    username: str,
    *,
    size: int | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["size"] = size

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/{username}/avatar".format(
            username=quote(str(username), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> File | ModelsMessage | None:
    if response.status_code == 200:
        response_200 = File(payload=BytesIO(response.content))

        return response_200

    if response.status_code == 404:
        response_404 = ModelsMessage.from_dict(response.content)

        return response_404

    if response.status_code == 500:
        response_500 = ModelsMessage.from_dict(response.content)

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[File | ModelsMessage]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    username: str,
    *,
    client: AuthenticatedClient | Client,
    size: int | Unset = UNSET,
) -> Response[File | ModelsMessage]:
    """User Avatar

     Returns the user avatar as image.

    Args:
        username (str):
        size (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[File | ModelsMessage]
    """

    kwargs = _get_kwargs(
        username=username,
        size=size,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    username: str,
    *,
    client: AuthenticatedClient | Client,
    size: int | Unset = UNSET,
) -> File | ModelsMessage | None:
    """User Avatar

     Returns the user avatar as image.

    Args:
        username (str):
        size (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        File | ModelsMessage
    """

    return sync_detailed(
        username=username,
        client=client,
        size=size,
    ).parsed


async def asyncio_detailed(
    username: str,
    *,
    client: AuthenticatedClient | Client,
    size: int | Unset = UNSET,
) -> Response[File | ModelsMessage]:
    """User Avatar

     Returns the user avatar as image.

    Args:
        username (str):
        size (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[File | ModelsMessage]
    """

    kwargs = _get_kwargs(
        username=username,
        size=size,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    username: str,
    *,
    client: AuthenticatedClient | Client,
    size: int | Unset = UNSET,
) -> File | ModelsMessage | None:
    """User Avatar

     Returns the user avatar as image.

    Args:
        username (str):
        size (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        File | ModelsMessage
    """

    return (
        await asyncio_detailed(
            username=username,
            client=client,
            size=size,
        )
    ).parsed
