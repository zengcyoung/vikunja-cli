from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.models_message import ModelsMessage
from ...models.web_http_error import WebHTTPError
from ...types import Response


def _get_kwargs(
    project_id: int,
    view: int,
    bucket_id: int,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/projects/{project_id}/views/{view}/buckets/{bucket_id}".format(
            project_id=quote(str(project_id), safe=""),
            view=quote(str(view), safe=""),
            bucket_id=quote(str(bucket_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ModelsMessage | WebHTTPError | None:
    if response.status_code == 200:
        response_200 = ModelsMessage.from_dict(response.json())

        return response_200

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
) -> Response[ModelsMessage | WebHTTPError]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    project_id: int,
    view: int,
    bucket_id: int,
    *,
    client: AuthenticatedClient,
) -> Response[ModelsMessage | WebHTTPError]:
    """Deletes an existing bucket

     Deletes an existing kanban bucket and dissociates all of its task. It does not delete any tasks. You
    cannot delete the last bucket on a project.

    Args:
        project_id (int):
        view (int):
        bucket_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ModelsMessage | WebHTTPError]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        view=view,
        bucket_id=bucket_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    project_id: int,
    view: int,
    bucket_id: int,
    *,
    client: AuthenticatedClient,
) -> ModelsMessage | WebHTTPError | None:
    """Deletes an existing bucket

     Deletes an existing kanban bucket and dissociates all of its task. It does not delete any tasks. You
    cannot delete the last bucket on a project.

    Args:
        project_id (int):
        view (int):
        bucket_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ModelsMessage | WebHTTPError
    """

    return sync_detailed(
        project_id=project_id,
        view=view,
        bucket_id=bucket_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    project_id: int,
    view: int,
    bucket_id: int,
    *,
    client: AuthenticatedClient,
) -> Response[ModelsMessage | WebHTTPError]:
    """Deletes an existing bucket

     Deletes an existing kanban bucket and dissociates all of its task. It does not delete any tasks. You
    cannot delete the last bucket on a project.

    Args:
        project_id (int):
        view (int):
        bucket_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ModelsMessage | WebHTTPError]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        view=view,
        bucket_id=bucket_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    project_id: int,
    view: int,
    bucket_id: int,
    *,
    client: AuthenticatedClient,
) -> ModelsMessage | WebHTTPError | None:
    """Deletes an existing bucket

     Deletes an existing kanban bucket and dissociates all of its task. It does not delete any tasks. You
    cannot delete the last bucket on a project.

    Args:
        project_id (int):
        view (int):
        bucket_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ModelsMessage | WebHTTPError
    """

    return (
        await asyncio_detailed(
            project_id=project_id,
            view=view,
            bucket_id=bucket_id,
            client=client,
        )
    ).parsed
