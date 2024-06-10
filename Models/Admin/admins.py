from sqladmin import ModelView

from Models.user import User
from database_initializer import  engine
from Models.tags import Tags, user_tags, post_tags, story_tags
from sqlalchemy import inspect
from Models.post import Post
from Models.story import Story
from Models.story_likes import Like
from Models.post_likes import PostLike
from Models.complaint_post import Complaint_post
from Models.complaints_user import Complaint_user
from Models.complaint_story import Complaint_story

from sqladmin import Admin

from main import app


admin = Admin(app, engine)


class UserAdmin(ModelView, model=User):
    column_list = [User.id, User.name]
    column_details_exclude_list = [User.hashed_password]
    can_delete = False


class PostAdmin(ModelView):
    model = Post
    column_list = [c_attr.key for c_attr in inspect(Post).mapper.column_attrs] + Post.owner


class StoryAdmin(ModelView):
    model = Story
    column_list = [c_attr.key for c_attr in inspect(Story).mapper.column_attrs] + Story.owner


class TagsAdmin(ModelView):
    model = Tags
    column_list = [c_attr.key for c_attr in inspect(Tags).mapper.column_attrs]


class UserTagsAdmin(ModelView):
    model = user_tags
    column_list = user_tags.columns.keys()


class PostTagsAdmin(ModelView):
    model = post_tags
    column_list = post_tags.columns.keys()


class StoryTagsAdmin(ModelView):
    model = story_tags
    column_list = story_tags.columns.keys()


class PostLikesAdmin(ModelView):
    model = PostLike
    column_list = [c_attr.key for c_attr in inspect(PostLike).mapper.column_attrs]


class StoryLikesAdmin(ModelView):
    model = Like
    column_list = [c_attr.key for c_attr in inspect(Like).mapper.column_attrs]


class ComplaintPostAdmin(ModelView):
    model = Complaint_post
    column_list = [c_attr.key for c_attr in inspect(Complaint_post).mapper.column_attrs]


class ComplaintUserAdmin(ModelView):
    model = Complaint_user
    column_list = [c_attr.key for c_attr in inspect(Complaint_user).mapper.column_attrs]


class ComplaintStoryAdmin(ModelView):
    model = Complaint_story
    column_list = [c_attr.key for c_attr in inspect(Complaint_story).mapper.column_attrs]


admin.add_view(ComplaintUserAdmin)
admin.add_view(ComplaintStoryAdmin)
admin.add_view(ComplaintPostAdmin)
admin.add_view(UserAdmin)
admin.add_view(PostAdmin)
admin.add_view(StoryAdmin)
admin.add_view(TagsAdmin)
admin.add_view(UserTagsAdmin)
admin.add_view(PostTagsAdmin)
admin.add_view(StoryTagsAdmin)
admin.add_view(StoryLikesAdmin)
admin.add_view(PostLikesAdmin)
