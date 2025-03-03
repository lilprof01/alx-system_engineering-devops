![3828553](https://github.com/user-attachments/assets/0f649a01-50db-4cb9-a451-64c717523c7b)

# Issue Summary

Duration: February 15, 2024, 14:00–16:00 UTC (2 hours).

Impact: 100% of users experienced HTTP 503 errors when accessing the website. The web service was completely unavailable.

Root Cause: A syntax error in a newly deployed Nginx configuration file caused the service to crash.

## Timeline

14:00 UTC: Issue detected via automated monitoring alerts (HTTP 503 errors spiked to 100%).

14:05: Engineering team began investigating server health, assuming a potential DDoS attack. Firewall logs and network traffic were analyzed, but no anomalies found.

14:20: Misleading path: Focus shifted to database connectivity issues. Database cluster was verified as operational, ruling this out.

14:40: Incident escalated to DevOps team after discovering Nginx had crashed on all servers.

14:50: Rollback initiated to revert to the last stable Nginx configuration (version 1.2).

15:10: Configuration rollback completed, but service remained down due to a missed dependency restart.

15:25: Engineers restarted Nginx globally after identifying the oversight.

15:55: Full service restoration confirmed via monitoring and synthetic user tests.

## Root Cause and Resolution
### Root Cause:
A deployment at 13:55 UTC introduced an Nginx configuration file (app_v2.conf) with a missing semicolon in a location block. This syntax error caused Nginx to fail during reload, crashing the service. The error went undetected due to a lack of automated configuration validation pre-deployment.

### Resolution:

* Rollback: Reverted to the previous Nginx configuration (app_v1.conf).

* Validation: Manually tested the configuration using nginx -t before reapplying.

* Restart: Executed a global systemctl restart nginx to reload the corrected config.

## Corrective and Preventative Measures

### Improvements:

* Strengthen deployment pipelines to catch configuration errors earlier.

* Improve monitoring to detect service failures immediately after deployments.

* Formalize rollback procedures to reduce recovery time.

## Tasks:

* Implement pre-deployment configuration validation: Add nginx -t as a CI/CD step for all Nginx config changes. (Due: March 30)

* Enhance monitoring: Create alerts for failed Nginx reloads and HTTP error rates >5%. (Due: April 5)

* Deploy canary releases: Test configuration changes on 10% of servers before full rollout. (Due: April 10)

* Document rollback playbook: Include explicit steps to restart dependencies post-rollback. (Due: March 25)

* Conduct postmortem review: Train team on configuration management best practices. (Due: March 20)
