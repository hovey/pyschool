

class Command:
    """
    Command line commands in json format used by Factory to generate objects
    """
    def __init__(self, guid_command, **kwargs):

        self._guid = guid_command
        self._kwargs = kwargs
        a = 4
    

    @property
    def guid(self):
        """
        Returns:
            The globally unique identification (guid) of a command instance.

        Raises:
            To be determined.  
        """
        return self._guid
