# Application Security and Development STIGs

**Date:** 2024-12-06

**Description:** This Security Technical Implementation Guide is published as a tool to improve the security of Department of Defense (DOD) information systems. The requirements are derived from the National Institute of Standards and Technology (NIST) 800-53 and related documents. Comments or proposed revisions to this document should be sent via e-mail to the following address: disa.stig_spt@mail.mil.

---

## The application must provide a capability to limit the number of logon sessions per user.

<span style="color:#ff8c00;font-size:150%;">Medium Severity</span>

### Description

Application management includes the ability to control the number of users and user sessions that utilize an application. Limiting the number of allowed users and sessions per user is helpful in limiting risks related to DoS attacks.

This requirement may be met via the application or by utilizing information system session control provided by a web server or other underlying solution that provides specialized session management capabilities.

If it has been specified that this requirement will be handled by the application, the capability to limit the maximum number of concurrent single user sessions must be designed and built into the application.

This requirement addresses concurrent sessions for individual system accounts and does not address concurrent sessions by single users via multiple system accounts.

The maximum number of concurrent sessions should be defined based upon mission needs and the operational environment for each system.

### Check Text

For production environments;  Review the system documentation, identify the number of application user logon sessions allowed per user, identify the methods utilized for user session management or have application administrator describe how the application implements user session management.

Utilize the management interface that is used to set the user session values, or examine configuration files in order to review user session configuration settings.

Ensure the number of sessions allowed per user is specified in accordance with the organizational requirements.

For development environments;  have the developer provide design documentation or demonstrate how the application is designed to limit the number of simultaneous user logon sessions.

If the application is not configured to limit the number of logon sessions per user as defined by the organization, this is a finding.

**Check ID:**  C-24057r493069_chk

### Fix Text 

Design and configure the application to specify the number of logon sessions that are allowed per user.

**Fix ID:**  F-24046r493070_fix

**Vulnerability ID:**  V-222387

**Rule ID:**  SV-222387r960735_rule

---

## The application must clear temporary storage and cookies when the session is terminated.

<span style="color:#ff8c00;font-size:150%;">Medium Severity</span>

### Description

Persistent cookies are a primary means by which a web application will store application state and user information.  Since HTTP is a stateless protocol, this persistence allows the web application developer to provide a robust and customizable user experience.

However, if a web application stores user authentication information within a persistent cookie or other temporary storage mechanism, this information can be stolen and used to compromise the users account.

Likewise, HTML 5 provides the developer with a client storage capability where application data larger than the 4K cookie size limit can be stored on the local client.  While this can be beneficial to the developer, this is considered insecure storage and should not be used for storing sensitive session or security tokens.  A cross site scripting attack can put this data at risk.

Web applications must clear sensitive data from files and storage areas on the client when the session is terminated.

### Check Text

Review application design documentation and interview application administrator to identify how the application makes use of temporary client storage and cookies.  Identify cookie and web storage locations on the client.  Clear all browser cookies and web cache.

Log on to the application and perform several standard operations, noting if the application ever prompts the user to accept a cookie. If prompted by the browser to save the user ID and password (decline to save the user ID and password), this is a finding. 

Log out of the application and close the browser. Reopen the browser and examine the stored cookies. The cookies displayed should be related to the application website.

The procedure to view cookies will vary according to the browser used. Some modern browsers are making use of SQLite databases to store cookie data so use of a SQLite db reader/browser may be required.

Open the cookies related to the application website and search for any identification or authentication information. While authentication information can vary on a per application basis, this is most often specified as "username=x", or "password=x".

If the web application prompts the user to save their password, or if a username or password value exists within a cookie or within local storage locations, even if hashed, this is a finding.

The application may use means other than cookies to store user information. If the reviewer detects an alternative mechanism for storing information locally, examine the data storage to ensure no authentication or other sensitive information is present.

**Check ID:**  C-24058r493072_chk

### Fix Text 

Design and configure the application to clear sensitive data from cookies and local storage when the user logs out of the application.

**Fix ID:**  F-24047r493073_fix

**Vulnerability ID:**  V-222388

**Rule ID:**  SV-222388r1043182_rule

---

## The application must automatically terminate the non-privileged user session and log off non-privileged users after a 15 minute idle time period has elapsed.

<span style="color:#ff8c00;font-size:150%;">Medium Severity</span>

### Description

Leaving a user’s application session established for an indefinite period of time increases the risk of session hijacking.

Session termination terminates an individual user's logical application session after 15 minutes of application inactivity at which time the user must re-authenticate and a new session must be established if the user desires to continue work in the application.

### Check Text

Ask the application representative to demonstrate the configuration setting where the idle time out value is defined.

Alternatively, logon with a regular application user account and let the session sit idle for 15 minutes.

Attempt to access the application after 15 minutes of inactivity.

If the configuration setting is not set to time out user sessions after 15 minutes of inactivity, or if the regular user session used for testing does not time out after 15 minutes of inactivity, this is a finding.

**Check ID:**  C-24059r493075_chk

### Fix Text 

Design and configure the application to terminate the non-privileged users session after 15 minutes of inactivity.

**Fix ID:**  F-24048r493076_fix

**Vulnerability ID:**  V-222389

**Rule ID:**  SV-222389r1043182_rule

---

## The application must automatically terminate the admin user session and log off admin users after a 10 minute idle time period is exceeded.

<span style="color:#ff8c00;font-size:150%;">Medium Severity</span>

### Description

Leaving an admin user's application session established for an indefinite period of time increases the risk of session hijacking.

Session termination terminates an individual user's logical application session after 10 minutes of application inactivity at which time the user must re-authenticate and a new session must be established if the user desires to continue work in the application.

### Check Text

Ask the application representative to demonstrate the application configuration setting where the idle time out value is defined for admin users.

Alternatively, logon with an admin user account and let the session sit idle for 10 minutes.

Attempt to access the application after 10 minutes of inactivity.

If the configuration setting is not set to time out admin user sessions after 10 minutes of inactivity, or if the session used for testing does not time out after 10 minutes of inactivity, this is a finding.

**Check ID:**  C-24060r493078_chk

### Fix Text 

Design and configure the application to terminate the admin users session after 10 minutes of inactivity.

**Fix ID:**  F-24049r493079_fix

**Vulnerability ID:**  V-222390

**Rule ID:**  SV-222390r1043182_rule

---

## Applications requiring user access authentication must provide a logoff capability for user initiated communication session.

<span style="color:#ff8c00;font-size:150%;">Medium Severity</span>

### Description

If a user cannot explicitly end an application session, the session may remain open and be exploited by an attacker.  Applications providing user access must provide the ability for users to manually terminate their sessions and log off.

### Check Text

If the application does not provide an interface for interactive user access, this is not applicable.

Log on to the application with a valid user account. Examine the user interface. Identify the command or link that provides the logoff function.

Activate the user logoff function.

Observe user interface and attempt to interact with the application.  Confirm user interaction with the application is no longer possible.

If the user session is not terminated or if the logoff function does not exist, this is a finding.

**Check ID:**  C-24061r493081_chk

### Fix Text 

Design and configure the application to provide all users with the capability to manually terminate their application session.

**Fix ID:**  F-24050r493082_fix

**Vulnerability ID:**  V-222391

**Rule ID:**  SV-222391r961224_rule

---

## The application must display an explicit logoff message to users indicating the reliable termination of authenticated communications sessions.

<span style="color:#b3b31a;font-size:150%;">Low Severity</span>

### Description

If a user is not explicitly notified that their application session has been terminated, they cannot be certain that their session did not remain open. Applications with a user access interface must provide an explicit logoff message to the user upon successful termination of the user session.

### Check Text

If the application does not provide an interface for interactive user access, this is not applicable.

Log on to the application with a valid user account. Examine the user interface. Identify the command or link that provides the logoff function.

Activate the user logoff function.

If the application does not provide an explicit logoff message indicating the user session has been terminated, this is a finding.

**Check ID:**  C-24062r493084_chk

### Fix Text 

Design and configure the application to provide an explicit logoff message to users indicating a successful logoff has occurred upon user session termination.

**Fix ID:**  F-24051r493085_fix

**Vulnerability ID:**  V-222392

**Rule ID:**  SV-222392r961227_rule

---

## The application must associate organization-defined types of security attributes having organization-defined security attribute values with information in storage.

<span style="color:#ff8c00;font-size:150%;">Medium Severity</span>

### Description

Without the association of security attributes to information, there is no basis for the application to make security related access-control decisions.

Security attributes are abstractions representing the basic properties or characteristics of an entity (e.g., subjects and objects) with respect to safeguarding information.

These attributes are typically associated with internal data structures (e.g., records, buffers, files) within the information system and are used to enable the implementation of access control and flow control policies, reflect special dissemination, handling or distribution instructions, or support other aspects of the information security policy.

One example includes marking data as classified or FOUO. These security attributes may be assigned manually or during data processing but either way, it is imperative these assignments are maintained while the data is in storage. If the security attributes are lost when the data is stored, there is the risk of a data compromise.

Classify the system hosting the application with default classification.  Treat all unmarked data at the highest classification as the overall hosting system is classified.  If there is no classification, mark system high.

### Check Text

Review the application documentation and interview the application administrator.

Determine if the application processes classified, FOUO, or other data that is required to be marked and identify if the application requirements specify data markings of any other types of data.

If the application does not contain classified, FOUO, or other data that is required to be marked, this requirement is not applicable.

Review the database or other storage mechanism and have the application administrator identify and demonstrate how the application assigns and maintains data markings while the data is in storage.

Typical methods for marking data include utilizing a table or data base field that contains the marking information and associating the marking information with the data.

If application data required to be marked is not marked and does not retain its marking while it is being stored, this is a finding.

**Check ID:**  C-24063r493087_chk

### Fix Text 

Design and configure the application to assign data marking and ensure the marking is retained when the data is stored.

**Fix ID:**  F-24052r493088_fix

**Vulnerability ID:**  V-222393

**Rule ID:**  SV-222393r961269_rule

---

## The application must associate organization-defined types of security attributes having organization-defined security attribute values with information in process.

<span style="color:#ff8c00;font-size:150%;">Medium Severity</span>

### Description

Without the association of security attributes to information, there is no basis for the application to make security related access-control decisions.

Security attributes are abstractions representing the basic properties or characteristics of an entity (e.g., subjects and objects) with respect to safeguarding information.

These attributes are typically associated with internal data structures (e.g., records, buffers, files) within the information system and are used to enable the implementation of access control and flow control policies, reflect special dissemination, handling or distribution instructions, or support other aspects of the information security policy.

One example includes marking data as classified or FOUO. These security attributes may be assigned manually or during data processing but either way, it is imperative these assignments are maintained while the data is in process. If the security attributes are lost when the data is being processed, there is the risk of a data compromise.

### Check Text

Review the application documentation and interview the application administrator.

Identify if the application requirements include data marking.  Also determine if the application processes classified, FOUO or other data that is required to be marked.

If the application does not contain classified, FOUO or have data marking requirements, this requirement is not applicable.

Access the user interface for the application and navigate through the application. Perform several application actions that will manipulate data contained within the application.

For example, create a test record and assign a data marking to the data element. Save the test record, close the data entry fields and navigate to display the test record. Perform an edit action on the test data that does not edit the marking itself or perform any other form of data processing such as assigning the data to another users work queue for review or printing the data, ensure the data marking is retained throughout the data processing actions.

If application data required to be marked does not retain its marking while it is being processed by the application, this is a finding.

**Check ID:**  C-24064r493090_chk

### Fix Text 

Design and configure the application to retain the data marking when processing data.

**Fix ID:**  F-24053r493091_fix

**Vulnerability ID:**  V-222394

**Rule ID:**  SV-222394r961272_rule

---

## The application must associate organization-defined types of security attributes having organization-defined security attribute values with information in transmission.

<span style="color:#ff8c00;font-size:150%;">Medium Severity</span>

### Description

Without the association of security attributes to information, there is no basis for the application to make security related access-control decisions.

Security attributes are abstractions representing the basic properties or characteristics of an entity (e.g., subjects and objects) with respect to safeguarding information.

These attributes are typically associated with internal data structures (e.g., records, buffers, files) within the information system and are used to enable the implementation of access control and flow control policies, reflect special dissemination, handling or distribution instructions, or support other aspects of the information security policy.

One example includes marking data as classified or FOUO. These security attributes may be assigned manually or during data processing but either way, it is imperative these assignments are maintained while the data is in transmission. If the security attributes are lost when the data is being transmitted, there is the risk of a data compromise.

### Check Text

Review the application documentation and interview the application administrator.

Identify if the application requirements include data marking also determine if the application processes classified, FOUO or other data that is required to be marked.

Access the user interface for the application and navigate through the application. Perform an application action that will transmit marked data that is contained within the application.

If the application does not contain classified, FOUO or have data marking requirements, or if the application does not transmit data, this requirement is not applicable.

E.g., create a test record and assign a data marking to the data element. Save the test record, close the data entry fields and navigate to display the test record. Initiate the application processes to transmit data. Access remote system or have person with access to remote system verify the data marking is retained after the data transmission.

If application data required to be marked does not retain its marking when it is being transmitted by the application, this is a finding.

**Check ID:**  C-24065r493093_chk

### Fix Text 

Design and configure the application to retain the data marking when transmitting data.

**Fix ID:**  F-24054r493094_fix

**Vulnerability ID:**  V-222395

**Rule ID:**  SV-222395r961275_rule

---

## The application must implement DoD-approved encryption to protect the confidentiality of remote access sessions.

<span style="color:#ff8c00;font-size:150%;">Medium Severity</span>

### Description

Without confidentiality protection mechanisms, unauthorized individuals may gain access to sensitive information via a remote access session.

Remote access is access to DoD nonpublic information systems by an authorized user (or an information system) communicating through an external, non-organization-controlled network. Remote access methods include, for example, dial-up, broadband, and wireless.

Encryption provides a means to secure the remote connection to prevent unauthorized access to the data traversing the remote access connection thereby providing a degree of confidentiality. The encryption strength of mechanism is selected based on the security categorization of the information.

### Check Text

Review the application documentation and interview the system administrator.

Identify the application encryption capabilities and methods for implementing encryption protection.

For web based applications; open the web browser and access the website URL. Use the browser and determine if the session is protected via TLS. A secure connection is usually indicated in the upper left hand corner of the URL by a padlock icon. Click on the padlock icon and examine the connection information. Determine if TLS encryption is used to secure the session.

For non-web based applications, determine the TCP/IP port, protocol and method used for establishing client connections to the remote server. Review application configuration settings to ensure encryption is specified and  via TLS.

If the connection is not secured with TLS, this is a finding.

**Check ID:**  C-24066r493096_chk

### Fix Text 

Design and configure applications to use TLS encryption to protect the confidentiality of remote access sessions.

**Fix ID:**  F-24055r493097_fix

**Vulnerability ID:**  V-222396

**Rule ID:**  SV-222396r960759_rule

---

## The application must implement cryptographic mechanisms to protect the integrity of remote access sessions.

<span style="color:#ff8c00;font-size:150%;">Medium Severity</span>

### Description

Without integrity protection mechanisms, unauthorized individuals may gain access to sensitive information via a remote access session.

Remote access is access to DoD nonpublic information systems by an authorized user (or an information system) communicating through an external, non-organization-controlled network. Remote access methods include, for example, dial-up, broadband, and wireless.

Encryption provides a means to secure the remote connection to prevent unauthorized access to the data traversing the remote access connection. Without integrity protection mechanisms, unauthorized individuals may be able to insert inauthentic content into a remote session. The encryption strength of mechanism is selected based on the security categorization of the information.

### Check Text

Review the application documentation and interview the system administrator.

Identify the application encryption capabilities and methods for implementing encryption protection.

For web based applications; open the web browser and access the website URL. Use the browser and determine if the session is protected via TLS. A secure connection is usually indicated in the upper left hand corner of the URL by a padlock icon. Click on the padlock icon and examine the connection information. Determine if TLS encryption is used to secure the session.

For non-web based applications, determine the TCP/IP port, protocol and method used for establishing client connections to the remote server. Review application configuration settings to ensure encryption is specified and  via TLS.

If the connection is not secured with TLS, this is a finding.

**Check ID:**  C-24067r493099_chk

### Fix Text 

Design and configure applications to use TLS encryption to protect the integrity of remote access sessions.

**Fix ID:**  F-24056r493100_fix

**Vulnerability ID:**  V-222397

**Rule ID:**  SV-222397r960762_rule

---

## Applications with SOAP messages requiring integrity must include the following message elements:-Message ID-Service Request-Timestamp-SAML Assertion (optionally included in messages) and all elements of the message must be digitally signed.

<span style="color:#ff8c00;font-size:150%;">Medium Severity</span>

### Description

Digitally signed SOAP messages provide message integrity and authenticity of the signer of the message independent of the transport layer. Service requests may be intercepted and changed in transit and the data integrity may be at risk if the SOAP message is not digitally signed.

Functional architecture aspects of the application security plan identify the application data elements that require data integrity protection.

### Check Text

Review the application documentation, system security plan, application architecture diagrams and interview the application administrator.

Review the design document for web services using SOAP messages.

If the application does not utilize SOAP messages, this check is not applicable.

Review the design document and SOAP messages.
Verify the Message ID, Service Request, Timestamp, and SAML Assertion are included in the SOAP message.
If they are included, verify they are signed with a certificate.

If SOAP messages requiring integrity do not have the Message ID, Service Request, Timestamp, and SAML Assertion signed, or if any part of the message is not digitally signed, this is a finding.

**Check ID:**  C-24068r493102_chk

### Fix Text 

Design and configure the application to sign the following message elements for SOAP messages requiring integrity:

- Message ID
- Service Request
- Timestamp
- SAML Assertion
- Message elements

**Fix ID:**  F-24057r493103_fix

**Vulnerability ID:**  V-222398

**Rule ID:**  SV-222398r960762_rule

---

## Messages protected with WS_Security must use time stamps with creation and expiration times.

<span style="color:#ff0000;font-size:150%;">High Severity</span>

### Description

The lack of time stamps could lead to the eventual replay of the message, leaving the application susceptible to replay events which may result in an immediate loss of confidentiality.

### Check Text

Ask the application representative for the design document. Review the design document for web services using WS-Security tokens.

If the application does not utilize WS-Security tokens, this check is not applicable.

Examine the contents of a SOAP message using WS Security; all messages should contain time stamps, sequence numbers, and expiration.

If messages using WS Security do not contain time stamps, sequence numbers, and expiration, this is a finding.

**Check ID:**  C-24069r493105_chk

### Fix Text 

Design and configure applications using WS-Security messages to use time stamps with creation and expiration times and sequence numbers.

**Fix ID:**  F-24058r493106_fix

**Vulnerability ID:**  V-222399

**Rule ID:**  SV-222399r960759_rule

---

## Validity periods must be verified on all application messages using WS-Security or SAML assertions.

<span style="color:#ff0000;font-size:150%;">High Severity</span>

### Description

When using WS-Security in SOAP messages, the application should check the validity of the time stamps with creation and expiration times. Time stamps that are not validated may lead to a replay event and provide immediate unauthorized access of the application. Unauthorized access results in an immediate loss of confidentiality.

### Check Text

Ask the application representative for the design document.

Review the design document for web services.

If the application does not utilize WSS or SAML assertions, this requirement is not applicable.

Review the design document and verify validity periods are checked on all messages using WS-Security or SAML assertions.

If the design document does not exist, or does not indicate validity periods are checked on messages using WS-Security or SAML assertions, this is a finding.

**Check ID:**  C-24070r493108_chk

### Fix Text 

Design and configure the application to use validity periods, ensure validity periods are verified on all WS-Security token profiles and SAML Assertions.

**Fix ID:**  F-24059r493109_fix

**Vulnerability ID:**  V-222400

**Rule ID:**  SV-222400r960759_rule

---

## The application must ensure each unique asserting party provides unique assertion ID references for each SAML assertion.

<span style="color:#ff8c00;font-size:150%;">Medium Severity</span>

### Description



### Check Text

Ask the application representative for the design document.

Review the design document for web services using SAML assertions.

If the application does not utilize SAML assertions, this check is not applicable.

Review the design document and verify SAML assertion identifiers are not reused by a single asserting party.

If the design document does not exist, or does not indicate SAML assertion identifiers which are unique for each asserting party, this is a finding.

**Check ID:**  C-24071r493111_chk

### Fix Text 

Design and configure each SAML assertion authority to use unique assertion identifiers.

**Fix ID:**  F-24060r493112_fix

**Vulnerability ID:**  V-222401

**Rule ID:**  SV-222401r960759_rule

---

## The application must ensure encrypted assertions, or equivalent confidentiality protections are used when assertion data is passed through an intermediary, and confidentiality of the assertion data is required when passing through the intermediary.

<span style="color:#ff8c00;font-size:150%;">Medium Severity</span>

### Description



### Check Text

Ask the application representative for the design document.

Review the design document for web services using WS-Security tokens.  

If the application does not utilize WS-Security tokens, this check is not applicable.

Verify all WS-Security tokens are transmitted via an approved encryption method.

If the design document does not exist, or does not indicate all WS-Security tokens are only transmitted via an approved encryption method, this is a finding.

**Check ID:**  C-24072r493114_chk

### Fix Text 

Encrypt assertions or use equivalent confidentiality when sensitive assertion data is passed through an intermediary.

**Fix ID:**  F-24061r493115_fix

**Vulnerability ID:**  V-222402

**Rule ID:**  SV-222402r960759_rule

---

## The application must use the NotOnOrAfter condition when using the SubjectConfirmation element in a SAML assertion.

<span style="color:#ff0000;font-size:150%;">High Severity</span>

### Description



### Check Text

Ask the application representative for the design document.

Review the design document for web services using SAML assertions.

If the application does not utilize SAML assertions, this check is not applicable.

Examine the contents of a SOAP message using the <SubjectConfirmation> element. All messages should contain the <NotOnOrAfter> element. This can be accomplished if the application allows the ability to view XML messages or via a protocol analyzer like Wireshark.

If SOAP messages do not contain <NotOnOrAfter> elements, this is a finding.

**Check ID:**  C-24073r493117_chk

### Fix Text 

Design and configure the application to use the <NotOnOrAfter> condition when using the <SubjectConfirmation> element in a SAML assertion.

**Fix ID:**  F-24062r493118_fix

**Vulnerability ID:**  V-222403

**Rule ID:**  SV-222403r960759_rule

---

## The application must use both the NotBefore and NotOnOrAfter elements or OneTimeUse element when using the Conditions element in a SAML assertion.

<span style="color:#ff0000;font-size:150%;">High Severity</span>

### Description



### Check Text

Ask the application representative for the design document.

Review the design document for web services using SAML assertions.

If the application does not utilize SAML assertions, this check is not applicable.

Examine the contents of a SOAP message using the <Conditions> element; all messages should contain the <NotBefore> and <NotOnOrAfter> or <OneTimeUse> element when in a SAML Assertion. This can be accomplished using a protocol analyzer such as Wireshark.

If SOAP using the <Conditions> element does not contain <NotBefore> and <NotOnOrAfter> or <OneTimeUse> elements, this is a finding.

**Check ID:**  C-24074r493120_chk

### Fix Text 

Design and configure the application to implement the use of the <NotBefore> and <NotOnOrAfter> or <OneTimeUse> when using the <Conditions> element in a SAML assertion.

**Fix ID:**  F-24063r493121_fix

**Vulnerability ID:**  V-222404

**Rule ID:**  SV-222404r960759_rule

---

## The application must ensure if a OneTimeUse element is used in an assertion, there is only one of the same used in the Conditions element portion of an assertion.

<span style="color:#ff8c00;font-size:150%;">Medium Severity</span>

### Description



### Check Text

Ask the application representative for the design document.

Review the design document for web services using SAML assertions.

If the application does not utilize SAML assertions, this check is not applicable.

Examine the contents of a SOAP message using the OneTimeUse element; all messages should contain only one instance of a <OneTimeUse> element in a SAML assertion. This can be accomplished using a protocol analyzer such as Wireshark.

If SOAP message uses more than one, OneTimeUse element in a SAML assertion, this is a finding.

**Check ID:**  C-24075r493123_chk

### Fix Text 

When using OneTimeUse elements in a SAML assertion only allow one, OneTimeUse element to be used in the conditions element of a SAML assertion.

**Fix ID:**  F-24064r493124_fix

**Vulnerability ID:**  V-222405

**Rule ID:**  SV-222405r960759_rule

---

## The application must ensure messages are encrypted when the SessionIndex is tied to privacy data.

<span style="color:#ff8c00;font-size:150%;">Medium Severity</span>

### Description

When the SessionIndex is tied to privacy data (e.g., attributes containing privacy data) the message should be encrypted. If the message is not encrypted there is the possibility of compromise of privacy data.

### Check Text

Ask the application representative for the design document.

Review the design document for web services using SAML assertions.

If the application does not utilize SAML assertions, this check is not applicable.

Examine the contents of a SOAP message using a SessionIndex in the SAML element AuthnStatement. Verify the information which is tied to the SessionIndex.

If the SessionIndex is tied to privacy information, and it is not encrypted, this is a finding.

**Check ID:**  C-24076r493126_chk

### Fix Text 

Encrypt messages when the SessionIndex is tied to privacy data.

**Fix ID:**  F-24065r493127_fix

**Vulnerability ID:**  V-222406

**Rule ID:**  SV-222406r960759_rule

---

## The application must provide automated mechanisms for supporting account management functions.

<span style="color:#ff8c00;font-size:150%;">Medium Severity</span>

### Description

Enterprise environments make application account management challenging and complex. A manual process for account management functions adds the risk of a potential oversight or other error.

Manual examples include but are not limited to admin staff logging into the system or systems and manually performing step by step actions affecting user accounts that could otherwise be automated.  This does not include any manual steps taken to initiate automated processes or the use of automated systems.

A comprehensive application account management process that includes automation helps to ensure accounts designated as requiring attention are consistently and promptly addressed. Examples include, but are not limited to, using automation to take action on multiple accounts designated as inactive, suspended or terminated or by disabling accounts located in non-centralized account stores such as multiple servers. This requirement applies to all account types, including individual/user, shared, group, system, guest/anonymous, emergency, developer/manufacturer/vendor, temporary, and service.

The application must be configured to automatically provide account management functions and these functions must immediately enforce the organization's current account policy. The automated mechanisms may reside within the application itself or may be offered by the operating system or other infrastructure providing automated account management capabilities. Automated mechanisms may be comprised of differing technologies that when placed together contain an overall automated mechanism supporting an organization's automated account management requirements.

Account management functions include: assignment of group or role membership; identifying account type; specifying user access authorizations (i.e., privileges); account removal, update, or termination; and administrative alerts. The use of automated mechanisms can include, for example: using email or text messaging to automatically notify account managers when users are terminated or transferred; using the information system to monitor account usage; and using automated telephonic notification to report atypical system account usage.

### Check Text

Review the application documentation and interview the application administrator.

Identify the account management methods, processes and procedures that are used.

If the application is utilizing a centralized authentication mechanism such as Active Directory or LDAP, verify all user account activity is conducted via that solution and no local user accounts that circumvent the automated solution are used.

Determine if automated mechanisms are used when managing application user accounts and taking management action on application user accounts. Automated methods include but are not limited to:

Taking action on accounts that have been determined to be inactive, suspended, terminated, or disabled.

Automated action examples include: deleting such accounts, reactivating accounts in conjunction with a validation or verification process, or sending notifications or reminders to the account holders that their account is about to be disabled or deleted.

Verify the action that is taken is automated and repeatable.

If the account management process is manual in nature, this is a finding.

**Check ID:**  C-24077r493129_chk

### Fix Text 

Use automated processes and mechanisms for account management functions.

**Fix ID:**  F-24066r493130_fix

**Vulnerability ID:**  V-222407

**Rule ID:**  SV-222407r1043176_rule

---

## Shared/group account credentials must be terminated when members leave the group.

<span style="color:#ff8c00;font-size:150%;">Medium Severity</span>

### Description

If shared/group account credentials are not terminated when individuals leave the group, the user that left the group can still gain access even though they are no longer authorized. A shared/group account credential is a shared form of authentication that allows multiple individuals to access the application using a single account. There may also be instances when specific user actions need to be performed on the information system without unique user identification or authentication. Examples of credentials include passwords and group membership certificates.

### Check Text

Review the application documentation and determine if there is a requirement for shared or group accounts.

If there is no official requirement for shared or group application accounts, this requirement is Not Applicable.

Interview the application representative and identify shared/group accounts.

Have the application representative provide their procedures for account management as it pertains to group users.

Validate there is a procedure for deleting either member accounts or the entire group account when member leave the group.

If there is no process for handling group account credentials, this is a finding.

**Check ID:**  C-24078r985901_chk

### Fix Text 

Create a procedure for deleting either member accounts or the entire group account when members leave the group.

**Fix ID:**  F-24067r493133_fix

**Vulnerability ID:**  V-222408

**Rule ID:**  SV-222408r1015683_rule

---

## The application must automatically remove or disable temporary user accounts 72 hours after account creation.

<span style="color:#ff8c00;font-size:150%;">Medium Severity</span>

### Description

If temporary user accounts remain active when no longer needed or for an excessive period, these accounts may be used to gain unauthorized access. To mitigate this risk, automated termination of all temporary accounts must be set upon account creation.

Temporary accounts are established as part of normal account activation procedures when there is a need for short-term accounts without the demand for immediacy in account activation.

If temporary accounts are used, the application must be configured to automatically terminate these types of accounts after a DoD-defined time period of 72 hours starting from the point of account creation.

To address access requirements, many application developers choose to integrate their applications with enterprise-level authentication/access mechanisms meeting or exceeding access control policy requirements. Such integration allows the application developer to off-load those access control functions and focus on core application features and functionality.

### Check Text

If official documentation exist that disallows the use of temporary user accounts within the application, this requirement is not applicable.

Examine the application documentation or interview the application representative to identify how the application users are managed.

Navigate to the screen where user accounts are configured.

Create a test account and determine if there is a setting to specify the user account as being temporary in nature.

Determine if there is an available setting to expire the account after a period of time.

If the application has no ability to specify a user account as being temporary in nature, or if the account has no ability to automatically disable or remove the account after 72 hours after account creation, this is a finding.

**Check ID:**  C-24079r493135_chk

### Fix Text 

Configure temporary accounts to be automatically removed or disabled after 72 hours after account creation.

**Fix ID:**  F-24068r493136_fix

**Vulnerability ID:**  V-222409

**Rule ID:**  SV-222409r960771_rule

---

## The application must have a process, feature or function that prevents removal or disabling of emergency accounts. 

<span style="color:#b3b31a;font-size:150%;">Low Severity</span>

### Description

Emergency accounts are administrator accounts which are established in response to crisis situations where the need for rapid account activation is required. Therefore, emergency account activation may bypass normal account authorization processes.

If these accounts are automatically disabled, system maintenance during emergencies may not be possible, thus adversely affecting system availability.

Emergency accounts are different from infrequently used accounts (i.e., local logon accounts used by system administrators when network or normal logon/access is not available). Infrequently used accounts also remain available and are not subject to automatic termination dates. However, an emergency account is normally a different account which is created for use by vendors or system maintainers.

To address access requirements, many application developers choose to integrate their applications with enterprise-level authentication/access mechanisms that meet or exceed access control policy requirements. Such integration allows the application developer to off-load those access control functions and focus on core application features and functionality.

### Check Text

Review the application documentation and interview the application administrator. Identify if emergency accounts are ever used. 

If emergency accounts are not used, this requirement is not applicable.

If emergency accounts are used, validate a procedure, process, feature or function exists that will prevent the emergency account from being deleted or disabled during a crisis situation.

Examples include but are not limited to adding a flag to the account to ensure it is not deleted during a specified emergency period or placing the account in a designated group that is monitored and controlled in accordance with the crisis.

If a process, procedure, function or feature designed to prevent emergency accounts from being  deleted or disabled during a crisis situation is not available, this is a finding.

**Check ID:**  C-24080r493138_chk

### Fix Text 

Identify accounts that are created in an emergency situation and ensure procedures or processes are in place to prevent disabling or deleting the account while the emergency is underway.

**Fix ID:**  F-24069r493139_fix

**Vulnerability ID:**  V-222410

**Rule ID:**  SV-222410r961863_rule

---

## The application must automatically disable accounts after a 35 day period of account inactivity.

<span style="color:#b3b31a;font-size:150%;">Low Severity</span>

### Description

Attackers that are able to exploit an inactive account can potentially obtain and maintain undetected access to an application. Owners of inactive accounts will not notice if unauthorized access to their user account has been obtained. Applications need to track periods of user inactivity and disable accounts after 35 days of inactivity. Such a process greatly reduces the risk that accounts will be hijacked, leading to a data compromise.

To address access requirements, many application developers choose to integrate their applications with enterprise-level authentication/access mechanisms that meet or exceed access control policy requirements. Such integration allows the application developer to off-load those access control functions and focus on core application features and functionality.

This policy does not apply to either emergency accounts or infrequently used accounts. Infrequently used accounts are local logon administrator accounts used by system administrators when network or normal logon/access is not available. Emergency accounts are administrator accounts created in response to crisis situations.

### Check Text

Examine the application documentation or interview the application representative to identify how the application users are managed.

Interview the application administrator and determine if the application is configured to utilize a centralized user management system like Active Directory (AD) for user management or if the application manages user accounts within the application.

If the application is configured to use an enterprise-based application user management capability that is STIG compliant, the requirement is not applicable.

If the application handles the management tasks for user accounts, access the applications user management utility.

Navigate to the screen where user accounts are configured to be disabled after 35 days of inactivity.

Confirm this setting is active.

If the application is not set to expire inactive accounts after 35 days, or if the application has no ability to expire accounts after 35 days of inactivity, this is a finding.

**Check ID:**  C-24081r493141_chk

### Fix Text 

Design and configure the application to expire user accounts after 35 days of inactivity.

**Fix ID:**  F-24070r493142_fix

**Vulnerability ID:**  V-222411

**Rule ID:**  SV-222411r960774_rule

---

## Unnecessary application accounts must be disabled, or deleted.

<span style="color:#ff8c00;font-size:150%;">Medium Severity</span>

### Description

Test or demonstration accounts are sometimes created during the application installation process. This creates a security risk as these accounts often remain after the initial installation process and can be used to gain unauthorized access to the application. Applications must be designed and configured to disable or delete any unnecessary accounts that may be created. 

Care must be taken to ensure valid accounts used for valid application operations are not disabled or deleted when this requirement is applied.

### Check Text

Review the system documentation and identify any valid application accounts that are required in order for the application to operate. Accounts the application itself uses in order to function are not in scope for this requirement.

Have the application administrator generate a list of all application users. This should include relevant user metadata such as phone numbers or department identifiers.

Have the application administrator identify and validate all user accounts.

If any accounts cannot be validated and are deemed to be unnecessary, this is a finding.

**Check ID:**  C-24082r493144_chk

### Fix Text 

Design the application so unessential user accounts are not created during installation. Disable or delete all unnecessary application user accounts.

**Fix ID:**  F-24071r493145_fix

**Vulnerability ID:**  V-222412

**Rule ID:**  SV-222412r960774_rule

---

## The application must automatically audit account creation.

<span style="color:#ff8c00;font-size:150%;">Medium Severity</span>

### Description

Once an attacker establishes initial access to a system, the attacker often attempts to create a persistent method of re-establishing access. One way to accomplish this is for the attacker to simply create a new account. Auditing of account creation is one method for mitigating this risk. A comprehensive account management process will ensure an audit trail documents the creation of application user accounts and, as required, notifies administrators and/or application owners exists. Such a process greatly reduces the risk that accounts will be surreptitiously created and provides logging that can be used for forensic purposes.

To address access requirements, many application developers choose to integrate their applications with enterprise-level authentication/access/auditing mechanisms meeting or exceeding access control policy requirements. Such integration allows the application developer to off-load those access control functions and focus on core application features and functionality.

### Check Text

Examine the application documentation to identify how the application users are managed.

Interview the application administrator and determine if the application is configured to utilize a centralized user management system like Active Directory for user management or if the application manages user accounts within the application.

If the application is configured to use an enterprise-based application user management capability that is STIG compliant, the requirement is not applicable.

Identify the location of the audit logs and review the end of the logs.

Access the user account management functionality and create a new user account.

Examine the log file again and determine if the account creation event was logged. The information logged should, at a minimum, include enough detail to determine which account was created and when.

If the account creation event was not logged, this is a finding.

**Check ID:**  C-24083r493147_chk

### Fix Text 

Configure the application to write a log entry when a new user account is created.

At a minimum, ensure account name, date and time of the event are recorded.

**Fix ID:**  F-24072r493148_fix

**Vulnerability ID:**  V-222413

**Rule ID:**  SV-222413r960777_rule

---

## The application must automatically audit account modification.

<span style="color:#ff8c00;font-size:150%;">Medium Severity</span>

### Description

One way for an attacker to establish persistent access is for the attacker to modify or copy an existing account. Auditing of account modification is one method for mitigating this risk. A comprehensive account management process will ensure an audit trail documents the modification of application user accounts. Such a process greatly reduces the risk that accounts will be surreptitiously modified and provides logging that can be used for forensic purposes.

To address account requirements and to ensure application accounts follow requirements consistently, application developers are strongly encouraged to integrate their applications with enterprise-level authentication/access/auditing mechanisms that meet or exceed access control policy requirements. Such integration allows the application developer to off-load those access control functions and focus on core application features and functionality.

### Check Text

Examine the application documentation to identify how the application users are managed.

Interview the application administrator and determine if the application is configured to utilize a centralized user management system like Active Directory for user management or if the application manages user accounts within the application.

If the application is configured to use an enterprise-based application user management capability that is STIG compliant, the requirement is not applicable.

Identify the location of the audit logs and review the end of the logs.

Access the user account management functionality and modify a test user account.

Examine the log file again and determine if the account event was logged. The information logged should, at a minimum, include enough detail to determine which account was modified and when.

If the account modification event information was not logged, this is a finding.

**Check ID:**  C-24084r493150_chk

### Fix Text 

Configure the application to write a log entry when a user account is modified.

At a minimum, ensure account name, date and time of the event are recorded.

**Fix ID:**  F-24073r493151_fix

**Vulnerability ID:**  V-222414

**Rule ID:**  SV-222414r960780_rule

---

## The application must automatically audit account disabling actions.

<span style="color:#ff8c00;font-size:150%;">Medium Severity</span>

### Description

When application accounts are disabled, user accessibility is affected. Accounts are utilized for identifying individual application users or for identifying the application processes themselves. In order to detect and respond to events affecting user accessibility and application processing, applications must audit account disabling actions and, as required, notify the appropriate individuals, so they can investigate the event. Such a capability greatly reduces the risk that application accessibility will be negatively affected for extended periods of time and provides logging that can be used for forensic purposes. 

Application developers are encouraged to integrate their applications with enterprise-level authentication/access/audit mechanisms such as Syslog, Active Directory or LDAP.

### Check Text

Examine the application documentation to identify how the application users are managed.

Interview the application administrator and determine if the application is configured to utilize a centralized user management system like Active Directory for user management or if the application manages user accounts within the application.

If the application is configured to use an enterprise-based application user management capability that is STIG compliant, the requirement is not applicable.

Identify the location of the audit logs and review the end of the logs.

Access the user account management functionality and disable a test user account.

Examine the log file again and determine if the account disable event was logged. The information logged should, at a minimum, include enough detail to determine which account was disabled and when.

If the account disabling event information was not logged, this is a finding.

**Check ID:**  C-24085r493153_chk

### Fix Text 

Configure the application to write a log entry when a user account is disabled.

At a minimum, ensure account name, date and time of the event are recorded.

**Fix ID:**  F-24074r493154_fix

**Vulnerability ID:**  V-222415

**Rule ID:**  SV-222415r960783_rule

---

## The application must automatically audit account removal actions.

<span style="color:#ff8c00;font-size:150%;">Medium Severity</span>

### Description

When application accounts are removed, user accessibility is affected. Accounts are utilized for identifying individual application users or for identifying the application processes themselves. In order to detect and respond to events affecting user accessibility and application processing, applications must audit account removal actions and, as required, notify the appropriate individuals, so they can investigate the event. Such a capability greatly reduces the risk that application accessibility will be negatively affected for extended periods of time and provides logging that can be used for forensic purposes.

Application developers are encouraged to integrate their applications with enterprise-level authentication/access/audit mechanisms such as Syslog, Active Directory or LDAP.

### Check Text

Examine the application documentation to identify how the application users are managed.

Interview the application administrator and determine if the application is configured to utilize a centralized user management system like Active Directory for user management or if the application manages user accounts within the application.

If the application is configured to use an enterprise-based application user management capability that is STIG compliant, the requirement is not applicable.

Identify the location of the audit logs and review the end of the logs.

Access the user account management functionality and remove a test user account.

Examine the log file again and determine if the account removal event was logged. The information logged should, at a minimum, include enough detail to determine which account was disabled and when.

If the account removal event information was not logged, this is a finding.

**Check ID:**  C-24086r493156_chk

### Fix Text 

Configure the application to write a log entry when a user account is removed.

At a minimum, ensure account name, date and time of the event are recorded.

**Fix ID:**  F-24075r493157_fix

**Vulnerability ID:**  V-222416

**Rule ID:**  SV-222416r960786_rule

---

## The application must notify system administrators (SAs) and information system security officers (ISSOs) when accounts are created.

<span style="color:#b3b31a;font-size:150%;">Low Severity</span>

### Description

Once an attacker establishes access to a system, the attacker often attempts to create a persistent method of re-establishing access. One way to accomplish this is for the attacker to simply create a new account. Notification of account creation is one method for mitigating this risk. A comprehensive account management process will ensure an audit trail which documents the creation of application user accounts and notifies administrators and ISSOs such accounts exist. This type of process greatly reduces the risk that accounts will be surreptitiously created and provides logging that can be used for forensic purposes.

To address access requirements, many application developers choose to integrate their applications with enterprise-level authentication/access/auditing mechanisms that meet or exceed access control policy requirements. Such integration allows the application developer to offload those access control functions and focus on core application features and functionality.

### Check Text

Review the application and system documentation.

Interview the application administrator and determine if the application is configured to utilize a centralized user management system like Active Directory for user management or if the application manages user accounts within the application.

If the application is configured to use an enterprise-based application user management capability that is STIG compliant, the requirement is Not Applicable.

Ensure the application is configured to notify SAs when new accounts are created by identifying SAs who will be notified, creating a test account, and checking with SAs to verify the notification was received.

If SAs and ISSOs are not notified when accounts are created, this is a finding.

**Check ID:**  C-24087r985903_chk

### Fix Text 

Configure the application to notify the SA and the ISSO when application accounts are created.

**Fix ID:**  F-24076r985904_fix

**Vulnerability ID:**  V-222417

**Rule ID:**  SV-222417r1015684_rule

---

## The application must notify system administrators (SAs) and information system security officers (ISSOs) when accounts are modified.

<span style="color:#b3b31a;font-size:150%;">Low Severity</span>

### Description

Once an attacker establishes access to a system, the attacker often attempts to create a persistent method of re-establishing access. One way to accomplish this is for the attacker to simply create a new account. Notification of account creation is one method for mitigating this risk. A comprehensive account management process will ensure an audit trail which documents the modification of application user accounts and notifies administrators and ISSOs such accounts were modified. This type of process greatly reduces the risk that accounts will be surreptitiously modified and provides logging that can be used for forensic purposes.

To address access requirements, many application developers choose to integrate their applications with enterprise-level authentication/access/auditing mechanisms that meet or exceed access control policy requirements. Such integration allows the application developer to offload those access control functions and focus on core application features and functionality.

### Check Text

Review the application and system documentation.

Interview the application administrator and determine if the application is configured to utilize a centralized user management system like Active Directory for user management or if the application manages user accounts within the application.

If the application is configured to use an enterprise-based application user management capability that is STIG compliant, this requirement is Not Applicable.

Ensure the application is configured to notify SAs when accounts are modified by identifying the SAs who will be notified when accounts are modified.

Modify a test account and check with a SA to verify the notification was received.

If SAs and ISSOs are not notified when accounts are modified, this is a finding.

**Check ID:**  C-24088r985906_chk

### Fix Text 

Configure the application to notify the SA and the ISSO when application accounts are modified.

**Fix ID:**  F-24077r985907_fix

**Vulnerability ID:**  V-222418

**Rule ID:**  SV-222418r1015685_rule

---

## The application must notify system administrators (SAs) and information system security officers (ISSOs) of account disabling actions.

<span style="color:#b3b31a;font-size:150%;">Low Severity</span>

### Description

Once an attacker establishes access to a system, the attacker often attempts to create a persistent method of re-establishing access. One way to accomplish this is for the attacker to simply create a new account. Notification of account creation is one method for mitigating this risk. A comprehensive account management process will ensure an audit trail which documents the creation of application user accounts and notifies administrators and ISSOs such accounts exist. This type of process greatly reduces the risk that accounts will be surreptitiously created and provides logging that can be used for forensic purposes.

To address access requirements, many application developers choose to integrate their applications with enterprise-level authentication/access/auditing mechanisms that meet or exceed access control policy requirements. Such integration allows the application developer to offload those access control functions and focus on core application features and functionality.

### Check Text

Review the application and system documentation.

Interview the application administrator and determine if the application is configured to utilize a centralized user management system like Active Directory for user management or if the application manages user accounts within the application.

If the application is configured to use an enterprise-based application user management capability that is STIG compliant, the requirement is Not Applicable.

Ensure the application is configured to notify SAs when accounts are disabled by identifying the SAs who will be notified when accounts are disabled.

Disable a test account and check with a SA to verify the notification was received.

If SAs and ISSOs are not notified when accounts are disabled, this is a finding.

**Check ID:**  C-24089r985909_chk

### Fix Text 

Configure the application to notify the SA and the ISSO when application accounts are disabled.

**Fix ID:**  F-24078r985910_fix

**Vulnerability ID:**  V-222419

**Rule ID:**  SV-222419r1015686_rule

---

## The application must notify system administrators (SAs) and information system security officers (ISSOs) of account removal actions.

<span style="color:#b3b31a;font-size:150%;">Low Severity</span>

### Description

Once an attacker establishes access to a system, the attacker often attempts to create a persistent method of re-establishing access. One way to accomplish this is for the attacker to remove an account. Notification of account removal is one method for mitigating this risk. A comprehensive account management process will ensure an audit trail which documents the removal of application user accounts and notifies administrators and ISSOs such accounts no longer exist. This type of process greatly reduces the risk that accounts will be surreptitiously removed and provides logging that can be used for forensic purposes.

To address access requirements, many application developers choose to integrate their applications with enterprise-level authentication/access/auditing mechanisms that meet or exceed access control policy requirements. Such integration allows the application developer to offload those access control functions and focus on core application features and functionality.

### Check Text

Review the application and system documentation.

Interview the application administrator and determine if the application is configured to utilize a centralized user management system like Active Directory for user management or if the application manages user accounts within the application.

If the application is configured to use an enterprise-based application user management capability that is STIG compliant, the requirement is Not Applicable.

Ensure the application is configured to notify SAs when accounts are removed by identifying the SAs who will be notified when accounts are removed.

Remove a test account and check with a SA to verify the notification was received.

If SAs and ISSOs are not notified when accounts are removed, this is a finding.

**Check ID:**  C-24090r985912_chk

### Fix Text 

Configure the application to notify the SA and the ISSO when application accounts are removed.

**Fix ID:**  F-24079r985913_fix

**Vulnerability ID:**  V-222420

**Rule ID:**  SV-222420r1015687_rule

---

## The application must automatically audit account enabling actions.

<span style="color:#ff8c00;font-size:150%;">Medium Severity</span>

### Description

When application accounts are enabled, user accessibility is affected. Accounts are utilized for identifying individual application users or for identifying the application processes themselves. In order to detect and respond to events affecting user accessibility and application processing, applications must audit account removal actions and, as required, notify the appropriate individuals, so they can investigate the event. Such a capability greatly reduces the risk that application accessibility will be negatively affected for extended periods of time and provides logging that can be used for forensic purposes.

Application developers are encouraged to integrate their applications with enterprise-level authentication/access/audit mechanisms such as Syslog, Active Directory or LDAP.

### Check Text

Examine the application documentation or interview the application representative to identify how the application users are managed.

Interview the application administrator and determine if the application is configured to utilize a centralized user management system such as Active Directory for user management or if the application manages user accounts within the application.

If the application is configured to use an enterprise-based application user management capability that is STIG compliant, the requirement is not applicable.

Identify the location of the audit logs and review the end of the logs.

Access the user account management functionality and enable a test user account.

Examine the log file again and determine if the account enable event was logged. The information logged should, at a minimum, include enough detail to determine which account was enabled and when.

If the account enabling event information was not logged, this is a finding.

**Check ID:**  C-24091r918114_chk

### Fix Text 

Configure the application to write a log entry when a user account is enabled. 

At a minimum, ensure account name, date and time of the event are recorded.

**Fix ID:**  F-24080r493172_fix

**Vulnerability ID:**  V-222421

**Rule ID:**  SV-222421r961290_rule

---

## The application must notify system administrators (SAs) and information system security officers (ISSOs) of account enabling actions.

<span style="color:#b3b31a;font-size:150%;">Low Severity</span>

### Description

Once an attacker establishes access to a system, the attacker often attempts to create a persistent method of re-establishing access. One way to accomplish this is for the attacker to enable an account. Notification of account enabling is one method for mitigating this risk. A comprehensive account management process will ensure an audit trail which documents the enabling of application user accounts and notifies administrators and ISSOs such accounts exist. This type of process greatly reduces the risk that accounts will be surreptitiously enabled and provides logging that can be used for forensic purposes.

To address access requirements, many application developers choose to integrate their applications with enterprise-level authentication/access/auditing mechanisms that meet or exceed access control policy requirements. Such integration allows the application developer to offload those access control functions and focus on core application features and functionality.

### Check Text

Review the application and system documentation.

Interview application administrator and determine if the application is configured to utilize a centralized user management system like Active Directory for user management or if the application manages user accounts within the application.

If the application is configured to use an enterprise-based application user management capability that is STIG compliant, the requirement is Not Applicable.

Ensure the application is configured to notify SAs when accounts are enabled by identifying the SAs who will be notified when accounts are enabled.

Disable and then enable a test account and check with the SA to verify the notification was received to indicate the account was enabled.

If SAs and ISSOs are not notified when accounts are enabled, this is a finding.

**Check ID:**  C-24092r985915_chk

### Fix Text 

Configure the application to notify the SA and the ISSO when application accounts are enabled.

**Fix ID:**  F-24081r985916_fix

**Vulnerability ID:**  V-222422

**Rule ID:**  SV-222422r1015688_rule

---

## Application data protection requirements must be identified and documented.

<span style="color:#ff8c00;font-size:150%;">Medium Severity</span>

### Description

Failure to protect organizational information from data mining may result in a compromise of information. In order to assign the appropriate data protections, application data must be identified and then protection requirements assigned. Access to sensitive data and sensitive data objects should be restricted to those authorized to access the data.

Examples of sensitive data include but are not limited to; Social Security Numbers, Personally Identifiable Information, or any other data that is has been identified as being sensitive in nature by the data owner.

Data storage objects include, for example, databases, database records, and database fields.

Data mining prevention and detection techniques include, for example: limiting the types of responses provided to database queries; limiting the number/frequency of database queries to increase the work factor needed to determine the contents of such databases; and notifying organizational personnel when atypical database queries or accesses occur.

Protection methods include but are not limited to data encryption, Role-Based Access Controls and access authentication.

### Check Text

Ask the application representative for the documentation that identifies the application data elements, the protection requirements, and any associated steps that are being taken to protect the data.

If the application data protection requirements are not documented, this is a finding.

**Check ID:**  C-24093r493177_chk

### Fix Text 

Identify and document the application data elements and the data protection requirements.

**Fix ID:**  F-24082r493178_fix

**Vulnerability ID:**  V-222423

**Rule ID:**  SV-222423r961302_rule

---

## The application must utilize organization-defined data mining detection techniques for organization-defined data storage objects to adequately detect data mining attempts.

<span style="color:#ff8c00;font-size:150%;">Medium Severity</span>

### Description

Failure to protect organizational information from data mining may result in a compromise of information.

Data mining occurs when the application is programmatically probed and data is automatically extracted. While there are valid uses for data mining within data sets, the organization should be mindful that adversaries may attempt to use data mining capabilities built into the application in order to completely extract application data so it can be evaluated using methods that are not natively offered by the application. This can provide the adversary with an opportunity to utilize inference attacks or obtain additional insights that might not have been intended when the application was designed.

Methods of extraction include database queries or screen scrapes using the application itself. The entity performing the data mining must have access to the application in order to extract the data. Data mining attacks will usually occur with publicly releasable data access but can also occur when access is limited to authorized or authenticated inside users.

Data storage objects include, for example, databases, database records, and database fields.

Data mining prevention and detection techniques include, for example: limiting the types of responses provided to database queries; limiting the number/frequency of database queries to increase the work factor needed to determine the contents of such databases; and notifying organizational personnel when atypical database queries or accesses occur.

### Check Text

Review the security plan, application and system documentation and interview the application administrator to identify data mining protections that are required of the application.

If there are no data mining protections required, this requirement is not applicable.

Review the application authentication requirements and permissions.

Review documented protections that have been established to protect from data mining.

This can include limiting the number of queries allowed.

Automated alarming on atypical query events.

Limiting the number of records allowed to be returned in a query.

Not allowing data dumps.

If the application requirements specify protections for data mining and the application administrator is unable to identify or demonstrate that the protections are in place, this is a finding.

**Check ID:**  C-24094r493180_chk

### Fix Text 

Utilize and implement data mining protections when requirements specify it.

**Fix ID:**  F-24083r493181_fix

**Vulnerability ID:**  V-222424

**Rule ID:**  SV-222424r961305_rule

---

## The application must enforce approved authorizations for logical access to information and system resources in accordance with applicable access control policies.

<span style="color:#ff0000;font-size:150%;">High Severity</span>

### Description

To mitigate the risk of unauthorized access to sensitive information by entities that have been issued certificates by DoD-approved PKIs, all DoD systems (e.g., networks, web servers, and web portals) must be properly configured to incorporate access control methods that do not rely solely on the possession of a certificate for access. 

Successful authentication must not automatically give an entity access to a restricted asset or security boundary.

Authorization procedures and controls must be implemented to ensure each authenticated entity also has a validated and current authorization.

Authorization is the process of determining whether an entity, once authenticated, is permitted to access a specific asset.

Information systems use access control policies and enforcement mechanisms to implement this requirement.

Access control policies include identity-based policies, role-based policies, and attribute-based policies.

Access enforcement mechanisms include access control lists, access control matrices, and cryptography.

These policies and mechanisms must be employed by the application to control access between users (or processes acting on behalf of users) and objects (e.g., devices, files, records, processes, programs, and domains) in the information system.

This requirement is applicable to access control enforcement applications (e.g., authentication servers) and other applications that perform information and system access control functions.

### Check Text

Review the application documentation and interview the application administrator.

Review application data protection requirements.

Identify application resources that require protection and authentication over and above the authentication required to access the application itself.

This can be access to a URL, a folder, a file, a process or a database record that should only be available to certain individuals.

Identify the access control methods utilized by the application in order to control access to the resource.

Examples include Role-Based Access Control policies (RBAC).

Using RBAC as an example, utilize a test account placed into a test role.

Set a protection control on a resource and explicitly deny access to the role assigned to the test user account.

Try to access an application resource that is not configured to allow access. Access should be denied.

If the enforcement of configured access restrictions is not performed, this is a finding.

**Check ID:**  C-24095r493183_chk

### Fix Text 

Design or configure the application to enforce access to application resources.

**Fix ID:**  F-24084r493184_fix

**Vulnerability ID:**  V-222425

**Rule ID:**  SV-222425r960792_rule

---

## The application must enforce organization-defined discretionary access control policies over defined subjects and objects.

<span style="color:#ff8c00;font-size:150%;">Medium Severity</span>

### Description

Discretionary Access Control allows users to determine who is allowed to access their data. To mitigate the risk of unauthorized access to sensitive information by entities that have been issued certificates by DoD-approved PKIs, all DoD systems (e.g., networks, web servers, and web portals) must be properly configured to incorporate access control methods that do not rely solely on the possession of a certificate for access. Successful authentication must not automatically give an entity access to an asset or security boundary. Authorization procedures and controls must be implemented to ensure each authenticated entity also has a validated and current authorization. Authorization is the process of determining whether an entity, once authenticated, is permitted to access a specific asset. Information systems use access control policies and enforcement mechanisms to implement this requirement.

Access control policies include identity-based policies, role-based policies, and attribute-based policies. Access enforcement mechanisms include access control lists, access control matrices, and cryptography. These policies and mechanisms must be employed by the application to control access between users (or processes acting on behalf of users) and objects (e.g., devices, files, records, processes, programs, and domains) in the information system.

This requirement is applicable to access control enforcement applications (e.g., authentication servers) and other applications that perform information and system access control functions.

### Check Text

Review the application documentation and interview the application administrator.

Review application data protection requirements and application integrated access control methods.

Identify if the application implements discretionary access control to application resources. Discretionary Access Controls (DAC) allows application users to determine and set permissions on application data and application objects. The result is the user is given the ability to control who has access to the data they control.

If the application does not implement discretionary access controls, this requirement is not applicable.

Resources can be a URL, a folder, a file, a process, a database record, or any other application asset that warrants sharing or authorization permission reassignment.

Create 3 test accounts.

Using test account 1 set protection control on a test user 1 controlled resource.

Grant access to test user 2 and only test user 2.

Authenticate as test user 3 and attempt to access the application resource where test user 1 and test user 2 are granted access. Access should be denied.

If the enforcement of configured access restrictions is not performed, this is a finding.

**Check ID:**  C-24096r493186_chk

### Fix Text 

Design and configure the application to enforce discretionary access control policies.

**Fix ID:**  F-24085r493187_fix

**Vulnerability ID:**  V-222426

**Rule ID:**  SV-222426r961317_rule

---

## The application must enforce approved authorizations for controlling the flow of information within the system based on organization-defined information flow control policies.

<span style="color:#ff8c00;font-size:150%;">Medium Severity</span>

### Description

A mechanism to detect and prevent unauthorized communication flow must be configured or provided as part of the system design. If information flow is not enforced based on approved authorizations, the system may become compromised. Information flow control regulates where information is allowed to travel within a system and between interconnected systems. The flow of all system information must be monitored and controlled so it does not introduce any unacceptable risk to the systems or data.

Application specific examples of enforcement occurs in systems that employ rule sets or establish configuration settings that restrict information system services, or message-filtering capability based on message content (e.g., implementing key word searches or using document characteristics).

This is usually established by identifying if there are rulesets, policies or other configurations settings provided by the application which serve to control the flow of information within the system. Control of data flow is established by using labels on data and data subsets, evaluating the destination of the data within or without the system (similar security domain) and referencing a corresponding policy that is used to control the flow of data.

Applications providing information flow control must be able to enforce approved authorizations for controlling the flow of information within the system in accordance with applicable policy.

### Check Text

Review the application documentation and interview the application and system administrators.

Review application features and functions to determine if the application is designed to control the flow of information within the system.
Identify:

- rulesets,
- data labels, and
- policies

to determine if the application is designed to control the flow of data within the system.

If the application does not provide data flow control capabilities, the requirement is not applicable.

Access the system as a user with access rights that allow the creation of test data or use of existing test data.

Create a test data set and label the data with a data label provided with or by the application, e.g., Personally Identifiable Information (PII) data.

Review the policy to determine where in the system the PII labeled data is allowed and is not allowed to go.

Using application features and functions, attempt to transmit the labeled data to an area that is prohibited by policy.

Verify the flow control policy was enforced and the data was not transmitted.

If the application does not enforce the approved authorizations for controlling data flow, this is a finding.

**Check ID:**  C-24097r493189_chk

### Fix Text 

Configure the application to enforce data flow control in accordance with data flow control policies.

**Fix ID:**  F-24086r493190_fix

**Vulnerability ID:**  V-222427

**Rule ID:**  SV-222427r960801_rule

---

## The application must enforce approved authorizations for controlling the flow of information between interconnected systems based on organization-defined information flow control policies.

<span style="color:#ff8c00;font-size:150%;">Medium Severity</span>

### Description

A mechanism to detect and prevent unauthorized communication flow must be configured or provided as part of the system design. If information flow is not enforced based on approved authorizations, the system may become compromised. Information flow control regulates where information is allowed to travel within a system and between interconnected systems. The flow of all system information must be monitored and controlled so it does not introduce any unacceptable risk to the systems or data.

Application specific examples of enforcement occurs in systems that employ rule sets or establish configuration settings that restrict information system services, or message-filtering capability based on message content (e.g., implementing key word searches or using document characteristics).

This is usually established by identifying if there are rulesets, policies or other configurations settings provided by the application which serve to control the flow of information within the system. Control of data flow is established by using labels on data and data subsets, evaluating the destination of the data within or without the system (similar security domain) and referencing a corresponding policy that is used to control the flow of data.

Applications providing information flow control must be able to enforce approved authorizations for controlling the flow of information within the system in accordance with applicable policy.

### Check Text

Review the application documentation and interview the application and system administrators.

Identify application features and functions to determine if the application is designed to control the flow of information between interconnected systems.

Identify:

- rulesets,
- data labels
- policies
- systems

to determine if the application is designed to control the flow of data between interconnected systems.

If the application does not provide data flow control capabilities, the requirement is not applicable.

Access the system as a user with access rights allowing the creation of test data or use of existing test data.

Create a test data set and label the data with a data label provided with or by the application (for example, a Personally Identifiable Information (PII) data label).

Review the policy settings to determine where the PII labeled data is allowed and is not allowed.

Using application features and functions, attempt to transmit the labeled data to an interconnected system that is prohibited by policy.

Verify the flow control policy was enforced and the data was not transmitted.

If the application does not enforce the approved authorizations for controlling data flow, this is a finding.

**Check ID:**  C-24098r493192_chk

### Fix Text 

Configure the application to enforce data flow control in accordance with data flow control policies.

**Fix ID:**  F-24087r493193_fix

**Vulnerability ID:**  V-222428

**Rule ID:**  SV-222428r960804_rule

---

## The application must prevent non-privileged users from executing privileged functions to include disabling, circumventing, or altering implemented security safeguards/countermeasures.

<span style="color:#ff8c00;font-size:150%;">Medium Severity</span>

### Description

Preventing non-privileged users from executing privileged functions mitigates the risk that unauthorized individuals or processes may gain unnecessary access to information or privileges.

Privileged functions include, for example, establishing accounts, performing system integrity checks, or administering cryptographic key management activities. Non-privileged users are individuals that do not possess appropriate authorizations. Circumventing intrusion detection and prevention mechanisms or malicious code protection mechanisms are examples of privileged functions that require protection from non-privileged users.

### Check Text

Identify the application user account(s) that the application uses to run. These accounts include the application processes (defined by Control Panel Services (Windows) or ps –ef (UNIX)) or for an n-tier application, the account that connects from one service (such as a web server) to another (such as a database server).

Determine the OS user groups in which each account is a member.

List the user rights assigned to these users and groups and evaluate whether any of them are unnecessary.

If the OS rights exceed application operational requirements, this is a finding.

If the application user account is a member of the Administrators group (Windows) or has a User Identification (UID) of 0 (i.e., is equivalent to root in UNIX), this is a finding.

Search the file system to determine if the application user or groups have ownership or permissions to any files or directories.

Review the list of files and identify any that are outside the scope of the application.

If there are such files outside the scope of the application, this is a finding.

Check ownership and permissions; identify permissions beyond the minimum necessary to support the application.

If there are instances of unnecessary ownership or permissions, this is a finding.

The finding details should note the full path of the file(s) and the associated issue (i.e., outside scope, permissions improperly granted to user X, etc.).

**Check ID:**  C-24099r493195_chk

### Fix Text 

Modify the application to limit access and prevent the disabling or circumvention of security safeguards.

**Fix ID:**  F-24088r493196_fix

**Vulnerability ID:**  V-222429

**Rule ID:**  SV-222429r961353_rule

---

## The application must execute without excessive account permissions.

<span style="color:#ff0000;font-size:150%;">High Severity</span>

### Description

Applications are often designed to utilize a user account.  The account represents a means to control application permissions and access to OS resources, application resources or both.  

When the application is designed and installed, care must be taken not to assign excessive permissions to the user account that is used by the application.  

An application operating with unnecessary privileges can potentially give an attacker access to the underlying operating system or if the privileges required for application execution are at a higher level than the privileges assigned to organizational users invoking such applications/programs, those users are indirectly provided with greater privileges than assigned by organizations.

Applications must be designed and configured to operate with only those permissions that are required for proper operation.

### Check Text

Review the system documentation or interview the application representative and identify if the application utilizes an account in order to operate.

Determine the OS user groups in which each application account is a member.  List the user rights assigned to these users and groups using relevant OS commands and evaluate whether any of them provide admin rights or if they are unnecessary or excessive. 

If the application connects to a database, open an admin console to the database and view the database users, their roles and group rights.

Locate the application user account used to access the database and examine the accounts privileges. This includes group privileges.

If the application user account has excessive OS privileges such as being in the admin group, database privileges such as being in the DBA role, has the ability to create, drop, alter the database (not application database tables), or if the application user account has other excessive or undefined system privileges, this is a finding.

**Check ID:**  C-24100r493198_chk

### Fix Text 

Configure the application accounts with minimalist privileges. Do not allow the application to operate with admin credentials.

**Fix ID:**  F-24089r493199_fix

**Vulnerability ID:**  V-222430

**Rule ID:**  SV-222430r961359_rule

---

## The application must audit the execution of privileged functions.

<span style="color:#ff8c00;font-size:150%;">Medium Severity</span>

### Description

Misuse of privileged functions, either intentionally or unintentionally by authorized users, or by unauthorized external entities that have compromised information system accounts, is a serious and ongoing concern and can have significant adverse impacts on organizations. Auditing the use of privileged functions is one way to detect such misuse, and identify the risk from insider threats and the advanced persistent threat.

### Check Text

Log on to the application as an administrative user.

Identify functionality within the application that requires utilizing the admin role.

Monitor application logs while performing privileged functions within the application.

Perform administrative types of tasks such as adding or modifying user accounts, modifying application configuration, or managing encryption keys.

Review logs for entries that indicate the administrative actions performed were logged.

Ensure the specific action taken, date and time or event is recorded.

If the execution of privileged functionality is not logged, this is a finding.

**Check ID:**  C-24101r493201_chk

### Fix Text 

Configure the application to write log entries when privileged functions are executed. At a minimum, ensure the specific action taken, date and time of event are recorded.

**Fix ID:**  F-24090r493202_fix

**Vulnerability ID:**  V-222431

**Rule ID:**  SV-222431r961362_rule

---

## The application must enforce the limit of three consecutive invalid logon attempts by a user during a 15 minute time period.

<span style="color:#ff0000;font-size:150%;">High Severity</span>

### Description

By limiting the number of failed logon attempts, the risk of unauthorized system access via user password guessing, otherwise known as brute forcing, is reduced.

Limits are imposed by locking the account.

User notification when three failed logon attempts are exceeded is an operational consideration determined by the application owner. In some instances the operational situation may dictate that no notice is to be provided to the user when their account is locked. In other situations, the user may be notified their account is now locked. This decision is left to the application owner based upon their operational scenarios.

### Check Text

All testing must be performed within a 15-minute window.

Log on to the application with a test user account.

Intentionally enter an incorrect user password or pin.

Repeat 2 times within 15 minutes for a total of three failed attempts.

Notification of a locked account may or may not be provided.

Using the correct user password or pin, attempt to logon a 4th time.

If the logon is successful upon the 4th attempt the account was not locked after the third failed attempt and this is a finding.

**Check ID:**  C-24102r493204_chk

### Fix Text 

Configure the application to enforce an account lock after 3 failed logon attempts occurring within a 15-minute window.

**Fix ID:**  F-24091r493205_fix

**Vulnerability ID:**  V-222432

**Rule ID:**  SV-222432r960840_rule

---

## The application administrator must follow an approved process to unlock locked user accounts.

<span style="color:#ff8c00;font-size:150%;">Medium Severity</span>

### Description

Once a user account has been locked, it must be unlocked by an administrator.

An ISSM and ISSO approved process must be created and followed to ensure the user requesting access is properly authenticated prior to access being re-established.

The process must include having the user provide information only the user would know and having the administrator verify the accuracy of the information prior to unlocking the account. This means having the user provide this information when their account is created so the information can be referenced when they are locked out.    

The process utilized may be manual in nature, however it is recognized that password resets are a time consuming task. To minimize helpdesk resource constraints related to user lockout requests, procedures may be automated by administrators in order to unlock the account or reset the password.  

Authentication process examples include having the user provide personal information known only by the user and provided when the account was created and/or using Out-of-Band or side channel communication methods such as text messages to the users established cell phone number in order to provide a temporary password or token that can be used to logon once and reset the password.

The OWASP site provides an acceptable password reset process that can be used as a reference.  https://www.owasp.org/index.php/Forgot_Password_Cheat_Sheet.  

Automated procedures should follow industry standards and best practice for securely automating password reset/account unlocks and must be reviewed, tested, and then approved by the ISSM and ISSO.

### Check Text

Interview the application administrator and identify the approved process for unlocking user accounts.

The process may involve a manual or automated reset after the locked out user has identified themselves using standard user identification processes outlined in the vulnerability discussion.

If the admin does not unlock the account following the approved process, and if the process does not have documented ISSO and ISSM approvals, this is a finding.

**Check ID:**  C-24103r493207_chk

### Fix Text 

Create a standard approved process for unlocking locked application accounts which includes validating user identity prior to unlocking the account.

Use that process when unlocking application user accounts.

**Fix ID:**  F-24092r493208_fix

**Vulnerability ID:**  V-222433

**Rule ID:**  SV-222433r961368_rule

---

## The application must display the Standard Mandatory DoD Notice and Consent Banner before granting access to the application.

<span style="color:#b3b31a;font-size:150%;">Low Severity</span>

### Description



### Check Text

If the application has no interactive user interface, this requirement is not applicable.

Log on to the application as a user.

Observe the screen and ensure the DoD-approved banner is displayed prior to obtaining access to the application. Refer to the vulnerability discussion for the approved text.

If the only way to access the application is through the OS console, e.g., a fat client application installed on a GFE desktop or laptop, and that GFE is configured to display the DoD banner, an additional banner is not required at the application level.

If the standard DoD-approved banner is not displayed prior to obtaining access, this is a finding.

**Check ID:**  C-24104r493210_chk

### Fix Text 

Configure the application to present the standard DoD-approved banner prior to granting access to the application.

**Fix ID:**  F-24093r493211_fix

**Vulnerability ID:**  V-222434

**Rule ID:**  SV-222434r960843_rule

---

## The application must retain the Standard Mandatory DoD Notice and Consent Banner on the screen until users acknowledge the usage conditions and take explicit actions to log on for further access.

<span style="color:#b3b31a;font-size:150%;">Low Severity</span>

### Description

The banner must be acknowledged by the user prior to allowing the user access to the application. This provides assurance that the user has seen the message and accepted the conditions for access. If the consent banner is not acknowledged by the user, DoD will not be in compliance with system use notifications required by law.

To establish acceptance of the application usage policy, a click-through banner at application logon is required. The application must prevent further activity until the user executes a positive action to manifest agreement by clicking on a box indicating "OK".

### Check Text

If the application has no interactive user interface, this requirement is not applicable.

If the user interface is only available via the OS console, e.g., a fat client application installed on a GFE desktop or laptop, and that GFE is configured to display the DoD banner, this requirement is not applicable.

Access the application and authenticate if necessary. Verify the banner is displayed and action must be taken to accept terms of use.

If the banner is not displayed or no action must be taken to accept terms of use, this is a finding.

**Check ID:**  C-24105r493213_chk

### Fix Text 

Configure the application to retain the standard DoD-approved banner until the user accepts the usage conditions prior to granting access to the application.

**Fix ID:**  F-24094r493214_fix

**Vulnerability ID:**  V-222435

**Rule ID:**  SV-222435r960846_rule

---

## The publicly accessible application must display the Standard Mandatory DoD Notice and Consent Banner before granting access to the application.

<span style="color:#b3b31a;font-size:150%;">Low Severity</span>

### Description



### Check Text

This requirement only applies to publicly accessible applications. If the application is not publicly accessible, this requirement is not applicable.

Access the application and observe the screen to ensure the DoD-approved banner is displayed prior to obtaining full access to the application. Refer to the vulnerability discussion for the approved banner text.

If the standard DoD-approved banner is not displayed prior to obtaining access, this is a finding.

**Check ID:**  C-24106r493216_chk

### Fix Text 

Configure the application to present the standard DoD-approved banner prior to granting access to the application.

**Fix ID:**  F-24095r493217_fix

**Vulnerability ID:**  V-222436

**Rule ID:**  SV-222436r960849_rule

---

## The application must display the time and date of the users last successful logon.

<span style="color:#b3b31a;font-size:150%;">Low Severity</span>

### Description

Providing a last successful logon date and time stamp notification to the user when they authenticate and access the application allows the user to determine if their application account has been used without their knowledge. 

Armed with that information, the user can notify the application administrator and initiate a forensics investigation to identify root cause.  Without providing this information to the user, a potential compromise of user accounts could go unnoticed.

### Check Text

Review the application documentation and interview the application administrator.

If the application does not provide a user interface, this requirement is not applicable.

Logon to the application as a test user and verify successful authentication by creating test data, navigating the application functionality or otherwise utilizing the application.

Note the date and time access was granted.

Log out of the application.

Re-authenticate to the application as the same user.

Validate the last logon date and time is displayed in the user interface. 

If the date and time the user account was last granted access to the application is not displayed in the user interface, this is a finding.

**Check ID:**  C-24107r493219_chk

### Fix Text 

Design and configure the application to display the date and time when the user was last successfully granted access to the application.

**Fix ID:**  F-24096r493220_fix

**Vulnerability ID:**  V-222437

**Rule ID:**  SV-222437r987626_rule

---

## The application must protect against an individual (or process acting on behalf of an individual) falsely denying having performed organization-defined actions to be covered by non-repudiation.

<span style="color:#ff8c00;font-size:150%;">Medium Severity</span>

### Description

Without non-repudiation, it is impossible to positively attribute an action to an individual (or process acting on behalf of an individual).

Non-repudiation services can be used to determine if information originated from a particular individual, or if an individual took specific actions (e.g., sending an email, signing a contract, approving a procurement request) or received specific information. Non-repudiation protects individuals against later claims by an author of not having authored a particular document, a sender of not having transmitted a message, a receiver of not having received a message, or a signatory of not having signed a document. The application will be configured to provide non-repudiation services for an organization-defined set of commands that are used by the user (or processes action on behalf of the user).

DoD PKI provides for non-repudiation through the use of digital signatures. Non-repudiation requirements will vary from one application to another and will be defined based on application functionality, data sensitivity, and mission requirements.

### Check Text

Review the application documentation, the design requirements if available and interview the application administrator.

Identify application services or application commands that are formerly required and designed to provide non-repudiation services (e.g., digital signatures).  

If the application documentation specifically states that non-repudiation services for application users are not defined as part of the application design, this requirement is not applicable.  

Email is one example of an application specifically required to provide non-repudiation services for application users within the DoD. 

Interview the application administrators and have them describe which aspect of the application, if any, is required to provide digital signatures.

Access the application as a test user or observe the application administrator as they demonstrate the applications signature capabilities.

If the application is required to provide non-repudiation services and does not, or if the non-repudiation functionality fails on demonstration, this is a finding.

**Check ID:**  C-24108r493222_chk

### Fix Text 

Configure the application to provide users with a non-repudiation function in the form of digital signatures when it is required by the organization or by the application design and architecture.

**Fix ID:**  F-24097r493223_fix

**Vulnerability ID:**  V-222438

**Rule ID:**  SV-222438r960864_rule

---

## For applications providing audit record aggregation, the application must compile audit records from organization-defined information system components into a system-wide audit trail that is time-correlated with an organization-defined level of tolerance for the relationship between time stamps of individual records in the audit trail.

<span style="color:#ff8c00;font-size:150%;">Medium Severity</span>

### Description

Without the ability to collate records based on the time when the events occurred, the ability to perform forensic analysis and investigations across multiple components is significantly degraded.

Audit trails are time-correlated if the time stamps in the individual audit records can be reliably related to the time stamps in other audit records to achieve a time ordering of the records within organization-defined level of tolerance.

This requirement applies to applications which provide the capability to compile system-wide audit records for multiple systems or system components. However, all applications must provide the relevant log details that are used to aggregate the information.

### Check Text

Review the application documentation and interview the application administrator.

Determine if the application has the ability to compile audit records from multiple systems or system components.

If the application does not provide log aggregation services, this requirement is not applicable.

Identify the systems that comprise the application.

Access each system comprising the application or a random sample of several application systems. Review the application logs and obtain date and time stamps for several random audit events. Record the information.

Access the server providing the log aggregation. Access the application logs that have been written to the server and compare the samples obtained from the application systems to the aggregated logs. Ensure the dates and time stamps correlate with one another.

If the log dates and times do not correlate when the logs are aggregated, this is a finding.

**Check ID:**  C-36237r602277_chk

### Fix Text 

Configure the application to correlate time stamps when aggregating audit records.

**Fix ID:**  F-36204r602278_fix

**Vulnerability ID:**  V-222439

**Rule ID:**  SV-222439r960873_rule

---

## The application must provide audit record generation capability for the creation of session IDs.

<span style="color:#ff8c00;font-size:150%;">Medium Severity</span>

### Description

Applications create session IDs at the onset of a user session in order to manage user access to the application and differentiate between different user sessions. It is important to log the creation of these session ID creation events for forensic purposes.

It is equally important to not log the session ID itself. Logging the session ID puts active sessions at risk if log data is compromised. Specific session ID information should be removed, masked, sanitized, or encrypted.

A hash value of the session ID that can be mapped to the session ID is an acceptable method for assuring active session protection when logging session ID information. Alternatively, logging protections that protect the logs and defend from unauthorized access are means to assure log confidentiality and protect session integrity.

Web based applications will often utilize an application server that creates, manages and logs user session IDs.  It is acceptable for the application to delegate this requirement to the application server.

### Check Text

Access the management interface for the application or configuration file and evaluate the log/audit management settings.

Determine if the setting that enables session ID creation event auditing is activated.

Create a new user session by logging in to the application.

Review the logs to ensure the session creation event was recorded.

If the application is not configured to log session ID creation events, or if no creation event was recorded, this is a finding.

If a web-based application delegates session ID creation to an application server, this is not a finding. 

If the application generates session ID creation event logs by default, and that behavior cannot be disabled, this is not a finding.

**Check ID:**  C-24111r493231_chk

### Fix Text 

Enable session ID creation event auditing.

**Fix ID:**  F-24100r493232_fix

**Vulnerability ID:**  V-222441

**Rule ID:**  SV-222441r960879_rule

---

## The application must provide audit record generation capability for the destruction of session IDs.

<span style="color:#ff8c00;font-size:150%;">Medium Severity</span>

### Description

Applications should destroy session IDs at the end of a user session in order to terminate user access to the application session and to reduce the possibility of an unauthorized attacker high jacking the session and impersonating the user. It is important to log when session IDs are destroyed for forensic purposes.

Web based applications will often utilize an application server that creates, manages and logs session IDs.  It is acceptable for the application to delegate this requirement to the application server.

### Check Text

Access the management interface for the application or configuration file and evaluate the log/audit management settings.

Determine if the setting that enables session ID destruction event auditing is activated.

Terminate a user session within the application and review the logs to ensure the session destruction event was recorded.

If the application is not configured to log session ID destruction events, or if the application has no means to enable auditing of session ID destruction events, this is a finding.

If a web-based application delegates session ID destruction to an application server, this is not a finding. 

If the application generates audit logs by default when session IDs are destroyed, and that behavior cannot be disabled, this is not a finding.

**Check ID:**  C-24112r493234_chk

### Fix Text 

Enable session ID destruction event auditing.

**Fix ID:**  F-24101r493235_fix

**Vulnerability ID:**  V-222442

**Rule ID:**  SV-222442r960879_rule

---

## The application must provide audit record generation capability for the renewal of session IDs.

<span style="color:#ff8c00;font-size:150%;">Medium Severity</span>

### Description

Application design sometimes requires the renewal of session IDs in order to continue approved user access to the application.

Session renewal is done on a case by case basis under circumstances defined by the application architecture. The following are some examples of when session renewal must be done; whenever there is a change in user privilege such as transitioning from a user to an admin role or when a user changes from an anonymous user to an authenticated user or when a user's permissions have changed.

For these types of critical application functionalities, the previous session ID needs to be destroyed or otherwise invalidated and a new session ID must be created.

It is important to log when session IDs are renewed for forensic purposes.

Web based applications will often utilize an application server that creates, manages and logs session IDs.  It is acceptable for the application to delegate this requirement to the application server.

### Check Text

Interview the system admin and review the application documentation.

Identify any web pages or application functionality where a user's privileges or permissions will change. This is most likely to occur during the authentication stages.

Evaluate the log/audit output by opening the log files and observing changes to the logs.

Create a new user session by accessing the application.

Review the logs and save the relevant session creation event recorded.

Utilize the application pages that provide privilege escalation.

Escalate privileges by authenticating as a privileged user.

Review the logs and determine if new session information is created and being used.

If a web-based application delegates session ID renewals to an application server, this is not a finding. 

If the application is not configured to log session ID renewal events this is a finding.

**Check ID:**  C-24113r493237_chk

### Fix Text 

Design or reconfigure the application to log session renewal events on those application events that provide changes in the users privileges or permissions to the application.

**Fix ID:**  F-24102r493238_fix

**Vulnerability ID:**  V-222443

**Rule ID:**  SV-222443r960879_rule

---

## The application must not write sensitive data into the application logs.

<span style="color:#ff8c00;font-size:150%;">Medium Severity</span>

### Description

It is important to identify and exclude certain types of data that is written into the logs. If the logs are compromised and sensitive data is included in the logs, this could assist an attacker in furthering their attack or it could completely compromise the system.

Examples of such data include but are not limited to; Passwords, Session IDs, Application source code, encryption keys, and sensitive data such as personal health information (PHI), Personally Identifiable Information (PII), or government identifiers (e.g., SSN).

### Check Text

Review the application logs and identify application logging format. Using the format of the log and the requisite search data as a guide to create your search, create search strings that could successfully identify the existence of passwords, session IDs, or other sensitive information such as SSN.

Utilizing the UNIX grep-based search utility include the following examples which are meant to illustrate the purpose of the requirement.

Password values are usually associated with usernames so searching for "username" in the provided log file will often assist in determining if password values are included.

grep -i "username" <  logfile.txt

Search for social security numbers in the provided log file.

grep -i "[0-9]{3}[-]?[0-9]{2}[-]?[0-9]{4}" <  logfile.txt

Use regular expressions to aid in searching log files. All search syntax cannot be provided within the STIG, the reviewer must utilize their knowledge to create new search criteria based upon the log format used and the potentially sensitive data processed by the application.

If the application logs sensitive data such as session IDs, application source code, encryption keys, or passwords, this is a finding.

**Check ID:**  C-24114r493240_chk

### Fix Text 

Design or reconfigure the application to not write sensitive data to the logs.

**Fix ID:**  F-24103r493241_fix

**Vulnerability ID:**  V-222444

**Rule ID:**  SV-222444r960879_rule

---

## The application must provide audit record generation capability for session timeouts.

<span style="color:#ff8c00;font-size:150%;">Medium Severity</span>

### Description

When a user's session times out, it is important to be able to identify these events in the application logs.

Without the capability to generate audit records, it would be difficult to establish, correlate, and investigate the events relating to an incident, or identify those responsible for one.

Audit records can be generated from various components within the application (e.g., process, module). Certain specific application functionalities may be audited as well. The list of audited events is the set of events for which audits are to be generated. This set of events is typically a subset of the list of all events for which the system is capable of generating audit records.

DoD has defined the list of events for which the application will provide an audit record generation capability as the following:

(i) Successful and unsuccessful attempts to access, modify, or delete privileges, security objects, security levels, or categories of information (e.g., classification levels);

(ii) Access actions, such as successful and unsuccessful logon attempts, privileged activities or other system level access, starting and ending time for user access to the system, concurrent logons from different workstations, successful and unsuccessful accesses to objects, all program initiations, and all direct access to the information system; and

(iii) All account creation, modification, disabling, and termination actions.

Web-based applications will often utilize an application server that creates, manages, and logs session timeout information. It is acceptable for the application to delegate this requirement to the application server.

### Check Text

Review the application documentation and interview the application administrator to identify log locations for application session activity.

Open the log file that tracks user session activity.

Access the application as a regular user and identify the user session within the log files.

Identify the session timeout threshold defined by the application.

Perform no action within the application in order to allow the session to timeout.

Once the session timeout threshold has been exceeded, verify the session has been terminated due to the timeout event and review the logs again to ensure the session timeout event was recorded in the logs.

If a web-based application delegates session timeout auditing to an application server, this is not a finding. 

If the session timeout event is not recorded in the logs, this is a finding.

**Check ID:**  C-24115r493243_chk

### Fix Text 

Configure the application to record session timeout events in the logs.

**Fix ID:**  F-24104r493244_fix

**Vulnerability ID:**  V-222445

**Rule ID:**  SV-222445r960879_rule

---

## The application must record a time stamp indicating when the event occurred.

<span style="color:#ff8c00;font-size:150%;">Medium Severity</span>

### Description

It is important to include the time stamps for when an event occurred. Failure to include time stamps in the event logs is detrimental to forensic analysis.

### Check Text

Review the application logs.

If the time the event occurred is not included as part of the event, this is a finding.

**Check ID:**  C-24116r493246_chk

### Fix Text 

Configure the application to record the time the event occurred when recording the event.

**Fix ID:**  F-24105r493247_fix

**Vulnerability ID:**  V-222446

**Rule ID:**  SV-222446r960879_rule

---

## The application must provide audit record generation capability for HTTP headers including User-Agent, Referer, GET, and POST.

<span style="color:#ff8c00;font-size:150%;">Medium Severity</span>

### Description

HTTP header information is a critical component of data that is used when evaluating forensic activity.

Without the capability to generate audit records, it would be difficult to establish, correlate, and investigate the events relating to an incident, or identify those responsible for one.

Audit records can be generated from various components within the application (e.g., process, module). Certain specific application functionalities may be audited as well. The list of audited events is the set of events for which audits are to be generated. This set of events is typically a subset of the list of all events for which the system is capable of generating audit records.

DoD has defined the list of events for which the application will provide an audit record generation capability as the following:

(i) Successful and unsuccessful attempts to access, modify, or delete privileges, security objects, security levels, or categories of information (e.g., classification levels);

(ii) Access actions, such as successful and unsuccessful logon attempts, privileged activities or other system level access, starting and ending time for user access to the system, concurrent logons from different workstations, successful and unsuccessful accesses to objects, all program initiations, and all direct access to the information system; and

(iii) All account creation, modification, disabling, and termination actions.

### Check Text

Review the application documentation and interview the application administrator to identify log locations for application session activity.

Open the log file that tracks user session activity.

Access the application as a regular user and identify the user session within the log files.

Perform several actions within the application in order to generate HTTP header traffic.

Review the logs to ensure the HTTP header information is recorded in the logs. Header information logged will vary based upon the application and environment. Examples of headers include but are not limited to:

User-Agent:
Referer:
X-Forwarded-For:
Date:
Expires:

If HTTP headers are not logged, this is a finding.

**Check ID:**  C-24117r493249_chk

### Fix Text 

Configure the web application and/or the web server to log HTTP headers.

**Fix ID:**  F-24106r493250_fix

**Vulnerability ID:**  V-222447

**Rule ID:**  SV-222447r960879_rule

---

## The application must provide audit record generation capability for connecting system IP addresses.

<span style="color:#ff8c00;font-size:150%;">Medium Severity</span>

### Description

Without the capability to generate audit records, it would be difficult to establish, correlate, and investigate the events relating to an incident, or identify those responsible for one.

Audit records can be generated from various components within the application (e.g., process, module). Certain specific application functionalities may be audited as well. The list of audited events is the set of events for which audits are to be generated. This set of events is typically a subset of the list of all events for which the system is capable of generating audit records.

The IP addresses of remote systems that connect to the application are an important aspect of identifying the sources of application activity. Recording these IP addresses in the application logs provides forensic evidence and aids in investigating and identifying sources of malicious behavior related to security events.

### Check Text

Review the application documentation and interview the application administrator to identify where audit logs are stored.

Review audit logs and determine if the IP address information of systems that connect to the application is kept in the logs.

If connecting IP addresses are not seen in the logs, connect to the application remotely and review the logs to determine if the connection was logged.

If the IP addresses of the systems that connect to the application are not recorded in the logs, this is a finding.

**Check ID:**  C-24118r493252_chk

### Fix Text 

Configure the application or application server to log all connecting IP address information

**Fix ID:**  F-24107r493253_fix

**Vulnerability ID:**  V-222448

**Rule ID:**  SV-222448r960879_rule

---

## The application must record the username or user ID of the user associated with the event.

<span style="color:#ff8c00;font-size:150%;">Medium Severity</span>

### Description

When users conduct activity within an application, that user’s identity must be recorded in the audit log. Failing to record the identity of the user responsible for the activity within the application is detrimental to forensic analysis.

### Check Text

Review and monitor the application logs.

Connect to the application and perform application activity that is allowed by the user such as accessing data or running reports.

Observe if the log includes an entry to indicate the user ID of the user that conducted the activity.

If the user ID is not recorded along with the event in the event log, this is a finding.

**Check ID:**  C-24119r493255_chk

### Fix Text 

Configure the application to record the user ID of the user responsible for the log event entry.

**Fix ID:**  F-24108r493256_fix

**Vulnerability ID:**  V-222449

**Rule ID:**  SV-222449r960879_rule

---

## The application must generate audit records when successful/unsuccessful attempts to grant privileges occur.

<span style="color:#ff8c00;font-size:150%;">Medium Severity</span>

### Description

Without generating audit records that are specific to the security and mission needs of the organization, it would be difficult to establish, correlate, and investigate the events relating to an incident, or identify those responsible for one.

Audit records can be generated from various components within the information system (e.g., module or policy filter).

When a user is granted access or rights to application features and function not afforded to an ordinary user, they have been granted access to privilege and that action must be logged.

### Check Text

Review the application documentation and interview the application admin to identify application management interfaces and features.

Access the application management utility and create a test user account or use the account of a regular unprivileged user who is cooperating with the testing.

Access and open the auditing logs.

Using an account with the appropriate privileges, grant the user a privilege they previously did not have.

Attempt to grant privileges in a manner that will cause a failure event such as granting privileges to a non-existent user or attempting to grant privileges with an account that doesn't have the rights to do so.

Review the application logs and ensure both events were captured in the logs. The event data should include the user’s identity and the privilege that was granted and the privilege that failed to be granted.

If the application does not log when successful and unsuccessful attempts to grant privilege occur, this is a finding.

**Check ID:**  C-24120r493258_chk

### Fix Text 

Configure the application to audit successful and unsuccessful attempts to grant privileges.

**Fix ID:**  F-24109r493259_fix

**Vulnerability ID:**  V-222450

**Rule ID:**  SV-222450r960885_rule

---

## The application must generate audit records when successful/unsuccessful attempts to access security objects occur.

<span style="color:#ff8c00;font-size:150%;">Medium Severity</span>

### Description

Security objects represent application objects that provide or require security protections or have a security role within the application. Examples include but are not limited to, files, application modules, folders, and database records. Essentially, if permissions are assigned to protect it, it can be considered a security object. Without generating audit records that are specific to the security and mission needs of the organization, it would be difficult to establish, correlate, and investigate the events relating to an incident, or identify those responsible for one.

Audit records can be generated from various components within the information system (e.g., module or policy filter).

### Check Text

Review the application documentation and interview the application administrator.

Identify where the application logs are stored.

Identify application functionality that provides privilege or permission settings to security objects within the application.
This can be an application function that assigns privileges to an application object or data element.

Authenticate to the application as a regular user. Using application functionality, attempt to access the security object within the application.

Perform two attempts, one successfully and one unsuccessfully.

Review the log data and ensure both the successful and unsuccessful access attempts are logged.

If the application does not generate an audit record when successful and unsuccessful attempts to access security objects occur, this is a finding.

**Check ID:**  C-24121r493261_chk

### Fix Text 

Configure the application to create an audit record for both successful and unsuccessful attempts to access security objects.

**Fix ID:**  F-24110r493262_fix

**Vulnerability ID:**  V-222451

**Rule ID:**  SV-222451r961791_rule

---

## The application must generate audit records when successful/unsuccessful attempts to access security levels occur.

<span style="color:#ff8c00;font-size:150%;">Medium Severity</span>

### Description

A security level denotes a permissions or authorization capability within the application. This is most often associated with a user role. Attempts to access a security level can occur when a user attempts an action such as escalating their privilege from within the application itself. Attempts to access a security level can be construed as an attempt to change your user role from within the application. 

Without generating audit records that are specific to the security and mission needs of the organization, it would be difficult to establish, correlate, and investigate the events relating to an incident, or identify those responsible for one. Audit records can be generated from various components within the information system (e.g., module or policy filter).

### Check Text

Review the application documentation and interview the application administrator. Identify where the application logs are stored.

Identify application functionality that provides privilege escalation or access to additional security levels within the application.

This can be performing a function that escalates the privileges of the user, or accessing a protected area of the application that requires additional authentication in order to access.

Authenticate to the application as a regular user. Using application functionality, attempt to access a different security level or domain within the application.

Perform two attempts, one successfully and one unsuccessfully.

Review the log data and ensure both the successful and unsuccessful access attempts are logged.

If the application does not generate an audit record when successful and unsuccessful attempts to access security levels occur, this is a finding.

**Check ID:**  C-24122r493264_chk

### Fix Text 

Configure the application to create an audit record for both successful and unsuccessful attempts to access security levels.

**Fix ID:**  F-24111r493265_fix

**Vulnerability ID:**  V-222452

**Rule ID:**  SV-222452r961794_rule

---

## The application must generate audit records when successful/unsuccessful attempts to access categories of information (e.g., classification levels) occur.

<span style="color:#ff8c00;font-size:150%;">Medium Severity</span>

### Description

Without generating audit records that are specific to the security and mission needs of the organization, it would be difficult to establish, correlate, and investigate the events relating to an incident, or identify those responsible for one.

Categories of information is information that is identified as being sensitive or requiring additional protection from regular user access. The data is accessed on a need to know basis and has been assigned a category or a classification in order to assign protections and track access.

Audit records can be generated from various components within the information system (e.g., module or policy filter).

### Check Text

Review the application documentation and interview the application administrator. Identify where the application logs are stored.

Identify any data protections that are required.

Identify any categories of data or classification of data.

If the application requirements do not call for compartmentalized data and data protection, this requirement is not applicable.

Authenticate to the application as a regular user. Using application functionality, attempt to access data that has been assigned to a protected category.

Perform two access attempts, one successful and one unsuccessful.

Testing this will require obtaining access to test data that has been assigned to a protected category, or having an authorized user access the data for you.

Review the log data and ensure both the successful and unsuccessful access attempts are logged.

If the application does not generate an audit record when successful and unsuccessful attempts to access categories of information occur, this is a finding.

**Check ID:**  C-24123r493267_chk

### Fix Text 

Configure the application to create an audit record for both successful and unsuccessful attempts to access protected categories of information.

**Fix ID:**  F-24112r493268_fix

**Vulnerability ID:**  V-222453

**Rule ID:**  SV-222453r961797_rule

---

## The application must generate audit records when successful/unsuccessful attempts to modify privileges occur.

<span style="color:#ff8c00;font-size:150%;">Medium Severity</span>

### Description

Without generating audit records that are specific to the security and mission needs of the organization, it would be difficult to establish, correlate, and investigate the events relating to an incident, or identify those responsible for one.

Audit records can be generated from various components within the information system (e.g., module or policy filter).

### Check Text

Review the application documentation and interview the application admin to identify application management interfaces and features.

Access the application management utility and create a test user account or use the account of a regular privileged user who is cooperating with the testing.

Access and open the auditing logs.

Using an admin account, modify the privileges of a privileged user.

Attempt to modify privileges in a manner that will cause a failure event such as attempting to modify a user’s privileges with an account that doesn't have the rights to do so.

Review the application logs and ensure both events were captured in the logs. The event data should include the user’s identity and the privilege that was granted and the privilege that failed to be granted.

If the application does not log when successful and unsuccessful attempts to modify privileges occur, this is a finding.

**Check ID:**  C-24124r493270_chk

### Fix Text 

Configure the application to audit successful and unsuccessful attempts to modify privileges.

**Fix ID:**  F-24113r493271_fix

**Vulnerability ID:**  V-222454

**Rule ID:**  SV-222454r961800_rule

---

## The application must generate audit records when successful/unsuccessful attempts to modify security objects occur.

<span style="color:#ff8c00;font-size:150%;">Medium Severity</span>

### Description

Without generating audit records that are specific to the security and mission needs of the organization, it would be difficult to establish, correlate, and investigate the events relating to an incident, or identify those responsible for one.

Audit records can be generated from various components within the information system (e.g., module or policy filter).

### Check Text

Review the application documentation and interview the application administrator.

Identify where the application logs are stored.

Identify application functionality that provides privilege or permission settings to security objects within the application.
This can be an application function that assigns privileges to an application object or data element.

Authenticate to the application as a regular user.  Using application functionality, attempt to modify the security object within the application.

Perform two attempts, one successfully and one unsuccessfully.

Review the log data and ensure the modification events both successful and unsuccessful are logged.

If the application does not generate an audit record when successful and unsuccessful attempts to modify security objects occur, this is a finding.

**Check ID:**  C-24125r493273_chk

### Fix Text 

Configure the application to create an audit record for both successful and unsuccessful attempts to modify security objects.

**Fix ID:**  F-24114r493274_fix

**Vulnerability ID:**  V-222455

**Rule ID:**  SV-222455r961803_rule

---

## The application must generate audit records when successful/unsuccessful attempts to modify security levels occur.

<span style="color:#ff8c00;font-size:150%;">Medium Severity</span>

### Description

A security level denotes a permissions or authorization capability within the application. This is most often associated with a user role. Attempts to modify a security level can be construed as an attempt to change the configuration of the application so as to create a new security role or modify an existing security role. Some applications may or may not provide this capability.

Without generating audit records that are specific to the security and mission needs of the organization, it would be difficult to establish, correlate, and investigate the events relating to an incident, or identify those responsible for one.

Audit records can be generated from various components within the information system (e.g., module or policy filter).

### Check Text

Review the application documentation and interview the application administrator.

Identify where the application logs are stored.

Identify application functionality that provides privilege escalation or access to additional security levels within the application.

This can be performing a function that escalates the privileges of the user, or accessing a protected area of the application that requires additional authentication in order to access.

Authenticate to the application as a regular user. Using application functionality, attempt to modify the permissions of a different security level or domain within the application.

Perform two attempts, one successfully and one unsuccessfully.

Review the log data and ensure the modify events, both successful and unsuccessful, are logged.

If the application does not generate an audit record when successful and unsuccessful attempts to modify the permissions regarding the security levels occur, this is a finding.

**Check ID:**  C-24126r493276_chk

### Fix Text 

Configure the application to create an audit record for both successful and unsuccessful attempts to modify security levels.

**Fix ID:**  F-24115r493277_fix

**Vulnerability ID:**  V-222456

**Rule ID:**  SV-222456r961806_rule

---

## The application must generate audit records when successful/unsuccessful attempts to modify categories of information (e.g., classification levels) occur.

<span style="color:#ff8c00;font-size:150%;">Medium Severity</span>

### Description

Without generating audit records that are specific to the security and mission needs of the organization, it would be difficult to establish, correlate, and investigate the events relating to an incident, or identify those responsible for one.

Audit records can be generated from various components within the information system (e.g., module or policy filter).

### Check Text

Review the application documentation and interview the application administrator.

Identify where the application logs are stored.

Identify any data protections that are required.

Identify any categories of data or classification of data.

If the application requirements do not call for compartmentalized data and data protection, this requirement is not applicable.

Authenticate to the application as a regular user. Using application functionality, attempt to modify data that has been assigned to a protected category.

Perform two modification attempts, one successful and one unsuccessful.

Testing this will require obtaining access to test data that has been assigned to a protected category, or having an authorized user access the data for you.

Review the log data and ensure both the successful and unsuccessful modification attempts are logged.

If the application does not generate an audit record when successful and unsuccessful attempts to modify categories of information occur, this is a finding.

**Check ID:**  C-24127r493279_chk

### Fix Text 

Configure the application to create an audit record for both successful and unsuccessful attempts to modify protected categories of information.

**Fix ID:**  F-24116r493280_fix

**Vulnerability ID:**  V-222457

**Rule ID:**  SV-222457r961809_rule

---

## The application must generate audit records when successful/unsuccessful attempts to delete privileges occur.

<span style="color:#ff8c00;font-size:150%;">Medium Severity</span>

### Description

Without generating audit records that are specific to the security and mission needs of the organization, it would be difficult to establish, correlate, and investigate the events relating to an incident, or identify those responsible for one.

Audit records can be generated from various components within the information system (e.g., module or policy filter).

### Check Text

Review the application documentation and interview the application admin to identify application management interfaces and features.

Access the application management utility and create a test user account or use the account of a regular privileged user who is cooperating with the testing.

Access and open the auditing logs.

Using an admin account, delete some or all of the privileges of a privileged user.

Attempt to delete privileges in a manner that will cause a failure event such as attempting to delete a user’s privileges with an account that doesn't have the rights to do so.

Review the application logs and ensure both events were captured in the logs. The event data should include the user’s identity and the privilege that was granted and the privilege that failed to be granted.

If the application does not log when successful and unsuccessful attempts to delete privileges occur, this is a finding.

**Check ID:**  C-24128r493282_chk

### Fix Text 

Configure the application to audit successful and unsuccessful attempts to delete privileges.

**Fix ID:**  F-24117r493283_fix

**Vulnerability ID:**  V-222458

**Rule ID:**  SV-222458r961812_rule

---

## The application must generate audit records when successful/unsuccessful attempts to delete security levels occur.

<span style="color:#ff8c00;font-size:150%;">Medium Severity</span>

### Description

A security level denotes a permissions or authorization capability within the application. This is most often associated with a user role. Attempts to delete a security level can be construed as an attempt to change the configuration of the application so as to delete an existing security role. Some applications may or may not provide this capability.

Without generating audit records that are specific to the security and mission needs of the organization, it would be difficult to establish, correlate, and investigate the events relating to an incident, or identify those responsible for one.

Audit records can be generated from various components within the information system (e.g., module or policy filter).

### Check Text

Review the application documentation and interview the application administrator.

Identify where the application logs are stored.

Identify application functionality that provides privilege escalation or access to additional security levels within the application.

This can be performing a function that escalates the privileges of the user, or accessing a protected area of the application that requires additional authentication in order to access.

Authenticate to the application as a regular user. Using application functionality, attempt to delete permissions of a different security level or domain within the application.

Perform two attempts, one successfully and one unsuccessfully.

Review the log data and ensure the deletion events, both successful and unsuccessful are logged.

If the application does not generate an audit record when successful and unsuccessful attempts to delete permissions regarding the security levels occur, this is a finding.

**Check ID:**  C-24129r493285_chk

### Fix Text 

Configure the application to create an audit record for both successful and unsuccessful attempts to delete security levels.

**Fix ID:**  F-24118r493286_fix

**Vulnerability ID:**  V-222459

**Rule ID:**  SV-222459r961815_rule

---

## The application must generate audit records when successful/unsuccessful attempts to delete application database security objects occur.

<span style="color:#ff8c00;font-size:150%;">Medium Severity</span>

### Description

Without generating audit records that are specific to the security and mission needs of the organization, it would be difficult to establish, correlate, and investigate the events relating to an incident, or identify those responsible for one.

Audit records can be generated from various components within the information system (e.g., module or policy filter).

### Check Text

Review the application documentation and interview the application administrator.

Identify where the application logs are stored.

Identify application functionality that provides privilege or permission settings to database security objects within the application. This can be an application function that assigns privileges to an application object or data element.

Authenticate to the application as a regular user. Using application functionality, attempt to delete the database security object within the application.

Perform two attempts, one successfully and one unsuccessfully.

Review the log data and ensure the deletion events, both successful and unsuccessful, are logged.

If the application does not generate an audit record when successful and unsuccessful attempts to delete database security objects occur, this is a finding.

**Check ID:**  C-24130r493288_chk

### Fix Text 

Configure the application to create an audit record for both successful and unsuccessful attempts to delete database security objects.

**Fix ID:**  F-24119r493289_fix

**Vulnerability ID:**  V-222460

**Rule ID:**  SV-222460r961818_rule

---

## The application must generate audit records when successful/unsuccessful attempts to delete categories of information (e.g., classification levels) occur.

<span style="color:#ff8c00;font-size:150%;">Medium Severity</span>

### Description

Without generating audit records that are specific to the security and mission needs of the organization, it would be difficult to establish, correlate, and investigate the events relating to an incident, or identify those responsible for one.

Audit records can be generated from various components within the information system (e.g., module or policy filter).

### Check Text

Review the application documentation and interview the application administrator.

Identify where the application logs are stored.

Identify any data protections that are required.

Identify any categories of data or classification of data.

If the application requirements do not call for compartmentalized data and data protection, this requirement is not applicable.

Authenticate to the application as a regular user. Using application functionality, attempt to delete data that has been assigned to a protected category.

Perform two modification attempts, one successful and one unsuccessful.

Testing this will require obtaining access to test data that has been assigned to a protected category, or having an authorized user access the data for you.

Review the log data and ensure both the successful and unsuccessful deletion attempts are logged.

If the application does not generate an audit record when successful and unsuccessful attempts to delete categories of information occur, this is a finding.

**Check ID:**  C-24131r493291_chk

### Fix Text 

Configure the application to create an audit record for both successful and unsuccessful attempts to delete protected categories of information.

**Fix ID:**  F-24120r493292_fix

**Vulnerability ID:**  V-222461

**Rule ID:**  SV-222461r961821_rule

---

## The application must generate audit records when successful/unsuccessful logon attempts occur.

<span style="color:#ff8c00;font-size:150%;">Medium Severity</span>

### Description

Without generating audit records that are specific to the security and mission needs of the organization, it would be difficult to establish, correlate, and investigate the events relating to an incident, or identify those responsible for one.

Audit records can be generated from various components within the information system (e.g., module or policy filter).

Knowing when a user successfully or unsuccessfully logged on to the application is critical information that aids in forensic analysis.

### Check Text

Review and monitor the application logs.

Authenticate to the application and observe if the log includes an entry to indicate the user’s authentication was successful.

Terminate the user session by logging out.

Reauthenticate using invalid user credentials and observe if the log includes an entry to indicate the authentication was unsuccessful.

If successful and unsuccessful logon events are not recorded in the logs, this is a finding.

**Check ID:**  C-24132r493294_chk

### Fix Text 

Configure the application or application server to write a log entry when successful and unsuccessful logon events occur.

**Fix ID:**  F-24121r493295_fix

**Vulnerability ID:**  V-222462

**Rule ID:**  SV-222462r961824_rule

---

## The application must generate audit records for privileged activities or other system-level access.

<span style="color:#ff8c00;font-size:150%;">Medium Severity</span>

### Description

Privileged activities include the tasks or actions taken by users in an administrative role (admin, backup operator, manager, etc.) which are used to manage or reconfigure application function. Examples include but are not limited to:

Modifying application logging verbosity, starting or stopping of application services, application user account management, managing application functionality, or otherwise changing the underlying application capabilities such as adding a new application module or plugin.

Privileged access does not include an application design which does not modify the application but does provide users with the functionality or the ability to manage their own user specific preferences or otherwise tailor the application to suit individual user needs based upon choices or selections built into the application.

### Check Text

Review and monitor the application logs.

Authenticate to the application as a privileged user and observe if the log includes an entry to indicate the user’s authentication was successful.

Perform actions as an admin or other privileged user such as modifying the logging verbosity, or starting or stopping an application service, or terminating a test user session.

If log events that correspond with the actions performed are not recorded in the logs, this is a finding.

**Check ID:**  C-24133r493297_chk

### Fix Text 

Configure the application to write a log entry when privileged activities or other system-level events occur.

**Fix ID:**  F-24122r493298_fix

**Vulnerability ID:**  V-222463

**Rule ID:**  SV-222463r961827_rule

---

## The application must generate audit records showing starting and ending time for user access to the system.

<span style="color:#ff8c00;font-size:150%;">Medium Severity</span>

### Description

Knowing when a user’s application session began and when it ended is critical information that aids in forensic analysis.

### Check Text

Review and monitor the application logs.

Initiate a user session and observe if the log includes a time stamp showing the start of the session.

Terminate the user session and observe if the log includes a time stamp showing the end of the session.

If the start and the end time of the session are not recorded in the logs, this is a finding.

**Check ID:**  C-24134r493300_chk

### Fix Text 

Configure the application or application server to record the start and end time of user session activity.

**Fix ID:**  F-24123r493301_fix

**Vulnerability ID:**  V-222464

**Rule ID:**  SV-222464r961830_rule

---

## The application must generate audit records when successful/unsuccessful accesses to objects occur.

<span style="color:#ff8c00;font-size:150%;">Medium Severity</span>

### Description

Without generating audit records that are specific to the security and mission needs of the organization, it would be difficult to establish, correlate, and investigate the events relating to an incident, or identify those responsible for one.

Application objects are system or application components that comprise the application. This includes but is not limited to; application files, folders, processes and modules.

This requirement is not intended to force the use of debug logging which would be used for troubleshooting or forensic actions; rather it is intended to assure the application strikes a balance when auditing access to application objects and logs normal and potentially abnormal application activity.

Audit records can be generated from various components within the information system (e.g., module or policy filter).

### Check Text

Review the application documentation and interview the application administrator to identify log locations.

Access the application logs.

Review the logs and identify if the application is logging both successful and unsuccessful access to application objects such as files, folders, processes, or application modules and sub components, or systems.

If the application does not log application object access, this is a finding.

**Check ID:**  C-24135r493303_chk

### Fix Text 

Configure the application to log successful and unsuccessful access to application objects.

**Fix ID:**  F-24124r493304_fix

**Vulnerability ID:**  V-222465

**Rule ID:**  SV-222465r961836_rule

---

## The application must generate audit records for all direct access to the information system.

<span style="color:#ff8c00;font-size:150%;">Medium Severity</span>

### Description

Without generating audit records that are specific to the security and mission needs of the organization, it would be difficult to establish, correlate, and investigate the events relating to an incident, or identify those responsible for one.

When an application provides direct access to underlying OS features and functions, that access must be audited.
Audit records can be generated from various components within the information system (e.g., module or policy filter).

### Check Text

Review the application documentation and interview the application administrator.

Identify if the application implements a direct access feature or function that allows users to directly access the underlying OS.

Direct access includes but is not limited to: executing OS commands, navigating the file system, manipulating system resources such as print queues, or reading files hosted on the OS that are not specifically shared or made available on the website.

If the application does not provide direct access to the system, this requirement is not applicable.

Access the application logs.

Access the application as a user or test user with appropriate permissions and attempt to execute application features and functions that provide direct access to the system.

Review the logs and ensure the actions executed were logged.

Log information must include the user responsible for executing the action, the action executed, and the result of the action.

If the application does not log all direct access to the system, this is a finding.

**Check ID:**  C-24136r493306_chk

### Fix Text 

Configure the application to log all direct access to the system.

**Fix ID:**  F-24125r493307_fix

**Vulnerability ID:**  V-222466

**Rule ID:**  SV-222466r961839_rule

---

## The application must generate audit records for all account creations, modifications, disabling, and termination events.

<span style="color:#ff8c00;font-size:150%;">Medium Severity</span>

### Description

When application user accounts are created, modified, disabled or terminated the event must be logged.

Centralized management of user accounts allows for rapid response to user related security events and also provides ease of management.

Allowing the centralized user management solution to log these events is acceptable practice; however, if the application provides a user management interface to manage these tasks, the application must also log these events.

Application developers are encouraged to integrate their applications with enterprise-level authentication/access/audit mechanisms such as Syslog, Active Directory or LDAP.

### Check Text

Examine the application documentation or interview the application representative to identify how the application users are managed.

Interview the application administrator and determine if the application is configured to utilize a centralized user management system such as Active Directory for user management or if the application manages user accounts within the application.

If the application is configured to use an enterprise-based application user management capability that is STIG compliant, the requirement is not applicable.

Identify the location of the audit logs and review the end of the logs.

Access the user account management functionality.

Create an application test account and then review the log to ensure a log record that documents the event is created.

Modify the test account and then review the log to ensure a log record that documents the event is created.

Disable the test account and then review the log to ensure a log record that documents the event is created.

Terminate/remove the test account and then review the log to ensure a log record that documents the event is created.

If log events are not created that document all of these events, this is a finding.

If some but not all of the aforementioned events are documented in the logs, this is a finding.

Findings should document which of the events was not logged.

**Check ID:**  C-24137r918116_chk

### Fix Text 

Configure the application to log user account creation, modification, disabling, and termination events.

**Fix ID:**  F-24126r493310_fix

**Vulnerability ID:**  V-222467

**Rule ID:**  SV-222467r961842_rule

---

## The application must initiate session auditing upon startup.

<span style="color:#ff8c00;font-size:150%;">Medium Severity</span>

### Description

If the application does not begin logging upon startup, important log events could be missed.

### Check Text

Examine the application design documentation and interview the application administrator to identify application logging behavior.

If the application is writing to an existing log or log file:

Open and monitor the application log.

Start the application service and view the log entries. 

Log entries indicating the application is starting should commence as soon as the application starts. Determine if the log events correlate with the time the application was started and if event log entries include an application start up sequence of events.

If the application writes events to a new log on startup: 

Identify location logs are written to, start the application and then identify and access the new log.

Determine if the log events correlate with the time the application was started and if event log entries include an application start up sequence of events.

If the application does not begin logging events upon start up, this is a finding.

**Check ID:**  C-24138r493312_chk

### Fix Text 

Configure the application to begin logging application events as soon as the application starts up.

**Fix ID:**  F-24127r493313_fix

**Vulnerability ID:**  V-222468

**Rule ID:**  SV-222468r960888_rule

---

## The application must log application shutdown events.

<span style="color:#ff8c00;font-size:150%;">Medium Severity</span>

### Description

Forensics is a large part of security incident response.  Applications must provide a record of their actions so application events can be investigated post-event.  

Attackers may attempt to shut off the application logging capability to cover their activity while on the system.  Recording the shutdown event and the time it occurred in the application or  system logs helps to provide forensic evidence that aids in investigating the events.

### Check Text

Review and monitor the application and system logs.

If an application shutdown event is not recorded in the logs, either initiate a shutdown event and review the logs after reestablishing access or request backup copies of the application or system logs that indicate shutdown events are being recorded.

Alternatively, check for a setting within the application that controls application logging events and determine if application shutdown logging is configured.

If the application is not recording application shutdown events in either the application or system log, or if the application is not configured to record shutdown events, this is a finding.

**Check ID:**  C-36238r602280_chk

### Fix Text 

Configure the application or application server to record application shutdown events in the event logs.

**Fix ID:**  F-24128r493316_fix

**Vulnerability ID:**  V-222469

**Rule ID:**  SV-222469r960891_rule

---

## The application must log destination IP addresses.

<span style="color:#ff8c00;font-size:150%;">Medium Severity</span>

### Description

The IP addresses of the systems that the application connects to are an important aspect of identifying application network related activity. Recording the IP addresses of the system the application connects to in the application logs provides forensic evidence and aids in investigating and correlating the sources of malicious behavior related to security events. Logging this information can be particularly useful for Service-Oriented Applications where there is application to application connectivity.

### Check Text

If the application design documentation indicates the application does not initiate connections to remote systems this requirement is not applicable.

Network connections to systems used for support services such as DNS, AD, or LDAP may be stored in the system logs. These connections are applicable.

Identify log source based upon application architecture, design documents and input from application admin.

Review and monitor the application or system logs.

Connect to the application and utilize the application functionality that initiates connections to a destination system.

If the application routinely connects to remote system on a regular basis you may simply allow the application to operate in the background while the logs are observed.

Observe the log activity and determine if the log includes an entry to indicate the IP address of the destination system.

If the IP address of the remote system is not recorded along with the event in the event log, this is a finding.

**Check ID:**  C-24140r493318_chk

### Fix Text 

Configure the application to record the destination IP address of the remote system.

**Fix ID:**  F-24129r493319_fix

**Vulnerability ID:**  V-222470

**Rule ID:**  SV-222470r960891_rule

---

## The application must log user actions involving access to data.

<span style="color:#ff8c00;font-size:150%;">Medium Severity</span>

### Description

When users access application data, there is risk of data compromise or seepage if the account used to access is compromised or access is granted improperly. To be able to investigate which account accessed data, the account access must be logged. Without establishing when the access event occurred, it would be difficult to establish, correlate, and investigate the events relating to an incident, or identify those responsible for one.

Associating event types with detected events in the application and audit logs provides a means of investigating an attack; recognizing resource utilization or capacity thresholds; or identifying an improperly configured application.

### Check Text

Review and monitor the application logs. When accessing data, the logs are most likely database logs.

If the application design documents include specific data elements that require protection, ensure user access to those data elements are logged.

Utilize the application as a regular user and operate the application so as to access data elements contained within the application. This includes using the application user interface to browse through data elements, query/search data elements and using report generation capability if it exists.

Observe and determine if the application log includes an entry to indicate the user’s access to the data was recorded.

If successful access to application data elements is not recorded in the logs, this is a finding.

**Check ID:**  C-24141r493321_chk

### Fix Text 

Identify the specific data elements requiring protection and audit access to the data.

**Fix ID:**  F-24130r493322_fix

**Vulnerability ID:**  V-222471

**Rule ID:**  SV-222471r960891_rule

---

## The application must log user actions involving changes to data.

<span style="color:#ff8c00;font-size:150%;">Medium Severity</span>

### Description

When users change/modify application data, there is risk of data compromise if the account used to access is compromised or access is granted improperly. To be able to investigate which account accessed data, the account making the data changes must be logged. Without establishing when the data change event occurred, it would be difficult to establish, correlate, and investigate the events relating to an incident, or identify those responsible for one.

Associating event types with detected events in the application and audit logs provides a means of investigating an attack; recognizing resource utilization or capacity thresholds; or identifying an improperly configured application.

### Check Text

Review and monitor the application logs. When modifying data, the logs are most likely database logs.

If the application design documents include specific data elements that require protection, ensure any changes to those specific data elements are logged. Otherwise, a random check is sufficient.

If the application uses a database configured to use Transaction SQL logging this is not a finding if the application admin can demonstrate a process for reviewing the transaction log for data changes. The process must include using the transaction log and some form of query capability to identify users and the data they changed within the application and vice versa.

Utilize the application as a regular user and operate the application so as to modify a data element contained within the application.

Observe and determine if the application log includes an entry to indicate the users data change event was recorded.

If successful changes/modifications to application data elements are not recorded in the logs, this is a finding.

**Check ID:**  C-24142r493324_chk

### Fix Text 

Configure the application to log all changes to application data.

**Fix ID:**  F-24131r493325_fix

**Vulnerability ID:**  V-222472

**Rule ID:**  SV-222472r960891_rule

---

## The application must produce audit records containing information to establish when (date and time) the events occurred.

<span style="color:#ff8c00;font-size:150%;">Medium Severity</span>

### Description

Without establishing when events occurred, it is impossible to establish, correlate, and investigate the events relating to an incident.

In order to compile an accurate risk assessment, and provide forensic analysis, it is essential for security personnel to know when events occurred (date and time).

### Check Text

Access the application logs and review the log entries for date and time. Each event written into the log must have a corresponding date and time stamp associated with it.

If the audit logs do not have a corresponding date and time associated with each event, this is a finding.

**Check ID:**  C-24143r493327_chk

### Fix Text 

Configure the application or application server to include the date and the time of the event in the audit logs.

**Fix ID:**  F-24132r493328_fix

**Vulnerability ID:**  V-222473

**Rule ID:**  SV-222473r960894_rule

---

## The application must produce audit records containing enough information to establish which component, feature or function of the application triggered the audit event.

<span style="color:#ff8c00;font-size:150%;">Medium Severity</span>

### Description

It is impossible to establish, correlate, and investigate the events relating to an incident if the details regarding the source of the event it not available.

In order to compile an accurate risk assessment, and provide forensic analysis, it is essential for security personnel to know where within the application the events occurred, such as which application component, application modules, filenames, and functionality.

Associating information about where the event occurred within the application provides a means of quickly investigating an attack; recognizing resource utilization or capacity thresholds; or identifying an improperly configured application.

### Check Text

Review application administration and/or design documents.

Identify key aspects of application architecture objects and components, e.g., Web Server, Application server, Database server.

Interview the application administrator and identify the log locations.

Access the application logs and review the log entries for events that indicate the application is auditing the internal components, objects, or functions of the application.

Confirm the event logs provide information as to which component, feature, or functionality of the application triggered the event.

Examples of the types of events to look for are as follows:

- Application and Protocol events. e.g., Application loads or unloads and Protocol use.
- Data Access events. e.g., Database connections.

Events could include reference to database library or executable initiating connectivity:

- Middleware events. e.g., Source code initiating calls or being invoked.
- Name of application modules being loaded or unloaded.
- Library loads and unloads.
- Application deployment activity.

Events written into the log must be able to be traced back to the originating component, feature or function name, service name, application name, library name etcetera in order to establish which aspect of the application triggered the event.

If the audit logs do not contain enough data in the logs to establish which component, feature or functionality of the application triggered the event, this is a finding.

**Check ID:**  C-24144r493330_chk

### Fix Text 

Configure the application to log which component, feature or functionality of the application triggered the event.

**Fix ID:**  F-24133r493331_fix

**Vulnerability ID:**  V-222474

**Rule ID:**  SV-222474r960897_rule

---

## When using centralized logging; the application must include a unique identifier in order to distinguish itself from other application logs.

<span style="color:#ff8c00;font-size:150%;">Medium Severity</span>

### Description

Without establishing the source, it is impossible to establish, correlate, and investigate the events leading up to an outage or attack.

In the case of centralized logging, or other instances where log files are consolidated, there is risk that the application's log data could be co-mingled with other log data.  To address this issue, the application itself must be identified as well as the application host or client name. 

In order to compile an accurate risk assessment, and provide forensic analysis, it is essential for security personnel to know the source of the event, particularly in the case of centralized logging.

Associating information about the source of the event within the application provides a means of investigating an attack; recognizing resource utilization or capacity thresholds; or identifying an improperly configured application.

### Check Text

If the application is logging locally and does not utilize a centralized logging solution, this requirement is not applicable.

Review system documentation and identify log location.  Access the application logs.

Review the application logs.

Ensure the application is uniquely identified either within the logs themselves or via log storage mechanisms.

Ensure the hosts or client names hosting the application are also identified.  Either hostname or IP address is acceptable.

If the application name and the hosts or client names are not identified, this is a finding.

**Check ID:**  C-24145r493333_chk

### Fix Text 

Configure the application logs or the centralized log storage facility so the application name and the hosts hosting the application are uniquely identified in the logs.

**Fix ID:**  F-24134r493334_fix

**Vulnerability ID:**  V-222475

**Rule ID:**  SV-222475r960900_rule

---

## The application must produce audit records that contain information to establish the outcome of the events.

<span style="color:#ff8c00;font-size:150%;">Medium Severity</span>

### Description

Without information about the outcome of events, security personnel cannot make an accurate assessment as to whether an attack was successful or if changes were made to the security state of the system.

Event outcomes can include indicators of event success or failure and event-specific results (e.g., the security state of the information system after the event occurred). As such, they also provide a means to measure the impact of an event and help authorized personnel to determine the appropriate response.

Successful application events are expected to far outnumber errors.   Therefore, success events may be implied by default and not specified in the logs if this behavior is documented.

### Check Text

Review system and application documentation to identify application operation and function.

Access the application logs and review the logs to determine if the results of application operations are logged.

Successful application events are expected to far outnumber errors.   Therefore, success events may be implied by default and not specified in the logs if this behavior is documented.

The outcome will be a log record that displays the application event/operation that occurred followed by the result of the operation such as "ERROR", "FAILURE", "SUCCESS" or "PASS".

Operation outcomes may also be indicated by numeric code where a "1" might indicate success and a "0" may indicate operation failure.

If the application does not produce audit records that contain information regarding the results of application operations, this is a finding.

**Check ID:**  C-24146r493336_chk

### Fix Text 

Configure the application to include the outcome of application functions or events.

**Fix ID:**  F-24135r493337_fix

**Vulnerability ID:**  V-222476

**Rule ID:**  SV-222476r960903_rule

---

## The application must generate audit records containing information that establishes the identity of any individual or process associated with the event.

<span style="color:#ff8c00;font-size:150%;">Medium Severity</span>

### Description

Without information that establishes the identity of the subjects (i.e., users or processes acting on behalf of users) associated with the events, security personnel cannot determine responsibility for the potentially harmful event.

Event identifiers (if authenticated or otherwise known) include, but are not limited to, user database tables, primary key values, user names, or process identifiers.

### Check Text

Review system documentation and discuss application operation with application administrator.

Identify application processes and application users.
Identify application components, e.g., application features framework and function. Identify server components, such as web server, database server.

Review application logs. Ensure the application event logs include an identifier or identifiers that will allow an investigator to determine the user or the application process responsible for the application event.

If the event logs do not include the appropriate identifier or identifiers, this is a finding.

**Check ID:**  C-24147r493339_chk

### Fix Text 

Configure the application to log the identity of the user and/or the process associated with the event.

**Fix ID:**  F-24136r493340_fix

**Vulnerability ID:**  V-222477

**Rule ID:**  SV-222477r960906_rule

---

## The application must generate audit records containing the full-text recording of privileged commands or the individual identities of group account users.

<span style="color:#ff8c00;font-size:150%;">Medium Severity</span>

### Description

Reconstruction of harmful events or forensic analysis is not possible if audit records do not contain enough information.

Organizations consider limiting the additional audit information to only that information explicitly needed for specific audit requirements. The additional information required is dependent on the type of information (i.e., sensitivity of the data and the environment within which it resides). At a minimum, the organization must audit either full-text recording of privileged commands or the individual identities of group users, or both. The organization must maintain audit trails in sufficient detail to reconstruct events to determine the cause and impact of compromise. 

In addition, the application must have the capability to include organization-defined additional, more detailed information in the audit records for audit events.

### Check Text

Review application documentation and interview application administrator. Identify audit log locations and review audit logs.

Access the system as a privileged user and execute privileged commands.

Review the application logs and ensure that the logs contain all details of the actions performed.  

If a privileged command was typed within the application that command text must be included in the logs. Authentication information provided as part of the text must NOT be logged, just the commands.

If an action was performed, such as activating a check box, that action must be logged.

Review group account users, review logs to determine if the individual users of group accounts are identified in the logs.

If the application does not log the full text recording of privileged commands or if the application does not identify and log the individuals associated with group accounts, this is a finding.

**Check ID:**  C-24148r493342_chk

### Fix Text 

Configure the application to log the full text recording of privileged commands or the individual identities of group users.

**Fix ID:**  F-24137r493343_fix

**Vulnerability ID:**  V-222478

**Rule ID:**  SV-222478r960909_rule

---

## The application must implement transaction recovery logs when transaction based.

<span style="color:#ff8c00;font-size:150%;">Medium Severity</span>

### Description

Without required logging and access control, security issues related to data changes will not be identified. This could lead to security compromises such as data misuse, unauthorized changes, or unauthorized access.

Transaction logs contain a sequential record of all changes to the database. Using a transaction log helps with maintaining application availability and aids in speedy recovery. Transactional logging should be enabled whenever the application database offers the transactional logging capability.

### Check Text

Review the application documentation and interview the application administrator.  Have the application administrator provide configuration settings that demonstrate transaction logging is enabled.

Review configuration settings for the location of transaction specific logs and verify transaction logs exist and the log records access and changes to the data.

If the application is not configured to utilize transaction logging, this is a finding.

**Check ID:**  C-24149r493345_chk

### Fix Text 

Configure the application database to utilize transactional logging.

**Fix ID:**  F-24138r493346_fix

**Vulnerability ID:**  V-222479

**Rule ID:**  SV-222479r960909_rule

---

## The application must provide centralized management and configuration of the content to be captured in audit records generated by all application components.

<span style="color:#ff8c00;font-size:150%;">Medium Severity</span>

### Description

Without the ability to centrally manage the content captured in the audit records, identification, troubleshooting, and correlation of suspicious behavior would be difficult and could lead to a delayed or incomplete analysis of an ongoing attack.

This requirement requires that the content captured in audit records be managed from a central location (necessitating automation). Centralized management of audit records and logs provides for efficiency in maintenance and management of records, as well as the backup and archiving of those records. Application components requiring centralized audit log management must have the capability to support centralized management.

This requirement applies to centralized management applications or similar types of applications designed to manage and configure audit record capture.

### Check Text

Review the application documentation and interview the application administrator to determine the logging architecture of the application.

If the application is configured to log application event entries to a centralized, enterprise based logging solution that meets this requirement, this requirement is Not Applicable.

Review the application components and the log management capabilities of the application.

Verify the application log management interface includes the ability to centrally manage the configuration of what is captured in the logs of all application components. 

If the application does not provide the ability to centrally manage the content captured in the audit logs, this is a finding.

**Check ID:**  C-24150r985971_chk

### Fix Text 

Configure the application to utilize a centralized log management system that provides the capability to configure the content of audit records.

**Fix ID:**  F-24139r493349_fix

**Vulnerability ID:**  V-222480

**Rule ID:**  SV-222480r985972_rule

---

## The application must off-load audit records onto a different system or media than the system being audited.

<span style="color:#ff8c00;font-size:150%;">Medium Severity</span>

### Description

Information stored in one location is vulnerable to accidental or incidental deletion or alteration.  In addition, attackers often manipulate logs to hide or obfuscate their activity.

The goal is to off-load application logs to a separate server as quickly and efficiently as possible so as to mitigate these risks.  

A centralized logging solution offering applications an enterprise designed and managed logging capability which is the desired solution.

However, when a centralized logging solution is not an option due to the operational environment or other situations where the risk has been officially recognized and accepted, off-loading is a common process utilized to address this type of scenario.

### Check Text

Review application documentation and interview application administrator.  Identify log functionality and locations of log files.  Obtain risk acceptance documentation and task scheduling information.

If the application is configured to utilize a centralized logging solution, this requirement is not applicable.

Evaluate log management processes and determine if there are automated tasks that move the logs off of the system hosting the application.   

Verify automated tasks are performed on an ISSO approved schedule (hourly, daily etc.).  Automation can be via scripting, log management oriented tools or other automated means.

Review risk acceptance documentation for not utilizing a centralized logging solution.

If the logs are not automatically moved off the system as per approved schedule, or if there is no formal risk acceptance documentation, this is a finding.

**Check ID:**  C-24151r493351_chk

### Fix Text 

Configure the application to off-load audit records onto a different system as per approved schedule.

**Fix ID:**  F-24140r493352_fix

**Vulnerability ID:**  V-222481

**Rule ID:**  SV-222481r961395_rule

---

## The application must be configured to write application logs to a centralized log repository.

<span style="color:#ff8c00;font-size:150%;">Medium Severity</span>

### Description

Information stored in one location is vulnerable to accidental or incidental deletion or alteration.  In addition, attackers often manipulate logs to hide or obfuscate their activity.

Off-loading is a common process in information systems with limited audit storage capacity or when trying to assure log availability and integrity.

This requirement is meant to address space limitations and integrity issues that can be encountered when storing logs on the local server.

The goal of the requirement being to offload application logs to a separate server as quickly and efficiently as possible so as to mitigate these risks.

### Check Text

Review application documentation and interview application administrator.

Evaluate application log management processes and determine if the system is configured to utilize a centralized log management system for the hosting and management of application audit logs.

If the system is not configured to write the application logs to the centralized log management repository in an expeditious manner, this is a finding.

**Check ID:**  C-24152r493354_chk

### Fix Text 

Configure the application to utilize a centralized log repository and ensure the logs are off-loaded from the application system as quickly as possible.

**Fix ID:**  F-24141r493355_fix

**Vulnerability ID:**  V-222482

**Rule ID:**  SV-222482r961860_rule

---

## The application must provide an immediate warning to the SA and ISSO (at a minimum) when allocated audit record storage volume reaches 75% of repository maximum audit record storage capacity.

<span style="color:#ff8c00;font-size:150%;">Medium Severity</span>

### Description

If security personnel are not notified immediately upon storage volume utilization reaching 75%, they are unable to plan for storage capacity expansion.

Due to variances in application usage and audit records storage usage, the SA and the ISSO may evaluate usage patterns and determine if a higher percentage of usage is warranted before an alarm is sent.  The intent of the requirement is to provide a warning that will allow the SA and ISSO ample time to plan and implement an audit storage capacity expansion that will provide for the increased audit log storage requirements without forcing an emergency or otherwise negatively impacting the recording of audit events.

The requirement will take into account a reasonable amount of processing time such as 1 or 2 minutes that may be required of the system in order to satisfy the requirement.

### Check Text

Review system documentation and interview application administrator for details regarding logging configuration. 

If the application utilizes a centralized logging system that provides storage capacity alarming, this requirement is not applicable.

Identify application alarming capability relating to storage capacity alarming for the log repository. Coordinate with the appropriate personnel regarding the generation of test alarms.

Review log alarm settings and ensure audit log storage capacity alarming is enabled and set to alarm when the storage threshold exceeds 75% of disk storage capacity or the capacity value the SA and ISSO have determined will provide adequate time to plan for capacity expansion.

Ensure the alarm will be sent to the ISSO and the application administrator when the utilization threshold is exceeded by changing the threshold settings to below the current disk space utilization. An alarm should be triggered at that point and forwarded to the ISSO and the SA/application admin.

If the application is not configured to send an alarm when storage volume exceeds 75% of disc capacity or if the designated alarm recipients did not receive an alarm when the test was conducted, this is a finding.

**Check ID:**  C-36239r602282_chk

### Fix Text 

Configure the application to send an immediate alarm to the application admin/SA and the ISSO when the allocated log storage capacity exceeds 75% of usage or exceeds the capacity value the SA and ISSO have determined will provide adequate time to plan for capacity expansion.

**Fix ID:**  F-36205r865216_fix

**Vulnerability ID:**  V-222483

**Rule ID:**  SV-222483r961398_rule

---

## Applications categorized as having a moderate or high impact must provide an immediate real-time alert to the SA and ISSO (at a minimum) for all audit failure events.

<span style="color:#ff8c00;font-size:150%;">Medium Severity</span>

### Description

Applications that are categorized as having a high or moderate impact on the organization must provide immediate alerts when encountering failures with the application audit system.  It is critical for the appropriate personnel to be aware if a system is at risk of failing to process audit logs as required. Without this notification, the security personnel may be unaware of an impending failure of the audit capability and system operation may be adversely affected. 

Audit processing failures include software/hardware errors, failures in the audit capturing mechanisms, and audit storage capacity being reached or exceeded.

While alerts provide organizations with urgent messages containing important information regarding application audit log activity, real-time alerts provide these messages at information technology speed (i.e., the time from event detection to alert occurs in seconds or no more than 1-2 minutes).  

Without a real-time alert, security personnel may be unaware of an impending failure of the audit capability and system operation may be adversely affected.

### Check Text

Review system documentation and interview application administrator for details regarding application security categorization and logging configuration.

If the application utilizes a centralized logging system that provides the real-time alarms, this requirement is not applicable.

Review application log alert configuration.

Identify audit failure events and associated alarming configuration.

If the application is categorized as having a moderate or high impact and is not configured to provide a real-time alert that indicates the audit system has failed or is failing, this is a finding.

**Check ID:**  C-24154r493360_chk

### Fix Text 

Configure the log alerts to send an alarm when the audit system is in danger of failing or has failed.  

Configure the log alerts to be immediately sent to the application admin/SA and ISSO.

**Fix ID:**  F-24143r493361_fix

**Vulnerability ID:**  V-222484

**Rule ID:**  SV-222484r961401_rule

---

## The application must alert the ISSO and SA (at a minimum) in the event of an audit processing failure.

<span style="color:#ff8c00;font-size:150%;">Medium Severity</span>

### Description

It is critical for the appropriate personnel to be aware if a system is at risk of failing to process audit logs as required. Without this notification, the security personnel may be unaware of an impending failure of the audit capability and system operation may be adversely affected. 

Audit processing failures include software/hardware errors, failures in the audit capturing mechanisms, and audit storage capacity being reached or exceeded.

This requirement applies to each audit data storage repository (i.e., distinct information system component where audit records are stored), the centralized audit storage capacity of organizations (i.e., all audit data storage repositories combined), or both.

### Check Text

Review system documentation and interview application administrator for details regarding logging configuration.

If the application utilizes a centralized logging system that provides the audit processing failure alarms, this requirement is not applicable.

Identify application alarming capability regarding audit processing failure events.

Verify the application is configured to alarm when the auditing system fails.

Example alarm events include but are not limited to: 

hardware failure events
failures to capture audit record events
audit storage errors

If the application is not configured to alarm on alerts that indicate the audit system has failed or is failing, this is a finding.

**Check ID:**  C-24155r493363_chk

### Fix Text 

Configure the application to send an alarm in the event the audit system has failed or is failing.

**Fix ID:**  F-24144r493364_fix

**Vulnerability ID:**  V-222485

**Rule ID:**  SV-222485r960912_rule

---

## The application must shut down by default upon audit failure (unless availability is an overriding concern).

<span style="color:#ff8c00;font-size:150%;">Medium Severity</span>

### Description

It is critical that when the application is at risk of failing to process audit logs as required, it take action to mitigate the failure. Audit processing failures include: software/hardware errors; failures in the audit capturing mechanisms; and audit storage capacity being reached or exceeded. Responses to audit failure depend upon the nature of the failure mode.

When availability is an overriding concern, other approved actions in response to an audit failure are as follows: 

(i) If the failure was caused by the lack of audit record storage capacity, the application must continue generating audit records if possible (automatically restarting the audit service if necessary), overwriting the oldest audit records in a first-in-first-out manner.

(ii) If audit records are sent to a centralized collection server and communication with this server is lost or the server fails, the application must queue audit records locally until communication is restored or until the audit records are retrieved manually. Upon restoration of the connection to the centralized collection server, action should be taken to synchronize the local audit data with the collection server.

### Check Text

Review system documentation and interview application administrator for details regarding logging configuration.

Identify application shut down capability regarding audit processing failure events.  Locate and verify application logging settings that specify the application will halt processing on detected audit failure.

If ISSO approval to continue operating and not shut down the application upon an audit failure exists and is documented, validate the application is configured as follows:

If logging locally and the failure is attributed to a lack of disk space:

Ensure the application is configured to overwrite the oldest logs first so as to maintain the most up to date audit events in the event of an audit failure.

When logging centrally:

Ensure the application is configured to locally spool/queue audit events in the event an audit failure is detected with the centralized system.

If the application does not shut down processing when an audit failure is detected, or if the application does not take steps needed to ensure audit events are not lost due to audit failure, this is a finding.

**Check ID:**  C-24156r493366_chk

### Fix Text 

Configure the application to cease processing if the audit system fails or configure the application to continue logging in a manner that compensates for the audit failure.

**Fix ID:**  F-24145r493367_fix

**Vulnerability ID:**  V-222486

**Rule ID:**  SV-222486r1043188_rule

---

## The application must provide the capability to centrally review and analyze audit records from multiple components within the system.

<span style="color:#ff8c00;font-size:150%;">Medium Severity</span>

### Description

Successful incident response and auditing relies on timely, accurate system information and analysis in order to allow the organization to identify and respond to potential incidents in a proficient manner. If the application does not provide the ability to centrally review the application logs, forensic analysis is negatively impacted.

Segregation of logging data to multiple disparate computer systems is counterproductive and makes log analysis and log event alarming difficult to implement and manage, particularly when the system or application has multiple logging components written to different locations or systems.

Automated mechanisms for centralized reviews and analyses include, for example, Security Information Management products.

### Check Text

Review system documentation and interview application administrator for details regarding application architecture and logging configuration.  Identify the application components, the logs that are associated with the components and the locations of the logs.

If the application utilizes a centralized logging system that provides the capability to review the log files from one central location, this requirement is not applicable.

Access the application's log management utility and review the log files.  Ensure all of the applications logs are reviewable from within the centralized log management function and access to other systems in order to review application logs are not required.

If all of the application logs are not reviewable from a central location, this is a finding.

**Check ID:**  C-24157r493369_chk

### Fix Text 

Configure the application so all of the applications logs are available for review from one centralized location.

**Fix ID:**  F-24146r493370_fix

**Vulnerability ID:**  V-222487

**Rule ID:**  SV-222487r960918_rule

---

## The application must provide the capability to filter audit records for events of interest based upon organization-defined criteria.

<span style="color:#ff8c00;font-size:150%;">Medium Severity</span>

### Description

The ability to specify the event criteria that are of interest provides the persons reviewing the logs with the ability to quickly isolate and identify these events without having to review entries that are of little or no consequence to the investigation. Without this capability, forensic investigations are impeded.

Events of interest can be identified by the content of specific audit record fields including, for example, identities of individuals, event types, event locations, event times, event dates, system resources involved, IP addresses involved, or information objects accessed. Organizations may define audit event criteria to any degree of granularity required, for example, locations selectable by general networking location (e.g., by network or subnetwork) or selectable by specific information system component. This requires applications to provide the capability to customize audit record reports based on organization-defined criteria.

### Check Text

Review the system documentation and interview the application administrator for details regarding application architecture and logging configuration.

Identify the application components and the logs associated with the components as well as the locations of the logs.

If the application utilizes a centralized logging system that provides the capability to filter log events based upon the following events, this requirement is not applicable.

Review the application log management utility.

Ensure the application provides the ability to filter on audit events based upon the following minimum criteria:

Users: e.g., specific users or groups
Event types:
Event dates and time:
System resources involved: e.g., application components or modules.
IP addresses:
Information objects accessed:
Event level categories: e.g., high, critical, warning, error
Key words: e.g., a specific search string

Additional details may be logged as needed or prescribed by operational requirements.

If the application does not provide the ability to filter audit events, this is a finding.

**Check ID:**  C-24158r493372_chk

### Fix Text 

Configure the application filters to search event logs based on defined criteria.

**Fix ID:**  F-24147r493373_fix

**Vulnerability ID:**  V-222488

**Rule ID:**  SV-222488r960924_rule

---

## The application must provide an audit reduction capability that supports on-demand reporting requirements.

<span style="color:#ff8c00;font-size:150%;">Medium Severity</span>

### Description

The ability to generate on-demand reports, including after the audit data has been subjected to audit reduction, greatly facilitates the organization's ability to generate incident reports as needed to better handle larger-scale or more complex security incidents.

Audit reduction is a process that manipulates collected audit information and organizes such information in a summary format that is more meaningful to analysts. The report generation capability provided by the application must support on-demand (i.e., customizable, ad-hoc, and as-needed) reports.

This requirement is specific to applications with audit reduction capabilities; however, applications need to support on-demand audit review and analysis.

### Check Text

Review the system documentation and interview the application administrator for details regarding application architecture and logging configuration.

Identify the application components and the logs associated with the components.

If the application utilizes a centralized logging system that provides the capability to generate reports based on filtered log events, this requirement is not applicable.

Using the relevant application features for generating reports and/or searching application data, (this is usually executed directly within a logging utility or within a reports feature or function) configure a filter based on any of the security criteria provided below.

Alternatively, you can use security-oriented criteria provided by the application administrator.

Once the data filter has been selected, filter the audit event data so only filtered data is displayed and generate the report.

The report can be any combination of screen-based, soft copy, or a printed report.

Criteria:
Users: e.g., specific users or groups
Event types:
Event dates and time:
System resources involved: e.g., application components or modules.
IP addresses:
Information objects accessed:
Event level categories: e.g., high, critical, warning, error

If the application does not provide on demand reports based on the filtered audit event data, this is a finding.

**Check ID:**  C-24159r493375_chk

### Fix Text 

Configure the application to generate soft copy, hard copy and/or screen-based reports based on the selected filtered event data.

**Fix ID:**  F-24148r493376_fix

**Vulnerability ID:**  V-222489

**Rule ID:**  SV-222489r961056_rule

---

## The application must provide an audit reduction capability that supports on-demand audit review and analysis.

<span style="color:#ff8c00;font-size:150%;">Medium Severity</span>

### Description

The ability to perform on-demand audit review and analysis, including after the audit data has been subjected to audit reduction, greatly facilitates the organization's ability to generate incident reports as needed to better handle larger-scale or more complex security incidents.

Audit reduction is a technique used to reduce the volume of audit records in order to facilitate a manual review. Audit reduction does not alter original audit records. The report generation capability provided by the application must support on-demand (i.e., customizable, ad-hoc, and as-needed) reports.

This requirement is specific to applications with audit reduction capabilities; however, applications need to support on-demand audit review and analysis.

### Check Text

Review the system documentation and interview the application administrator for details regarding application architecture and logging configuration.

Identify the application components and the logs associated with the components.

If the application utilizes a centralized logging system that provides the capability to generate reports based on filtered log events, this requirement is not applicable.

Using the relevant application features for generating reports and/or searching application data, (this is usually executed directly within a logging utility or within a reports feature or function) configure a filter based on any of the security criteria provided below.

Alternatively, you can use security-oriented criteria provided by the application administrator.

Once the data filter has been selected, filter the audit event data so only filtered data is displayed and generate the report.

The report can be any combination of screen-based, soft copy, or a printed report.

Criteria:
Users: e.g., specific users or groups
Event types:
Event dates and time:
System resources involved: e.g., application components or modules.
IP addresses:
Information objects accessed:
Event level categories: e.g., high, critical, warning, error

If the application does not provide an audit reduction capability that supports on-demand reports based on the filtered audit event data, this is a finding.

**Check ID:**  C-24160r493378_chk

### Fix Text 

Configure the application to log to a centralized auditing capability that provides on-demand reports based on the filtered audit event data or design or configure the application to meet the requirement.

**Fix ID:**  F-24149r493379_fix

**Vulnerability ID:**  V-222490

**Rule ID:**  SV-222490r961413_rule

---

## The application must provide an audit reduction capability that supports after-the-fact investigations of security incidents.

<span style="color:#ff8c00;font-size:150%;">Medium Severity</span>

### Description

If the audit reduction capability does not support after-the-fact investigations, it is difficult to establish, correlate, and investigate the events leading up to an outage or attack, or identify those responses for one. This capability is also required to comply with applicable Federal laws and DoD policies.

Audit reduction capability must support after-the-fact investigations of security incidents either natively or through the use of third-party tools.

This requirement is specific to applications with audit reduction capabilities.

### Check Text

Review application documentation and interview application administrator for details regarding audit reduction (log record event filtering).

Access the application with user rights sufficient to read and filter audit records.

Navigate the application user interface and select the application functionality that provides access and interface to audit records and audit reduction (event filtering).

If the application uses a centralized logging solution that performs the audit reduction (event filtering) functions, the requirement is not applicable.

Examine the log files; take note of dates and times of events such as logon events.

Note: dates and times as well as the original content and any unique record identifiers.

Record the identifying information as well as the dates and times and content of the audit records.

Apply filters to reduce the amount of audit records displayed to just the logon events for the day.

Review the records and ensure the application provides the ability to filter on audit events.

If the application does not provide an audit reduction (event filtering) capability, this is a finding.

**Check ID:**  C-24161r493381_chk

### Fix Text 

Configure the application to provide an audit reduction capability that supports forensic investigations.

**Fix ID:**  F-24150r493382_fix

**Vulnerability ID:**  V-222491

**Rule ID:**  SV-222491r961416_rule

---

## The application must provide a report generation capability that supports on-demand audit review and analysis.

<span style="color:#ff8c00;font-size:150%;">Medium Severity</span>

### Description

The report generation capability must support on-demand review and analysis in order to facilitate the organization's ability to generate incident reports as needed to better handle larger-scale or more complex security incidents.

Report generation must be capable of generating on-demand (i.e., customizable, ad-hoc, and as-needed) reports. On-demand reporting allows personnel to report issues more rapidly to more effectively meet reporting requirements. Collecting log data and aggregating it to present the data in a single, consolidated report achieves this objective.

Audit reduction and report generation capabilities do not always reside on the same information system or within the same organizational entities conducting auditing activities. The audit reduction capability can include, for example, modern data mining techniques with advanced data filters to identify anomalous behavior in audit records. The report generation capability provided by the information system can generate customizable reports. Time ordering of audit records can be a significant issue if the granularity of the time stamp in the record is insufficient.

This requirement is specific to applications with report generation capabilities; however, applications need to support on-demand audit review and analysis.

### Check Text

Review the application documentation and interview the application administrator for details regarding audit reduction (log record event filtering).

Access the application with user rights sufficient to read and filter audit records.

Navigate the application user interface and select the application functionality that provides access and interface to audit records and audit reporting.

If the application uses a centralized logging solution that provides immediate, customizable audit review and analysis functions, the requirement is not applicable.

Create an event report. Report data can be based on date ranges, times or events, or other criteria that could be used in an investigation. Use of data from previous checks for audit reduction is encouraged.

Review the report and ensure the data in the report coincides with event filters used to create the report.

If the application does not provide an immediate, ad-hoc audit review and analysis capability, this is a finding.

**Check ID:**  C-24162r493384_chk

### Fix Text 

Design or configure the application to provide an immediate audit review capability or utilize a centralized utility designed for the purpose of on-demand log management and reporting.

**Fix ID:**  F-24151r493385_fix

**Vulnerability ID:**  V-222492

**Rule ID:**  SV-222492r961419_rule

---

## The application must provide a report generation capability that supports on-demand reporting requirements.

<span style="color:#ff8c00;font-size:150%;">Medium Severity</span>

### Description

The report generation capability must support on-demand reporting in order to facilitate the organization's ability to generate incident reports as needed to better handle larger-scale or more complex security incidents.

The report generation capability provided by the application must be capable of generating on-demand (i.e., customizable, ad-hoc, and as-needed) reports. On-demand reporting allows personnel to report issues more rapidly to more effectively meet reporting requirements. Collecting log data and aggregating it to present the data in a single, consolidated report achieves this objective.

This requirement is specific to applications with report generation capabilities; however, applications need to support on-demand reporting requirements.

### Check Text

Review the application documentation and interview the application administrator for details regarding audit reduction (log record event filtering).

Access the application with user rights sufficient to read and filter audit records.

Navigate the application user interface and select the application functionality that provides access and interface to audit records and audit reduction (event filtering).

If the application uses a centralized logging solution that provides immediate, customizable, ad-hoc report generation functions, the requirement is not applicable.

Create an event report. Report data can be based on date ranges, times or events, or other criteria that could be used in an investigation. Use of data from previous checks for audit reduction is encouraged.

Review the report and ensure the data in the report coincides with event filters used to create the report.

If the application does not provide customizable, immediate, ad-hoc audit log reporting, this is a finding.

**Check ID:**  C-24163r493387_chk

### Fix Text 

Design or configure the application to provide an on-demand report generation capability or utilize a centralized utility designed for the purpose of on-demand log management and reporting.

**Fix ID:**  F-24152r493388_fix

**Vulnerability ID:**  V-222493

**Rule ID:**  SV-222493r961422_rule

---

## The application must provide a report generation capability that supports after-the-fact investigations of security incidents.

<span style="color:#ff8c00;font-size:150%;">Medium Severity</span>

### Description

If the report generation capability does not support after-the-fact investigations, it is difficult to establish, correlate, and investigate the events leading up to an outage or attack, or identify those responses for one. This capability is also required to comply with applicable Federal laws and DoD policies.

The report generation capability must support after-the-fact investigations of security incidents either natively or through the use of third-party tools.

This requirement is specific to applications with report generation capabilities; however, applications need to support on-demand reporting requirements.

### Check Text

Review the application documentation and interview the application administrator for details regarding audit reduction (log record event filtering).

Access the application with user rights sufficient to read and filter audit records.

Navigate the application user interface and select the application functionality that provides access and interface to audit records and audit reduction (event filtering).

If the application uses a centralized logging solution that performs the report generation functions, the requirement is not applicable.

Create an event report. Report data can be based on date ranges, times or events, or other criteria that could be used in an investigation. Use of data from previous checks for audit reduction is encouraged.

Review the report and ensure the data in the report coincides with event filters used to create the report.

If the application does not have a report generation capability that supports after the fact security investigations, this is a finding.

**Check ID:**  C-24164r493390_chk

### Fix Text 

Design or configure the application to provide after-the-fact report generation capability or utilize a centralized utility designed for the purpose of log management and reporting.

**Fix ID:**  F-24153r493391_fix

**Vulnerability ID:**  V-222494

**Rule ID:**  SV-222494r961425_rule

---

## The application must provide an audit reduction capability that does not alter original content or time ordering of audit records.

<span style="color:#ff8c00;font-size:150%;">Medium Severity</span>

### Description

If the audit reduction capability alters the content or time ordering of audit records, the integrity of the audit records is compromised, and the records are no longer usable for forensic analysis. Time ordering refers to the chronological organization of records based on time stamps. The degree of time stamp precision can affect this.

Audit reduction is a process that manipulates collected audit information and organizes such information in a summary format that is more meaningful to analysts.

This requirement is specific to applications with audit reduction capabilities; however, applications need to support on-demand audit review and analysis.

### Check Text

Review the application documentation and interview the application administrator for details regarding audit reduction (log record event filtering).

Access the application with user rights sufficient to read and filter audit records.

Navigate the application user interface and select the application functionality that provides access and interface to audit records and audit reduction (event filtering).

If the application uses a centralized logging solution that performs the audit reduction (event filtering) functions, the requirement is not applicable.

Examine the log files; take note of dates and times of events such as logon events.

Note: dates and times as well as the original content and any unique record identifiers.

Record the identifying information as well as the dates and times and content of the audit records.

Apply filters to reduce the amount of audit records displayed to just the logon events for the day.

Review the records and ensure nothing in the records has changed. Once validated, clear the filter and review the records again to validate nothing changed within the audit record itself.

If the application of event filters modifies the original log records, this is a finding.

**Check ID:**  C-24165r493393_chk

### Fix Text 

Configure the application to not alter original log content or time ordering of audit records.

**Fix ID:**  F-24154r493394_fix

**Vulnerability ID:**  V-222495

**Rule ID:**  SV-222495r961428_rule

---

## The application must provide a report generation capability that does not alter original content or time ordering of audit records.

<span style="color:#ff8c00;font-size:150%;">Medium Severity</span>

### Description

If the audit report generation capability alters the original content or time ordering of audit records, the integrity of the audit records is compromised, and the records are no longer usable for forensic analysis. Time ordering refers to the chronological organization of records based on time stamps. The degree of time stamp precision can affect this.

The report generation capability provided by the application can generate customizable reports.

This requirement is specific to applications with audit reduction capabilities; however, applications need to support on-demand audit review and analysis.

### Check Text

Review the application documentation and interview the application administrator for details regarding audit reduction (log record event filtering).

Access the application with user rights sufficient to read and filter audit records.

Navigate the application user interface and select the application functionality that provides access and interface to audit records and audit reduction (event filtering).

If the application does not provide a report generation capability, the requirement is not applicable.

Examine the log files; take note of dates and times of events such as logon events.

Note: dates and times as well as the original content and any unique record identifiers.

Record the identifying information as well as the dates and times and content of the audit records.

Apply filters to reduce the amount of audit records displayed to just the logon events for the day.

Review the records and ensure nothing in the records has changed. Once validated, clear the filter and review the records again to validate nothing changed within the audit record itself.

If the application of event filters modifies the original log records, this is a finding.

**Check ID:**  C-24166r493396_chk

### Fix Text 

Configure and design the application to not modify source logs when filtering events.

**Fix ID:**  F-24155r493397_fix

**Vulnerability ID:**  V-222496

**Rule ID:**  SV-222496r961431_rule

---

## The applications must use internal system clocks to generate time stamps for audit records.

<span style="color:#ff8c00;font-size:150%;">Medium Severity</span>

### Description

Without an internal clock used as the reference for the time stored on each event to provide a trusted common reference for the time, forensic analysis would be impeded. Determining the correct time a particular event occurred on a system is critical when conducting forensic analysis and investigating system events.

If the internal clock is not used, the system may not be able to provide time stamps for log messages. Additionally, externally generated time stamps may not be accurate. Applications can use the capability of an operating system or purpose-built module for this purpose.

### Check Text

Review the system documentation and interview the application administrator for details regarding application architecture and logging configuration.

Identify the application components and the logs associated with the components.

Ensure the time written into the logs coincides with the OS timeclock.

Access random audit records and review the most recent logs.
 
Access the system OS hosting the application and use the related OS commands to determine the time of the system.

Perform an action in the application that causes a log event to be written and review the log to ensure the system times and the application log times correlate; compensating for any time delays that may have occurred between running the OS time command and running the application action.

If the application doesn't use the internal system clocks to generate time stamps for the audit event logs, this is a finding.

**Check ID:**  C-24167r493399_chk

### Fix Text 

Configure the application to use the hosting systems internal clock for audit record generation.

**Fix ID:**  F-24156r493400_fix

**Vulnerability ID:**  V-222497

**Rule ID:**  SV-222497r960927_rule

---

## The application must record time stamps for audit records that can be mapped to Coordinated Universal Time (UTC) or Greenwich Mean Time (GMT).

<span style="color:#ff8c00;font-size:150%;">Medium Severity</span>

### Description

If time stamps are not consistently applied and there is no common time reference, it is difficult to perform forensic analysis.

Time stamps generated by the application include date and time. Time is commonly expressed in Coordinated Universal Time (UTC), a modern continuation of Greenwich Mean Time (GMT), or local time with an offset from UTC.

### Check Text

Review the system documentation and interview the application administrator for details regarding application architecture and logging configuration.

Identify the application components and the logs associated with the components. 

If the application utilizes the underlying OS system clock, and the system clock is mapped to UTC or GMT, this is not a finding.

Identify where clock settings are configured within the application.

Access the configuration settings and determine if the application is configured to set the time stamps for audit records according to UTC or GMT (e.g., East coast standard time is represented as GMT -5, east coast daylight savings time is represented as GMT-4).

If the application is not configured to map to UTC or GMT, this is a finding.

**Check ID:**  C-24168r493402_chk

### Fix Text 

Configure the application to use the underlying system clock that maps to relevant UTC or GMT timezone.

**Fix ID:**  F-24157r493403_fix

**Vulnerability ID:**  V-222498

**Rule ID:**  SV-222498r961443_rule

---

## The application must record time stamps for audit records that meet a granularity of one second for a minimum degree of precision.

<span style="color:#ff8c00;font-size:150%;">Medium Severity</span>

### Description

Without sufficient granularity of time stamps, it is not possible to adequately determine the chronological order of records.

Time stamps generated by the application include date and time. Granularity of time measurements refers to the degree of synchronization between information system clocks and reference clocks.

### Check Text

Review the system documentation and interview the application administrator to determine where application audit logs are written and how time stamps are recorded.

If the application utilizes the underlying OS for time stamping and time synchronization when writing the audit logs, this requirement is not applicable.

Access and review log files over a period of at least 10 minutes; compare time stamps written in the application log to the system clock to ensure time is synchronized to within 1 second of precision.

If the application audit log time stamps differ from the OS time source by more than one second, this is a finding.

**Check ID:**  C-24169r493405_chk

### Fix Text 

Configure the application to leverage the underlying operating system as the time source when recording time stamps or design the application to ensure granularity of 1 second as the minimum degree of precision.

**Fix ID:**  F-24158r493406_fix

**Vulnerability ID:**  V-222499

**Rule ID:**  SV-222499r961446_rule

---

## The application must protect audit information from any type of unauthorized read access.

<span style="color:#ff8c00;font-size:150%;">Medium Severity</span>

### Description

If audit data were to become compromised, then competent forensic analysis and discovery of the true source of potentially malicious system activity is difficult if not impossible to achieve. In addition, access to audit records provides information an attacker could potentially use to his or her advantage.

To ensure the veracity of audit data, the information system and/or the application must protect audit information from any and all unauthorized access. This includes read, write, and copy access.

This requirement can be achieved through multiple methods which will depend upon system architecture and design. Commonly employed methods for protecting audit information include least privilege permissions as well as restricting the location and number of log file repositories.

Additionally, applications with user interfaces to audit records should not allow for the unfettered manipulation of or access to those records via the application. If the application provides access to the audit data, the application becomes accountable for ensuring audit information is protected from unauthorized access.

Audit information includes all information (e.g., audit records, audit settings, and audit reports) needed to successfully audit information system activity.

### Check Text

Review the system documentation and interview the application administrator for details regarding application architecture and logging configuration.

Identify the application components and the logs associated with the components.

Identify the roles and users allowed to access audit information and the circumstances in which they are allowed to read or otherwise access the data.

Identify the methods used to manage audit records and audit components. Typical methods are file system-based, via an application user interface via database access or a combination thereof.

For file system access: Review file system permissions to ensure the audit logs and the application audit components such as executable files and libraries are protected by adequate file permission restrictions.

Permissions must be configured to limit access to only those who have been identified and whose access has been approved.

If file permissions are configured to allow unapproved access, this is a finding.

For application-oriented and database access: Identify the application module that provides access to audit settings and audit data. Attempt to access audit configuration features and logs by using a regular non-privileged application or database user account.

If a non-privileged user account is allowed to access the audit data or the audit configuration settings, this is a finding.

**Check ID:**  C-24170r493408_chk

### Fix Text 

Configure the application to protect audit data from unauthorized access. Limit users to roles that are assigned the rights to view, edit or copy audit data, and establish permissions that control access to the audit logs and audit configuration settings.

**Fix ID:**  F-24159r493409_fix

**Vulnerability ID:**  V-222500

**Rule ID:**  SV-222500r960930_rule

---

## The application must protect audit information from unauthorized modification.

<span style="color:#ff8c00;font-size:150%;">Medium Severity</span>

### Description

If audit data were to become compromised, then forensic analysis and discovery of the true source of potentially malicious system activity is impossible to achieve.

To ensure the veracity of audit data, the information system and/or the application must protect audit information from unauthorized modification.

This requirement can be achieved through multiple methods, which will depend upon system architecture and design. Some commonly employed methods include ensuring log files receive the proper file system permissions, and limiting log data locations.

Applications providing a user interface to audit data will leverage user permissions and roles identifying the user accessing the data and the corresponding rights that the user enjoys in order to make access decisions regarding the modification of audit data.

Audit information includes all information (e.g., audit records, audit settings, and audit reports) needed to successfully audit information system activity.

### Check Text

Review the system documentation and interview the application administrator for details regarding application architecture and logging configuration.

Identify the application components and the logs associated with the components.

Identify the roles and users allowed to modify audit information and the circumstances in which they are allowed to modify the data.

Identify the methods used to manage audit records and audit components. Typical methods are file system-based, via an application user interface via database access or a combination thereof.

For file system access: Review file system permissions to ensure the audit logs and the application audit components such as executable files and libraries are protected by adequate file permission restrictions.

Permissions must be configured to limit write/modify access to only those who have been identified and whose access has been approved.

If file permissions are configured to allow unapproved write/modify access, this is a finding.

For application oriented and database access: Identify the application module that provides access to audit settings and audit data. Attempt to access audit configuration features and logs by using a regular non-privileged application or database user account. Once access has been established, attempt to modify an audit record and attempt to modify the audit settings.

If a non-privileged user account is allowed to modify the audit data or the audit configuration settings, this is a finding.

**Check ID:**  C-36240r602285_chk

### Fix Text 

Configure the application to protect audit data from unauthorized modification and changes. Limit users to roles that are assigned the rights to edit audit data and establish permissions that control access to the audit logs and audit configuration settings.

**Fix ID:**  F-36206r602286_fix

**Vulnerability ID:**  V-222501

**Rule ID:**  SV-222501r960933_rule

---

## The application must protect audit information from unauthorized deletion.

<span style="color:#ff8c00;font-size:150%;">Medium Severity</span>

### Description

If audit data were to become compromised, then forensic analysis and discovery of the true source of potentially malicious system activity is impossible to achieve.

To ensure the veracity of audit data, the information system and/or the application must protect audit information from unauthorized deletion. This requirement can be achieved through multiple methods, which will depend upon system architecture and design.

Some commonly employed methods include: ensuring log files receive the proper file system permissions utilizing file system protections, restricting access, and backing up log data to ensure log data is retained.

Applications providing a user interface to audit data will leverage user permissions and roles identifying the user accessing the data and the corresponding rights the user enjoys in order make access decisions regarding the deletion of audit data.

Audit information includes all information (e.g., audit records, audit settings, and audit reports) needed to successfully audit information system activity. Audit information may include data from other applications or be included with the audit application itself.

### Check Text

Review the system documentation and interview the application administrator for details regarding application architecture and logging configuration.

Identify the application components and the logs associated with the components.

Identify the roles and users allowed to delete audit information and the circumstances in which they are allowed to delete the data.

Identify the methods used to manage audit records and audit components. Typical methods are file system-based, via an application user interface via database access or a combination thereof.

For file system access: Review file system permissions to ensure the audit logs and the application audit components such as executable files and libraries are protected by adequate file permission restrictions.

Permissions must be configured to limit deletions to only those who have been identified and whose rights to delete audit data and audit configurations has been approved.

If file permissions are configured to allow unapproved deletions of audit settings and data, this is a finding.

For application oriented and database access: Identify the application module that provides access to audit settings and audit data. Attempt to access audit configuration features and logs by using a regular non-privileged application or database user account. Once access has been established, attempt to delete a test audit record and attempt to delete a test audit settings.

If a non-privileged user account is allowed to delete the audit data or the audit configuration settings, this is a finding.

**Check ID:**  C-24172r493414_chk

### Fix Text 

Configure the application to protect audit data from unauthorized deletion. Limit users to roles that are assigned the rights to delete audit data and establish permissions that control access to the audit logs and audit configuration settings.

**Fix ID:**  F-24161r493415_fix

**Vulnerability ID:**  V-222502

**Rule ID:**  SV-222502r960936_rule

---

## The application must protect audit tools from unauthorized access.

<span style="color:#ff8c00;font-size:150%;">Medium Severity</span>

### Description

Protecting audit data also includes identifying and protecting the tools used to view and manipulate log data. Therefore, protecting audit tools is necessary to prevent unauthorized operation on audit data.

Applications providing tools to interface with audit data will leverage user permissions and roles identifying the user accessing the tools and the corresponding rights the user enjoys in order make access decisions regarding the access to audit tools.

Audit tools include, but are not limited to, vendor-provided and open source audit tools needed to successfully view and manipulate audit information system activity and records. Audit tools include custom queries and report generators.

### Check Text

Review the system documentation and interview the application administrator for details regarding application architecture, audit methods, and audit tools.

Identify the application audit tools and their locations.

If the application does not provide a distinct audit tool oriented functionality that is a separate tool with an ability to view and manipulate log data, this requirement is not applicable.

Identify the methods used for implementing the audit tool functionality within the application. Typical methods are file system-based, e.g., a separate executable file that when invoked provides audit functionality, an application user interface to an audit module, or a combination thereof.

For file system access: Review file system permissions to ensure the application audit components such as executable files and libraries are protected by adequate file permission restrictions.

Permissions must be configured to limit access to only those who have been identified and whose access has been approved.

If file permissions are configured to allow unapproved access, this is a finding.

For circumstances where audit tools are accessed via application sub-modules or menus: Identify the application module that provides access to audit settings and audit data. Attempt to access audit configuration features and logs by using a regular non-privileged application or database user account.

If a non-privileged user account is allowed to access the audit data or the audit configuration settings, this is a finding.

**Check ID:**  C-36241r602288_chk

### Fix Text 

Configure the application to protect audit data from unauthorized access. Limit users to roles that are assigned the rights to view, edit or copy audit data, and establish file permissions that control access to the audit tools and audit tool capabilities and configuration settings.

**Fix ID:**  F-36207r602289_fix

**Vulnerability ID:**  V-222503

**Rule ID:**  SV-222503r960939_rule

---

## The application must protect audit tools from unauthorized modification.

<span style="color:#ff8c00;font-size:150%;">Medium Severity</span>

### Description

Protecting audit data also includes identifying and protecting the tools used to view and manipulate log data. Therefore, protecting audit tools is necessary to prevent unauthorized operation on audit data.

Applications providing tools to interface with audit data will leverage user permissions and roles identifying the user accessing the tools and the corresponding rights the user enjoys in order make access decisions regarding the modification of audit tools.

Audit tools include, but are not limited to, vendor-provided and open source audit tools needed to successfully view and manipulate audit information system activity and records. Audit tools include custom queries and report generators.

### Check Text

Review the system documentation and interview the application administrator for details regarding application architecture, audit methods, and provided audit tools.

Identify the application audit tools and their locations.

If the application does not provide a distinct audit tool oriented functionality that is a separate tool with an ability to view and manipulate log data, this requirement is not applicable.

Identify the methods used for implementing an audit tool functionality that is separate from the application. Typical methods are file-oriented in nature, e.g., the application includes a separate executable file or library that when invoked allows users to view and manipulate logs.

Identify the users with the rights to modify the audit tools. This capability will usually be reserved for admin staff.

Review file system permissions to ensure the application audit components such as executable files and libraries are protected by adequate file permission restrictions.

File permissions must be configured to limit access to only those users who have been identified and whose access has been approved.

If file permissions are configured so as to allow unapproved modifications to the audit tools, this is a finding.

**Check ID:**  C-36242r602291_chk

### Fix Text 

Configure the application to protect audit tools from unauthorized modifications. Limit users to roles that are assigned the rights to edit or update audit tools and establish file permissions that control access to the audit tools and audit tool capabilities and configuration settings.

**Fix ID:**  F-36208r602292_fix

**Vulnerability ID:**  V-222504

**Rule ID:**  SV-222504r960942_rule

---

## The application must protect audit tools from unauthorized deletion.

<span style="color:#ff8c00;font-size:150%;">Medium Severity</span>

### Description

Protecting audit data also includes identifying and protecting the tools used to view and manipulate log data. Therefore, protecting audit tools is necessary to prevent unauthorized operation on audit data.

Applications providing tools to interface with audit data will leverage user permissions and roles identifying the user accessing the tools and the corresponding rights the user enjoys in order make access decisions regarding the deletion of audit tools.

Audit tools include, but are not limited to, vendor-provided and open source audit tools needed to successfully view and manipulate audit information system activity and records. Audit tools include custom queries and report generators.

### Check Text

Review the system documentation and interview the application administrator for details regarding application architecture, audit methods and provided audit tools.

Identify the application audit tools and their locations.

If the application does not provide a distinct audit tool oriented functionality that is a separate tool with an ability to view and manipulate log data, this requirement is not applicable.

Identify the methods used for implementing an audit tool functionality that is separate from the application. Typical methods are file-oriented in nature, e.g., the application includes a separate executable file or library that when invoked allows users to view and manipulate logs.

Identify the users with the rights to delete the audit tools. This capability is normally reserved for admin staff.

Review file system permissions to ensure the application audit components such as executable files and libraries are protected by adequate file permission restrictions.

File permissions must be configured to limit access to only those users who have been identified and whose access has been approved.

If file permissions are configured to allow unapproved deletions of the audit tools, this is a finding.

**Check ID:**  C-36243r602294_chk

### Fix Text 

Configure the application to protect audit tools from unauthorized deletions. Limit users to roles that are assigned the rights to edit or delete audit tools and establish file permissions that control access to the audit tools and audit tool capabilities and configuration settings.

**Fix ID:**  F-36209r602295_fix

**Vulnerability ID:**  V-222505

**Rule ID:**  SV-222505r960945_rule

---

## The application must back up audit records at least every seven days onto a different system or system component than the system or component being audited.

<span style="color:#ff8c00;font-size:150%;">Medium Severity</span>

### Description

Protection of log data includes assuring log data is not accidentally lost or deleted. Backing up audit records to a different system or onto separate media than the system being audited on an organizationally defined frequency helps to assure in the event of a catastrophic system failure, the audit records will be retained.

This helps to ensure a compromise of the information system being audited does not also result in a compromise of the audit records.

This requirement only applies to applications that have a native backup capability for audit records. Operating system backup requirements cover applications that do not provide native backup functions.

### Check Text

Review the application documentation and interview the application administrator.

Identify log functionality and locations of log files.

If the application does not include a built-in backup capability for backing up its own audit records, this requirement is not applicable.

Access the management interface for configuring application audit logs and review the backup settings.

If the application backup settings are not configured to backup application audit records every 7 days, this is a finding.

**Check ID:**  C-24176r493426_chk

### Fix Text 

Configure application backup settings to backup application audit logs every 7 days.

**Fix ID:**  F-24165r493427_fix

**Vulnerability ID:**  V-222506

**Rule ID:**  SV-222506r960948_rule

---

## The application must use cryptographic mechanisms to protect the integrity of audit information.

<span style="color:#ff8c00;font-size:150%;">Medium Severity</span>

### Description

Audit records may be tampered with; if the integrity of audit data were to become compromised, then forensic analysis and discovery of the true source of potentially malicious system activity is impossible to achieve.

Protection of audit records and audit data is of critical importance. Cryptographic mechanisms are the industry established standard used to protect the integrity of audit data. An example of a cryptographic mechanism is the computation and application of a cryptographic-signed hash using asymmetric cryptography.

This requirement applies to applications that generate, process or manage audit records and is applied once audit processing has completed and the audit record is being stored.

### Check Text

Review the system documentation and interview the application administrator for details regarding application architecture, audit methods, and provided audit tools.

Identify the location of the application audit information.

If the application is configured to utilize a centralized audit log solution that uses cryptographic methods that meet this requirement such as creating cryptographic hash values or message digests that can be used to validate integrity of audit files, the requirement is not applicable.

Ask application administrator to demonstrate the cryptographic mechanisms used to protect the integrity of audit data.

Verify when application logs are stored on the file system, a process that includes the creation of an integrity check of the audit file being stored is utilized. This integrity check can be the creation of a checksum, message digest or other one-way cryptographic hash of the audit file that is created.

If an integrity check is not created to protect the integrity of the audit information, this is a finding.

**Check ID:**  C-24177r493429_chk

### Fix Text 

Configure the application to create an integrity check consisting of a cryptographic hash or one-way digest that can be used to establish the integrity when storing log files.

**Fix ID:**  F-24166r493430_fix

**Vulnerability ID:**  V-222507

**Rule ID:**  SV-222507r960951_rule

---

## Application audit tools must be cryptographically hashed.

<span style="color:#ff8c00;font-size:150%;">Medium Severity</span>

### Description

Protecting the integrity of the tools used for auditing purposes is a critical step to ensuring the integrity of audit data. Audit data includes all information (e.g., audit records, audit settings, and audit reports) needed to successfully audit information system activity.

Audit tools include, but are not limited to, vendor provided and open source audit tools needed to successfully view and manipulate audit information system activity and records. Audit tools include custom queries and report generators.

It is not uncommon for attackers to replace the audit tools or inject code into the existing tools with the purpose of providing the capability to hide or erase system activity from the audit logs.

To address this risk, audit tools must be cryptographically signed/hashed and the resulting value securely stored in order to provide the capability to identify when the audit tools have been modified, manipulated or replaced.

Some OSs provide a native command line tool capable of extracting or creating a hash value. Care must be taken to ensure any hashing algorithm strength used is acceptable.  An example is UNIX OS variants that provide the "shasum" utility with SHA256 capabilities.  Windows is not known to provide a native cryptographic tool that utilizes an acceptable hashing algorithm.  The Windows fciv.exe checksum tool currently only utilizes MD5 and SHA1 which are not acceptable hashing algorithms.

### Check Text

Review the system documentation and interview the application administrator for details regarding application architecture, audit methods, and provided audit tools.

Identify the location of the application audit tools.

Separate audit tools will be file-oriented in nature, e.g., the application includes a separate executable file or library that when invoked allows users to view and manipulate logs.

If the application does not provide a separate tool in the form of a file which provides an ability to view and manipulate application log data, query data, or generate reports, this requirement is not applicable.

If the system hosting the application has a separate file monitoring utility installed that is configured to identify changes to audit tools and alarm on changes to audit tools, this is not applicable.

Ask application administrator to demonstrate the cryptographic hashing mechanisms used to create the one way hashes that can be used to validate the integrity of audit tools.

For example, "shasum /path/to/file > checksum.filename".

Ask the application administrator to provide the list of checksum values and the associated file names of the audit tools.

If a cryptographic checksum or hash value of the audit tool file is not created for future reference, this is a finding.

**Check ID:**  C-24178r493432_chk

### Fix Text 

Cryptographically hash the audit tool files used by the application. Store and protect the generated hash values for future reference.

**Fix ID:**  F-24167r493433_fix

**Vulnerability ID:**  V-222508

**Rule ID:**  SV-222508r961206_rule

---

## The integrity of the audit tools must be validated by checking the files for changes in the cryptographic hash value.

<span style="color:#ff8c00;font-size:150%;">Medium Severity</span>

### Description

Protecting the integrity of the tools used for auditing purposes is a critical step to ensuring the integrity of audit data. Audit data includes all information (e.g., audit records, audit settings, and audit reports) needed to successfully audit information system activity.

Audit tools include, but are not limited to, vendor provided and open source audit tools needed to successfully view and manipulate audit information system activity and records. Audit tools include custom queries and report generators.

It is not uncommon for attackers to replace the audit tools or inject code into the existing tools with the purpose of providing the capability to hide or erase system activity from the audit logs. 

To address this risk, audit tools must be cryptographically signed/hashed in order to provide the capability to identify when the audit tools have been modified, manipulated or replaced. An example is a checksum hash of the file or files.

### Check Text

Review the system documentation and interview the application administrator for details regarding application architecture, audit methods, and provided audit tools.

Identify the location of the application audit tools.

Separate audit tools will be file-oriented in nature, e.g., the application includes a separate executable file or library that when invoked allows users to view and manipulate logs.

If the application does not provide a separate tool in the form of a file which provides an ability to view and manipulate application log data, query data or generate reports, this requirement is not applicable.

If the system hosting the application has a separate file monitoring utility installed that is configured to identify changes to audit tools and alarm on changes to audit tools, this is not applicable.

Ask the application administrator to provide their process for periodically checking the list of checksum values against the associated file names of the audit tools to ensure none of the audit tools have been tampered with.

If a cryptographic checksum or hash value of the audit tool file is not periodically checked to ensure the integrity of audit tools, this is a finding.

**Check ID:**  C-24179r493435_chk

### Fix Text 

Establish a process to periodically check the audit tool cryptographic hashes to ensure the audit tools have not been tampered with.

**Fix ID:**  F-24168r493436_fix

**Vulnerability ID:**  V-222509

**Rule ID:**  SV-222509r961206_rule

---

## The application must prohibit user installation of software without explicit privileged status.

<span style="color:#ff8c00;font-size:150%;">Medium Severity</span>

### Description

Allowing regular users to install software without explicit privileges creates the risk that untested or potentially malicious software will be installed on the system. Explicit privileges (escalated or administrative privileges) provide the regular user with explicit capabilities and control that exceeds the rights of a regular user.

Application functionality will vary, and while users are not permitted to install unapproved applications, there may be instances where the organization allows the user to install approved software packages such as from an approved software repository.

The application must enforce software installation by users based upon what types of software installations are permitted (e.g., updates and security patches to existing software) and what types of installations are prohibited (e.g., software whose pedigree with regard to being potentially malicious is unknown or suspect) by the organization.

For example, this requirement applies to applications that provide the ability to extend application functionality (e.g., plug-ins, add-ons) and software management applications.

### Check Text

Review the application documentation and interview the application administrator to determine the capabilities of the application as it relates to software installation or product function extension.

Identify any software configuration change capabilities which are allowed by design and incorporated into the user interface. An example is utilizing a known software repository of tested and approved extensions, plugins, or modules which can be used by application users to extend application features or functions.

If the application does not provide the ability to install software components, modules, plugins, or extensions, the requirement is Not Applicable.

Access the application user interface as a regular user, navigate to the application screen that provides the software installation function and attempt to install software components, modules, extensions, or plugins.

If the application utilizes an approved repository of approved software that has been tested and approved for all application users to install, this is not a finding.

If the application allows regular users to install untested or unapproved software components, extensions, modules, or plugins without explicit authorization, this is a finding.

**Check ID:**  C-24180r985918_chk

### Fix Text 

Configure the application to prohibit user installation of software without explicit permission.

**Fix ID:**  F-24169r493439_fix

**Vulnerability ID:**  V-222510

**Rule ID:**  SV-222510r1015689_rule

---

## The application must enforce access restrictions associated with changes to application configuration.

<span style="color:#ff8c00;font-size:150%;">Medium Severity</span>

### Description

Failure to provide logical access restrictions associated with changes to application configuration may have significant effects on the overall security of the system.

When dealing with access restrictions pertaining to change control, it should be noted that any changes to the hardware, software, and/or firmware components of the information system and/or application can potentially have significant effects on the overall security of the system.

Accordingly, only qualified and authorized individuals should be allowed to obtain access to application components for the purposes of initiating changes, including upgrades and modifications.

Logical access restrictions include, for example, controls that restrict access to workflow automation, media libraries, abstract layers (e.g., changes implemented into third-party interfaces rather than directly into information systems), and change windows (e.g., changes occur only during specified times, making unauthorized changes easy to discover).

### Check Text

Review the application documentation and configuration settings.

Access the application configuration settings interface as a regular non-privileged user. Attempt to make configuration changes to the application.

If configuration changes can be made by regular non-privileged users, this is a finding.

Review the locations of all configuration files used by the application.

Examine the file permission settings and determine who has access to the configuration files.

If access permissions to configuration files are not restricted to application administrators, this is a finding.

**Check ID:**  C-24181r493441_chk

### Fix Text 

Configure the application to limit access to configuration settings to only authorized users.

**Fix ID:**  F-24170r493442_fix

**Vulnerability ID:**  V-222511

**Rule ID:**  SV-222511r961461_rule

---

## The application must audit who makes configuration changes to the application.

<span style="color:#ff8c00;font-size:150%;">Medium Severity</span>

### Description

Without auditing the enforcement of access restrictions against changes to the application configuration, it will be difficult to identify attempted attacks and an audit trail will not be available for forensic investigation for after-the-fact actions.

Enforcement actions are the methods or mechanisms used to prevent unauthorized changes to configuration settings. Enforcement action methods may be as simple as denying access to a file based on the application of file permissions (access restriction). Audit items may consist of lists of actions blocked by access restrictions or changes identified after the fact.

If application configuration is maintained by using a text editor to modify a configuration file, this function may be delegated to an operating system file monitoring/auditing capability.

### Check Text

Review the application documentation and configuration settings.

Access the application configuration settings interface as a privileged user.

Make configuration changes to the application.

Review the application audit logs and ensure a log entry is made identifying the privileged user account that was used to make the changes.

If application configuration is maintained by using a text editor to modify a configuration file, modify the configuration file with a text editor. Review the system logs and ensure a log entry is made for the file modification that identifies the user that was used to make the changes.

If the user account is not logged, or is a group account such as "root", this is a finding.

If the user account used to make the changes is not logged in the audit records, this is a finding.

**Check ID:**  C-24182r493444_chk

### Fix Text 

Configure the application to create log entries that can be used to identify the user accounts that make application configuration changes.

**Fix ID:**  F-24171r493445_fix

**Vulnerability ID:**  V-222512

**Rule ID:**  SV-222512r1015690_rule

---

## The application must have the capability to prevent the installation of patches, service packs, or application components without verification the software component has been digitally signed using a certificate that is recognized and approved by the organization.

<span style="color:#ff8c00;font-size:150%;">Medium Severity</span>

### Description

Changes to any software components can have significant effects on the overall security of the application. Verifying software components have been digitally signed using a certificate that is recognized and approved by the organization ensures the software has not been tampered with and that it has been provided by a trusted vendor.

Accordingly, patches, service packs, or application components must be signed with a certificate recognized and approved by the organization.

Verifying the authenticity of the software prior to installation validates the integrity of the patch or upgrade received from a vendor. This ensures the software has not been tampered with and that it has been provided by a trusted vendor. Self-signed certificates are disallowed by this requirement. The application should not have to verify the software again. This requirement does not mandate DOD certificates for this purpose; however, the certificate used to verify the software must be from an approved certificate authority (CA).

If this capability is not present, the vendor must provide a cryptographic hash value that can be verified by a system administrator prior to installation.

### Check Text

Review the application documentation and interview the application administrator to determine the process and commands used for patching the application.

Access application configuration settings.

Review commands and procedures used to patch the application and ensure a capability exists to prevent unsigned patches from being applied.

If the application is not capable of preventing installation of patches and packages that are not signed, or if the vendor does not provide a cryptographic hash value that can be manually checked prior to installation, this is a finding.

**Check ID:**  C-36244r602297_chk

### Fix Text 

Design and configure the application to have the capability to prevent unsigned patches and packages from being installed.

Provide a cryptographic hash value that can be verified by a system administrator prior to installation.

**Fix ID:**  F-36210r985921_fix

**Vulnerability ID:**  V-222513

**Rule ID:**  SV-222513r1015691_rule

---

## The applications must limit privileges to change the software resident within software libraries.

<span style="color:#ff8c00;font-size:150%;">Medium Severity</span>

### Description

If the application were to allow any user to make changes to software libraries, then those changes might be implemented without undergoing the appropriate testing and approvals that are part of a robust change management process.

This requirement applies to applications with software libraries that are accessible and configurable, as in the case of interpreted languages. Software libraries also include privileged programs which execute with escalated privileges. Only qualified and authorized individuals will be allowed to obtain access to information system components for purposes of initiating changes, including upgrades and modifications.

### Check Text

Review the application documentation and interview the application administrator to identify the application architecture.

Identify application folders where application libraries are stored.

Review permissions of application folders and library files contained with the folders to ensure file permissions restrict access to authorized users or processes.

Access application configuration settings.

Examine settings for capability to update software libraries or extend application functionality via the application.

Review user roles and access rights within the application to determine if access to this capability is restricted to authorized users.

If file restrictions do not limit write access to library files and if the application does not restrict access to library update functionality, this is a finding.

**Check ID:**  C-24184r493450_chk

### Fix Text 

Configure the application OS file permissions to restrict access to software libraries and configure the application to restrict user access regarding software library update functionality to only authorized users or processes.

**Fix ID:**  F-24173r493451_fix

**Vulnerability ID:**  V-222514

**Rule ID:**  SV-222514r960960_rule

---

## An application vulnerability assessment must be conducted.

<span style="color:#ff8c00;font-size:150%;">Medium Severity</span>

### Description

An application vulnerability assessment is a test conducted in order to identify weaknesses and security vulnerabilities that may exist within an application.  The testing must cover all aspects and components of the application architecture.  If an application consists of a web server and a database, then both components must be tested for vulnerabilities to the fullest extent possible.

Vulnerability assessment tests normally utilize a combination of specialized software called application vulnerability scanners as well as custom scripts and manual tests.  In some instances, multiple tools are required in order to test all aspects of application features, functions and architecture.  The vulnerability scanner is typically configured to communicate with the application through the user interface or via an applications communication port.  In addition to using automated tools, manual tests conducted from the OS console such as executing custom scripts or reviewing configuration settings for known vulnerabilities may also be included as part of the test.

Testers will typically utilize application user test accounts in order to test application features and functionality such as adding content, executing queries and completing transactions. The vulnerability testing software utilizes user actions and access as well as a list of known security vulnerabilities in order to detect and identify weak security controls or misconfigurations that could potentially be manipulated by the user or create a security vulnerability.

The Open Web Application Security Project (OWASP) top 10 for 2013 includes the following top issues that should be tested.  The site is available by pointing your browser to https://www.owasp.org. 

A1 Injection
A2 Weak authentication and session management
A3 XSS
A4 Insecure Direct Object References
A5 Security Misconfiguration
A6 Sensitive Data Exposure
A7 Missing Function Level Access Control
A8 Cross Site Request Forgery
A9 Using Components with Known Vulnerabilities
A10 Unvalidated Redirects and Forwards

The OWASP top 10 are categories of tests that can be applied to most but not necessarily all applications and are provided as an example of what to test for.  Scanning tools include a multitude of tests that fall under these categories but may refer to these tests by a different name.

Testing must be conducted on a periodic basis while the application is in production and subsequent to system changes to ensure any changes made to the system do not introduce new security vulnerabilities.

### Check Text

Review the application documentation to understand application architecture.

Interview the application administrator, obtain and review their application vulnerability scanning process.

Request the latest scan results including scan configuration settings.

Review scan configurations and ensure coverage of all application architecture has been tested.  The proper scanning tool or combination of tools must be utilized in order to ensure the full range of application features and functionality is tested. 

For example, if the application includes a web interface and a SQL database, then ensure test results for web and SQL vulnerabilities are provided.  Although web and SQL applications are included as examples and are the prevalent types of applications, this requirement is not intended to be limited to just the aforementioned application architectures.   Ensure test results are provided from all testing tools employed during vulnerability testing.

If high risk security vulnerabilities are identified in the scan results, request subsequent test results that indicate the issues have been fixed or mitigated.

If the high risk issues identified in the report have not been fixed or mitigated to a level accepted by the ISSO and the ISSM, or if the application administrator cannot produce vulnerability security testing results that cover the range of application functionality, this is a finding.

**Check ID:**  C-24185r493453_chk

### Fix Text 

Configure the application vulnerability scanners to test all components of the application, conduct vulnerability scans on a regular basis and remediate identified issues.  Retain scan results for compliance verification.

**Fix ID:**  F-24174r493454_fix

**Vulnerability ID:**  V-222515

**Rule ID:**  SV-222515r961863_rule

---

## The application must prevent program execution in accordance with organization-defined policies regarding software program usage and restrictions, and/or rules authorizing the terms and conditions of software program usage.

<span style="color:#ff8c00;font-size:150%;">Medium Severity</span>

### Description

Control of application execution is a mechanism used to prevent execution of unauthorized applications in order to follow the rules of least privilege. Some applications may provide a capability that runs counter to the mission or provides users with functionality that exceeds mission requirements.

Some of the functions and services, provided by default, may not be necessary to support essential organizational operations (e.g., key missions, functions). Removal of executable programs is not always possible; therefore, establishing a method of preventing program execution is critical to maintaining a secure system baseline.

Software program restrictions include restricting execution of programs in certain environments, while preventing execution in other environments; or limiting execution of certain application functionality based on organization-defined criteria (e.g., privileges, subnets, sandboxed environments, security managers, roles).

### Check Text

Review the application documentation and interview the application administrator to determine if policies, rules, or restrictions exist regarding application usage or terms which authorize the conditions of application use.

If the policy, terms, or conditions state there are no usage restrictions, this requirement is not applicable.

Interview the application administrator, review policy, terms, and conditions documents to determine what the terms and conditions of application usage are.

Have the application administrator demonstrate how the program execution is restricted in accordance with the policy terms and conditions. Typical methods include but are not limited to the use of Windows Group Policy, AppLocker, Software Restriction Policies, Java Security Manager, and Role-Based Access Control (RBAC).

If application requirements or policy documents specify application execution restriction requirements and the execution of the application or its subcomponents are not restricted in accordance with requirements or policy, this is a finding.

**Check ID:**  C-24186r493456_chk

### Fix Text 

Restrict application execution in accordance with the policy, terms, and conditions specified.

**Fix ID:**  F-24175r493457_fix

**Vulnerability ID:**  V-222516

**Rule ID:**  SV-222516r961473_rule

---

## The application must employ a deny-all, permit-by-exception (whitelist) policy to allow the execution of authorized software programs.

<span style="color:#ff8c00;font-size:150%;">Medium Severity</span>

### Description

Utilizing a whitelist provides a configuration management method for allowing the execution of only authorized software. Using only authorized software decreases risk by limiting the number of potential vulnerabilities.

The organization must identify authorized software programs and permit execution of authorized software. The process used to identify software programs that are authorized to execute on organizational information systems is commonly referred to as whitelisting.

Verification of whitelisted software can occur either prior to execution or at system startup.

This requirement applies to configuration management applications or similar types of applications designed to manage system processes and configurations (e.g., HBSS and software wrappers).

### Check Text

If the application is not a configuration management or similar type of application designed to manage system processes and configurations, this requirement is not applicable.

Review the application documentation and interview the application administrator to identify if application whitelisting specifying which applications or application subcomponents are allowed to execute is in use.

Check for the existence of policy settings or policy files that can be configured to restrict application execution. Have the application administrator demonstrate how the program execution is restricted. Look for a deny-all, permit-by-exception policy of restriction.

Some methods for restricting execution include but are not limited to the use of custom capabilities built into the application or leveraging of Windows Group Policy, AppLocker, Software Restriction Policies, Java Security Manager or Role-Based Access Controls (RBAC).

If application whitelisting is not utilized or does not follow a deny-all, permit-by-exception (whitelist) policy, this is a finding.

**Check ID:**  C-24187r493459_chk

### Fix Text 

Configure the application to utilize a deny-all, permit-by-exception policy when allowing the execution of authorized software.

**Fix ID:**  F-24176r493460_fix

**Vulnerability ID:**  V-222517

**Rule ID:**  SV-222517r961479_rule

---

## The application must be configured to disable non-essential capabilities.

<span style="color:#ff8c00;font-size:150%;">Medium Severity</span>

### Description

It is detrimental for applications to provide, or install by default, functionality exceeding requirements or mission objectives. These unnecessary capabilities or services are often overlooked and therefore may remain unsecured. They increase the risk to the platform by providing additional attack vectors.

Applications are capable of providing a wide variety of functions and services. Some of the functions and services, provided by default, may not be necessary to support essential organizational operations (e.g., key missions, functions).

Examples of non-essential capabilities include, but are not limited to, advertising software or browser plug-ins not related to requirements or providing a wide array of functionality not required for every mission, but cannot be disabled.

### Check Text

Review the application guidance, application requirements documentation, and interview the application administrator.

Identify the application's operational requirements and what services the application is intended to provide users.

Review the overall application features and functionality via the user interface.

Review and identify installed application software modules via configuration settings.

Using the relevant OS commands, identify services running on the system and have the application administrator identify the services related to the application.

If the application is operating with extraneous capabilities that have not been defined as required in order to meet mission objectives, this is a finding.

**Check ID:**  C-24188r493462_chk

### Fix Text 

Disable application extraneous application functionality that is not required in order to fulfill the application's mission.

**Fix ID:**  F-24177r493463_fix

**Vulnerability ID:**  V-222518

**Rule ID:**  SV-222518r960963_rule

---

## The application must be configured to use only functions, ports, and protocols permitted to it in the PPSM CAL.

<span style="color:#ff8c00;font-size:150%;">Medium Severity</span>

### Description

In order to prevent unauthorized connection of devices, unauthorized transfer of information, or unauthorized tunneling (i.e., embedding of data types within data types), organizations must disable or restrict unused or unnecessary physical and logical ports/protocols on information systems.

Applications are capable of providing a wide variety of functions and services. Some of the functions and services provided by default may not be necessary to support essential organizational operations. Additionally, it is sometimes convenient to provide multiple services from a single component (e.g., email and web services; however, doing so increases risk over limiting the services provided by any one component.

To support the requirements and principles of least functionality, the application must support the organizational requirements providing only essential capabilities and limiting the use of ports, protocols, and/or services to only those required, authorized, and approved to conduct official business or to address authorized quality of life issues.

### Check Text

Review the application documentation and configuration.

Interview the application administrator.

Identify the network ports and protocols that are utilized by the application.

Using a combination of relevant OS commands and application configuration utilities, identify the TCP/IP port numbers the application is configured to utilize and is utilizing.

Review the PPSM Category Assurance List (CAL) at: 

https://cyber.mil/ppsm/cal/

Verify the ports used by the application are approved by the PPSM CAL.

If the ports are not approved by the PPSM CAL, this is a finding.

**Check ID:**  C-24189r918118_chk

### Fix Text 

Configure the application to utilize application ports approved by the PPSM CAL.

**Fix ID:**  F-24178r493466_fix

**Vulnerability ID:**  V-222519

**Rule ID:**  SV-222519r1043177_rule

---

## The application must require users to reauthenticate when organization-defined circumstances or situations require reauthentication.

<span style="color:#ff8c00;font-size:150%;">Medium Severity</span>

### Description

Without reauthentication, users may access resources or perform tasks for which they do not have authorization.

When applications provide the capability to change security roles or escalate the functional capability of the application, it is critical the user reauthenticate.

In addition to the reauthentication requirements associated with session locks, organizations may require reauthentication of individuals and/or devices in other situations, including (but not limited to) the following circumstances:

(i) When authenticators change;
(ii) When roles change;
(iii) When security categories of information systems change;
(iv) When the execution of privileged functions occurs;
(v) After a fixed period of time;
or
(vi) Periodically.

Within the DOD, the minimum circumstances requiring reauthentication are privilege escalation and role changes.

### Check Text

Review the application guidance and interview the application administrator.

Identify the application user roles.

Identify the methods and manner in which an application user is allowed to escalate their privileges or change their role.

Create or utilize an account that has two roles within the application, both should be nonadministrator.
Example: User role and Report Creator role.

Authenticate to the application as the user in the User role.

Access the application functionality that allows the user to change their role and change from the User role to the Report Creator role.

If the user is not prompted to reauthenticate before the user’s role is changed, this is a finding.

Log out of the application and log back in as the User role.

Access the application functionality that allows the user to escalate their privileges to an administrative user.

Attempt to escalate the privileges of the user.

If the user is not prompted to reauthenticate before the user is allowed to proceed with escalated privileges, this is a finding.

**Check ID:**  C-24190r985923_chk

### Fix Text 

Configure the application to require reauthentication before user privilege is escalated and user roles are changed.

**Fix ID:**  F-24179r493469_fix

**Vulnerability ID:**  V-222520

**Rule ID:**  SV-222520r1050664_rule

---

## The application must require devices to reauthenticate when organization-defined circumstances or situations requiring reauthentication.

<span style="color:#ff8c00;font-size:150%;">Medium Severity</span>

### Description

Without reauthenticating devices, unidentified or unknown devices may be introduced; thereby facilitating malicious activity.

In addition to the reauthentication requirements associated with session locks, organizations may require reauthentication of devices, including (but not limited to), the following other situations:

(i) When authenticators change;
(ii) When roles change;
(iii) When security categories of information systems change;
(iv) After a fixed period of time;
or
(v) Periodically.

For distributed architectures (e.g., service-oriented architectures), the decisions regarding the validation of identification claims may be made by services separate from the services acting on those decisions. In such situations, it is necessary to provide the identification decisions (as opposed to the actual identifiers) to the services that need to act on those decisions.

Gateways and SOA applications are examples of where this requirement would apply.

### Check Text

Review the application guidance and interview the application administrator.

Identify the methods and manner in which application devices such as an XML gateway, SOA application gateway, or application firewall is allowed to access the application. Most devices themselves will not change role or authenticators once they are established but will need to periodically reauthenticate.

Review the configuration setting in the application where the time period is set to force the device to reauthenticate.

Review local policy requirements to determine if reauthentication intervals are specified.

If the device is not forced to reauthenticate periodically, this is a finding.

**Check ID:**  C-24191r985973_chk

### Fix Text 

Configure the application to require reauthentication periodically.

**Fix ID:**  F-24180r493472_fix

**Vulnerability ID:**  V-222521

**Rule ID:**  SV-222521r985974_rule

---

## The application must uniquely identify and authenticate organizational users (or processes acting on behalf of organizational users).

<span style="color:#ff0000;font-size:150%;">High Severity</span>

### Description

To assure accountability and prevent unauthenticated access, organizational users must be identified and authenticated to prevent potential misuse and compromise of the system.

Organizational users include organizational employees or individuals the organization deems to have equivalent status of employees (e.g., contractors). 

Organizational users (and any processes acting on behalf of users) must be uniquely identified and authenticated for all accesses, except the following:

(i) Accesses explicitly identified and documented by the organization. Organizations document specific user actions that can be performed on the information system without identification or authentication; and 
(ii) Accesses that occur through authorized use of group authenticators without individual authentication. Organizations may require unique identification of individuals in group accounts (e.g., shared privilege accounts) or for detailed accountability of individual activity.

### Check Text

Review the application documentation and interview the application administrator to determine how organizational users access the application.

If the application is publicly available, providing access to publicly releasable data and the users are non-organizational users such as individuals who no longer have a CAC (e.g., retirees) or  members of the public with no requirement for DoD credentials, this requirement is not applicable.

The requirement still applies to DoD organizational users and admins when accessing the non-public data areas or system resources of the system.

Attempt to access the application and confirm that a unique user account and password or CAC token and pin are required in order to access the application.

If the application does not uniquely identify and authenticate users, this is a finding.

**Check ID:**  C-24192r493474_chk

### Fix Text 

Configure the application to uniquely identify and authenticate users and user processes.

**Fix ID:**  F-24181r493475_fix

**Vulnerability ID:**  V-222522

**Rule ID:**  SV-222522r1051115_rule

---

## The application must use multifactor (Alt. Token) authentication for network access to privileged accounts.

<span style="color:#ff8c00;font-size:150%;">Medium Severity</span>

### Description

Multifactor authentication requires using two or more factors to achieve authentication and access.

Factors include:
(i) something a user knows (e.g., password/PIN);
(ii) something a user has (e.g., cryptographic identification device, token); or
(iii) something a user is (e.g., biometric).

Multifactor authentication decreases the attack surface by virtue of the fact that attackers must obtain two factors, a physical token or a biometric and a PIN, in order to authenticate.  It is not enough to simply steal a user's password to obtain access.  

A privileged account is defined as an information system account with authorizations of a privileged user.  

An Alt. Token is a separate CAC like token used specifically for administrative account access and serves as a separate identifier much like a separate user account.

Network access is defined as access to an information system by a user (or a process acting on behalf of a user) communicating through a network (e.g., local area network, wide area network, or the Internet).

### Check Text

Review the application documentation and interview the application administrator to identify application access methods.

Ask the application administrator to present both their primary CAC and their Alt. Token.  Ask the application administrator to log on to the application using application relevant network based access methods.  Attempt to use both CAC and Alt. Tokens to authenticate to the application. 

Validate the application requests the user to input their CAC PIN and that they cannot perform administrative functions.

Have user logoff and reauthenticate with their Alt. Token and that they can perform administrative functions.

If the application allows administrative access to the application without requiring an Alt. Token, this is a finding.

**Check ID:**  C-24193r493477_chk

### Fix Text 

Configure the application to use an Alt. Token when providing network access to privileged application accounts.

**Fix ID:**  F-24182r493478_fix

**Vulnerability ID:**  V-222523

**Rule ID:**  SV-222523r960972_rule

---

## The application must accept Personal Identity Verification (PIV) credentials.

<span style="color:#ff8c00;font-size:150%;">Medium Severity</span>

### Description

The use of PIV credentials facilitates standardization and reduces the risk of unauthorized access.

DoD has mandated the use of the CAC to support identity management and personal authentication for systems covered under HSPD 12, as well as a primary component of layered protection for national security systems.

### Check Text

Review the application documentation and interview the application administrator to identify application access methods.

If the application is not PK-enabled due to the hosted data being publicly releasable, this check is not applicable.

Ask the application administrator to log on to the application. Have the application admin use their non-privileged credentials.

Validate the application prompts the user to provide a certificate from the CAC.

If the application allows access without requiring a CAC, this is a finding.

**Check ID:**  C-24194r493480_chk

### Fix Text 

Configure the application to require CAC authentication.

**Fix ID:**  F-24183r493481_fix

**Vulnerability ID:**  V-222524

**Rule ID:**  SV-222524r961494_rule

---

## The application must electronically verify Personal Identity Verification (PIV) credentials.

<span style="color:#ff8c00;font-size:150%;">Medium Severity</span>

### Description

The use of PIV credentials facilitates standardization and reduces the risk of unauthorized access.

DoD has mandated the use of the CAC to support identity management and personal authentication for systems covered under HSPD 12, as well as a primary component of layered protection for national security systems.

If the application does not verify the credentials provided, user authentication cannot be established which places the integrity and confidentiality of the application at risk.

### Check Text

Review the application documentation and interview the application administrator to identify application access methods.

If the application is not PK-enabled due to the hosted data being publicly releasable, this check is not applicable.

Ask the application administrator to log on to the application.

Validate the application prompts the user to provide a certificate from the CAC.

Validate the application requests the user to input their CAC PIN.

If the application allows access without requiring a CAC, this is a finding.

**Check ID:**  C-24195r493483_chk

### Fix Text 

Configure the application to require CAC authentication.

**Fix ID:**  F-24184r493484_fix

**Vulnerability ID:**  V-222525

**Rule ID:**  SV-222525r961497_rule

---

## The application must use multifactor (e.g., CAC, Alt. Token) authentication for network access to non-privileged accounts.

<span style="color:#ff8c00;font-size:150%;">Medium Severity</span>

### Description

To assure accountability and prevent unauthenticated access, non-privileged users must utilize multifactor authentication to prevent potential misuse and compromise of the system.

Multifactor authentication uses two or more factors to achieve authentication.

Factors include:

(i) Something you know (e.g., password/PIN);
(ii) Something you have (e.g., cryptographic identification device, CAC/SIPRNet token); or
(iii) Something you are (e.g., biometric).

A non-privileged account is any information system account with authorizations of a non-privileged user.

Network access is any access to an application by a user (or process acting on behalf of a user) where said access is obtained through a network connection.

Applications integrating with the DoD Active Directory and utilize the DoD CAC are an example of compliant multifactor authentication solutions.

### Check Text

Review the application documentation and interview the application administrator to identify application access methods.

If the application is not PK-enabled due to the hosted data being publicly releasable, this check is not applicable.

Ask the application administrator to log on to the application. Have the application admin use their non-privileged credentials.

Validate the application prompts the user to provide a certificate from the CAC.

Validate the application requests the user to input their CAC PIN. 

If the application allows access without requiring a CAC or Alt. Token, this is a finding.

**Check ID:**  C-24196r493486_chk

### Fix Text 

Configure the application to require CAC or Alt. Token authentication for non-privileged network access to non-privileged accounts.

**Fix ID:**  F-24185r493487_fix

**Vulnerability ID:**  V-222526

**Rule ID:**  SV-222526r960975_rule

---

## The application must use multifactor (Alt. Token) authentication for local access to privileged accounts.

<span style="color:#ff8c00;font-size:150%;">Medium Severity</span>

### Description

Multifactor authentication (MFA) requires using two or more factors to achieve authentication and access.

Factors include:
(i) something a user knows (e.g., password/PIN);
(ii) something a user has (e.g., cryptographic identification device, token); or
(iii) something a user is (e.g., biometric).

MFA decreases the attack surface by virtue of the fact that attackers must obtain two factors, a physical token or a biometric and a PIN, in order to authenticate. It is not enough to simply steal a user's password to obtain access. 

A privileged account is defined as an information system account with authorizations of a privileged user.

An Alt. Token is a separate CAC or token used specifically for administrative account access and serves as a separate identifier much like a separate user account.

Local access is defined as access to an organizational information system by a user (or process acting on behalf of a user) communicating through a direct connection without the use of a network.

### Check Text

Review the application documentation and interview the application administrator to identify application access methods.

Ask the application administrator to present both their primary CAC and their Alt. Token. Ask the application administrator to log on to the application using the local application console. 

Attempt to use both the CAC and Alt. Tokens to authenticate to the application.

Validate the application requests the user to input their CAC PIN and that they cannot perform administrative functions.

Have user log off and reauthenticate with their Alt. Token and verify they can perform administrative functions.

If the application allows administrative access to the application without requiring an Alt. Token, this is a finding.

**Check ID:**  C-24197r985925_chk

### Fix Text 

Configure the application to only use Alt. Tokens when locally accessing privileged application accounts.

**Fix ID:**  F-24186r493490_fix

**Vulnerability ID:**  V-222527

**Rule ID:**  SV-222527r1015693_rule

---

## The application must use multifactor (e.g., CAC, Alt. Token) authentication for local access to nonprivileged accounts.

<span style="color:#ff8c00;font-size:150%;">Medium Severity</span>

### Description

To assure accountability, prevent unauthenticated access, and prevent misuse of the system, privileged users must utilize multifactor authentication (MFA) for local access.

MFA is defined as using two or more factors to achieve authentication.

Factors include:
(i) Something a user knows (e.g., password/PIN);
(ii) Something a user has (e.g., cryptographic identification device, token); or
(iii) Something a user is (e.g., biometric).

A nonprivileged account is defined as an information system account with authorizations of a regular or nonprivileged user.

Local access is defined as access to an organizational information system by a user (or process acting on behalf of a user) communicating through a direct connection without the use of a network.

Applications integrating with the DOD Active Directory and utilize the DOD CAC are examples of compliant multifactor authentication solutions.

### Check Text

Review the application documentation and interview the application administrator to identify application access methods.

If the application is not PKI-enabled due to the hosted data being publicly releasable, this check is Not Applicable.

Ask the application administrator to log on to the application. Have the application admin use their nonprivileged credentials.

Validate the application prompts the user to provide a certificate from the CAC.

Validate the application requests the user to input their CAC PIN.

If the application allows access without requiring a CAC or Alt. Token, this is a finding.

**Check ID:**  C-24198r985927_chk

### Fix Text 

Configure the application to require CAC or Alt. Token authentication for nonprivileged network access.

**Fix ID:**  F-24187r985928_fix

**Vulnerability ID:**  V-222528

**Rule ID:**  SV-222528r1015694_rule

---

## The application must ensure users are authenticated with an individual authenticator prior to using a group authenticator.

<span style="color:#ff8c00;font-size:150%;">Medium Severity</span>

### Description

To ensure individual accountability and prevent unauthorized access, application users must be individually identified and authenticated. Individual accountability mandates that each user is uniquely identified.

A group authenticator is a shared account or some other form of authentication that allows multiple unique individuals to access the application using a single account.

If an application allows or provides for group authenticators, it must first individually authenticate users prior to implementing group authenticator functionality.

Some applications may not have the need to provide a group authenticator; this is considered a matter of application design. In those instances where the application design includes the use of a group authenticator, this requirement will apply.

There may also be instances when specific user actions need to be performed on the information system without unique user identification or authentication. An example of this type of access is a web server which contains publicly releasable information.

### Check Text

Review the application documentation, examine user accounts and group membership, and interview the application administrator to identify group or shared accounts. Document the group or shared account information.

If the application does not use group or shared accounts, this requirement is Not Applicable.

Create a test account or use an existing group member account.

Ensure the test account is not authenticated to the application and attempt to access the application with the group account credentials.

If the application allows access without first requiring the group member to authenticate with their individual credentials, this is a finding.

**Check ID:**  C-24199r985930_chk

### Fix Text 

Design and configure the application to individually authenticate group account members prior to allowing access.

**Fix ID:**  F-24188r493496_fix

**Vulnerability ID:**  V-222529

**Rule ID:**  SV-222529r1015695_rule

---

## The application must implement replay-resistant authentication mechanisms for network access to privileged accounts.

<span style="color:#ff8c00;font-size:150%;">Medium Severity</span>

### Description

A replay attack may enable an unauthorized user to gain access to the application. Authentication sessions between the authenticator and the application validating the user credentials must not be vulnerable to a replay attack.

An authentication process resists replay attacks if it is impractical to achieve a successful authentication by recording and replaying a previous authentication message.

A privileged account is any information system account with authorizations of a privileged user.

Techniques used to address this include protocols using nonces (e.g., numbers generated for a specific one time use) or challenges (e.g., TLS, WS_Security). Additional techniques include time-synchronous or challenge-response one-time authenticators.

### Check Text

Review application documentation and interview application administrator to identify what authentication mechanisms are used when accessing the application.

If the application is hosting publicly releasable information that does not require authentication, or if the application users are not eligible for a DoD CAC as per DoD 8520, this requirement is not applicable.

Review to ensure the application is utilizing TLSV1.2 or greater to protect communication and privileged user authentication traffic.

Verify the application utilizes a strong authentication mechanism such as Kerberos, IPSEC, or Secure Shell (SSH).

- Cryptographically sign web services packets.
- Time stamps and cryptographic hashes are used with web services packets.
- Use WS_Security for web services.

Request the most recent vulnerability scan results and configuration settings.

Verify the configuration is set to test for known replay vulnerabilities.

Request code review results (if available) and review for issues that have been identified as potential replay attack vulnerabilities.

Verify identified issues have been remediated.

If the application is not implementing replay-resistant authentication methods applicable to the application architecture, this is a finding.

**Check ID:**  C-36245r602300_chk

### Fix Text 

Design and configure the application to utilize replay-resistant mechanisms when authenticating privileged accounts.

**Fix ID:**  F-24189r493499_fix

**Vulnerability ID:**  V-222530

**Rule ID:**  SV-222530r960993_rule

---

## The application must implement replay-resistant authentication mechanisms for network access to nonprivileged accounts.

<span style="color:#ff8c00;font-size:150%;">Medium Severity</span>

### Description

A replay attack is a man-in-the-middle style attack which allows an attacker to repeat or alter a valid data transmission that may enable unauthorized access to the application. Authentication sessions between the authenticating client and the application server validating the user credentials must not be vulnerable to a replay attack.

The protection methods selected to protect against a replay attack will vary according to the application architecture.

An authentication process resists replay attacks if it is impractical to achieve a successful authentication by recording and replaying a previous authentication message.

A nonprivileged account is any operating system account with authorizations of a nonprivileged user.

Techniques used to address this include protocols using nonces (e.g., numbers generated for a specific one time use), challenges (e.g., TLS, WS_Security), and PKI certificates. Additional techniques include time-synchronous or challenge-response one-time authenticators.

### Check Text

Review the application documentation and interview the application administrator to identify what authentication mechanisms are used when accessing the application.

If the application is hosting publicly releasable information that does not require authentication, or if the application users are not eligible for a DOD CAC as per DOD 8520, this requirement is Not Applicable.

Review to ensure the application is utilizing TLSV1.2 or greater to protect communication and nonprivileged user authentication traffic.

Verify the application utilizes a strong authentication mechanism such as Kerberos, IPSEC, or Secure Shell (SSH).

- Cryptographically sign web services packets.
- Time stamps and cryptographic hashes are used with web services packets.
- Use WS_Security for web services.

Request the most recent vulnerability scan results and configuration settings.

Verify the configuration is set to test for known replay vulnerabilities.

Request code review results (if available) and review for issues that have been identified as potential replay attack vulnerabilities.

Verify identified issues have been remediated.

If the application is not implementing replay-resistant authentication methods applicable to the application architecture, this is a finding.

**Check ID:**  C-36246r985932_chk

### Fix Text 

Design and configure the application to utilize replay-resistant mechanisms when authenticating nonprivileged accounts.

**Fix ID:**  F-24190r985933_fix

**Vulnerability ID:**  V-222531

**Rule ID:**  SV-222531r1015696_rule

---

## The application must utilize mutual authentication when endpoint device non-repudiation protections are required by DoD policy or by the data owner.

<span style="color:#ff8c00;font-size:150%;">Medium Severity</span>

### Description

Without identifying devices, unidentified or unknown devices may be introduced, thereby facilitating malicious activity.

With one way SSL authentication which is the typical form of SSL authentication done between a web browser client and a web server, the client requests the server certificate to validate the server's identity and establish a secure connection.

When SSL mutual authentication is used, the server is configured to request the client’s certificate as well so the server can also identify the client.

For distributed architectures (e.g., service-oriented architectures), the decisions regarding the validation of identification claims may be made by services separate from the services acting on those decisions. In such situations, it is necessary to provide the identification decisions (as opposed to the actual identifiers) to the services that need to act on those decisions.

This requirement applies to applications that connect either locally, remotely, or through a network to an endpoint device (including but not limited to: workstations, printers, servers (outside a datacenter), VoIP Phones, VTC CODECs). Gateways and SOA applications are examples of where this requirement would apply.

### Check Text

Review the application documentation and interview the application administrator.

Determine if mutual authentication is mandated by the data owner or by mission data protection objectives and data type.

Review application architecture and design documents.

Identify endpoint devices that interact with the application. These can be SOA gateways, VOIP phones, or other devices that are used to connect to and exchange data with the application.

If the design documentation specifies, this could potentially also include remote client workstations.

In order for two way SSL/mutual authentication to work properly, the server must be configured to request client certificates.

Access the applications management console.

Navigate to the SSL management utility or web page that is used to configure two way mutual authentication.

Verify endpoints are configured for client authentication (mutual authentication).

Some application architectures such as Java configure their settings in text/xml formatted files; in that case, have the application administrator identify the configuration files used by the application.
E.g., web.xml stored in WEB-INF/ sub directory of the application root folder.

Open the web.xml file using a text editor.

Verify the application deployment descriptor for the application and the resource requiring protection under the "login-config" element is set to CLIENT-CERT.

If SSL mutual authentication is required and is not being utilized, this is a finding.

**Check ID:**  C-24202r493504_chk

### Fix Text 

Configure the application to utilize mutual authentication when specified by data protection requirements.

**Fix ID:**  F-24191r493505_fix

**Vulnerability ID:**  V-222532

**Rule ID:**  SV-222532r960999_rule

---

## The application must authenticate all network connected endpoint devices before establishing any connection.

<span style="color:#ff8c00;font-size:150%;">Medium Severity</span>

### Description

Without authenticating devices, unidentified or unknown devices may be introduced, thereby facilitating malicious activity.

For distributed architectures (e.g., service-oriented architectures), the decisions regarding the validation of authentication claims may be made by services separate from the services acting on those decisions.

In such situations, it is necessary to provide authentication decisions (as opposed to the actual authenticators) to the services that need to act on those decisions.

This requirement applies to applications that connect either locally, remotely, or through a network to an endpoint device (including but not limited to: workstations, printers, servers (outside a datacenter), VoIP Phones, VTC CODECs).

Gateways and SOA applications are examples of where this requirement would apply.

End point devices are not:
Client desktop workstations only offer browser-based web application access where the user authenticates at the app layer.

Device authentication is a solution enabling an organization to manage devices. It is an additional layer of authentication ensuring only specific pre-authorized devices can access the system.

### Check Text

Review the application documentation, implementation documentation and interview the application administrator.

Identify if the application utilizes Web Services/Service-Oriented Architecture (SOA). Using the web services framework that has been implemented, have the application administrator identify the remote devices allowed to communicate to the service provider.

If the application is designed to provide end-user, interactive application access only and does not use web services or allow connections from remote devices, this requirement is not applicable.

Identify the authentication mechanism used to authenticate the remote consumers/devices. Commonly available authentication methods are Client Certificate Authentication and Basic Authentication.

The Basic Authentication method provides insufficient protection for authentication sessions and is not allowed.

If no authentication mechanism is used to authenticate remote service consumers/devices, or if Basic Authentication is used to authentication remote service consumers/devices, this is a finding.

**Check ID:**  C-24203r493507_chk

### Fix Text 

Configure the application to authenticate all network connected endpoint devices/service consumers before establishing connections.

**Fix ID:**  F-24192r493508_fix

**Vulnerability ID:**  V-222533

**Rule ID:**  SV-222533r961503_rule

---

## Service-Oriented Applications handling non-releasable data must authenticate endpoint devices via mutual SSL/TLS.

<span style="color:#ff8c00;font-size:150%;">Medium Severity</span>

### Description

Without identifying devices, unidentified or unknown devices may be introduced, thereby facilitating malicious activity.

One way SSL/TLS authentication is the typical form of  authentication done between a web browser client and a web server. The client requests the server certificate to validate the server's identity and establish a secure connection.

When SSL/TLS mutual authentication is used, the server is configured to request the client’s certificate as well so the server can also identify the client. This form of authentication is normally chosen for system to system communications that leverage HTTP as the transport.

It should be noted that SSL is being deprecated and replaced with TLS.

For distributed architectures (e.g., service-oriented architectures), the decisions regarding the validation of identification claims may be made by services separate from the services acting on those decisions. In such situations, it is necessary to provide the identification decisions (as opposed to the actual identifiers) to the services that need to act on those decisions.

This requirement applies to applications that connect either locally, remotely, or through a network to an endpoint device (including but not limited to: workstations, printers, servers (outside a datacenter), VoIP Phones, VTC CODECs). Gateways and SOA applications are examples of where this requirement would apply.

### Check Text

Review application documentation and interview application administrator.

Identify application data elements and determine if the application is handling/processing non-releasable data.

Review the application architecture and design documents.

Identify endpoint devices that interact with the application. These can be SOA gateways, VOIP phones, or other devices that are used to connect to and exchange data with the application.

If the design documentation specifies it, this could also include remote client workstations. However, this requirement is usually reserved for system-oriented endpoints rather than client workstations.

In order for two way SSL/TLS mutual authentication to work properly, the server must be configured to request client certificates.

Access the applications management console and navigate to the SSL/TLS management utility or web page that is used to configure two-way mutual authentication.

Verify endpoints are configured for client authentication (mutual authentication).

Some application architectures configure their settings in text/xml formatted files; in that case, have the application administrator identify the configuration files used by the application (e.g., web.xml stored in WEB-INF/ sub directory of the application root folder).

Open the web.xml file using a text editor and verify the application deployment descriptor for the application and the resource requiring protection under the "login-config" element is set to CLIENT-CERT.

If SSL/TLS mutual authentication is required due to the application processing non-releasable data and SSL/TLS mutual authentication not being utilized, this is a finding.

**Check ID:**  C-24204r493510_chk

### Fix Text 

Configure the application to utilize mutual authentication when the application is processing non-releasable data.

**Fix ID:**  F-24193r493511_fix

**Vulnerability ID:**  V-222534

**Rule ID:**  SV-222534r961506_rule

---

## The application must disable device identifiers after 35 days of inactivity unless a cryptographic certificate is used for authentication.

<span style="color:#ff8c00;font-size:150%;">Medium Severity</span>

### Description

Device identifiers are used to identify hardware devices that interact with the application much like a user account is used to identify an application user. Examples of hardware devices include but are not limited to mobile phones, application gateways, or other types of smart hardware.

This requirement does not apply to individual application user accounts.

This requirement is not applicable to shared information system accounts, application groups, or roles (e.g., guest and anonymous accounts) that are used by the application itself in order to function. Care must be taken to not disable identifiers that are used by the application in order to function.

Inactive device identifiers pose a risk to systems and applications. Attackers that are able to exploit an inactive identifier can potentially obtain and maintain undetected access to the application.

Applications need to track periods of device inactivity and disable the device identifier after 35 days of inactivity. This is usually accomplished by disabling the account used by the device to access the application.

Applications that use cryptographic certificates for device authentication may use the expiration date assigned to the certificate to meet this requirement with the understanding that the certificate is created and managed in accordance with DOD PKI policy and can be revoked by a trusted certificate authority (CA).

To avoid having to build complex device management capabilities directly into their application, developers should leverage the underlying OS or other account management infrastructure (AD, LDAP) that is already in place within the organization and meets organizational user account management requirements.

Applications are encouraged to utilize a centralized data store such as Active Directory or LDAP to offload device management requirements and ensure compliance with policy requirements.

### Check Text

Review the application documentation and interview the application administrator.

If the application is not designed to authenticate devices (such as mobile phones, gateways or other smart devices), or uses DOD PKI certificates to authenticate these devices, this requirement is Not Applicable.

Access the user management interface for the application.

Identify application device IDs.

If the application utilizes approved certificates or a centralized authentication store (Active Directory or LDAP) as the authoritative source for application authentication, and the authentication store is configured to meet the requirement to disable device IDs after 35 days of inactivity, this is not a finding.

Accounts such as guest and anonymous as well as roles and groups or other identities used to operate the application or to provide limited guest access are not applicable.

Access the application user management interface and review the account settings that pertain to devices.

Verify the application is configured to disable device accounts that have not been active or logged into the application for the past 35 days.

If the application does not disable accounts used to authenticate devices after 35 days of inactivity, this is a finding.

**Check ID:**  C-24205r985935_chk

### Fix Text 

Configure the application to disable device accounts after 35 days of inactivity or to utilize DOD PKI certificates that provide an expiration date.

**Fix ID:**  F-24194r985936_fix

**Vulnerability ID:**  V-222535

**Rule ID:**  SV-222535r1015697_rule

---

## The application must enforce a minimum 15-character password length.

<span style="color:#ff0000;font-size:150%;">High Severity</span>

### Description

The shorter the password, the lower the number of possible combinations that need to be tested before the password is compromised.

Use of passwords for application authentication is intended only for limited situations and should not be used as a replacement for two-factor CAC-enabled authentication.

Examples of situations where a user ID and password might be used include but are not limited to:

- When the application user base does not have a CAC and is not a current DOD employee, member of the military, or a DOD contractor.
- When an application user has been officially designated as a Temporary Exception User; one who is temporarily unable to present a CAC for some reason (lost, damaged, not yet issued, broken card reader) and to satisfy urgent organizational needs must be temporarily permitted to use user ID/password authentication until the problem with CAC use has been remedied.
- When the application is publicly available and or hosting publicly releasable data requiring some degree of need-to-know protection.

Password complexity, or strength, is a measure of the effectiveness of a password in resisting attempts at guessing and brute-force attacks. Password length is one factor of several that helps to determine strength and how long it takes to crack a password. The shorter the password, the lower the number of possible combinations that need to be tested before the password is compromised.

Use of more characters in a password helps to exponentially increase the time and/or resources required to compromise the password.

### Check Text

Review the application documentation and interview the application administrator to identify if the application uses passwords for user authentication.

If the application does not use passwords, this requirement is Not Applicable.

Access the application management interface and create a test user account or log on to the system with a test account and access the functionality that provides password change capabilities.

When prompted to provide the password, attempt to create a password shorter than 15 characters in length.

If a password shorter than 15 characters can be created, this is a finding.

**Check ID:**  C-24206r985938_chk

### Fix Text 

Configure the application to require 15 characters in the password.

**Fix ID:**  F-24195r493517_fix

**Vulnerability ID:**  V-222536

**Rule ID:**  SV-222536r1015698_rule

---

## The application must enforce password complexity by requiring that at least one uppercase character be used.

<span style="color:#ff8c00;font-size:150%;">Medium Severity</span>

### Description

Use of passwords for application authentication is intended only for limited situations and should not be used as a replacement for two-factor CAC-enabled authentication.

Examples of situations where a user ID and password might be used include but are not limited to:

- When the application user base does not have a CAC and is not a current DOD employee, member of the military, or a DOD contractor.
- When an application user has been officially designated as a Temporary Exception User; one who is temporarily unable to present a CAC for some reason (lost, damaged, not yet issued, broken card reader) and to satisfy urgent organizational needs must be temporarily permitted to use user ID/password authentication until the problem with CAC use has been remedied.
- When the application is publicly available and or hosting publicly releasable data requiring some degree of need-to-know protection.

Use of a complex password helps to increase the time and resources required to compromise the password. Password complexity, or strength, is a measure of the effectiveness of a password in resisting attempts at guessing and brute-force attacks.

Password complexity is one factor of several that determine how long it takes to crack a password. The more complex the password is, the greater the number of possible combinations that need to be tested before the password is compromised.

### Check Text

Review the application documentation and interview the application administrator to identify if the application uses passwords for user authentication.

If the application does not use passwords, this requirement is Not Applicable.

Access the application management interface and create a test user account or logon to the system with a test account and access the functionality that provides password change capabilities.

When prompted to provide the password, attempt to create a password that does not have one uppercase character.

If a password without at least one upper-case character can be created, this is a finding.

**Check ID:**  C-24207r985940_chk

### Fix Text 

Configure the application to require at least one uppercase character in the password.

**Fix ID:**  F-24196r985941_fix

**Vulnerability ID:**  V-222537

**Rule ID:**  SV-222537r1015699_rule

---

## The application must enforce password complexity by requiring that at least one lowercase character be used.

<span style="color:#ff8c00;font-size:150%;">Medium Severity</span>

### Description

Use of passwords for application authentication is intended only for limited situations and should not be used as a replacement for two-factor CAC-enabled authentication.

Examples of situations where a user ID and password might be used include but are not limited to:

- When the application user base does not have a CAC and is not a current DOD employee, member of the military, or a DOD contractor.
- When an application user has been officially designated as a Temporary Exception User; one who is temporarily unable to present a CAC for some reason (lost, damaged, not yet issued, broken card reader) and to satisfy urgent organizational needs must be temporarily permitted to use user ID/password authentication until the problem with CAC use has been remedied.
- When the application is publicly available and or hosting publicly releasable data requiring some degree of need-to-know protection.

Use of a complex password helps to increase the time and resources required to compromise the password. Password complexity, or strength, is a measure of the effectiveness of a password in resisting attempts at guessing and brute-force attacks.

Password complexity is one factor of several that determine how long it takes to crack a password. The more complex the password, the greater the number of possible combinations that need to be tested before the password is compromised.

### Check Text

Review the application documentation and interview the application administrator to identify if the application uses passwords for user authentication.

If the application does not use passwords, this requirement is Not Applicable.

Access the application management interface and create a test user account or logon to the system with a test account and access the functionality that provides password change capabilities.

When prompted to provide the password, attempt to create a password that does not have one lowercase character.

If a password without at least one lower-case character can be created, this is a finding.

**Check ID:**  C-24208r985943_chk

### Fix Text 

Configure the application to require at least one lowercase character in the password.

**Fix ID:**  F-24197r985944_fix

**Vulnerability ID:**  V-222538

**Rule ID:**  SV-222538r1015700_rule

---

## The application must enforce password complexity by requiring that at least one numeric character be used.

<span style="color:#ff8c00;font-size:150%;">Medium Severity</span>

### Description

Use of passwords for application authentication is intended only for limited situations and should not be used as a replacement for two-factor CAC-enabled authentication.

Examples of situations where a user ID and password might be used include but are not limited to:

- When the application user base does not have a CAC and is not a current DOD employee, member of the military, or a DOD contractor.
- When an application user has been officially designated as a Temporary Exception User; one who is temporarily unable to present a CAC for some reason (lost, damaged, not yet issued, broken card reader) and to satisfy urgent organizational needs must be temporarily permitted to use user ID/password authentication until the problem with CAC use has been remedied.
- When the application is publicly available and or hosting publicly releasable data requiring some degree of need-to-know protection.

Use of a complex password helps to increase the time and resources required to compromise the password. Password complexity, or strength, is a measure of the effectiveness of a password in resisting attempts at guessing and brute-force attacks.

Password complexity is one factor of several that determine how long it takes to crack a password. The more complex the password, the greater the number of possible combinations that need to be tested before the password is compromised.

### Check Text

Review the application documentation and interview the application administrator to identify if the application uses passwords for user authentication.

If the application does not use passwords, this requirement is Not Applicable.

Access the application management interface and create a test user account or logon to the system with a test account and access the functionality that provides password change capabilities.

When prompted to provide the password, attempt to create a password that does not have one numeric character.

If a password without at least one numeric character can be created, this is a finding.

**Check ID:**  C-24209r985946_chk

### Fix Text 

Configure the application to require at least one numeric character in the password.

**Fix ID:**  F-24198r493526_fix

**Vulnerability ID:**  V-222539

**Rule ID:**  SV-222539r1015701_rule

---

## The application must enforce password complexity by requiring that at least one special character be used.

<span style="color:#ff8c00;font-size:150%;">Medium Severity</span>

### Description

Use of passwords for application authentication is intended only for limited situations and should not be used as a replacement for two-factor CAC-enabled authentication.

Examples of situations where a user ID and password might be used include but are not limited to:

- When the application user base does not have a CAC and is not a current DOD employee, member of the military, or a DOD contractor.
- When an application user has been officially designated as a Temporary Exception User; one who is temporarily unable to present a CAC for some reason (lost, damaged, not yet issued, broken card reader) and to satisfy urgent organizational needs must be temporarily permitted to use user ID/password authentication until the problem with CAC use has been remedied.
- When the application is publicly available and or hosting publicly releasable data requiring some degree of need-to-know protection.

Use of a complex password helps to increase the time and resources required to compromise the password. Password complexity, or strength, is a measure of the effectiveness of a password in resisting attempts at guessing and brute-force attacks.

Password complexity is one factor of several that determine how long it takes to crack a password. The more complex the password, the greater the number of possible combinations that need to be tested before the password is compromised.

### Check Text

Review the application documentation and interview the application administrator to identify if the application uses passwords for user authentication.

If the application does not use passwords, this requirement is Not Applicable.

Access the application management interface and create a test user account or logon to the system with a test account and access the functionality that provides password change capabilities.

When prompted to provide the password, attempt to create a password that does not have one special character.

If a password without at least one special character can be created, this is a finding.

**Check ID:**  C-24210r985948_chk

### Fix Text 

Configure the application to require at least one special character in the password.

**Fix ID:**  F-24199r493529_fix

**Vulnerability ID:**  V-222540

**Rule ID:**  SV-222540r1015702_rule

---

## The application must require the change of at least eight of the total number of characters when passwords are changed.

<span style="color:#ff8c00;font-size:150%;">Medium Severity</span>

### Description

Use of passwords for application authentication is intended only for limited situations and should not be used as a replacement for two-factor CAC-enabled authentication.

Examples of situations where a user ID and password might be used include but are not limited to:

- When the application user base does not have a CAC and is not a current DOD employee, member of the military, or a DOD contractor.
- When an application user has been officially designated as a Temporary Exception User; one who is temporarily unable to present a CAC for some reason (lost, damaged, not yet issued, broken card reader) and to satisfy urgent organizational needs must be temporarily permitted to use user ID/password authentication until the problem with CAC use has been remedied.
- When the application is publicly available and or hosting publicly releasable data requiring some degree of need-to-know protection.

Use of a complex password helps to increase the time and resources required to compromise the password. Password complexity, or strength, is a measure of the effectiveness of a password in resisting attempts at guessing and brute-force attacks.

Password complexity is one factor of several that determine how long it takes to crack a password. The more complex the password, the greater the number of possible combinations that need to be tested before the password is compromised.

### Check Text

Review the application documentation and interview the application administrator to identify if the application uses passwords for user authentication.

If the application does not use passwords, this requirement is Not Applicable.

Access the application management interface and create a test user account or logon to the system with a test account and access the functionality that provides password change capabilities.

When prompted to provide the password, attempt to change less than 8 characters of the total number of characters in the password.

If less than 8 characters of the password are changed, this is a finding.

**Check ID:**  C-24211r985950_chk

### Fix Text 

Configure the application to require the change of at least eight characters in the password when passwords are changed.

**Fix ID:**  F-24200r985951_fix

**Vulnerability ID:**  V-222541

**Rule ID:**  SV-222541r1043189_rule

---

## The application must only store cryptographic representations of passwords.

<span style="color:#ff0000;font-size:150%;">High Severity</span>

### Description

Use of passwords for application authentication is intended only for limited situations and should not be used as a replacement for two-factor CAC-enabled authentication.

Examples of situations where a user ID and password might be used include but are not limited to:

- When the application user base does not have a CAC and is not a current DOD employee, member of the military, or a DOD contractor.
- When an application user has been officially designated as a Temporary Exception User; one who is temporarily unable to present a CAC for some reason (lost, damaged, not yet issued, broken card reader) and to satisfy urgent organizational needs must be temporarily permitted to use user ID/password authentication until the problem with CAC use has been remedied.
- When the application is publicly available and or hosting publicly releasable data requiring some degree of need-to-know protection.

Passwords need to be protected at all times and using a strong one-way hashing encryption algorithm with a salt is the standard method for providing a means to validate a user's password without having to store the actual password. 

Performance and time required to access are factors that must be considered and the one way hash is the most feasible means of securing the password and providing an acceptable measure of password security. If passwords are stored in clear text, they can be plainly read and easily compromised.

In many instances, verifying the user knows a password is performed using a password verifier. In its simplest form, a password verifier is a computational function that is capable of creating a hash of a password and determining if the value provided by the user matches the hash. 

A more secure version of verifying a user knowing a password is to store the result of an iterating hash function and a large random SALT value as follows:

H0 = H(pwd, H(salt))
Hn = H(Hn-1,H(salt))

Where n is a cryptographically-strong random [*3] number. Hn is stored, along with the salt. When the application wishes to verify that the user knows a password, it simply repeats the process and compares Hn with the stored Hn.

A SALT is essentially a fixed-length cryptographically-strong random value. 

Another method used is utilizing a keyed hash message authentication code (HMAC). HMAC calculates a message authentication code via a cryptographic hash function used in conjunction with an encryption key. The key must be protected as with any private key.
 
Applications must only store passwords that have been cryptographically protected.

### Check Text

Review the application documentation and interview the application administrator to identify if the application uses passwords for user authentication.

If the application does not use passwords, this requirement is Not Applicable.

Have the application administrator identify the application's password storage locations. Potential locations include the local file system where the application is stored or in an application-related database table that should not be accessible to application users.

Review application files and folders using a text editor or by using a database tool that allows you to view data stored in database tables. Look for indications of stored user information and review that information. Determine if password strings are readable/discernable.

Determine if the application uses the MD5 hashing algorithm to create password hashes.

If the passwords are readable or there is no indication the application utilizes cryptographic hashing to protect passwords, or if the MD5 hash algorithm is used to create password hashes, this is a finding.

**Check ID:**  C-24212r985953_chk

### Fix Text 

Use strong cryptographic hash functions when creating password hash values.

Utilize random salt values when creating the password hash.

Ensure strong access control permissions on data files containing authentication data.

**Fix ID:**  F-24201r493535_fix

**Vulnerability ID:**  V-222542

**Rule ID:**  SV-222542r1015704_rule

---

## The application must transmit only cryptographically-protected passwords.

<span style="color:#ff0000;font-size:150%;">High Severity</span>

### Description

Use of passwords for application authentication is intended only for limited situations and should not be used as a replacement for two-factor CAC-enabled authentication.

Examples of situations where a user ID and password might be used include but are not limited to:

- When the application user base does not have a CAC and is not a current DoD employee, member of the military, or a DoD contractor.

- When an application user has been officially designated as a Temporary Exception User; one who is temporarily unable to present a CAC for some reason (lost, damaged, not yet issued, broken card reader) and to satisfy urgent organizational needs must be temporarily permitted to use user ID/password authentication until the problem with CAC use has been remedied.

and

- When the application is publicly available and or hosting publicly releasable data requiring some degree of need-to-know protection.

Passwords need to be protected at all times and encryption is the standard method for protecting passwords. If passwords are not encrypted, they can be plainly read (i.e., clear text) and easily compromised.

Applications can accomplish this by making direct function calls to encryption modules or by leveraging operating system encryption capabilities.

### Check Text

Review the application documentation and interview the application administrator to identify if the application uses passwords for user authentication.

If the application does not use passwords, the requirement is not applicable.

Identify when the application transmits passwords. This will most likely be when the user authenticates to the application or when the application authenticates to another resource.

Access the application management interface with a test account and access the functionality that requires a password be provided. If the interface is via a web browser, verify the web browser has gone secure prior to entering any password or authentication information.

This can be done by viewing the browser and observing a “lock” icon displayed somewhere in the browser as well as an https:// to indicate an SSL connection. Most browsers display this in the upper left hand corner.

If the application is transmitting the password rather than the user, obtain design documentation from the application admin that provides the details on how they are protecting the password during transmission. This will usually be via a TLS/SSL tunneled connection or VPN.

If the passwords are not encrypted when being transmitted, this is a finding.

**Check ID:**  C-24213r493537_chk

### Fix Text 

Configure the application to encrypt passwords when they are being transmitted.

**Fix ID:**  F-24202r493538_fix

**Vulnerability ID:**  V-222543

**Rule ID:**  SV-222543r961029_rule

---

## The application must enforce 24 hours/1 day as the minimum password lifetime.

<span style="color:#ff8c00;font-size:150%;">Medium Severity</span>

### Description

Use of passwords for application authentication is intended only for limited situations and should not be used as a replacement for two-factor CAC-enabled authentication.

Examples of situations where a user ID and password might be used include but are not limited to:

- When the application user base does not have a CAC and is not a current DOD employee, member of the military, or a DOD contractor.
- When an application user has been officially designated as a Temporary Exception User; one who is temporarily unable to present a CAC for some reason (lost, damaged, not yet issued, broken card reader) and to satisfy urgent organizational needs must be temporarily permitted to use user ID/password authentication until the problem with CAC use has been remedied.
- When the application is publicly available and or hosting publicly releasable data requiring some degree of need-to-know protection.

Enforcing a minimum password lifetime helps prevent repeated password changes to defeat the password reuse or history enforcement requirement.

Restricting this setting limits the user's ability to change their password. Passwords need to be changed at specific policy-based intervals; however, if the application allows the user to immediately and continually change their password, then the password could be repeatedly changed in a short period of time to defeat the organization's policy regarding password reuse.

### Check Text

Review the application documentation and interview the application administrator to identify if the application uses passwords for user authentication.

If the application does not use passwords, this requirement is Not Applicable.

Access the application management interface and create a test user account or logon to the system with a test account and access the functionality that provides password change capabilities.

Attempt to change the password more than once.

If a password can be changed more than once within 24 hours, the minimum lifetime setting is not set and this is a finding.

**Check ID:**  C-24214r985955_chk

### Fix Text 

Configure the application to have a minimum password lifetime of 24 hours.

**Fix ID:**  F-24203r493541_fix

**Vulnerability ID:**  V-222544

**Rule ID:**  SV-222544r1015705_rule

---

## The application must enforce a 60-day maximum password lifetime restriction.

<span style="color:#ff8c00;font-size:150%;">Medium Severity</span>

### Description

Use of passwords for application authentication is intended only for limited situations and should not be used as a replacement for two-factor CAC-enabled authentication.

Examples of situations where a user ID and password might be used include but are not limited to:

- When the application user base does not have a CAC and is not a current DOD employee, member of the military, or a DOD contractor.
- When an application user has been officially designated as a Temporary Exception User; one who is temporarily unable to present a CAC for some reason (lost, damaged, not yet issued, broken card reader) and to satisfy urgent organizational needs must be temporarily permitted to use user ID/password authentication until the problem with CAC use has been remedied.
- When the application is publicly available and or hosting publicly releasable data requiring some degree of need-to-know protection.

Any password, no matter how complex, can eventually be cracked. Therefore, passwords need to be changed at specific intervals.

One method of minimizing this risk is to use complex passwords and periodically change them. If the application does not limit the lifetime of passwords and force users to change their passwords, there is the risk that the system and/or application passwords could be compromised.

This requirement does not include emergency administration accounts which are meant for access to the application in case of failure. These accounts are not required to have maximum password lifetime restrictions.

### Check Text

Review the application documentation and interview the application administrator to identify if the application uses passwords for user authentication.

If the application does not use passwords, this requirement is Not Applicable.

Access the application management interface and view the user password settings page.

Review user password settings and validate the application is configured to expire and force a password change after 60 days.

If user passwords are not configured to expire after 60 days, or if the application does not have the ability to control this setting, this is a finding.

**Check ID:**  C-24215r985957_chk

### Fix Text 

Configure the application to have a maximum password lifetime of 60 days.

**Fix ID:**  F-24204r493544_fix

**Vulnerability ID:**  V-222545

**Rule ID:**  SV-222545r1043190_rule

---

## The application must prohibit password reuse for a minimum of five generations.

<span style="color:#ff8c00;font-size:150%;">Medium Severity</span>

### Description

Use of passwords for application authentication is intended only for limited situations and should not be used as a replacement for two-factor CAC-enabled authentication.

Examples of situations where a user ID and password might be used include but are not limited to:

- When the application user base does not have a CAC and is not a current DOD employee, member of the military, or a DOD contractor.
- When an application user has been officially designated as a Temporary Exception User; one who is temporarily unable to present a CAC for some reason (lost, damaged, not yet issued, broken card reader) and to satisfy urgent organizational needs must be temporarily permitted to use user ID/password authentication until the problem with CAC use has been remedied.
- When the application is publicly available and or hosting publicly releasable data requiring some degree of need-to-know protection.

Password complexity, or strength, is a measure of the effectiveness of a password in resisting attempts at guessing and brute-force attacks.

To meet password policy requirements, passwords need to be changed at specific policy-based intervals.

If the information system or application allows the user to consecutively reuse their password when that password has exceeded its defined lifetime, the end result is a password that is not changed as per policy requirements.

### Check Text

Review the application documentation and interview the application administrator to identify if the application uses passwords for user authentication.

If the application does not use passwords, this requirement is Not Applicable.

Access the application management interface and view the user password settings page.

Review user password settings and validate the application is configured to prohibit password reuse for a minimum of five password generations.

If the application does not prevent users from reusing their previous five passwords, or if the application does not have the ability to control this setting, this is a finding.

**Check ID:**  C-24216r985959_chk

### Fix Text 

Configure the application to prohibit password reuse for up to five passwords.

**Fix ID:**  F-24205r985960_fix

**Vulnerability ID:**  V-222546

**Rule ID:**  SV-222546r1015267_rule

---

## The application must allow the use of a temporary password for system logons with an immediate change to a permanent password.

<span style="color:#ff8c00;font-size:150%;">Medium Severity</span>

### Description

Use of passwords for application authentication is intended only for limited situations and should not be used as a replacement for two-factor CAC-enabled authentication.

Examples of situations where a user ID and password might be used include but are not limited to:

- When the application user base does not have a CAC and is not a current DOD employee, member of the military, or a DOD contractor.
- When an application user has been officially designated as a Temporary Exception User; one who is temporarily unable to present a CAC for some reason (lost, damaged, not yet issued, broken card reader) and to satisfy urgent organizational needs must be temporarily permitted to use user ID/password authentication until the problem with CAC use has been remedied.
- When the application is publicly available and or hosting publicly releasable data requiring some degree of need-to-know protection.

Without providing this capability, an account may be created without a password. Nonrepudiation cannot be guaranteed once an account is created if a user is not forced to change the temporary password upon initial logon.

Temporary passwords are typically used to allow access to applications when new accounts are created or passwords are changed. It is common practice for administrators to create temporary passwords for user accounts which allow the users to log on, yet force them to change the password once they have successfully authenticated.

### Check Text

Review the application documentation and interview the application administrator to identify if the application uses passwords for user authentication.

If the application does not use passwords, this requirement is Not Applicable.

Access the application management interface and view the user password settings page.

Review user password settings and validate the application is configured to specify when a password is temporary and force a password change when the administrator either creates a new user account or changes a user’s password.

If the application can not specify a password as temporary and force the user to change the temporary password upon successful authentication, this is a finding.

**Check ID:**  C-24217r985975_chk

### Fix Text 

Configure the application to specify when a password is temporary and change the temporary password on the first use.

**Fix ID:**  F-24206r493550_fix

**Vulnerability ID:**  V-222547

**Rule ID:**  SV-222547r985976_rule

---

## The application password must not be changeable by users other than the administrator or the user with which the password is associated.

<span style="color:#ff8c00;font-size:150%;">Medium Severity</span>

### Description

If the application allows user A to change user B's password,  user B can be locked out of the application, and user A is provided the ability to grant themselves access to the application as user B.  This violates application integrity and availability principles.

Many applications provide a password reset capability that allows the user to reset their password if they forget it.

Protections must be utilized when establishing a password change or reset capability to prevent user A from changing user B's password.

Protection is usually accomplished by having each user provide an out of bounds (OOB) communication address such as a separate email address or SMS/text address (mobile phone) that can be used to transmit password reset/change information.

This  OOB information is usually provided by the user when the user account is created.   The OOB information is validated as part of the user account creation process by sending an account validation request to the OOB address and having the user respond to the request.

Applications must prevent users other than the administrator or the user associated with the account from changing the account password.

### Check Text

Review the application documentation and interview application administrator.

Determine if the application utilizes passwords. If the application does not utilize passwords, the requirement is NA.

Identify the processes, commands or web pages the application uses to allow application users to change their own passwords. This includes but is not limited to password resets.

If the application does not allow users to change or reset their passwords, the requirement is NA.

Obtain two application test accounts, referred to here as User A and User B. Access the application as User A. Utilize the application password reset or change processes and determine if User A is allowed to specify or otherwise force a password change for User B.

If User A is allowed to change or force a reset of User B's password, this is a finding.

**Check ID:**  C-36247r602304_chk

### Fix Text 

Use a CAC to authenticate users instead of using passwords. If application users are prohibited or prevented from obtaining a CAC due to DoD policy requirements and passwords are the only viable option, design the application to utilize a secure password change or password reset process.

Utilize out of band (OOB) communication techniques to communicate password change requests to users.

Ensure verification processes exist that allow users to validate the change request prior to implementing the password change.

Ensure users are only allowed to change their own passwords.

**Fix ID:**  F-36211r865212_fix

**Vulnerability ID:**  V-222548

**Rule ID:**  SV-222548r961863_rule

---

## The application must terminate existing user sessions upon account deletion.

<span style="color:#ff8c00;font-size:150%;">Medium Severity</span>

### Description

The application must ensure that a user does not retain any rights that may have been granted or retain access to the application after the user's authorization or role within the application has been deleted or modified.  This means once a user's role/account within the application has been modified, deleted or disabled, the changes must be enforced immediately within the application.  Any privileges or access the user had prior to the change must not be retained.  For example; any application sessions that the user may have already established prior to the configuration change must be terminated when the user account changes occur.

Simply removing a user from a web application without terminating any existing application user sessions can introduce a scenario where the deleted user still has access to the application even though their account has been deleted from the authentication store. This can be attributed to browser caching and session management on the web server.

To address this, the web application must provide a means for ensuring this type of "zombie" access does not occur. Applications must provide a user management feature or function that will terminate any existing user sessions at the same time or just before the user account is terminated from the authoritative authentication source.

### Check Text

Review the application documentation and interview the application administrator.

Identify the user management functions of the application and create a test user account.

Access the application and perform application functions as the test user.

Access the user management functions and delete the test account while the test user sessions are still active.

Verify the test user application sessions are terminated by attempting to perform additional application functions.

If the test user retains access after the test account has been deleted, this is a finding.

**Check ID:**  C-24219r493555_chk

### Fix Text 

Configure the application to terminate existing sessions of users whose accounts are deleted.

**Fix ID:**  F-24208r493556_fix

**Vulnerability ID:**  V-222549

**Rule ID:**  SV-222549r961521_rule

---

## The application, when utilizing PKI-based authentication, must validate certificates by constructing a certification path (which includes status information) to an accepted trust anchor.

<span style="color:#ff0000;font-size:150%;">High Severity</span>

### Description

Without path validation, an informed trust decision by the relying party cannot be made when presented with any certificate not already explicitly trusted.

A trust anchor is an authoritative entity represented via a public key and associated data. It is used in the context of public key infrastructures, X.509 digital certificates, and DNSSEC.

When there is a chain of trust, usually the top entity to be trusted becomes the trust anchor; it can be, for example, a Certification Authority (CA). A certification path starts with the subject certificate and proceeds through a number of intermediate certificates up to a trusted root certificate, typically issued by a trusted CA.

This requirement verifies that a certification path to an accepted trust anchor is used for certificate validation and that the path includes status information. Path validation is necessary for a relying party to make an informed trust decision when presented with any certificate not already explicitly trusted. Status information for certification paths includes certificate revocation lists or online certificate status protocol responses. Validation of the certificate status information is out of scope for this requirement.

### Check Text

Review the application documentation, the application architecture and interview the application administrator to identify the method employed by the application for validating certificates.

Review the method to determine if a certification path that includes status information is constructed when certificate validation occurs.

Some applications may utilize underlying OS certificate validation and certificate path building capabilities while others may build the capability into the application itself.

The certification path will include the intermediary certificate CAs along with a status of the CA server's signing certificate and will end at the trusted root anchor.

If the application does not construct a certificate path to an accepted trust anchor, this is a finding.

**Check ID:**  C-24220r493558_chk

### Fix Text 

Design the application to construct a certification path to an accepted trust anchor when using PKI-based authentication.

**Fix ID:**  F-24209r493559_fix

**Vulnerability ID:**  V-222550

**Rule ID:**  SV-222550r961038_rule

---

## The application, when using PKI-based authentication, must enforce authorized access to the corresponding private key.

<span style="color:#ff0000;font-size:150%;">High Severity</span>

### Description

If the private key is discovered, an attacker can use the key to authenticate as an authorized user and gain access to the network infrastructure.

The cornerstone of the PKI is the private key used to encrypt or digitally sign information.

If the private key is stolen, this will lead to the compromise of the authentication and non-repudiation gained through PKI because the attacker can use the private key to digitally sign documents and pretend to be the authorized user.

Both the holders of a digital certificate and the issuing authority must protect the computers, storage devices, or whatever they use to keep the private keys.

### Check Text

Review the application documentation and interview the application administrator to identify where the application's private key is stored.

If the application does not perform code signing or other cryptographic tasks requiring a private key, this requirement is not applicable.

Ask the administrator to demonstrate where the application private key(s) are stored. Examine access restrictions and ensure access controls are in place to restrict access to the private key(s).

If the key(s) are stored on the file system, ensure adequate file permissions are set so as to only allow authorized users and processes.

If the key(s) are maintained or available via an application interface, ensure the application provides access controls that limit access via the application interface to only authorized users and processes.

Review access controls and attempt to use a relevant user account, group or application role that is not allowed access to the private key.

Verify access to the keys is denied.

If unauthorized access is granted to the private key(s), this is a finding.

**Check ID:**  C-24221r493561_chk

### Fix Text 

Configure the application or relevant access control mechanism to enforce authorized access to the application private key(s).

**Fix ID:**  F-24210r493562_fix

**Vulnerability ID:**  V-222551

**Rule ID:**  SV-222551r961041_rule

---

## The application must map the authenticated identity to the individual user or group account for PKI-based authentication.

<span style="color:#ff8c00;font-size:150%;">Medium Severity</span>

### Description

Without mapping the certificate used to authenticate to a corresponding user account, the ability to determine the identity of the individual user or group will not be available for forensic analysis.

Some CAs will include identifying information like an email address within the certificate itself. When the email is assigned to an individual, this helps to identify the individual user who has been assigned the certificate. When identifying information is not available within the certificate itself, the application must provide a mapping that allows administrators to quickly determine who the owner of the certificate is. When responding to a security incident, particularly involving user access violations, time is of the essence so this information must be readily available to investigators.

### Check Text

Review the application documentation and interview the application administrator to identify how the application maps individual user certificates or group accounts to individual users.

Access the application as a regular user while reviewing the application logs to determine if the application records the individual name of the user or if the application only includes certificate information.

If the application only logs certificate information which contains no discernable user data, ask the system admin what their process is for mapping the certificate information to the user.

If the application does not map the certificate data to an individual user or group, or if the administrator has no automated process established for determining the identity of the user, this is a finding.

**Check ID:**  C-24222r493564_chk

### Fix Text 

Configure the application to map certificate information to individual users or group accounts or create a process for automatically determining the individual user or group based on certificate information provided in the logs.

**Fix ID:**  F-24211r493565_fix

**Vulnerability ID:**  V-222552

**Rule ID:**  SV-222552r961044_rule

---

## The application, for PKI-based authentication, must implement a local cache of revocation data to support path discovery and validation in case of the inability to access revocation information via the network.

<span style="color:#ff8c00;font-size:150%;">Medium Severity</span>

### Description

A local cache of revocation data is also known as a CRL list. This list contains a list of revoked certificates and can be periodically downloaded to ensure certificates can still be checked for revocation when network access is not available or access to the Online Certificate Status Protocol (OCSP) server is not available.

Without configuring a local cache of revocation data, there is the potential to allow access to users who are no longer authorized (users with revoked certificates).

### Check Text

Review the application documentation and interview the system administrator to identify how the application checks certificate revocation.

If the application resides on the SIPRnet and does not have access to the root CAs, this requirement is Not Applicable.

Different application frameworks may handle this requirement for the developer or the developer may have chosen to implement their own implementation for managing and implementing the CRL.

Have the administrator demonstrate the process used for obtaining and importing the CRL. CAs may publish the CRL in an LDAP directory or it may be posted to an HTTP server.

Verify the application is configured to import the CRL on a regular basis.

Have the administrator demonstrate the configuration setting that enables CRL checking in the event the OCSP server is not available.

If the application is not configured to implement a CRL, this is a finding.

**Check ID:**  C-24223r985962_chk

### Fix Text 

Implement a CRL import process and configure the application to check the CRL if OCSP is not available.

**Fix ID:**  F-24212r985963_fix

**Vulnerability ID:**  V-222553

**Rule ID:**  SV-222553r1015707_rule

---

## The application must not display passwords/PINs as clear text.

<span style="color:#ff0000;font-size:150%;">High Severity</span>

### Description

To prevent the compromise of authentication information such as passwords during the authentication process, the feedback from the information system must not provide any information that would allow an unauthorized user to compromise the authentication mechanism.

Obfuscation of user-provided information when typed into the system is a method used in addressing this risk.

For example, displaying asterisks when a user types in a password is an example of obscuring feedback of authentication information.

Another method is to display authentication feedback for a very limited time, usually in fractions of a second. This occurs during password character entry where the password characters are displayed for a very small window of time and then automatically obfuscated. This allows users with just enough time to confirm their password as they type it while limiting the ability of "shoulder surfers" to covertly witness the values.

A common tactic employed to circumvent password obfuscation is to copy the obfuscated password and paste it to a text file.  Proper obfuscation techniques will not paste the clear text password.

### Check Text

Ask the application admin to log on to the application.

Observe the authentication process and verify any display feedback provided when the admin enters her/his password is obfuscated and not clear text.

For applications that display authentication feedback for a very limited time, ensure the feedback time the character is displayed is only momentary i.e., fractions of a second.

Using a text editor, copy the obfuscated password and paste to a text file.  Do not save the file.

If the application displays clear text when the password/PIN is entered, or if the time period for displayed feedback exceeds fractions of a second, or if the clear text password/PIN is displayed when pasted, this is a finding.

**Check ID:**  C-24224r493570_chk

### Fix Text 

Configure the application to obfuscate passwords and PINs when they are being entered so they cannot be read.

Design the application so obfuscated passwords cannot be copied and then pasted as clear text.

**Fix ID:**  F-24213r493571_fix

**Vulnerability ID:**  V-222554

**Rule ID:**  SV-222554r961047_rule

---

## The application must use mechanisms meeting the requirements of applicable federal laws, Executive Orders, directives, policies, regulations, standards, and guidance for authentication to a cryptographic module.

<span style="color:#ff0000;font-size:150%;">High Severity</span>

### Description

A cryptographic module is a hardware or software device or component that performs cryptographic operations securely within a physical or logical boundary, using a hardware, software or hybrid cryptographic engine contained within the boundary, and cryptographic keys that do not leave the boundary.
Based on the criticality of the application, system designers might choose to utilize a hardware based cryptographic module due to the protections and security benefits a hardware based solution provides over a software based solution. Due to various factors, including expense, hardware based encryption modules are usually relegated to only those applications where the system requirements specify it as a required protection. Examples include applications that handle extremely sensitive data or those used in life and death situations, e.g., weapons systems. 

General purpose applications such as a web site will often opt to leverage an underlying software based encryption capability that is offered by the OS, database or application development framework.  Operating systems or database products often provide their own cryptographic modules that are FIPS 140-2 compliant and can meet the authentication to the crypto module requirement via their Role Based Access Controls (users and groups) built into the product.  
In all cases, user’s accessing the cryptographic module must be authenticated and granted the appropriate rights in order to access the encryption module.  Any encryption utilized by the access control mechanisms must be FIPS 140-2 compliant.

### Check Text

Review the application documentation and interview the application administrator.

Identify if the application provides access to cryptographic modules and if access is required in order to manage cryptographic modules contained within the application.

If the application does not provide authenticated access to a cryptographic module, the requirement is not applicable.

Review and identify the cryptographic module. Refer to the NIST website listing all FIPS-approved cryptographic modules.

http://csrc.nist.gov/groups/STM/cmvp/documents/140-1/140val-all.htm

If the cryptographic module that requires authentication is not on the FIPS-approved module list, this is a finding.

**Check ID:**  C-24225r493573_chk

### Fix Text 

Use FIPS-approved cryptographic modules.

**Fix ID:**  F-24214r493574_fix

**Vulnerability ID:**  V-222555

**Rule ID:**  SV-222555r961050_rule

---

## The application must uniquely identify and authenticate non-organizational users (or processes acting on behalf of non-organizational users).

<span style="color:#ff8c00;font-size:150%;">Medium Severity</span>

### Description

Lack of authentication and identification enables non-organizational users to gain access to the application or possibly other information systems and provides an opportunity for intruders to compromise resources within the application or information system.

Non-organizational users include all information system users other than organizational users which include organizational employees or individuals the organization deems to have equivalent status of employees (e.g., contractors and guest researchers).

Non-organizational users must be uniquely identified and authenticated for all accesses other than those accesses explicitly identified and documented by the organization when related to the use of anonymous access, such as accessing a web server.

### Check Text

Review the application documentation and interview the application administrator.

If the application does not host non-organizational users, this requirement is not applicable.

Review the application and verify authentication is enabled and required in order for users to access the application.

Review the application user base and determine if all user accounts are documented and assigned to a unique individual.

Review risk acceptance documentation to determine if there are specific accesses identified that do not require authentication.

If the application does not identify and authenticate non-organizational users and there is no risk acceptance documentation approving the exception, this is a finding.

**Check ID:**  C-24226r493576_chk

### Fix Text 

Configure the application to identify and authenticate all non-organizational users.

**Fix ID:**  F-24215r493577_fix

**Vulnerability ID:**  V-222556

**Rule ID:**  SV-222556r961053_rule

---

## The application must accept Personal Identity Verification (PIV) credentials from other federal agencies.

<span style="color:#ff8c00;font-size:150%;">Medium Severity</span>

### Description

Access may be denied to authorized users if federal agency PIV credentials are not accepted.

Personal Identity Verification (PIV) credentials are those credentials issued by federal agencies that conform to FIPS Publication 201 and supporting guidance documents. OMB Memorandum 11-11 requires federal agencies to continue implementing the requirements specified in HSPD-12 to enable agency-wide use of PIV credentials.

### Check Text

Review the application documentation and interview the application administrator to identify application access methods.

If the application is not PK-enabled due to the hosted data being publicly releasable, this check is not applicable.

If the application is only deployed to SIPRNet, this requirement is not applicable.

If the application is not intended to be available to Federal government (non-DoD) partners this requirement is not applicable.

Ask the application administrator to demonstrate how the application is configured to allow the use of PIV credentials from other agencies.

If the application is required to provide authenticated access to Federal agencies and it does not accept a PIV, this is a finding.

**Check ID:**  C-24227r493579_chk

### Fix Text 

Configure the application to accept PIV credentials when utilizing authentication provided by Federal (Non-DoD) agencies.

**Fix ID:**  F-24216r493580_fix

**Vulnerability ID:**  V-222557

**Rule ID:**  SV-222557r961527_rule

---

## The application must electronically verify Personal Identity Verification (PIV) credentials from other federal agencies.

<span style="color:#ff8c00;font-size:150%;">Medium Severity</span>

### Description

Inappropriate access may be granted to unauthorized users if federal agency PIV credentials are not electronically verified.

Personal Identity Verification (PIV) credentials are those credentials issued by federal agencies that conform to FIPS Publication 201 and supporting guidance documents. OMB Memorandum 11-11 requires federal agencies to continue implementing the requirements specified in HSPD-12 to enable agency-wide use of PIV credentials.

### Check Text

Review the application documentation and interview the application administrator to identify application access methods.

If the application is not PK-enabled due to the hosted data being publicly releasable, this check is not applicable.

If the application is only deployed to SIPRNet, this requirement is not applicable.

If the application is not intended to be available to Federal government (non-DoD) partners this requirement is not applicable.

Ask the application administrator to demonstrate how the application is configured to verify the PIV credentials from other agencies when they are presented as an authentication token.

If the application is required to provide authenticated access to Federal agencies and it does not verify the PIV, this is a finding.

**Check ID:**  C-24228r493582_chk

### Fix Text 

Configure the application to verify the PIV credentials presented when utilizing authentication provided by Federal (Non-DoD) agencies.

**Fix ID:**  F-24217r493583_fix

**Vulnerability ID:**  V-222558

**Rule ID:**  SV-222558r961530_rule

---

## The application must accept Federal Identity, Credential, and Access Management (FICAM)-approved third-party credentials.

<span style="color:#ff8c00;font-size:150%;">Medium Severity</span>

### Description

FICAM establishes a federated identity framework for the federal government. FICAM provides government-wide services for common Identity, Credential and Access Management (ICAM) requirements. The FICAM Trust Framework Solutions (TFS) is the federated identity framework for the U.S. federal government.
 The TFS is a process by which Industry Trust Frameworks (The codification of requirements for credentials and their issuance, privacy and security requirements, as well as auditing qualifications and processes) are evaluated and assessed for potential use by the government. 

A Trust Framework that is comparable to federal standards is adopted through this process, which allows federal government Relying Parties (Federal Government websites or RP's) to trust Credential Service Providers (a.k.a. Identity Providers) that have been assessed under that particular trust framework. This allows federal government relying parties to trust such credentials at their approved assurance levels. 

This requirement only applies to applications that are intended to be accessible to nonfederal government agencies and other partners through FICAM. 

Third-party credentials are those credentials issued by nonfederal government entities approved by the FICAM TFS initiative.

### Check Text

Review the application documentation and interview the application administrator to identify application access methods.

If the application is not PKI-enabled due to the hosted data being publicly releasable, this check is Not Applicable.

If the application is only deployed to SIPRNet, this requirement is Not Applicable.

If the application is not intended to be available to federal government partners this requirement is Not Applicable.

Ask the application administrator to demonstrate how the application is configured to allow the use of third-party credentials, verify the third-party credentials are FICAM approved.

If the application does not accept FICAM-approved credentials when accepting third-party credentials, this is a finding.

**Check ID:**  C-24229r985965_chk

### Fix Text 

Configure applications intended to be accessible to nonfederal government agencies to use FICAM-approved third-party credentials.

**Fix ID:**  F-24218r985966_fix

**Vulnerability ID:**  V-222559

**Rule ID:**  SV-222559r1015708_rule

---

## The application must conform to Federal Identity, Credential, and Access Management (FICAM)-issued profiles.

<span style="color:#ff8c00;font-size:150%;">Medium Severity</span>

### Description

FICAM establishes a federated identity framework for the federal government. FICAM provides government-wide services for common Identity, Credential, and Access Management (ICAM) requirements. The FICAM Trust Framework Solutions (TFS) is the federated identity framework for the U.S. federal government.
 The TFS is a process by which Industry Trust Frameworks (The codification of requirements for credentials and their issuance, privacy and security requirements, as well as auditing qualifications and processes) are evaluated and assessed for potential use by the government. 

This requirement only applies to applications that are intended to be accessible to nonfederal government agencies and other partners or nonorganizational (non-DOD) users.

Without conforming to FICAM-issued profiles, the information system may not be interoperable with FICAM-authentication protocols, such as SAML 2.0, OpenID 2.0 or other protocols such as the FICAM backend Attribute Exchange.

This requirement addresses open identity management standards. More information regarding these standards is available here: info.idmanagement.gov/2012/10/what-are-ficam-technical-profiles-and.html

### Check Text

Review the application documentation and interview the application administrator to identify application access methods.

If the application is not PKI-enabled due to the hosted data being publicly releasable, this check is Not Applicable.

If the application is only deployed to SIPRnet, this requirement is Not Applicable.

If the application is not intended to be available to federal government partners this requirement is Not Applicable.

This requirement applies to DOD service providers who are relying parties of external (federal government) identity providers.
 
Ask the application administrator to demonstrate how the application conforms to FICAM issued profiles such as SAML or OPENID. 

If the application is designed to be a service provider utilizing an external identify provider and doesn't conform to FICAM-issued profiles, this is a finding.

**Check ID:**  C-24230r985968_chk

### Fix Text 

Configure the application to conform to FICAM-issued technical profiles when providing services that rely on external (federal government) identity providers.

**Fix ID:**  F-24219r985969_fix

**Vulnerability ID:**  V-222560

**Rule ID:**  SV-222560r1015709_rule

---

## Applications used for non-local maintenance sessions must audit non-local maintenance and diagnostic sessions for organization-defined auditable events.

<span style="color:#ff8c00;font-size:150%;">Medium Severity</span>

### Description

Non-local maintenance and diagnostic activities are those activities conducted by individuals communicating through a network, either an external network (e.g., the Internet) or an internal network. Local maintenance and diagnostic activities are those activities carried out by individuals physically present at the information system or information system component and not communicating across a network connection.

If events associated with non-local administrative access or diagnostic sessions are not logged and audited, a major tool for assessing and investigating attacks would not be available.

This requirement addresses auditing-related issues associated with maintenance tools used specifically for diagnostic and repair actions on organizational information systems.

This requirement applies to hardware/software diagnostic test equipment or tools. This requirement does not cover hardware/software components that may support information system maintenance, yet are a part of the system (e.g., the software implementing "ping," "ls," "ipconfig," or the hardware and software implementing the monitoring port of an Ethernet switch).

### Check Text

Review the application documentation and interview the application administrator to identify application maintenance functions.

If the application does not provide non-local maintenance and diagnostic capability, this requirement is not applicable.

Identify the maintenance functions/capabilities that are provided by the application and performed by an individual which can be performed remotely.

For example, the application may provide the ability to clean up a folder of temporary files, add users, remove users, restart processes, backup certain files, manage logs, or execute diagnostic sessions.

Identify and open the audit logs that capture maintenance actions performed by the application.

Accessing the application in the appropriate role to execute maintenance tasks, perform several maintenance tasks and observe the logs.

If the application provides maintenance functions and capabilities and those functions are not logged when they are executed, this is a finding.

**Check ID:**  C-24231r493591_chk

### Fix Text 

Configure the application to log when application maintenance functionality is executed remotely.

**Fix ID:**  F-24220r493592_fix

**Vulnerability ID:**  V-222561

**Rule ID:**  SV-222561r961548_rule

---

## Applications used for non-local maintenance sessions must implement cryptographic mechanisms to protect the integrity of non-local maintenance and diagnostic communications.

<span style="color:#ff8c00;font-size:150%;">Medium Severity</span>

### Description

Privileged access contains control and configuration information which is particularly sensitive, so additional protections are necessary. This is maintained by using cryptographic mechanisms to protect integrity.

Non-local maintenance and diagnostic activities are those activities conducted by individuals communicating through a network, either an external network (e.g., the Internet) or an internal network. Local maintenance and diagnostic activities are those activities carried out by individuals physically present at the information system or information system component and not communicating across a network connection.

This requirement applies to hardware/software diagnostic test equipment or tools. This requirement does not cover hardware/software components that may support information system maintenance, yet are a part of the system (e.g., the software implementing "ping," "ls," "ipconfig," or the hardware and software implementing the monitoring port of an Ethernet switch).

The application can meet this requirement through leveraging a cryptographic module.

### Check Text

Review the application documentation and interview the application administrator to identify application maintenance functions.

If the application does not provide non-local maintenance and diagnostic capability, this requirement is not applicable.

Identify the maintenance functions/capabilities that are provided by the application and performed by an individual which can be performed remotely.

For example, the application may provide the ability to clean up a folder of temporary files, add users, remove users, restart processes, backup certain files, manage logs, or execute diagnostic sessions.

Access the application in the appropriate role needed to execute maintenance tasks. Observe the manner in which the application is connecting and ensure the session is being encrypted.

For example, observe the browser to ensure the session is being encrypted with TLS/SSL.

If the application provides remote access to maintenance functions and capabilities and the remote access methods are not encrypted, this is a finding.

**Check ID:**  C-24232r493594_chk

### Fix Text 

Configure the application to encrypt remote application maintenance sessions.

**Fix ID:**  F-24221r493595_fix

**Vulnerability ID:**  V-222562

**Rule ID:**  SV-222562r961554_rule

---

## Applications used for non-local maintenance sessions must implement cryptographic mechanisms to protect the confidentiality of non-local maintenance and diagnostic communications.

<span style="color:#ff8c00;font-size:150%;">Medium Severity</span>

### Description

Privileged access contains control and configuration information which is particularly sensitive, so additional protections are necessary. This is maintained by using cryptographic mechanisms to protect confidentiality.

Non-local maintenance and diagnostic activities are those activities conducted by individuals communicating through a network, either an external network (e.g., the Internet) or an internal network. Local maintenance and diagnostic activities are those activities carried out by individuals physically present at the information system or information system component and not communicating across a network connection.

The application can meet this requirement through leveraging a cryptographic module.

### Check Text

Review the application documentation and interview the application administrator to identify application maintenance functions.

If the application does not provide non-local maintenance and diagnostic capability, this requirement is not applicable.

Identify the maintenance functions/capabilities that are provided by the application and performed by an individual which can be performed remotely.

For example, the application may provide the ability to clean up a folder of temporary files, add users, remove users, restart processes, backup certain files, manage logs, or execute diagnostic sessions.

Access the application in the appropriate role needed to execute maintenance tasks. Observe the manner in which the application is connecting and verify the session is being encrypted.

For example, observe the browser to ensure the session is being encrypted with TLS/SSL.

If the application provides remote access to maintenance functions and capabilities and the remote access methods are not encrypted, this is a finding.

**Check ID:**  C-24233r493597_chk

### Fix Text 

Configure the application to encrypt remote application maintenance sessions.

**Fix ID:**  F-24222r493598_fix

**Vulnerability ID:**  V-222563

**Rule ID:**  SV-222563r961557_rule

---

## Applications used for non-local maintenance sessions must verify remote disconnection at the termination of non-local maintenance and diagnostic sessions.

<span style="color:#ff8c00;font-size:150%;">Medium Severity</span>

### Description

Non-local maintenance and diagnostic activities are those activities conducted by individuals communicating through a network, either an external network (e.g., the Internet) or an internal network. Local maintenance and diagnostic activities are those activities carried out by individuals physically present at the information system or information system component and not communicating across a network connection.

If the remote connection is not closed and verified as closed, the session may remain open and be exploited by an attacker; this is referred to as a zombie session. Remote connections must be disconnected and verified as disconnected when non-local maintenance sessions have been terminated and are no longer available for use.

### Check Text

Review the application documentation and interview the application administrator to identify application maintenance functions.

If the application does not provide non-local maintenance and diagnostic capability, this requirement is not applicable.

Identify the maintenance functions/capabilities that are provided by the application, performed by an individual/admin and which can be performed remotely.

Examples include but are not limited to:

The application may provide the ability to clean up a folder of temporary files, add users, remove users, restart processes, backup certain files, manage logs, or execute diagnostic sessions.

Identify the IP address of the source system used to originate testing traffic. The IP address will be used to identify sessions on the application host so verify traffic is not traversing a proxy connection in order to reach the application host.

Access the operating system of the application host and execute the relevant OS commands to identify active TCP/IP sessions on the application host.

For example, the "netstat -a" command will provide a status of all TCP/IP connections on both Windows and UNIX systems.

Netstat output can be redirected to a file or the grep command can be used on UNIX systems to identify the specific application processes and network connections.

netstat -a |grep -i "application process name" > filename
or
netstat  -a |grep -i source IP address > filename

Utilizing the application, access using the appropriate role needed to execute maintenance tasks.

Execute a maintenance task or tasks from within the application.

Re-execute the netstat commands and identify what network connections and process IDs were created to handle the new application session.

Terminate the application session via the application interface and then execute the netstat commands a third time. The network connections should terminate or change to a state that indicates the connections are closed or are in the process of closing. Continue to execute netstat command until it is verified that the application has terminated the process sessions and closed the network connections.

Review the application logs to ensure the application has logged the disconnection event thereby verifying the disconnection.

If the application provides remote access to maintenance functions and capabilities and the remote access connections are not terminated and then verified, this is a finding.

**Check ID:**  C-24234r493600_chk

### Fix Text 

Configure the application to verify termination of remote maintenance sessions.

**Fix ID:**  F-24223r493601_fix

**Vulnerability ID:**  V-222564

**Rule ID:**  SV-222564r961560_rule

---

## The application must employ strong authenticators in the establishment of non-local maintenance and diagnostic sessions.

<span style="color:#ff8c00;font-size:150%;">Medium Severity</span>

### Description

If maintenance tools are used by unauthorized personnel, they may accidentally or intentionally damage or compromise the system. The act of managing systems and applications includes the ability to access sensitive application information, such as, system configuration details, diagnostic information, user information, and potentially sensitive application data.

Non-local maintenance and diagnostic activities are those activities conducted by individuals communicating through a network, either an external network (e.g., the Internet) or an internal network. Local maintenance and diagnostic activities are those activities carried out by individuals physically present at the information system or information system component and not communicating across a network connection.

Typically, strong authentication requires authenticators that are resistant to replay attacks and employ multifactor authentication. Strong authenticators include, for example, PKI where certificates are stored on a token protected by a password, passphrase, or biometric.

This requirement applies to hardware/software diagnostic test equipment or tools. This requirement does not cover hardware/software components that may support information system maintenance, yet are a part of the system (e.g., the software implementing "ping," "ls," "ipconfig," or the hardware and software implementing the monitoring port of an Ethernet switch).

### Check Text

Review the application documentation and interview the application administrator to identify application maintenance functions.

If the application does not provide non-local maintenance and diagnostic capability, this requirement is not applicable.

Identify the maintenance functions/capabilities that are provided by the application, performed by an individual/admin and which can be performed remotely.

Examples include but are not limited to:

The application may provide the ability to clean up a folder of temporary files, add users, remove users, restart processes, backup certain files, manage logs, or execute diagnostic sessions.

Have the application admin authenticate to the application in an administrative role and verify that strong credentials (CAC) are required to access when performing application maintenance.

Have the application admin authenticate to the application host OS and verify that strong credentials (CAC) are required to access when performing application maintenance.

If the application administrator is prevented from accessing the OS by policy requirement or separation of duties requirements, this is not a finding.

If a CAC is not used when remotely accessing the application for maintenance or diagnostic sessions, this is a finding.

**Check ID:**  C-24235r493603_chk

### Fix Text 

Configure the application to use strong authentication (CAC) when accessing the application for maintenance purposes.

**Fix ID:**  F-24224r493604_fix

**Vulnerability ID:**  V-222565

**Rule ID:**  SV-222565r961062_rule

---

## The application must terminate all sessions and network connections when nonlocal maintenance is completed.

<span style="color:#ff8c00;font-size:150%;">Medium Severity</span>

### Description

If a maintenance session or connection remains open after maintenance is completed, it may be hijacked by an attacker and used to compromise or damage the system.

Nonlocal maintenance and diagnostic activities are those activities conducted by individuals communicating through a network, either an external network (e.g., the Internet) or an internal network. Local maintenance and diagnostic activities are those activities carried out by individuals physically present at the information system or information system component and not communicating across a network connection.

This requirement applies to hardware/software diagnostic test equipment or tools. This requirement does not cover hardware/software components that may support information system maintenance, yet are a part of the system (e.g., the software implementing "ping," "ls," "ipconfig," or the hardware and software implementing the monitoring port of an Ethernet switch).

### Check Text

Review the application documentation and interview the system administrator to determine how the application is configured to terminate network sessions after sessions have been idle for a period of time. Identify any documented exceptions.

If the application does not provide nonlocal maintenance and diagnostic capability, this requirement is Not Applicable.

For privileged management sessions the period of time is 10 minutes of inactivity.

For regular user or nonprivileged sessions, the period of time is 15 minutes of inactivity.

Authenticate to the application using normal in-band access methods and as an application admin.

Perform any operation to verify access and then leave the session idle for 10 minutes and perform no activity within the application.

Access the application after the period of inactivity has expired and determine if the application still allows access.

If necessary, logout of the application, clear the browser cache, and repeat the same test procedure using the account privileges of a regular user. Leave the session inactive for 15 minutes.

If the application does not deny access after each user session has exceeded the relevant idle timeout period and there is no documented risk exceptions needed to fulfill mission requirements, this is a finding.

**Check ID:**  C-24236r985977_chk

### Fix Text 

Configure the application to expire idle user sessions after 10 minutes of inactivity for admin users and after 15 minutes of inactivity for regular users.

**Fix ID:**  F-24225r493607_fix

**Vulnerability ID:**  V-222566

**Rule ID:**  SV-222566r985978_rule

---

## The application must not be vulnerable to race conditions.

<span style="color:#ff8c00;font-size:150%;">Medium Severity</span>

### Description

A race condition is a timing event within an application that can become a security vulnerability.  A race condition can occur when a pair of programming calls operating simultaneously do not work in a sequential or coordinated manner.  A race condition is a timing event within software that can become a security vulnerability if the calls are not performed in the correct order.  

There are different types of race conditions and they are dependent upon the action that the application is undertaking when the race condition occurs.  Some examples of race conditions include but are not limited to:

- Time of check, time of use: the time in which a given resource is checked, and the time that resource is used.
- Thread based: two threads of execution use a resource simultaneously, resource may be invalid when used.
- Switch based: variable switches values while switch statement is in progress.

Developers must be cognizant of programming sequence and use sanity checks to validate data prior to acting upon it.

A code review or a static code analysis is the method used to identify race conditions.

### Check Text

Review the application documentation and architecture.

If the application is a COTS application and the vendor will not provide code review test results that demonstrate the application has been tested and is not susceptible to race conditions, the requirement is NA.

Interview the application admin and identify the most recent code testing and analysis that has been conducted.

Review the test results; verify configuration of analysis tools are set to check for the existence of  race conditions.  

If race conditions are identified in the test results, verify the latest test results are being used, if not, ensure remediation has been completed.

If the test results show race conditions exist and no remediation evidence is presented, or if test results are not available, this is a finding.

**Check ID:**  C-24237r493609_chk

### Fix Text 

Be aware of potential timing issues related to application programming calls when designing and building the application.

Validate that variable values do not change while a switch event is occurring.

**Fix ID:**  F-24226r493610_fix

**Vulnerability ID:**  V-222567

**Rule ID:**  SV-222567r961863_rule

---

## The application must terminate all network connections associated with a communications session at the end of the session.

<span style="color:#ff8c00;font-size:150%;">Medium Severity</span>

### Description

Networked applications routinely open connections to and from other systems as part of their design and function.  When connections are opened by the application, system resources are consumed.  Terminating the network connection at the end of the application session frees up these resources for later use and aids in maintaining system stability. 

Terminating network connections associated with communications sessions includes, for example, de-allocating associated TCP/IP address/port pairs at the operating system level, or de-allocating networking assignments at the application level if multiple application sessions are using a single, operating system level network connection. 

This does not mean that the application terminates all sessions or network access; it only ends the inactive session and releases the resources associated with that session.

Many applications rely on the underlying OS to control the network connection aspect of the application which is perfectly acceptable.

Additionally, application specific operational issues may occasionally be encountered which dictate exceptions be granted to this requirement in order to ensure continuity of operations and application availability.

When the aforementioned type of situation occurs, the root cause of the issue as well as the mitigations implemented in order to prevent a loss of availability must be documented.   Common mitigation procedures include but are not limited to stopping and restarting application or system services in order to manually release system resources.

### Check Text

Review the application documentation and interview the system administrator to determine how the application is designed and configured to terminate network connections at the end of the application session.

Identify any documented exceptions to the requirement and review associated mitigations.

If the application provides a management interface for controlling or monitoring application network sessions, access that management interface.  Monitor application network activity.  

If the application utilizes the underlying OS to control network connections, access the command prompt of the OS.  Run the OS command for observing network connections at the OS.  For Windows and Unix OS's, use the "netstat" command.  Include command parameters that identify the application and/or process ID. netstat /? or -h provides the list of available parameters.

Observe network activity and associate application processes with network connections.  Repeat use of the command to identify changing network state.

Determine if application session network connections are being terminated at the end of the session by observing the "state" column of the netstat command output with each iteration.

If the application does not terminate network connections when application sessions end, this is a finding.

If exceptions are documented with no mitigation this is a finding.

**Check ID:**  C-24238r493612_chk

### Fix Text 

Configure or design the application to terminate application network sessions at the end of the session.

**Fix ID:**  F-24227r493613_fix

**Vulnerability ID:**  V-222568

**Rule ID:**  SV-222568r961068_rule

---

## The application must utilize FIPS-validated cryptographic modules when signing application components.

<span style="color:#ff8c00;font-size:150%;">Medium Severity</span>

### Description

Applications that distribute components of the application must sign the components to provide an identity assurance to consumers of the application component. Components can include application messages or application code.

Use of weak or untested encryption algorithms undermines the purposes of utilizing encryption to validate the author of application components. The application must implement cryptographic modules adhering to the higher standards approved by the federal government since this provides assurance the modules have been tested and validated.

If the application resides on a National Security System (NSS) it must not use algorithms weaker than SHA-384.

### Check Text

Review the application documentation and interview the application administrator to identify the cryptographic modules used by the application.

Review the application components and application requirements. Interview application developers and application admins to determine if code signing is performed on distributable application components, files or packages.  

For example, a developer may sign application code components or an admin may sign application files or packages in order to provide application consumers with integrity assurances.

If signing has been identified in the application security plan as not being required and if a documented acceptance of risk is provided, this is not a finding.

Have the application admin or the developer demonstrate how the signing algorithms are used and how signing of components including files, code and packages is performed.

While SHA1 is currently FIPS-140-2 approved, due to known vulnerabilities with this algorithm, DoD PKI policy prohibits the use of SHA1 as of December 2016.  See DoD CIO Memo Subject: Revised Schedule to Update DoD Public Key Infrastructure Certificates to Secure Hash Algorithm-256. 

If the application signing process does not use FIPS validated cryptographic modules, or if the signing process includes SHA1 or MD5 hashing algorithms, this is a finding.

**Check ID:**  C-24240r493618_chk

### Fix Text 

Utilize FIPS-validated algorithms when signing application components.

**Fix ID:**  F-24229r493619_fix

**Vulnerability ID:**  V-222570

**Rule ID:**  SV-222570r961857_rule

---

## The application must utilize FIPS-validated cryptographic modules when generating cryptographic hashes.

<span style="color:#ff8c00;font-size:150%;">Medium Severity</span>

### Description

Use of weak or untested encryption algorithms undermines the purposes of utilizing encryption to protect data. The application must implement cryptographic modules adhering to the higher standards approved by the federal government since this provides assurance they have been tested and validated.

If the application resides on a National Security System (NSS) it must not use a hashing algorithm weaker than SHA-384.

### Check Text

Review the application components and the application requirements to determine if the application is capable of generating cryptographic hashes.

Review the application documentation and interview the application developer or administrator to identify the cryptographic modules used by the application.

If hashing of application components has been identified in the application security plan as not being required and if a documented acceptance of risk is provided, this is not a finding.

Have the application admin or the developer demonstrate how the application generates hashes and what hashing algorithms are used when generating a hash value.

While SHA1 is currently FIPS-140-2 approved, due to known vulnerabilities with this algorithm, DoD PKI policy prohibits the use of SHA1 as of December 2016.  See DoD CIO Memo Subject: Revised Schedule to Update DoD Public Key Infrastructure Certificates to Secure Hash Algorithm-256. 

If the application resides on a National Security System (NSS) and uses an algorithm weaker than SHA-384, this is a finding.

If FIPS-validated cryptographic modules are not used when generating hashes or if the application is configured to use the MD5 or SHA1 hashing algorithm, this is a finding.

**Check ID:**  C-24241r493621_chk

### Fix Text 

Configure the application to use a FIPS-validated hashing algorithm when creating a cryptographic hash.

**Fix ID:**  F-24230r493622_fix

**Vulnerability ID:**  V-222571

**Rule ID:**  SV-222571r961857_rule

---

## The application must utilize FIPS-validated cryptographic modules when protecting unclassified information that requires cryptographic protection.

<span style="color:#ff8c00;font-size:150%;">Medium Severity</span>

### Description

Use of weak or untested encryption algorithms undermines the purposes of utilizing encryption to protect data. The application must implement cryptographic modules adhering to the higher standards approved by the federal government since this provides assurance they have been tested and validated.

### Check Text

Interview the system administrator, review the application components, and the application requirements to determine if the application processes data requiring cryptographic protection.

Review the application documentation and interview the application administrator to identify the cryptographic modules used by the application.

Access the NIST site to determine if the cryptographic modules used by the application have been FIPS-validated.

http://csrc.nist.gov/groups/STM/cmvp/documents/140-1/140val-all.htm

If the application is using cryptographic modules that are not FIPS-validated to protect unclassified data, this is a finding.

**Check ID:**  C-24242r493624_chk

### Fix Text 

Configure the application to use a FIPS-validated cryptographic module.

**Fix ID:**  F-24231r493625_fix

**Vulnerability ID:**  V-222572

**Rule ID:**  SV-222572r961857_rule

---

## Applications making SAML assertions must use FIPS-approved random numbers in the generation of SessionIndex in the SAML element AuthnStatement.

<span style="color:#ff8c00;font-size:150%;">Medium Severity</span>

### Description

A predictable SessionIndex could lead to an attacker computing a future SessionIndex, thereby, possibly compromising the application.

Use of weak or untested encryption algorithms undermines the purposes of utilizing encryption to protect data. The application must implement cryptographic modules adhering to the higher standards approved by the federal government since this provides assurance they have been tested and validated.

### Check Text

Interview the system administrator, review the application components, and the application requirements to determine if the application uses SAML assertions.

If the application does not use SAML assertions, the requirement is not applicable.

Review the application documentation and interview he application administrator to identify the cryptographic modules used by the application.

Access the NIST site to determine if the cryptographic modules used by the application have been FIPS-validated.

http://csrc.nist.gov/groups/STM/cmvp/documents/140-1/140val-all.htm

If the application is using cryptographic modules that are not FIPS-validated when generating the SessionIndex in the SAML AuthnStatement, this is a finding.

**Check ID:**  C-24243r493627_chk

### Fix Text 

Configure the application to use a FIPS-validated cryptographic module.

**Fix ID:**  F-24232r493628_fix

**Vulnerability ID:**  V-222573

**Rule ID:**  SV-222573r961857_rule

---

## The application user interface must be either physically or logically separated from data storage and management interfaces.

<span style="color:#ff8c00;font-size:150%;">Medium Severity</span>

### Description

Application management functionality includes functions necessary for administration and requires privileged user access. Allowing non-privileged users to access application management functionality capabilities increases the risk that non-privileged users may obtain elevated privileges.

The separation of user functionality from information system management functionality is either physical or logical and is accomplished by using different computers, different central processing units, different instances of the operating system, different network addresses, different TCP/UDP ports, virtualization techniques, combinations of these methods, or other methods, as appropriate.

An example of this type of separation is observed in web administrative interfaces that use separate authentication methods for users of any other information system resources. This may include isolating the administrative interface on a different security domain and with additional access controls.

### Check Text

Review the application documentation and interview the application administrator.

Review the design documents and the interfaces used by the application.

Verify that the application provides separate interfaces for user traffic and for management traffic. The separation may be virtual in nature (virtual host, virtual NIC, virtual network) or physically separate.

If the application user interface and the application management interface are shared, this is a finding.

**Check ID:**  C-24244r493630_chk

### Fix Text 

Configure the application so user interface to the application and management interface to the application is separated.

**Fix ID:**  F-24233r493631_fix

**Vulnerability ID:**  V-222574

**Rule ID:**  SV-222574r961095_rule

---

## The application must set the HTTPOnly flag on session cookies.

<span style="color:#ff8c00;font-size:150%;">Medium Severity</span>

### Description

HTTPOnly is a flag included in a Set-Cookie HTTP response header. If the HTTPOnly flag is included in the HTTP response header, the cookie cannot be accessed through client side scripts like JavaScript.

If the HTTPOnly flag is set, even if a cross-site scripting (XSS) flaw in the application exists, and a user accidentally accesses a link that exploits this flaw, the browser will not reveal the cookie to a third party.

The HTTPOnly setting is browser dependent however most popular browsers support the feature. If a browser does not support HTTPOnly and a website attempts to set an HTTPOnly cookie, the HTTPOnly flag will be ignored by the browser, thus creating a traditional, script accessible cookie. As a result, the cookie (typically the session cookie) becomes vulnerable to theft or modification by a malicious script running on the client system.

### Check Text

Review the application documentation and interview the application administrator to identify when session cookies are created.

Identify any mitigating controls the application developer may have implemented. Examples include utilizing a separate Web Application Firewall that is configured to provide this capability or configuring the web server with Mod_Security or ESAPI WAF with the HTTPOnly flag directives enabled.

Reference the most recent vulnerability scan documentation.

Verify the configuration settings for the scan include web application checks including HTTPOnly tests.

Review the scan results and determine if vulnerabilities related to HTTPOnly flag not being set for session cookies have been identified.

Utilize a web browser or other web application diagnostic tool to view the session cookies the application sets on the client.

Internet Explorer versions 8, 9, and 10 includes a utility called Developer tools.

Access the application website and establish an application session.

Access the page that sets the session cookie.

Press “F12” to open Developer Tools.

Select "cache" and then "view cookie information".

Identify the session cookies. An example of an HTTPOnly session cookie is as follows:

Set-Cookie: SessionId=z5ymkk45aworjo2l31tlhqqv; path=/; HttpOnly

If the application does not set the HTTPOnly flag on session cookies or if the application administrator cannot demonstrate mitigating controls, this is a finding.

**Check ID:**  C-24245r493633_chk

### Fix Text 

Configure the application to set the HTTPOnly flag on session cookies.

**Fix ID:**  F-24234r493634_fix

**Vulnerability ID:**  V-222575

**Rule ID:**  SV-222575r1043178_rule

---

## The application must set the secure flag on session cookies.

<span style="color:#ff8c00;font-size:150%;">Medium Severity</span>

### Description

Many web development frameworks such as PHP, .NET, ASP as well as application servers include their own mechanisms for session management. Whenever possible it is recommended to utilize the provided session management framework.

Setting the secure bit on session cookie ensures the session cookie is only sent via TLS/SSL HTTPS connections.  This helps to ensure confidentiality as the session cookie is not able to be viewed by unauthorized parties as it transits the network.

Setting the secure flag on all cookies may also be warranted depending upon application design but at a minimum, the session cookie must always be secured.

### Check Text

Review the application documentation and interview the application administrator to identify when session cookies are created.

If vulnerability scan results are available, reference the most recent vulnerability scan results.

Verify that the scan configuration includes checks for the secure flag on session cookies.  If scan configuration settings are not available, follow the manual procedure provided below.

Review the scan results and determine if the secure flag not being set was identified as a vulnerability.

To manually perform the check, open a web browser, logon to the web application and use the web browser to view the new session cookie.  

The procedures used for viewing and clearing browser cookies will vary based upon the web browser used.  Providing steps for every browser is outside the scope of the STIG.  There are numerous sites that document how to view cookies using various web browsers.

For IE11:
Alt-X >> Internet options >> General >> Settings >> View Files

A windows explorer box will open that contains the contents of the Temporary Internet Files.  Browse the folder and locate the application session cookie(s).  View the contents of the cookie(s).

If the "secure" flag is not set on the session cookie, or if the vulnerability scan results indicate the application does not set the secure flag on cookies, this is a finding.

**Check ID:**  C-24246r493636_chk

### Fix Text 

Configure the application to ensure the secure flag is set on session cookies.

**Fix ID:**  F-24235r493637_fix

**Vulnerability ID:**  V-222576

**Rule ID:**  SV-222576r1043178_rule

---

## The application must not expose session IDs.

<span style="color:#ff0000;font-size:150%;">High Severity</span>

### Description

Authenticity protection provides protection against man-in-the-middle attacks/session hijacking and the insertion of false information into sessions.

Application communication sessions are protected utilizing transport encryption protocols, such as SSL or TLS. SSL/TLS provides web applications with a means to be able to authenticate user sessions and encrypt application traffic. Session authentication can be single (one-way) or mutual (two-way) in nature. Single authentication authenticates the server for the client, whereas mutual authentication provides a means for both the client and the server to authenticate each other.

This requirement applies to applications that utilize communications sessions. This includes, but is not limited to, web-based applications and Service-Oriented Architectures (SOA).

This requirement addresses communications protection at the application session, versus the network packet, and establishes grounds for confidence at both ends of communications sessions in ongoing identities of other parties and in the validity of information transmitted. Depending on the required degree of confidentiality and integrity, web services/SOA will require the use of SSL/TLS mutual authentication (two-way/bidirectional).

### Check Text

Review the application documentation and configuration.

Interview the application administrator and obtain implementation documentation identifying system architecture.

Identify the application communication paths. This includes system to system communication and client to server communication that transmit session identifiers over the network.

Have the application administrator identify the methods and mechanisms used to protect the application session ID traffic. Acceptable methods include SSL/TLS both one-way and two-way and VPN tunnel.

The protections must be implemented on a point-to-point basis based upon the architecture of the application.

For example; a web application hosting static data will provide SSL/TLS encryption from web client to the web server. More complex designs may encrypt from application server to application server (if applicable) and application server to database as well.

If the session IDs are unencrypted across network segments, this is a finding.

**Check ID:**  C-24247r493639_chk

### Fix Text 

Configure the application to protect session IDs from interception or from manipulation.

**Fix ID:**  F-24236r493640_fix

**Vulnerability ID:**  V-222577

**Rule ID:**  SV-222577r1043178_rule

---

## The application must destroy the session ID value and/or cookie on logoff or browser close.

<span style="color:#ff0000;font-size:150%;">High Severity</span>

### Description

Many web development frameworks such as PHP, .NET, and ASP include their own mechanisms for session management. Whenever possible it is recommended to utilize the provided session management framework.

Session cookies contain application session information that can be used to impersonate the web application user or hijack their application session. Once the user's session has terminated, these session IDs must be destroyed and not reused.

### Check Text

Review the application documentation and interview the application administrator.

Identify how the application destroys session IDs.

If using a web development framework, ask the application administrator to provide details on the framework's session configuration.

Review framework configuration setting to determine how the session identifiers are destroyed.

Review the client system and using a browser or other tool capable of viewing client cookies, identify cookies set by the application and verify that application session ID cookies are destroyed once the user has logged off or the browser has closed.

If the session IDs and associated cookies are not destroyed on logoff or browser close, this is a finding.

**Check ID:**  C-24248r493642_chk

### Fix Text 

Configure the application to destroy session ID cookies once the application session has terminated.

**Fix ID:**  F-24237r493643_fix

**Vulnerability ID:**  V-222578

**Rule ID:**  SV-222578r1043179_rule

---

## Applications must use system-generated session identifiers that protect against session fixation.

<span style="color:#ff8c00;font-size:150%;">Medium Severity</span>

### Description

Session fixation allows an attacker to hijack a valid user’s application session. The attack focuses on the manner in which a web application manages the user’s session ID. Applications become vulnerable when they do not assign a new session ID when authenticating users thereby using the existing session ID.

Many web development frameworks such as PHP, .NET, and ASP include their own mechanisms for session management. Whenever possible it is recommended to utilize the provided session management framework.

In many cases, creating a new session ID cookie containing a new unique value whenever authentication is performed will address the issue of session fixation.

Allowing the user to submit a session ID also introduces the risk that the application could be subject to a session fixation attack.

### Check Text

Review the application documentation and interview the application administrator to identify how the application generates user session IDs.

Application session testing is required in order to verify this requirement.

Request the latest application vulnerability or penetration test results.

Verify the test configuration includes session handling vulnerability tests.

If the application is re-using/copying the users existing session ID that was created on one system in order to maintain user state when traversing multiple application servers in the same domain, this is not a finding.

If the session testing results indicate application session IDs are re-used after the user has logged out, this is a finding.

**Check ID:**  C-24249r493645_chk

### Fix Text 

Design the application to generate new session IDs with unique values when authenticating user sessions.

**Fix ID:**  F-24238r493646_fix

**Vulnerability ID:**  V-222579

**Rule ID:**  SV-222579r1043180_rule

---

## Applications must validate session identifiers.

<span style="color:#ff8c00;font-size:150%;">Medium Severity</span>

### Description

Many web development frameworks such as PHP, .NET, and ASP include their own mechanisms for session management. Whenever possible it is recommended to utilize the provided session management framework.

### Check Text

Review the application documentation and interview the application administrator.

Identify how the application validates session IDs.

If using a web development framework, ask the application administrator to provide details on the framework's session configuration as it relates to session validation.

If the application is not configured to validate user session identifiers, this is a finding.

**Check ID:**  C-24250r493648_chk

### Fix Text 

Configure the application to configure user session identifiers.

**Fix ID:**  F-24239r493649_fix

**Vulnerability ID:**  V-222580

**Rule ID:**  SV-222580r1043180_rule

---

## Applications must not use URL embedded session IDs.

<span style="color:#ff8c00;font-size:150%;">Medium Severity</span>

### Description

Many web development frameworks such as PHP, .NET, and ASP include their own mechanisms for session management. Whenever possible it is recommended to utilize the provided session management framework.

Using a session ID that is copied to the URL introduces the risks that the session ID information will be written to log files, made available in browser history files, or made publicly available within the URL.

Using cookies to establish session ID information is desired.

### Check Text

Review the application documentation and interview the application administrator.

Identify how the application generates session IDs.

If using a web development framework, ask the application administrator to provide details on the framework's session configuration.

Review the framework configuration setting to determine how the session identifiers are created.

Identify any compensating controls that may be leveraged to minimize risk to user sessions.

If the framework or the application is configured to transmit cookies within the URL or via URL rewriting, or if the session ID is created using a GET method and there are no compensating controls configured to address user session security, this is a finding.

**Check ID:**  C-24251r493651_chk

### Fix Text 

Configure the application to transmit session ID information via cookies.

**Fix ID:**  F-24240r493652_fix

**Vulnerability ID:**  V-222581

**Rule ID:**  SV-222581r1043180_rule

---

## The application must not re-use or recycle session IDs.

<span style="color:#ff8c00;font-size:150%;">Medium Severity</span>

### Description

Many web development frameworks such as PHP, .NET, and ASP include their own mechanisms for session management. Whenever possible it is recommended to utilize the provided session management framework.

Session identifiers are assigned to application users so they can be uniquely identified. This allows the user to customize their web application experience and also allows the developer to differentiate between users thereby providing the opportunity to customize the user’s features and functions.

Once a user has logged out of the application or had their session terminated, their session IDs should not be re-used. Session IDs should also not be used for other purposes such as creating unique file names and they should also not be re-assigned to other users once the original user has logged out or otherwise quit the application.

Allowing session ID reuse increases the risk of replay attacks.

Session testing is a detailed undertaking and is usually done in the course of a web application vulnerability or penetration assessment.

### Check Text

Review the application documentation and interview the application administrator to identify how the application generates user session IDs.

Application session testing is required in order to verify this requirement.

Request the latest application vulnerability or penetration test results.

Verify the test configuration includes session handling vulnerability tests.

If the application is re-using/copying the users existing session ID that was created on one system in order to maintain user state when traversing multiple application servers in the same domain, this is not a finding.

If the session testing results indicate application session IDs are re-used after the user has logged out, this is a finding.

**Check ID:**  C-24252r493654_chk

### Fix Text 

Design the application to not re-use session IDs.

**Fix ID:**  F-24241r493655_fix

**Vulnerability ID:**  V-222582

**Rule ID:**  SV-222582r1043180_rule

---

## The application must generate a unique session identifier using a FIPS 140-2/140-3 approved random number generator.

<span style="color:#ff8c00;font-size:150%;">Medium Severity</span>

### Description

The application server will use session IDs to communicate between modules or applications within the application server and between the application server and users. The session ID allows the application to track the communications along with credentials that may have been used to authenticate users or modules.

Unique session IDs are the opposite of sequentially generated session IDs, which can be easily guessed by an attacker. Unique session identifiers help to reduce predictability of those identifiers.

Unique session IDs address man-in-the-middle attacks, including session hijacking or insertion of false information into a session. If the attacker is unable to identify or guess the session information related to pending application traffic, they will have more difficulty in hijacking the session or otherwise manipulating valid sessions.

### Check Text

Review the application server configuration and documentation to determine if the application server uses a FIPS 140-2/140-3 approved random number generator to create unique session identifiers.

Have a user log on to the application server to determine if the session IDs generated are random and unique.

If the application server does not generate unique session identifiers and does not use a FIPS 140-2/140-3 random number generator to create the randomness of the session ID, this is a finding.

**Check ID:**  C-24253r1051268_chk

### Fix Text 

Configure the application server to generate unique session identifiers and to use a FIPS 140-2/140-3 random number generator to generate the randomness of the session identifiers.

**Fix ID:**  F-24242r1051269_fix

**Vulnerability ID:**  V-222583

**Rule ID:**  SV-222583r1051270_rule

---

## The application must only allow the use of DoD-approved certificate authorities for verification of the establishment of protected sessions.

<span style="color:#ff8c00;font-size:150%;">Medium Severity</span>

### Description

Untrusted Certificate Authorities (CA) can issue certificates, but they may be issued by organizations or individuals that seek to compromise DoD systems or by organizations with insufficient security controls. If the CA used for verifying the certificate is not a DoD-approved CA, trust of this CA has not been established.

The DoD will only accept PKI certificates obtained from a DoD-approved internal or external certificate authority. Reliance on CAs for the establishment of secure sessions includes, for example, the use of SSL/TLS certificates.

This requirement focuses on communications protection for the application session rather than for the network packet.

This requirement applies to applications that utilize communications sessions. This includes, but is not limited to, web-based applications and Service-Oriented Architectures (SOA).

### Check Text

Review the application documentation and interview the application administrator to identify certificate location.

Internet Explorer can be used to view certificate information:

Select “Tools”
Select “Internet Options”
Select “Content” tab
Select “Certificates”
Select the certificate used for authentication:

Click “View”
Select “Details” tab
Select “Issuer”

If the application utilizes PKI certificates other than DoD-approved PKI and ECA certificates, this is a finding.

**Check ID:**  C-24254r493660_chk

### Fix Text 

Configure the application to utilize DoD-approved PKI established CAs when verifying DoD-signed certificates.

**Fix ID:**  F-24243r493661_fix

**Vulnerability ID:**  V-222584

**Rule ID:**  SV-222584r961596_rule

---

## The application must fail to a secure state if system initialization fails, shutdown fails, or aborts fail.

<span style="color:#ff0000;font-size:150%;">High Severity</span>

### Description

Failure to a known safe state helps prevent systems from failing to a state that may cause loss of data or unauthorized access to system resources. Applications or systems that fail suddenly and with no incorporated failure state planning may leave the hosting system available but with a reduced security protection capability. Preserving information system state information also facilitates system restart and return to the operational mode of the organization with less disruption of mission-essential processes.

In general, application security mechanisms should be designed so that a failure will follow the same execution path as disallowing the operation. For example, security methods, such as isAuthorized(), isAuthenticated(), and validate(), should all return false if there is an exception during processing. If security controls can throw exceptions, they must be very clear about exactly what that condition means.

Abort refers to stopping a program or function before it has finished naturally. The term abort refers to both requested and unexpected terminations.

### Check Text

Review application design documentation, vulnerability scanner reports and interview application administrator to identify application components.

The design of the application should account for the following:

- Connections to databases are left open
- Access control mechanisms are disabled
- Data left in temporary locations

Testing application failure will require taking down parts of the application.

Review the vulnerability assessment configuration settings included in vulnerability report.

Examine the application test plans and procedures to determine if this type of failure was previously tested.

If test plans exist, validate the tests by performing a subset of the checks.

If test plans do not exist, an application failure must be simulated.

Simulate a failure. This can be accomplished by stopping the web server service and/or the database service. Also, for applications using web services stop the web service and/or the database.

Check to ensure that application data is still protected. Some examples of tests follow:

- Try to submit SQL queries to the database. Verify that the database requires authentication before returning data.
- Try to read the application source files; access should not be granted to these files because the application is not operating.
- Try to open database files; data should not be available because the application is not operational.

If the application fails in such a way that the application security controls are rendered inoperable, this is a finding.

**Check ID:**  C-24255r493663_chk

### Fix Text 

Fix any vulnerability found when the application is an insecure state (initialization, shutdown and aborts).

**Fix ID:**  F-24244r493664_fix

**Vulnerability ID:**  V-222585

**Rule ID:**  SV-222585r961122_rule

---

## In the event of a system failure, applications must preserve any information necessary to determine cause of failure and any information necessary to return to operations with least disruption to mission processes.

<span style="color:#ff8c00;font-size:150%;">Medium Severity</span>

### Description

Failure to a known state can address safety or security in accordance with the mission/business needs of the organization. Failure to a known secure state helps prevent a loss of confidentiality, integrity, or availability in the event of a failure of the information system or a component of the system. Preserving application state information helps to facilitate application restart and return to the operational mode of the organization with less disruption to mission-essential processes.

### Check Text

Review application documentation, interview application administrator to identify how the application logs error events.

The application operational requirements documentation should provide the specific information that must be preserved in order to return the application back into operation as quickly and efficiently as possible. The application administrator will need to identify and provide the information based upon operational requirements documents.

Application diagnostic information should be kept in logs for evaluation and investigation into root cause.

If documentation is provided stating that no particular information needs to be retained in order to expediently bring the application back online, this is not a finding.

If the application does not log the data required to determine root cause of application failure, or if information specified as required in order to expediently bring the application back online is not retained, this is a finding.

**Check ID:**  C-24256r493666_chk

### Fix Text 

Create operational configuration documentation that identifies information needed for the application to return back into service or specify no such data is required, and retain data required to determine root cause of application failures.

**Fix ID:**  F-24245r493667_fix

**Vulnerability ID:**  V-222586

**Rule ID:**  SV-222586r961125_rule

---

## The application must protect the confidentiality and integrity of stored information when required by DoD policy or the information owner.

<span style="color:#ff8c00;font-size:150%;">Medium Severity</span>

### Description

Information at rest refers to the state of information when it is located on a secondary storage device (e.g., disk drive and tape drive) within an organizational information system. Mobile devices, laptops, desktops, and storage devices can be either lost or stolen, and the contents of their data storage (e.g., hard drives and non-volatile memory) can be read, copied, or altered. 

Applications and application users generate information throughout the course of their application use, including data that is stored in areas of volatile memory.  Volatile memory must not be overlooked when assigning protections.

This requirement addresses protection of user-generated data, as well as, operating system-specific configuration data. 

Applications must employ mechanisms to achieve confidentiality and integrity protections, as appropriate, in accordance with the security category and/or classification of the information.

This can include segmenting and controlling access to the data such as utilizing file permissions to restrict access, using role based controls to restrict access or applying a cryptographic hash to the data and evaluating hash values for changes made to data.

### Check Text

Review the application documentation and interview the application administrator.

Identify the data processed by the application and the accompanying data protection requirements.

Determine if the data owner has specified stored data protection requirements.

Determine if the application is processing publicly releasable, FOUO or classified stored data.

Determine if the application configuration information contains sensitive information.

Access the data repository and have the application administrator, application developer or designer identify the data integrity and confidentiality protections utilized to protect stored data.

If the application processes classified data or if the data owner has specified data protection requirements and the application administrator is unable to demonstrate how the data is protected, this is a finding.

**Check ID:**  C-24257r493669_chk

### Fix Text 

Identify data elements that require protection. Document the data types and specify protection requirements and methods used.

**Fix ID:**  F-24246r493670_fix

**Vulnerability ID:**  V-222587

**Rule ID:**  SV-222587r961128_rule

---

## The application must implement approved cryptographic mechanisms to prevent unauthorized modification of organization-defined information at rest on organization-defined information system components.

<span style="color:#ff8c00;font-size:150%;">Medium Severity</span>

### Description

Applications handling data requiring "data at rest" protections must employ cryptographic mechanisms to prevent unauthorized disclosure and modification of the information at rest.

Selection of a cryptographic mechanism is based on the need to protect the integrity of organizational information. The strength of the mechanism is commensurate with the security category and/or classification of the information. Organizations have the flexibility to either encrypt all information on storage devices (i.e., full disk encryption) or encrypt specific data structures (e.g., files, records, or fields).

### Check Text

Review the documentation and interview the application administrator.

Identify the data processed by the application and the accompanying data protection requirements.

Determine if the data owner has specified data protection encryption requirements regarding modification of data.

Determine if the application is processing publicly releasable, FOUO or classified data.

Determine if the application configuration information contains sensitive information.

If the data is strictly publicly releasable information and system documentation specifies no data encryption is required for any hosted application data, this is not applicable.

Access the data repository and have the application administrator identify the encryption protections that are utilized.

If the application processes classified data or if the data owner has specified encryption requirements and the application administrator is unable to demonstrate how the data is encrypted, this is a finding.

**Check ID:**  C-24258r493672_chk

### Fix Text 

Identify data elements that require protection.

Document the data types and specify encryption requirements.

Encrypt data according to DoD policy or data owner requirements.

**Fix ID:**  F-24247r493673_fix

**Vulnerability ID:**  V-222588

**Rule ID:**  SV-222588r961599_rule

---

## The application must use appropriate cryptography in order to protect stored DoD information when required by the information owner or DoD policy.

<span style="color:#ff8c00;font-size:150%;">Medium Severity</span>

### Description

Applications handling data requiring "data at rest" protections must employ cryptographic mechanisms to prevent unauthorized disclosure and modification of the information at rest.

Selection of a cryptographic mechanism is based on the need to protect the confidentiality of organizational information. The strength of mechanism is commensurate with the security category and/or classification of the information. Organizations have the flexibility to either encrypt all information on storage devices (i.e., full disk encryption) or encrypt specific data structures (e.g., files, records, or fields).

Special care must be taken to cryptographically protect classified data.

### Check Text

Review the application documentation and interview the application administrator.

Identify the data processed by the application and the accompanying data protection requirements.

Determine if the application is processing publicly releasable, SBU, FOUO, or classified data.

If the data is strictly publicly releasable information with no SBU, FOUO, or classified and system documentation specifies no data encryption is required for any hosted application data, this requirement is not applicable.

Have the application administrator identify the encryption protections that are utilized.

Validate the application is using encryption protections that are commensurate with the data being protected.

If the application is processing classified data, type 1, suite B cryptography, or hardware-based encryption solutions; meeting NSA encryption requirements for classified data processing and storage is required.

If the application processes classified data or if the data owner has specified encryption requirements and the application administrator is unable to demonstrate the type of encryption used or if the application processes classified and does not use type 1, suite B, or NSA-approved hardware-based encryption, this is a finding.

**Check ID:**  C-24259r493675_chk

### Fix Text 

Identify data elements that require protection.

Document the data types and specify encryption requirements.

Encrypt classified data using Type 1, Suite B, or other NSA-approved encryption solutions.

**Fix ID:**  F-24248r493676_fix

**Vulnerability ID:**  V-222589

**Rule ID:**  SV-222589r961602_rule

---

## The application must isolate security functions from non-security functions.

<span style="color:#ff8c00;font-size:150%;">Medium Severity</span>

### Description

An isolation boundary provides access control and protects the integrity of the hardware, software, and firmware that perform security functions.

Security functions are the hardware, software, and/or firmware of the information system responsible for enforcing the system security policy and supporting the isolation of code and data on which the protection is based.

Developers and implementers can increase the assurance in security functions by employing well-defined security policy models; structured, disciplined, and rigorous hardware and software development techniques; and sound system/security engineering principles. Implementation may include isolation of memory space and libraries. Applications restrict access to security functions through the use of access control mechanisms and by implementing least privilege capabilities.

### Check Text

Review the application documentation and interview the application administrator.

Identify if the application utilizes access controls.

Commonly employed access controls include Role-Based Access Controls (RBAC), Access Control Lists (ACL) and Mandatory Access Controls (MAC).

Ensure the application utilizes a control structure that is capable of protecting security assets such as policy and configuration settings from unauthorized modification.

If the application does not protect security functions that enforce security policy and protect security configuration settings, this is a finding.

**Check ID:**  C-24260r493678_chk

### Fix Text 

Implement controls within the application that limits access to security configuration functionality and isolates regular application function from security-oriented function.

**Fix ID:**  F-24249r493679_fix

**Vulnerability ID:**  V-222590

**Rule ID:**  SV-222590r961131_rule

---

## The application must maintain a separate execution domain for each executing process.

<span style="color:#ff8c00;font-size:150%;">Medium Severity</span>

### Description

Applications can maintain separate execution domains for each executing process by assigning each process a separate address space. Each process has a distinct address space so that communication between processes is performed in a manner controlled through the security functions, and one process cannot modify the executing code of another process. Maintaining separate execution domains for executing processes can be achieved, for example, by implementing separate address spaces.

An example is a web browser with process isolation that provides tabs that are separate processes using separate address spaces to prevent one tab crashing the entire browser.

### Check Text

Review the application documentation, the architecture documentation and interview the application administrator.

Identify if the application architecture provides the capability to sandbox executing processes so as to prevent a process in one application domain from sharing another application domain.

Ask the application administrator to demonstrate how the application processes are separated. This may be demonstrated by examining the OS processes running on the system and identifying the separate application processes.

If the application does not maintain a separate execution domain for each executing process, this is a finding.

**Check ID:**  C-24261r493681_chk

### Fix Text 

Design and configure applications to maintain a separate execution domain for each executing process.

**Fix ID:**  F-24250r493682_fix

**Vulnerability ID:**  V-222591

**Rule ID:**  SV-222591r961608_rule

---

## Applications must prevent unauthorized and unintended information transfer via shared system resources.

<span style="color:#ff8c00;font-size:150%;">Medium Severity</span>

### Description

Preventing unauthorized information transfers mitigates the risk of information, including encrypted representations of information, produced by the actions of prior users/roles (or the actions of processes acting on behalf of prior users/roles) from being available to any current users/roles (or current processes) that obtain access to shared system resources (e.g., registers, main memory, hard disks) after those resources have been released back to information systems. The control of information in shared resources is also commonly referred to as object reuse and residual information protection.

This requirement generally applies to the design of an information technology product, but it can also apply to the configuration of particular information system components that are, or use, such products. This can be verified by acceptance/validation processes in DoD or other government agencies.

There may be shared resources with configurable protections (e.g., files on storage) that may be assessed on specific information system components.

### Check Text

Review the application documentation and interview the application administrator to identify if the application shares information resources via file sharing protocol or if the application includes configuration settings that provide access to data files on the hard drive.

Also determine if the application transfers data via shared system resources.

If the application shares system resources with other applications, verify that a security boundary exists which controls and prevents other applications, processes, or users from accessing application data. The control mechanism will vary based upon the resource that is being shared. Hard disk sharing could possibly utilize file permissions restrictions, whereas shared overall system resources could implement virtualization or containers that restrict access.

If the application does not prevent unauthorized and unintended information transfer via shared system resources, this is a finding.

**Check ID:**  C-24262r493684_chk

### Fix Text 

 Configure or design the application to utilize a security control that will implement a boundary that will prevent unauthorized and unintended information transfer via shared system resources.

**Fix ID:**  F-24251r493685_fix

**Vulnerability ID:**  V-222592

**Rule ID:**  SV-222592r961149_rule

---

## XML-based applications must mitigate DoS attacks by using XML filters, parser options, or gateways.

<span style="color:#ff8c00;font-size:150%;">Medium Severity</span>

### Description

DoS is a condition when a resource is not available for legitimate users. When this occurs, the organization either cannot accomplish its mission or must operate at degraded capacity.

XML-based applications are susceptible to DoS attacks due to the nature of XML parsing being processor intensive and complicated.

Best practice for parsing XML to avoid DoS include:

- Using a proven XML parser
- Using an XML gateway that provides DoS protection
- Using parser options that provide limits on recursive payloads, oversized payloads, and entity expansion.

This requirement addresses the configuration of applications to mitigate the impact of DoS attacks that have occurred or are ongoing on application availability. For each application, known and potential DoS attacks must be identified and solutions for each type implemented. A variety of technologies exist to limit or, in some cases, eliminate the effects of DoS attacks (e.g., limiting processes or restricting the number of sessions the application opens at one time). Employing increased capacity and bandwidth, combined with service redundancy, may reduce the susceptibility to some DoS attacks.

### Check Text

Review the application architecture documentation and interview the application administrator to identify what steps have been taken to protect the XML aspect of the application from DoS attacks.

If the application does not contain or utilize XML, the requirement is not applicable.

Ask the application administrator to demonstrate how the application is configured to provide the following protections:

- Validation against recursive payloads
- Validation against oversized payloads
- Protection against XML entity expansion
- Validation against overlong element names
- Optimized configuration for maximum message throughput

If the application administrator cannot demonstrate how these protections are implemented either within the application itself or by third-party tools or utilities like an XML gateway, this is a finding.

**Check ID:**  C-36248r602307_chk

### Fix Text 

Implement:

- Validation against recursive payloads
- Validation against oversized payloads
- Protection against XML entity expansion
- Validation against overlong element names
- Optimized configuration for maximum message throughput in order to ensure DoS attacks against web services are limited.

**Fix ID:**  F-36212r864576_fix

**Vulnerability ID:**  V-222593

**Rule ID:**  SV-222593r961620_rule

---

## The application must restrict the ability to launch Denial of Service (DoS) attacks against itself or other information systems.

<span style="color:#ff8c00;font-size:150%;">Medium Severity</span>

### Description

Denial of Service (DoS) is a condition where a resource is not available for legitimate users. When this occurs, the organization either cannot accomplish its mission or must operate at degraded capacity.

Individuals of concern can include hostile insiders or external adversaries that have access or have successfully breached the information system and are using the system as a platform to launch cyber attacks on the application, the application host or other third-parties.

Application developers and application administrators must take the steps needed to ensure an application cannot be used to launch DoS attacks against the application itself, the application host or other systems and networks. 

Application developers should be cognizant that many attackers using DoS techniques will attempt to identify resource intensive processes and functions within the application.  For web applications, this can be application objects that perform database queries or other resource intensive tasks.  Improper application memory management can also lead to memory leaks which can exhaust system resources forcing a system or application restart.  

Limiting attempts to repeatedly execute application processes by validating the requests also reduces the ability to launch some DoS attacks.

For application administrators, ensuring network access controls are in place to protect the application host.

The methods employed to counter DoS risks are dependent upon the application layer methods that can be used to exploit it.

### Check Text

Review the application documentation and interview the application administrator.

Ask the application administrator if any anti-DoS technology or anti-DoS emergency response services are deployed to protect the application.

Check for code review, penetration or vulnerability test results that attempt to DoS the application or use the application as a DoS tool.

Examine test results and testing configuration to ensure that the application was tested and the application was not reported as being susceptible to DoS attacks either from external sources or from the application itself. Also verify the testing results show that the application cannot be weaponized to attack other systems.

If the test results indicate the application is susceptible to DoS attacks or can be weaponized to attack other applications or systems, this is a finding.

**Check ID:**  C-36249r602310_chk

### Fix Text 

Design and deploy the application to utilize controls that will prevent the application from being affected by DoS attacks or being used to attack other systems. This includes but is not limited to utilizing throttling techniques for application traffic such as QoS or implementing logic controls within the application code itself that prevents application use that results in network or system capabilities being exceeded.

**Fix ID:**  F-36213r602311_fix

**Vulnerability ID:**  V-222594

**Rule ID:**  SV-222594r961152_rule

---

## The web service design must include redundancy mechanisms when used with high-availability systems.

<span style="color:#ff8c00;font-size:150%;">Medium Severity</span>

### Description

DoS is a condition when a resource is not available for legitimate users. When this occurs, the organization either cannot accomplish its mission or must operate at degraded capacity.

In the case of application DoS attacks, care must be taken when designing the application to ensure the application makes the best use of system resources. SQL queries have the potential to consume large amounts of CPU cycles if they are not tuned for optimal performance. Web services containing complex calculations requiring large amounts of time to complete can bog down if too many requests for the service are encountered within a short period of time.

The methods employed to meet this requirement will vary depending upon the technology the application utilizes. However, a variety of technologies exist to limit or, in some cases, eliminate the effects of application related DoS attacks. Employing increased capacity and bandwidth combined with specialized application layer protection devices and service redundancy may reduce the susceptibility to some DoS attacks.

### Check Text

Interview the application administrator and review the system documentation to determine if the application has been designated as a high availability system and if the application is designed to operate in a high availability environment.

If the application has not been designated as a high availability system, this requirement is not applicable.

Review the application architecture documentation and identify solutions that provide application DoS protections. 

Verify the application has been built to work in a clustered or otherwise high availability environment in accordance with documented availability requirements.

This includes:

- load balancers
- redundant systems such as multiple web, application servers or DB servers
- high bandwidth or redundant data circuits
- multiple data centers (geographic dispersal)
- server clusters

If the application has been designated as high availability but the architecture is not built to high availability standards, this is a finding.

**Check ID:**  C-24265r493693_chk

### Fix Text 

Build the application to address issues that are found in a redundant environment and utilize redundancy mechanisms to provide high availability.

**Fix ID:**  F-24254r493694_fix

**Vulnerability ID:**  V-222595

**Rule ID:**  SV-222595r961155_rule

---

## The application must protect the confidentiality and integrity of transmitted information.

<span style="color:#ff0000;font-size:150%;">High Severity</span>

### Description

Without protection of the transmitted information, confidentiality and integrity may be compromised since unprotected communications can be intercepted and either read or altered.

This requirement applies  to those applications that transmit data, or allow access to data non-locally. Application and data owners have a responsibility for ensuring data integrity and confidentiality is maintained at every step of the data transfer and handling process. 

Application and data owners need to identify the data that requires cryptographic protection. If no data protection requirements are defined as to what specific data must be encrypted and what data is non-sensitive and doesn't require encryption, all data must be encrypted.
 
When transmitting data, applications need to leverage transmission protection mechanisms, such as TLS, SSL VPNs, or IPSEC.

Communication paths outside the physical protection of a controlled boundary are exposed to the possibility of interception and modification. Protecting the confidentiality and integrity of organizational information can be accomplished by physical means (e.g., employing physical distribution systems) or by logical means (e.g., employing cryptographic techniques). If physical means of protection are employed, then logical means (cryptography) do not have to be employed, and vice versa.

### Check Text

Review the application documentation and interview the application administrator.

Identify application clients, servers and associated network connections including application networking ports.  

Identify the types of data processed by the application and review any documented data protection requirements.

Identify the application communication protocols.

Review application documents for instructions or guidance on configuring application encryption settings.

Verify the application is configured to enable encryption protections for data in accordance with the data protection requirements. If no data protection requirements exist, ensure all application data is encrypted.

If the application does not utilize TLS, IPsec or other approved encryption mechanism to protect the confidentiality and integrity of transmitted information, this is a finding.

**Check ID:**  C-24266r493696_chk

### Fix Text 

Configure all of the application systems to require TLS encryption in accordance with data protection requirements.

**Fix ID:**  F-24255r493697_fix

**Vulnerability ID:**  V-222596

**Rule ID:**  SV-222596r961632_rule

---

## The application must implement cryptographic mechanisms to prevent unauthorized disclosure of information and/or detect changes to information during transmission unless otherwise protected by alternative physical safeguards, such as, at a minimum, a Protected Distribution System (PDS).

<span style="color:#ff8c00;font-size:150%;">Medium Severity</span>

### Description

Data is subject to manipulation and other integrity related attacks whenever that data is transferred across a network. To protect data integrity during transmission, the application must implement mechanisms to ensure the integrity of all transmitted information.

All transmitted information means that the protections are not restricted to just the data itself. Protection mechanisms must be extended to include data labels, security parameters, or metadata if data protection requirements specify.

Modern web application data transfer methods can be complex and are not necessarily just point-to-point in nature. Service-Oriented Architecture (SOA) and RESTFUL web services allow for XML-based application data to be transmitted in a manner similar to network traffic wherein the application data is transmitted along multiple servers' hops.

In such cases, point-to-point protection methods like TLS or SSL may not be the best choice for ensuring data integrity and alternative data integrity protection methods like XML Integrity Signature protections where the XML payload itself is signed may be required as part of the application design.

Overall application design and architecture must always be taken into account when establishing data integrity protection mechanisms. Custom-developed solutions that provide a file transfer capability should implement data integrity checks for incoming and outgoing files. Transmitted information requires mechanisms to ensure the data integrity (e.g., digital signatures, SSL, TLS, or cryptographic hashing).

### Check Text

Review the application documentation, the application architecture designs and interview the application administrator.

Ask the application admin to identify the network path taken by the application data and demonstrate the application support integrity mechanisms for transmission of both incoming and outgoing files and any transmitted data.

For example, hashing/digital signature and cyclic redundancy checks (CRCs) can be used to confirm integrity on data streams and transmitted files.

Use of TLS can be used to assure integrity in point-to-point communication sessions.

When the application uses messaging or web services or other technologies where the data can traverse multiple hops, the individual message or packet must be encrypted to protect the integrity of the message.

If the application is not configured to provide cryptographic protections to application data while it is transmitted unless protected by alternative safety measures like a PDS, this is a finding.

**Check ID:**  C-36250r602313_chk

### Fix Text 

Configure the application to use cryptographic protections to prevent unauthorized disclosure of application data based upon the application architecture.

**Fix ID:**  F-36214r602314_fix

**Vulnerability ID:**  V-222597

**Rule ID:**  SV-222597r961635_rule

---

## The application must maintain the confidentiality and integrity of information during preparation for transmission.

<span style="color:#ff8c00;font-size:150%;">Medium Severity</span>

### Description

Data is subject to manipulation and other integrity related attacks whenever that data is transferred across a network. To protect data integrity during transmission, the application must implement mechanisms to ensure the integrity of all transmitted information. All transmitted information means that the protections are not restricted to just the data itself. Protection mechanisms must be extended to include data labels, security parameters or metadata if data protection requirements specify. Modern web application data transfer methods can be complex and are not necessarily just point-to-point in nature. Service-Oriented Architecture (SOA) and RESTFUL web services allow for XML-based application data to be transmitted in a manner similar to network traffic wherein the application data is transmitted along multiple servers' hops. In such cases, point-to-point protection methods like TLS or SSL may not be the best choice for ensuring data integrity and alternative data integrity protection methods like XML Integrity Signature protections where the XML payload itself is signed may be required as part of the application design. Overall application design and architecture must always be taken into account when establishing data integrity protection mechanisms. Custom-developed solutions that provide a file transfer capability should implement data integrity checks for incoming and outgoing files. Transmitted information requires mechanisms to ensure the data integrity (e.g., digital signatures, SSL, TLS, or cryptographic hashing).

### Check Text

Review the application documentation and interview the application administrator.

Identify web servers and associated network connections.

Access the application with a web browser.

Verify the web browser goes secure automatically by automatically redirecting the browser to a secure port running TLS encryption, or ensure the port used by the application uses TLS encryption by default.

For tiered applications, (web server, application server, database server) verify the communication channels between the tiers is also encrypted.

If the application does not utilize TLS to protect the confidentiality and integrity of transmitted information, this is a finding.

**Check ID:**  C-24268r493702_chk

### Fix Text 

Configure all of the application systems to require TLS encryption.

**Fix ID:**  F-24257r493703_fix

**Vulnerability ID:**  V-222598

**Rule ID:**  SV-222598r961638_rule

---

## The application must maintain the confidentiality and integrity of information during reception.

<span style="color:#ff8c00;font-size:150%;">Medium Severity</span>

### Description

Data is subject to manipulation and other integrity related attacks whenever that data is transferred across a network. To protect data integrity during transmission, the application must implement mechanisms to ensure the integrity of all transmitted information. All transmitted information means that the protections are not restricted to just the data itself. Protection mechanisms must be extended to include data labels, security parameters or metadata if data protection requirements specify. Modern web application data transfer methods can be complex and are not necessarily just point-to-point in nature. Service-Oriented Architecture (SOA) and RESTFUL web services allow for XML-based application data to be transmitted in a manner similar to network traffic wherein the application data is transmitted along multiple servers' hops. In such cases, point-to-point protection methods like TLS or SSL may not be the best choice for ensuring data integrity and alternative data integrity protection methods like XML Integrity Signature protections where the XML payload itself is signed may be required as part of the application design. Overall application design and architecture must always be taken into account when establishing data integrity protection mechanisms. Custom-developed solutions that provide a file transfer capability should implement data integrity checks for incoming and outgoing files. Transmitted information requires mechanisms to ensure the data integrity (e.g., digital signatures, SSL, TLS, or cryptographic hashing).

### Check Text

Review the application documentation and interview the application administrator.

Identify web servers and associated network connections.

Access the application with a web browser.

Verify the web browser goes secure automatically by automatically redirecting the browser to a secure port running TLS encryption, or ensure the port used by the application uses TLS encryption by default.

For tiered applications, (web server, application server, database server) ensure the communication channels between the tiers is also encrypted.

If the application does not utilize TLS to protect the confidentiality and integrity of transmitted information, this is a finding.

**Check ID:**  C-24269r493705_chk

### Fix Text 

Configure all of the application systems to require TLS encryption.

**Fix ID:**  F-24258r493706_fix

**Vulnerability ID:**  V-222599

**Rule ID:**  SV-222599r961641_rule

---

## The application must not disclose unnecessary information to users.

<span style="color:#ff8c00;font-size:150%;">Medium Severity</span>

### Description

Applications should not disclose information not required for the transaction. (e.g., a web application should not divulge the fact there is a SQL server database and/or its version).

These events usually occur when the web application has not been configured to send specific error messages for error events. Instead, when a processing anomaly occurs, the application displays technical information about the type of application server, database in use, or other technical details.

This provides attackers additional information which they can use to find other attack avenues, or tailor specific attacks, on the application.

### Check Text

Review the application system documentation and interview the application administrators.

Ask them to demonstrate how the web server and application configuration does not disclose any information about the application which could be used by an attacker to gain access to the application.

Ask the application representative to logon as a non-privileged user and review all screens of the application to identify any potential data that should not be disclosed to the user.

Review web server configuration and determine if custom error pages are configured to display on error events.

Review error pages sent to application users to verify the pages are generic in nature and provide no technical details related to application architecture.

If the application displays any application technical data such as database version, application server information, or any other technical details that should not be disclosed to a regular user, this is a finding.

**Check ID:**  C-24270r493708_chk

### Fix Text 

Configure the application to not display technical details about the application architecture on error events.

**Fix ID:**  F-24259r493709_fix

**Vulnerability ID:**  V-222600

**Rule ID:**  SV-222600r961638_rule

---

## The application must not store sensitive information in hidden fields.

<span style="color:#ff0000;font-size:150%;">High Severity</span>

### Description

Hidden fields allow developers to process application data without having to display it on the screen.  Using hidden fields to pass data in forms is a common practice among web applications and by itself is not a security risk.  

However, hidden fields are not secure and can be easily manipulated by users.  Information requiring confidentiality or integrity protections must not be placed in a hidden field.   If data that is sensitive must be stored in a hidden field, it must be encrypted.

Furthermore, hidden fields used to control access decisions can lead to a complete compromise of access control mechanisms allowing immediate compromise of the user's application session.

### Check Text

Interview application administrator and review application documentation to identify and familiarize with the application features and functions.

Request most recent code review and vulnerability scan results.  Review test configuration to ensure testing for hidden fields was conducted.  Review test results for incidents of hidden data fields.  

Examine identified hidden fields and determine what type of data is stored in the hidden fields.

If the data stored in the hidden fields are determined to be authentication or session related data, or if the code review or vulnerability scan results are not available and configured to test for hidden fields, this is a finding.

**Check ID:**  C-24271r493711_chk

### Fix Text 

Design and configure the application to not store sensitive information in hidden fields.  

Encrypt sensitive information stored in hidden fields using DoD-approved encryption and use server side session management techniques for user session management.

**Fix ID:**  F-24260r493712_fix

**Vulnerability ID:**  V-222601

**Rule ID:**  SV-222601r961638_rule

---

## The application must protect from Cross-Site Scripting (XSS) vulnerabilities.

<span style="color:#ff0000;font-size:150%;">High Severity</span>

### Description



### Check Text

Review the application documentation and the vulnerability assessment scan results from automated vulnerability assessment tools.

Verify scan configuration settings include web-based applications settings which include XSS tests.

Review scan results for XSS vulnerabilities.

If the scan results indicate aspects of the application are vulnerable to XSS, request subsequent scan data that shows the XSS vulnerabilities previously detected have been fixed.

If results that show compliance are not available, request proof of any steps that have been taken to mitigate the risk. This can include using network-based IPS to detect and prevent XSS attacks from occurring.

If scan results are not available, perform manual testing in various data entry fields to determine if XSS exist.

Navigate through the web application as a regular user and identify any data entry fields where data can be input.

Input the following strings:

<script>alert('hello')</script>
<img src=x onerror="alert(document.cookie);"

If the script pop up box is displayed, or if scan reports show unremediated XSS results and no mitigating steps have been taken, this is a finding.

**Check ID:**  C-36251r602316_chk

### Fix Text 

Verify user input is validated and encode or escape user input to prevent embedded script code from executing.

Develop your application using a web template system or a web application development framework that provides auto escaping features rather than building your own escape logic.

**Fix ID:**  F-36215r602317_fix

**Vulnerability ID:**  V-222602

**Rule ID:**  SV-222602r961158_rule

---

## The application must protect from Cross-Site Request Forgery (CSRF) vulnerabilities.

<span style="color:#ff8c00;font-size:150%;">Medium Severity</span>

### Description

Cross-Site Request Forgery (CSRF) is an attack where a website user is forced to execute an unwanted action on a website that he or she is currently authenticated to. An attacker, through social engineering (e.g., e-mail or chat) creates a hyperlink which executes unwanted actions on the website the victim is authenticated to and sends it to the victim. If the victim clicks on the link, the action is executed unbeknownst to the victim.

A CSRF attack executes a website request on behalf of the user which can lead to a compromise of the user’s data. What is needed to be successful is for the attacker to know the URL, an authenticated application user, and trick the user into clicking the malicious link.

While XSS is not needed for a CSRF attack to work, XSS vulnerabilities can provide the attacker with a vector to obtain information from the user that may be used in mitigating the risk. The application must not be vulnerable to XSS as an XSS attack can be used to help defeat token, double-submit cookie, referrer and origin-based CSRF defenses.

### Check Text

Review the application documentation, the code review reports and the vulnerability assessment scan results from the automated vulnerability assessment tools.

Verify scan configuration settings include web-based application settings which include XSS tests.

Review the scan results for CSRF vulnerabilities.

If the scan results indicate aspects of the application are vulnerable to CSRF, request subsequent scan data that shows the CSRF vulnerabilities previously detected have been fixed.

If results that show compliance are not available, request proof of any steps that have been taken to mitigate the risk.

Mitigation steps include using web reputation filters to identify sources of exploits delivered via CSRF, web application firewalls that validate cookie and the referrer field in the HTTP headers, or product specific IPS filters that identify and intercept known CSRF vulnerabilities in web-based applications.

If scan results are not available ask the application administrator to provide evidence that shows the application is designed to address CSRF security issues. There are various methods for mitigating the risk, including using a challenge token that is tied to the users session.

If application scan results show an unremediated CSRF vulnerability, or if no scan results are available, or no mitigations have been enabled, this is a finding.

**Check ID:**  C-24273r493717_chk

### Fix Text 

Configure the application to use unpredictable challenge tokens and check the HTTP referrer to ensure the request was issued from the site itself.  Implement mitigating controls as required such as using web reputation services.

**Fix ID:**  F-24262r493718_fix

**Vulnerability ID:**  V-222603

**Rule ID:**  SV-222603r961158_rule

---

## The application must protect from command injection.

<span style="color:#ff0000;font-size:150%;">High Severity</span>

### Description

A command injection attack is an attack on a vulnerable application where improperly validated input is passed to a command shell setup in the application. The result is the ability of an attacker to execute OS commands via the application.

A command injection allows an attacker to execute their own commands with the same privileges as the application executing.

The following is an example of a URL based command injection attack.

Before alteration:
http://sitename/cgi-bin/userData.pl?doc=user1.txt

Example URL modified: 
http://sitename/cgi-bin/userData.pl?doc=/bin/ls|

The result is the execution of the command “/bin/ls” which could allow the attacker to list contents of the directory via the browser.

The following is a list of functions vulnerable to command injection sorted according to language.  

Language Functions/Characters
- C/C++  - system(), popen(), execlp(), execvp(), ShellExecute(), ShellExecuteEx(), _wsystem()
- Perl - system, exec, `,open, |, eval, /e
- Python - exec, eval, os.system, os.popen, execfile, input, compile
- Java - Class.forName(), Class.newInstance(), Runtime.exec()

### Check Text

Review the application documentation and the system configuration settings.

Interview the application administrator for details regarding security assessment including automated code review and vulnerability scans conducted to test for command injection.

Review the scan results from the entire application.

Verify scan configuration is set to check for command injection vulnerabilities.

If results indicate vulnerability, verify a subsequent scan has been run to ensure the issue has been remediated.

Manual test procedures are available on the OWASP website. Procedures may need to be modified to suit application architecture.

https://www.owasp.org/index.php/Testing_for_Command_Injection_%28OTG-INPVAL-013%29

If testing results are not provided demonstrating the vulnerability does not exist, or if the application representative cannot demonstrate how actions are taken to identify and protect from command injection vulnerabilities, this is a finding.

**Check ID:**  C-24274r493720_chk

### Fix Text 

Modify the application so as to escape/sanitize special character input or configure the system to protect against command injection attacks based on application architecture.

**Fix ID:**  F-24263r493721_fix

**Vulnerability ID:**  V-222604

**Rule ID:**  SV-222604r961158_rule

---

## The application must protect from canonical representation vulnerabilities.

<span style="color:#ff8c00;font-size:150%;">Medium Severity</span>

### Description

Canonical representation vulnerabilities can occur when a data conversion process does not convert the data to its simplest form resulting in the possible misrepresentation of the data.

The application may behave in an unexpected manner when acting on input that has not been sanitized or normalized.

Vulnerable application code is written to expect one form of data and executes its program logic on another form of data thereby creating instability or unexpected behavior.

The Open Web Application Security Project (OWASP) website provides test and remediation procedures that can be used for testing if vulnerability scan tools or results are not available.

The site is available by pointing your browser to https://www.owasp.org.

### Check Text

Review the application documentation and interview the application administrator for details regarding security assessment code reviews or vulnerability scans.

Review the scan results from the entire application. This can be provided as results from an automated code review or a vulnerability scanning tool.

Review the scan results to determine if there are any existing canonical representation vulnerabilities.

Review web server and application configuration.

The OWASP website provides the following test procedures:

"Investigate the web application to determine if it asserts an internal code page, locale, or culture.

If the default character set, locale is not asserted it will be one of the following:

HTTP Posts. Interesting tidbit: All HTTP posts are required to be ISO 8859-1, which will lose data for most double byte character sets. You must test your application with your supported browsers to determine if they pass in fully encoded double byte characters safely

HTTP Gets. Depends on the previously rendered page and per-browser implementations, but URL encoding is not properly defined for double byte character sets. IE can be optionally forced to do all submits as UTF-8 which is then properly canonicalized on the server

.NET: Unicode (little endian)

JSP implementations, such as Tomcat: UTF8 - see “javaEncoding” in web.xml by many servlet containers

Java: Unicode (UTF-16, big endian, or depends on the OS during JVM startup)

PHP: Set in php.ini, ISO 8859-1”

If the results are not provided or the application representative cannot demonstrate that the application does not use Unicode encoding, this is a finding.

**Check ID:**  C-36252r602319_chk

### Fix Text 

A suitable canonical form should be chosen and all user input canonicalized into that form before any authorization decisions are performed.

Security checks should be carried out after decoding is completed. Moreover, it is recommended to check that the encoding method chosen is a valid canonical encoding for the symbol it represents.

**Fix ID:**  F-36216r602320_fix

**Vulnerability ID:**  V-222605

**Rule ID:**  SV-222605r961158_rule

---

## The application must validate all input.

<span style="color:#ff8c00;font-size:150%;">Medium Severity</span>

### Description

Checking the valid syntax and semantics of information system inputs (e.g., character set, length, numerical range, and acceptable values) verifies that inputs match specified definitions for format and content. Software applications typically follow well-defined protocols that use structured messages (i.e., commands or queries) to communicate between software modules or system components. 

Structured messages can contain raw or unstructured data interspersed with metadata or control information. If software applications use attacker-supplied inputs to construct structured messages without properly encoding such messages, then the attacker could insert malicious commands or special characters that can cause the data to be interpreted as control information or metadata. 

Consequently, the module or component that receives the tainted output will perform the wrong operations or otherwise interpret the data incorrectly. Prescreening inputs prior to passing to interpreters prevents the content from being unintentionally interpreted as commands. Input validation helps to ensure accurate and correct inputs and prevent attacks such as cross-site scripting and a variety of injection attacks.

Absence of input validation opens an application to improper manipulation of data. The lack of input validation can lead immediate access of application, denial of service, and corruption of data.

Invalid input includes presence of scripting tags within text fields, query string manipulation, and invalid data types and sizes.

When an application validates input, it will only execute provided input after it has evaluated the input, validated the input and determined the data is in an expected format, and content is not extraneous or malformed.

Comprehensive application security testing and code reviews are required to ensure the application is not vulnerable to input validation vulnerabilities.

Application security code reviews should be conducted during the development phase to find and address input validation errors. When code reviews are not possible, fuzz testing can be performed on the application to attempt and identify vulnerable data input fields.

### Check Text

Review the application documentation, the code review reports and the vulnerability assessment scan results from automated vulnerability assessment tools.

Verify scan configuration settings include input validation and fuzzing tests.

Test data entry fields on all pages/screens of the application.

Procedures on testing input are relevant to the architecture of the application.

A reference on input validation testing is included at the OWASP website. The site includes testing procedures for input validation that affect many different technologies.

Identify the relevant testing procedures based upon the application architecture and components being tested.

https://www.owasp.org/index.php/Testing_for_Input_Validation

If test results include input validation errors, or if no test results exist, this is a finding.

**Check ID:**  C-24276r493726_chk

### Fix Text 

Design and configure the application to validate input prior to executing commands.

**Fix ID:**  F-24265r493727_fix

**Vulnerability ID:**  V-222606

**Rule ID:**  SV-222606r961158_rule

---

## The application must not be vulnerable to SQL Injection.

<span style="color:#ff0000;font-size:150%;">High Severity</span>

### Description

SQL Injection is a code injection attack against database applications. Malicious SQL statements are inserted into an application data entry field where they are submitted to the database and executed. This is a direct result of not validating input that is used by the application to perform a command or execute an action.

Successful attacks can read data, write data, execute administrative functions within the database, shutdown the DBMS, and in some cases execute OS commands.

Best practices to reduce the potential for SQL Injection vulnerabilities include:

Not using concatenation or replacement to build SQL queries.

Using prepared statements with parameterized queries that have been tested and validated not to be vulnerable to SQL Injection.

Using stored procedures that have been tested and validated not to be vulnerable to SQL Injection.

Escaping all user supplied input.

Additional steps to prevent SQL Injection can be found at the OWASP website:

https://www.owasp.org/index.php/SQL_Injection_Prevention_Cheat_Sheet

### Check Text

Review the application documentation and interview the application administrator.

Request the latest vulnerability scan test results.

Verify the scan configuration is configured to test for SQL injection flaws.

Review the scan results to determine if any SQL injection flaws were detected during application testing.

If SQL injection flaws were discovered, request a subsequent scan that will show that the issues have been remediated.

If the scan results are not available, identify the database product in use and refer to the OWASP web application testing guide for detailed instructions on performing a manual SQL injection test. The instructions are located here and many tests are organized by database product:

https://www.owasp.org/index.php/Testing_for_SQL_Injection_%28OTG-INPVAL-005%29

If the application is vulnerable to SQL injection attack, contains SQL injection flaws, or if scan results do not exist, this is a finding.

**Check ID:**  C-24277r493729_chk

### Fix Text 

Modify the application and remove SQL injection vulnerabilities.

**Fix ID:**  F-24266r493730_fix

**Vulnerability ID:**  V-222607

**Rule ID:**  SV-222607r961158_rule

---

## The application must not be vulnerable to XML-oriented attacks.

<span style="color:#ff0000;font-size:150%;">High Severity</span>

### Description

Extensible Markup Language (XML) is widely employed in web technology and applications like web services (SOAP, REST, and WSDL) and is also used for configuration files. XML vulnerability examples include XML injection, XML Spoofing, XML-based Denial of Service attacks and information disclosure attacks.

When utilizing XML, web applications must take steps to ensure they are addressing XML-related security issues. This is accomplished by choosing well-designed application components, building application code that follows security best practices and by patching application components when vulnerabilities are identified.

XML firewalls or gateways may be employed to assist in protecting applications by controlling access to XML-based applications, filtering XML content, rate-limiting requests, and validating XML traffic.

### Check Text

Review the application documentation, the application architecture and interview the application administrator.

Identify any XML-based web services or XML functionality performed by the application.

Determine if an XML firewall is deployed to protect application from XML-related attacks.

If the application does not process XML, the requirement is not applicable.

Review the latest application vulnerability assessment and verify the scan was configured to test for XML-related vulnerabilities and security issues.

Examples include but are not limited to:

XML Injection
XML related Denial of Service
XPATH injection
XML Signature attacks
XML Spoofing

If an XML firewall is deployed, request configuration information regarding the application and validate the firewall is configured to protect the application.

If the vulnerability scan is not configured to scan for XML-oriented vulnerabilities, if no scan results exist, or if the XML firewall is not configured to protect the application, this is a finding.

**Check ID:**  C-24278r493732_chk

### Fix Text 

Design the application to utilize components that are not vulnerable to XML attacks.

Patch the application components when vulnerabilities are discovered.

**Fix ID:**  F-24267r493733_fix

**Vulnerability ID:**  V-222608

**Rule ID:**  SV-222608r961158_rule

---

## The application must not be subject to input handling vulnerabilities.

<span style="color:#ff0000;font-size:150%;">High Severity</span>

### Description

A common application vulnerability is unpredictable behavior due to improper input validation. This requirement guards against adverse or unintended system behavior caused by invalid inputs, where information system responses to the invalid input may be disruptive or cause the system to fail into an unsafe state.

Data received from the user should always be suspected as being malicious and always validated prior to using it as input to the application.

Some examples of input methods:

- Forms Data
- URL parameters
- Hidden Fields
- Cookies
- HTTP Headers or anything in the HTTP request
- Client data entry fields

Items to validate:

- Out of range values/Boundary 
- Data length 
- Validate types of characters allowed
- Whitelist validation for known good data input while denying all other input.

Other recommendations include: 

- Using drop down menus for lists
- Validating input on the server, not on the client.

If validating on the client, also validate on the server:

- Using regular expressions to validate input
- Using HTML filter libraries that implement input validation tasks.

### Check Text

Review the application documentation and interview the application administrator.

If working with the developer, request documentation on their development processes and what their standard operating procedure is for sanitizing all application input.

Identify the latest vulnerability scan results.

Review the scan results and scan configuration settings.

Verify the scan was configured to identify input validation vulnerabilities.

If the scan results detected high risk vulnerabilities, verify a more recent scan shows remediation of the vulnerabilities is available for examination.

Review any risk acceptance documentation that indicates the ISSO has reviewed and accepted the risk.

If the vulnerability scan is not configured to test for input validation vulnerabilities if the most recent scan results show that high risk input validation vulnerabilities exist and a documented risk acceptance from the ISSO is not available, or if the scan results do not exist, this is a finding.

**Check ID:**  C-36253r602322_chk

### Fix Text 

Follow best practice when accepting user input and verify that all input is validated before the application processes the input.

Remediate identified vulnerabilities and obtain documented risk acceptance for those issues that cannot be remediated immediately.

**Fix ID:**  F-36217r864578_fix

**Vulnerability ID:**  V-222609

**Rule ID:**  SV-222609r961656_rule

---

## The application must generate error messages that provide information necessary for corrective actions without revealing information that could be exploited by adversaries.

<span style="color:#ff8c00;font-size:150%;">Medium Severity</span>

### Description

Only authorized personnel should be aware of errors and the details of the errors. Error messages are an indicator of an organization's operational state or can identify application components. Additionally, Personally Identifiable Information (PII) and operational information must not be revealed through error messages to unauthorized personnel or their designated representatives.

The structure and content of error messages must be carefully considered by the organization and development team. The extent to which the information system is able to identify and handle error conditions is guided by organizational policy and operational requirements.

Error messages should not include variable names, variable types, SQL strings, or source code. Errors that contain field names from the screen and a description of what should be in the field should not be considered a finding.

### Check Text

Review the application documentation and interview the application administrator for details regarding how the application displays error messages.

Utilize the application as a non-privileged user and attempt to execute functionality that will generate error messages.

Review the error messages displayed to ensure no sensitive information is provided to end users.

If error messages are designed to provide users with just enough detail to pass along to support staff in order to aid in troubleshooting such as date, time, or other generic information, this is not a finding.

If variable names, SQL strings, system path information, or source or program code are displayed in error messages sent to non-privileged users, this is a finding.

**Check ID:**  C-24280r493738_chk

### Fix Text 

Configure the server to not send error messages containing system information or sensitive data to users.

Use generic error messages.

**Fix ID:**  F-24269r493739_fix

**Vulnerability ID:**  V-222610

**Rule ID:**  SV-222610r961167_rule

---

## The application must reveal error messages only to the ISSO, ISSM, or SA.

<span style="color:#ff8c00;font-size:150%;">Medium Severity</span>

### Description

Only authorized personnel should be aware of errors and the details of the errors. Error messages are an indicator of an organization's operational state or can identify application components. Additionally, Personally Identifiable Information (PII) and operational information must not be revealed through error messages to unauthorized personnel or their designated representatives.

The structure and content of error messages must be carefully considered by the organization and development team. The extent to which the information system is able to identify and handle error conditions is guided by organizational policy and operational requirements.

Error messages should not include variable names, variable types, SQL strings, or source code. Errors that contain field names from the screen and a description of what should be in the field should not be considered a finding.

### Check Text

Review the application documentation and interview the application administrator for details regarding how the application displays error messages.

Authenticate to the application as a non-privileged user and attempt to execute functionality that will generate error messages.

Review the error messages displayed to ensure no sensitive information is provided to end users.

Authenticate as a privileged user and repeat tests.

If error messages are designed to provide users with just enough detail to pass along to support staff in order to aid in troubleshooting such as date, time or other generic information, this is not a finding.

If detailed error messages are provided to privileged users, this is not a finding.

If variable names, SQL strings, system path information, or source or program code are displayed in error messages sent to non-privileged users, this is a finding.

**Check ID:**  C-24281r493741_chk

### Fix Text 

Configure the server to only send error messages containing system information or sensitive data to privileged users.

Use generic error messages for non-privileged users.

**Fix ID:**  F-24270r493742_fix

**Vulnerability ID:**  V-222611

**Rule ID:**  SV-222611r961170_rule

---

## The application must not be vulnerable to overflow attacks.

<span style="color:#ff0000;font-size:150%;">High Severity</span>

### Description

A buffer overflow occurs when a program exceeds the amount of data allocated to a buffer. The buffer is a sequential section of memory and when the data is written outside the memory bounds, the program can crash or malicious code can be executed.

Security safeguards employed to protect memory include, for example, data execution prevention and address space layout randomization. Data execution prevention safeguards can either be hardware-enforced or software-enforced with hardware providing the greater strength of mechanism.

Buffer overflows can manifest as stack overflows, heap overflows integer overflows and format string overflows. Each type of overflow is dependent upon the underlying application language and the context in which the overflow is executed.

Integer overflows can lead to infinite looping when loop index variables are compromised and cause a denial of service.  If the integer is used in data references, the data can become corrupt. Also, using the integer in memory allocation can cause buffer overflows, and a denial of service.  Integers used in access control mechanisms can potentially trigger buffer overflows, which can be used to execute arbitrary code. 

Almost all known web servers, application servers, and web application environments are susceptible to buffer overflows. Proper validation of user input is required to mitigate the risk. Notably, limiting the size of the strings a user is allowed to input to a program to a predetermined, acceptable length.

A code review, static code analysis or active vulnerability or fuzz testing are methods used to identify overflows within application code.

### Check Text

Review the application documentation and architecture.

Interview the application admin and identify the most recent code testing and analysis that has been conducted.

Review the test results; verify configuration of analysis tools are set to check for the existence of overflows. This includes but is not limited to buffer overflows, stack overflows, heap overflows, integer overflows and format string overflows.

If overflows are identified in the test results, verify the latest test results are being used, if not, ensure remediation has been completed.

If the test results show overflows exist and no remediation evidence is presented, or if test results are not available, this is a finding.


**Check ID:**  C-36254r602325_chk

### Fix Text 

Design the application to use a language or compiler that performs automatic bounds checking.

Use an abstraction library to abstract away risky APIs.

Use compiler-based canary mechanisms such as StackGuard, ProPolice, and the Microsoft Visual Studio/GS flag.

Use OS-level preventative functionality and control user input validation.

Patch applications when overflows are identified in vendor products.

**Fix ID:**  F-36218r864579_fix

**Vulnerability ID:**  V-222612

**Rule ID:**  SV-222612r961665_rule

---

## The application must remove organization-defined software components after updated versions have been installed.

<span style="color:#ff8c00;font-size:150%;">Medium Severity</span>

### Description

Previous versions of software components that are not removed from the information system after updates have been installed may be exploited by adversaries. Some information technology products may remove older versions of software automatically from the information system.

### Check Text

Review the application documentation and interview the application admin to identify application locations on system.

Identify application versions that are installed on the system.

Review the file system structure to see if older versions of the application are still installed.

If old versions of the application or components are still installed on the system, this is a finding.

**Check ID:**  C-24283r493747_chk

### Fix Text 

Configure or design the application to remove old components when updating.

**Fix ID:**  F-24272r493748_fix

**Vulnerability ID:**  V-222613

**Rule ID:**  SV-222613r961677_rule

---

## Security-relevant software updates and patches must be kept up to date.

<span style="color:#ff8c00;font-size:150%;">Medium Severity</span>

### Description



### Check Text

Review the application documentation to identify application versions and patching.

Interview the application administrator and inquire about patching process.

Review IAVMs and CTOs to determine if the application is being updated in accordance with authoritative sources.

If application updates are not checked on at least on a weekly basis and applied immediately or in accordance with POA&Ms, IAVMs, CTOs, DTMs or other authoritative patching guidelines or sources, this is a finding.

**Check ID:**  C-24284r493750_chk

### Fix Text 

Check for application updates at least weekly and apply patches immediately or in accordance with POA&Ms, IAVMs, CTOs, DTMs or other authoritative patching guidelines or sources.

**Fix ID:**  F-24273r493751_fix

**Vulnerability ID:**  V-222614

**Rule ID:**  SV-222614r961683_rule

---

## The application performing organization-defined security functions must verify correct operation of security functions.

<span style="color:#ff8c00;font-size:150%;">Medium Severity</span>

### Description

Without verification, security functions may not operate correctly and this failure may go unnoticed.

Security function is defined as the hardware, software, and/or firmware of the information system responsible for enforcing the system security policy and supporting the isolation of code and data on which the protection is based. Security functionality includes, but is not limited to, establishing system accounts, configuring access authorizations (i.e., permissions, privileges), setting events to be audited, and setting intrusion detection parameters.

This requirement applies to applications performing security functions and security function verification/testing.

### Check Text

Review the application documentation and interview the system administrator to determine if the application performs security function testing.

If the application is not designed or intended to perform security function testing, the requirement is not applicable.

Access the application design documents and determine if the application is designed to verify the correct operation of security functions.

Review application logs and take note of log entries that indicate security function testing is being performed and verified.

If the application is designed to perform security function testing and does not verify the correct operation of security functions, this is a finding.

**Check ID:**  C-24285r493753_chk

### Fix Text 

Design the application to verify the correct operation of security functions.

**Fix ID:**  F-24274r493754_fix

**Vulnerability ID:**  V-222615

**Rule ID:**  SV-222615r961731_rule

---

## The application must perform verification of the correct operation of security functions: upon system startup and/or restart; upon command by a user with privileged access; and/or every 30 days.

<span style="color:#ff8c00;font-size:150%;">Medium Severity</span>

### Description

Without verification, security functions may not operate correctly and this failure may go unnoticed.

Security function is defined as the hardware, software, and/or firmware of the information system responsible for enforcing the system security policy and supporting the isolation of code and data on which the protection is based. Security functionality includes, but is not limited to, establishing system accounts, configuring access authorizations (i.e., permissions, privileges), setting events to be audited, and setting intrusion detection parameters.

Notifications provided by information systems include, for example, electronic alerts to system administrators, messages to local computer consoles, and/or hardware indications, such as lights.

This requirement applies to applications performing security functions and the applications performing security function verification/testing.

### Check Text

Review the application documentation and interview the system administrator to determine if the application performs security function testing.

If the application is not designed or intended to perform security function testing, the requirement is not applicable.

Access the application design documents or have the system administrator provide proof if the application is designed to verify the correct operation of security functions.

Review application logs and take note of log entries that indicate security function testing is being performed and verified on startup, restart, or on command by an authorized user.

If the application is designed to perform security function testing and does not verify the correct operation of security functions on startup, restart, or upon command by a privileged user, this is a finding.

**Check ID:**  C-24286r493756_chk

### Fix Text 

Design the application to verify the correct operation of security functions on command and on application startup and restart.

**Fix ID:**  F-24275r493757_fix

**Vulnerability ID:**  V-222616

**Rule ID:**  SV-222616r961734_rule

---

## The application must notify the ISSO and ISSM of failed security verification tests.

<span style="color:#b3b31a;font-size:150%;">Low Severity</span>

### Description

If personnel are not notified of failed security verification tests, they will not be able to take corrective action and the unsecure condition(s) will remain.

Security function is defined as the hardware, software, and/or firmware of the information system responsible for enforcing the system security policy and supporting the isolation of code and data on which the protection is based. Security functionality includes, but is not limited to, establishing system accounts, configuring access authorizations (i.e., permissions, privileges), setting events to be audited, and setting intrusion detection parameters.

Notifications provided by information systems include messages to local computer consoles, and/or hardware indications, such as lights.

This requirement applies to applications performing security functions and the applications performing security function verification/testing.

### Check Text

Review the application documentation and interview the system administrator to determine if the application performs security function testing.

If the application is not designed or intended to perform security function testing, the requirement is not applicable.

Access the application design documents or have the system administrator provide proof the application is designed to verify the correct operation of security functions.

Review application logs and take note of log entries that indicate security function testing is being performed and verified on startup, restart, or on command by an authorized user.

Review logs to identify if the application has sent notifications to ISSO and ISSM when security verification tests fail.

Review application features and function to identify areas of the management interfaces that specify where failed security verifications tests are to be sent and validate the ISSO and ISSM are configured as recipients.
 
If the application is designed to perform security function testing and does not notify the ISSO and ISSM of failed verification tests, this is a finding.

**Check ID:**  C-24287r493759_chk

### Fix Text 

Configure the application to send notices to the ISSO and ISSM indicating the application failed a verification test.

**Fix ID:**  F-24276r493760_fix

**Vulnerability ID:**  V-222617

**Rule ID:**  SV-222617r961185_rule

---

## Unsigned Category 1A mobile code must not be used in the application in accordance with DoD policy.

<span style="color:#ff8c00;font-size:150%;">Medium Severity</span>

### Description

Use of un-trusted Level 1A mobile code technologies can introduce security vulnerabilities and malicious code into the client system.

1A code is defined as:

- ActiveX controls
- Mobile code script (JavaScript, VBScript)
- Windows Scripting Host (WSH) (downloaded via URL or email)

When JavaScript and VBScript execute within the browser they are Category 3, however, when they execute in WSH, they are 1A.

### Check Text

Review the application documentation and interview the application administrator to identify any mobile code that is provided by the application for client consumption.

If the application does not contain mobile code, or if the mobile code executes within the client browser, this is not applicable.

The URL of the application must be added to the Trusted Sites zone. This is accomplished via the Tools, Internet Options, and “Security” Tab.

Select the “Trusted Sites” zone.
Click the “sites” button.
Enter the URL into the text box below the “Add this site to this zone” message.
Click "Add”.
Click “OK”.

Note: This requires administrator privileges to add URL to sites on a STIG compliant workstation.

Next, test the application. This testing should include functional testing from all major components of the application.

If mobile code is in use, the browser will prompt to download the control. At the download prompt, the browser will indicate that code has been digitally signed.

If the code has not been signed or the application warns that a control cannot be invoked due to security settings, this is a finding.

**Check ID:**  C-24288r493762_chk

### Fix Text 

Configure the application so Category 1A mobile code is signed.

**Fix ID:**  F-24277r493763_fix

**Vulnerability ID:**  V-222618

**Rule ID:**  SV-222618r961083_rule

---

## The ISSO must ensure an account management process is implemented, verifying only authorized users can gain access to the application, and individual accounts designated as inactive, suspended, or terminated are promptly removed.

<span style="color:#ff8c00;font-size:150%;">Medium Severity</span>

### Description

A comprehensive account management process will ensure that only authorized users can gain access to applications and that individual accounts designated as inactive, suspended, or terminated are promptly deactivated. Such a process greatly reduces the risk that accounts will be misused, hijacked, or data compromised.

### Check Text

Interview the application representative to verify that a documented process exists for user and system account creation, termination, and expiration.

Obtain a list of recently departed personnel and verify that their accounts were removed or deactivated on all systems in a timely manner (e.g., less than two days).
 
If a documented account management process does not exist or unauthorized users have active accounts, this is a finding.

**Check ID:**  C-24289r493765_chk

### Fix Text 

Establish an account management process.

**Fix ID:**  F-24278r493766_fix

**Vulnerability ID:**  V-222619

**Rule ID:**  SV-222619r961863_rule

---

## Application web servers must be on a separate network segment from the application and database servers if it is a tiered application operating in the DoD DMZ.

<span style="color:#ff0000;font-size:150%;">High Severity</span>

### Description

A tiered application usually consists of 3 tiers, the web layer (presentation tier), the application layer (application logic tier), and the database layer (data storage tier).

Using one system for hosting all 3 tiers introduces risk that if one tier is compromised, there are no additional protection layers available to defend the other tiers.
Security controls must be in place in order to provide different levels and types of defenses for each type of server based upon data protection requirements identified by policy or data owner.

DoD DMZ policy specifies that logical separation is allowed but when hosting different data types on the same server, physical separation is required.

1) Unrestricted web servers and Restricted web servers must be on separate virtual or physical servers from Private web servers, application servers, or database servers.
2) Unrestricted web servers and Restricted web servers can either be on separate physical servers from each other, or they can be on separate virtual servers.
3) If application and database servers have been separated by service type into Unrestricted, Restricted, and Private servers (permitted but not required in Increment 1 Phase 1), they must be on separate virtual or physical servers from each other by server type (Application or Database) and by service type (Unrestricted, Restricted, or Private).

Reference the DoD DMZ STIG for details on data types and separation requirements.

Security controls include firewalls or other forms of access controls that restrict the ability to traverse the network from one system to the other.

Separation can be performed either physically or logically based upon data protection and application protection design requirements.

Physically separate networks require distinct physical network devices for connections (e.g., two separate switches or two separate routers).

Physically separate machines utilize a non-virtual OS.

Logically separate networks are usually implemented via a VLAN.

Logically separate systems are implemented with virtual machines or other system emulation.

Security controls are firewall rules or ACLs that provide access restrictions on network traffic and limit communications between systems to only application and application/system support traffic.

For complete explanation of DoD DMZ requirements, reference DoD DMZ requirements.

### Check Text

Review the application documentation.

Review the application data protection requirements and identify if all data types hosted on server are identical.

Review the network diagram and identify web servers/web services, web application servers, and database servers.

If the application is not hosted in the DoD DMZ, this requirement is not applicable.

Verify the application web servers are separated from the application and database servers if the application is a tiered design as per DoD DMZ STIG requirements.

If the application is tiered and the network infrastructure hosting the application is not configured to provide separation and security access controls between the tiered layers in accordance with DoD DMZ requirements, this is a finding.

**Check ID:**  C-24290r493768_chk

### Fix Text 

Separate web server from other application tiers and place it on a separate network segment apart from the application and database servers in accordance with DoD DMZ data access controls requirements.

**Fix ID:**  F-24279r493769_fix

**Vulnerability ID:**  V-222620

**Rule ID:**  SV-222620r961863_rule

---

## The ISSO must ensure application audit trails are retained for at least 1 year for applications without SAMI data, and 5 years for applications including SAMI data.

<span style="color:#ff8c00;font-size:150%;">Medium Severity</span>

### Description

Log files are a requirement to trace intruder activity or to audit user activity.

### Check Text

Verify a process is in place to retain application audit log files for one year and five years for SAMI data.

If audit logs have not been retained for one year or five years for SAMI data, this is a finding.

**Check ID:**  C-24291r493771_chk

### Fix Text 

Retain application audit log files for one year and five years for SAMI data.

**Fix ID:**  F-24280r493772_fix

**Vulnerability ID:**  V-222621

**Rule ID:**  SV-222621r961863_rule

---

## The ISSO must review audit trails periodically based on system documentation recommendations or immediately upon system security events.

<span style="color:#ff8c00;font-size:150%;">Medium Severity</span>

### Description

Without access control the data is not secure. It can be compromised, misused, or changed by unauthorized access at any time.

### Check Text

Interview the application representative and ask for the system documentation that states how often audit logs are reviewed. Also, determine when the audit logs were last reviewed.

If the application representative cannot provide system documentation identifying how often the auditing logs are reviewed, or has not audited within the last time period stated in the system documentation, this is a finding.

**Check ID:**  C-24292r493774_chk

### Fix Text 

Establish a scheduled process for reviewing logs.

Maintain a log or records of dates and times audit logs are reviewed.

**Fix ID:**  F-24281r493775_fix

**Vulnerability ID:**  V-222622

**Rule ID:**  SV-222622r961863_rule

---

## The ISSO must report all suspected violations of IA policies in accordance with DoD information system IA procedures.

<span style="color:#ff8c00;font-size:150%;">Medium Severity</span>

### Description

Violations of IA policies must be reviewed and reported. If there are no policies regarding the reporting of IA violations, IA violations may not be tracked or addressed in a proper manner.

### Check Text

Interview the application representative and review the SOPs to ensure that violations of IA policies are analyzed and reported.
 
If there is no policy for reporting IA violations, this is a finding.

**Check ID:**  C-24293r493777_chk

### Fix Text 

Create and maintain a policy to report IA violations.

**Fix ID:**  F-24282r493778_fix

**Vulnerability ID:**  V-222623

**Rule ID:**  SV-222623r961863_rule

---

## The ISSO must ensure active vulnerability testing is performed.

<span style="color:#ff8c00;font-size:150%;">Medium Severity</span>

### Description

Use of automated scanning tools accompanied with manual testing/validation which confirms or expands on the automated test results is an accepted best practice when performing application security testing. Automated scanning tools expedite and help to standardize security testing, they can incorporate known attack methods and procedures, test for libraries and other software modules known to be vulnerable to attack and utilize a test method known as "fuzz testing". Fuzz testing is a testing process where the application is provided invalid, unexpected, or random data. Poorly designed and coded applications will become unstable or crash. Properly designed and coded applications will reject improper and unexpected data input from application clients and remain stable.

Many vulnerability scanning tools provide automated fuzz testing capabilities for the testing of web applications. All of these tools help to identify a wide range of application vulnerabilities including, but not limited to; buffer overflows, cross-site scripting flaws, denial of service format bugs and SQL injection, all of which can lead to a successful compromise of the system or result in a denial of service.

Due to changes in the production environment, it is a good practice to schedule periodic active testing of production web applications. Ideally, this will occur prior to deployment and after updates or changes to the application production environment.

It is imperative that automated scanning tools are configured properly to ensure that all of the application components that can be tested are tested. In the case of web applications, some of the application code base may be accessible on the website and could potentially be corrected by a knowledgeable system administrator. Active testing is different from code review testing in that active testing does not require access to the application source code base. A code review requires complete code base access and is normally performed by the development team.

If vulnerability testing is not conducted, there is the distinct potential that security vulnerabilities could be unknowingly introduced into the application environment.

The following website provides an overview of fuzz testing and examples:

http://www.owasp.org/index.php/Fuzzing

### Check Text

Ask the application representative to provide vulnerability test procedures and vulnerability test results.

Ask the application representative to provide the settings that were used to conduct the vulnerability testing.

Verify the automated vulnerability scanning tool was appropriately configured to ensure as complete a test as possible of the application architecture components (e.g., if the application includes a web server, web server tests must be included).

If the vulnerability scan report includes informational and/or noncritical results, this is not a finding.

If previously identified vulnerabilities have subsequently been resolved, this is not a finding.

If the application test procedures and test results do not include active vulnerability and fuzz testing, this is a finding.

If the vulnerability scan results include critical vulnerabilities 21 business days or older, this is a finding.

If the vulnerability scanning tests are not relevant to the architecture of the application, this is a finding.

**Check ID:**  C-24294r1051271_chk

### Fix Text 

Perform active vulnerability and fuzz testing of the application.

Verify the vulnerability scanning tool is configured to test all application components and functionality.

Address discovered vulnerabilities.

**Fix ID:**  F-24283r493781_fix

**Vulnerability ID:**  V-222624

**Rule ID:**  SV-222624r1051272_rule

---

## Execution flow diagrams and design documents must be created to show how deadlock and recursion issues in web services are being mitigated.

<span style="color:#ff8c00;font-size:150%;">Medium Severity</span>

### Description

In order to understand data flows within web services, the process flow of data must be developed and documented.

There are several different ways that web service deadlock occurs, many times it is due to when a client invokes a synchronous method on a web service, the client will block waiting for the method to complete. If attempts to call the client (invoke a callback) while the client is waiting for the original method to complete, then each party will deadlock waiting for the other.

This is referred to as deadlock. The same situation could occur if a callback handler attempted to call a synchronous method on its caller.

Applications that utilize web services must account for and document how they deal with a deadlock issue. This can be accomplished by documenting data flow and specifically accounting for the risk in the design of the application.

### Check Text

Review the application documentation and the system diagrams detailing application system to system and service to service communication methods.

Interview the application admin to identify any application web services that are deployed by the application.

If the application does not deploy web services, the requirement is not applicable.

If the application consumes web services but is not responsible for development of the services, the requirement is not applicable.

Review the data flow diagrams and the system documentation to determine if the issue of web service deadlock is addressed.

If the issue is not addressed in the documentation or configuration settings, ask the application admin to demonstrate how deadlock issues are addressed.

If deadlock issues are not being addressed via documented web service configuration or design, this is a finding.

**Check ID:**  C-24295r493783_chk

### Fix Text 

Develop web services to account for deadlock issues.

**Fix ID:**  F-24284r493784_fix

**Vulnerability ID:**  V-222625

**Rule ID:**  SV-222625r961863_rule

---

## The designer must ensure the application does not store configuration and control files in the same directory as user data.

<span style="color:#ff8c00;font-size:150%;">Medium Severity</span>

### Description

Application configuration settings and user data are required to be stored in separate locations in order to prevent application users from possibly being able to access application configuration settings or application data files. Without proper access controls and separation of application configuration settings from user data, there is the potential that existing code or configuration settings could be changed by users. These changes in code can lead to a Denial of Service (DoS) attack or allow malicious code to be placed within the application. In addition, collocating application data and code complicates many issues such as backup, recovery, directory access privilege, and upgrades.

### Check Text

Review the application documentation and interview the application administrator.

Ask the application administrator or examine the application documentation to determine the file location of the application configuration settings and user data.

Identify the directory where the application code, configuration settings and other application control data are located.

Identify where user data is stored.

Examine file permissions to application folder.

If the application user data is located in the same directory as the application configuration settings or control files, or if the file permissions allow application users write access to application configuration settings, this is a finding.

**Check ID:**  C-24296r493786_chk

### Fix Text 

Separate the application user data into a different directory than the application code and user file permissions to restrict user access to application configuration settings.

**Fix ID:**  F-24285r493787_fix

**Vulnerability ID:**  V-222626

**Rule ID:**  SV-222626r961863_rule

---

## The ISSO must ensure if a DoD STIG or NSA guide is not available, a third-party product will be configured by following available guidance.

<span style="color:#ff8c00;font-size:150%;">Medium Severity</span>

### Description

Not all COTS products are covered by a STIG. Those products not covered by a STIG, should follow commercially accepted best practices, independent testing results and vendors lock down guides and recommendations if they are available.

### Check Text

Review the application documentation to identify application name, features and version.

Identify if a DoD STIG or NSA guide is available.

If no STIG is available for the product, the application and application components must be configured by the following as available: 

- commercially accepted practices, 
- independent testing results, or 
- vendor literature and lock down guides.

If the application and application components do not have DoD STIG or NSA guidance available and are not configured according to: 
commercially accepted practices, 
independent testing results,
or vendor literature and lock down guides, this is a finding.

**Check ID:**  C-24297r493789_chk

### Fix Text 

Configure the application according to the product STIG or when a STIG is not available, utilize:

- commercially accepted practices,
- independent testing results, or
- vendor literature and lock down guides.

**Fix ID:**  F-24286r493790_fix

**Vulnerability ID:**  V-222627

**Rule ID:**  SV-222627r961863_rule

---

## New IP addresses, data services, and associated ports used by the application must be submitted to the appropriate approving authority for the organization, which in turn will be submitted through the DoD Ports, Protocols, and Services Management (DoD PPSM)

<span style="color:#ff8c00;font-size:150%;">Medium Severity</span>

### Description

Failure to comply with DoD Ports, Protocols, and Services (PPS) Vulnerability Analysis and associated PPS mitigations may result in compromise of enclave boundary protections and/or functionality of the application.

### Check Text

All application ports, protocols, and services needed for application operation need to be in compliance with the DoD Ports and Protocols guidance.

Check:

http://iase.disa.mil/ppsm/Pages/index.aspx

to verify the ports, protocols, and services are in compliance with the PPS CAL.

Check all necessary ports and protocols needed for application operation (only those accessed from outside the local enclave) are checked against the DoD Ports and Protocols guidance to ensure compliance.

Identify the ports needed for the application:

- Look at System Security Plan/Accreditation documentation
- Ask System Administrator
- Go to Network Administrator
- Go to Network Reviewer
- If a network scan is available, use it
- Use netstat/task manager
- Check /etc./services

If the application is not in compliance with DoD Ports and Protocols guidance, this is a finding.


**Check ID:**  C-36255r602328_chk

### Fix Text 

Verify the accreditation documentation lists all interfaces and the ports, protocols, and services used.

Verify that all ports, protocols, and services are used in accordance with the DoD PPSM.

**Fix ID:**  F-36219r602329_fix

**Vulnerability ID:**  V-222628

**Rule ID:**  SV-222628r961863_rule

---

## The application must be registered with the DoD Ports and Protocols Database.

<span style="color:#ff8c00;font-size:150%;">Medium Severity</span>

### Description

Failure to register the applications usage of ports, protocols, and services with the DoD PPS Database may result in a Denial of Service (DoS) because of enclave boundary protections at other end points within the network.

### Check Text

Verify registration of the application and ports in the Ports and Protocols Database for a production site.

If the application requires registration, and is not registered or all ports used have not been identified in the database, this is a finding.

**Check ID:**  C-24299r493795_chk

### Fix Text 

Register the application and ports in the Ports and Protocols Database.

**Fix ID:**  F-24288r493796_fix

**Vulnerability ID:**  V-222629

**Rule ID:**  SV-222629r961863_rule

---

## The Configuration Management (CM) repository must be properly patched and STIG compliant.

<span style="color:#ff8c00;font-size:150%;">Medium Severity</span>

### Description

A Configuration Management (CM) repository is used to manage application code versions and to securely store application code.

Failure to properly apply security patches and secure the software Configuration Management system could affect the confidentiality and integrity of the application source-code.  

Compromise of the Configuration Management system could lead to unauthorized changes to applications including the addition of malware, root kits, back doors, logic bombs or other malicious functions into valid application code.   

This requirement is intended to be applied to application developers or organizations responsible for code management or who have and operate an application CM repository.

### Check Text

Review the application system documentation and interview the application administrator.

Identify if the STIG is being applied to application developers or organizations responsible for code management or who have and operate an application CM repository. If this is not the case, the requirement is not applicable.

Review CM patch management processes and procedures.  Have the system and CM admins demonstrate their patch management processes and verify the system has the latest security patches applied.  

Review the ATO documentation and verify the system that operates the CM repository software has had all relevant STIGs applied.

If CM repository is not at the latest security patch level and is not operating on a STIG compliant system, this is a finding.

**Check ID:**  C-24300r493798_chk

### Fix Text 

Patch the CM system when new security patches are made available and apply the relevant STIGs.

**Fix ID:**  F-24289r493799_fix

**Vulnerability ID:**  V-222630

**Rule ID:**  SV-222630r961863_rule

---

## Access privileges to the Configuration Management (CM) repository must be reviewed every three months.

<span style="color:#ff8c00;font-size:150%;">Medium Severity</span>

### Description

A Configuration Management (CM) repository is used to manage application code versions and to securely store application code.

Incorrect access privileges to the CM repository can lead to malicious code or unintentional code being introduced into the application.

This requirement is intended to be applied to application developers or organizations responsible for code management or who have and operate an application CM repository.

### Check Text

Review the application system documentation.

Interview the application administrator.

Identify if development of the application is done in house and if application configuration management repository exists.

If application development is not done in house and if a code configuration management repository does not exist, the requirement is not applicable.

Review CM management processes and procedures.

Verify the CM repository access permissions are reviewed at least every three months.

Ask the application administrator or the CM administrator when the last time the CM access privileges were reviewed.

If CM access privileges have not been reviewed within the last three months, this is a finding.

**Check ID:**  C-24301r493801_chk

### Fix Text 

Review access privileges to the CM repository at least every three months.

**Fix ID:**  F-24290r493802_fix

**Vulnerability ID:**  V-222631

**Rule ID:**  SV-222631r961863_rule

---

## A Software Configuration Management (SCM) plan describing the configuration control and change management process of application objects developed by the organization and the roles and responsibilities of the organization must be created and maintained.

<span style="color:#ff8c00;font-size:150%;">Medium Severity</span>

### Description

Software Configuration Management (SCM) is very important in tracking code releases, baselines, and managing access to the configuration management repository. The SCM plan identifies what should be under configuration management control.

Without an SCM plan that addresses code security issues, code releases can be tracked and vulnerabilities can be inserted intentionally or unintentionally into the code base of the application.

This requirement is intended to be applied to application developers or organizations responsible for code management or who have and operate an application configuration management repository (CMR).

The SCM plan identifies all objects created during the development process subject to configuration control.

The SCM plan maintains procedures for identifying individual application components, as well as, entire application releases during all phases of the software development lifecycle.

The SCM plan identifies and tracks all actions and changes resulting from a change request from initiation to release.

The SCM plan contains procedures to identify, document, review, and authorize any change requests to the application.

The SCM plan defines the responsibilities, the actions to be performed, the tools, techniques and methodologies, and defines an initial set of baselined software components.

The SCM plan objects have security classifications labels.

The SCM plan identifies tools and version numbers used in the software development lifecycle.

The SCM plan identifies mechanisms for controlled access of simultaneous individuals updating the same application component.

The SCM plan assures only authorized changes by authorized persons are possible.

The SCM plan identifies mechanisms to control access and audit changes between different versions of objects subject to configuration control.

The SCM plan identifies mechanisms to track and audit all modifications of objects under configuration control.  Audits include the originator and date and time of the modification.

The SCM plan should contain the following:

- Description of the configuration control and change management process
- Types of objects developed
- Roles and responsibilities of the organization

The SCM plan should also contain the following:

- Defined responsibilities
- Actions to be performed
- Tools used in the process
- Techniques and methodologies
- Initial set of baselined software components

The SCM plan should identify all objects that are under configuration management control.

The SCM plan should identify third-party tools and respective version numbers.

The SCM plan should identify mechanisms for controlled access of individuals simultaneously updating the same application component.

The SCM plan assures only authorized changes by authorized persons are allowed.

The SCM plan should identify mechanisms to control access and audit changes between different versions of objects subject to configuration control.

The SCM plan should have procedures for label versions of application components and application builds under configuration management control.

The configuration management repository (CMR) should track change requests from beginning to end.

The configuration management repository (CMR) should authorize change requests to the application.
 
The configuration management repository (CMR) should contain security classification labels for code and documentation in the repository. Classification labels are not applicable to unclassified systems.

The configuration management repository (CMR) should monitor all objects under CMR control for auditing.

### Check Text

Interview ISSM or application administrator.

Identify if development of the application is done in house and if application configuration management repository exists.

If application development is not done in house and if a code configuration management repository does not exist, the requirement is not applicable.

Verify the SCM plan identifies all objects created during the development process subject to configuration control.

Verify the SCM plan maintains procedures for identifying individual application components, as well as, entire application releases during all phases of the software development lifecycle.

Verify the SCM plan identifies and tracks all actions and changes resulting from a change request from initiation to release.

Verify the SCM plan contains procedures to identify, document, review, and authorize any change requests to the application.

Verify the SCM plan defines the responsibilities, the actions to be performed, the tools, techniques and methodologies, and defines an initial set of base-lined software components.

Verify the SCM plan objects have security classifications labels if processing classified data.

Verify the SCM plan identifies tools and version numbers used in the software development lifecycle.

Verify the SCM plan identifies mechanisms for controlled access of simultaneous individuals updating the same application component.

Verify the SCM plan assures only authorized changes by authorized persons are possible.

Verify the SCM plan identifies mechanisms to control access and audit changes between different versions of objects subject to configuration control.

Verify the SCM plan identifies mechanisms to track and audit all modifications of objects under configuration control. Audits will include the originator and date and time of the modification.

Ask the application representative to review the applications SCM plan.

The SCM plan should contain the following:

- Description of the configuration control and change management process
- Types of objects developed
- Roles and responsibilities of the organization
- Defined responsibilities
- Actions to be performed
- Tools used in the process
- Techniques and methodologies
- Initial set of baselined software components

If the SCM plan does not include the above, this is a finding.

The SCM plan should identify all objects that are under configuration management control. Ask the application representative to provide access to the CMR and to identify the objects shown in the SCM plan.

If the application representative cannot display all types of objects under CMR control, this is a finding.

The SCM plan should identify third-party tools and respective version numbers.

If the SCM plan does not identify third-party tools, this is a finding.

The SCM plan should identify mechanisms for controlled access of individuals simultaneously updating the same application component.

If the SCM plan does not identify mechanisms for controlled access, this is a finding.

The SCM plan assures only authorized changes by authorized persons are allowed.

If the SCM plan does not assure only authorized changes are made, this is a finding.

The SCM plan should identify the mechanisms used to control access and audit changes between different versions of objects subject to CMR control.

If the SCM plan does not identify mechanisms used to control access and to audit changes between different versions of objects subject to CMR control, this is a finding.

The SCM plan should have procedures for label versions of application components and application builds under configuration management control. Ask the application representative to demonstrate the CMR and ensure it contains versions and releases of the application. Ask the application representative to create a build or demonstrate a current release of the application that can be recreated.

If the application representative cannot display releases and application component versions, this is a finding.

The CMR should track change requests from beginning to end. Ask the application representative to display a completed or in-process change request.

If the CMR cannot track change requests, this is a finding.

If the application has just completed its first release, there may not be any change requests logged in the CMR.  In this case, this finding is not applicable.

The CMR should authorize change requests to the application. Ask the application representative to display an authorized change request and identify who is responsible for authorizing change requests.

If the CMR does not track authorized change requests, this is a finding.

If the application has just completed its first release, there may not be any change requests logged in the CMR. In this case, this finding is not applicable.

The CMR should contain security classification labels for code and documentation in the repository. 

Classification labels are not applicable to unclassified systems.  If the applications managed by the CMR are not classified, this requirement is not applicable.

If the CMR manages classified applications and there are no classification labels of code and documentation in the CMR, this is a finding.

The CMR should audit all objects under CM control for modification.

If the CMR does not audit for modifications, this is a finding.

**Check ID:**  C-24302r493804_chk

### Fix Text 

Create and update a SCM plan describing the configuration control and change management process of application objects developed by the organization and the roles and responsibilities of the organization.  Configure CMR to comply.

**Fix ID:**  F-24291r493805_fix

**Vulnerability ID:**  V-222632

**Rule ID:**  SV-222632r961863_rule

---

## A Configuration Control Board (CCB) that meets at least every release cycle, for managing the Configuration Management (CM) process must be established.

<span style="color:#ff8c00;font-size:150%;">Medium Severity</span>

### Description

Software Configuration Management (SCM) is very important in tracking code releases, baselines, and managing access to the configuration management repository. An SCM plan or charter identifies what should be under configuration management control. Without an SCM plan and a CCB, application releases can't be tracked and vulnerabilities can be inserted intentionally or unintentionally into the code base of the application.

This requirement is intended to be applied to application developers or organizations responsible for code management or who have and operate an application CM repository.

### Check Text

Interview the application representative and determine if application development is performed on site by the organization.

If application development is not done in house, the requirement is not applicable.

If so, determine if a CCB exists. Ask about the membership of the CCB, and identify the primary members. Ask if there is CCB charter documentation.

Interview the application representative and determine how often the CCB meets.

Ask if there is CCB charter documentation. The CCB charter documentation should indicate how often the CCB meets.

If there is no charter documentation, ask when the last time the CCB met and when was the last release of the application.

CCBs do not have to physically meet, and the CCB chair may authorize a release based on phone and/or e-mail conversations.

If there is no evidence of CCB activity or meetings prior to the last release cycle, this is a finding.

**Check ID:**  C-24303r493807_chk

### Fix Text 

Setup and maintain a Configuration Control Board.

**Fix ID:**  F-24292r493808_fix

**Vulnerability ID:**  V-222633

**Rule ID:**  SV-222633r961863_rule

---

## The application services and interfaces must be compatible with and ready for IPv6 networks.

<span style="color:#ff8c00;font-size:150%;">Medium Severity</span>

### Description

If the application has not been upgraded to execute on an IPv6-only network, there is a possibility the application will not execute properly, and as a result, a denial of service could occur.

In order to operate on an IPV6 network, the application must be capable of making IPV6 compatible network socket calls.

### Check Text

Verify the application environment is compliant with all DoD IPv6 Standards Profile for IPv6 Capable Products guidance for servers.

If the application environment is not compliant with all DoD IPv6 Standards Profile for IPv6 Capable Products guidance for servers, this is a finding.

**Check ID:**  C-24304r493810_chk

### Fix Text 

Design application to be compliant with all Department of Defense (DoD) Information Technology Standards Registry (DISR) IPv6 profiles.

**Fix ID:**  F-24293r493811_fix

**Vulnerability ID:**  V-222634

**Rule ID:**  SV-222634r987685_rule

---

## The application must not be hosted on a general purpose machine if the application is designated as critical or high availability by the ISSO.

<span style="color:#ff8c00;font-size:150%;">Medium Severity</span>

### Description

Critical applications should not be hosted on a multi-purpose server with other applications. Applications that share resources are susceptible to the other shared application security defects. Even if the critical application is designed and deployed securely, an application that is not designed and deployed securely, can cause resource issues and possibly crash effecting the critical application.

### Check Text

Ask the application representative to review the servers where the application is deployed. 

Ask what other applications are deployed on those servers.

Identify the criticality of the applications installed on the system.

If a mission critical application is deployed onto the same server as non-mission critical applications, this is a finding.

**Check ID:**  C-24305r493813_chk

### Fix Text 

Deploy mission critical applications on servers that are not shared by other less critical applications.

**Fix ID:**  F-24294r493814_fix

**Vulnerability ID:**  V-222635

**Rule ID:**  SV-222635r961863_rule

---

## A contingency plan must exist in accordance with DOD policy based on the application's availability requirements.

<span style="color:#ff8c00;font-size:150%;">Medium Severity</span>

### Description

Contingency planning for systems is part of an overall program for achieving continuity of operations for organizational mission and business functions. Contingency planning addresses system restoration and implementation of alternative mission or business processes when systems are compromised or breached. 

All applications must document procedures to include business recovery plans, system contingency plans, facility disaster recovery plans, and plan acceptance.

### Check Text

Review contingency plans.

For high availability applications, verify the contingency plan exists and provides for the smooth transfer of all mission or business essential functions to an alternate site for the duration of an event with little or no loss of operational continuity.
 
For moderate availability applications, verify the contingency plan exists and provides for the resumption of mission or business essential functions within 12 hours activation or as defined in the contingency plan.

For low availability applications, verify the contingency plan exists and provides for the partial resumption of mission or business essential functions within 5 to 30 days of activation as defined in the contingency plan.
 
If the contingency plan does not exist or does not meet the severity level requirements, this is a finding.

**Check ID:**  C-24306r1051323_chk

### Fix Text 

Create and maintain a contingency plan that identifies essential mission and business functions and associated contingency requirements.

**Fix ID:**  F-24295r1051274_fix

**Vulnerability ID:**  V-222636

**Rule ID:**  SV-222636r1051323_rule

---

## Recovery procedures and technical system features must exist so recovery is performed in a secure and verifiable manner. The ISSO will document circumstances inhibiting a trusted recovery.

<span style="color:#ff8c00;font-size:150%;">Medium Severity</span>

### Description

Without a disaster recovery plan, the application is susceptible to interruption in service due to damage within the processing site.

If the application is part of the site’s disaster recovery plan, ensure that the plan contains detailed instructions pertaining to the application. Verify that recovery procedures indicate the steps needed for secure and trusted recovery.

### Check Text

Review disaster recovery plan.

Verify that a disaster recovery plan is in place for the application.

Verify that the recovery procedures include any special considerations for trusted recovery.

If the application is not part of the site’s disaster recovery plan, or if any special considerations for trusted recovery are not documented, this is a finding.

**Check ID:**  C-24307r493819_chk

### Fix Text 

Create and maintain a disaster recovery plan.

**Fix ID:**  F-24296r493820_fix

**Vulnerability ID:**  V-222637

**Rule ID:**  SV-222637r961863_rule

---

## Data backup must be performed at required intervals in accordance with DoD policy.

<span style="color:#ff8c00;font-size:150%;">Medium Severity</span>

### Description

Without proper backups, the application is not protected from the loss of data or the operating environment in the event of hardware or software failure.

### Check Text

Interview the application and system admins and review documented backup procedures.

Check the following based on the risk level of the application.

For low risk applications:

Validate backup procedures exist and are performed at least weekly.

A sampling of system backups should be checked to ensure compliance with the control.

For medium risk applications:

Validate backup procedures exist and are performed at least daily.

Validate recovery media is stored at an off-site location and ensure the data is protected in accordance with its risk category and confidentiality level. This validation can be performed by examining an SLA or MOU/MOA that states the protection levels of the data and how it should be stored.

A sampling of system backups should be checked to ensure compliance with the control.

Verify that the organization tests backup information to ensure media reliability and information integrity.

Verify that the organization selectively uses backup information in the restoration of information system functions as part of annual contingency plan testing.

For high risk applications:

Validate that the procedures have been defined for system redundancy and they are properly implemented and are executing the procedures.

Verify that the redundant system is properly separated from the primary system (i.e., located in a different building or in a different city). This validation should be performed by examining the secondary system and ensuring its operation.

Examine the SLA or MOU/MOA to ensure redundant capability is addressed. Finding details should indicate the type of validation performed. Examine the mirror capability testing procedures and results to insure the capability is properly tested at 6 month minimum intervals.

If any of the requirements above for the associated risk level of the application are not met, this is a finding.

**Check ID:**  C-24308r493822_chk

### Fix Text 

Develop and implement backup procedures based on risk level of the system and in accordance with DoD policy.

**Fix ID:**  F-24297r493823_fix

**Vulnerability ID:**  V-222638

**Rule ID:**  SV-222638r961863_rule

---

## Back-up copies of the application software or source code must be stored in a fire-rated container or stored separately (offsite).

<span style="color:#ff8c00;font-size:150%;">Medium Severity</span>

### Description

Application developers and application administrators must take steps to ensure continuity of development effort and operations should a disaster strike.  

Steps include protecting back-up copies of development code and application software.

Improper storage of the back-up copies can result in extended outages of the information system in the event of a fire or other situation that results in destruction of the back-up as well as the operating copy.

To address this risk, copies of application software and application source code must be stored in a fire-rated container or separately (offsite) from the operational or development environments.

### Check Text

When reviewing a COTS or GOTS application, verify that a back-up copy of the software is stored in a fire rated container or is stored separately (offsite) from the operational environment.

Determine if application development is done in-house. 

If application development occurs in-house and source code is available, verify a back-up copy of the source code is kept in a fire-rated container or stored offsite from the development environment.

If back-up copies of the application software or source code are not stored in a fire-rated container or stored separately (offsite) from their respective environments, this is a finding.

**Check ID:**  C-24309r493825_chk

### Fix Text 

Store a back-up copy of the application software and source code in a fire-rated container or store it separately (offsite) from their respective environments.

**Fix ID:**  F-24298r493826_fix

**Vulnerability ID:**  V-222639

**Rule ID:**  SV-222639r961863_rule

---

## Procedures must be in place to assure the appropriate physical and technical protection of the backup and restoration of the application.

<span style="color:#ff8c00;font-size:150%;">Medium Severity</span>

### Description

Protection of backup and restoration assets is essential for the successful restore of operations after a catastrophic failure or damage to the system or data files. Failure to follow proper procedures may result in the permanent loss of system data and/or the loss of system capability resulting in failure of the customer’s mission.

### Check Text

Validate that backup and recovery procedures incorporate protection of the backup and restoration assets.

Verify assets housing the backup data (e.g., SANS, tapes, backup directories, software) and the assets used for restoration (e.g., equipment and system software) are included in the backup and recovery procedures.

If backup and restoration devices are not included in the recovery procedures, this is a finding.

**Check ID:**  C-24310r493828_chk

### Fix Text 

Develop and implement procedures to insure that backup and restoration assets are properly protected and stored in an area/location where it is unlikely they would be affected by an event that would affect the primary assets.

**Fix ID:**  F-24299r493829_fix

**Vulnerability ID:**  V-222640

**Rule ID:**  SV-222640r961863_rule

---

## The application must use encryption to implement key exchange and authenticate endpoints prior to establishing a communication channel for key exchange.

<span style="color:#ff8c00;font-size:150%;">Medium Severity</span>

### Description

If the application does not use encryption and authenticate endpoints prior to establishing a communication channel and prior to transmitting encryption keys, these keys may be intercepted, and could be used to decrypt the traffic of the current session, leading to potential loss or compromise of DoD data.

### Check Text

If the application does not implement key exchange, this check is not applicable.

Identify all application or supporting infrastructure features using key exchange.

Verify the application is using FIPS-140-2 validated cryptographic modules for encryption of keys during key exchange.

If the application does not implement encryption for key exchange, this is a finding.

**Check ID:**  C-24311r493831_chk

### Fix Text 

Use encryption for key exchange.

**Fix ID:**  F-24300r493832_fix

**Vulnerability ID:**  V-222641

**Rule ID:**  SV-222641r961863_rule

---

## The application must not contain embedded authentication data.

<span style="color:#ff0000;font-size:150%;">High Severity</span>

### Description

Authentication data stored in code could potentially be read and used by anonymous users to gain access to a backend database or application servers. This could lead to compromise of application data.

### Check Text

Review the application documentation and any available source code; this includes configuration files such as global.asa, if present, scripts, HTML files, and any ASCII files.

Identify any instances of passwords, certificates, or sensitive data included in code.

If credentials were found, check the file permissions and ownership of the offending file.

If access to the folder hosting the file is not restricted to the related application process and administrative users, this is a finding.

The finding details should note specifically where the offending credentials or data were located and what resources they enabled.

**Check ID:**  C-24312r493834_chk

### Fix Text 

Remove embedded authentication data stored in code, configuration files, scripts, HTML file, or any ASCII files.

**Fix ID:**  F-24301r493835_fix

**Vulnerability ID:**  V-222642

**Rule ID:**  SV-222642r961863_rule

---

## The application must have the capability to mark sensitive/classified output when required.

<span style="color:#ff0000;font-size:150%;">High Severity</span>

### Description

Failure to properly mark output could result in a disclosure of sensitive or classified data which is an immediate loss in confidentiality.

### Check Text

Review the application documentation and interview the application administrator.

Ask the application representative for the application’s classification guide. This guide should document the data elements and their classification.

Determine which application functions to examine, giving preference to report generation capabilities and the most common user transactions that involve sensitive data (FOUO, secret or above).

Log on to the application and perform these in sequence, printing output when applicable. The application representative’s assistance may be required to perform these steps. For each function, note whether the appropriate markings appear on the displayed and printed output. If a classification document does not exist, data must be marked at the highest classification of the system.

Appropriate markings for an application are as follows: For classified data, markings are required at a minimum at the top and the bottom of screens and reports.

For FOUO data, markings are required at a minimum of the bottom of the screen or report. In some cases, technology may prohibit the appropriate markings on printed documents. For example, in some cases, it is not possible to mark all pages top and bottom when a user prints from a browser. If this is the case, ask the application representative if user procedures exist for manually marking printed documents. If procedures do exist, examine the procedures to verify if the users were to follow the procedures the data would be marked correctly.

Ask how these procedures are distributed to the users.

If appropriate markings are not present within the application and it is technically possible to have the markings present, this is a finding.

If it is not technically feasible to meet the minimum marking requirement and no user procedures exist or if followed the procedures will result in incorrect markings, or the procedures are not readily available to users, this is a finding.

In any case of a finding, the finding details should specify which functions failed to produce the desired results.

After completing the test, destroy all printed output using the site’s preferred method for disposal. For example: utilizing a shredder or disposal in burn bags.

**Check ID:**  C-24313r493837_chk

### Fix Text 

Enable the application to adequately mark sensitive/classified output.

**Fix ID:**  F-24302r493838_fix

**Vulnerability ID:**  V-222643

**Rule ID:**  SV-222643r961863_rule

---

## Prior to each release of the application, updates to system, or applying patches; tests plans and procedures must be created and executed.

<span style="color:#b3b31a;font-size:150%;">Low Severity</span>

### Description

Without test plans and procedures for application releases or updates, unexpected results may occur which could lead to a denial of service to the application or components.

This requirement is meant to apply to developers or organizations that are doing development work when releasing a version update or a patch to the application.

### Check Text

If the review is not being done with the developer of the application, this requirement is not applicable.

Ask the application representative to provide tests plans, procedures, and results to ensure they are updated for each application release or updates to system patches.

If test plans, procedures, and results do not exist, or are not updated for each application release, this is a finding.

**Check ID:**  C-24314r493840_chk

### Fix Text 

Execute tests plans prior to release or patch update.

**Fix ID:**  F-24303r493841_fix

**Vulnerability ID:**  V-222644

**Rule ID:**  SV-222644r961863_rule

---

## Application files must be cryptographically hashed prior to deploying to DoD operational networks.

<span style="color:#ff8c00;font-size:150%;">Medium Severity</span>

### Description

When application code and binaries are transferred from one environment to another, there is the potential for malware to be introduced into either the application code or even the application binaries themselves. Care must be taken to ensure that application code and binaries are validated for integrity prior to deployment into a production environment.

To ensure file integrity, application files and/or application packages are cryptographically hashed using a strong hashing algorithm. Comparing hashes after transferring the files makes it possible to detect changes in files that could indicate potential integrity issues with the application.

Currently, SHA256 is the DoD approved standard for cryptographic hash functions. DoD application developers must use SHA256 when creating cryptographic hashes; however, some non-DoD vendors might still use MD5 or SHA1 when generating a checksum hash for their application packages. It is important to use the same algorithms when validating the hash. If a non DoD vendor uses SHA1 when hashing their files, you must use SHA1 to validate the hash. Otherwise, the hashes will not match and a false positive indication of tampering will result.

Prior to release of the application receiving an ATO/IATO for deployment into a DoD operational network, the application must be validated for integrity to ensure no tampering of source code or binaries has occurred. Failure to validate the integrity of application code and/or application binaries prior to deploying an application into a production environment may compromise the operational network.

### Check Text

Ask the application representative to demonstrate their cryptographic hash validation process or provide process documentation. The validation process will vary based upon the operating system used as there are numerous clients available that will display a file's cryptographic hash for validation purposes.

Linux operating systems include the "sha256sum" utility. For Linux systems using sha256sum command syntax is: sha256sum [OPTION]... [FILE]...

Recent Windows PowerShell versions include the "get-filehash" PowerShell cmdlet. The default algorithm value used is SHA256.

Syntax is: 
Get-FileHash
[-Path] <String[]>
[-Algorithm <String>]
[<CommonParameters>] 

A validation process involves obtaining the application files’ cryptographic hash value from the programs author or other authoritative source such as the application's website. A utility like the "sha256sum" utility is then run using the downloaded application file name as the argument. The output is the files' hash value. The two hash values are compared and if they match, then file integrity is ensured.

If the application being reviewed is a COTS product and the vendor used a SHA1 or MD5 algorithm to generate a hash value, this is not a finding.

If the application being reviewed is a COTS product and the vendor did not provide a hash value for validating the package, this is not a finding.

If the integrity of the application files/code is not validated prior to deployment to DoD operational networks, this is a finding.

**Check ID:**  C-36256r602331_chk

### Fix Text 

Developers/release managers create cryptographic hash values of application files and/or application packages prior to transitioning the application from test to a production environment. They protect cryptographic hash information so it cannot be altered and make a read copy of the hash information available to application Admins so they can validate application packages and files after they download the files.

Application Admins validate cryptographic hashes prior to deploying the application to production.

**Fix ID:**  F-36220r602332_fix

**Vulnerability ID:**  V-222645

**Rule ID:**  SV-222645r961863_rule

---

## At least one tester must be designated to test for security flaws in addition to functional testing.

<span style="color:#ff8c00;font-size:150%;">Medium Severity</span>

### Description

If there is no person designated to test for security flaws, vulnerabilities can potentially be missed during testing.

This requirement is meant to apply to developers or organizations that are doing development work.

### Check Text

Review the organization chart and interview the admin staff.

Identify personnel designated as application security testers.

If the organization operating the application is not doing development work, this requirement is not applicable.

If the organization has not designated personnel to conduct security testing, this is a finding.

**Check ID:**  C-24316r493846_chk

### Fix Text 

Designate personnel to conduct security testing on the applications.

**Fix ID:**  F-24305r493847_fix

**Vulnerability ID:**  V-222646

**Rule ID:**  SV-222646r961863_rule

---

## Test procedures must be created and at least annually executed to ensure system initialization, shutdown, and aborts are configured to verify the system remains in a secure state.

<span style="color:#b3b31a;font-size:150%;">Low Severity</span>

### Description

Secure state assurance cannot be accomplished without testing the system state at least annually to ensure the system remains in a secure state upon initialization, shutdown, and aborts.

### Check Text

Review the process documentation and interview the admin staff.

Identify if testing procedures exist and if they include annual testing to ensure the application remains in a secure state on initialization, shutdown, and aborts.

Checks should include at a minimum, attempts to access the application and application configuration settings without credentials or with improper credentials both locally and remotely.

Dates should be noted as to the last date of testing.

If annual testing procedures do not exist, or if administrators are unable to provide testing dates that indicate the tests were conducted within the last year, this is a finding.

**Check ID:**  C-24317r493849_chk

### Fix Text 

Create test procedures to test the security state of the application and exercise test procedures annually.

**Fix ID:**  F-24306r493850_fix

**Vulnerability ID:**  V-222647

**Rule ID:**  SV-222647r961863_rule

---

## An application code review must be performed on the application.

<span style="color:#ff8c00;font-size:150%;">Medium Severity</span>

### Description

A code review is a systematic evaluation of computer source code conducted for the purposes of identifying and remediating the security flaws in the software.

This requirement is meant to apply to developers or organizations that are doing application development work and have the responsibility for maintaining the application source code.

Examples of security flaws include but are not limited to:

- format string exploits
- memory leaks 
- buffer overflows 
- race conditions
- sql injection
- dead/unused/commented code
- input validation exploits

The code review is conducted during the application development phase, this allows discovered security issues to be corrected prior to release.

Code reviews performed after the development phase must eventually go back to development for correction so conducting the code review during development is the logical and preferred action.

Automated code review tools are to be used whenever reviewing application source code. These tools are often incorporated into Integrated Development Environments (IDE) so code reviews can be conducted during all stages of the development life cycle. Periodically reviewing code during the development phase makes transition to a production environment easier as flaws are continually identified and addressed during the development phase rather than en masse at the end of the development effort.

Code review processes and the tools used to conduct the code review analysis will vary depending upon application architecture and the development languages utilized.

In addition to automated testing, manual code reviews may also be used to validate or augment automated code review results. Larger projects will have a large code base and will require the use of automated code review tools in order to achieve complete code review coverage.

A manual code review may consist of a peer review wherein other programmers on the team manually examine source code and automated code review results for known flaws that introduce security bugs into the application.

As with any testing, there is no single best approach and the tests must be tailored to the application architecture. Use of automated tools along with manual review of code and testing results is considered a best practice when conducting code reviews. This method is the most likely way to ensure the maximum number of errors are caught and addressed prior to implementing the application in a production environment.

### Check Text

This requirement is meant to apply to developers or organizations that are doing the application development work and have the responsibility for maintaining the application source code.  Otherwise, the requirement is not applicable.

Review the system documentation and ask the application representative to describe the code review process or provide documentation outlining the organizations code review process.

If code reviews are conducted with software tools, have the application representative provide the latest code review report for the application.

Ensure the code review looks for all known security flaws including but not limited to:

- format string exploits
- memory leaks
- buffer overflows
- race conditions
- sql injection
- dead/unused/commented code
- input validation exploits

If the organization does not conduct code reviews on the application that attempt to identify all known and potential security issues, or if code review results are not available for review, this is a finding.

**Check ID:**  C-24318r493852_chk

### Fix Text 

Conduct and document code reviews on the application during development and identify and remediate all known and potential security vulnerabilities prior to releasing the application.

**Fix ID:**  F-24307r493853_fix

**Vulnerability ID:**  V-222648

**Rule ID:**  SV-222648r961863_rule

---

## Code coverage statistics must be maintained for each release of the application.

<span style="color:#b3b31a;font-size:150%;">Low Severity</span>

### Description

This requirement is meant to apply to developers or organizations that are doing application development work.

Code coverage statistics describes the overall functionality provided by the application and how much of the source code has been tested during the release cycle.

To avoid the potential for testing the same pieces of code over and over again, code coverage statistics are used to track which aspects or modules of the application are tested.

Some applications are so large that it is not feasible to test every last bit of the application code on one release cycle. In those instances, it is acceptable to prioritize and identify the modules that are critical to the applications security posture and test those first. Rolling over to test other modules later as resources permit. E.g., testing functionality that performs authentication and authorization before testing printing capabilities.

Application developers should keep statistics that show all of the modules of the application and identify which modules were tested and when. This will help testers to keep track of what has been tested and help to verify all functionality is tested.

The developer makes sure that flaws are documented in a defect tracking system.

If the application is smaller in nature and all aspects of the application can be tested, the code coverage statistics would be 100%.

### Check Text

If the organization does not do or manage the application development work for the application, this requirement is not applicable.

Ask the application representative to provide code coverage statistics maintained for the application.

If these code coverage statistics do not exist, this is a finding.

**Check ID:**  C-24319r493855_chk

### Fix Text 

Track application testing and maintain statistics that show how much of the application function was tested.

**Fix ID:**  F-24308r493856_fix

**Vulnerability ID:**  V-222649

**Rule ID:**  SV-222649r961863_rule

---

## Flaws found during a code review must be tracked in a defect tracking system.

<span style="color:#ff8c00;font-size:150%;">Medium Severity</span>

### Description

This requirement is meant to apply to developers or organizations that are doing application development work.

If flaws are not tracked they may possibly be forgotten to be included in a release. Tracking flaws in the configuration management repository will help identify code elements to be changed, as well as the requested change.

### Check Text

This requirement is meant to apply to developers or organizations that are doing application development work.

If application development is not being done or managed by the organization, this requirement is not applicable.

Ask the application representative to demonstrate that the configuration management repository captures flaws in the code review process. The configuration management repository may consist of a separate application for capturing code defects.

If there is no configuration management repository or the code review flaws are not captured in the configuration management repository, this is a finding.

**Check ID:**  C-24320r493858_chk

### Fix Text 

Track software defects in a defect tracking system.

**Fix ID:**  F-24309r493859_fix

**Vulnerability ID:**  V-222650

**Rule ID:**  SV-222650r961863_rule

---

## The changes to the application must be assessed for IA and accreditation impact prior to implementation.

<span style="color:#ff8c00;font-size:150%;">Medium Severity</span>

### Description

When changes are made to an application, either in the code or in the configuration of underlying components such as the OS or the web or application server, there is the potential for security vulnerabilities to be opened up on the system.

IA assessment of proposed changes is necessary to verify security integrity is maintained within the application.

### Check Text

Interview the application and system administrators and determine if changes to the application are assessed for IA impact prior to implementation.

Review the CCB process documentation to ensure potential changes to the application are evaluated to determine impact. An informal group may be tasked with impact assessment of upcoming version changes.

If IA impact analysis is not performed, this is a finding.

**Check ID:**  C-24321r493861_chk

### Fix Text 

Review IA impact to the system prior to implementing changes.

**Fix ID:**  F-24310r493862_fix

**Vulnerability ID:**  V-222651

**Rule ID:**  SV-222651r961863_rule

---

## Security flaws must be fixed or addressed in the project plan.

<span style="color:#ff8c00;font-size:150%;">Medium Severity</span>

### Description

This requirement is meant to apply to developers or organizations that are doing application development work.

Application development efforts include the creation of a project plan to track and organize the development work.

If security flaws are not tracked within the project plan, it is possible the flaws will be overlooked and included in a release.

Tracking flaws in the project plan will help identify code elements to be changed as well as the requested change.

### Check Text

This requirement is meant to apply to developers or organizations that are doing application development work. If the organization managing the application is not performing or managing the development of the application the requirement is not applicable.

Ask the application representative to demonstrate how security flaws are integrated into the project plan.

If security flaws are not addressed in the project plan or there is no process to introduce security flaws into the project plan, this is a finding.

**Check ID:**  C-24322r493864_chk

### Fix Text 

Address security flaws within a project plan to ensure they are tracked and addressed by management.

**Fix ID:**  F-24311r493865_fix

**Vulnerability ID:**  V-222652

**Rule ID:**  SV-222652r961863_rule

---

## The application development team must follow a set of coding standards.

<span style="color:#b3b31a;font-size:150%;">Low Severity</span>

### Description

Coding standards are guidelines established by the development team or individual developers that recommend programming style, practices and methods.  The coding standards employed will vary based upon the programming language that is being used to develop the application and the development team.

Coding standards often cover the use of white space characters, variable naming conventions, function naming conventions, and comment styles.  Implementing coding standards provides many benefits to the development process.  These benefits include code readability, coding consistency among both individual and teams of developers as well as ease of code integration.  

The following are examples of what will typically be in a coding standards document.  This list is an example of what one can expect to find in typical coding standard documents and is not a comprehensive list:

- Indent style conventions
- Naming conventions
- Line length conventions
- Comment conventions
- Programming best practices
- Programming style conventions

Coding standards allow developers to quickly adapt to code which has been developed by various members of a development team.  Coding standards are useful in the code review process as well as in situations where a team member leaves and duties must then be assigned to another team member.  

Code conforming to a standard format is easier to read, especially if someone other than the original developer is examining the code.  In addition, formatted code can be debugged and corrected faster than unformatted code.

Introducing coding standards can help increase the consistency, reliability, and security of the application by ensuring common programming structures and tasks are handled by similar methods, as well as, reducing the occurrence of common logic errors.

### Check Text

This requirement is meant to apply to developers or organizations that are doing application development work. If the organization operating the application under review is not doing the development or managing the development of the application, the requirement is not applicable.

Ask the application representative about their coding standards. Ask for a coding standards document, review the document and ask the developers if they are aware of and if they use the coding standards. Make a determination if the application developers follow the coding standard. 

If the developers do not follow a coding standard, or if a coding standard document does not exist, this is a finding.

**Check ID:**  C-36257r602334_chk

### Fix Text 

Create and maintain a coding standard process and documentation for developers to follow. 

Include programming best practices based on the languages being used for application development. Include items that should be standardized across the team that deals with how developers write their application code.

**Fix ID:**  F-36221r864580_fix

**Vulnerability ID:**  V-222653

**Rule ID:**  SV-222653r961863_rule

---

## The designer must create and update the Design Document for each release of the application.

<span style="color:#b3b31a;font-size:150%;">Low Severity</span>

### Description

This requirement is meant to apply to developers or organizations that are doing application development work.

The application design document or configuration guide includes configuration settings, recommendations and best practices that pertain to the secure deployment of the application.

It also contains the detailed functional architecture as well as any changes to the application architecture corresponding to a new version release and must be documented to ensure all risks are assessed and mitigated to the maximum extent practical.

Failure to do so may result in unexposed risk, and failure to mitigate the risk leading to failure or compromise of the system.

### Check Text

This requirement is meant to apply to developers or organizations that are doing application development work. If the organization operating the application is not doing the development or managing the development of the application, the requirement is not applicable.

Ask the application representative for the design document for the application. Review the design document.

Examine the design document and/or the threat model for the application and verify the following information is documented:

- All external interfaces.
- The nature of information being exchanged
- Any protections on the external interface
- User roles required for access control and the access privileges assigned to each role
- Unique security requirements (e.g., encryption of key data elements at rest)
- Categories of sensitive information processed by the application and their specific protection plans (e.g., PII, HIPAA).
- Restoration priority of subsystems, processes, or information
- Verify the organization includes documentation describing the design and implementation details of the security controls employed within the information system with sufficient detail
- Application incident response plan that provides details on how to provide the development team with application vulnerability or bug information.

If the design document is incomplete, this is a finding.

**Check ID:**  C-36258r602337_chk

### Fix Text 

Create and maintain the Design Document for each release of the application and identify the following:

- All external interfaces (from the threat model)
- The nature of information being exchanged
- Categories of sensitive information processed or stored and their specific protection plans
- The protection mechanisms associated with each interface
- User roles required for access control
- Access privileges assigned to each role
- Unique application security requirements
- Categories of sensitive information processed or stored and specific protection plans (e.g., Privacy Act, HIPAA, etc.)
- Restoration priority of subsystems, processes, or information.

**Fix ID:**  F-36222r864581_fix

**Vulnerability ID:**  V-222654

**Rule ID:**  SV-222654r961863_rule

---

## Threat models must be documented and reviewed for each application release and updated as required by design and functionality changes or when new threats are discovered.

<span style="color:#ff8c00;font-size:150%;">Medium Severity</span>

### Description

Threat modeling is an approach for analyzing the security of an application. It is a structured approach that enables you to identify, quantify, and address the security risks associated with an application. Threat modeling is not an approach to reviewing code, but it does complement the security code review process.

Threat modeling can optimize application security by identifying objectives and vulnerabilities, and then defining countermeasures to prevent, or mitigate the effects of, threats to the system.

The lack of threat modeling will potentially leave unidentified threats for attackers to utilize to gain access to the application. To execute a threat model you should do the following:

- Decompose the Application. The first step in the threat modeling process is gaining an understanding of the application and how it interacts with external entities. This includes identifying application components such as web server, application server, database server and languages used by the application. It also includes identifying network connections and the means utilized to access the application.

- Determine and rank threats. Use a threat categorization methodology to understand the different threat categories.
E.g., Auditing, authentication, configuration management and data protection. The goal of the threat categorization is to help identify threats both from the attacker perspective and the defensive perspective.

- Determine countermeasures and mitigation. A lack of protection against a threat might indicate a vulnerability whose risk exposure could be mitigated with the implementation of a countermeasure.

Countermeasures could include using application firewalls, IDS/IPS to block or identify known attacks against the architecture and alarming on audit log events.

Refer to the OWASP website for additional details on application threat modeling.

https://www.owasp.org/index.php/Application_Threat_Modeling

### Check Text

This requirement is meant to apply to developers or organizations that are doing application development work.

If the organization operating the application is not doing the development or is not managing the development of the application, the requirement is not applicable.

Review the threat model document and identify the following sections are present:

- Identified threats
- Potential vulnerabilities
- Counter measures taken
- Potential mitigations
- Mitigations selected based on risk analysis

Review the identified threats, vulnerabilities, and countermeasures.
Countermeasures could include implementing application firewalls or IDS/IPS and configuring certain IDS filters.

Review the application documentation.
Verify the architecture and components of the application match with the components in the threat model document.
Verify identified threats and vulnerabilities are addressed or mitigated and the ISSO and ISSM have reviewed and approved the document.

If the described threat model documentation does not exist, this is a finding.

**Check ID:**  C-24325r493873_chk

### Fix Text 

Establish and maintain threat models and review for each application release and when new threats are discovered. Identify potential mitigations to identified threats. Verify mitigations are implemented to threats based on their risk analysis.

**Fix ID:**  F-24314r493874_fix

**Vulnerability ID:**  V-222655

**Rule ID:**  SV-222655r961863_rule

---

## The application must not be subject to error handling vulnerabilities.

<span style="color:#ff8c00;font-size:150%;">Medium Severity</span>

### Description

Error handling is the failure to check the return values of functions or catch top level exceptions within a program. Improper error handling in an application can lead to an application failure or possibly result in the application entering an insecure state. 

The primary way to detect error handling vulnerabilities is to perform code reviews. If a manual code review cannot be performed, static code analysis tools should be employed in conjunction with tests to help force the error conditions by specifying invalid input (such as fuzzed data and malformed filenames) and by using different accounts to run the application. These tests may give indications of vulnerability, but they are not comprehensive.

In order to minimize error handling errors, ensure proper return code and exception handling is implemented throughout the application.

### Check Text

Review the application documentation, code review reports and the results from static code analysis tools.

Identify the most recent security scans and code analysis testing conducted.  Verify testing configuration includes tests for error handling issues.

Check test results for identified error handling vulnerabilities within the application.

If the test results indicate the existence of error handling vulnerabilities and no remediation evidence is presented, this is a finding.

If no test results are available for review, this is a finding.

**Check ID:**  C-24326r493876_chk

### Fix Text 

Ensure proper return code and exception handling is implemented throughout the application.

**Fix ID:**  F-24315r493877_fix

**Vulnerability ID:**  V-222656

**Rule ID:**  SV-222656r961863_rule

---

## The application development team must provide an application incident response plan.

<span style="color:#ff8c00;font-size:150%;">Medium Severity</span>

### Description

An application incident response process is managed by the development team and should include a method for individuals to submit potential security vulnerabilities to the development or maintenance team. 

The plan should dictate what is to be done with the reported vulnerabilities. Reported vulnerabilities must be tracked throughout the process to ensure they are triaged, corrected, and tested. The corresponding update is released to the user community and the user community is notified of the availability of the application update.

Without an established application incident management plan and process, discovered issues and vulnerabilities will go unreported.   Vulnerabilities will not be triaged and managed, and there may be delays in corrective actions.

Information on how to submit bug and vulnerability reports must also be included in the application design document or configuration guide.

This requirement is meant to be applied when reviewing an application with the development team.

### Check Text

If the application is a COTS application and the development team is not accessible to interview this requirement is not applicable.

Interview the application development team members. Request and review the application incident response plan. 

Ensure the plan includes an implemented process that:

- Tracks reported vulnerabilities and bugs
- Confirms reported vulnerabilities and bugs
- Tracks remediation effort
- Notifies application users of available updates that address the reported issues.

If the application incident response plan does not exist and at a minimum does not implement the aforementioned processes, this is a finding.


**Check ID:**  C-36259r602340_chk

### Fix Text 

The development team creates an application incident response plan documenting and establishing a process that at a minimum:

- Tracks reported vulnerabilities and bugs
- Confirms reported vulnerabilities and bugs
- Tracks remediation effort
- Notifies application users of available updates that address the reported issues.

**Fix ID:**  F-36223r864582_fix

**Vulnerability ID:**  V-222657

**Rule ID:**  SV-222657r961863_rule

---

## All products must be supported by the vendor or the development team.

<span style="color:#ff0000;font-size:150%;">High Severity</span>

### Description

Unsupported commercial and government developed software products should not be used because fixes to newly identified bugs will not be implemented by the vendor or development team. The lack of security updates can result in potential vulnerabilities.

### Check Text

Review the application documentation and interview the application administrator.

Identify all software components.

Review the version information and identify the vendor if COTS software.

Access the vendor website to verify the version is still supported.

Ask the application representative for proof that the application and all of its components are supported.

Examples of proof may include:

design documentation that includes support information, support specific contract documentation, successful creation of vendor support tickets, website toll free support phone numbers etcetera.

If any of the software components are not supported by a COTS vendor or a GOTS organization, this is a finding.

**Check ID:**  C-24328r493882_chk

### Fix Text 

Remove or decommission all unsupported software products in the application.

**Fix ID:**  F-24317r493883_fix

**Vulnerability ID:**  V-222658

**Rule ID:**  SV-222658r961863_rule

---

## The application must be decommissioned when maintenance or support is no longer available.

<span style="color:#ff0000;font-size:150%;">High Severity</span>

### Description

Unsupported software products should not be used because fixes to newly identified bugs will not be implemented by the vendor or development team. The lack of security updates can result in potential vulnerabilities.

When maintenance updates and patches are no longer available, the application is no longer considered supported, and should be decommissioned.

### Check Text

Interview the application representative and determine if all the application components are under maintenance contract. The entire application may be covered by a single maintenance agreement. The application should be decommissioned if maintenance or security support is no longer being provided by the vendor or by the development staff of a custom developed application.

If the application or any of the application components are not being maintained, this is a finding.

**Check ID:**  C-24329r493885_chk

### Fix Text 

Ensure there is maintenance for the application.

**Fix ID:**  F-24318r493886_fix

**Vulnerability ID:**  V-222659

**Rule ID:**  SV-222659r961863_rule

---

## Procedures must be in place to notify users when an application is decommissioned.

<span style="color:#b3b31a;font-size:150%;">Low Severity</span>

### Description

When maintenance no longer exists for an application, there are no individuals responsible for making security updates. The application support staff should maintain procedures for decommissioning. The decommissioning process should include notifying users of the pending decommissioning event. If the users are not informed of the decommissioning event, attackers may be able to stand up similar looking system and fool users into attempting to log onto a duplicate system. This can be as simple as a banner informing users.

This risk is primarily geared towards insider threat scenarios and externally accessible applications that provide access to publicly releasable data but should also be applied to internal systems as a best practice.

### Check Text

Interview the application representative to determine if provisions are in place to notify users when an application is decommissioned.
 
If provisions are not in place to notify users when an application is decommissioned, this is a finding.

**Check ID:**  C-24330r493888_chk

### Fix Text 

Create and establish procedures to notify users when an application is decommissioned.

**Fix ID:**  F-24319r493889_fix

**Vulnerability ID:**  V-222660

**Rule ID:**  SV-222660r961863_rule

---

## Unnecessary built-in application accounts must be disabled.

<span style="color:#ff8c00;font-size:150%;">Medium Severity</span>

### Description

Default passwords and properties of built-in accounts are often publicly available. Anyone with necessary knowledge, internal or external, can compromise an application using built-in accounts.

Built-in accounts are those that are added as part of the installation of the application software. These accounts exist for many common Commercial Off-the-Shelf (COTS) or open source components of enterprise applications (e.g., OS, web browser or database software).

### Check Text

Review the application documentation and identify if the application creates or utilizes built-in accounts.

Examine the account list for obvious examples (e.g., accounts with vendor names such as Oracle or Tivoli).

Verify that these accounts have been removed or disabled.

If enabled built-in accounts are present, ask the application representative the reason for their existence.

If the account is required in order for the application to operate properly, verify the account password has been changed to a DoD acceptable value.

If these accounts are not necessary to run the application, or if the accounts are required and the password has not been changed to meet DoD password requirements, this is a finding.

**Check ID:**  C-24331r493891_chk

### Fix Text 

Disable unnecessary built-in userids, use other strong authentication when possible and use strong passwords if accounts are necessary for application operation.

**Fix ID:**  F-24320r493892_fix

**Vulnerability ID:**  V-222661

**Rule ID:**  SV-222661r961863_rule

---

## Default passwords must be changed.

<span style="color:#ff0000;font-size:150%;">High Severity</span>

### Description

Default passwords can easily be compromised by attackers allowing immediate access to the applications.

### Check Text

Identify the application name and version and do an Internet search for the product name and the string "default password".

If default passwords are found, attempt to authenticate with the published default passwords.

If authentication is successful, this is a finding.

**Check ID:**  C-24332r493894_chk

### Fix Text 

Configure the application to use strong authenticators instead of passwords when possible. Otherwise, change default passwords to a DoD-approved strength password and follow all guidance for passwords.

**Fix ID:**  F-24321r493895_fix

**Vulnerability ID:**  V-222662

**Rule ID:**  SV-222662r961863_rule

---

## An Application Configuration Guide must be created and included with the application.

<span style="color:#ff8c00;font-size:150%;">Medium Severity</span>

### Description

The Application Configuration Guide is any document or collection of documents used to configure the application.  These documents may be part of a user guide, secure configuration guide, or any guidance that satisfies the requirements provided herein.  

Configuration examples include but are not limited to:

 - Encryption Settings
 - PKI Certificate Configuration Settings
 - Password Settings
 - Auditing configuration
 - AD configuration
 - Backup and disaster recovery settings
 - List of hosting enclaves and network connection requirements
 - Deployment configuration settings 
 - Known security assumptions, implications, system level protections, best practices, and required permissions

Development systems, build systems, and test systems must operate in a standardized environment. These settings are to be documented in the Application Configuration Guide.

Examples include but are not limited to:

 - List of development systems, build systems, and test systems. 
 - Versions of compilers used
 - Build options when creating applications and components
 - Versions of COTS software (used as part of the application)
 - Operating systems and versions
 - For web applications, which browsers and what versions are supported.
 
All deployment configuration settings are to be documented in the Application Configuration Guide and the Application Configuration Guide must be made available to application hosting providers and application/system administrators.

### Check Text

Interview the application administrator.  Request and review the Application Configuration Guide. 

Verify the configuration guide at a minimum provides configuration details for the following examples.  The examples provided herein are not intended to limit the configuration settings that are documented in the guide.

Configuration examples include but are not limited to:

 - Encryption Settings
 - PKI Certificate Configuration Settings
 - Password Settings
 - Auditing configuration
 - AD configuration
 - Backup and disaster recovery settings
 - List of hosting enclaves and network connection requirements
 - Deployment configuration settings 
 - Known security assumptions, implications, system level protections, best practices, and required permissions

Review the Application Configuration Guide and determine if development systems are documented.  If no development is being performed where the application is hosted, this part of the requirement is NA.

Development systems, build systems, and test systems must operate in a standardized environment.

Examples include but are not limited to:

 - List of development systems, build systems, and test systems. 
 - Versions of compilers used
 - Build options when creating applications and components
 - Versions of COTS software (used as part of the application)
 - Operating systems and versions
 - For web applications, which browsers and what versions are supported.

If there is no application configuration guide included with the application, this is a finding.

**Check ID:**  C-24333r493897_chk

### Fix Text 

Create the application configuration guide in accordance with configuration examples provided in the vulnerability discussion and check.

Verify the application configuration guide is distributed along  with the application.

**Fix ID:**  F-24322r493898_fix

**Vulnerability ID:**  V-222663

**Rule ID:**  SV-222663r961863_rule

---

## If the application contains classified data, a Security Classification Guide must exist containing data elements and their classification.

<span style="color:#ff8c00;font-size:150%;">Medium Severity</span>

### Description

Without a classification guide the marking, storage, and output media of classified material can be inadvertently mixed with unclassified material, leading to its possible loss or compromise.

### Check Text

If the application does not process classified information, this check is not applicable.
 
The application may already be covered by a higher level program or other classification guide. If the classification guide is not written specifically to the application, the sensitive application data should be reviewed to determine whether it is contained in the classification guide.

DOD 5200.01 Volume 1 identifies requirements for security classification and declassification guides.

https://www.esd.whs.mil/Portals/54/Documents/DD/issuances/dodm/520001m_vol1.pdf

Security classification guides must provide the following information:

Identify specific items, elements, or categories of information to be protected.

State the specific classification to be assigned to each item or element of information and, when useful, specify items of information that are unclassified.

Provide declassification instructions for each item or element of information, including the applicable exemption category for information exempted from automatic declassification.

State a concise reason for classification for each item, element, or category of information that, at a minimum, cites the applicable classification categories in Section 1.5 of E.O. 12958.

Identify any special handling caveats that apply to items, elements, or categories of information.

Identify, by name or personal identifier and position title, the original classification authority approving the guide and the date of that approval.

Provide a point of contact for questions about the guide and suggestions for improvement.

For information exempted from automatic declassification because its disclosure would reveal foreign government information or violate a statute, treaty, or international agreement, the security classification guide will identify the government or specify the applicable statute, treaty, or international agreement, as appropriate.

If the security classification guide does not exist, or does not contain application data elements and their classification, this is a finding.

**Check ID:**  C-24334r1051276_chk

### Fix Text 

Create and maintain a security classification guide.

**Fix ID:**  F-24323r493901_fix

**Vulnerability ID:**  V-222664

**Rule ID:**  SV-222664r1051277_rule

---

## The designer must ensure uncategorized or emerging mobile code is not used in applications.

<span style="color:#ff8c00;font-size:150%;">Medium Severity</span>

### Description

By definition, mobile code is software obtained from remote systems outside the enclave boundary, transferred across a network, and then downloaded and executed on a local system without explicit installation or execution by the recipient.  

For a complete list of mobile code categorizations, refer to the overview document included with this STIG.
Categorized mobile code includes but is not limited to:

- ActiveX
- Windows Scripting Host when used as mobile code
- Unix Shell Scripts when used as mobile code
- DOS batch scripts when used as mobile code
- Java applets and other Java mobile code
- Visual Basic for Applications (VBA)
- LotusScript
- PerfectScript
- Postscript
- JavaScript (including Jscript and ECMAScript variants)
- VBScript
- Portable Document Format (PDF)
- Shockwave/Flash
- Rich Internet Applications

The following technologies are not currently designated as mobile code:

- XML
- SMIL
- QuickTime
- VRML (exclusive of any associated Java applets or JavaScript scripts)

The following are outside the scope of the mobile code requirements:

- Scripts and applets embedded in or linked to web pages and executed in the context of the web server.  Examples of this are Java servlets, Java Server pages, CGI, Active Server Pages, CFML, PHP, SSI, server-side JavaScript, server-side LotusScript.
- Local programs and command scripts 
- Distributed object-oriented programming systems (e.g., CORBA, DCOM).
- Software patches, updates, including self-extracting updates - software updates that must be invoked explicitly by the user are outside the mobile code policy.  Examples of technologies in this area include: Netscape SmartUpdate, Microsoft Windows Update, Netscape web browser plug-ins and Linux.

If other types of mobile code technologies are present that are not listed here, a written waiver must be granted by the CIO (allowing use of emerging mobile code technology). Also uncategorized mobile code must be submitted for AO approval.

### Check Text

Review the application documentation and interview application administrator.

Determine what mobile code types are used by the application.

If uncategorized mobile code types are found, ask the application administrator to provide the documented waiver and risk acceptance. If the application is using uncategorized or emerging mobile code and there is no waiver provided, this is a finding.

**Check ID:**  C-24335r493903_chk

### Fix Text 

Remove uncategorized or emerging mobile code from the application or obtain a waiver and risk acceptance to operate.

**Fix ID:**  F-24324r493904_fix

**Vulnerability ID:**  V-222665

**Rule ID:**  SV-222665r961863_rule

---

## Production database exports must have database administration credentials and sensitive data removed before releasing the export.

<span style="color:#ff8c00;font-size:150%;">Medium Severity</span>

### Description

Production database exports are often used to populate development databases. Test and development environments do not typically have the same rigid security protections that production environments do. When production data is used in test and development, the production database exports will need to be scrubbed to prevent information like passwords and other sensitive data from becoming available to development and test staff that may not have a need to know. Sensitive data should not be included in database exports because of classification, privacy, and other types of data protection requirement issues. Not all application developers have need-to-know sensitive information such as HIPAA data, Privacy Act Data, production admin passwords or classified data.

### Check Text

Review the application documentation and identify the existence of databases within the application architecture.

Ask the application admin to identify when data exports from this database are imported to test or development databases.
 
If no data is exported to test or development databases, this check is not applicable.

If there are such data exports, ask if the production database includes sensitive data identified by the data owner as sensitive such as passwords, financial, personnel, personal, HIPAA, Privacy Act, or classified data is included.

If any database exports include sensitive data and that data is not sanitized or removed prior to or immediately after import to the development database, this is a finding.

**Check ID:**  C-24336r493906_chk

### Fix Text 

Remove sensitive data from production database exports.

**Fix ID:**  F-24325r493907_fix

**Vulnerability ID:**  V-222666

**Rule ID:**  SV-222666r961863_rule

---

## Protections against DoS attacks must be implemented.

<span style="color:#ff8c00;font-size:150%;">Medium Severity</span>

### Description

Known DoS threats documented in the threat model should be mitigated, to prevent DoS type attacks.

### Check Text

Ask the application representative for the threat model document.

Examine the threat model document and determine if DoS attacks are specified as a threat.

If there are no DoS threats identified in the threat model, the requirement is not applicable.

Verify the mitigations provided for DoS attacks are implemented from the threat model.

If mitigations for DoS attacks are identified in the threat model but are not implemented, this is a finding.

**Check ID:**  C-24337r493909_chk

### Fix Text 

Implement mitigations from the threat model for DOS attacks.

**Fix ID:**  F-24326r493910_fix

**Vulnerability ID:**  V-222667

**Rule ID:**  SV-222667r961863_rule

---

## The system must alert an administrator when low resource conditions are encountered.

<span style="color:#ff8c00;font-size:150%;">Medium Severity</span>

### Description

In order to prevent DoS type attacks, applications should be monitored when resource conditions reach a predefined threshold. This could indicate the onset of a DoS attack or could be the precursor to an application outage.

### Check Text

Review the system documentation and interview the application and system administrators.

Examine the system to determine if an automated, continuous on-line monitoring and audit trail creation capability is present with the capability to immediately alert personnel of any unusual or inappropriate activity with potential IA implications, and with a user configurable capability to automatically disable the system if serious IA violations are detected.

If this monitoring capability does not exist, this is a finding.

**Check ID:**  C-24338r493912_chk

### Fix Text 

Implement mechanisms to alert system administrators about a low resource condition.

**Fix ID:**  F-24327r493913_fix

**Vulnerability ID:**  V-222668

**Rule ID:**  SV-222668r961863_rule

---

## At least one application administrator must be registered to receive update notifications, or security alerts, when automated alerts are available.

<span style="color:#b3b31a;font-size:150%;">Low Severity</span>

### Description

Administrators should register for updates to all COTS and custom-developed software, so when security flaws are identified, they can be tracked for testing and updates of the application can be applied.

Admin personnel should be registered to receive updates to all components of the application, such as Web Server, Application Servers, and Database Servers. Also, if update notifications are provided for any custom-developed software, libraries or third-party tools, deployment personnel must also register for these updates.

### Check Text

Review the components of the application.

Ask the application representative to demonstrate deployment personnel are registered to receive notifications for update notification for all of the application components including custom-developed software, libraries and third-party tools.

If no deployment personnel are registered to receive the alerts, this is a finding.

**Check ID:**  C-24339r493915_chk

### Fix Text 

Register administrators to receive update notifications so they can patch and update applications and application components.

**Fix ID:**  F-24328r493916_fix

**Vulnerability ID:**  V-222669

**Rule ID:**  SV-222669r961863_rule

---

## The application must provide notifications or alerts when product update and security related patches are available.

<span style="color:#b3b31a;font-size:150%;">Low Severity</span>

### Description

An application vulnerability management and update process must be in place to notify and provide users and administrators with a means of obtaining security patches and updates for the application.

An important part of the maintenance phase of an application is managing vulnerabilities for updated versions of the application after the application is released.  When a security flaw is discovered in an application deployed in a production environment, notification to the user community must take place as quickly as possible. 

This notification should be planned for in the design phase of the application. This notification should be a warning of any potential risks to the application or data. A notification mechanism will be established to notify users of the vulnerability and the potential risks, the availability of a solution, and/or potential mitigations reducing risks to the application.

### Check Text

Review the components of the application.  Interview the application administrator.

Have the application administrator demonstrate the application notification process that occurs when a security patch or product update is available.

The process must include a brief description of the issue and any potential risks related to the issue.

The process must also include information regarding the availability of the patch or update and how it can be obtained as well as any potential mitigations that can be utilized in the interim.

If there is no application security patch or update notification process, this is a finding.

If the application notification process does not include a brief description, information on risks, how to obtain the patch or update and any potential mitigations, this is a finding.

**Check ID:**  C-24340r493918_chk

### Fix Text 

Provide a distribution mechanism for obtaining updates to the application.

Include a description of the issue, a summary of risk as well as potential mitigations and how to obtain the update.

**Fix ID:**  F-24329r493919_fix

**Vulnerability ID:**  V-222670

**Rule ID:**  SV-222670r961863_rule

---

## Connections between the DoD enclave and the Internet or other public or commercial wide area networks must require a DMZ.

<span style="color:#ff8c00;font-size:150%;">Medium Severity</span>

### Description

In order to protect DoD data and systems, all remote access to DoD information systems must be mediated through a managed access control point, such as a remote access server in a DMZ.

### Check Text

Interview the application representative and determine if the application is publicly accessible.

If the application is publicly accessible and traffic is not being routed through a DMZ, this is a finding.

**Check ID:**  C-24341r493921_chk

### Fix Text 

Setup a DMZ between DoD and public networks.

**Fix ID:**  F-24330r493922_fix

**Vulnerability ID:**  V-222671

**Rule ID:**  SV-222671r961863_rule

---

## The application must generate audit records when concurrent logons from different workstations occur.

<span style="color:#b3b31a;font-size:150%;">Low Severity</span>

### Description

When an application provides users with the ability to concurrently logon, an event must be recorded that indicates the user has logged on from different workstations. It is important to ensure that audit logs differentiate between the two sessions.

The event data must include the user ID, the workstation information and application session information that provides the details necessary to determine which application session executed what action on the system.

### Check Text

Review the application documentation and interview the application administrator to identify where log records are stored.

Access log records then log on to the application as a regular user from one workstation. Take note of workstation IP address and confirm the address as the source workstation.

Have the application administrator log on to the application from another workstation using the same account.

Validate the IP address of the second workstation is recorded in the logs.

If the application does not create an audit record when concurrent logons occur from different workstations, this is a finding.

**Check ID:**  C-24342r493924_chk

### Fix Text 

Configure the application to log concurrent logons from different workstations.

**Fix ID:**  F-24331r493925_fix

**Vulnerability ID:**  V-222672

**Rule ID:**  SV-222672r961833_rule

---

## The Program Manager must verify all levels of program management, designers, developers, and testers receive annual security training pertaining to their job function.

<span style="color:#ff8c00;font-size:150%;">Medium Severity</span>

### Description

Many application team members may not be aware of the security implications regarding the code that they design, write and test.  To address this concern, the Program Manager will ensure all levels of program management receive security training regarding the necessity, impact, and benefits of integrating secure development practices into the development lifecycle.  

This training is in addition to DoD 8570 training requirements as DoD 8570 annual security training does not presently cover application SDLC security concerns.

The Program Manager will ensure development team members are provided training on secure design principles for the entire SDLC and newly discovered vulnerability types on, at least, an annual basis. 

Development team members include:

- Designers/Application Architects
- Developers/Programmers
- Testers
- Application managers

This requirement applies to development teams or individual application developers and does not apply when reviewing a COTS application or an application hosted at a DECC or other hosting facility when the application team is not available to interview.

### Check Text

This requirement is meant to be applied to developers and development teams only, otherwise, this requirement is not applicable.  

Interview the application representative.

Ask for evidence of annual security training for application managers, designers, developers, and testers. 

Examples of evidence include course completion certificates and a class roster. At a minimum, security training should include security awareness training pertaining to overall principles of secure application development.

Training must be in addition to DoD 8570 training requirements as DoD 8570 annual security training does not presently cover application SDLC security concerns. 

If there is no evidence of security training, this is a finding.

**Check ID:**  C-24343r493927_chk

### Fix Text 

Provide application development/operational related security specific annual training for managers, designers, developers, and testers.

**Fix ID:**  F-24332r493928_fix

**Vulnerability ID:**  V-222673

**Rule ID:**  SV-222673r961863_rule

---

## The application must implement NSA-approved cryptography to protect classified information in accordance with applicable federal laws, Executive Orders, directives, policies, regulations, and standards.

<span style="color:#ff8c00;font-size:150%;">Medium Severity</span>

### Description

Use of weak or untested encryption algorithms undermines the purposes of utilizing encryption to protect classified data. The application must implement cryptographic modules adhering to the higher standards approved by the federal government since this provides assurance they have been tested and validated.
 
Advanced Encryption Standard (AES)
Symmetric block cipher used for information protection
FIPS Pub 197
Use 256 bit keys to protect up to TOP SECRET

Elliptic Curve Diffie-Hellman (ECDH) Key Exchange
Asymmetric algorithm used for key establishment
NIST SP 800-56A
Use Curve P-384 to protect up to TOP SECRET.

Elliptic Curve Digital Signature Algorithm (ECDSA)
Asymmetric algorithm used for digital signatures
FIPS Pub 186-4
Use Curve P-384 to protect up to TOP SECRET.

Secure Hash Algorithm (SHA)
Algorithm used for computing a condensed representation of information
FIPS Pub 180-4

Use SHA-384 to protect up to TOP SECRET.
 
Diffie-Hellman (DH) Key Exchange
Asymmetric algorithm used for key establishment
IETF RFC 3526 
Minimum 3072-bit modulus to protect up to TOP SECRET

RSA
Asymmetric algorithm used for key establishment
NIST SP 800-56B rev 1
Minimum 3072-bit modulus to protect up to TOP SECRET

RSA 
Asymmetric algorithm used for digital signatures
FIPS PUB 186-4
Minimum 3072 bit-modulus to protect up to TOP SECRET.

### Check Text

Review the application documentation, system security plan and interview the application administrator to determine if the application processes classified data.

If the application does not process classified data, this requirement is not applicable.

Identify the data classifications and the cryptographic protections established to protect the application data.

Verify the application is configured to utilize the appropriate encryption based upon data classification, cryptographic tasks that need to be performed (information protection, hashing, signing) and information protection requirements.

NIST-certified cryptography must be used to store classified non-Sources and Methods Intelligence (SAMI) information if required by the information owner.

NSA-validated type-1 encryption must be used for all SAMI data stored in the enclave.

If the application is not configured to utilize the NSA-approved cryptographic modules in accordance with data protection requirements specified in the security plan, this is a finding.

**Check ID:**  C-69551r997305_chk

### Fix Text 

Configure application to encrypt stored classified information; Ensure encryption is performed using NIST FIPS 140-2-validated encryption.

Encrypt stored, non-SAMI classified information using NIST FIPS 140-2-validated encryption.

Implement NSA-validated type-1 encryption of all SAMI data stored in the enclave.

**Fix ID:**  F-69459r997306_fix

**Vulnerability ID:**  V-265634

**Rule ID:**  SV-265634r997307_rule

---

