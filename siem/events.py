"""Script used for the event class, variables and functions"""

class EventCategory:
    """base class for event categories, not to be used on its own
    """
    name: str
    desc: dict
    
    def __init__(self, level: int) -> None:
        """initialise the event category

        Args:
            level (int): initial severity score
        """
        self.level = level
    
    def __str__(self) -> str:
        """converts event to string

        Returns:
            str: formatted as event category: event, desc_key: desc,...
        """
        return ", ".join(f"{key}: {item}" for key, item in self.desc.items())

class Error:
    """base/general class for events that are also an error, not necessarily an exception
    """
    name = "error: error"
    desc = {"error": "error"}
    
    def __init__(self, msg, **kw) -> None:
        self.msg = msg
        self.desc += {"msg": msg, **kw}

class AuthEvent(EventCategory):
    """Used for Authentication based events

    Inherits:
        EventCategory (class): Base class for event categories
    """
    name = "authentication event"
    desc = {"authentication event": "authentication event"}
    
    def __init__(self, level: int, **kw) -> None:
        """create an authentication event

        Args:
            level (int): level of severity
            kw (**Any): informative fields
        """
        super().__init__(level)
        self.desc += kw
        
class FailedAuth(AuthEvent):
    """Used for when an Authentication attempt fails

    Inherits:
        AuthEvent: class for authentication based events
    """
    name = AuthEvent.name + ": failed authentication"
    desc = {"authentication event": "failed authentication"}

class SuccessfulAuth(AuthEvent):
    """Used for when an Authentication attempt succeeds

    Inherits:
        AuthEvent: class for authentication based events
    """
    name = AuthEvent.name + ": successful authentication"
    desc = {"authentication event": "failed authentication"}

class AuthenticationError(AuthEvent, Error):
    name = AuthEvent.name + ": authentication error"
    desc = {"authentication event": "authentication error"}