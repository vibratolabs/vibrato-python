"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import dateutil.parser
from .tasktemplateproperty import TaskTemplateProperty
from dataclasses_json import Undefined, dataclass_json
from datetime import datetime
from typing import List, Optional
from vibrato import utils


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class TaskTemplate:
    UNSET='__SPEAKEASY_UNSET__'
    uuid: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('uuid'), 'exclude': lambda f: f is None }})
    created_at: Optional[datetime] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('created_at'), 'encoder': utils.datetimeisoformat(True), 'decoder': dateutil.parser.isoparse, 'exclude': lambda f: f is None }})
    updated_at: Optional[datetime] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('updated_at'), 'encoder': utils.datetimeisoformat(True), 'decoder': dateutil.parser.isoparse, 'exclude': lambda f: f is None }})
    task_name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('task_name'), 'exclude': lambda f: f is None }})
    task_description: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('task_description'), 'exclude': lambda f: f is None }})
    task_instructions: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('task_instructions'), 'exclude': lambda f: f is None }})
    task_properties: Optional[List[TaskTemplateProperty]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('task_properties'), 'exclude': lambda f: f is None }})
    recipient_name: Optional[str] = dataclasses.field(default=UNSET, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('recipient_name'), 'exclude': lambda f: f is TaskTemplate.UNSET }})
    recipient_phone_number: Optional[str] = dataclasses.field(default=UNSET, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('recipient_phone_number'), 'exclude': lambda f: f is TaskTemplate.UNSET }})
    recipient_country_code: Optional[str] = dataclasses.field(default=UNSET, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('recipient_country_code'), 'exclude': lambda f: f is TaskTemplate.UNSET }})
    call_locale: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('call_locale'), 'exclude': lambda f: f is None }})
    public: Optional[bool] = dataclasses.field(default=False, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('public'), 'exclude': lambda f: f is None }})
    featured: Optional[bool] = dataclasses.field(default=False, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('featured'), 'exclude': lambda f: f is None }})
    tags: Optional[List[str]] = dataclasses.field(default=UNSET, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('tags'), 'exclude': lambda f: f is TaskTemplate.UNSET }})
    iconoir_icon: Optional[str] = dataclasses.field(default=UNSET, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('iconoir_icon'), 'exclude': lambda f: f is TaskTemplate.UNSET }})
    

