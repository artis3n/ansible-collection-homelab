# Ansible Collection - artis3n.homelab

This collection is a bundle of Ansible content used to configure my homelab environment.
You may find some roles useful yourself.

For user guides and references, see each role's README.md page.
High-level summaries and documented below.

# Included Roles

## `artis3n.homelab.canonical_ads`

Disables Canonical's advertisement injections into Ubuntu servers and desktops.

```yaml
- hosts: servers
  roles:
     - role: artis3n.homelab.canonical_ads
```
