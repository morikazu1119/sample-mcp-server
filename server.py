from mcp.server.fastmcp import FastMCP
import uvicorn

mcp = FastMCP("recommendation-game-mcp")

@mcp.tool()
def recommend_game(request):
    return "おすすめはオセロです。"

def main():
    uvicorn.run(
        mcp.streamable_http_app,
        host="0.0.0.0",
        port=8765,
    )

if __name__ == "__main__":
    main()