from datetime import datetime

def analyze_heartbeat_log(input_file='hblog.txt', output_file='hb_test.log'):
    key = "Key TSTFEED0300|7E3E|0400"
    timestamps = []

    # 1. Read the file and filter the required lines
    with open(input_file, 'r', encoding='utf-8') as f:
        for line in f:
            if key in line:
                # Find the time after 'Timestamp '
                ts_index = line.find("Timestamp ")
                if ts_index != -1:
                    time_str = line[ts_index + len("Timestamp "):ts_index + len("Timestamp ") + 8]
                    try:
                        ts = datetime.strptime(time_str, "%H:%M:%S")
                        timestamps.append((ts, line.strip()))
                    except ValueError:
                        # Skip if time is invalid
                        continue

    # 2. Analyze the difference between consecutive timestamps
    with open(output_file, 'w', encoding='utf-8') as out:
        for i in range(len(timestamps) - 1):
            current_ts, current_line = timestamps[i]
            next_ts, next_line = timestamps[i + 1]

            # Handle midnight rollover
            if next_ts < current_ts:
                next_ts = next_ts.replace(day=current_ts.day + 1)

            diff_seconds = abs((current_ts - next_ts).total_seconds())

            # Logging rules
            if 31 < diff_seconds < 33:
                out.write(
                    f"WARNING at {current_ts.time()} "
                    f"(diff={diff_seconds}s)\nLine: {current_line}\n\n"
                )
            elif diff_seconds >= 33:
                out.write(
                    f"ERROR at {current_ts.time()} "
                    f"(diff={diff_seconds}s)\nLine: {current_line}\n\n"
                )

    print(f"Analysis completed. Result saved to {output_file}")

# Run the function
if __name__ == "__main__":
    analyze_heartbeat_log('hblog.txt', 'hb_test.log')
