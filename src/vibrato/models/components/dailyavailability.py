"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from typing import Optional
from vibrato import utils


class Day(str, Enum):
    MONDAY = 'Monday'
    TUESDAY = 'Tuesday'
    WEDNESDAY = 'Wednesday'
    THURSDAY = 'Thursday'
    FRIDAY = 'Friday'
    SATURDAY = 'Saturday'
    SUNDAY = 'Sunday'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class DailyAvailability:
    day: Optional[Day] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('day'), 'exclude': lambda f: f is None }})
    start_time: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('start_time'), 'exclude': lambda f: f is None }})
    end_time: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('end_time'), 'exclude': lambda f: f is None }})
    

