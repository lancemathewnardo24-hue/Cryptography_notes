# CPT Recap – ValenFind LFI to Admin API

## Overview

This challenge involves exploiting a **Local File Inclusion (LFI)** vulnerability in the *ValenFind* web application to obtain sensitive configuration data, which is then used to access a protected **admin API endpoint** and extract the database.

---

## 1. Initial Reconnaissance

* We are given a **site URL**.
* Opening the site reveals an application called **ValenFind**.
* The site allows users to **log in** and view different user profiles.

### Notable Finding

* One user named **`cupid`** stands out.
* The profile description contains unusual text referencing **databases**, unlike other users.
* This suggests the profile may be important or vulnerable.

---

## 2. Traffic Interception with Burp Suite

* We open **Burp Suite** and enable the **Proxy (Intercept ON)**.
* We navigate to Cupid’s profile and forward the request.
* In **Proxy → HTTP history**, we inspect the server responses.

### Key Discovery

* While scrolling through a response, we find a comment indicating a **vulnerability**:

  > The `layout` parameter allows **Local File Inclusion (LFI)**

This confirms that user-controlled input is being used to load files on the server.

---

## 3. Exploiting the LFI Vulnerability

### Normal Behavior

* The profile page uses a parameter similar to:

```
layout=theme_modern.html
```

### Malicious Payload

* We modify the `layout` parameter to attempt LFI:

```
layout=/../../etc/passwd
```

* We send the modified request to **Repeater** for easier testing.

### Server Response

* The server returns an error indicating the file could not be found.
* However, the error message **leaks the full file path**:

```
/opt/Valenfind/templates/components/app.py
```

This is extremely valuable information.

---

## 4. Path Traversal to Application Source Code

* Using the leaked path, we progressively remove directories from the right:

```
/opt/Valenfind/templates/components/app.py
/opt/Valenfind/app.py
```

* We then request:

```
layout=/../../app.py
```

### Result

* The request succeeds and reveals the contents of **app.py**.

---

## 5. Sensitive Data Disclosure

Inside `app.py`, we find critical information:

```python
ADMIN_API_KEY = "CUPID_MASTER_KEY_XOXO"
```

* This is clearly an **administrator API key**.
* We save this key for later use.

### Additional Observation

* Scrolling further shows references to the **database** and admin-related routes.

---

## 6. Discovering the Admin API Endpoint

* While reviewing the source code, we find the endpoint:

```
/api/admin/export_db
```

* Attempting to access it directly fails due to missing authentication.

---

## 7. Understanding the Authentication Mechanism

From the source code:

```python
if auth_header == AUTHENTICATION_KEY:
```

* The application checks for a specific **HTTP header**.
* Above this logic, the required header name is defined as:

```
X-Valentine-Token
```

---

## 8. Authorized Database Export

Using the information gathered:

### Request Format

```
GET /api/admin/export_db
X-Valentine-Token: CUPID_MASTER_KEY_XOXO
```

* We send this request using **Burp Repeater**.

### Result

* The server accepts the request.
* The **database is successfully exported**, revealing the final key / flag.

---

## 9. Attack Chain Summary

1. Reconnaissance reveals a suspicious user (Cupid)
2. Burp Suite interception exposes an LFI vulnerability
3. LFI leaks internal file paths
4. Path traversal allows reading `app.py`
5. Admin API key is extracted
6. Admin endpoint is discovered
7. Custom authentication header is identified
8. Database export is successfully accessed

---

## Key Concepts Used

* Local File Inclusion (LFI)
* Path Traversal
* Source Code Disclosure
* API Key Extraction
* Custom HTTP Header Authentication

---

## Lessons Learned

* Error messages can leak critical internal paths
* LFI vulnerabilities often lead to full application compromise
* Hardcoded secrets in source code are extremely dangerous
* Defense-in-depth is essential for admin APIs
