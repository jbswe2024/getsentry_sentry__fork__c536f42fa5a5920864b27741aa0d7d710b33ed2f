from typing import TypedDict

from sentry.api.serializers import Serializer, register
from sentry.utils.avatar import get_gravatar_url
from sentry.utils.eventuser import EventUser


class EventUserSerializerResponse(TypedDict):
    id: str | None
    tagValue: str
    identifier: str
    username: str
    email: str
    name: str
    ipAddress: str
    avatarUrl: str
    hash: str
    dateCreated: None


@register(EventUser)
class EventUserSerializer(Serializer):
    def serialize(self, obj, attrs, user, **kwargs) -> EventUserSerializerResponse:
        return {
            "id": str(obj.id) if obj.id is not None else obj.id,
            "tagValue": obj.tag_value,
            "identifier": obj.user_ident,
            "username": obj.username,
            "email": obj.email,
            "name": obj.get_display_name(),
            "ipAddress": obj.ip_address,
            "avatarUrl": get_gravatar_url(obj.email, size=32),
            # Legacy fields from `EventUser` model
            "hash": obj.hash,
            "dateCreated": None,
        }
