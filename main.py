import schedule
import time
from scrapers.leetcode import get_leetcode_contests
from scrapers.codechef import get_codechef_contests
from scrapers.gfg import get_gfg_contests
from scrapers.codeforces import get_codeforces_contests
from email_notifier import send_email

def job():
    # Example: LeetCode on Saturday and Sunday
    if time.strftime("%A") in ["Saturday", "Sunday"]:
        contests = get_leetcode_contests()
        if contests:
            send_email("LeetCode Contest Reminder", f"Upcoming contests: {', '.join(contests)}", "gt281203@gmail.com")

    # CodeChef on Wednesday
    if time.strftime("%A") == "Wednesday":
        contests = get_codechef_contests()
        if contests:
            send_email("CodeChef Contest Reminder", f"Upcoming contests: {', '.join(contests)}", "gt281203@gmail.com")

    # GFG and Codeforces daily
    gfg_contests = get_gfg_contests()
    if gfg_contests:
        send_email("GeeksforGeeks Contest Reminder", f"Upcoming contests: {', '.join(gfg_contests)}", "gt281203@gmail.com")

    codeforces_contests = get_codeforces_contests()
    if codeforces_contests:
        send_email("Codeforces Contest Reminder", f"Upcoming contests: {', '.join(codeforces_contests)}", "gt281203@gmail.com")

# Schedule for every day at 9 AM
schedule.every().day.at("9:00").do(job)

while True:
    schedule.run_pending()
    time.sleep(60)
