

def form_service(form):
    userid = form.cleaned_data['UserID']
    serial = form.cleaned_data['Serial']
    description = form.cleaned_data['ProblemDescription']
    indicator1 = form.cleaned_data['Indicator1']
    indicator2 = form.cleaned_data['Indicator2']
    indicator3 = form.cleaned_data['Indicator3']
    if serial.isdecimal():
        return "bad serial"
    elif serial.startswith('24-X'):
        return "upgrade"
    elif serial.startswith('36-X'):
        if (indicator1 == 'on') & (indicator2 == 'on') & (indicator3 == 'on'):
            return "OK"
        elif (indicator1 == 'off') & (indicator2 == 'off') & (indicator3 == 'off'):
            return "turn on"
        elif indicator1 == 'blinking':
            if (indicator2 == 'blinking') | (indicator3 == 'blinking'):
                return "wait"
        elif (indicator2 == 'blinking') & (indicator3 == 'blinking'):
            return "wait"
    elif serial.startswith('51-B'):
        if (indicator1 == 'off') & (indicator2 == 'off') & (indicator3 == 'off'):
            return "turn on"
        elif (indicator1 == 'blinking') | (indicator2 == 'blinking') | (indicator3 == 'blinking'):
            return "wait"
        elif (indicator1 == 'on') | (indicator2 == 'on') | (indicator3 == 'on'):
            return "ok"
    return "unknown"
