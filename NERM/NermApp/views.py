from django.shortcuts import render
from . import forms
from NermApp.forms import UserForm
import os
import json
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.models import Permission, User


def getJsonData(filename):
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    JSON_DIR = os.path.join(BASE_DIR, 'static', 'json', filename)
    with open(JSON_DIR, 'rt') as my_file:
        data = json.load(my_file)
    my_file.close()
    return data

def setJsonData(filename, data):
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    JSON_DIR = os.path.join(BASE_DIR, 'static', 'json', filename)
    with open(JSON_DIR, 'wt') as my_file:
       new_data = json.dumps(data)
       my_file.write(new_data)
    my_file.close()

def gauge_ticks(max_value, major_tick):
    ticks = []
    range_val = int(max_value/major_tick + 1)
    for i in range(0, range_val):
        ticks.append(i*major_tick)
    return ticks

# Create your views here.
def monitor(request):
    return render(request, 'NermApp/monitor.html')

def events(request):
    return render(request, 'NermApp/events.html')

@login_required
@permission_required('auth.can_register_user')
def register(request):

    registered = False

    if request.method == "POST":
        user_form = UserForm(data=request.POST)

        if user_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            permission = Permission.objects.get(
                codename='can_set_ip',
            )

            user.user_permissions.add(permission)

            user.save()

            registered = True
        else:
            print(user_form.errors)
    else:
        user_form = UserForm()

    return render(request, 'NermApp/registration.html', {'user_form': user_form, 'registered': registered})

def user_login(request):

    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username,password=password)

        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('monitor'))
            else:
                return HttpResponse("ACCOUNT NOT ACTIVE")
        else:
            print("Unauthorized user tried to login!")
            print("Username: {} and Password: {}".format(username, password))
            # return HttpResponse("Invalid login details supplied!\nUsername: {} and Password: {}".format(username, password))
            return HttpResponseRedirect(reverse('monitor'))

    else:
        return render(request, 'NermApp/login.html', {})

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('monitor'))

@login_required
@permission_required('auth.can_set_digital')
def digitalSet(request):
    i_labels = forms.inputLabels()
    i_alarms = forms.AlarmSet()
    i_used = forms.DigitalUsed()

    if request.method == 'GET':
        data = getJsonData('digitals.json')

        i_labels.fields['input_00'].initial = data['input_lbl'][0]
        i_labels.fields['input_01'].initial = data['input_lbl'][1]
        i_labels.fields['input_02'].initial = data['input_lbl'][2]
        i_labels.fields['input_03'].initial = data['input_lbl'][3]
        i_labels.fields['input_04'].initial = data['input_lbl'][4]
        i_labels.fields['input_05'].initial = data['input_lbl'][5]
        i_labels.fields['input_06'].initial = data['input_lbl'][6]
        i_labels.fields['input_07'].initial = data['input_lbl'][7]
        i_labels.fields['input_08'].initial = data['input_lbl'][8]
        i_labels.fields['input_09'].initial = data['input_lbl'][9]
        i_labels.fields['input_10'].initial = data['input_lbl'][10]
        i_labels.fields['input_11'].initial = data['input_lbl'][11]
        i_labels.fields['input_12'].initial = data['input_lbl'][12]
        i_labels.fields['input_13'].initial = data['input_lbl'][13]
        i_labels.fields['input_14'].initial = data['input_lbl'][14]
        i_labels.fields['input_15'].initial = data['input_lbl'][15]

        i_alarms.fields['i_alm_00'].initial = data['alarm_on'][0]
        i_alarms.fields['i_alm_01'].initial = data['alarm_on'][1]
        i_alarms.fields['i_alm_02'].initial = data['alarm_on'][2]
        i_alarms.fields['i_alm_03'].initial = data['alarm_on'][3]
        i_alarms.fields['i_alm_04'].initial = data['alarm_on'][4]
        i_alarms.fields['i_alm_05'].initial = data['alarm_on'][5]
        i_alarms.fields['i_alm_06'].initial = data['alarm_on'][6]
        i_alarms.fields['i_alm_07'].initial = data['alarm_on'][7]
        i_alarms.fields['i_alm_08'].initial = data['alarm_on'][8]
        i_alarms.fields['i_alm_09'].initial = data['alarm_on'][9]
        i_alarms.fields['i_alm_10'].initial = data['alarm_on'][10]
        i_alarms.fields['i_alm_11'].initial = data['alarm_on'][11]
        i_alarms.fields['i_alm_12'].initial = data['alarm_on'][12]
        i_alarms.fields['i_alm_13'].initial = data['alarm_on'][13]
        i_alarms.fields['i_alm_14'].initial = data['alarm_on'][14]
        i_alarms.fields['i_alm_15'].initial = data['alarm_on'][15]

        i_used.fields['i_used_00'].initial = bool(data['used'][0])
        i_used.fields['i_used_01'].initial = bool(data['used'][1])
        i_used.fields['i_used_02'].initial = bool(data['used'][2])
        i_used.fields['i_used_03'].initial = bool(data['used'][3])
        i_used.fields['i_used_04'].initial = bool(data['used'][4])
        i_used.fields['i_used_05'].initial = bool(data['used'][5])
        i_used.fields['i_used_06'].initial = bool(data['used'][6])
        i_used.fields['i_used_07'].initial = bool(data['used'][7])
        i_used.fields['i_used_08'].initial = bool(data['used'][8])
        i_used.fields['i_used_09'].initial = bool(data['used'][9])
        i_used.fields['i_used_10'].initial = bool(data['used'][10])
        i_used.fields['i_used_11'].initial = bool(data['used'][11])
        i_used.fields['i_used_12'].initial = bool(data['used'][12])
        i_used.fields['i_used_13'].initial = bool(data['used'][13])
        i_used.fields['i_used_14'].initial = bool(data['used'][14])
        i_used.fields['i_used_15'].initial = bool(data['used'][15])



    if request.method == 'POST':
        i_labels = forms.inputLabels(request.POST)
        i_alarms = forms.AlarmSet(request.POST)
        i_used = forms.DigitalUsed(request.POST)

        if i_labels.is_valid():
            lbls = getJsonData('digitals.json')

            # Digital input labels
            lbls['input_lbl'][0] = i_labels.cleaned_data['input_00']
            lbls['input_lbl'][1] = i_labels.cleaned_data['input_01']
            lbls['input_lbl'][2] = i_labels.cleaned_data['input_02']
            lbls['input_lbl'][3] = i_labels.cleaned_data['input_03']
            lbls['input_lbl'][4] = i_labels.cleaned_data['input_04']
            lbls['input_lbl'][5] = i_labels.cleaned_data['input_05']
            lbls['input_lbl'][6] = i_labels.cleaned_data['input_06']
            lbls['input_lbl'][7] = i_labels.cleaned_data['input_07']
            lbls['input_lbl'][8] = i_labels.cleaned_data['input_08']
            lbls['input_lbl'][9] = i_labels.cleaned_data['input_09']
            lbls['input_lbl'][10] = i_labels.cleaned_data['input_10']
            lbls['input_lbl'][11] = i_labels.cleaned_data['input_11']
            lbls['input_lbl'][12] = i_labels.cleaned_data['input_12']
            lbls['input_lbl'][13] = i_labels.cleaned_data['input_13']
            lbls['input_lbl'][14] = i_labels.cleaned_data['input_14']
            lbls['input_lbl'][15] = i_labels.cleaned_data['input_15']

            setJsonData('digitals.json', lbls)

        if i_alarms.is_valid():
            lbls = getJsonData('digitals.json')

            # Digital input Alarm Conditions
            lbls['alarm_on'][0] = i_alarms.cleaned_data['i_alm_00']
            lbls['alarm_on'][1] = i_alarms.cleaned_data['i_alm_01']
            lbls['alarm_on'][2] = i_alarms.cleaned_data['i_alm_02']
            lbls['alarm_on'][3] = i_alarms.cleaned_data['i_alm_03']
            lbls['alarm_on'][4] = i_alarms.cleaned_data['i_alm_04']
            lbls['alarm_on'][5] = i_alarms.cleaned_data['i_alm_05']
            lbls['alarm_on'][6] = i_alarms.cleaned_data['i_alm_06']
            lbls['alarm_on'][7] = i_alarms.cleaned_data['i_alm_07']
            lbls['alarm_on'][8] = i_alarms.cleaned_data['i_alm_08']
            lbls['alarm_on'][9] = i_alarms.cleaned_data['i_alm_09']
            lbls['alarm_on'][10] = i_alarms.cleaned_data['i_alm_10']
            lbls['alarm_on'][11] = i_alarms.cleaned_data['i_alm_11']
            lbls['alarm_on'][12] = i_alarms.cleaned_data['i_alm_12']
            lbls['alarm_on'][13] = i_alarms.cleaned_data['i_alm_13']
            lbls['alarm_on'][14] = i_alarms.cleaned_data['i_alm_14']
            lbls['alarm_on'][15] = i_alarms.cleaned_data['i_alm_15']

            setJsonData('digitals.json', lbls)

        if i_used.is_valid():
            lbls = getJsonData('digitals.json')

            # Digital input Alarm Conditions
            lbls['used'][0] = int(i_used.cleaned_data['i_used_00'])
            lbls['used'][1] = int(i_used.cleaned_data['i_used_01'])
            lbls['used'][2] = int(i_used.cleaned_data['i_used_02'])
            lbls['used'][3] = int(i_used.cleaned_data['i_used_03'])
            lbls['used'][4] = int(i_used.cleaned_data['i_used_04'])
            lbls['used'][5] = int(i_used.cleaned_data['i_used_05'])
            lbls['used'][6] = int(i_used.cleaned_data['i_used_06'])
            lbls['used'][7] = int(i_used.cleaned_data['i_used_07'])
            lbls['used'][8] = int(i_used.cleaned_data['i_used_08'])
            lbls['used'][9] = int(i_used.cleaned_data['i_used_09'])
            lbls['used'][10] = int(i_used.cleaned_data['i_used_10'])
            lbls['used'][11] = int(i_used.cleaned_data['i_used_11'])
            lbls['used'][12] = int(i_used.cleaned_data['i_used_12'])
            lbls['used'][13] = int(i_used.cleaned_data['i_used_13'])
            lbls['used'][14] = int(i_used.cleaned_data['i_used_14'])
            lbls['used'][15] = int(i_used.cleaned_data['i_used_15'])

            setJsonData('digitals.json', lbls)

            return HttpResponseRedirect(reverse('monitor'))

    return render(request, 'NermApp/digitalsettings.html', {'my_labels':i_labels, 'my_alarms':i_alarms, 'my_digitals':i_used})

@login_required
@permission_required('auth.can_set_analog')
def analogSet(request):
    g1 = forms.gauge1Parameters()
    g2 = forms.gauge2Parameters()
    g3 = forms.gauge3Parameters()
    g4 = forms.gauge4Parameters()

    if request.method == 'GET':
        data = getJsonData('analogs.json')
        g1.fields['Qty_gauges'].initial = data['qty_gauges']
        g1.fields['Label_Gauge_1'].initial = data['lables'][0]
        g1.fields['Text_Gauge_1'].initial = data['legend_color'][0]
        g1.fields['LM35_Temp_1'].initial = bool(data['lm35'][0])
        g1.fields['Color_Gauge_1'].initial = data['face_color'][0]
        g1.fields['Trip_Level_1'].initial = data['trip_level'][0]
        g1.fields['Alarm_Level_1'].initial = data['alarm_level'][0]
        g1.fields['Units_Gauge_1'].initial = data['unit'][0]
        g1.fields['Min_Value_1'].initial = data['min_value'][0]
        g1.fields['Max_Value_1'].initial = data['max_value'][0]
        g1.fields['Alm_Direction_1'].initial = data['direction'][0]
        g1.fields['Major_Tick_1'].initial = data['major_tick'][0]
        g1.fields['Minor_Tick_1'].initial = data['minor_tick'][0]
        g1.fields['Zone_1_1'].initial = data['high_lights'][0][0]['to']
        g1.fields['Zone_1_Clr_1'].initial = data['high_lights'][0][0]['color']
        g1.fields['Zone_2_1'].initial = data['high_lights'][0][1]['to']
        g1.fields['Zone_2_Clr_1'].initial = data['high_lights'][0][1]['color']
        g1.fields['Zone_3_1'].initial = data['high_lights'][0][2]['to']
        g1.fields['Zone_3_Clr_1'].initial = data['high_lights'][0][2]['color']

        g2.fields['Label_Gauge_2'].initial = data['lables'][1]
        g2.fields['Text_Gauge_2'].initial = data['legend_color'][1]
        g2.fields['LM35_Temp_2'].initial = bool(data['lm35'][1])
        g2.fields['Color_Gauge_2'].initial = data['face_color'][1]
        g2.fields['Trip_Level_2'].initial = data['trip_level'][1]
        g2.fields['Alarm_Level_2'].initial = data['alarm_level'][1]
        g2.fields['Units_Gauge_2'].initial = data['unit'][1]
        g2.fields['Min_Value_2'].initial = data['min_value'][1]
        g2.fields['Max_Value_2'].initial = data['max_value'][1]
        g2.fields['Alm_Direction_2'].initial = data['direction'][1]
        g2.fields['Major_Tick_2'].initial = data['major_tick'][1]
        g2.fields['Minor_Tick_2'].initial = data['minor_tick'][1]
        g2.fields['Zone_1_2'].initial = data['high_lights'][1][0]['to']
        g2.fields['Zone_1_Clr_2'].initial = data['high_lights'][1][0]['color']
        g2.fields['Zone_2_2'].initial = data['high_lights'][1][1]['to']
        g2.fields['Zone_2_Clr_2'].initial = data['high_lights'][1][1]['color']
        g2.fields['Zone_3_2'].initial = data['high_lights'][1][2]['to']
        g2.fields['Zone_3_Clr_2'].initial = data['high_lights'][1][2]['color']

        g3.fields['Label_Gauge_3'].initial = data['lables'][2]
        g3.fields['Text_Gauge_3'].initial = data['legend_color'][2]
        g3.fields['LM35_Temp_3'].initial = bool(data['lm35'][2])
        g3.fields['Color_Gauge_3'].initial = data['face_color'][2]
        g3.fields['Trip_Level_3'].initial = data['trip_level'][2]
        g3.fields['Alarm_Level_3'].initial = data['alarm_level'][2]
        g3.fields['Units_Gauge_3'].initial = data['unit'][2]
        g3.fields['Min_Value_3'].initial = data['min_value'][2]
        g3.fields['Max_Value_3'].initial = data['max_value'][2]
        g3.fields['Alm_Direction_3'].initial = data['direction'][2]
        g3.fields['Major_Tick_3'].initial = data['major_tick'][2]
        g3.fields['Minor_Tick_3'].initial = data['minor_tick'][2]
        g3.fields['Zone_1_3'].initial = data['high_lights'][2][0]['to']
        g3.fields['Zone_1_Clr_3'].initial = data['high_lights'][2][0]['color']
        g3.fields['Zone_2_3'].initial = data['high_lights'][2][1]['to']
        g3.fields['Zone_2_Clr_3'].initial = data['high_lights'][2][1]['color']
        g3.fields['Zone_3_3'].initial = data['high_lights'][2][2]['to']
        g3.fields['Zone_3_Clr_3'].initial = data['high_lights'][2][2]['color']

        g4.fields['Label_Gauge_4'].initial = data['lables'][3]
        g4.fields['Text_Gauge_4'].initial = data['legend_color'][3]
        g4.fields['LM35_Temp_4'].initial = bool(data['lm35'][3])
        g4.fields['Color_Gauge_4'].initial = data['face_color'][3]
        g4.fields['Trip_Level_4'].initial = data['trip_level'][3]
        g4.fields['Alarm_Level_4'].initial = data['alarm_level'][3]
        g4.fields['Units_Gauge_4'].initial = data['unit'][3]
        g4.fields['Min_Value_4'].initial = data['min_value'][3]
        g4.fields['Max_Value_4'].initial = data['max_value'][3]
        g4.fields['Alm_Direction_4'].initial = data['direction'][3]
        g4.fields['Major_Tick_4'].initial = data['major_tick'][3]
        g4.fields['Minor_Tick_4'].initial = data['minor_tick'][3]
        g4.fields['Zone_1_4'].initial = data['high_lights'][3][0]['to']
        g4.fields['Zone_1_Clr_4'].initial = data['high_lights'][3][0]['color']
        g4.fields['Zone_2_4'].initial = data['high_lights'][3][1]['to']
        g4.fields['Zone_2_Clr_4'].initial = data['high_lights'][3][1]['color']
        g4.fields['Zone_3_4'].initial = data['high_lights'][3][2]['to']
        g4.fields['Zone_3_Clr_4'].initial = data['high_lights'][3][2]['color']


    if request.method == 'POST':
        g1 = forms.gauge1Parameters(request.POST)
        g2 = forms.gauge2Parameters(request.POST)
        g3 = forms.gauge3Parameters(request.POST)
        g4 = forms.gauge4Parameters(request.POST)

        if g1.is_valid():
            data = getJsonData('analogs.json')

            data['qty_gauges'] = g1.cleaned_data['Qty_gauges']
            data['lables'][0] = g1.cleaned_data['Label_Gauge_1']
            data['legend_color'][0] = g1.cleaned_data['Text_Gauge_1']
            data['lm35'][0] = int(g1.cleaned_data['LM35_Temp_1'])
            data['face_color'][0] = g1.cleaned_data['Color_Gauge_1']
            data['trip_level'][0] = g1.cleaned_data['Trip_Level_1']
            data['alarm_level'][0] = g1.cleaned_data['Alarm_Level_1']
            data['unit'][0] = g1.cleaned_data['Units_Gauge_1']
            data['min_value'][0] = g1.cleaned_data['Min_Value_1']
            data['max_value'][0] = g1.cleaned_data['Max_Value_1']
            data['direction'][0] = g1.cleaned_data['Alm_Direction_1']
            data['major_tick'][0] = g1.cleaned_data['Major_Tick_1']
            data['minor_tick'][0] = g1.cleaned_data['Minor_Tick_1']
            data['high_lights'][0][0]['from'] = g1.cleaned_data['Min_Value_1']
            data['high_lights'][0][0]['to'] = g1.cleaned_data['Zone_1_1']
            data['high_lights'][0][0]['color'] = g1.cleaned_data['Zone_1_Clr_1']
            data['high_lights'][0][1]['from'] = g1.cleaned_data['Zone_1_1']
            data['high_lights'][0][1]['to'] = g1.cleaned_data['Zone_2_1']
            data['high_lights'][0][1]['color'] = g1.cleaned_data['Zone_2_Clr_1']
            data['high_lights'][0][2]['from'] = g1.cleaned_data['Zone_2_1']
            data['high_lights'][0][2]['to'] = g1.cleaned_data['Max_Value_1']
            data['high_lights'][0][2]['color'] = g1.cleaned_data['Zone_3_Clr_1']

            setJsonData('analogs.json', data)

        if g2.is_valid():
            data = getJsonData('analogs.json')

            data['lables'][1] = g2.cleaned_data['Label_Gauge_2']
            data['legend_color'][1] = g2.cleaned_data['Text_Gauge_2']
            data['lm35'][1] = int(g2.cleaned_data['LM35_Temp_2'])
            data['face_color'][1] = g2.cleaned_data['Color_Gauge_2']
            data['trip_level'][1] = g2.cleaned_data['Trip_Level_2']
            data['alarm_level'][1] = g2.cleaned_data['Alarm_Level_2']
            data['unit'][1] = g2.cleaned_data['Units_Gauge_2']
            data['min_value'][1] = g2.cleaned_data['Min_Value_2']
            data['max_value'][1] = g2.cleaned_data['Max_Value_2']
            data['direction'][1] = g2.cleaned_data['Alm_Direction_2']
            data['major_tick'][1] = g2.cleaned_data['Major_Tick_2']
            data['minor_tick'][1] = g2.cleaned_data['Minor_Tick_2']
            data['high_lights'][1][0]['from'] = g2.cleaned_data['Min_Value_2']
            data['high_lights'][1][0]['to'] = g2.cleaned_data['Zone_1_2']
            data['high_lights'][1][0]['color'] = g2.cleaned_data['Zone_1_Clr_2']
            data['high_lights'][1][1]['from'] = g2.cleaned_data['Zone_1_2']
            data['high_lights'][1][1]['to'] = g2.cleaned_data['Zone_2_2']
            data['high_lights'][1][1]['color'] = g2.cleaned_data['Zone_2_Clr_2']
            data['high_lights'][1][2]['from'] = g2.cleaned_data['Zone_2_2']
            data['high_lights'][1][2]['to'] = g2.cleaned_data['Max_Value_2']
            data['high_lights'][1][2]['color'] = g2.cleaned_data['Zone_3_Clr_2']

            setJsonData('analogs.json', data)

        if g3.is_valid():
            data = getJsonData('analogs.json')

            data['lables'][2] = g3.cleaned_data['Label_Gauge_3']
            data['legend_color'][2] = g3.cleaned_data['Text_Gauge_3']
            data['lm35'][2] = int(g3.cleaned_data['LM35_Temp_3'])
            data['face_color'][2] = g3.cleaned_data['Color_Gauge_3']
            data['trip_level'][2] = g3.cleaned_data['Trip_Level_3']
            data['alarm_level'][2] = g3.cleaned_data['Alarm_Level_3']
            data['unit'][2] = g3.cleaned_data['Units_Gauge_3']
            data['min_value'][2] = g3.cleaned_data['Min_Value_3']
            data['max_value'][2] = g3.cleaned_data['Max_Value_3']
            data['direction'][2] = g3.cleaned_data['Alm_Direction_3']
            data['major_tick'][2] = g3.cleaned_data['Major_Tick_3']
            data['minor_tick'][2] = g3.cleaned_data['Minor_Tick_3']
            data['high_lights'][2][0]['from'] = g3.cleaned_data['Min_Value_3']
            data['high_lights'][2][0]['to'] = g3.cleaned_data['Zone_1_3']
            data['high_lights'][2][0]['color'] = g3.cleaned_data['Zone_1_Clr_3']
            data['high_lights'][2][1]['from'] = g3.cleaned_data['Zone_1_3']
            data['high_lights'][2][1]['to'] = g3.cleaned_data['Zone_2_3']
            data['high_lights'][2][1]['color'] = g3.cleaned_data['Zone_2_Clr_3']
            data['high_lights'][2][2]['from'] = g3.cleaned_data['Zone_2_3']
            data['high_lights'][2][2]['to'] = g3.cleaned_data['Max_Value_3']
            data['high_lights'][2][2]['color'] = g3.cleaned_data['Zone_3_Clr_3']


            setJsonData('analogs.json', data)

        if g4.is_valid():
            data = getJsonData('analogs.json')

            data['lables'][3] = g4.cleaned_data['Label_Gauge_4']
            data['legend_color'][3] = g4.cleaned_data['Text_Gauge_4']
            data['lm35'][3] = int(g4.cleaned_data['LM35_Temp_4'])
            data['face_color'][3] = g4.cleaned_data['Color_Gauge_4']
            data['trip_level'][3] = g4.cleaned_data['Trip_Level_4']
            data['alarm_level'][3] = g4.cleaned_data['Alarm_Level_4']
            data['unit'][3] = g4.cleaned_data['Units_Gauge_4']
            data['min_value'][3] = g4.cleaned_data['Min_Value_4']
            data['max_value'][3] = g4.cleaned_data['Max_Value_4']
            data['direction'][3] = g4.cleaned_data['Alm_Direction_4']
            data['major_tick'][3] = g4.cleaned_data['Major_Tick_4']
            data['minor_tick'][3] = g4.cleaned_data['Minor_Tick_4']
            data['high_lights'][3][0]['from'] = g4.cleaned_data['Min_Value_4']
            data['high_lights'][3][0]['to'] = g4.cleaned_data['Zone_1_4']
            data['high_lights'][3][0]['color'] = g4.cleaned_data['Zone_1_Clr_4']
            data['high_lights'][3][1]['from'] = g4.cleaned_data['Zone_1_4']
            data['high_lights'][3][1]['to'] = g4.cleaned_data['Zone_2_4']
            data['high_lights'][3][1]['color'] = g4.cleaned_data['Zone_2_Clr_4']
            data['high_lights'][3][2]['from'] = g4.cleaned_data['Zone_2_4']
            data['high_lights'][3][2]['to'] = g4.cleaned_data['Max_Value_4']
            data['high_lights'][3][2]['color'] = g4.cleaned_data['Zone_3_Clr_4']

            setJsonData('analogs.json', data)

        analog_data = getJsonData('analogs.json')
        analog_data['ticks'] = []
        for i in range(0,4):
            analog_data['ticks'].append(gauge_ticks(analog_data['max_value'][i], analog_data['major_tick'][i]))
        setJsonData('analogs.json', analog_data)

        return HttpResponseRedirect(reverse('monitor'))

    return render(request, 'NermApp/analogsettings.html', {'settings1': g1, 'settings2':g2, 'settings3':g3, 'settings4': g4})

@login_required
@permission_required('auth.can_set_jobinfo')
def jobInfo(request):
    job = forms.JobInfo()

    if request.method == 'GET':
        data = getJsonData('jobinfo.json')
        job.fields['Customer'].initial = data['info'][0]
        job.fields['Job_Number'].initial = data['info'][1]
        job.fields['Date_of_Manufacture'].initial = data['info'][2]
        job.fields['NERM_serial_number'].initial = data['info'][4]
        job.fields['Bar_graph_serial_number'].initial = data['info'][5]
        if os.popen('uname -a').read().split(' ')[1] == 'raspberrypi':
            current_IP = os.popen('ifconfig eth0 | grep "inet" | grep -v "inet6"').read().strip(' ').split(' ')[1]
            job.fields['IP_Address'].initial = current_IP

    if request.method == 'POST':
        job = forms.JobInfo(request.POST)

        if job.is_valid():
            data = getJsonData('jobinfo.json')

            data['info'][0] = job.cleaned_data['Customer']
            data['info'][1] = job.cleaned_data['Job_Number']
            data['info'][2] = job.cleaned_data['Date_of_Manufacture']
            data['info'][3] = job.cleaned_data['IP_Address']
            data['info'][4] = job.cleaned_data['NERM_serial_number']
            data['info'][5] = job.cleaned_data['Bar_graph_serial_number']
            if job.cleaned_data['Clear_Events']:
                BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
                JSON_DIR = os.path.join(BASE_DIR, 'static', 'json', 'events.json')
                with open(JSON_DIR, 'wt') as my_file:
                   my_file.write('')
                my_file.close()
            if os.popen('uname -a').read().split(' ')[1] == 'raspberrypi':
                current_IP = os.popen('ifconfig eth0 | grep "inet" | grep -v "inet6"').read().strip(' ').split(' ')[1]
                ip_data = open('/etc/dhcpcd.conf', 'rt').read()
                ip_data = ip_data.replace(current_IP, job.cleaned_data['IP_Address'])
                with open('/etc/dhcpcd.conf', 'wt') as my_file:
                    my_file.write(ip_data)
                my_file.close()
                ip_data = open('/etc/rc.local', 'rt').read()
                ip_data = ip_data.replace(current_IP, job.cleaned_data['IP_Address'])
                with open('/etc/rc.local', 'wt') as my_file:
                    my_file.write(ip_data)
                my_file.close()
                ip_data = open('/etc/nginx/sites-available/nermapp', 'rt').read()
                ip_data = ip_data.replace(current_IP, job.cleaned_data['IP_Address'])
                with open('/etc/nginx/sites-available/nermapp', 'wt') as my_file:
                    my_file.write(ip_data)
                my_file.close()
                import time
                logout(request)
                time.sleep(2)
                os.popen('sudo reboot -h now')


            setJsonData('jobinfo.json', data)

            return HttpResponse("System Reboot Initiated!")

    return render(request, 'NermApp/jobinfo.html', {'jobInfo': job})


@login_required
@permission_required('auth.can_set_ip')
def changeIp(request):
    job = forms.ChangeIp()

    if request.method == 'GET':
        if os.popen('uname -a').read().split(' ')[1] == 'raspberrypi':
            current_IP = os.popen('ifconfig eth0 | grep "inet" | grep -v "inet6"').read().strip(' ').split(' ')[1]
            job.fields['IP_Address'].initial = current_IP

    if request.method == 'POST':
        job = forms.ChangeIp(request.POST)

        if job.is_valid():
            data = getJsonData('jobinfo.json')

            data['info'][3] = job.cleaned_data['IP_Address']

            if os.popen('uname -a').read().split(' ')[1] == 'raspberrypi':
                current_IP = os.popen('ifconfig eth0 | grep "inet" | grep -v "inet6"').read().strip(' ').split(' ')[1]
                ip_data = open('/etc/dhcpcd.conf', 'rt').read()
                ip_data = ip_data.replace(current_IP, job.cleaned_data['IP_Address'])
                with open('/etc/dhcpcd.conf', 'wt') as my_file:
                    my_file.write(ip_data)
                my_file.close()
                ip_data = open('/etc/rc.local', 'rt').read()
                ip_data = ip_data.replace(current_IP, job.cleaned_data['IP_Address'])
                with open('/etc/rc.local', 'wt') as my_file:
                    my_file.write(ip_data)
                my_file.close()
                ip_data = open('/etc/nginx/sites-available/nermapp', 'rt').read()
                ip_data = ip_data.replace(current_IP, job.cleaned_data['IP_Address'])
                with open('/etc/nginx/sites-available/nermapp', 'wt') as my_file:
                    my_file.write(ip_data)
                my_file.close()
                import time
                logout(request)
                time.sleep(2)
                os.popen('sudo reboot -h now')


            setJsonData('jobinfo.json', data)

            return HttpResponse("System Reboot Initiated!")

    return render(request, 'NermApp/changeip.html', {'jobInfo': job})
