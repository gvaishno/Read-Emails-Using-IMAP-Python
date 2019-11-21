# Read-Emails-Using-IMAP-Python
Read Emails Using IMAP (Python)

There are many, many ways to get communication data using Python, and there are also many different forms of communication texts, comments, video uploads, etc. This section shows only one of the ways to use Python to get and parse email data.

First, we need to get some emails. You can do this with IMAP and the Python library imaplib. Any personal information has been removed from the script, so you can either take all of this at my word, or you can use your own information.

This example uses a Gmail account. For the script to work, IMAP needs to be enabled on your Gmail account.

To enable IMAP, first open Gmail. Then click the settings button (settings) and select Settings. Or navigate to here https://mail.google.com/mail/u/0/#settings/fwdandpop

Choose the Forwarding and POP/IMAP tab.

In the “IMAP Access” section, select Enable IMAP. Then click Save Changes. If you need more help, visit this Gmail help page.

You also need to change some settings in your Google account. Navigate to your Google dashboard either by clicking on your account avatar in the upper right-hand corner of your screen and then clicking My Account or by navigating to https://myaccount.google.com.

Then choose Sign-in & security, scroll down until you see the option Allow less secure apps, or navigate to https://myaccount.google.com/u/1/lesssecureapps and turn the access on.

And then navigate to https://accounts.google.com/DisplayUnlockCaptcha and click "continue". This is going to allow access from other servers.

After all of this is done, the script should be able to access your email using the imaplib Python library.

Essentially, you’ve now changed your Gmail settings so that when the script sends a request, with the proper credentials, Gmail will attempt to fulfill the request.
