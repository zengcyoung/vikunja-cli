from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.models_message import ModelsMessage
from ...models.models_team_with_permission import ModelsTeamWithPermission
from ...models.web_http_error import WebHTTPError
from ...types import UNSET, Response, Unset


def _get_kwargs(
    id: int,
    *,
    page: int | Unset = UNSET,
    per_page: int | Unset = UNSET,
    s: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["page"] = page

    params["per_page"] = per_page

    params["s"] = s

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/projects/{id}/teams".format(
            id=quote(str(id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ModelsMessage | WebHTTPError | list[ModelsTeamWithPermission] | None:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = ModelsTeamWithPermission.from_dict(
                response_200_item_data
            )

            response_200.append(response_200_item)

        return response_200

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
) -> Response[ModelsMessage | WebHTTPError | list[ModelsTeamWithPermission]]:
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
    page: int | Unset = UNSET,
    per_page: int | Unset = UNSET,
    s: str | Unset = UNSET,
) -> Response[ModelsMessage | WebHTTPError | list[ModelsTeamWithPermission]]:
    """Get teams on a project

     Returns a project with all teams which have access on a given project.

    Args:
        id (int):
        page (int | Unset):
        per_page (int | Unset):
        s (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ModelsMessage | WebHTTPError | list[ModelsTeamWithPermission]]
    """

    kwargs = _get_kwargs(
        id=id,
        page=page,
        per_page=per_page,
        s=s,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    id: int,
    *,
    client: AuthenticatedClient,
    page: int | Unset = UNSET,
    per_page: int | Unset = UNSET,
    s: str | Unset = UNSET,
) -> ModelsMessage | WebHTTPError | list[ModelsTeamWithPermission] | None:
    """Get teams on a project

     Returns a project with all teams which have access on a given project.

    Args:
        id (int):
        page (int | Unset):
        per_page (int | Unset):
        s (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ModelsMessage | WebHTTPError | list[ModelsTeamWithPermission]
    """

    return sync_detailed(
        id=id,
        client=client,
        page=page,
        per_page=per_page,
        s=s,
    ).parsed


async def asyncio_detailed(
    id: int,
    *,
    client: AuthenticatedClient,
    page: int | Unset = UNSET,
    per_page: int | Unset = UNSET,
    s: str | Unset = UNSET,
) -> Response[ModelsMessage | WebHTTPError | list[ModelsTeamWithPermission]]:
    """Get teams on a project

     Returns a project with all teams which have access on a given project.

    Args:
        id (int):
        page (int | Unset):
        per_page (int | Unset):
        s (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ModelsMessage | WebHTTPError | list[ModelsTeamWithPermission]]
    """

    kwargs = _get_kwargs(
        id=id,
        page=page,
        per_page=per_page,
        s=s,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: int,
    *,
    client: AuthenticatedClient,
    page: int | Unset = UNSET,
    per_page: int | Unset = UNSET,
    s: str | Unset = UNSET,
) -> ModelsMessage | WebHTTPError | list[ModelsTeamWithPermission] | None:
    """Get teams on a project

     Returns a project with all teams which have access on a given project.

    Args:
        id (int):
        page (int | Unset):
        per_page (int | Unset):
        s (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ModelsMessage | WebHTTPError | list[ModelsTeamWithPermission]
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            page=page,
            per_page=per_page,
            s=s,
        )
    ).parsed
