# coding: utf-8

from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, validator  # noqa: F401


class TAAAcceptance(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    TAAAcceptance - a model defined in OpenAPI

        mechanism: The mechanism of this TAAAcceptance [Optional].
        time: The time of this TAAAcceptance [Optional].
    """

    mechanism: Optional[str] = None
    time: Optional[int] = None

    @validator("time")
    def time_max(cls, value):
        assert value <= -1
        return value

    @validator("time")
    def time_min(cls, value):
        assert value >= 0
        return value


TAAAcceptance.update_forward_refs()
