<!-- image -->

## 1 T

## Agenda

- What is OWASP Top 10 Project?
- What have been changed since first release in 2023?
- What have been changed since last reales this November?
- Brief overview of all current findings

<!-- image -->

## What is OWASP

- A global nonprofit focused on improving software security.
- Founded in 2001 by security practitioners.
- Known for open, free security resources: Top 10, ASVS, Cheat Sheets, ZAP, etc.
- Community-driven: thousands of volunteers, local chapters, and projects.
- Goal: make security transparent, practical, and built into how software is made.

## What is OWASP Top 10

- A community-driven list of the most critical web application security risks .
- Updated every few years based on real-world data and industry feedback.
- Helps organizations prioritize what actually gets attacked , not theoretical flaws.
- Used globally as a baseline standard for secure development and assessments.
- Not a compliance checklist, but a minimum bar for application security.

## Comparison 2003 until 2013

| OWASP Top Ten Entries (Unordered)             | Releases   | Releases   | Releases   | Releases   | Releases   |
|-----------------------------------------------|------------|------------|------------|------------|------------|
|                                               | 2003       | 2004       | 2007       | 2010       | 2013       |
| Unvalidated Input                             | A1         | A1[9]      |            | x          | X          |
| Buffer Overflows                              | A5         | A5         | X          | x          | X          |
| Denial of Service                             | X          | A9[2]      | X          | X          | X          |
| Injection                                     | A6         | A6[3]      | A2         | A1[10]     | A1         |
| Cross Site Scripting (XSS)                    | A4         | A4         | A1         | A2         | A3         |
| Broken Authentication and Session Management  | A3         | A3         | A7         | A3         | A2         |
| InsecureDirectObjectReference                 |            | A2         | A4[11]     | A4         | A4         |
| Cross Site Request Forgery (CSRF)             | x          |            | A5         | A5         | A8         |
| Security Misconfiguration                     | A10        | A10[3][5]  | X          | A6         | A5         |
| Missing Functional Level Access Control       | A2         | A2[1]      | A10[13]    | A8         | A7[16]     |
| Unvalidated Redirects and Forwards            | x          | x          | x          | A10        | A10        |
| Information Leakage and ImproperErrorHandling | A7         | A7[14][4]  | A6         | A6[8]      | X          |
| Malicious File Execution                      | x          | X          | A3         | A6[8]      | X          |
| Sensitive Data Exposure                       | A8         | A8[6][5]   | A8         | A7         | A6[17]     |
| Insecure Communications                       | x          | A10        | A9[7]      | A9         | X          |
| Remote AdministrationFlaws                    | A9         |            | X          | x          | X          |
| Using Known Vulnerable Components             | X          | X          | X          | X          | A9[18][19] |

## 2013 vs 2017

| A1 - Injection A2 - Broken Authentication and Session Management A3 - Cross-Site Scripting (XSS) A4 - Insecure Direct Object References [Merged + A7] A5 - Security Misconfiguration A6 - Sensitive Data Exposure A7 - Missing Function Level Access Control [Merged + A4] A8 - Cross-Site Request Forgery (CSRF) A9 - Using Components with Known Vulnerabilities A10 - Unvalidated Redirects and Forwards   | A1 - Injection A2 - Broken Authentication A3 - Sensitive Data Exposure A4 - XML External Entities (XXE) [NEW] >A5 - Broken Access Control [MERGED] A6 - Security Misconfiguration A7 - Cross-Site Scripting (XSS) A8 - Insecure Deserialization [NEW, COMMUNITY] A9 - Using Components with Known Vulnerabilities A10 - Insufficient Logging & Monitoring [NEW, CoMMUNITY]   |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

Source: https://www.owasp.org/images/7/72/0WASP\_Top\_10-2017\_%28en%29.pdf.pdf

<!-- image -->

## 2017 vs 2021

<!-- image -->

<!-- image -->

## 2021 vs 2025

<!-- image -->

<!-- image -->

## A01:2025 - Broken Access Control

- Violation of the principle of least privilege.
- Bypassing access control checks by modifying the URL.
- Permitting viewing or editing someone else's account.
- Accessing API with missing access controls for POST, PUT and DELETE.
- Elevation of privilege. Acting as a user without being logged in or acting as an admin when logged in as a user.
- Metadata manipulation, such as replaying or tampering with a JSON Web Token (JWT).

<!-- image -->

<!-- image -->

9

## A01:2025 - Prevention

- Except for public resources, deny by default.
- Model access controls should enforce record ownership.
- Implement access control mechanisms once and re-use them.
- Unique application business limit requirements should be enforced by domain models.
- Log access control failures, alert admins.
- Disable web server directory listing.
- Rate limit API and controller access to minimize the harm.

<!-- image -->

<!-- image -->

## A02:2025 - Security Misconfiguration

- Missing appropriate security hardening.
- Default accounts and their passwords are still used.
- Unnecessary features are enabled or installed.
- Error handling reveals stack traces.
- The security settings in the servers and application frameworks are not set to secure values.
- For upgraded systems, the latest security features are disabled.
- The server does not send security headers or directives.
- The software is out of date or vulnerable

<!-- image -->

<!-- image -->

## A02:2025 - Prevention

- A repeatable hardening process makes it fast and easy to deploy another environment that is appropriately locked down.
- A task to review and update the configurations appropriate to all security notes, updates, and patches.
- Remove or do not install unused features and frameworks.
- A segmented application architecture provides effective and secure separation between components or tenants.

<!-- image -->

An automated process to verify the effectiveness of the configurations and settings in all environments.

- Sending security directives to clients, e.g., Security Headers.

<!-- image -->

## A03:2025 - Software Supply Chain Failures

- If you do not know the versions of all components you use.
- If you do not scan for vulnerabilities regularly.
- If the software is vulnerable, unsupported, or out of date.
- If you do not fix or upgrade the underlying platform, frameworks, and dependencies in a risk-based, timely fashion.
- If you do not secure the components configurations.
- If software developers do not test the compatibility of updated, upgraded, or patched libraries.

<!-- image -->

13

<!-- image -->

## A03:2025 - Prevention

- Remove unused dependencies, unnecessary features, components, files, and documentation.
- Only obtain components from official sources over secure links.
- Continuously inventory the versions of both client-side and server-side components (e.g., frameworks, libraries) and their dependencies using tools like versions,
- Monitor for libraries and components that are unmaintained or do not create security patches for older versions.

<!-- image -->

14

<!-- image -->

## A04:2025 - Cryptographic Failures

- Is any data transmitted in clear text?
- Are default crypto keys in use?
- Are any old or weak cryptographic algorithms or protocols used either by default or in older code?
- Is encryption not enforced, e.g., are any HTTP headers (browser) security directives or headers missing?
- Are deprecated hash functions such as MD5 or SHA1 in use, or
- Is the received server certificate and the trust chain properly validated?
- are non-cryptographic hash functions used when cryptographic hash functions are needed? · Is randomness used for cryptographic purposes that was not designed to meet cryptographic requirements?

<!-- image -->

<!-- image -->

## A04:2025 - Prevention

- Classify data processed, stored, or transmitted by an application. Identify which data is sensitive according to privacy laws, regulatory requirements, or business needs.
- Make sure to encrypt all sensitive data at rest &amp; transit.
- Don't store sensitive data unnecessarily.
- Disable caching for response that contain sensitive data.
- Store passwords using strong adaptive and salted hashing functions with a work factor (delay factor), such as Argon2, scrypt, bcrypt or PBKDF2.
- Do not use legacy protocols such as FTP and SMTP for transporting sensitive data.
- Avoid deprecated cryptographic functions and padding schemes, such as MD5, SHA1, PKCS number 1 v1.5 .

<!-- image -->

<!-- image -->