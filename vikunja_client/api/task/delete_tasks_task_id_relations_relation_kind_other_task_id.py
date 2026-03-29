from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.models_message import ModelsMessage
from ...models.models_task_relation import ModelsTaskRelation
from ...models.web_http_error import WebHTTPError
from ...types import Response


def _get_kwargs(
    task_id: int,
    relation_kind: str,
    other_task_id: int,
    *,
    body: ModelsTaskRelation,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/tasks/{task_id}/relations/{relation_kind}/{other_task_id}".format(
            task_id=quote(str(task_id), safe=""),
            relation_kind=quote(str(relation_kind), safe=""),
            other_task_id=quote(str(other_task_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ModelsMessage | WebHTTPError | None:
    if response.status_code == 200:
        response_200 = ModelsMessage.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = WebHTTPError.from_dict(response.json())

        return response_400

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
    task_id: int,
    relation_kind: str,
    other_task_id: int,
    *,
    client: AuthenticatedClient,
    body: ModelsTaskRelation,
) -> Response[ModelsMessage | WebHTTPError]:
    """Remove a task relation

    Args:
        task_id (int):
        relation_kind (str):
        other_task_id (int):
        body (ModelsTaskRelation):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ModelsMessage | WebHTTPError]
    """

    kwargs = _get_kwargs(
        task_id=task_id,
        relation_kind=relation_kind,
        other_task_id=other_task_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    task_id: int,
    relation_kind: str,
    other_task_id: int,
    *,
    client: AuthenticatedClient,
    body: ModelsTaskRelation,
) -> ModelsMessage | WebHTTPError | None:
    """Remove a task relation

    Args:
        task_id (int):
        relation_kind (str):
        other_task_id (int):
        body (ModelsTaskRelation):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ModelsMessage | WebHTTPError
    """

    return sync_detailed(
        task_id=task_id,
        relation_kind=relation_kind,
        other_task_id=other_task_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    task_id: int,
    relation_kind: str,
    other_task_id: int,
    *,
    client: AuthenticatedClient,
    body: ModelsTaskRelation,
) -> Response[ModelsMessage | WebHTTPError]:
    """Remove a task relation

    Args:
        task_id (int):
        relation_kind (str):
        other_task_id (int):
        body (ModelsTaskRelation):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ModelsMessage | WebHTTPError]
    """

    kwargs = _get_kwargs(
        task_id=task_id,
        relation_kind=relation_kind,
        other_task_id=other_task_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    task_id: int,
    relation_kind: str,
    other_task_id: int,
    *,
    client: AuthenticatedClient,
    body: ModelsTaskRelation,
) -> ModelsMessage | WebHTTPError | None:
    """Remove a task relation

    Args:
        task_id (int):
        relation_kind (str):
        other_task_id (int):
        body (ModelsTaskRelation):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ModelsMessage | WebHTTPError
    """

    return (
        await asyncio_detailed(
            task_id=task_id,
            relation_kind=relation_kind,
            other_task_id=other_task_id,
            client=client,
            body=body,
        )
    ).parsed
