import asyncio
from typing import AsyncGenerator, Generator

import pytest
from async_asgi_testclient import TestClient

from app.main import app


@pytest.fixture
async def client() -> AsyncGenerator[TestClient, None]:
    host, port = "127.0.0.1", "8000"
    scope = {"client": (host, port)}

    async with TestClient(app, scope=scope) as client:
        yield client


@pytest.fixture(scope="session")
def event_loop() -> Generator[asyncio.AbstractEventLoop, None, None]:
    loop = asyncio.get_event_loop_policy().new_event_loop()
    yield loop
    loop.close()
