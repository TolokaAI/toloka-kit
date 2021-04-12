from enum import Enum
from typing import Any, Dict, Optional

from .primitives.base import BaseTolokaObject


class AnalyticsRequest(BaseTolokaObject):
    """Base class for all analytics requests in Toloka

    How to use this requests and get some useful information see in example in "TolokaClient.get_analytics".

    Attributes:
        subject_id: ID of the object you want to get analytics about.
    """

    class Subject(Enum):
        ...

    def __repr__(self): ...

    def __str__(self): ...

    def __eq__(self, other): ...

    def __ne__(self, other): ...

    def __lt__(self, other): ...

    def __le__(self, other): ...

    def __gt__(self, other): ...

    def __ge__(self, other): ...

    def __init__(self, *, subject_id: str) -> None: ...

    _unexpected: Optional[Dict[str, Any]]
    subject_id: str

class PoolAnalyticsRequest(AnalyticsRequest):
    """Base class for all analytics requests about pools

    Right now you can get analytics only about pool.
    """

    class Subject(Enum):
        ...

    def __repr__(self): ...

    def __str__(self): ...

    def __eq__(self, other): ...

    def __ne__(self, other): ...

    def __lt__(self, other): ...

    def __le__(self, other): ...

    def __gt__(self, other): ...

    def __ge__(self, other): ...

    def __init__(self, *, subject_id: str) -> None: ...

    _unexpected: Optional[Dict[str, Any]]
    subject_id: str

class RealTasksCountPoolAnalytics(PoolAnalyticsRequest):
    """The number of tasks in the pool

    It does not take into account the overlap, how many tasks will be on one page, or the presence of golden tasks.
    """

    def __repr__(self): ...

    def __str__(self): ...

    def __eq__(self, other): ...

    def __ne__(self, other): ...

    def __lt__(self, other): ...

    def __le__(self, other): ...

    def __gt__(self, other): ...

    def __ge__(self, other): ...

    def __init__(self, *, subject_id: str) -> None: ...

    _unexpected: Optional[Dict[str, Any]]
    subject_id: str

class SubmitedAssignmentsCountPoolAnalytics(PoolAnalyticsRequest):
    """Number of assignments in the "submited" status in the pool

    Do not confuse it with the approved status.
    "Submited" status means that the task was completed by the performer and send for review.
    "Approved" status means that the task has passed review and money has been paid for it.
    """

    def __repr__(self): ...

    def __str__(self): ...

    def __eq__(self, other): ...

    def __ne__(self, other): ...

    def __lt__(self, other): ...

    def __le__(self, other): ...

    def __gt__(self, other): ...

    def __ge__(self, other): ...

    def __init__(self, *, subject_id: str) -> None: ...

    _unexpected: Optional[Dict[str, Any]]
    subject_id: str

class SkippedAssignmentsCountPoolAnalytics(PoolAnalyticsRequest):
    """Number of assignments in the "skipped" status in the pool
    """

    def __repr__(self): ...

    def __str__(self): ...

    def __eq__(self, other): ...

    def __ne__(self, other): ...

    def __lt__(self, other): ...

    def __le__(self, other): ...

    def __gt__(self, other): ...

    def __ge__(self, other): ...

    def __init__(self, *, subject_id: str) -> None: ...

    _unexpected: Optional[Dict[str, Any]]
    subject_id: str

class RejectedAssignmentsCountPoolAnalytics(PoolAnalyticsRequest):
    """Number of assignments in the "rejected" status in the pool
    """

    def __repr__(self): ...

    def __str__(self): ...

    def __eq__(self, other): ...

    def __ne__(self, other): ...

    def __lt__(self, other): ...

    def __le__(self, other): ...

    def __gt__(self, other): ...

    def __ge__(self, other): ...

    def __init__(self, *, subject_id: str) -> None: ...

    _unexpected: Optional[Dict[str, Any]]
    subject_id: str

class ApprovedAssignmentsCountPoolAnalytics(PoolAnalyticsRequest):
    """Number of assignments in the "approved" status in the pool

    Do not confuse it with the submited status.
    "Submited" status means that the task was completed by the performer and send for review.
    "Approved" status means that the task has passed review and money has been paid for it.
    """

    def __repr__(self): ...

    def __str__(self): ...

    def __eq__(self, other): ...

    def __ne__(self, other): ...

    def __lt__(self, other): ...

    def __le__(self, other): ...

    def __gt__(self, other): ...

    def __ge__(self, other): ...

    def __init__(self, *, subject_id: str) -> None: ...

    _unexpected: Optional[Dict[str, Any]]
    subject_id: str

class CompletionPercentagePoolAnalytics(PoolAnalyticsRequest):
    """Approximate percentage of completed tasks in the pool
    """

    def __repr__(self): ...

    def __str__(self): ...

    def __eq__(self, other): ...

    def __ne__(self, other): ...

    def __lt__(self, other): ...

    def __le__(self, other): ...

    def __gt__(self, other): ...

    def __ge__(self, other): ...

    def __init__(self, *, subject_id: str) -> None: ...

    _unexpected: Optional[Dict[str, Any]]
    subject_id: str

class AvgSubmitAssignmentMillisPoolAnalytics(PoolAnalyticsRequest):
    """Average time to complete one task page in milliseconds
    """

    def __repr__(self): ...

    def __str__(self): ...

    def __eq__(self, other): ...

    def __ne__(self, other): ...

    def __lt__(self, other): ...

    def __le__(self, other): ...

    def __gt__(self, other): ...

    def __ge__(self, other): ...

    def __init__(self, *, subject_id: str) -> None: ...

    _unexpected: Optional[Dict[str, Any]]
    subject_id: str

class SpentBudgetPoolAnalytics(PoolAnalyticsRequest):
    """How much money has already been spent on this pool, excluding fee
    """

    def __repr__(self): ...

    def __str__(self): ...

    def __eq__(self, other): ...

    def __ne__(self, other): ...

    def __lt__(self, other): ...

    def __le__(self, other): ...

    def __gt__(self, other): ...

    def __ge__(self, other): ...

    def __init__(self, *, subject_id: str) -> None: ...

    _unexpected: Optional[Dict[str, Any]]
    subject_id: str

class UniqueWorkersCountPoolAnalytics(PoolAnalyticsRequest):
    """The number of unique performers who took tasks from the pool
    """

    def __repr__(self): ...

    def __str__(self): ...

    def __eq__(self, other): ...

    def __ne__(self, other): ...

    def __lt__(self, other): ...

    def __le__(self, other): ...

    def __gt__(self, other): ...

    def __ge__(self, other): ...

    def __init__(self, *, subject_id: str) -> None: ...

    _unexpected: Optional[Dict[str, Any]]
    subject_id: str

class UniqueSubmittersCountPoolAnalytics(PoolAnalyticsRequest):
    """The number of unique performers who have submitted to the pool
    """

    def __repr__(self): ...

    def __str__(self): ...

    def __eq__(self, other): ...

    def __ne__(self, other): ...

    def __lt__(self, other): ...

    def __le__(self, other): ...

    def __gt__(self, other): ...

    def __ge__(self, other): ...

    def __init__(self, *, subject_id: str) -> None: ...

    _unexpected: Optional[Dict[str, Any]]
    subject_id: str

class ActiveWorkersByFilterCountPoolAnalytics(PoolAnalyticsRequest):
    """The number of active performers matching the pool filters for the last hours

    Attributes:
        interval_hours: The number of hours to take into account when collecting statistics.
    """

    def __repr__(self): ...

    def __str__(self): ...

    def __eq__(self, other): ...

    def __ne__(self, other): ...

    def __lt__(self, other): ...

    def __le__(self, other): ...

    def __gt__(self, other): ...

    def __ge__(self, other): ...

    def __init__(self, *, subject_id: str, interval_hours: int) -> None: ...

    _unexpected: Optional[Dict[str, Any]]
    subject_id: str
    interval_hours: int

class EstimatedAssignmentsCountPoolAnalytics(PoolAnalyticsRequest):
    """The approximate number of responses to task pages.
    """

    def __repr__(self): ...

    def __str__(self): ...

    def __eq__(self, other): ...

    def __ne__(self, other): ...

    def __lt__(self, other): ...

    def __le__(self, other): ...

    def __gt__(self, other): ...

    def __ge__(self, other): ...

    def __init__(self, *, subject_id: str) -> None: ...

    _unexpected: Optional[Dict[str, Any]]
    subject_id: str
