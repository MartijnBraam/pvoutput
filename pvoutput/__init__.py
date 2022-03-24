import requests
import datetime


class PvOutputApi(object):
    def __init__(self, api_key, system_id, cumulative=False):
        self.api_key = api_key
        self.system_id = system_id
        self.cumulative = cumulative
        self.api_url = 'http://pvoutput.org/service/r2/addstatus.jsp'

    def update_status(self, energy_generation=None, power_generation=None, energy_consumption=None,
                      power_consumption=None, temperature=None,
                      voltage=None, time=None):

        if not energy_generation and not power_generation and not energy_consumption and not power_consumption:
            raise ValueError("You need at least one of: enegergy_generation, power_generation,"
                             "energy_consumption, power_consumption")

        if not time:
            time = datetime.datetime.now()

        parameters = {
            'c': "1" if self.cumulative else "0",
            'd': time.strftime("%Y%m%d"),
            't': time.strftime("%H:%M")
        }

        if energy_generation:
            parameters['v1'] = str(energy_generation)

        if power_generation:
            parameters['v2'] = str(power_generation)

        if energy_consumption:
            parameters['v3'] = str(energy_consumption)

        if power_consumption:
            parameters['v4'] = str(power_consumption)

        if temperature:
            parameters['v5'] = str(temperature)

        if voltage:
            parameters['v6'] = str(voltage)

        headers = {
            'X-Pvoutput-Apikey': self.api_key,
            'X-Pvoutput-SystemId': self.system_id
        }

        response = requests.post(self.api_url, parameters, headers=headers)

        return response.status_code == 200
