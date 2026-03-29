from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.models_message import ModelsMessage
from ...models.models_task import ModelsTask
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    page: int | Unset = UNSET,
    per_page: int | Unset = UNSET,
    s: str | Unset = UNSET,
    sort_by: str | Unset = UNSET,
    order_by: str | Unset = UNSET,
    filter_: str | Unset = UNSET,
    filter_timezone: str | Unset = UNSET,
    filter_include_nulls: str | Unset = UNSET,
    expand: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["page"] = page

    params["per_page"] = per_page

    params["s"] = s

    params["sort_by"] = sort_by

    params["order_by"] = order_by

    params["filter"] = filter_

    params["filter_timezone"] = filter_timezone

    params["filter_include_nulls"] = filter_include_nulls

    params["expand"] = expand

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/tasks",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ModelsMessage | list[ModelsTask] | None:
    if response.status_code == 200:
        # Guard against empty body (server returns 200 with no content when there are no tasks)
        if not response.content:
            return []
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = ModelsTask.from_dict(response_200_item_data)

            response_200.append(response_200_item)

        return response_200

    if response.status_code == 204:
        # No Content — no tasks found
        return []

    if response.status_code == 500:
        response_500 = ModelsMessage.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[ModelsMessage | list[ModelsTask]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    page: int | Unset = UNSET,
    per_page: int | Unset = UNSET,
    s: str | Unset = UNSET,
    sort_by: str | Unset = UNSET,
    order_by: str | Unset = UNSET,
    filter_: str | Unset = UNSET,
    filter_timezone: str | Unset = UNSET,
    filter_include_nulls: str | Unset = UNSET,
    expand: str | Unset = UNSET,
) -> Response[ModelsMessage | list[ModelsTask]]:
    """Get tasks

     Returns all tasks on any project the user has access to.

    Args:
        page (int | Unset):
        per_page (int | Unset):
        s (str | Unset):
        sort_by (str | Unset):
        order_by (str | Unset):
        filter_ (str | Unset):
        filter_timezone (str | Unset):
        filter_include_nulls (str | Unset):
        expand (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ModelsMessage | list[ModelsTask]]
    """

    kwargs = _get_kwargs(
        page=page,
        per_page=per_page,
        s=s,
        sort_by=sort_by,
        order_by=order_by,
        filter_=filter_,
        filter_timezone=filter_timezone,
        filter_include_nulls=filter_include_nulls,
        expand=expand,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    page: int | Unset = UNSET,
    per_page: int | Unset = UNSET,
    s: str | Unset = UNSET,
    sort_by: str | Unset = UNSET,
    order_by: str | Unset = UNSET,
    filter_: str | Unset = UNSET,
    filter_timezone: str | Unset = UNSET,
    filter_include_nulls: str | Unset = UNSET,
    expand: str | Unset = UNSET,
) -> ModelsMessage | list[ModelsTask] | None:
    """Get tasks

     Returns all tasks on any project the user has access to.

    Args:
        page (int | Unset):
        per_page (int | Unset):
        s (str | Unset):
        sort_by (str | Unset):
        order_by (str | Unset):
        filter_ (str | Unset):
        filter_timezone (str | Unset):
        filter_include_nulls (str | Unset):
        expand (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ModelsMessage | list[ModelsTask]
    """

    return sync_detailed(
        client=client,
        page=page,
        per_page=per_page,
        s=s,
        sort_by=sort_by,
        order_by=order_by,
        filter_=filter_,
        filter_timezone=filter_timezone,
        filter_include_nulls=filter_include_nulls,
        expand=expand,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    page: int | Unset = UNSET,
    per_page: int | Unset = UNSET,
    s: str | Unset = UNSET,
    sort_by: str | Unset = UNSET,
    order_by: str | Unset = UNSET,
    filter_: str | Unset = UNSET,
    filter_timezone: str | Unset = UNSET,
    filter_include_nulls: str | Unset = UNSET,
    expand: str | Unset = UNSET,
) -> Response[ModelsMessage | list[ModelsTask]]:
    """Get tasks

     Returns all tasks on any project the user has access to.

    Args:
        page (int | Unset):
        per_page (int | Unset):
        s (str | Unset):
        sort_by (str | Unset):
        order_by (str | Unset):
        filter_ (str | Unset):
        filter_timezone (str | Unset):
        filter_include_nulls (str | Unset):
        expand (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ModelsMessage | list[ModelsTask]]
    """

    kwargs = _get_kwargs(
        page=page,
        per_page=per_page,
        s=s,
        sort_by=sort_by,
        order_by=order_by,
        filter_=filter_,
        filter_timezone=filter_timezone,
        filter_include_nulls=filter_include_nulls,
        expand=expand,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    page: int | Unset = UNSET,
    per_page: int | Unset = UNSET,
    s: str | Unset = UNSET,
    sort_by: str | Unset = UNSET,
    order_by: str | Unset = UNSET,
    filter_: str | Unset = UNSET,
    filter_timezone: str | Unset = UNSET,
    filter_include_nulls: str | Unset = UNSET,
    expand: str | Unset = UNSET,
) -> ModelsMessage | list[ModelsTask] | None:
    """Get tasks

     Returns all tasks on any project the user has access to.

    Args:
        page (int | Unset):
        per_page (int | Unset):
        s (str | Unset):
        sort_by (str | Unset):
        order_by (str | Unset):
        filter_ (str | Unset):
        filter_timezone (str | Unset):
        filter_include_nulls (str | Unset):
        expand (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ModelsMessage | list[ModelsTask]
    """

    return (
        await asyncio_detailed(
            client=client,
            page=page,
            per_page=per_page,
            s=s,
            sort_by=sort_by,
            order_by=order_by,
            filter_=filter_,
            filter_timezone=filter_timezone,
            filter_include_nulls=filter_include_nulls,
            expand=expand,
        )
    ).parsed
