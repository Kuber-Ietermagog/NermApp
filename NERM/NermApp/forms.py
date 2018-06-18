from django import forms
from django.contrib.auth.models import User
from NermApp.models import UserProfileInfo
import os
import json

def getJsonData(filename):
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    JSON_DIR = os.path.join(BASE_DIR, 'static', 'json', filename)
    with open(JSON_DIR, 'rt') as my_file:
        data = json.load(my_file)
    my_file.close()
    return data

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta():
        model = User
        fields = ('username', 'email', 'password')

class gauge1Parameters(forms.Form):
    Qty_gauges = forms.IntegerField()
    Label_Gauge_1 = forms.CharField()
    Text_Gauge_1 = forms.CharField()
    LM35_Temp_1 = forms.BooleanField(required=False)
    Color_Gauge_1 = forms.CharField()
    Alm_Direction_1 = forms.CharField()
    Alarm_Level_1 = forms.IntegerField()
    Trip_Level_1 = forms.IntegerField()
    Units_Gauge_1 = forms.CharField()
    Min_Value_1 = forms.IntegerField()
    Max_Value_1 = forms.IntegerField()
    Major_Tick_1 = forms.IntegerField()
    Minor_Tick_1 = forms.IntegerField()
    Zone_1_1 = forms.IntegerField()
    Zone_1_Clr_1 = forms.CharField()
    Zone_2_1 = forms.IntegerField()
    Zone_2_Clr_1 = forms.CharField()
    Zone_3_1 = forms.IntegerField()
    Zone_3_Clr_1 = forms.CharField()

class gauge2Parameters(forms.Form):
    Label_Gauge_2 = forms.CharField()
    Text_Gauge_2 = forms.CharField()
    LM35_Temp_2 = forms.BooleanField(required=False)
    Color_Gauge_2 = forms.CharField()
    Alm_Direction_2 = forms.CharField()
    Alarm_Level_2 = forms.IntegerField()
    Trip_Level_2 = forms.IntegerField()
    Units_Gauge_2 = forms.CharField()
    Min_Value_2 = forms.IntegerField()
    Max_Value_2 = forms.IntegerField()
    Major_Tick_2 = forms.IntegerField()
    Minor_Tick_2 = forms.IntegerField()
    Zone_1_2 = forms.IntegerField()
    Zone_1_Clr_2 = forms.CharField()
    Zone_2_2 = forms.IntegerField()
    Zone_2_Clr_2 = forms.CharField()
    Zone_3_2 = forms.IntegerField()
    Zone_3_Clr_2 = forms.CharField()


class gauge3Parameters(forms.Form):
    Label_Gauge_3 = forms.CharField()
    Text_Gauge_3 = forms.CharField()
    LM35_Temp_3 = forms.BooleanField(required=False)
    Color_Gauge_3 = forms.CharField()
    Alm_Direction_3 = forms.CharField()
    Alarm_Level_3 = forms.IntegerField()
    Trip_Level_3 = forms.IntegerField()
    Units_Gauge_3 = forms.CharField()
    Min_Value_3 = forms.IntegerField()
    Max_Value_3 = forms.IntegerField()
    Major_Tick_3 = forms.IntegerField()
    Minor_Tick_3 = forms.IntegerField()
    Zone_1_3 = forms.IntegerField()
    Zone_1_Clr_3 = forms.CharField()
    Zone_2_3 = forms.IntegerField()
    Zone_2_Clr_3 = forms.CharField()
    Zone_3_3 = forms.IntegerField()
    Zone_3_Clr_3 = forms.CharField()

class gauge4Parameters(forms.Form):
    Label_Gauge_4 = forms.CharField()
    Text_Gauge_4 = forms.CharField()
    LM35_Temp_4 = forms.BooleanField(required=False)
    Color_Gauge_4 = forms.CharField()
    Alm_Direction_4 = forms.CharField()
    Alarm_Level_4 = forms.IntegerField()
    Trip_Level_4 = forms.IntegerField()
    Units_Gauge_4 = forms.CharField()
    Min_Value_4 = forms.IntegerField()
    Max_Value_4 = forms.IntegerField()
    Major_Tick_4 = forms.IntegerField()
    Minor_Tick_4 = forms.IntegerField()
    Zone_1_4 = forms.IntegerField()
    Zone_1_Clr_4 = forms.CharField()
    Zone_2_4 = forms.IntegerField()
    Zone_2_Clr_4 = forms.CharField()
    Zone_3_4 = forms.IntegerField()
    Zone_3_Clr_4 = forms.CharField()

class inputLabels(forms.Form):
    input_00 = forms.CharField()
    input_01 = forms.CharField()
    input_02 = forms.CharField()
    input_03 = forms.CharField()
    input_04 = forms.CharField()
    input_05 = forms.CharField()
    input_06 = forms.CharField()
    input_07 = forms.CharField()
    input_08 = forms.CharField()
    input_09 = forms.CharField()
    input_10 = forms.CharField()
    input_11 = forms.CharField()
    input_12 = forms.CharField()
    input_13 = forms.CharField()
    input_14 = forms.CharField()
    input_15 = forms.CharField()


class AlarmSet(forms.Form):
    i_alm_00 = forms.IntegerField()
    i_alm_01 = forms.IntegerField()
    i_alm_02 = forms.IntegerField()
    i_alm_03 = forms.IntegerField()
    i_alm_04 = forms.IntegerField()
    i_alm_05 = forms.IntegerField()
    i_alm_06 = forms.IntegerField()
    i_alm_07 = forms.IntegerField()
    i_alm_08 = forms.IntegerField()
    i_alm_09 = forms.IntegerField()
    i_alm_10 = forms.IntegerField()
    i_alm_11 = forms.IntegerField()
    i_alm_12 = forms.IntegerField()
    i_alm_13 = forms.IntegerField()
    i_alm_14 = forms.IntegerField()
    i_alm_15 = forms.IntegerField()

class DigitalUsed(forms.Form):
    i_used_00 = forms.BooleanField(required=False)
    i_used_01 = forms.BooleanField(required=False)
    i_used_02 = forms.BooleanField(required=False)
    i_used_03 = forms.BooleanField(required=False)
    i_used_04 = forms.BooleanField(required=False)
    i_used_05 = forms.BooleanField(required=False)
    i_used_06 = forms.BooleanField(required=False)
    i_used_07 = forms.BooleanField(required=False)
    i_used_08 = forms.BooleanField(required=False)
    i_used_09 = forms.BooleanField(required=False)
    i_used_10 = forms.BooleanField(required=False)
    i_used_11 = forms.BooleanField(required=False)
    i_used_12 = forms.BooleanField(required=False)
    i_used_13 = forms.BooleanField(required=False)
    i_used_14 = forms.BooleanField(required=False)
    i_used_15 = forms.BooleanField(required=False)


class JobInfo(forms.Form):
    Customer = forms.CharField()
    Job_Number = forms.CharField()
    Date_of_Manufacture = forms.CharField()
    Clear_Events = forms.BooleanField(required=False)
    IP_Address = forms.GenericIPAddressField()
    NERM_serial_number = forms.CharField()
    Bar_graph_serial_number = forms.CharField()

class ChangeIp(forms.Form):
    IP_Address = forms.GenericIPAddressField()
