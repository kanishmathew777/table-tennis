def error_msg_string(self, errors):
    errors_string = ''
    for k, v in errors.items():
        if isinstance(v, dict):
            v = self.error_msg_list(v)
        for msg in v:
            errors_string = ''.join(str(msg))
    return errors_string
