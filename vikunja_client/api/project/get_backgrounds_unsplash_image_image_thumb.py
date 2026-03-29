from http import HTTPStatus
from io import BytesIO
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.models_message import ModelsMessage
from ...types import File, Response


def _get_kwargs(
    image: int,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/backgrounds/unsplash/image/{image}/thumb".format(
            image=quote(str(image), safe=""),
        ),
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
    image: int,
    *,
    client: AuthenticatedClient,
) -> Response[File | ModelsMessage]:
    """Get an unsplash thumbnail image

     Get an unsplash thumbnail image. The thumbnail is cropped to a max width of 200px. **Returns json on
    error.**

    Args:
        image (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[File | ModelsMessage]
    """

    kwargs = _get_kwargs(
        image=image,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    image: int,
    *,
    client: AuthenticatedClient,
) -> File | ModelsMessage | None:
    """Get an unsplash thumbnail image

     Get an unsplash thumbnail image. The thumbnail is cropped to a max width of 200px. **Returns json on
    error.**

    Args:
        image (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        File | ModelsMessage
    """

    return sync_detailed(
        image=image,
        client=client,
    ).parsed


async def asyncio_detailed(
    image: int,
    *,
    client: AuthenticatedClient,
) -> Response[File | ModelsMessage]:
    """Get an unsplash thumbnail image

     Get an unsplash thumbnail image. The thumbnail is cropped to a max width of 200px. **Returns json on
    error.**

    Args:
        image (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[File | ModelsMessage]
    """

    kwargs = _get_kwargs(
        image=image,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    image: int,
    *,
    client: AuthenticatedClient,
) -> File | ModelsMessage | None:
    """Get an unsplash thumbnail image

     Get an unsplash thumbnail image. The thumbnail is cropped to a max width of 200px. **Returns json on
    error.**

    Args:
        image (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        File | ModelsMessage
    """

    return (
        await asyncio_detailed(
            image=image,
            client=client,
        )
    ).parsed
