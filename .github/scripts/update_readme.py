import os
from datetime import datetime, timezone, timedelta

README_PATH = "README.md"
PROBLEM_DIR = "problems/python"  # ← あなたの環境に合わせて
LOG_START = "<!-- log:start -->"
LOG_END = "<!-- log:end -->"

# JSTのタイムゾーンを定義（+09:00）
JST = timezone(timedelta(hours=9))

def get_logged_files(lines):
    logged = set()
    for line in lines:
        if '](' in line:
            path = line.strip().split('](')[-1].rstrip(')')
            logged.add(path)
    return logged

def main():
    with open(README_PATH, "r", encoding="utf-8") as f:
        lines = f.readlines()

    start = next(i for i, line in enumerate(lines) if LOG_START in line) + 1
    end = next(i for i, line in enumerate(lines) if LOG_END in line)

    logged_paths = get_logged_files(lines[start:end])
    new_logs = []

    for filename in sorted(os.listdir(PROBLEM_DIR)):
        if filename.endswith(".py"):
            path = f"{PROBLEM_DIR}/{filename}"
            if path not in logged_paths:
                # ファイルの最終更新日時を取得（秒 → datetime）→ JST に変換
                mod_timestamp = os.path.getmtime(path)
                mod_time_jst = datetime.fromtimestamp(mod_timestamp, JST)
                formatted_time = mod_time_jst.strftime('%Y-%m-%d %H:%M')

                # ログ行を作成
                log_line = f"- {formatted_time}: [{filename}]({path})\n"
                new_logs.append(log_line)

    if not new_logs:
        print("No new problems to log.")
        return

    new_lines = lines[:start] + new_logs + lines[end:]
    with open(README_PATH, "w", encoding="utf-8") as f:
        f.writelines(new_lines)

    print(f"Logged {len(new_logs)} new problem(s).")

if __name__ == "__main__":
    main()
