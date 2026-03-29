from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.models_link_sharing import ModelsLinkSharing
from ...models.models_message import ModelsMessage
from ...models.web_http_error import WebHTTPError
from ...types import Response


def _get_kwargs(
    project: int,
    share: int,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/projects/{project}/shares/{share}".format(
            project=quote(str(project), safe=""),
            share=quote(str(share), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ModelsLinkSharing | ModelsMessage | WebHTTPError | None:
    if response.status_code == 200:
        response_200 = ModelsLinkSharing.from_dict(response.json())

        return response_200

    if response.status_code == 403:
        response_403 = WebHTTPError.from_dict(response.json())

        return response_403

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
) -> Response[ModelsLinkSharing | ModelsMessage | WebHTTPError]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    project: int,
    share: int,
    *,
    client: AuthenticatedClient,
) -> Response[ModelsLinkSharing | ModelsMessage | WebHTTPError]:
    """Get one link shares for a project

     Returns one link share by its ID.

    Args:
        project (int):
        share (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ModelsLinkSharing | ModelsMessage | WebHTTPError]
    """

    kwargs = _get_kwargs(
        project=project,
        share=share,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    project: int,
    share: int,
    *,
    client: AuthenticatedClient,
) -> ModelsLinkSharing | ModelsMessage | WebHTTPError | None:
    """Get one link shares for a project

     Returns one link share by its ID.

    Args:
        project (int):
        share (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ModelsLinkSharing | ModelsMessage | WebHTTPError
    """

    return sync_detailed(
        project=project,
        share=share,
        client=client,
    ).parsed


async def asyncio_detailed(
    project: int,
    share: int,
    *,
    client: AuthenticatedClient,
) -> Response[ModelsLinkSharing | ModelsMessage | WebHTTPError]:
    """Get one link shares for a project

     Returns one link share by its ID.

    Args:
        project (int):
        share (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ModelsLinkSharing | ModelsMessage | WebHTTPError]
    """

    kwargs = _get_kwargs(
        project=project,
        share=share,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    project: int,
    share: int,
    *,
    client: AuthenticatedClient,
) -> ModelsLinkSharing | ModelsMessage | WebHTTPError | None:
    """Get one link shares for a project

     Returns one link share by its ID.

    Args:
        project (int):
        share (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ModelsLinkSharing | ModelsMessage | WebHTTPError
    """

    return (
        await asyncio_detailed(
            project=project,
            share=share,
            client=client,
        )
    ).parsed
