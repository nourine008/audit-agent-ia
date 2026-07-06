<!-- image -->

Home About ▼

Learn ▼

Access Content ▼

<!-- image -->

Community ▼

<!-- image -->

Search ▼

## CWE VIEW: Weaknesses in the 2025 CWE Top 25 Most Dangerous Software Weaknesses

View ID: 1435

Vulnerability Mapping:

Type:

Graph

PROHIBITED

## Objective

CWE entries in this view are listed in the 2025 CWE Top 25 Most Dangerous Software Weaknesses.

## Audience

| Stakeholder         | Description                                                                                                                                                                           |
|---------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Software Developers | By following the CWE Top 25, developers are able to significantly reduce the number of weaknesses that occur in their software.                                                       |
| Product Customers   | Customers can use the weaknesses in this view in order to formulate independent evidence of a claim by a product vendor to have eliminated / mitigated the most dangerous weaknesses. |
| Educators           | Educators can use this view to focus curriculum and teachings on the most dangerous weaknesses.                                                                                       |

## Relationships

The following graph shows the tree-like relationships between weaknesses that exist at different levels of abstraction. At the highest level, categories and pillars exist to group weaknesses. Categories (which are not technically weaknesses) are special CWE entries used to group weaknesses that share a common characteristic. Pillars are weaknesses that are described in the most abstract fashion. Below these top-level entries are weaknesses are varying levels of abstraction. Classes are still very abstract, typically independent of any specific language or technology. Base level weaknesses are used to present a more specific type of weakness. A variant is a weakness that is described at a very low level of detail, typically limited to a specific language or technology. A chain is a set of weaknesses that must be reachable consecutively in order to produce an exploitable vulnerability. While a composite is a set of weaknesses that must all be present simultaneously in order to produce an exploitable vulnerability.

## Expand All | Collapse All

## 1435 - Weaknesses in the 2025 CWE Top 25 Most Dangerous Software Weaknesses

- [-Improper Neutralization of Input During Web Page Generation ('Cross-site Scripting') - (79) B](https://cwe.mitre.org/data/definitions/79.html)
- [-Improper Neutralization of Special Elements used in an SQL Command ('SQL Injection') - (89) B](https://cwe.mitre.org/data/definitions/89.html)
- [-Cross-Site Request Forgery (CSRF) - (352)](https://cwe.mitre.org/data/definitions/352.html)
- [-Missing Authorization - (862)](https://cwe.mitre.org/data/definitions/862.html)
- [-Out-of-bounds Write - (787) B](https://cwe.mitre.org/data/definitions/787.html)
- [-Improper Limitation of a Pathname to a Restricted Directory ('Path Traversal') - (22) B](https://cwe.mitre.org/data/definitions/22.html)
- [-Use After Free - (416)](https://cwe.mitre.org/data/definitions/416.html)
- [-Out-of-bounds Read - (125) B](https://cwe.mitre.org/data/definitions/125.html)
- -B
- [Improper Neutralization of Special Elements used in an OS Command ('OS Command Injection') -](https://cwe.mitre.org/data/definitions/78.html)

[(78)](https://cwe.mitre.org/data/definitions/78.html)

- [-Improper Control of Generation of Code ('Code Injection') - (94) B](https://cwe.mitre.org/data/definitions/94.html)
- [-Buffer Copy without Checking Size of Input ('Classic Buffer Overflow') - (120) B](https://cwe.mitre.org/data/definitions/120.html)
- [-Unrestricted Upload of File with Dangerous Type - (434) B](https://cwe.mitre.org/data/definitions/434.html)
- [-NULL Pointer Dereference - (476) B](https://cwe.mitre.org/data/definitions/476.html)
- [-Stack-based Buffer Overflow - (121)](https://cwe.mitre.org/data/definitions/121.html)
- [-Deserialization of Untrusted Data - (502) B](https://cwe.mitre.org/data/definitions/502.html)
- [-Heap-based Buffer Overflow - (122)](https://cwe.mitre.org/data/definitions/122.html)
- [-Incorrect Authorization - (863)](https://cwe.mitre.org/data/definitions/863.html)
- [-Improper Input Validation - (20)](https://cwe.mitre.org/data/definitions/20.html)

-

- [Improper Access Control - (284)](https://cwe.mitre.org/data/definitions/284.html)
- [-Exposure of Sensitive Information to an Unauthorized Actor - (200)](https://cwe.mitre.org/data/definitions/200.html)
- [-Missing Authentication for Critical Function - (306) B](https://cwe.mitre.org/data/definitions/306.html)
- [-Server-Side Request Forgery (SSRF) - (918) B](https://cwe.mitre.org/data/definitions/918.html)
- [-Improper Neutralization of Special Elements used in a Command ('Command Injection') - (77) ?](https://cwe.mitre.org/data/definitions/77.html)
- [-Authorization Bypass Through User-Controlled Key - (639) B](https://cwe.mitre.org/data/definitions/639.html)
- [-Allocation of Resources Without Limits or Throttling - (770) B](https://cwe.mitre.org/data/definitions/770.html)

## Vulnerability Mapping Notes

Usage: PROHIBITED (this CWE ID must not be used to map to real-world vulnerabilities)

Reason:

View

Rationale:

This entry is a View. Views are not weaknesses and therefore inappropriate to describe the root causes of vulnerabilities.

## Comments:

Use this View or other Views to search and navigate for the appropriate weakness.

<!-- image -->

## View Components

## CWE-770: Allocation of Resources Without Limits or Throttling

## Weakness ID: 770

Vulnerability Mapping:

ALLOWED

Abstraction:

Base

## Description

The product allocates a reusable resource or group of resources on behalf of an actor without imposing any intended restrictions on the size or number of resources that can be allocated.

## Common Consequences

<!-- image -->

<!-- image -->

<!-- image -->

<!-- image -->

|                                         | something that does. When performing input validation, consider all potentially relevant properties, including length, type of input, the full range of acceptable values, missing or extra inputs, syntax, consistency across related fields, and conformance to business rules. As an example of business rule logic, "boat" may be syntactically valid because it only contains alphanumeric characters, but it is not valid if the input is only expected to contain colors such as "red" or "blue." Do not rely exclusively on looking for malicious or malformed inputs. This is likely to miss at least one undesirable input, especially if the code's environment changes. This can give attackers enough room to bypass the intended validation. However, denylists can be useful for detecting potential attacks or determining which inputs are so malformed that they should be rejected outright. Note: This will only be applicable to cases where user input can influence the size or frequency of resource allocations.   |
|-----------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Architecture and Design                 | For any security checks that are performed on the client side, ensure that these checks are duplicated on the server side, in order to avoid CWE-602. Attackers can bypass the client-side checks by modifying values after the checks have been performed, or by changing the client to remove the client-side checks entirely. Then, these modified values would be submitted to the server.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| Architecture and Design                 | Mitigation of resource exhaustion attacks requires that the target system either: recognizes the attack and denies that user further access for a given amount of time, typically by using increasing time delays uniformly throttles all requests in order to make it more difficult to consume resources more quickly than they can again be freed. The first of these solutions is an issue in itself though, since it may allow attackers to prevent the use of the system by a particular valid user. If the attacker impersonates the valid user, they may be able to prevent the user from accessing the server in question. The second solution can be difficult to effectively institute -- and even when properly done, it does not provide a full solution. It simply requires more resources on the part of the attacker.                                                                                                                                                                                                       |
| Architecture and Design                 | Ensure that protocols have specific limits of scale placed on them.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| Architecture and Design; Implementation | If the program must fail, ensure that it fails gracefully (fails closed). There may be a temptation to simply let the program fail poorly in cases such as low memory conditions, but an attacker may be able to assert control before the software has fully exited. Alternately, an uncontrolled failure could cause cascading problems with other downstream components; for example, the program could send a signal to a downstream process so the process immediately knows that a problem has occurred and has a better chance of recovery. Ensure that all failures in resource allocation place the system into a safe posture.                                                                                                                                                                                                                                                                                                                                                                                                    |
| Operation; Architecture and Design      | Strategy: Resource Limitation Use quotas or other resource-limiting settings provided by the operating system or environment. For example, when managing system resources in POSIX, setrlimit() can be used to set limits for certain types of resources, and getrlimit() can determine how many resources are available. However, these functions are not available on all operating systems. When the current levels get close to the maximum that is defined for the application (see CWE-770), then limit the allocation of further resources to privileged users; alternately, begin releasing resources for less-privileged users. While this mitigation may protect the system from attack, it will not necessarily stop attackers from adversely impacting other users. Ensure that the application performs the appropriate error checks and error handling in case resources become unavailable (CWE-703).                                                                                                                        |

Relationships

Relevant to the view "Research Concepts" (View-1000)

<!-- image -->

<!-- image -->

| Nature    | Type   |   ID | Name                                                                   |
|-----------|--------|------|------------------------------------------------------------------------|
| ChildOf   |        |  400 | Uncontrolled Resource Consumption                                      |
| ChildOf   |        |  665 | Improper Initialization                                                |
| ParentOf  |        |  774 | Allocation of File Descriptors or Handles Without Limits or Throttling |
| ParentOf  |        |  789 | Memory Allocation with Excessive Size Value                            |
| ParentOf  |        | 1325 | Improperly Controlled Sequential Memory Allocation                     |
| CanFollow |        |   20 | Improper Input Validation                                              |

- Relevant to the view "Software Development" (View-699)
- Relevant to the view "Weaknesses for Simplified Mapping of Published Vulnerabilities" (View1003)
- Relevant to the view "Architectural Concepts" (View-1008)

```
Nature Type ID Name MemberOf 399 Resource Management Errors MemberOf 840 Business Logic Errors
```

```
Nature Type ID Name ChildOf 400
```

Uncontrolled Resource Consumption

```
Nature Type ID Name MemberOf 1011
```

## Modes Of Introduction

```
Phase Note Architecture and Design OMISSION: This weakness is caused by missing a security tactic during the architecture and design phase. Implementation Operation System Configuration
```

- Applicable Platforms

Languages Class: Not Language-Specific (Often Prevalent) Technologies Class: Not Technology-Specific (Undetermined Prevalence)

- Likelihood Of Exploit

High

- Demonstrative Examples

Example 1

This code allocates a socket and forks each time it receives a new connection.

```
(bad code) Example Language: C sock=socket(AF_INET, SOCK_STREAM, 0); while (1) { newsock=accept(sock, ...); printf("A connection has been accepted\n"); pid = fork(); }
```

The program does not track how many connections have been made, and it does not limit the number of connections. Because forking is a relatively expensive operation, an attacker would be able to cause the system to run out of CPU, processes, or memory by making a large number of connections. Alternatively, an attacker could consume all available connections, preventing others from accessing the system remotely.

## Example 2

In the following example a server socket connection is used to accept a request to store data on the local file system using a specified filename. The method openSocketConnection establishes a server socket to accept requests from a client. When a client establishes a connection to this service the getNextMessage method is first used to retrieve from the socket the name of the file to store the data, the openFileToWrite method will validate the filename and open a file to write to on the local file system. The getNextMessage is then used within a while loop to continuously read data from the socket and output the data to the file until there is no longer any data from the socket.

```
(bad code) Example Language: C int writeDataFromSocketToFile(char *host, int port) { char filename[FILENAME_SIZE]; char buffer[BUFFER_SIZE]; int socket = openSocketConnection(host, port); if (socket < 0) { printf("Unable to open socket connection"); return(FAIL); } if (getNextMessage(socket, filename, FILENAME_SIZE) > 0) { if (openFileToWrite(filename) > 0) { hil ( tN tM ( k t b ff BUFFER SIZE) 0){
```

```
Authorize Actors
```

```
while (getNextMessage(socket, buffer, BUFFER_SIZE) > 0){ if (!(writeToFile(buffer) > 0)) break; } } closeFile(); } closeSocket(socket); }
```

This example creates a situation where data can be dumped to a file on the local file system without any limits on the size of the file. This could potentially exhaust file or disk resources and/or limit other clients' ability to access the service.

## Example 3

In the following example, the processMessage method receives a two dimensional character array containing the message to be processed. The two-dimensional character array contains the length of the message in the first character array and the message body in the second character array. The getMessageLength method retrieves the integer value of the length from the first character array. After validating that the message length is greater than zero, the body character array pointer points to the start of the second character array of the twodimensional character array and memory is allocated for the new body character array.

```
(bad code) Example Language: C /* process message accepts a two-dimensional character array of the form [length][body] containing the message to be processed */ int processMessage(char **message) { char *body; int length = getMessageLength(message[0]); if (length > 0) { body = &message[1][0]; processMessageBody(body); return(SUCCESS); } else { printf("Unable to process message; invalid message length"); return(FAIL); } }
```

This example creates a situation where the length of the body character array can be very large and will consume excessive memory, exhausting system resources. This can be avoided by restricting the length of the second character array with a maximum length check

Also, consider changing the type from 'int' to 'unsigned int', so that you are always guaranteed that the number is positive. This might not be possible if the protocol specifically requires allowing negative values, or if you cannot control the return value from getMessageLength(), but it could simplify the check to ensure the input is positive, and eliminate other errors such as signed-to-unsigned conversion errors (CWE-195) that may occur elsewhere in the code.

```
(good code) Example Language: C unsigned int length = getMessageLength(message[0]); if ((length > 0) && (length < MAX_LENGTH)) {...}
```

## Example 4

In the following example, a server object creates a server socket and accepts client connections to the socket. For every client connection to the socket a separate thread object is generated using the ClientSocketThread class that handles request made by the client through the socket.

```
(bad code) Example Language: Java public void acceptConnections() { try { ServerSocket serverSocket = new ServerSocket(SERVER_PORT); int counter = 0; boolean hasConnections = true; while (hasConnections) { Socket client = serverSocket.accept(); Thread t = new Thread(new ClientSocketThread(client)); t tN ( li t tI tAdd () tH tN () " " t )
```

```
t.setName(client.getInetAddress().getHostName() + ":" + counter++); t.start(); } serverSocket.close(); } catch (IOException ex) {...} }
```

In this example there is no limit to the number of client connections and client threads that are created. Allowing an unlimited number of client connections and threads could potentially overwhelm the system and system resources.

The server should limit the number of client connections and the client threads that are created. This can be easily done by creating a thread pool object that limits the number of threads that are generated.

```
(good code) Example Language: Java public static final int SERVER_PORT = 4444; public static final int MAX_CONNECTIONS = 10; ... public void acceptConnections() { try { ServerSocket serverSocket = new ServerSocket(SERVER_PORT); int counter = 0; boolean hasConnections = true; while (hasConnections) { hasConnections = checkForMoreConnections(); Socket client = serverSocket.accept(); Thread t = new Thread(new ClientSocketThread(client)); t.setName(client.getInetAddress().getHostName() + ":" + counter++); ExecutorService pool = Executors.newFixedThreadPool(MAX_CONNECTIONS); pool.execute(t); } serverSocket.close(); } catch (IOException ex) {...} }
```

## Example 5

An unnamed web site allowed a user to purchase tickets for an event. A menu option allowed the user to purchase up to 10 tickets, but the back end did not restrict the actual number of tickets that could be purchased.

```
Example 5 References: [REF-667] Rafal Los. "Real-Life Example of a 'Business Logic Defect' (Screen Shots!)". 2011. <http://h30501.www3.hp.com/t5/Following-the-White-Rabbit-A/Real-Life-Example-of-a-Business-LogicDefect-Screen-Shots/ba-p/22581>.
```

## Example 6

Here the problem is that every time a connection is made, more memory is allocated. So if one just opened up more and more connections, eventually the machine would run out of memory.

```
(bad code) Example Language: C bar connection() { foo = malloc(1024); return foo; } endConnection(bar foo) { free(foo); } int main() { while(1) { foo=connection(); } endConnection(foo) }
```

## Memberships

<!-- image -->

## Vulnerability Mapping Notes

<!-- image -->

## Notes

## Relationship

This entry is different from uncontrolled resource consumption (CWE-400) in that there are other weaknesses that are related to inability to control resource consumption, such as holding on to a resource too long after use, or not correctly keeping track of active resources so that they can be managed and released when they are finished (CWE-771).

## Theoretical

Vulnerability theory is largely about how behaviors and resources interact. "Resource exhaustion" can be regarded as either a consequence or an attack, depending on the perspective. This entry is an attempt to reflect one of the underlying weaknesses that enable these attacks (or consequences) to take place.

## Content History

| Submissions Submission Date 2009-05-13 (CWE 1.4, 2009-05-27)   | Submitter CWE Content Team                                                                                                 | Organization MITRE   |
|----------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------|----------------------|
| Contributions                                                  |                                                                                                                            |                      |
| Contribution Date                                              | Contributor                                                                                                                | Organization         |
| 2023-11-14 (CWE 4.14, 2024-02-29)                              | participants in the CWE ICS/OT SIG 62443 Mapping Fall Workshop Contributed or reviewed taxonomy mappings for ISA/IEC 62443 |                      |
| Modifications                                                  | Modifications                                                                                                              | Modifications        |

## CWE-639: Authorization Bypass Through User-Controlled Key

Weakness ID: 639

Vulnerability Mapping:

Abstraction:

Base

## Description

The system's authorization functionality does not prevent one user from gaining access to another user's data or record by modifying the key value identifying the data.

## Extended Description

Retrieval of a user record occurs in the system based on some key value that is under user control. The key would typically identify a user-related record stored in the system and would be used to lookup that record for presentation to the user. It is likely that an attacker would have to be an authenticated user in the system. However, the authorization process would not properly check the data access operation to ensure that the

ALLOWED

authenticated user performing the operation has sufficient entitlements to perform the requested data access, hence bypassing any other authorization checks present in the system.

For example, attackers can look at places where user specific data is retrieved (e.g. search screens) and determine whether the key for the item being looked up is controllable externally. The key may be a hidden field in the HTML form field, might be passed as a URL parameter or as an unencrypted cookie variable, then in each of these cases it will be possible to tamper with the key value.

One manifestation of this weakness is when a system uses sequential or otherwise easily-guessable session IDs that would allow one user to easily switch to another user's session and read/modify their data.

| Phase(s)                                | Mitigation                                                                                                                                                                                                  |
|-----------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Architecture and Design                 | For each and every data access, ensure that the user has sufficient privilege to access the record that is being requested.                                                                                 |
| Architecture and Design; Implementation | Make sure that the key that is used in the lookup of a specific user's record is not controllable externally by the user or that any tampering can be detected.                                             |
| Architecture and Design                 | Use encryption in order to make it more difficult to guess other legitimate values of the key or associate a digital signature with the key so that the server can verify that there has been no tampering. |

| Nature   | Type   |   ID | Name                  |
|----------|--------|------|-----------------------|
| MemberOf |        |  840 | Business Logic Errors |
| MemberOf |        | 1212 | Authorization Errors  |

Nature

Type

ID

Name

ChildOf

863

Incorrect Authorization

Nature

Type

ID

Name

ChildOf

284

Improper Access Control

<!-- image -->

<!-- image -->

## Likelihood Of Exploit

High

## Demonstrative Examples

## Example 1

The following code uses a parameterized statement, which escapes metacharacters and prevents SQL injection vulnerabilities, to construct and execute a SQL query that searches for an invoice matching the specified identifier [1]. The identifier is selected from a list of all invoices associated with the current authenticated user.

```
(bad code) Example Language: C# ... conn = new SqlConnection(_ConnectionString); conn.Open(); int16 id = System.Convert.ToInt16(invoiceID.Text); SqlCommand query = new SqlCommand( "SELECT * FROM invoices WHERE id = @id", conn); query.Parameters.AddWithValue("@id", id); SqlDataReader objReader = objCommand.ExecuteReader(); ...
```

The problem is that the developer has not considered all of the possible values of id. Although the interface generates a list of invoice identifiers that belong to the current user, an attacker can bypass this interface to request any desired invoice. Because the code in this example does not check to ensure that the user has permission to access the requested invoice, it will display any invoice, even if it does not belong to the current user.

| Submissions Submission Date 2008-01-30 (CWE Draft 8, 2008-01-30)   | Submitter Evgeny Lebanidze                                         | Organization Cigital   |
|--------------------------------------------------------------------|--------------------------------------------------------------------|------------------------|
| Contributions Contribution Date                                    |                                                                    |                        |
|                                                                    | Contributor                                                        |                        |
| 2024-08-09 (CWE 4.20, 2026-04-30)                                  |                                                                    | Organization           |
|                                                                    | Mateus Godinho Pantoja Suggested corrections to use of IDOR versus |                        |
| Modifications                                                      | BOLA                                                               |                        |
| Previous Entry                                                     | Names                                                              |                        |

<!-- image -->

## CWE-120: Buffer Copy without Checking Size of Input ('Classic Buffer Overflow')

Weakness ID: 120

Vulnerability Mapping: (with careful review of mapping notes) ALLOWED

Abstraction:

Base

## Description

The product copies an input buffer to an output buffer without verifying that the size of the input buffer is less than the size of the output buffer.

## Common Consequences

<!-- image -->

## Potential Mitigations

<!-- image -->

<!-- image -->

|                                  | When using functions that accept a number of bytes to copy, such as strncpy(), be aware that if the destination buffer size is equal to the source buffer size, it may not NULL-terminate the string. Check buffer boundaries if accessing the buffer in a loop and make sure there is no danger of writing past the allocated space. If necessary, truncate all input strings to a reasonable length before passing them to the copy and concatenation functions.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
|----------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Implementation                   | Strategy: Input Validation Assume all input is malicious. Use an "accept known good" input validation strategy, i.e., use a list of acceptable inputs that strictly conform to specifications. Reject any input that does not strictly conform to specifications, or transform it into something that does. When performing input validation, consider all potentially relevant properties, including length, type of input, the full range of acceptable values, missing or extra inputs, syntax, consistency across related fields, and conformance to business rules. As an example of business rule logic, "boat" may be syntactically valid because it only contains alphanumeric characters, but it is not valid if the input is only expected to contain colors such as "red" or "blue." Do not rely exclusively on looking for malicious or malformed inputs. This is likely to miss at least one undesirable input, especially if the code's environment changes. This can give attackers enough room to bypass the intended validation. However, denylists can be useful for detecting potential attacks or determining which inputs are so malformed that they should be rejected outright.                                                                                       |
| Architecture and Design          | For any security checks that are performed on the client side, ensure that these checks are duplicated on the server side, in order to avoid CWE-602. Attackers can bypass the client-side checks by modifying values after the checks have been performed, or by changing the client to remove the client-side checks entirely. Then, these modified values would be submitted to the server.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| Operation; Build and Compilation | Strategy: Environment Hardening Run or compile the software using features or extensions that randomly arrange the positions of a program's executable and libraries in memory. Because this makes the addresses unpredictable, it can prevent an attacker from reliably jumping to exploitable code. Examples include Address Space Layout Randomization (ASLR) [REF-58] [REF- 60] and Position-Independent Executables (PIE) [REF-64]. Imported modules may be similarly realigned if their default memory addresses conflict with other modules, in a process known as "rebasing" (for Windows) and "prelinking" (for Linux) [REF-1332] using randomly generated addresses. ASLR for libraries cannot be used in conjunction with prelink since it would require relocating the libraries at run-time, defeating the whole purpose of prelinking. For more information on these techniques see D3-SAOR (Segment Address Offset Randomization) from D3FEND [REF-1335]. Effectiveness: Defense in Depth Note: These techniques do not provide a complete solution. For instance, exploits frequently use a bug that discloses memory addresses in order to maximize reliability of code execution [REF-1337]. It has also been shown that a side-channel attack can bypass ASLR [REF-1333]. |
| Operation                        | Strategy: Environment Hardening Use a CPU and operating system that offers Data Execution Protection (using hardware NX or XD bits) or the equivalent techniques that simulate this feature in software, such as PaX [REF-60] [REF-61]. These techniques ensure that any instruction executed is exclusively at a memory address that is part of the code segment. For more information on these techniques see D3-PSEP (Process Segment Execution Prevention) from D3FEND [REF-1336]. Effectiveness: Defense in Depth Note: This is not a complete solution, since buffer overflows could be used to overwrite nearby variables to modify the software's state in dangerous ways. In addition, it cannot be used in cases in which self-modifying code is required. Finally, an attack could still cause a denial of service, since the typical response is to exit the application.                                                                                                                                                                                                                                                                                                                                                                                                        |
| Build and Compilation; Operation | Most mitigating technologies at the compiler or OS level to date address only a subset of buffer overflow problems and rarely provide complete protection against even that subset. It is good practice to implement strategies to increase the workload of an attacker, such as leaving the attacker to guess an unknown value that changes every program execution.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| Implementation                   | Replace unbounded copy functions with analogous functions that support length arguments, such as strcpy with strncpy. Create these if they are not available. Effectiveness: Moderate                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |

<!-- image -->

## Architecture and Design

## Architecture and Design; Operation

## Architecture and Design; Operation

## Relationships

## Relevant to the view "Research Concepts" (View-1000)

<!-- image -->

<!-- image -->

<!-- image -->

<!-- image -->

<!-- image -->

<!-- image -->

| Nature     | Type   |   ID | Name                                                           |
|------------|--------|------|----------------------------------------------------------------|
| ChildOf    |        |  787 | Out-of-bounds Write                                            |
| ParentOf   |        |  785 | Use of Path Manipulation Function without Maximum-sized Buffer |
| CanFollow  |        |  170 | Improper Null Termination                                      |
| CanFollow  |        |  231 | Improper Handling of Extra Values                              |
| CanFollow  |        |  416 | Use After Free                                                 |
| CanFollow  |        |  456 | Missing Initialization of a Variable                           |
| CanPrecede |        |  123 | Write-what-where Condition                                     |

- Relevant to the view "Software Development" (View-699)

Nature

MemberOf ID

[1218](https://cwe.mitre.org/data/definitions/1218.html)

Name

Memory Buffer Errors

Type

<!-- image -->

- Relevant to the view "Weaknesses for Simplified Mapping of Published Vulnerabilities" (View1003)
- Relevant to the view "CISQ Quality Measures (2020)" (View-1305)
- Relevant to the view "CISQ Data Protection Measures" (View-1340)
- Relevant to the view "Seven Pernicious Kingdoms" (View-700)

<!-- image -->

Nature

Type

ID

Name

ChildOf

119

Improper Restriction of Operations within the Bounds of a Memory Buffer

Nature

Type

ID

Name

ChildOf

787

Out-of-bounds Write

Nature

Type

ID

Name

ChildOf

787

Out-of-bounds Write

<!-- image -->

Nature

Type

ID

Name

ChildOf

20

Improper Input Validation

<!-- image -->

## Modes Of Introduction

<!-- image -->

Phase Note

Implementation

## Applicable Platforms

Note: This approach is still susceptible to calculation errors, including issues such as off-by-one errors (CWE193) and incorrectly calculating buffer lengths (CWE-131).

## Strategy: Enforcement by Conversion

When the set of acceptable objects, such as filenames or URLs, is limited or known, create a mapping from a set of fixed input values (such as numeric IDs) to the actual filenames or URLs, and reject all other inputs.

## Strategy: Environment Hardening

Run your code using the lowest privileges that are required to accomplish the necessary tasks [REF-76]. If possible, create isolated accounts with limited privileges that are only used for a single task. That way, a successful attack will not immediately give the attacker access to the rest of the software or its environment. For example, database applications rarely need to run as the database administrator, especially in day-to-day operations.

## Strategy: Sandbox or Jail

Run the code in a "jail" or similar sandbox environment that enforces strict boundaries between the process and the operating system. This may effectively restrict which files can be accessed in a particular directory or which commands can be executed by the software.

OS-level examples include the Unix chroot jail, AppArmor, and SELinux. In general, managed code may provide some protection. For example, java.io.FilePermission in the Java SecurityManager allows the software to specify restrictions on file operations.

This may not be a feasible solution, and it only limits the impact to the operating system; the rest of the application may still be subject to compromise. Be careful to avoid CWE-243 and other weaknesses related to jails.

## Effectiveness: Limited

Note: The effectiveness of this mitigation depends on the prevention capabilities of the specific sandbox or jail being used and might only help to reduce the scope of an attack, such as restricting the attacker to certain system calls or limiting the portion of the file system that can be accessed.

<!-- image -->

<!-- image -->

## Likelihood Of Exploit

High

Demonstrative Examples

## Example 1

The following code asks the user to enter their last name and then attempts to store the value entered in the last\_name array.

```
(bad code) Example Language: C char last_name[20]; printf ("Enter your last name: "); scanf ("%s", last_name);
```

The problem with the code above is that it does not restrict or limit the size of the name entered by the user. If the user enters "Very\_very\_long\_last\_name" which is 24 characters long, then a buffer overflow will occur since the array can only hold 20 characters total.

## Example 2

The following code attempts to create a local copy of a buffer to perform some manipulations to the data.

```
(bad code) Example Language: C void manipulate_string(char * string){ char buf[24]; strcpy(buf, string); ... }
```

However, the programmer does not ensure that the size of the data pointed to by string will fit in the local buffer and copies the data with the potentially dangerous strcpy() function. This may result in a buffer overflow condition if an attacker can influence the contents of the string parameter.

## Example 3

The code below calls the gets() function to read in data from the command line.

```
(bad code) Example Language: C char buf[24]; printf("Please enter your name and press <Enter>\n"); gets(buf); ... }
```

However, gets() is inherently unsafe, because it copies all input from STDIN to the buffer without checking size. This allows the user to provide a string that is larger than the buffer size, resulting in an overflow condition.

## Example 4

In the following example, a server accepts connections from a client and processes the client request. After accepting a client connection, the program will obtain client information using the gethostbyaddr method, copy the hostname of the client that connected to a local variable and output the hostname of the client to a log file.

```
(bad code) Example Language: C ... struct hostent *clienthp; char hostname[MAX_LEN]; // create server socket, bind to server address and listen on socket ... // t li t ti d t
```

```
Class: Memory-Unsafe (Undetermined Prevalence) C (Often Prevalent) C++ (Often Prevalent) Class: Assembly (Undetermined Prevalence)
```

```
// accept client connections and process requests int count = 0; for (count = 0; count < MAX_CONNECTIONS; count++) { int clientlen = sizeof(struct sockaddr_in); int clientsocket = accept(serversocket, (struct sockaddr *)&clientaddr, &clientlen); if (clientsocket >= 0) { clienthp = gethostbyaddr((char*) &clientaddr.sin_addr.s_addr, sizeof(clientaddr.sin_addr.s_addr), AF_INET); strcpy(hostname, clienthp->h_name); logOutput("Accepted client connection from host ", hostname); // process client request ... close(clientsocket); } } close(serversocket); ...
```

However, the hostname of the client that connected may be longer than the allocated size for the local hostname variable. This will result in a buffer overflow when copying the client hostname to the local variable using the strcpy method.

## Memberships

```
Nature Type ID Name MemberOf 722 OWASP Top Ten 2004 Category A1 - Unvalidated Input MemberOf 726 OWASP Top Ten 2004 Category A5 - Buffer Overflows MemberOf 741 CERT C Secure Coding Standard (2008) Chapter 8 - Characters and Strings (STR) MemberOf 802 2010 Top 25 - Risky Resource Management MemberOf 865 2011 Top 25 - Risky Resource Management MemberOf 875 CERT C++ Secure Coding Section 07 - Characters and Strings (STR) MemberOf 884 CWE Cross-section MemberOf 970 SFP Secondary Cluster: Faulty Buffer Access MemberOf 1129 CISQ Quality Measures (2016) - Reliability MemberOf 1131 CISQ Quality Measures (2016) - Security MemberOf 1161 SEI CERT C Coding Standard - Guidelines 07. Characters and Strings (STR) MemberOf 1399 Comprehensive Categorization: Memory Safety MemberOf 1435 Weaknesses in the 2025 CWE Top 25 Most Dangerous Software Weaknesses
```

## Vulnerability Mapping Notes

Usage

Reason

Rationale

Comments

## Notes

## Relationship

At the code level, stack-based and heap-based overflows do not differ significantly, so there usually is not a need to distinguish them. From the attacker perspective, they can be quite different, since different techniques are required to exploit them.

## Terminology

There is significant inconsistency regarding the "buffer overflow" term, which can have multiple interpretations and uses. Many people mean "writing past the end of a buffer." Others mean "writing past the end of a buffer, or before the beginning of a buffer." Still others might include "read" in the term.

## Other

A buffer overflow condition exists when a product attempts to put more data in a buffer than it can hold, or when it attempts to put data in a memory area outside of the boundaries of a buffer. The simplest type of error, and the most common cause of buffer overflows, is the "classic" case in which the product copies

## ALLOWED-WITH-REVIEW

(this CWE ID could be used to map to real-world vulnerabilities in limited situations requiring careful review)

Frequent Misuse

There are some indications that this CWE ID might be misused and selected simply because it mentions "buffer overflow" - an increasingly vague term. This CWE entry is only appropriate for "Buffer Copy" operations (not buffer reads), in which where there is no "Checking [the] Size of Input", and (by implication of the copy) writing past the end of the buffer.

If the vulnerability being analyzed involves out-of-bounds reads, then consider CWE-125 or descendants. For root cause analysis: if there is any input validation, consider children of CWE20 such as CWE-1284. If there is a calculation error for buffer sizes, consider CWE-131 or similar.

the buffer without restricting how much data is copied. Other variants exist, but the existence of a classic overflow strongly suggests that the programmer is not considering even the most basic of security protections.

## Content History

<!-- image -->

## CWE-352: Cross-Site Request Forgery (CSRF)

Weakness ID: 352 Vulnerability Mapping: (Structure: Composite ) ALLOWED

## Description

The web application does not, or cannot, sufficiently verify whether a request was intentionally provided by the user who sent the request, which could have originated from an unauthorized actor.

## Common Consequences

<!-- image -->

## Details

Scope: Confidentiality, Integrity, Availability, Non-Repudiation, Access Control

Gain Privileges or Assume Identity; Bypass Protection Mechanism; Read Application Data; Modify Application Data; DoS: Crash, Exit, or Restart The consequences will vary depending on the nature of the functionality that is vulnerable to CSRF. An attacker could trick a client into making an unintentional request to the web server via a URL, image load, XMLHttpRequest, etc., which would then be treated as an authentic request from the client - effectively performing any operations as the victim, leading to an exposure of data, unintended code execution, etc. If the victim is an administrator or privileged user, the consequences may include obtaining complete control over the web application - deleting or stealing data, uninstalling the product, or using it to launch other attacks against all of the product's users. Because the attacker has the identity of the victim, the scope of CSRF is limited only by the victim's privileges.

## Potential Mitigations

| Phase(s)                | Mitigation                                                                                                                                                                                                                                                                                                                                                                  |
|-------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Architecture and Design | Strategy: Libraries or Frameworks Use a vetted library or framework that does not allow this weakness to occur or provides constructs that make this weakness easier to avoid [REF-1482]. For example, use anti-CSRF packages such as the OWASP CSRFGuard. [REF-330] Another example is the ESAPI Session Management control, which includes a component for CSRF. [REF-45] |
| Implementation          | Ensure that the application is free of cross-site scripting issues (CWE-79), because most CSRF defenses can be bypassed using attacker-controlled script.                                                                                                                                                                                                                   |
| Architecture and Design | Generate a unique nonce for each form, place the nonce into the form, and verify the nonce upon receipt of the form. Be sure that the nonce is not predictable (CWE- 330). [REF-332] Note: Note that this can be bypassed using XSS (CWE-79).                                                                                                                               |

<!-- image -->

<!-- image -->

Modify Memory; Execute Unauthorized Code or Commands; Bypass Protection Mechanism; Other

## Scope: Integrity, Confidentiality, Availability, Access Control, Other

When the consequence is arbitrary code execution, this can often be used to subvert any other security service.

## Potential Mitigations

<!-- image -->

## Relationships

<!-- image -->

<!-- image -->

- Relevant to the view "Research Concepts" (View-1000)

Nature

Type

ID

Name

ChildOf

787

Out-of-bounds Write

ChildOf

788

Access of Memory Location After End of Buffer

## Modes Of Introduction

Phase

Note

Implementation

## Applicable Platforms

Languages

Class: Memory-Unsafe (Often Prevalent)

C (Often Prevalent)

C++ (Often Prevalent)

## Technologies

Class: Not Technology-Specific (Undetermined Prevalence)

- Likelihood Of Exploit

High

- Demonstrative Examples

Example 1

<!-- image -->

- Relevant to the view "CISQ Data Protection Measures" (View-1340)

```
Nature Type ID Name ChildOf 672
```

Operation on a Resource after Expiration or Release

```
Modes Of Introduction Phase Note Implementation Applicable Platforms Languages Class: Memory-Unsafe (Often Prevalent) C (Often Prevalent) C++ (Often Prevalent) Likelihood Of Exploit High Demonstrative Examples Example 1
```

The following example demonstrates the weakness.

```
(bad code) Example Language: C #include <stdio.h> #include <unistd.h> #define BUFSIZER1 512 #define BUFSIZER2 ((BUFSIZER1/2) - 8) int main(int argc, char **argv) { char *buf1R1; char *buf2R1; char *buf2R2; char *buf3R2; buf1R1 = (char *) malloc(BUFSIZER1); buf2R1 = (char *) malloc(BUFSIZER1); free(buf2R1); buf2R2 = (char *) malloc(BUFSIZER2); buf3R2 = (char *) malloc(BUFSIZER2); strncpy(buf2R1, argv[1], BUFSIZER1-1); free(buf1R1); free(buf2R2); free(buf3R2); }
```

## Example 2

The following code illustrates a use after free error:

```
(bad code) Example Language: C char* ptr = (char*)malloc (SIZE); if (err) { abrt = 1; free(ptr); } ... if (abrt) { logError("operation aborted before commit", ptr); }
```

When an error occurs, the pointer is immediately freed. However, this pointer is later incorrectly used in the logError function.

## Memberships

```
Nature Type ID Name MemberOf 398 7PK - Code Quality MemberOf 742 CERT C Secure Coding Standard (2008) Chapter 9 - Memory Management (MEM) MemberOf 808 2010 Top 25 - Weaknesses On the Cusp MemberOf 876 CERT C++ Secure Coding Section 08 - Memory Management (MEM) MemberOf 983 SFP Secondary Cluster: Faulty Resource Use
```

| MemberOf   |   1162 | SEI CERT C Coding Standard - Guidelines 08. Memory Management (MEM)   |
|------------|--------|-----------------------------------------------------------------------|
| MemberOf   |   1200 | Weaknesses in the 2019 CWE Top 25 Most Dangerous Software Errors      |
| MemberOf   |   1337 | Weaknesses in the 2021 CWE Top 25 Most Dangerous Software Weaknesses  |
| MemberOf   |   1350 | Weaknesses in the 2020 CWE Top 25 Most Dangerous Software Weaknesses  |
| MemberOf   |   1387 | Weaknesses in the 2022 CWE Top 25 Most Dangerous Software Weaknesses  |
| MemberOf   |   1399 | Comprehensive Categorization: Memory Safety                           |
| MemberOf   |   1425 | Weaknesses in the 2023 CWE Top 25 Most Dangerous Software Weaknesses  |
| MemberOf   |   1430 | Weaknesses in the 2024 CWE Top 25 Most Dangerous Software Weaknesses  |
| MemberOf   |   1435 | Weaknesses in the 2025 CWE Top 25 Most Dangerous Software Weaknesses  |

| Submissions                                              |                                                                                                                                                                      |              |
|----------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------|
| Submission Date                                          | Submitter                                                                                                                                                            | Organization |
| 2006-07-19 (CWE Draft 3, 2006-07-19)                     | 7 Pernicious Kingdoms                                                                                                                                                |              |
| Contributions                                            |                                                                                                                                                                      |              |
| Contribution Date                                        | Contributor                                                                                                                                                          | Organization |
| 2024-02-29                                               | Abhi Balakrishnan                                                                                                                                                    |              |
| (CWE 4.15, 2024-07-16) 2023-11-14 (CWE 4.14, 2024-02-29) | Provided diagram to improve CWE usability participants in the CWE ICS/OT SIG 62443 Mapping Fall Workshop Contributed or reviewed taxonomy mappings for ISA/IEC 62443 |              |
| 2022-06-28                                               | Anonymous External Contributor Suggested rephrase for extended description                                                                                           |              |

<!-- image -->