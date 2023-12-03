import re

def dob_mask(log_text):
    """
    Function used to anonymize patient's date of births to just the year while maintaining the original formatting of the log files
    :param log_text: Line of log text that potentially contains patient's unmasked DOB
    :return: Log text with patients DOB masked
    """
    def pattern_one(text):
        # function to catch date formatted with "/"
        pattern = re.compile(r"(\s*)DOB(\s*)=(\s*)'\d{1,2}/\d{1,2}/(\d{4})(\s*)'(\s*)")  # some DOBS have whitespace on either side
        mask = pattern.sub(r"\1DOB\2=\3'X/X/\4\5'\6", text)

        return mask

    def pattern_two(text):
        # function to catch date formatted with "-"
        pattern = re.compile(r"(\s*)DOB(\s*)=(\s*)'\d{1,2}-\d{1,2}-(\d{4})(\s*)'(\s*)")
        mask = pattern.sub(r"\1DOB\2=\3'X-X-\4\5'\6", text)

        return mask

    def pattern_three(text):
        # function for dates in text form (for example, July 4th 2023)
        pattern = re.compile(r"(\s*)([A-Za-z]+)\s+\d{1,2}(st|nd|rd|th)\s+(\d{4})(\s*)'(\s*)")
        mask = pattern.sub(r"\1X X \4\5'\6", text)

        return mask

    # format logs
    log_text_formatted = log_text.replace("DATE_OF_BIRTH", "DOB")
    dob_masked = pattern_three(pattern_two(pattern_one(log_text_formatted)))
    if "DATE_OF_BIRTH" in log_text:
        dob_masked = dob_masked.replace("DOB", "DATE_OF_BIRTH")  # maintain original log formatting

    return dob_masked