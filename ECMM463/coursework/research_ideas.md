# Memory Faults 
https://ieeexplore.ieee.org/stamp/stamp.jsp?tp=&arnumber=1199334


## arp spoofing
https://ieeexplore.ieee.org/stamp/stamp.jsp?tp=&arnumber=9396241
https://www.youtube.com/watch?v=CW0Mf9qGBOc&ab_channel=LoiLiangYang


# heart bleed

https://www.exploit-db.com/docs/49313
information disclosure or data leak vulnerability. Specifically, it can be considered a buffer over-read attack.


# cross sides scriptong
https://www.exploit-db.com/docs/18580

# ios jail break
https://ieeexplore.ieee.org/document/7774861


# buffer overflow
https://www.researchgate.net/publication/349880942_The_Buffer_Overflow_Attack_and_How_to_Solve_Buffer_Overflow_in_Recent_Research
https://www.exploit-db.com/docs/18346


# cors attacck 
https://www.exploit-db.com/docs/45906

What is CORS?
CORS stands for Cross-Origin Resource Sharing.
It is a security feature implemented by web browsers to control how web pages can request resources (like APIs, images, or scripts) from domains other than the one that served the web page.
Purpose: It restricts web pages from making requests to different domains unless the target domain allows it by including specific headers (like Access-Control-Allow-Origin).
What is a CORS Attack?
CORS attack occurs when misconfigured CORS settings allow malicious websites or scripts to bypass these security controls.
Attackers can abuse weak CORS policies to send authenticated requests to sensitive APIs from an attacker's domain and potentially steal data or perform unauthorized actions.
Example: If an API allows Access-Control-Allow-Origin: * without restrictions, it might allow any malicious site to access sensitive user data.
Is a CORS Attack Dangerous and Why?
Yes, it is dangerous, particularly if sensitive APIs are exposed without proper restrictions.
If CORS is poorly configured, attackers can:
Steal sensitive user data by tricking the browser into sending authenticated requests (like session cookies or tokens) to a vulnerable API.
Perform unauthorized actions on behalf of a user by exploiting their credentials during an active session.
Severity: The danger lies in how this attack can bypass browser security mechanisms, making it a serious issue for web applications with sensitive data.