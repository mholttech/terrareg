

class TerraregError(Exception):
    """Base terrareg exception."""

    pass


class UnknownFiletypeError(TerraregError):
    """Uploaded filetype is unknown."""

    pass


class NoModuleVersionAvailableError(TerraregError):
    """No version of this module available."""

    pass


class InvalidTerraregMetadataFileError(TerraregError):
    """Error whilst reading terrareg metadata file."""

    pass


class DatabaseMustBeIniistalisedError(TerraregError):
    """Database object must be initialised before accessing tables."""

    pass


class MetadataDoesNotContainRequiredAttributeError(TerraregError):
    """Module metadata does not contain required metadata attribute."""

    pass


class UploadError(TerraregError):
    """Error with file upload."""

    pass