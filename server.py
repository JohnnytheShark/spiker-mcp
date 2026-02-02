import asyncio
import logging
from pathlib import Path
from mcp.server import Server
from mcp.server.sse import SseServerTransport
from mcp.server.lowlevel import NotificationOptions
from mcp.server.models import InitializationOptions
import mcp.types as types
from starlette.applications import Starlette
from starlette.routing import Mount, Route
from starlette.responses import Response
import uvicorn

# Configure logging to stdout
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("spiker-mcp")

# 1. Initialize the S.P.I.K.E.R. Core Server
app_server = Server("SPIKER-Sensei")

# Define the Analysis Tool
@app_server.list_tools()
async def handle_list_tools() -> list[types.Tool]:
    logger.info("Listing tools...")
    return [
        types.Tool(
            name="analyze_spiker",
            description="Audit code via S.P.I.K.E.R. methodology.",
            inputSchema={
                "type": "object",
                "properties": {
                    "code": {"type": "string"},
                    "context": {"type": "string"}
                }
            }
        )
    ]

# Handle Tool Execution
@app_server.call_tool()
async def handle_call_tool(name: str, arguments: dict | None) -> list[types.TextContent | types.ImageContent | types.EmbeddedResource]:
    # Security/Hygiene: Log the call, but truncate arguments to avoid leaking secrets or flooding logs
    safe_args = str(arguments)
    if len(safe_args) > 500:
        safe_args = safe_args[:500] + "... (truncated)"
    
    logger.info(f"Tool called: {name} with arguments: {safe_args}")
    if name == "analyze_spiker":
        args = arguments or {}
        code = args.get("code", "")
        context = args.get("context", "")
        
        # The S.P.I.K.E.R. Logic Spike
        # We return a prompt that guides the LLM to apply the methodology.
        return [
            types.TextContent(
                type="text",
                text=f"""
Act as a S.P.I.K.E.R. Methodology Consultant. Evaluate the provided codebase against the six S.P.I.K.E.R. pillars.

CONTEXT:
{context}

CODE TO ANALYZE:
{code}

ANALYSIS FRAMEWORK:
1. [S]pike (Intent): Identify 'Systemic Ambiguity'. Is the intent clear?
2. [P]urge (Hygiene): Identify 'Sanguineous Logic' (dead code, redundancy).
3. [I]solate (Isolation): Check for 'Nerve Propagation' (side effects, coupling).
4. [K]inetic (Purity): Check for 'Tap Water Bloat' (unnecessary dependencies).
5. [E]nzymatic (Aging): Check for 'Rot-prone Design' (extensibility, docs).
6. [R]efine (Refinement): Suggest 'Rigorous Refinement' (testing strategies).

Format output as an ADR (Architecture Decision Record) and organize supporting docs via Diataxis where applicable.
"""
            )
        ]
    
    raise ValueError(f"Unknown tool: {name}")

# 3. Define Resources (The Manifesto)
@app_server.list_resources()
async def handle_list_resources() -> list[types.Resource]:
    logger.info("Listing resources...")
    return [
        types.Resource(
            uri="spiker://docs",
            name="S.P.I.K.E.R. Methodology",
            description="The full philosophical specification.",
            mimeType="text/markdown"
        )
    ]

@app_server.read_resource()
async def handle_read_resource(uri: str) -> list[types.TextResourceContents | types.BlobResourceContents]:
    logger.info(f"Reading resource: {uri}")
    if uri == "spiker://docs":
        # Read the sibling markdown file safely
        file_path = Path(__file__).parent / "SPIKE_METHODOLOGY.md"
        if not file_path.exists():
            raise ValueError("Methodology file not found.")
            
        return [
            types.TextResourceContent(
                uri=uri,
                mimeType="text/markdown",
                text=file_path.read_text()
            )
        ]
    
    raise ValueError(f"Unknown resource: {uri}")

# 4. SSE Transport Setup
sse = SseServerTransport("/messages/")

async def handle_sse(request):
    async with sse.connect_sse(request.scope, request.receive, request._send) as (read_stream, write_stream):
        await app_server.run(
            read_stream,
            write_stream,
            InitializationOptions(
                server_name="SPIKER-Sensei",
                server_version="0.1.0",
                capabilities=app_server.get_capabilities(
                    notification_options=NotificationOptions(),
                    experimental_capabilities={},
                ),
            ),
        )
    return Response()

# 3. Starlette Web Routing
starlette_app = Starlette(
    routes=[
        Route("/sse", endpoint=handle_sse, methods=["GET"]),
        Mount("/messages/", app=sse.handle_post_message),
    ]
)

if __name__ == "__main__":
    uvicorn.run(starlette_app, host="0.0.0.0", port=8000)