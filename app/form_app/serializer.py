from enum import Enum

from core.models import ApplicationIModel
from form_filling import AppInstructions
from rest_framework import serializers


class AppInstructionSerializer(serializers.ModelSerializer):
    appointment_duration = serializers.ChoiceField(choices=ApplicationIModel.appt_choice)
    double_booking = serializers.ChoiceField(choices=ApplicationIModel.double_booking_choice)
    p_new_appt = serializers.ChoiceField(choices=ApplicationIModel.check_box)
    p_denied = serializers.ChoiceField(choices=ApplicationIModel.check_box)
    p_cancelled = serializers.ChoiceField(choices=ApplicationIModel.check_box)
    p_confirmed = serializers.ChoiceField(choices=ApplicationIModel.check_box)
    p_time_change = serializers.ChoiceField(choices=ApplicationIModel.check_box)
    p_reminder = serializers.ChoiceField(choices=ApplicationIModel.check_box)
    access_instruction = serializers.ChoiceField(choices=ApplicationIModel.access_choices)
    is_alaram = serializers.ChoiceField(choices=ApplicationIModel.alaram_choice)
    turn_off_lights = serializers.ChoiceField(choices=ApplicationIModel.check_box)
    remove_shoes = serializers.ChoiceField(choices=ApplicationIModel.check_box)
    leave_card = serializers.ChoiceField(choices=ApplicationIModel.check_box)
    lock_doors = serializers.ChoiceField(choices=ApplicationIModel.check_box)
    call_if_late = serializers.ChoiceField(choices=ApplicationIModel.check_box)
    knock_first = serializers.ChoiceField(choices=ApplicationIModel.check_box)
    bring_reco_lic = serializers.ChoiceField(choices=ApplicationIModel.check_box)
    contact_1_notify_email = serializers.ChoiceField(choices=ApplicationIModel.check_box)
    contact_1_notify_text = serializers.ChoiceField(choices=ApplicationIModel.check_box)
    contact_1_notify_call = serializers.ChoiceField(choices=ApplicationIModel.check_box)
    contact_1_canconfirm = serializers.ChoiceField(choices=ApplicationIModel.check_box)
    contact_1_candenied = serializers.ChoiceField(choices=ApplicationIModel.check_box)
    contact_1_appt = serializers.ChoiceField(choices=ApplicationIModel.check_box)
    contact_1_denied = serializers.ChoiceField(choices=ApplicationIModel.check_box)
    contact_1_cancelled = serializers.ChoiceField(choices=ApplicationIModel.check_box)
    contact_1_confirmed = serializers.ChoiceField(choices=ApplicationIModel.check_box)
    contact_1_timechange = serializers.ChoiceField(choices=ApplicationIModel.check_box)
    contact_1_reminder = serializers.ChoiceField(choices=ApplicationIModel.check_box)

    contact_2_notify_email = serializers.ChoiceField(choices=ApplicationIModel.check_box)
    contact_2_notify_text = serializers.ChoiceField(choices=ApplicationIModel.check_box)
    contact_2_notify_call = serializers.ChoiceField(choices=ApplicationIModel.check_box)
    contact_2_canconfirm = serializers.ChoiceField(choices=ApplicationIModel.check_box)
    contact_2_candenied = serializers.ChoiceField(choices=ApplicationIModel.check_box)
    contact_2_appt = serializers.ChoiceField(choices=ApplicationIModel.check_box)
    contact_2_denied = serializers.ChoiceField(choices=ApplicationIModel.check_box)
    contact_2_cancelled = serializers.ChoiceField(choices=ApplicationIModel.check_box)
    contact_2_confirmed = serializers.ChoiceField(choices=ApplicationIModel.check_box)
    contact_2_timechange = serializers.ChoiceField(choices=ApplicationIModel.check_box)
    contact_2_reminder = serializers.ChoiceField(choices=ApplicationIModel.check_box)

    def __init__(self, *args, **kwargs):
        super(AppInstructionSerializer, self).__init__(*args, **kwargs)
        self.app = AppInstructions()

    class Meta:
        model = ApplicationIModel
        fields = [
            'mls_number',
            'property_name',
            'agent_name',
            'min_notice',
            'double_booking',
            'appointment_duration',
            'p_new_appt',
            'p_denied',
            'p_cancelled',
            'p_confirmed',
            'p_time_change',
            'p_reminder',
            'instructions',
            'access_instruction',
            'lbx_instruct',
            'is_alaram',
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
        ]


class ReferenceEnumfield(serializers.ChoiceField):
    def __init__(self, enum_type, **kwargs):
        if not issubclass(enum_type, str):
            raise TypeError
        if not issubclass(enum_type, Enum):
            raise TypeError("enum_type should be an Enum")
        self.enum_name = enum_type.__name__
        super().__init__(choices=[enum.name for enum in enum_type], **kwargs)
