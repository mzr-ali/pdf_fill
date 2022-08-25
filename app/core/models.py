from django.db import models  # noqa


class Form200(models.Model):
    broker_name = models.CharField(max_length=200)
    broker_street = models.CharField(max_length=200)
    broker_city = models.CharField(max_length=200)
    broker_state = models.CharField(max_length=200)
    broker_zip = models.CharField(max_length=200)
    broker_phone = models.CharField(max_length=200)
    broker_details = models.CharField(max_length=250)
    seller1_name = models.CharField(max_length=200)
    seller1_phone = models.CharField(max_length=200)
    seller2_name = models.CharField(max_length=200)
    seller2_phone = models.CharField(max_length=200)
    spouse_phone = models.CharField(max_length=200)
    list_date = models.CharField(max_length=200)
    expire_date = models.CharField(max_length=200)
    ack_date = models.CharField(max_length=200)
    list_price = models.CharField(max_length=200)
    list_price_in_word = models.CharField(max_length=200)
    commission_percent = models.CharField(max_length=200)
    commission_amount = models.CharField(max_length=200)
    coop_commission_per = models.CharField(max_length=200)
    coop_commission_amount = models.CharField(max_length=200)
    holdover_day = models.CharField(max_length=200)

    txtp_street = models.CharField(max_length=200)
    txtp_unitNumber = models.CharField(max_length=200)
    txtp_city = models.CharField(max_length=200)
    txtp_state = models.CharField(max_length=200)
    txtp_zipcode = models.CharField(max_length=200)


class ApplicationIModel(models.Model):
    access_choices = [
        ('door code', 'door code'),
        ('go direct', 'go direct'),
        ('key', 'key'),
        ('sentrilock', 'sentrilock'),
        ('lock box', 'lock box')
    ]
    check_box = [
        ('On', 1),
        ('Off', 0)
    ]
    alaram_choice = [('Yes', 'YES_2'), ('No', 'NO_2')]
    double_booking_choice = [('Yes', 'YES'), ('No', 'NO')]
    appt_choice = [('1 hour', '1 hour'), ('1/2 Hour', '1/2 Hour'), ('15 minutes', '15 minutes')]
    mls_number = models.CharField(max_length=255)
    property_name = models.CharField(max_length=255)
    agent_name = models.CharField(max_length=255)

    # Appointment Instructions
    min_notice = models.SmallIntegerField()
    double_booking = models.CharField(max_length=255, choices=double_booking_choice)
    appointment_duration = models.CharField(max_length=255, choices=appt_choice)

    # Page me regarding
    p_new_appt = models.SmallIntegerField(choices=check_box, default=0)
    p_denied = models.SmallIntegerField(choices=check_box, default=0)
    p_cancelled = models.SmallIntegerField(choices=check_box, default=0)
    p_confirmed = models.SmallIntegerField(choices=check_box, default=0)
    p_time_change = models.SmallIntegerField(choices=check_box, default=0)
    p_reminder = models.SmallIntegerField(choices=check_box, default=0)

    # special_instrctions
    instructions = models.TextField(max_length=500,
                                    help_text='Are there any restricted times / days / special instructions?')
    access_instruction = models.CharField(max_length=125, choices=access_choices, default='key')
    lbx_instruct = models.TextField(max_length=500,
                                    help_text='Where is the LBX located? / Any other access instructions?')
    is_alaram = models.CharField(choices=alaram_choice, max_length=255)
    alaram_code = models.CharField(max_length=255)

    turn_off_lights = models.SmallIntegerField(choices=check_box, default=1)
    remove_shoes = models.SmallIntegerField(choices=check_box, default=0)
    leave_card = models.SmallIntegerField(choices=check_box, default=1)
    lock_doors = models.SmallIntegerField(choices=check_box, default=0)
    call_if_late = models.SmallIntegerField(choices=check_box, default=1)
    knock_first = models.SmallIntegerField(choices=check_box, default=0)
    bring_reco_lic = models.SmallIntegerField(choices=check_box, default=1)

    contact_1_name = models.CharField(max_length=255)
    contact_1_areacode = models.IntegerField()
    contact_1_phone1 = models.IntegerField()
    contact_1_phone2 = models.IntegerField()
    contact_1_email = models.EmailField()
    contact_1_notify_email = models.SmallIntegerField(choices=check_box, default=1)
    contact_1_notify_text = models.SmallIntegerField(choices=check_box, default=1)
    contact_1_notify_call = models.SmallIntegerField(choices=check_box, default=1)
    contact_1_canconfirm = models.SmallIntegerField(choices=check_box, default=1)
    contact_1_candenied = models.SmallIntegerField(choices=check_box, default=1)

    contact_1_appt = models.SmallIntegerField(choices=check_box, default=1)
    contact_1_denied = models.SmallIntegerField(choices=check_box, default=1)
    contact_1_cancelled= models.SmallIntegerField(choices=check_box, default=1)
    contact_1_confirmed= models.SmallIntegerField(choices=check_box, default=1)
    contact_1_timechange= models.SmallIntegerField(choices=check_box, default=1)
    contact_1_reminder= models.SmallIntegerField(choices=check_box, default=1)

    contact_2_name = models.CharField(max_length=255)
    contact_2_areacode = models.IntegerField()
    contact_2_phone1 = models.IntegerField()
    contact_2_phone2 = models.IntegerField()
    contact_2_email = models.EmailField(max_length=255)
    contact_2_notify_email = models.SmallIntegerField(choices=check_box, default=1)
    contact_2_notify_text = models.SmallIntegerField(choices=check_box, default=1)
    contact_2_notify_call = models.SmallIntegerField(choices=check_box, default=1)
    contact_2_canconfirm = models.SmallIntegerField(choices=check_box, default=1)
    contact_2_candenied = models.SmallIntegerField(choices=check_box, default=1)

    contact_2_appt = models.SmallIntegerField(choices=check_box, default=1)
    contact_2_denied = models.SmallIntegerField(choices=check_box, default=1)
    contact_2_cancelled = models.SmallIntegerField(choices=check_box, default=1)
    contact_2_confirmed = models.SmallIntegerField(choices=check_box, default=1)
    contact_2_timechange = models.SmallIntegerField(choices=check_box, default=1)
    contact_2_reminder = models.SmallIntegerField(choices=check_box, default=1)
