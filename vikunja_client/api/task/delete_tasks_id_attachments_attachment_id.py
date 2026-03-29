from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.models_message import ModelsMessage
from ...types import Response


def _get_kwargs(
    id: int,
    attachment_id: int,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/tasks/{id}/attachments/{attachment_id}".format(
            id=quote(str(id), safe=""),
            attachment_id=quote(str(attachment_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ModelsMessage | None:
    if response.status_code == 200:
        response_200 = ModelsMessage.from_dict(response.json())

        return response_200

    if response.status_code == 403:
        response_403 = ModelsMessage.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = ModelsMessage.from_dict(response.json())

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
) -> Response[ModelsMessage]:
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
) -> Response[ModelsMessage]:
    """Delete an attachment

     Delete an attachment.

    Args:
        id (int):
        attachment_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ModelsMessage]
    """

    kwargs = _get_kwargs(
        id=id,
        attachment_id=attachment_id,
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
) -> ModelsMessage | None:
    """Delete an attachment

     Delete an attachment.

    Args:
        id (int):
        attachment_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ModelsMessage
    """

    return sync_detailed(
        id=id,
        attachment_id=attachment_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    id: int,
    attachment_id: int,
    *,
    client: AuthenticatedClient,
) -> Response[ModelsMessage]:
    """Delete an attachment

     Delete an attachment.

    Args:
        id (int):
        attachment_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ModelsMessage]
    """

    kwargs = _get_kwargs(
        id=id,
        attachment_id=attachment_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: int,
    attachment_id: int,
    *,
    client: AuthenticatedClient,
) -> ModelsMessage | None:
    """Delete an attachment

     Delete an attachment.

    Args:
        id (int):
        attachment_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ModelsMessage
    """

    return (
        await asyncio_detailed(
            id=id,
            attachment_id=attachment_id,
            client=client,
        )
    ).parsed
