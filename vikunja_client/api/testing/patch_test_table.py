from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.models_message import ModelsMessage
from ...models.user_user import UserUser
from ...types import Response


def _get_kwargs(
    table: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/test/{table}".format(
            table=quote(str(table), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ModelsMessage | list[UserUser] | None:
    if response.status_code == 201:
        response_201 = []
        _response_201 = response.json()
        for response_201_item_data in _response_201:
            response_201_item = UserUser.from_dict(response_201_item_data)

            response_201.append(response_201_item)

        return response_201

    if response.status_code == 500:
        response_500 = ModelsMessage.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[ModelsMessage | list[UserUser]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    table: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[ModelsMessage | list[UserUser]]:
    """Reset the db to a defined state

     Fills the specified table with the content provided in the payload. You need to enable the testing
    endpoint before doing this and provide the `Authorization: <token>` secret when making requests to
    this endpoint. See docs for more details.

    Args:
        table (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ModelsMessage | list[UserUser]]
    """

    kwargs = _get_kwargs(
        table=table,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    table: str,
    *,
    client: AuthenticatedClient | Client,
) -> ModelsMessage | list[UserUser] | None:
    """Reset the db to a defined state

     Fills the specified table with the content provided in the payload. You need to enable the testing
    endpoint before doing this and provide the `Authorization: <token>` secret when making requests to
    this endpoint. See docs for more details.

    Args:
        table (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ModelsMessage | list[UserUser]
    """

    return sync_detailed(
        table=table,
        client=client,
    ).parsed


async def asyncio_detailed(
    table: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[ModelsMessage | list[UserUser]]:
    """Reset the db to a defined state

     Fills the specified table with the content provided in the payload. You need to enable the testing
    endpoint before doing this and provide the `Authorization: <token>` secret when making requests to
    this endpoint. See docs for more details.

    Args:
        table (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ModelsMessage | list[UserUser]]
    """

    kwargs = _get_kwargs(
        table=table,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    table: str,
    *,
    client: AuthenticatedClient | Client,
) -> ModelsMessage | list[UserUser] | None:
    """Reset the db to a defined state

     Fills the specified table with the content provided in the payload. You need to enable the testing
    endpoint before doing this and provide the `Authorization: <token>` secret when making requests to
    this endpoint. See docs for more details.

    Args:
        table (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ModelsMessage | list[UserUser]
    """

    return (
        await asyncio_detailed(
            table=table,
            client=client,
        )
    ).parsed
