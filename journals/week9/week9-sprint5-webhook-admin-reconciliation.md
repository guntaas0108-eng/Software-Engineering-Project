# Week 9 Journal — Sprint 5: Webhooks, Admin & Payment Reconciliation

## Student
Atiksh Gupta — Person 4: Chat, Appointments, Payments, Admin, CI/CD and Testing

## Objective
Extend payment operations beyond checkout by defining webhook processing, reconciliation and useful admin visibility for payment support.

## Work Done
- Reviewed the need to reconcile browser verification results with provider-side payment events.
- Prepared webhook validation requirements, including raw request-body signature verification and safe handling of repeated events.
- Reviewed payment status transitions and the need to prevent an older or duplicate event from incorrectly overwriting a final status.
- Reviewed the payment admin dashboard fields needed for operational inspection and support.
- Coordinated with Guntaas on transaction identifiers and database constraints, and with Dhruv on buyer-visible payment result states.
- Prepared test cases for valid webhook signatures, invalid signatures, duplicate event delivery and unknown payment references.

## Outcome
Webhook and reconciliation requirements are documented for the payment workflow. They should not be described as operational until the endpoint is implemented, configured and tested with Razorpay test-mode events.

## Issues / Follow-up
- Implement or verify webhook endpoint and secret configuration.
- Make webhook processing idempotent.
- Confirm that webhook events are linked to the correct local payment record.
- Test payment status reconciliation and admin visibility.
- Ensure logs do not expose secrets or sensitive payment data.

## Learning
I learned that payment systems need a reliable server-to-server reconciliation path because a user may close the browser or lose connectivity after completing checkout.
