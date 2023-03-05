artis3n.homelab.canonical_ads
=========

This role disables Canonical's advertisement injections into Ubuntu servers and desktops.

Currently, the role disables:
- [Motd News](https://ubuntu.com/legal/motd)
- [Apt News](https://askubuntu.com/questions/1441035/what-is-meant-by-apt-news)

Requirements
------------

None

Role Variables
--------------

None

Dependencies
------------

None

Example Playbook
----------------

```yaml
- hosts: servers
  roles:
     - role: artis3n.homelab.canonical_ads
```

License
-------

MIT

Author Information
------------------

Ari Kalfus ([@artis3n](https://blog.artis3nal.com/)) <dev@artis3nal.com>
