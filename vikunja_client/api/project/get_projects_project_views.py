from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.models_message import ModelsMessage
from ...models.models_project_view import ModelsProjectView
from ...types import Response


def _get_kwargs(
    project: int,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/projects/{project}/views".format(
            project=quote(str(project), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ModelsMessage | list[ModelsProjectView] | None:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = ModelsProjectView.from_dict(response_200_item_data)

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
) -> Response[ModelsMessage | list[ModelsProjectView]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    project: int,
    *,
    client: AuthenticatedClient,
) -> Response[ModelsMessage | list[ModelsProjectView]]:
    """Get all project views for a project

     Returns all project views for a sepcific project

    Args:
        project (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ModelsMessage | list[ModelsProjectView]]
    """

    kwargs = _get_kwargs(
        project=project,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    project: int,
    *,
    client: AuthenticatedClient,
) -> ModelsMessage | list[ModelsProjectView] | None:
    """Get all project views for a project

     Returns all project views for a sepcific project

    Args:
        project (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ModelsMessage | list[ModelsProjectView]
    """

    return sync_detailed(
        project=project,
        client=client,
    ).parsed


async def asyncio_detailed(
    project: int,
    *,
    client: AuthenticatedClient,
) -> Response[ModelsMessage | list[ModelsProjectView]]:
    """Get all project views for a project

     Returns all project views for a sepcific project

    Args:
        project (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ModelsMessage | list[ModelsProjectView]]
    """

    kwargs = _get_kwargs(
        project=project,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    project: int,
    *,
    client: AuthenticatedClient,
) -> ModelsMessage | list[ModelsProjectView] | None:
    """Get all project views for a project

     Returns all project views for a sepcific project

    Args:
        project (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ModelsMessage | list[ModelsProjectView]
    """

    return (
        await asyncio_detailed(
            project=project,
            client=client,
        )
    ).parsed
