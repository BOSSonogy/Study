import logging
from datetime import datetime

KEY = "TSTFEED0300|7E3E|0400"
LOG_FILE = "hblog.txt"


def get_filtered_log():
    filtered_log = []
    with open(LOG_FILE, "r", encoding="utf-8") as file:
        for line in file:
            if KEY in line:
                filtered_log.append(line)
    return filtered_log

def get_timestamp(log_line):
    timestamp_index = log_line.find("Timestamp ")
    timestamp = log_line[timestamp_index + 10: timestamp_index + 18]
    return datetime.strptime(timestamp, "%H:%M:%S")

def check_heartbeat(filtered_log):
    logging.basicConfig(
        filename="hb_test.log",
        level=logging.WARNING,
        format="%(levelname)s | %(message)s",
        filemode="w"
    )
    for i in range(len(filtered_log) - 1):
        current_time = get_timestamp(filtered_log[i])
        next_time = get_timestamp(filtered_log[i + 1])
        heartbeat = (next_time - current_time).total_seconds()

        if heartbeat < 0:
            heartbeat += 24 * 60 * 60
        error_time = next_time.strftime("%H:%M:%S")

        if 31 < heartbeat < 33:
            logging.warning(
                f"Heartbeat = {heartbeat:.0f} sec, Time = {error_time}"
            )

        elif heartbeat >= 33:
            logging.error(
                f"Heartbeat = {heartbeat:.0f} sec, Time = {error_time}"
            )

def main():
    filtered_log = get_filtered_log()
    check_heartbeat(filtered_log)
    print("Analysis completed.")


main()