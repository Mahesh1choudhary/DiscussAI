from pydantic import BaseModel
from app_v1.commons.post_enums import PostType


class ClassificationResponse(BaseModel):
    post_type: PostType
    company_name: str
    designation: str