from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.models_message import ModelsMessage
from ...models.models_team_project import ModelsTeamProject
from ...models.web_http_error import WebHTTPError
from ...types import Response


def _get_kwargs(
    project_id: int,
    team_id: int,
    *,
    body: ModelsTeamProject,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/projects/{project_id}/teams/{team_id}".format(
            project_id=quote(str(project_id), safe=""),
            team_id=quote(str(team_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ModelsMessage | ModelsTeamProject | WebHTTPError | None:
    if response.status_code == 200:
        response_200 = ModelsTeamProject.from_dict(response.json())

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
) -> Response[ModelsMessage | ModelsTeamProject | WebHTTPError]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    project_id: int,
    team_id: int,
    *,
    client: AuthenticatedClient,
    body: ModelsTeamProject,
) -> Response[ModelsMessage | ModelsTeamProject | WebHTTPError]:
    """Update a team <-> project relation

     Update a team <-> project relation. Mostly used to update the permission that team has.

    Args:
        project_id (int):
        team_id (int):
        body (ModelsTeamProject):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ModelsMessage | ModelsTeamProject | WebHTTPError]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        team_id=team_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    project_id: int,
    team_id: int,
    *,
    client: AuthenticatedClient,
    body: ModelsTeamProject,
) -> ModelsMessage | ModelsTeamProject | WebHTTPError | None:
    """Update a team <-> project relation

     Update a team <-> project relation. Mostly used to update the permission that team has.

    Args:
        project_id (int):
        team_id (int):
        body (ModelsTeamProject):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ModelsMessage | ModelsTeamProject | WebHTTPError
    """

    return sync_detailed(
        project_id=project_id,
        team_id=team_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    project_id: int,
    team_id: int,
    *,
    client: AuthenticatedClient,
    body: ModelsTeamProject,
) -> Response[ModelsMessage | ModelsTeamProject | WebHTTPError]:
    """Update a team <-> project relation

     Update a team <-> project relation. Mostly used to update the permission that team has.

    Args:
        project_id (int):
        team_id (int):
        body (ModelsTeamProject):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ModelsMessage | ModelsTeamProject | WebHTTPError]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        team_id=team_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    project_id: int,
    team_id: int,
    *,
    client: AuthenticatedClient,
    body: ModelsTeamProject,
) -> ModelsMessage | ModelsTeamProject | WebHTTPError | None:
    """Update a team <-> project relation

     Update a team <-> project relation. Mostly used to update the permission that team has.

    Args:
        project_id (int):
        team_id (int):
        body (ModelsTeamProject):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ModelsMessage | ModelsTeamProject | WebHTTPError
    """

    return (
        await asyncio_detailed(
            project_id=project_id,
            team_id=team_id,
            client=client,
            body=body,
        )
    ).parsed
