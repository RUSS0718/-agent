
from service_adapter import MCPServiceAdapter
from fastmcp import FastMCP
adapter = MCPServiceAdapter()

mcp = FastMCP("dataanalysis-agent")

@mcp.tool("ask_with_rag")
def tool_ask_with_rag(payload: dict) -> dict:
    question = payload.get("question", "").strip()
    session_id = payload.get("session_id", "default")
    if not question:
        return {"ok": False, "error": "question 不能为空"}
    return adapter.ask_with_rag(question=question, session_id=session_id)


@mcp.tool("upload_knowledge_file")
def tool_upload_knowledge_file(payload: dict) -> dict:
    filename = payload.get("filename", "unknown.txt")
    content = payload.get("content", "")
    if not content:
        return {"ok": False, "error": "content 不能为空"}
    return adapter.upload_knowledge_file(filename=filename, content=content)



if __name__ == '__main__':
    mcp.run()