from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import (
    AbstractBaseUser,
    PermissionsMixin
)
from django.db import models


class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('User must have an email address.')
        user = self.model(email=self.normalize_email(email), **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password):
        user = self.create_user(email, password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    objects = UserManager()
    USERNAME_FIELD = 'email'


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


class ApplicationInstruction(models.Model):
    access_choices = [
        ('door code', 'door code'),
        ('go direct', 'go direct'),
        ('key', 'key'),
        ('sentrilock', 'sentrilock'),
        ('lock box', 'lock box')
    ]
    check_box = [
        ('1', 1),
        ('0', 0)
    ]

    alaram_choice = [('Yes', 'YES_2'), ('No', 'NO_2')]
    double_booking_choice = [('Yes', 'YES'), ('No', 'NO')]
    appt_choice = [('1 hour', '1 hour'), ('1/2 Hour', '1/2 Hour'), ('15 minutes', '15 minutes')]
    mls_number = models.CharField(max_length=255)
    property_name = models.CharField(max_length=255)
    agent_name = models.CharField(max_length=255)

    # Appointment Instructions
    min_notice = models.SmallIntegerField(default=2)
    double_booking = models.CharField(max_length=255, choices=double_booking_choice)
    appointment_duration = models.CharField(max_length=255, choices=appt_choice)

    # Page me regarding
    property_new_appointment = models.BooleanField(default=False)
    property_denied = models.BooleanField(default=False)
    property_cancelled = models.BooleanField(default=False)
    property_confirmed = models.BooleanField(default=False)
    property_time_change = models.BooleanField(default=False)
    property_reminder = models.BooleanField(default=False)

    # special_instrctions
    lbx_located = models.TextField(max_length=500,
                                   help_text='Where is the LBX located? / Any other access instructions?')
    restrict_time = models.TextField(max_length=500,
                                     help_text='Are there any restricted times / days / special instructions?')
    showing_agent_info = models.TextField(max_length=500, help_text='Other info for Showing Agent:')

    access_instruction = models.CharField(max_length=125, choices=access_choices, default='key')
    lbx_code = models.CharField(max_length=500,
                                help_text='')
    is_alarm = models.CharField(choices=alaram_choice, max_length=255)
    alaram_code = models.CharField(max_length=255)

    turn_off_lights = models.BooleanField(default=False)
    remove_shoes = models.BooleanField(default=False)
    leave_card = models.BooleanField(default=False)
    lock_doors = models.BooleanField(default=True)
    call_if_late = models.BooleanField(default=False)
    knock_first = models.BooleanField(default=False)
    bring_reco_lic = models.BooleanField(default=False)

    contact_1_name = models.CharField(max_length=255)
    contact_1_areacode = models.IntegerField()
    contact_1_phone1 = models.IntegerField()
    contact_1_phone2 = models.IntegerField()
    contact_1_notify_email = models.BooleanField(default=False)
    contact_1_email = models.EmailField()

    contact_1_notify_text = models.BooleanField(default=False)
    contact_1_notify_call = models.BooleanField(default=False)
    contact_1_canconfirm = models.BooleanField(default=False)
    contact_1_candenied = models.BooleanField(default=False)

    contact_1_appt = models.BooleanField(default=False)
    contact_1_denied = models.BooleanField(default=False)
    contact_1_cancelled = models.BooleanField(default=False)
    contact_1_confirmed = models.BooleanField(default=False)
    contact_1_timechange = models.BooleanField(default=False)
    contact_1_reminder = models.BooleanField(default=False)

    contact_2_name = models.CharField(max_length=255)
    contact_2_areacode = models.IntegerField()
    contact_2_phone1 = models.IntegerField()
    contact_2_phone2 = models.IntegerField()
    contact_2_email = models.EmailField(max_length=255)
    contact_2_notify_email = models.BooleanField(default=False)
    contact_2_notify_text = models.BooleanField(default=False)
    contact_2_notify_call = models.BooleanField(default=False)
    contact_2_canconfirm = models.BooleanField(default=False)
    contact_2_candenied = models.BooleanField(default=False)

    contact_2_appt = models.BooleanField(default=False)
    contact_2_denied = models.BooleanField(default=False)
    contact_2_cancelled = models.BooleanField(default=False)
    contact_2_confirmed = models.BooleanField(default=False)
    contact_2_timechange = models.BooleanField(default=False)
    contact_2_reminder = models.BooleanField(default=False)

    property_name_2 = models.CharField(max_length=255)
    agent_name_2 = models.CharField(max_length=255)
    date = models.CharField(max_length=255)
    time = models.CharField(max_length=255)
    premtive_choices = [
        ("Yes", "YES_3"),
        ("No", "NO_3"),
    ]
    minimum_irrevocable_choice = [
        ("Yes", "YES_4"),
        ("No", "NO_4"),
    ]
    admin_instruction_choices = [('Email / Text listing contact(s) & wait for confirmation',
                                  'Email / Text listing contact(s) & wait for confirmation'),
                                 ('Leave voicemail & immediatley confirm', 'Leave voicemail & immediatley confirm'),
                                 ('Property is vacant, always confirm', 'Property is vacant, always confirm'),
                                 ('Auto message listing contacts and confirm',
                                  'Auto message listing contacts and confirm'),
                                 ('Call listing agent for confirmation instructions',
                                  'Call listing agent for confirmation instructions'),
                                 ('Do not contact listing agent. They will confirm direct.',
                                  'Do not contact listing agent. They will confirm direct.'),
                                 ('Page listing agent for confirmation instructions',
                                  'Page listing agent for confirmation instructions'),
                                 ('Call listing contac(s) & wait for conf', 'Call listing contac(s) & wait for conf')]
    admin_instruction = models.CharField(max_length=255, choices=admin_instruction_choices,
                                         default='Email / Text listing contact(s) & wait for confirmation')
    premetive_offers = models.CharField(max_length=255, choices=premtive_choices, default='NO_3')
    minimum_irrevocable = models.CharField(max_length=255, choices=minimum_irrevocable_choice, default='NO_4')
    how_long = models.SmallIntegerField()

    notify_in_person = models.BooleanField(default=False)
    at_location = models.CharField(max_length=255, blank=True, null=True)

    notify_by_email = models.BooleanField(default=False)
    to_email = models.EmailField(max_length=255, blank=True, null=True)

    notify_by_fax = models.BooleanField(default=False)
    to_fax = models.CharField(max_length=255, blank=True, null=True)

    other_method = models.BooleanField(default=False)
    other_method_text = models.TextField(max_length=500,
                                         help_text='Other offer submission method', blank=True, null=True)
    additional_information = models.TextField(max_length=500,
                                              help_text='Is there any additional information you would like to include in the automated notification that goes to the showing agents when an offer is registered')

    other_offer_details = models.TextField(max_length=500,
                                           help_text='Other details showing agents should know?')
    notification_choices = [('All agents', 'All agents'),
                            ('Agents with registered offers', 'Agents with registered offers'),
                            ('Do Not Send', 'Do Not Send')]
    notification = models.CharField(max_length=255, choices=notification_choices, default='All agents')
    offer_choices = [('Offers accepted anytime', 'Offers accepted anytime'),
                     ('Holding offer date', 'Holding offer date')]
    when_offers_accept = models.CharField(max_length=255, choices=offer_choices, default='All agents')

    def __str__(self):
        return self.property_name


class Form120(models.Model):
    buyer_one = models.CharField(max_length=255)
    buyer_one_street = models.CharField(max_length=255)
    buyer_one_phone = models.CharField(max_length=255)

    buyer_two = models.CharField(max_length=255)
    buyer_two_street = models.CharField(max_length=255)

    seller_one = models.CharField(max_length=255)
    seller_one_street = models.CharField(max_length=255)
    seller_one_phone = models.CharField(max_length=255)

    seller_two = models.CharField(max_length=255)
    seller_two_street = models.CharField(max_length=255)

    prop_offer_date = models.DateField()
    prop_street_no = models.CharField(max_length=255)
    prop_street = models.CharField(max_length=255)
    prop_unit_no = models.CharField(max_length=255)
    prop_city = models.CharField(max_length=255)
    prop_state = models.CharField(max_length=255)
    prop_zipcode = models.CharField(max_length=255)
    irrevocable_person = models.CharField(max_length=255)
    irrevocable_time = models.TimeField(max_length=255)
    irrevocable_date = models.DateField(max_length=255)

    acceptance_time = models.TimeField()
    acceptance_date = models.DateField()
    seller_phone_number = models.PositiveIntegerField()

    seller_lawyer_name = models.CharField(max_length=255)
    seller_lawyer_address = models.CharField(max_length=255)
    seller_lawyer_email = models.CharField(max_length=255)
    seller_lawyer_phone = models.CharField(max_length=255)
    seller_lawyer_fax = models.CharField(max_length=255)

    buyer_lawyer_name = models.CharField(max_length=255)
    buyer_lawyer_address = models.CharField(max_length=255)
    buyer_lawyer_email = models.CharField(max_length=255)
    buyer_lawyer_phone = models.CharField(max_length=255)
    buyer_lawyer_fax = models.CharField(max_length=255)

    def __str__(self):
        return self.seller_one


class ReceptionEmail(models.Model):
    sender_name = models.CharField(max_length=255, default='test user')
    sender_email = models.EmailField(max_length=255)
    sender_password = models.CharField(max_length=255, default=11111)
    receiver_email = models.EmailField(max_length=255)

    def __str__(self):
        return self.sender_email


class ProcedureAgreement(models.Model):
    property_address = models.CharField(max_length=255)
    client_name = models.CharField(max_length=255)
    seller_1_name = models.CharField(max_length=255)
    seller_1_date = models.DateField(max_length=255)
    seller_2_name = models.CharField(max_length=255)
    seller_2_date = models.DateField(max_length=255)
    broker_name = models.CharField(max_length=255)
    broker_date = models.DateField(max_length=255)

    def __str__(self):
        return self.property_address


class Form810(models.Model):
    acknowledgement = models.CharField(max_length=255)
    broker_1 = models.CharField(max_length=255)
    broker_2 = models.CharField(max_length=255)

    def __str__(self):
        return self.acknowledgement


class AuthorizationRequest(models.Model):
    property_address = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    offer_until = models.DateField(max_length=255)

    def __str__(self):
        return self.property_address


class Form248(models.Model):
    seller_1 = models.CharField(max_length=255)
    seller_2 = models.CharField(max_length=255)
    buyer_1 = models.CharField(max_length=255)
    buyer_2 = models.CharField(max_length=255)
    street_number = models.CharField(max_length=255)
    street = models.CharField(max_length=255)
    unit_number = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    zip_code = models.CharField(max_length=255)
    broker = models.CharField(max_length=255)
    purpose_1 = models.CharField(max_length=255)
    entry_access_1 = models.CharField(max_length=255)
    purpose_2 = models.CharField(max_length=255)
    entry_access_2 = models.CharField(max_length=255)
    purpose_3 = models.CharField(max_length=255)
    entry_access_3 = models.CharField(max_length=255)
    tenent_ack = models.CharField(max_length=255)
    additional_terms = models.CharField(max_length=255)

    def __str__(self):
        return self.seller_1


class CheckList(models.Model):
    property_address = models.CharField(max_length=255)
    mls_num = models.CharField(max_length=255)
    ar_mls_num = models.CharField(max_length=255)
    already_loaded_no = models.BooleanField(max_length=255)
    already_loaded_yes = models.BooleanField(max_length=255)
    board_yes = models.BooleanField(max_length=255)
    board_no = models.BooleanField(max_length=255)
    already_loaded = models.BooleanField(max_length=255)
    s_data_sheet = models.BooleanField(max_length=255)
    s_listing_agreement = models.BooleanField(max_length=255)
    s_working_with_realtor = models.BooleanField(max_length=255)
    mortgage_verification = models.BooleanField(max_length=255)
    fintrac = models.BooleanField(max_length=255)
    property_facts = models.BooleanField(max_length=255)
    s_appt_instruc = models.BooleanField(max_length=255)
    s_process_to_seller = models.BooleanField(max_length=255)
    s_mls_depart = models.BooleanField(max_length=255)
    s_power_of_attorney = models.BooleanField(max_length=255)
    s_property_officer = models.BooleanField(max_length=255)
    s_property_tenant_ack = models.BooleanField(max_length=255)
    s_speak_design = models.BooleanField(max_length=255)
    s_privacy_act = models.BooleanField(max_length=255)
    s_auth_forms = models.BooleanField(max_length=255)
    except_listing_agreement = models.BooleanField(max_length=255)
    proceedure_agreement = models.BooleanField(max_length=255)
    l_data_sheet = models.BooleanField(max_length=255)
    l_listing_agreement = models.BooleanField(max_length=255)
    l_working_with_realtor = models.BooleanField(max_length=255)
    l_appt_instruc = models.BooleanField(max_length=255)
    l_process_to_seller = models.BooleanField(max_length=255)
    l_mls_depart = models.BooleanField(max_length=255)
    l_power_of_attorney = models.BooleanField(max_length=255)
    l_property_officer = models.BooleanField(max_length=255)
    l_property_tenant_ack = models.BooleanField(max_length=255)
    l_speak_design = models.BooleanField(max_length=255)
    l_privacy_act = models.BooleanField(max_length=255)
    l_auth_forms = models.BooleanField(max_length=255)

    def __str__(self):
        return self.mls_num


class ExceptionList(models.Model):
    commission = models.CharField(max_length=255)

    def __str__(self):
        return self.commission


class Form244(models.Model):
    street_number = models.CharField(max_length=255)
    street = models.CharField(max_length=255)
    unit_num = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    zip_code = models.CharField(max_length=255)
    seller_1 = models.CharField(max_length=255)
    seller_2 = models.CharField(max_length=255)
    broker = models.CharField(max_length=255)
    broker_id = models.CharField(max_length=255)
    msl_number = models.CharField(max_length=255)
    interboaard_mls = models.CharField(max_length=255)
    board = models.CharField(max_length=255)
    list_date = models.DateField(max_length=255)
    time_limit = models.CharField(max_length=255)
    offer_time = models.TimeField(max_length=255)
    present_date = models.DateField(max_length=255)
    other_dir = models.CharField(max_length=255)
    other_dir1 = models.CharField(max_length=255)
    other_dir2 = models.CharField(max_length=255)
    other_dir3 = models.CharField(max_length=255)
    disclaimer = models.CharField(max_length=255)
    seller1_sig = models.CharField(max_length=255)
    seller2_sig = models.CharField(max_length=255)

    def __str__(self):
        return self.msl_number
