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
    id: int,
    attachment_id: int,
    *,
    preview_size: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["preview_size"] = preview_size

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/tasks/{id}/attachments/{attachment_id}".format(
            id=quote(str(id), safe=""),
            attachment_id=quote(str(attachment_id), safe=""),
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

    if response.status_code == 403:
        response_403 = ModelsMessage.from_dict(response.content)

        return response_403

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
    id: int,
    attachment_id: int,
    *,
    client: AuthenticatedClient,
    preview_size: str | Unset = UNSET,
) -> Response[File | ModelsMessage]:
    """Get one attachment.

     Get one attachment for download. **Returns json on error.**

    Args:
        id (int):
        attachment_id (int):
        preview_size (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[File | ModelsMessage]
    """

    kwargs = _get_kwargs(
        id=id,
        attachment_id=attachment_id,
        preview_size=preview_size,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    id: int,
    attachment_id: int,
    *,
    client: AuthenticatedClient,
    preview_size: str | Unset = UNSET,
) -> File | ModelsMessage | None:
    """Get one attachment.

     Get one attachment for download. **Returns json on error.**

    Args:
        id (int):
        attachment_id (int):
        preview_size (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        File | ModelsMessage
    """

    return sync_detailed(
        id=id,
        attachment_id=attachment_id,
        client=client,
        preview_size=preview_size,
    ).parsed


async def asyncio_detailed(
    id: int,
    attachment_id: int,
    *,
    client: AuthenticatedClient,
    preview_size: str | Unset = UNSET,
) -> Response[File | ModelsMessage]:
    """Get one attachment.

     Get one attachment for download. **Returns json on error.**

    Args:
        id (int):
        attachment_id (int):
        preview_size (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[File | ModelsMessage]
    """

    kwargs = _get_kwargs(
        id=id,
        attachment_id=attachment_id,
        preview_size=preview_size,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: int,
    attachment_id: int,
    *,
    client: AuthenticatedClient,
    preview_size: str | Unset = UNSET,
) -> File | ModelsMessage | None:
    """Get one attachment.

     Get one attachment for download. **Returns json on error.**

    Args:
        id (int):
        attachment_id (int):
        preview_size (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        File | ModelsMessage
    """

    return (
        await asyncio_detailed(
            id=id,
            attachment_id=attachment_id,
            client=client,
            preview_size=preview_size,
        )
    ).parsed
