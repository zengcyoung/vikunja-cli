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
    username: int,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/teams/{id}/members/{username}".format(
            id=quote(str(id), safe=""),
            username=quote(str(username), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ModelsMessage | None:
    if response.status_code == 200:
        response_200 = ModelsMessage.from_dict(response.json())

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
) -> Response[ModelsMessage]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    id: int,
    username: int,
    *,
    client: AuthenticatedClient,
) -> Response[ModelsMessage]:
    """Remove a user from a team

     Remove a user from a team. This will also revoke any access this user might have via that team. A
    user can remove themselves from the team if they are not the last user in the team.

    Args:
        id (int):
        username (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ModelsMessage]
    """

    kwargs = _get_kwargs(
        id=id,
        username=username,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    id: int,
    username: int,
    *,
    client: AuthenticatedClient,
) -> ModelsMessage | None:
    """Remove a user from a team

     Remove a user from a team. This will also revoke any access this user might have via that team. A
    user can remove themselves from the team if they are not the last user in the team.

    Args:
        id (int):
        username (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ModelsMessage
    """

    return sync_detailed(
        id=id,
        username=username,
        client=client,
    ).parsed


async def asyncio_detailed(
    id: int,
    username: int,
    *,
    client: AuthenticatedClient,
) -> Response[ModelsMessage]:
    """Remove a user from a team

     Remove a user from a team. This will also revoke any access this user might have via that team. A
    user can remove themselves from the team if they are not the last user in the team.

    Args:
        id (int):
        username (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ModelsMessage]
    """

    kwargs = _get_kwargs(
        id=id,
        username=username,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: int,
    username: int,
    *,
    client: AuthenticatedClient,
) -> ModelsMessage | None:
    """Remove a user from a team

     Remove a user from a team. This will also revoke any access this user might have via that team. A
    user can remove themselves from the team if they are not the last user in the team.

    Args:
        id (int):
        username (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ModelsMessage
    """

    return (
        await asyncio_detailed(
            id=id,
            username=username,
            client=client,
        )
    ).parsed
