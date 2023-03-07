from dataclasses import dataclass
from typing import Tuple, List


@dataclass
class Resume:
    first_name: str | None
    last_name: str | None
    middle_name: str | None
    phone: str | None
    email: str | None
    education: List[Tuple[str, str]]
    experience: List[Tuple[str, str]]
