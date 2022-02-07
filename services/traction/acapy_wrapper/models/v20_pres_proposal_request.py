# coding: utf-8

from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, validator  # noqa: F401
from acapy_wrapper.models.v20_pres_proposal_by_format import V20PresProposalByFormat


class V20PresProposalRequest(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    V20PresProposalRequest - a model defined in OpenAPI

        auto_present: The auto_present of this V20PresProposalRequest [Optional].
        comment: The comment of this V20PresProposalRequest [Optional].
        connection_id: The connection_id of this V20PresProposalRequest.
        presentation_proposal: The presentation_proposal of this V20PresProposalRequest.
        trace: The trace of this V20PresProposalRequest [Optional].
    """

    auto_present: Optional[bool] = None
    comment: Optional[str] = None
    connection_id: str
    presentation_proposal: V20PresProposalByFormat
    trace: Optional[bool] = None


V20PresProposalRequest.update_forward_refs()
