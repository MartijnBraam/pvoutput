# Api wrapper for pvoutput.org

This is a simple python module for uploading your solarpanel data to pvoutput.

# Usage

```python
from pvoutput import PvOutputApi

api = PvOutputApi(api_key="something", system_id="something")

# Call every 5, 10 or 15 minutes with new data
api.update_status(power_generation=200, temperature=39.2, voltage=800)
```