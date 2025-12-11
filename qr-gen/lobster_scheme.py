from dataclasses import dataclass

from parsy import regex, string

scheme_prefix = string("lobsterfile://")
resource_path = string("/") >> regex(r".*")
LobsterURLParser = (scheme_prefix >> resource_path).map(
    lambda path: LobsterURL(filepath=path)
)

BASE_PATH = "recordings"


@dataclass
class LobsterURL:
    filepath: str


def parse(url: str) -> LobsterURL | None:
    """Parse a Lobster Scheme URL and return the corresponding YouTube URL."""
    try:
        return LobsterURLParser.optional().parse(url)
    except Exception:
        return None
