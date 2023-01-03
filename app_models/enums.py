from enumfields import Enum


class PullRequestStatus(Enum):
    OPENED = 1
    CLOSED = 2
    DRAFT = 3
    MERGED = 4


class IssueStatus(Enum):
    TODO = 1
    IN_PROGRESS = 2
    IN_REVIEW = 3
    DONE = 4


class ReactionType(Enum):
    LIKE = 1
    DISLIKE = 2

class MilestoneState(Enum):
    OPEN = 1
    CLOSED = 2
    ALL = 3


class PullRequestActions(Enum):
    OPENED = 1,
    CLOSED = 2,
    APPROVED = 3,
