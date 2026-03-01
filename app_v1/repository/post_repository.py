from sqlalchemy.orm import Session
from typing import Optional

from app_v1.models.database_models.post_model import Post

class PostRepository():
    def __init__(self, database_session: Session):
        self.database_session = database_session

    def find_by_post_id(self, post_id:int) -> Optional[Post]:
        post:Optional[Post] = self.database_session.query(Post).filter(Post.post_id == post_id).first()
        return post

    def save_post(self, post:Post):
        self.database_session.add(post)