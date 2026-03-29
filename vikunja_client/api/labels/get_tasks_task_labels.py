from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.models_label import ModelsLabel
from ...models.models_message import ModelsMessage
from ...types import UNSET, Response, Unset


def _get_kwargs(
    task: int,
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
        "url": "/tasks/{task}/labels".format(
            task=quote(str(task), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ModelsMessage | list[ModelsLabel] | None:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = ModelsLabel.from_dict(response_200_item_data)

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
) -> Response[ModelsMessage | list[ModelsLabel]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    task: int,
    *,
    client: AuthenticatedClient,
    page: int | Unset = UNSET,
    per_page: int | Unset = UNSET,
    s: str | Unset = UNSET,
) -> Response[ModelsMessage | list[ModelsLabel]]:
    """Get all labels on a task

     Returns all labels which are assicociated with a given task.

    Args:
        task (int):
        page (int | Unset):
        per_page (int | Unset):
        s (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ModelsMessage | list[ModelsLabel]]
    """

    kwargs = _get_kwargs(
        task=task,
        page=page,
        per_page=per_page,
        s=s,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    task: int,
    *,
    client: AuthenticatedClient,
    page: int | Unset = UNSET,
    per_page: int | Unset = UNSET,
    s: str | Unset = UNSET,
) -> ModelsMessage | list[ModelsLabel] | None:
    """Get all labels on a task

     Returns all labels which are assicociated with a given task.

    Args:
        task (int):
        page (int | Unset):
        per_page (int | Unset):
        s (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ModelsMessage | list[ModelsLabel]
    """

    return sync_detailed(
        task=task,
        client=client,
        page=page,
        per_page=per_page,
        s=s,
    ).parsed


async def asyncio_detailed(
    task: int,
    *,
    client: AuthenticatedClient,
    page: int | Unset = UNSET,
    per_page: int | Unset = UNSET,
    s: str | Unset = UNSET,
) -> Response[ModelsMessage | list[ModelsLabel]]:
    """Get all labels on a task

     Returns all labels which are assicociated with a given task.

    Args:
        task (int):
        page (int | Unset):
        per_page (int | Unset):
        s (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ModelsMessage | list[ModelsLabel]]
    """

    kwargs = _get_kwargs(
        task=task,
        page=page,
        per_page=per_page,
        s=s,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    task: int,
    *,
    client: AuthenticatedClient,
    page: int | Unset = UNSET,
    per_page: int | Unset = UNSET,
    s: str | Unset = UNSET,
) -> ModelsMessage | list[ModelsLabel] | None:
    """Get all labels on a task

     Returns all labels which are assicociated with a given task.

    Args:
        task (int):
        page (int | Unset):
        per_page (int | Unset):
        s (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ModelsMessage | list[ModelsLabel]
    """

    return (
        await asyncio_detailed(
            task=task,
            client=client,
            page=page,
            per_page=per_page,
            s=s,
        )
    ).parsed
