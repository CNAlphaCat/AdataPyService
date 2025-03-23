from pydantic import BaseModel
from typing import Any, Union

class AdataPyServiceResponseModel(BaseModel):
    status_code: int
    content: Union[dict, list, str, int, float, bool, None, Any]