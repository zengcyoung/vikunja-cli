from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.background_image import BackgroundImage
from ...models.models_message import ModelsMessage
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    s: str | Unset = UNSET,
    p: int | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["s"] = s

    params["p"] = p

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/backgrounds/unsplash/search",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ModelsMessage | list[BackgroundImage] | None:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = BackgroundImage.from_dict(response_200_item_data)

            response_200.append(response_200_item)

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
) -> Response[ModelsMessage | list[BackgroundImage]]:
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
    p: int | Unset = UNSET,
) -> Response[ModelsMessage | list[BackgroundImage]]:
    """Search for a background from unsplash

     Search for a project background from unsplash

    Args:
        s (str | Unset):
        p (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ModelsMessage | list[BackgroundImage]]
    """

    kwargs = _get_kwargs(
        s=s,
        p=p,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    s: str | Unset = UNSET,
    p: int | Unset = UNSET,
) -> ModelsMessage | list[BackgroundImage] | None:
    """Search for a background from unsplash

     Search for a project background from unsplash

    Args:
        s (str | Unset):
        p (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ModelsMessage | list[BackgroundImage]
    """

    return sync_detailed(
        client=client,
        s=s,
        p=p,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    s: str | Unset = UNSET,
    p: int | Unset = UNSET,
) -> Response[ModelsMessage | list[BackgroundImage]]:
    """Search for a background from unsplash

     Search for a project background from unsplash

    Args:
        s (str | Unset):
        p (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ModelsMessage | list[BackgroundImage]]
    """

    kwargs = _get_kwargs(
        s=s,
        p=p,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    s: str | Unset = UNSET,
    p: int | Unset = UNSET,
) -> ModelsMessage | list[BackgroundImage] | None:
    """Search for a background from unsplash

     Search for a project background from unsplash

    Args:
        s (str | Unset):
        p (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ModelsMessage | list[BackgroundImage]
    """

    return (
        await asyncio_detailed(
            client=client,
            s=s,
            p=p,
        )
    ).parsed
