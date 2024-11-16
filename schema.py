#!/usr/bin/env python
# -*- coding: utf-8 -*-

from typing import Optional, List, Dict, Any
from pydantic import BaseModel, Field


class InferenceInput(BaseModel):
    """
    Input values for model inference
    """
    text: str = Field(..., example='hello, my name is onemt.', title='a sentence at a time')
    source_language: str = Field(..., example='eng', title='language of given text, in 3 character language code, i.e eng for English')
    target_language: str = Field(..., example='hin', title='language of text in which translation needs to be happen, in 3 character language code, i.e hin for Hindi')

class InputItem(BaseModel):
    source: str = Field(..., description="Source text for translation")

class OutputItem(BaseModel):
    source: str = Field(..., description="Source text for translation")
    target: str = Field(..., description="Source text for translation")


class LanguageConfig(BaseModel):
    sourceLanguage: str = Field(..., description="Source language code")
    targetLanguage: str = Field(..., description="Target language code")

class Config(BaseModel):
    modelId: int = Field(..., description="ID of the translation model")
    language: LanguageConfig = Field(..., description="Language configuration")

class InferenceInputUCLA(BaseModel):
    input: List[InputItem] = Field(..., description="List of input items for translation")
    config: Config = Field(..., description="Configuration for translation request")

class InferenceOutputUCLA(BaseModel):
    output: List[OutputItem] = Field(..., description="List of input items for translation")
    config: Config = Field(..., description="Configuration for translation request")




class InferenceResult(BaseModel):
    """
    Inference result from the model
    """

    data: str = Field(..., example='hello, my name is onemt.', title='a translated sentence')
    languages: str = Field(..., example='eng:hin', title='language pair')
    version: str = Field(..., example='IIITHV0.0.0.3', title='model version')


class InferenceResponse(BaseModel):
    """
    Output response for model inference
    """
    error: bool = Field(..., example=False, title='Whether there is error')
    data: str = Field(..., example='hello, my name is onemt.', title='a translated sentence')
    languages: str = Field(..., example='eng:hin', title='language pair')
    version: str = Field(..., example='IIITHV0.0.0.3', title='model version')


class ErrorResponse(BaseModel):
    """
    Error response for the API
    """
    error: bool = Field(..., example=True, title='Whether there is error')
    message: str = Field(..., example='', title='Error message')
    traceback: str = Field(None, example='', title='Detailed traceback of the error')
