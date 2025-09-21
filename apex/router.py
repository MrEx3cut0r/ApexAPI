from typing import Callable

from starlette.applications import Starlette
from starlette.routing import Route

class ApexRouter():
    def __init__(self, prefix="") -> None:
        self.routes = []
        self.prefix = prefix

    def get(self, route: str) -> Callable:
        def decorator(func: Callable) -> None:
            self.routes.append(
                Route(
                    self.prefix+route,
                    endpoint=func,
                    methods=["GET"]
                )
            )
        return decorator

    def post(self, route: str) -> Callable:
        def decorator(func: Callable) -> None:
            self.routes.append(
                Route(
                    self.prefix+route,
                    endpoint=func,
                    methods=["POST"]
                )
            )
        return decorator
    
    def patch(self, route: str) -> Callable:
        def decorator(func: Callable) -> None:
            self.routes.append(
                Route(
                    self.prefix+route,
                    endpoint=func,
                    methods=["PATCH"]
                )
            )
        return decorator

    def put(self, route: str) -> Callable:
        def decorator(func: Callable) -> None:
            self.routes.append(
                Route(
                    self.prefix+route,
                    endpoint=func,
                    methods=["PUT"]
                )
            )
        return decorator

    def delete(self, route: str) -> Callable:
        def decorator(func: Callable) -> None:
            self.routes.append(
                Route(
                    self.prefix+route,
                    endpoint=func,
                    methods=["DELETE"]
                )
            )
        return decorator

    def head(self, route: str) -> Callable:
        def decorator(func: Callable) -> None:
            self.routes.append(
                Route(
                    self.prefix+route,
                    endpoint=func,
                    methods=["HEAD"]
                )
            )
        return decorator

    def options(self, route: str) -> Callable:
        def decorator(func: Callable) -> None:
            self.routes.append(
                Route(
                    self.prefix+route,
                    endpoint=func,
                    methods=["OPTIONS"]
                )
            )
        return decorator

    @classmethod
    def routes(self) -> list:
        return self.routes