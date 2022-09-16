from browser import document, alert
import convert

numeralInput = document["numeral-input"]
numeralSubmit = document["numeral-submit"]
numberInput = document["number-input"]
numberSubmit = document["number-submit"]



numeralSubmit.onclick = lambda: alert.message(convert.numeralToInt(numeralInput.value))
numberSubmit.onclick = lambda: alert.message(convert.intToNumeral(numberInput.value))