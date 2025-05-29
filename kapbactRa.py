import json

# ---------- CONFIG ----------
followers_file = "followers_1.json"
following_file = "following.json"
pending_requests_file = "pending_follow_requests.json"

# ---------- LOAD DATA ----------
with open(followers_file, 'r', encoding='utf-8') as f:
    followers_data = json.load(f)

with open(following_file, 'r', encoding='utf-8') as f:
    following_data = json.load(f)
    following_data = following_data.get("relationships_following", [])

with open(pending_requests_file, 'r', encoding='utf-8') as f:
    pending_data = json.load(f)
    pending_data = pending_data.get("relationships_follow_requests_sent", [])

# ---------- EXTRACT USERNAMES ----------
followers = {entry['string_list_data'][0]['value'] for entry in followers_data}
following = {entry['string_list_data'][0]['value'] for entry in following_data}
pending_requests = {entry['string_list_data'][0]['value'] for entry in pending_data}

# ---------- CALCULATE ----------
not_following_back = sorted(following - followers)

# ---------- DISPLAY ----------
print("\n📊 ΣΤΑΤΙΣΤΙΚΑ:")
print(f"➡️ Ακολουθείς: {len(following)}")
print(f"⬅️ Σε ακολουθούν: {len(followers)}")
print(f"⛔ Δεν σε ακολουθούν πίσω: {len(not_following_back)}")
print(f"⏳ Pending follow requests: {len(pending_requests)}")

print("\n📍 Δεν σε ακολουθούν πίσω:")
for user in not_following_back:
    print(f"- {user}")

print("\n🔄 Αιτήματα που περιμένουν:")
for user in sorted(pending_requests):
    print(f"- {user}")
input("AN KA was ~KapB.a.c.t.~sound~cloud.c.0.m")
