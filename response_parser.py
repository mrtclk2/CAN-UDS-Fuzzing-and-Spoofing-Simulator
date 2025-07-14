
def parse_response(data):
    if len(data) < 1:
        return "Invalid"

    sid = data[0]

    if sid == 0x7F:
        # Negative Response
        try:
            original_sid = data[1]
            response_code = data[2]
            return f"NEGATIVE_RESPONSE to SID 0x{original_sid:02X} → NRC 0x{response_code:02X}"
        except IndexError:
            return "Malformed NEGATIVE_RESPONSE"
    else:
        return "OK or Positive Response"
