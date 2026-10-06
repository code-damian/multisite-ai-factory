# WebStrefa — SMTP / Auth email

Supabase Auth has email confirmation enabled and the production Site URL configured.

For public production delivery configure custom SMTP in Supabase Authentication → Emails → SMTP Settings. Resend is a simple option.

Typical Resend SMTP settings:
- Host: smtp.resend.com
- Port: 465
- User: resend
- Password: Resend API key
- Sender: verified WebStrefa sender
- Sender name: WebStrefa

Use confirmation.html for Confirm sign up, recovery.html for Reset password and email-change.html for Change email address.