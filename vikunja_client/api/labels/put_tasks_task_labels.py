from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.models_label_task import ModelsLabelTask
from ...models.models_message import ModelsMessage
from ...models.web_http_error import WebHTTPError
from ...types import Response


def _get_kwargs(
    task: int,
    *,
    body: ModelsLabelTask,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/tasks/{task}/labels".format(
            task=quote(str(task), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ModelsLabelTask | ModelsMessage | WebHTTPError | None:
    if response.status_code == 201:
        response_201 = ModelsLabelTask.from_dict(response.json())

        return response_201

    if response.status_code == 400:
        response_400 = WebHTTPError.from_dict(response.json())

        return response_400

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
) -> Response[ModelsLabelTask | ModelsMessage | WebHTTPError]:
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
    body: ModelsLabelTask,
) -> Response[ModelsLabelTask | ModelsMessage | WebHTTPError]:
    """Add a label to a task

     Add a label to a task. The user needs to have write-access to the project to be able do this.

    Args:
        task (int):
        body (ModelsLabelTask):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ModelsLabelTask | ModelsMessage | WebHTTPError]
    """

    kwargs = _get_kwargs(
        task=task,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    task: int,
    *,
    client: AuthenticatedClient,
    body: ModelsLabelTask,
) -> ModelsLabelTask | ModelsMessage | WebHTTPError | None:
    """Add a label to a task

     Add a label to a task. The user needs to have write-access to the project to be able do this.

    Args:
        task (int):
        body (ModelsLabelTask):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ModelsLabelTask | ModelsMessage | WebHTTPError
    """

    return sync_detailed(
        task=task,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    task: int,
    *,
    client: AuthenticatedClient,
    body: ModelsLabelTask,
) -> Response[ModelsLabelTask | ModelsMessage | WebHTTPError]:
    """Add a label to a task

     Add a label to a task. The user needs to have write-access to the project to be able do this.

    Args:
        task (int):
        body (ModelsLabelTask):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ModelsLabelTask | ModelsMessage | WebHTTPError]
    """

    kwargs = _get_kwargs(
        task=task,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    task: int,
    *,
    client: AuthenticatedClient,
    body: ModelsLabelTask,
) -> ModelsLabelTask | ModelsMessage | WebHTTPError | None:
    """Add a label to a task

     Add a label to a task. The user needs to have write-access to the project to be able do this.

    Args:
        task (int):
        body (ModelsLabelTask):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ModelsLabelTask | ModelsMessage | WebHTTPError
    """

    return (
        await asyncio_detailed(
            task=task,
            client=client,
            body=body,
        )
    ).parsed
