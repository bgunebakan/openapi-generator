# coding: utf-8

"""
    OpenAPI Petstore

    This spec is mainly for testing Petstore server and contains fake endpoints, models. Please do not use this for any other purpose. Special characters: \" \\

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self

class Order(BaseModel):
    """
    Order
    """ # noqa: E501
    id: Optional[StrictInt] = None
    pet_id: Optional[StrictInt] = Field(default=None, alias="petId")
    quantity: Optional[StrictInt] = None
    ship_date: Optional[datetime] = Field(default=None, alias="shipDate")
    status: Optional[StrictStr] = Field(default=None, description="Order Status")
    complete: Optional[StrictBool] = False
    __properties: ClassVar[List[str]] = ["id", "petId", "quantity", "shipDate", "status", "complete"]

    @field_validator('status')
    def status_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['placed', 'approved', 'delivered']):
            raise ValueError("must be one of enum values ('placed', 'approved', 'delivered')")
        return value

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        excluded_fields: Set[str] = set([
        ])
        return self.model_dump_json(by_alias=True, exclude_unset=True, exclude=excluded_fields)

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of Order from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of Order from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "petId": obj.get("petId"),
            "quantity": obj.get("quantity"),
            "shipDate": obj.get("shipDate"),
            "status": obj.get("status"),
            "complete": obj.get("complete") if obj.get("complete") is not None else False
        })
        return _obj


