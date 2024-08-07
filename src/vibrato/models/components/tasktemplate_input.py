"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from .tasktemplateproperty import TaskTemplateProperty
from dataclasses_json import Undefined, dataclass_json
from typing import List, Optional
from vibrato import utils


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class TaskTemplateInput:
    UNSET='__SPEAKEASY_UNSET__'
    task_name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('task_name'), 'exclude': lambda f: f is None }})
    task_description: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('task_description'), 'exclude': lambda f: f is None }})
    task_instructions: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('task_instructions'), 'exclude': lambda f: f is None }})
    task_properties: Optional[List[TaskTemplateProperty]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('task_properties'), 'exclude': lambda f: f is None }})
    recipient_name: Optional[str] = dataclasses.field(default=UNSET, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('recipient_name'), 'exclude': lambda f: f is TaskTemplateInput.UNSET }})
    recipient_phone_number: Optional[str] = dataclasses.field(default=UNSET, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('recipient_phone_number'), 'exclude': lambda f: f is TaskTemplateInput.UNSET }})
    recipient_country_code: Optional[str] = dataclasses.field(default=UNSET, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('recipient_country_code'), 'exclude': lambda f: f is TaskTemplateInput.UNSET }})
    call_locale: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('call_locale'), 'exclude': lambda f: f is None }})
    public: Optional[bool] = dataclasses.field(default=False, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('public'), 'exclude': lambda f: f is None }})
    featured: Optional[bool] = dataclasses.field(default=False, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('featured'), 'exclude': lambda f: f is None }})
    tags: Optional[List[str]] = dataclasses.field(default=UNSET, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('tags'), 'exclude': lambda f: f is TaskTemplateInput.UNSET }})
    iconoir_icon: Optional[str] = dataclasses.field(default=UNSET, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('iconoir_icon'), 'exclude': lambda f: f is TaskTemplateInput.UNSET }})
    

