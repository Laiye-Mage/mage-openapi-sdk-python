# -*- coding:utf-8 -*-
'''
Author: Astral
Date: 2021-10-21 16:15:06
LastEditTime: 2021-10-26 13:33:12
LastEditors: Astral
'''
import os
import json
import time
import base64
import random
import string
import hashlib
import requests


class Mage():
    def __init__(self, endpoint="https://mage.uibot.com.cn"):
        self.endpoint = endpoint

    def generate_header(self, api_auth_pubkey, app_auth_secretkey):
        prefix = "Value Exception"
        if api_auth_pubkey == "":
            raise Exception(
                "{0}, the api_auth_pubkey must not be empty".format(prefix))
        if app_auth_secretkey == "":
            raise Exception(
                "{0}, the app_auth_secret_key must not be empty".format(prefix))
        prefix = "Type Exception"
        if not isinstance(api_auth_pubkey, str):
            raise Exception(
                "{0}, the type of api_auth_pubkey must be string".format(prefix))
        if not isinstance(app_auth_secretkey, str):
            raise Exception(
                "{0}, the type of app_auth_secretkey must be string".format(prefix))
        api_auth_timestamp = str(int(time.time()))
        api_auth_nounce = "".join(random.sample(
            string.ascii_letters + string.digits, 10))
        header_dict = dict()
        header_dict["Api-Auth-nonce"] = api_auth_nounce
        header_dict["Api-Auth-pubkey"] = api_auth_pubkey
        header_dict["Api-Auth-timestamp"] = api_auth_timestamp
        header_dict["Content-Type"] = "application/json"
        token_name = hashlib.sha1()
        token_key = api_auth_nounce + api_auth_timestamp+app_auth_secretkey
        token_name.update(token_key.encode("utf-8"))
        header_dict["Api-Auth-sign"] = token_name.hexdigest()
        return header_dict

    def file_encode(self, file_path_or_base64):
        if os.path.isfile(file_path_or_base64):
            with open(file_path_or_base64, "rb") as f:
                img_base64 = str(base64.b64encode(f.read()), encoding='utf-8')
        else:
            img_base64 = file_path_or_base64
        return img_base64

    def single_image_without_params(self, api_auth_pubkey, app_auth_secretkey, type, img_path_or_base64):
        url = "{}/v1/mage/ocr/{}".format(self.endpoint, type)
        req_data = {
            "img_base64": self.file_encode(img_path_or_base64)
        }
        resp = requests.post(url, data=json.dumps(
            req_data), headers=self.generate_header(api_auth_pubkey, app_auth_secretkey))
        return resp.status_code, json.loads(resp.content)

    def ocr_verification(self, api_auth_pubkey, app_auth_secretkey, img_path_or_base64, verification_format=0):
        """
        https://mage.uibot.com.cn/docs/latest/docUnderstanding/backend/api.html#operation/OcrService_OcrVerification
        """
        url = "{}/v1/document/ocr/verification".format(self.endpoint)
        req_data = {
            "format": verification_format,
            "img_base64": self.file_encode(img_path_or_base64)
        }
        print(json.dumps(req_data))
        resp = requests.post(url, data=json.dumps(
            req_data), headers=self.generate_header(api_auth_pubkey, app_auth_secretkey))
        print(resp.status_code)
        print(resp.content)
        return resp.status_code, json.loads(resp.content)

    def ocr_license(self, api_auth_pubkey, app_auth_secretkey, img_path_or_base64):
        """
        https://mage.uibot.com.cn/docs/latest/docUnderstanding/backend/api.html#operation/OcrService_OcrLicenseNew
        """
        return self.single_image_without_params(api_auth_pubkey, app_auth_secretkey, "license", img_path_or_base64)

    def ocr_stamp(self, api_auth_pubkey, app_auth_secretkey, img_path_or_base64):
        """
        https://mage.uibot.com.cn/docs/latest/docUnderstanding/backend/api.html#operation/OcrService_OcrStamp
        """
        return self.single_image_without_params(api_auth_pubkey, app_auth_secretkey, "stamp", img_path_or_base64)

    def ocr_bills(self, api_auth_pubkey, app_auth_secretkey, img_path_or_base64):
        """
        https://mage.uibot.com.cn/docs/latest/docUnderstanding/backend/api.html#operation/OcrService_OcrBillsNew
        """
        return self.single_image_without_params(api_auth_pubkey, app_auth_secretkey, "bills", img_path_or_base64)

    def ocr_table(self, api_auth_pubkey, app_auth_secretkey, img_path_or_base64):
        """
        https://mage.uibot.com.cn/docs/latest/docUnderstanding/backend/api.html#operation/OcrService_OcrTableNew
        """
        url = "{}/v1/mage/ocr/table".format(self.endpoint)
        req_data = {
            "img_base64": [self.file_encode(img_path_or_base64)]
        }
        resp = requests.post(url, data=json.dumps(
            req_data), headers=self.generate_header(api_auth_pubkey, app_auth_secretkey))
        return resp.status_code, json.loads(resp.content)

    def ocr_template(self, api_auth_pubkey, app_auth_secretkey, img_path_or_base64, with_struct_info=True, with_raw_info=True):
        """
        https://mage.uibot.com.cn/docs/latest/docUnderstanding/backend/api.html#operation/OcrService_OcrTemplateRecognize
        """
        url = "{}/v1/document/ocr/template".format(self.endpoint)
        req_data = {
            "with_struct_info": with_struct_info,
            "with_raw_info": with_raw_info,
            "img_base64": self.file_encode(img_path_or_base64)
        }
        resp = requests.post(url, data=json.dumps(
            req_data), headers=self.generate_header(api_auth_pubkey, app_auth_secretkey))
        return resp.status_code, json.loads(resp.content)

    def ocr_general(self, api_auth_pubkey, app_auth_secretkey, img_path_or_base64, with_struct_info=True, with_char_info=True):
        """
        https://mage.uibot.com.cn/docs/latest/docUnderstanding/backend/api.html#operation/OcrService_OcrGeneralNew
        """
        url = "{}/v1/mage/ocr/general".format(self.endpoint)
        req_data = {
            "with_struct_info": with_struct_info,
            "with_char_info": with_char_info,
            "img_base64": [
                self.file_encode(img_path_or_base64)
            ]
        }
        resp = requests.post(url, data=json.dumps(
            req_data), headers=self.generate_header(api_auth_pubkey, app_auth_secretkey))
        return resp.status_code, json.loads(resp.content)

    def nlp_docextract_create(self, api_auth_pubkey, app_auth_secretkey, file_path_or_base64):
        """
        https://mage.uibot.com.cn/docs/latest/docUnderstanding/backend/api.html#operation/AIService_DocExtract
        """
        url = "{}/v1/mage/nlp/docextract/create".format(self.endpoint)
        req_data = {
            "file_base64": self.file_encode(file_path_or_base64)
        }
        resp = requests.post(url, data=json.dumps(
            req_data), headers=self.generate_header(api_auth_pubkey, app_auth_secretkey))
        return resp.status_code, json.loads(resp.content)

    def nlp_docextract_query(self, api_auth_pubkey, app_auth_secretkey, task_id):
        """
        https://mage.uibot.com.cn/docs/latest/docUnderstanding/backend/api.html#operation/AIService_QueryDocExtract
        """
        url = "{}/v1/mage/nlp/docextract/query".format(self.endpoint)
        req_data = {
            "task_id": task_id
        }
        resp = requests.post(url, data=json.dumps(
            req_data), headers=self.generate_header(api_auth_pubkey, app_auth_secretkey))
        return resp.status_code, json.loads(resp.content)

    def nlp_geoextract(self, api_auth_pubkey, app_auth_secretkey, text):
        """
        https://mage.uibot.com.cn/docs/latest/docUnderstanding/backend/api.html#operation/AIService_GEOExtract
        """
        url = "{}/v1/mage/nlp/geoextract".format(self.endpoint)
        req_data = {
            "text": text
        }
        resp = requests.post(url, data=json.dumps(
            req_data), headers=self.generate_header(api_auth_pubkey, app_auth_secretkey))
        return resp.status_code, json.loads(resp.content)

    def nlp_document_classify(self, api_auth_pubkey, app_auth_secretkey, text):
        """
        https://mage.uibot.com.cn/docs/latest/docUnderstanding/backend/api.html#operation/ClassifierService_Classify
        """
        url = "{}/v1/document/classify".format(self.endpoint)
        req_data = {
            "doc": text
        }
        resp = requests.post(url, data=json.dumps(
            req_data), headers=self.generate_header(api_auth_pubkey, app_auth_secretkey))
        return resp.status_code, json.loads(resp.content)

    def nlp_textmatch(self, api_auth_pubkey, app_auth_secretkey, text):
        """
        https://mage.uibot.com.cn/docs/latest/docUnderstanding/backend/api.html#operation/AIService_TextMatch
        """
        url = "{}/v1/mage/nlp/textmatch".format(self.endpoint)
        req_data = {
            "doc": text
        }
        resp = requests.post(url, data=json.dumps(
            req_data), headers=self.generate_header(api_auth_pubkey, app_auth_secretkey))
        return resp.status_code, json.loads(resp.content)

    def nlp_document_extract(self, api_auth_pubkey, app_auth_secretkey, text):
        """
        https://mage.uibot.com.cn/docs/latest/docUnderstanding/backend/api.html#operation/ExtractorService_Extract
        """
        url = "{}/v1/document/extract".format(self.endpoint)
        req_data = {
            "doc": text
        }
        resp = requests.post(url, data=json.dumps(
            req_data), headers=self.generate_header(api_auth_pubkey, app_auth_secretkey))
        return resp.status_code, json.loads(resp.content)

    def solution_contract_compare(self, api_auth_pubkey, app_auth_secretkey, file_compare_path_or_base64, file_base_path_or_base64, file_compare_name, file_base_name):
        """
        https://mage.uibot.com.cn/docs/latest/docUnderstanding/backend/api.html#operation/ContractCompareService_ContractCompare
        """
        url = "{}/v1/mage/solution/contract/compare".format(self.endpoint)
        req_data = {
            "file_compare": self.file_encode(file_compare_path_or_base64),
            "file_base": self.file_encode(file_base_path_or_base64),
            "file_compare_name": file_compare_name,
            "file_base_name": file_base_name
        }
        resp = requests.post(url, data=json.dumps(
            req_data), headers=self.generate_header(api_auth_pubkey, app_auth_secretkey))
        return resp.status_code, json.loads(resp.content)

    def solution_contract_detail(self, api_auth_pubkey, app_auth_secretkey, task_id):
        """
        https://mage.uibot.com.cn/docs/latest/docUnderstanding/backend/api.html#operation/ContractCompareService_GetContractCompareResultDetail
        """
        url = "{}/v1/mage/solution/contract/detail".format(self.endpoint)
        req_data = {
            "task_id": task_id
        }
        resp = requests.post(url, data=json.dumps(
            req_data), headers=self.generate_header(api_auth_pubkey, app_auth_secretkey))
        return resp.status_code, json.loads(resp.content)

    def solution_contract_files(self, api_auth_pubkey, app_auth_secretkey, task_id):
        """
        https://mage.uibot.com.cn/docs/latest/docUnderstanding/backend/api.html#operation/ContractCompareService_GetCompareResultFiles
        """
        url = "{}/v1/mage/solution/contract/files".format(self.endpoint)
        req_data = {
            "task_id": task_id
        }
        resp = requests.post(url, data=json.dumps(
            req_data), headers=self.generate_header(api_auth_pubkey, app_auth_secretkey))
        return resp.status_code, json.loads(resp.content)

    def idp_flow_task_create(self, api_auth_pubkey, app_auth_secretkey, file_path_or_base64, name):
        """
        https://mage.uibot.com.cn/docs/latest/docUnderstanding/backend/api.html#operation/IDPService_CreateIdpTask
        """
        url = "{}/v1/mage/idp/flow/task/create".format(self.endpoint)
        req_data = {
            "file": {
                "base64": self.file_encode(file_path_or_base64),
                "name": name
            }
        }
        resp = requests.post(url, data=json.dumps(
            req_data), headers=self.generate_header(api_auth_pubkey, app_auth_secretkey))
        return resp.status_code, json.loads(resp.content)


    def idp_flow_task_query(self, api_auth_pubkey, app_auth_secretkey, task_id, with_ocr_general=True):
        """
        https://mage.uibot.com.cn/docs/latest/docUnderstanding/backend/api.html#operation/IDPService_GetIDPTaskDetail
        """
        url = "{}/v1/mage/idp/flow/task/query".format(self.endpoint)
        req_data = {
            "with_ocr_general": with_ocr_general,
            "task_id": task_id
        }
        resp = requests.post(url, data=json.dumps(
            req_data), headers=self.generate_header(api_auth_pubkey, app_auth_secretkey))
        return resp.status_code, json.loads(resp.content)

