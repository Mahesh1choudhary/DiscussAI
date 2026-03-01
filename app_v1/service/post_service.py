import asyncio
from autogen_agentchat.messages import TextMessage

from app_v1.agents.classification_agent import ClassificationAgent
from app_v1.database.database_manager import DatabaseManager
from app_v1.models.database_models.post_model import Post
from app_v1.repository.post_repository import PostRepository



class PostService:

    def __init__(self, database_manager: DatabaseManager):
        self.classification_agent = ClassificationAgent("classification_agent")
        self.database_manager = database_manager


    async def classify_post(self, post_id: int):
        """
        fetch post from db, classify and update the db
        """
        with self.database_manager.transaction() as session:
            post_repository = PostRepository(session)
            post: Post = post_repository.find_by_post_id(post_id)
            if post is None:
                #TODO: handle errors properly
                return ValueError(f"post with post_id :{post_id} not found")


            agent_response = await self.classification_agent.on_messages(
                messages=[TextMessage(content=post.post_link, source="system")],
                cancellation_token=None
            )

            data = agent_response.chat_message.content
            return data
