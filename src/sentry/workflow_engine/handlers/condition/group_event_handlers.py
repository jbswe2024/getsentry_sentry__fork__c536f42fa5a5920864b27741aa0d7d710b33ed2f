from typing import Any

from sentry.eventstore.models import GroupEvent
from sentry.workflow_engine.models.data_condition import Condition
from sentry.workflow_engine.registry import condition_handler_registry
from sentry.workflow_engine.types import DataConditionHandler


@condition_handler_registry.register(Condition.EVENT_CREATED_BY_DETECTOR)
class EventCreatedByDetectorConditionHandler(DataConditionHandler[GroupEvent]):
    @staticmethod
    def evaluate_value(event: GroupEvent, comparison: Any) -> bool:
        if event.occurrence is None or event.occurrence.evidence_data is None:
            return False

        return event.occurrence.evidence_data.get("detector_id", None) == comparison


@condition_handler_registry.register(Condition.EVENT_SEEN_COUNT)
class EventSeenCountConditionHandler(DataConditionHandler[GroupEvent]):
    @staticmethod
    def evaluate_value(event: GroupEvent, comparison: Any) -> bool:
        return event.group.times_seen == comparison
