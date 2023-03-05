# artis3n.homelab.code_server

This role installs [Code-Server](https://coder.com/docs/code-server/latest) onto an Ubuntu target.

## Requirements

- `passlib[argon2]` python package is installed on the host running Ansible if `code_server_password` is supplied.

## Role Variables

### `code_server_address`

Optional, defaults to the `ansible_host` fact.

The address Code-Server should bind to (e.g. localhost, or another network interface IP).

### `code_server_port`

Optional, defaults to `8080`.

What port Code-Server should listen on.

### `code_server_password`

Optional. Code-Server authentication is disabled if not present.

The password required to access Code-Server.
[Will be stored hashed](https://coder.com/docs/code-server/latest/FAQ#can-i-store-my-password-hashed) with argon2.

The Ansible host must have `passlib[argon2]` installed before invoking this role in order to hash the password.

> **Note**
> 
> Note that the generated hash value will change each time this role is invoked, even if the raw input to this variable has not changed.
> This will not impact your ability to use Code-Server, but will interfere with idempotency checks.

### `code_server_user`

Optional, defaults to the `ansible_user_id` fact.

Which local user should run the Code-Server systemd service.

## Dependencies

Collections:
- `community.general`

## Example Playbook

```yaml
- hosts: servers
  roles:
     - role: artis3n.homelab.code_server
```

Run Code-Server with a password:

```yaml
- hosts: servers
  roles:
     - role: artis3n.homelab.code_server
       vars:
        code_server_password: "my password"
```

Bind Code-Server to your [Tailscale](https://tailscale.com) interface.
Note that it is recommended to run Code-Server through Caddy with Tailscale.

```yaml
- hosts: servers
  roles:
     - role: artis3n.homelab.code_server
       vars:
        code_server_address: 100.101.102.103
        code_server_port: 8888
```

See:
- <https://tailscale.com/kb/1166/vscode-ipad/#step-3-make-code-server-available-on-the-tailscale-interface>
- <https://coder.com/docs/code-server/latest/guide#using-lets-encrypt-with-caddy>

## License

MIT

## Author Information

Ari Kalfus ([@artis3n](https://blog.artis3nal.com/)) <dev@artis3nal.com>
