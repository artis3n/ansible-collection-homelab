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

## `artis3n.homelab.code_server`

Install [Code-Server](https://github.com/coder/code-server) on an Ubuntu target.

See the [README](/roles/code_server/README.md) for full details.

```yaml
- hosts: servers
  roles:
    - role: artis3n.homelab.code_server
```

# Included Plugins

## Lookup Plugins

### `artis3n.homelab.password_hash`

Generate password hashes for the modern algorithms supported by [passlib](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.html#other-modular-crypt-hashes).

See the [plugin documentation](/plugins/lookup/password_hash.py) for full details.

Differs from [`ansible.builtin.password`](https://docs.ansible.com/ansible/latest/collections/ansible/builtin/password_lookup.html) in the method of password storage (this doesn't store anything to the file system) and the supported hash algorithms.

```yaml
- name: Argon2 hash
  ansible.builtin.set_fact:
     hashed_pass: "{{ lookup('artis3n.homelab.password_hash', 'mypassword') }}"

- name: Other hash
  ansible.builtin.set_fact:
    other_hashed_pass: "{{ lookup('artis3n.homelab.password_hash', 'mypassword', hash='pbkdf2_sha512') }}"
```
