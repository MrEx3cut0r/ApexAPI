from starlette.applications import Starlette
from starlette.routing import Router
import uvicorn

from cli.main import cli
from router import ApexRouter

class Main():
    def __init__(self, host="localhost", port=8080) -> None:        
        self.routes = []
        self.host = host
        self.port = port

    def include_router(self, router: ApexRouter) -> None:
        for r in router.routers:
            self.routes.append(r)

    def run(self, debug=True, on_startup=None):
        app = Starlette(debug=debug, on_startup=on_startup, routes=self.routes)
        uvicorn.run(app, host=self.host, port=self.port)

if __name__=="__main__":
    cli()