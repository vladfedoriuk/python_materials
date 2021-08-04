from wtforms_alchemy import ModelForm
from flasksqlalchemy_ex.tceh.models import User, Post
from wtforms.validators import Length


class UserForm(ModelForm):
    class Meta:
        model = User


def length(min=5):
    return Length(min=5, message="Title's too small")


class PostForm(ModelForm):
    class Meta:
        model = Post
        include = ["user_id"]
        field_args = {"title": {"validators": [length(min=5)]}}
