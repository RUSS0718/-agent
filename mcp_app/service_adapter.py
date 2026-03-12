
from rag_service.rag import RagService   
import  rag_service.config_data4rag as rag_config  # noqa: E402
from 离线知识库服务.knowledge_base import KnowledgeBaseService 
class MCPServiceAdapter:
    """只做一件事：把 MCP 请求转成现有业务函数调用。"""

    def __init__(self):
        self.rag_service = RagService()
        self.kb_service = KnowledgeBaseService()

    def ask_with_rag(self, question: str, session_id: str) -> dict:
        # 你后续可把 session_id 注入到 config.session_config 里
        # answer = self.rag_service.chain.invoke({"input": question})
        # config.session_config["session_id"] = session_id
        answer = self.rag_service.chain.invoke({"input": question},config=session_id )

        return {
            "ok": True,
            "answer": answer,
            "session_id": session_id,
        }

    def upload_knowledge_file(self, filename: str, content: str) -> dict:
        msg = self.kb_service.upload_by_str(content, filename)
        return {
            "ok": True,
            "message": msg,
        }