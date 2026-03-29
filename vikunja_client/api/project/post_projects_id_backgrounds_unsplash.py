from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.background_image import BackgroundImage
from ...models.models_message import ModelsMessage
from ...models.models_project import ModelsProject
from ...models.web_http_error import WebHTTPError
from ...types import Response


def _get_kwargs(
    id: int,
    *,
    body: BackgroundImage,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/projects/{id}/backgrounds/unsplash".format(
            id=quote(str(id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ModelsMessage | ModelsProject | WebHTTPError | None:
    if response.status_code == 200:
        response_200 = ModelsProject.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = WebHTTPError.from_dict(response.json())

        return response_400

    if response.status_code == 403:
        response_403 = WebHTTPError.from_dict(response.json())

        return response_403

    if response.status_code == 500:
        response_500 = ModelsMessage.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[ModelsMessage | ModelsProject | WebHTTPError]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    id: int,
    *,
    client: AuthenticatedClient,
    body: BackgroundImage,
) -> Response[ModelsMessage | ModelsProject | WebHTTPError]:
    """Set an unsplash photo as project background

     Sets a photo from unsplash as project background.

    Args:
        id (int):
        body (BackgroundImage):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ModelsMessage | ModelsProject | WebHTTPError]
    """

    kwargs = _get_kwargs(
        id=id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    id: int,
    *,
    client: AuthenticatedClient,
    body: BackgroundImage,
) -> ModelsMessage | ModelsProject | WebHTTPError | None:
    """Set an unsplash photo as project background

     Sets a photo from unsplash as project background.

    Args:
        id (int):
        body (BackgroundImage):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ModelsMessage | ModelsProject | WebHTTPError
    """

    return sync_detailed(
        id=id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    id: int,
    *,
    client: AuthenticatedClient,
    body: BackgroundImage,
) -> Response[ModelsMessage | ModelsProject | WebHTTPError]:
    """Set an unsplash photo as project background

     Sets a photo from unsplash as project background.

    Args:
        id (int):
        body (BackgroundImage):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ModelsMessage | ModelsProject | WebHTTPError]
    """

    kwargs = _get_kwargs(
        id=id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: int,
    *,
    client: AuthenticatedClient,
    body: BackgroundImage,
) -> ModelsMessage | ModelsProject | WebHTTPError | None:
    """Set an unsplash photo as project background

     Sets a photo from unsplash as project background.

    Args:
        id (int):
        body (BackgroundImage):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ModelsMessage | ModelsProject | WebHTTPError
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            body=body,
        )
    ).parsed
