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

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self

class SecondCircularAllOfRef(BaseModel):
    """
    SecondCircularAllOfRef
    """ # noqa: E501
    name: Optional[StrictStr] = Field(default=None, alias="_name")
    circular_all_of_ref: Optional[List[CircularAllOfRef]] = Field(default=None, alias="circularAllOfRef")
    __properties: ClassVar[List[str]] = ["_name", "circularAllOfRef"]

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
        """Create an instance of SecondCircularAllOfRef from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in circular_all_of_ref (list)
        _items = []
        if self.circular_all_of_ref:
            for _item_circular_all_of_ref in self.circular_all_of_ref:
                if _item_circular_all_of_ref:
                    _items.append(_item_circular_all_of_ref.to_dict())
            _dict['circularAllOfRef'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of SecondCircularAllOfRef from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "_name": obj.get("_name"),
            "circularAllOfRef": [CircularAllOfRef.from_dict(_item) for _item in obj["circularAllOfRef"]] if obj.get("circularAllOfRef") is not None else None
        })
        return _obj

from petstore_api.models.circular_all_of_ref import CircularAllOfRef
# TODO: Rewrite to not use raise_errors
SecondCircularAllOfRef.model_rebuild(raise_errors=False)

