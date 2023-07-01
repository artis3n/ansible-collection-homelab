=============================
artis3n.homelab Release Notes
=============================

.. contents:: Topics


v1.2.0
======

Release Summary
---------------

Removes the ``code_server`` role.

Minor Changes
-------------

- Removes the ``code_server`` role.

v1.1.0
======

Release Summary
---------------

Adds a ``code_server`` role, a ``password_hash`` lookup plugin, and fixes the CI setup for ease of inclusion of future roles. 

Minor Changes
-------------

- Adds a ``code_server`` role to install `Code-Server <https://github.com/coder/code-server>`_ on an Ubuntu target.
- Adds a ``password_hash`` lookup plugin to generate argon2, bcrypt, pbkdf2, or scrypt hashes.

Bugfixes
--------

- Adds a missing handler to ``canonical_ads`` to reload systemd after making service changes.

New Plugins
-----------

Lookup
~~~~~~

- artis3n.homelab.password_hash - generate a password hash

New Roles
---------

- artis3n.homelab.code_server - Installs code-server on Ubuntu
