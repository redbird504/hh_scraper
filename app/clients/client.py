import httpx


class Client:
    def __init__(self, headers: dict = None) -> None:
        self._headers: dict = headers

    async def get(self, url: str, **request_params) -> httpx.Response:
        return await self._request("GET", url, **request_params)

    async def post(self, url: str, **request_params) -> httpx.Response:
        return await self._request("POST", url, **request_params)

    async def _request(self, method: str, url: str, **request_params) -> httpx.Response:
        async with httpx.AsyncClient() as client:
            request_params = {
                "headers": self._headers,
                **request_params
                }
            response = await client.request(method, url, **request_params)
            response.raise_for_status()
            return response
