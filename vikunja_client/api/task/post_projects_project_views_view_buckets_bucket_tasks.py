from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.models_message import ModelsMessage
from ...models.models_task_bucket import ModelsTaskBucket
from ...models.web_http_error import WebHTTPError
from ...types import Response


def _get_kwargs(
    project: int,
    view: int,
    bucket: int,
    *,
    body: ModelsTaskBucket,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/projects/{project}/views/{view}/buckets/{bucket}/tasks".format(
            project=quote(str(project), safe=""),
            view=quote(str(view), safe=""),
            bucket=quote(str(bucket), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ModelsMessage | ModelsTaskBucket | WebHTTPError | None:
    if response.status_code == 200:
        response_200 = ModelsTaskBucket.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = WebHTTPError.from_dict(response.json())

        return response_400

    if response.status_code == 500:
        response_500 = ModelsMessage.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[ModelsMessage | ModelsTaskBucket | WebHTTPError]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    project: int,
    view: int,
    bucket: int,
    *,
    client: AuthenticatedClient,
    body: ModelsTaskBucket,
) -> Response[ModelsMessage | ModelsTaskBucket | WebHTTPError]:
    """Update a task bucket

     Updates a task in a bucket

    Args:
        project (int):
        view (int):
        bucket (int):
        body (ModelsTaskBucket):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ModelsMessage | ModelsTaskBucket | WebHTTPError]
    """

    kwargs = _get_kwargs(
        project=project,
        view=view,
        bucket=bucket,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    project: int,
    view: int,
    bucket: int,
    *,
    client: AuthenticatedClient,
    body: ModelsTaskBucket,
) -> ModelsMessage | ModelsTaskBucket | WebHTTPError | None:
    """Update a task bucket

     Updates a task in a bucket

    Args:
        project (int):
        view (int):
        bucket (int):
        body (ModelsTaskBucket):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ModelsMessage | ModelsTaskBucket | WebHTTPError
    """

    return sync_detailed(
        project=project,
        view=view,
        bucket=bucket,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    project: int,
    view: int,
    bucket: int,
    *,
    client: AuthenticatedClient,
    body: ModelsTaskBucket,
) -> Response[ModelsMessage | ModelsTaskBucket | WebHTTPError]:
    """Update a task bucket

     Updates a task in a bucket

    Args:
        project (int):
        view (int):
        bucket (int):
        body (ModelsTaskBucket):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ModelsMessage | ModelsTaskBucket | WebHTTPError]
    """

    kwargs = _get_kwargs(
        project=project,
        view=view,
        bucket=bucket,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    project: int,
    view: int,
    bucket: int,
    *,
    client: AuthenticatedClient,
    body: ModelsTaskBucket,
) -> ModelsMessage | ModelsTaskBucket | WebHTTPError | None:
    """Update a task bucket

     Updates a task in a bucket

    Args:
        project (int):
        view (int):
        bucket (int):
        body (ModelsTaskBucket):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ModelsMessage | ModelsTaskBucket | WebHTTPError
    """

    return (
        await asyncio_detailed(
            project=project,
            view=view,
            bucket=bucket,
            client=client,
            body=body,
        )
    ).parsed
