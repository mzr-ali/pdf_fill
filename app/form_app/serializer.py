from core.models import (Form810, ProcedureAgreement, Form120, ApplicationInstruction, AuthorizationRequest,
                         Form248, CheckList,ExceptionList,Form244)
from rest_framework import serializers


class AppInstructionSerializer(serializers.ModelSerializer):

    def __init__(self, *args, **kwargs):
        super(AppInstructionSerializer, self).__init__(*args, **kwargs)

    class Meta:
        model = ApplicationInstruction
        fields = [
            'mls_number',
            'property_name',
            'agent_name',
            'min_notice',
            'double_booking',
            'appointment_duration',
            'admin_instruction',
            'property_new_appointment',
            'property_denied',
            'property_cancelled',
            'property_confirmed',
            'property_time_change',
            'property_reminder',
            'lbx_located',
            'lbx_code',
            'restrict_time',
            'access_instruction',
            'is_alarm',
            'alaram_code',
            'showing_agent_info',
            'turn_off_lights',
            'remove_shoes',
            'leave_card',
            'lock_doors',
            'call_if_late',
            'knock_first',
            'bring_reco_lic',
            'contact_1_name',
            'contact_1_areacode',
            'contact_1_phone1',
            'contact_1_phone2',
            'contact_1_email',
            'contact_1_notify_email',
            'contact_1_notify_text',
            'contact_1_notify_call',
            'contact_1_canconfirm',
            'contact_1_candenied',
            'contact_1_appt',
            'contact_1_denied',
            'contact_1_cancelled',
            'contact_1_confirmed',
            'contact_1_timechange',
            'contact_1_reminder',
            'contact_2_name',
            'contact_2_areacode',
            'contact_2_phone1',
            'contact_2_phone2',
            'contact_2_email',
            'contact_2_notify_email',
            'contact_2_notify_text',
            'contact_2_notify_call',
            'contact_2_canconfirm',
            'contact_2_candenied',
            'contact_2_appt',
            'contact_2_denied',
            'contact_2_cancelled',
            'contact_2_confirmed',
            'contact_2_timechange',
            'contact_2_reminder',
            'property_name_2',
            'agent_name_2',
            'when_offers_accept',
            'date',
            'time',
            'premetive_offers',
            'minimum_irrevocable',
            'how_long',
            'notify_in_person',
            'at_location',
            'notify_by_email',
            'to_email',
            'notify_by_fax',
            'to_fax',
            'other_method',
            'other_method_text',
            'other_offer_details',
            'notification',
            'additional_information',

        ]
        read_only_fields = ['id']


class Form120Serializer(serializers.ModelSerializer):

    def __init__(self, *args, **kwargs):
        super(Form120Serializer, self).__init__(*args, **kwargs)

    class Meta:
        model = Form120
        fields = [
            'id',
            'buyer_one',
            'buyer_one_street',
            'buyer_one_phone',
            'buyer_two',
            'buyer_two_street',
            'seller_one',
            'seller_one_street',
            'seller_one_phone',
            'seller_two',
            'seller_two_street',
            'prop_offer_date',
            'prop_street_no',
            'prop_street',
            'prop_unit_no',
            'prop_city',
            'prop_state',
            'prop_zipcode',
            'irrevocable_person',
            'irrevocable_time',
            'irrevocable_date',
            'acceptance_time',
            'acceptance_date',
            'seller_phone_number',
            'seller_lawyer_name',
            'seller_lawyer_address',
            'seller_lawyer_email',
            'seller_lawyer_phone',
            'seller_lawyer_fax',
            'buyer_lawyer_name',
            'buyer_lawyer_address',
            'buyer_lawyer_email',
            'buyer_lawyer_phone',
            'buyer_lawyer_fax',

        ]
        read_only_fields = ['id']


class ProcedureAgreementSerializer(serializers.ModelSerializer):

    def __init__(self, *args, **kwargs):
        super(ProcedureAgreementSerializer, self).__init__(*args, **kwargs)

    class Meta:
        model = ProcedureAgreement
        fields = [
            'property_address',
            'client_name',
            'seller_1_name',
            'seller_1_date',
            'seller_2_name',
            'seller_2_date',
            'broker_name',
            'broker_date',

        ]


class Form810Serializer(serializers.ModelSerializer):

    def __init__(self, *args, **kwargs):
        super(Form810Serializer, self).__init__(*args, **kwargs)

    class Meta:
        model = Form810
        fields = [
            'acknowledgement',
            'broker_1',
            'broker_2',

        ]


class AuthRequestSerializer(serializers.ModelSerializer):

    def __init__(self, *args, **kwargs):
        super(AuthRequestSerializer, self).__init__(*args, **kwargs)

    class Meta:
        model = AuthorizationRequest
        fields = [
            'property_address',
            'name',
            'offer_until',

        ]


class Form248Serializer(serializers.ModelSerializer):

    def __init__(self, *args, **kwargs):
        super(Form248Serializer, self).__init__(*args, **kwargs)

    class Meta:
        model = Form248
        fields = [
            'seller_1',
            'seller_2',
            'buyer_1',
            'buyer_2',
            'street_number',
            'street',
            'unit_number',
            'city',
            'state',
            'zip_code',
            'broker',
            'purpose_1',
            'entry_access_1',
            'purpose_2',
            'entry_access_2',
            'purpose_3',
            'entry_access_3',
            'tenent_ack',
            'additional_terms',

        ]


class CheckListSerializer(serializers.ModelSerializer):

    def __init__(self, *args, **kwargs):
        super(CheckListSerializer, self).__init__(*args, **kwargs)

    class Meta:
        model = CheckList
        fields = [
            'property_address',
            'mls_num',
            'ar_mls_num',
            'already_loaded_no',
            'already_loaded_yes',
            'already_loaded',
            'board_yes',
            'board_no',
            's_data_sheet',
            's_listing_agreement',
            's_working_with_realtor',
            'mortgage_verification',
            'fintrac',
            'property_facts',
            's_appt_instruc',
            's_process_to_seller',
            's_mls_depart',
            's_power_of_attorney',
            's_property_officer',
            's_property_tenant_ack',
            's_speak_design',
            's_privacy_act',
            's_auth_forms',
            'except_listing_agreement',
            'proceedure_agreement',
            'l_data_sheet',
            'l_listing_agreement',
            'l_working_with_realtor',
            'l_appt_instruc',
            'l_process_to_seller',
            'l_mls_depart',
            'l_power_of_attorney',
            'l_property_officer',
            'l_property_tenant_ack',
            'l_speak_design',
            'l_privacy_act',
            'l_auth_forms',

        ]


class ExceptionListSerializer(serializers.ModelSerializer):

    def __init__(self, *args, **kwargs):
        super(ExceptionListSerializer, self).__init__(*args, **kwargs)

    class Meta:
        model = ExceptionList
        fields = [
            'commission'
        ]
class Form244Serializer(serializers.ModelSerializer):

    def __init__(self, *args, **kwargs):
        super(Form244Serializer, self).__init__(*args, **kwargs)

    class Meta:
        model = Form244
        fields = [
            'street_number',
            'street',
            'unit_num',
            'city',
            'state',
            'zip_code',
            'seller_1',
            'seller_2',
            'broker',
            'broker_id',
            'msl_number',
            'interboaard_mls',
            'board',
            'list_date',
            'time_limit',
            'offer_time',
            'present_date',
            'other_dir',
            'other_dir1',
            'other_dir2',
            'other_dir3',
            'disclaimer',
        ]
