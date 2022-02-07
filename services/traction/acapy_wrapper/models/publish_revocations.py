# coding: utf-8

from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, validator  # noqa: F401


class PublishRevocations(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    PublishRevocations - a model defined in OpenAPI

        rrid2crid: The rrid2crid of this PublishRevocations [Optional].
    """

    rrid2crid: Optional[Dict[str, List[str]]] = None


PublishRevocations.update_forward_refs()
