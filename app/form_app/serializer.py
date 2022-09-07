from enum import Enum

from core.models import ApplicationInstruction, Form120
from form_filling import AppInstructions
from rest_framework import serializers


class AppInstructionSerializer(serializers.ModelSerializer):

    def __init__(self, *args, **kwargs):
        super(AppInstructionSerializer, self).__init__(*args, **kwargs)

    class Meta:
        model = ApplicationInstruction
        fields = [
            'id',
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


