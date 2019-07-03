from aiohttp import web

async def handle(request):
    return web.Response(text="Hello!")

app = web.Application()
app.add_routes([web.get('/', handle)])

web.run_app(app)
