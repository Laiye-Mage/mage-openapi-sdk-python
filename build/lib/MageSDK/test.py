# -*- coding:utf-8 -*-
'''
Author: Astral
Date: 2021-10-22 09:51:22
LastEditTime: 2021-10-27 10:40:16
LastEditors: Astral
Description: 
'''
from mage import Mage


if __name__ == '__main__':
    mage = Mage()
    # =======================================================
    # https://mage.uibot.com.cn/docs/latest/docUnderstanding/backend/api.html#operation/OcrService_OcrVerification
    # --------------------------------------------------
    api_auth_pubkey = ""
    app_auth_secretkey = ""
    img_path = ""
    status_code, result = mage.ocr_verification(api_auth_pubkey, app_auth_secretkey, img_path_or_base64=img_path, verification_format=0)
    # =======================================================
    # https://mage.uibot.com.cn/docs/latest/docUnderstanding/backend/api.html#operation/OcrService_OcrLicenseNew
    # --------------------------------------------------
    api_auth_pubkey = ""
    app_auth_secretkey = ""
    img_path = ""
    status_code, result = mage.ocr_license(api_auth_pubkey, app_auth_secretkey, img_path_or_base64=img_path)
    # =======================================================
    # https://mage.uibot.com.cn/docs/latest/docUnderstanding/backend/api.html#operation/OcrService_OcrStamp
    # --------------------------------------------------
    api_auth_pubkey = ""
    app_auth_secretkey = ""
    img_path = ""
    status_code, result = mage.ocr_stamp(api_auth_pubkey, app_auth_secretkey, img_path_or_base64=img_path)
    # =======================================================
    # https://mage.uibot.com.cn/docs/latest/docUnderstanding/backend/api.html#operation/OcrService_OcrBillsNew
    # --------------------------------------------------
    api_auth_pubkey = ""
    app_auth_secretkey = ""
    img_path = ""
    status_code, result = mage.ocr_bills(api_auth_pubkey, app_auth_secretkey, img_path_or_base64=img_path)
    # =======================================================
    # https://mage.uibot.com.cn/docs/latest/docUnderstanding/backend/api.html#operation/OcrService_OcrTableNew
    # --------------------------------------------------
    api_auth_pubkey = ""
    app_auth_secretkey = ""
    img_path = ""
    status_code, result = mage.ocr_table(api_auth_pubkey, app_auth_secretkey, img_path_or_base64=img_path)
    # =======================================================
    # https://mage.uibot.com.cn/docs/latest/docUnderstanding/backend/api.html#operation/OcrService_OcrTemplateRecognize
    # --------------------------------------------------
    api_auth_pubkey = ""
    app_auth_secretkey = ""
    img_path = ""
    status_code, result = mage.ocr_template(api_auth_pubkey, app_auth_secretkey, img_path_or_base64=img_path, with_struct_info=True, with_raw_info=True)
    # =======================================================
    # https://mage.uibot.com.cn/docs/latest/docUnderstanding/backend/api.html#operation/OcrService_OcrGeneralNew
    # --------------------------------------------------
    api_auth_pubkey = ""
    app_auth_secretkey = ""
    img_path = ""
    status_code, result = mage.ocr_general(api_auth_pubkey, app_auth_secretkey, img_path_or_base64=img_path, with_struct_info=True, with_char_info=True)
    # =======================================================
    # https://mage.uibot.com.cn/docs/latest/docUnderstanding/backend/api.html#operation/AIService_DocExtract
    # --------------------------------------------------
    api_auth_pubkey = ""
    app_auth_secretkey = ""
    file_path_or_base64 = ""
    status_code, result = mage.nlp_docextract_create(api_auth_pubkey, app_auth_secretkey, file_path_or_base64)
    # =======================================================
    # https://mage.uibot.com.cn/docs/latest/docUnderstanding/backend/api.html#operation/AIService_QueryDocExtract
    # --------------------------------------------------
    api_auth_pubkey = ""
    app_auth_secretkey = ""
    task_id = ""
    status_code, result = mage.nlp_docextract_query(api_auth_pubkey, app_auth_secretkey, task_id)
    # =======================================================
    # https://mage.uibot.com.cn/docs/latest/docUnderstanding/backend/api.html#operation/AIService_GEOExtract
    # --------------------------------------------------
    api_auth_pubkey = ""
    app_auth_secretkey = ""
    text = ""
    status_code, result = mage.nlp_geoextract(api_auth_pubkey, app_auth_secretkey, text)
    # =======================================================
    # https://mage.uibot.com.cn/docs/latest/docUnderstanding/backend/api.html#operation/ClassifierService_Classify
    # --------------------------------------------------
    api_auth_pubkey = ""
    app_auth_secretkey = ""
    text = ""
    status_code, result = mage.nlp_document_classify(api_auth_pubkey, app_auth_secretkey, text)
    # =======================================================
    # https://mage.uibot.com.cn/docs/latest/docUnderstanding/backend/api.html#operation/AIService_TextMatch
    # --------------------------------------------------
    api_auth_pubkey = ""
    app_auth_secretkey = ""
    text = ""
    status_code, result = mage.nlp_textmatch(api_auth_pubkey, app_auth_secretkey, text)
    # =======================================================
    # https://mage.uibot.com.cn/docs/latest/docUnderstanding/backend/api.html#operation/ExtractorService_Extract
    # --------------------------------------------------
    api_auth_pubkey = ""
    app_auth_secretkey = ""
    text = ""
    status_code, result = mage.nlp_document_extract(api_auth_pubkey, app_auth_secretkey, text)
    # =======================================================
    # https://mage.uibot.com.cn/docs/latest/docUnderstanding/backend/api.html#operation/ContractCompareService_ContractCompare
    # --------------------------------------------------
    api_auth_pubkey = ""
    app_auth_secretkey = ""
    file_compare_path_or_base64 = ""
    file_base_path_or_base64 = ""
    file_compare_name = ""
    file_base_name = ""
    status_code, result = mage.solution_contract_compare(api_auth_pubkey, app_auth_secretkey, file_compare_path_or_base64, file_base_path_or_base64, file_compare_name, file_base_name)
    # =======================================================
    # https://mage.uibot.com.cn/docs/latest/docUnderstanding/backend/api.html#operation/ContractCompareService_GetContractCompareResultDetail
    # --------------------------------------------------
    api_auth_pubkey = ""
    app_auth_secretkey = ""
    task_id = ""
    status_code, result = mage.solution_contract_detail(api_auth_pubkey, app_auth_secretkey, task_id)
    # =======================================================
    # https://mage.uibot.com.cn/docs/latest/docUnderstanding/backend/api.html#operation/ContractCompareService_GetCompareResultFiles
    # --------------------------------------------------
    api_auth_pubkey = ""
    app_auth_secretkey = ""
    task_id = ""
    status_code, result = mage.solution_contract_files(api_auth_pubkey, app_auth_secretkey, task_id)
    # =======================================================
    # https://mage.uibot.com.cn/docs/latest/docUnderstanding/backend/api.html#operation/ContractCompareService_ContractCompare
    # --------------------------------------------------
    api_auth_pubkey = ""
    app_auth_secretkey = ""
    name = ""
    status_code, result = mage.idp_flow_task_create(api_auth_pubkey, app_auth_secretkey, file_path_or_base64, name)
    # =======================================================
    # https://mage.uibot.com.cn/docs/latest/docUnderstanding/backend/api.html#operation/IDPService_GetIDPTaskDetail
    # --------------------------------------------------
    api_auth_pubkey = ""
    app_auth_secretkey = ""
    task_id = ""
    status_code, result = mage.idp_flow_task_query(api_auth_pubkey, app_auth_secretkey, task_id, with_ocr_general=True)