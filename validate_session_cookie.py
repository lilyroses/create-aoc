def get_session_cookie(SESSION_COOKIE_FILE):
    session_cookie = ""
    # user may have accidentally deleted cookie file
    if not os.path.exists(SESSION_COOKIE_FILE):
        with open(SESSION_COOKIE_FILE, "w") as f:
            f.write("")
    # open and read cookie file
    with open(SESSION_COOKIE_FILE, "r") as f:
        session_cookie = f.read().strip()
    return session_cookie



def validate_session_cookie(session_cookie):
    """Validate the session cookie within the SESSION_COOKIE_FILE.

    args: SESSION_COOKIE_FILE (str, path)
    returns: cookie_is_valid (Boolean value)
    """
    cookie_is_valid = False

    # cookie file returned an empty string
    if not session_cookie:
        return cookie_is_valid
    
    # cookie file is not empty
    # Test cookie for validity
    session = requests.Session()
    HEADERS = {
        "Cookie":f"session={SESSION_COOKIE}",
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36"
    }
    test_url = f"{ADVENT_OF_CODE_BASE_URL}/2015/day/1/input"
    response = session.get(test_url, headers=HEADERS)

    # cookie is valid
    if response.status_code == 200:
        cookie_is_valid = True

    return cookie_is_valid
