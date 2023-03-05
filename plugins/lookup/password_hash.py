DOCUMENTATION = """
    name: password_hash
    version_added: "1.1.0"
    author:
      - Ari Kalfus (@artis3n) <dev@artis3nal.com>
    short_description: generate a password hash
    description:
      - Generates a password hash from plaintext input.
      - This lookup function does not currently generate a random password and requires a password to be inputted.
    options:
      _terms:
        description:
          - Input data to hash
        required: true
      hash:
        description:
          - Which hash scheme to use, should be one hash scheme from C(passlib.hash): C(argon2, bcrypt_sha256, pbkdf2_sha512, scrypt).
          - If not provided, C(argon2) will be used by default.
        default: 'argon2'
    notes:
      - This is inspired by the ansible.builtin.password lookup function, but supports modern hashing algorithms and does not support writing out to a file on the Ansible host.
      - This lookup function will generate a new hash if re-run from the same input, so this function will break idempotency.
      - 'As all lookups, this runs on the Ansible host as the user running the playbook, and "become" has no effect.
        Depending on the hash algorithm chosen, appropriate pip dependencies must be installed on the Ansible host.
        See https://passlib.readthedocs.io/en/stable/install.html#optional-libraries for required dependencies.
        For example, to use argon2 the Ansible host must C(pip install passlib[argon2]).'
"""

EXAMPLES = """
- name: Create an argon2 hash
  ansible.builtin.set_fact:
    passhash: "{{ lookup('artis3n.homelab.password_hash', 'mypassword' }}"

- name: Create a bcrypt hash
  ansible.builtin.set_fact:
    passhash: "{{ lookup('artis3n.homelab.password_hash', 'mypassword', hash='bcrypt_sha256' }}"

- name: Create a PBKDF2 hash
  ansible.builtin.set_fact:
    passhash: "{{ lookup('artis3n.homelab.password_hash', 'mypassword', hash='pbkdf2_sha512' }}"

- name: Create an scrypt hash
  ansible.builtin.set_fact:
    passhash: "{{ lookup('artis3n.homelab.password_hash', 'mypassword', hash='scrypt' }}"
"""

RETURN = """
_raw:
  description:
    - a password hash
  type: list
  elements: str
"""

from ansible.errors import AnsibleError, AnsibleModuleError
from ansible.module_utils._text import to_text, to_native
from ansible.parsing.splitter import parse_kv
from ansible.plugins.lookup import LookupBase
from ansible.utils.display import Display

display = Display()

VALID_PARAMS = frozenset(('hash'))
VALID_HASH_TYPES = frozenset(('argon2', 'bcrypt_sha256', 'pbkdf2_sha512', 'scrypt'))

PASSLIB_E = None
PASSLIB_AVAILABLE = False
try:
    import passlib
    import passlib.hash
    PASSLIB_AVAILABLE = True
except Exception as e:
    PASSLIB_E = e


class PassLibHash:
    def __init__(self, algorithm):
        self.algorithm = algorithm
        if not PASSLIB_AVAILABLE:
            raise AnsibleError(f"passlib must be installed and usable to hash with '{algorithm}'", orig_exc=PASSLIB_E)

        try:
            self.crypt_algo = getattr(passlib.hash, algorithm)
        except Exception:
            raise AnsibleError(f"passlib does not support '{algorithm}' algorithm")

    def hash(self, secret):
        result = self.crypt_algo.hash(secret)
        # passlib.hash should always return something or raise an exception.
        # Still ensure that there is always a result.
        # Otherwise an empty password might be assumed by some modules, like the user module.
        if not result:
            raise AnsibleError(f"failed to hash with algorithm '{self.algorithm}'")

        return to_text(result, errors='strict')


class LookupModule(LookupBase):

    def _parse_parameters(self, term):
        data = None
        params = parse_kv(term)
        if '_raw_params' in params:
            data = params['_raw_params']
            del params['_raw_params']

        # Check for invalid parameters
        invalid_params = frozenset(params.keys()).difference(VALID_PARAMS)
        if invalid_params:
            raise AnsibleError(f"Unrecognized parameter(s) given to password_hash lookup: {', '.join(invalid_params)}")

        # Set defaults
        params['hash'] = params.get('hash', self.get_option('hash'))

        # Enforce valid hash selected
        invalid_hash_type = params.get('hash') not in VALID_HASH_TYPES
        if invalid_hash_type:
            raise AnsibleError(f"Unrecognized hash type: {params.get('hash')}."
                               f" Acceptable hash types are: {VALID_HASH_TYPES}")

        return data, params

    @staticmethod
    def _do_hash(data, hash_type):
        return PassLibHash(hash_type).hash(data)

    def run(self, terms, variables=None, **kwargs):
        ret = []
        self.set_options(var_options=variables, direct=kwargs)

        for term in terms:
            data, params = self._parse_parameters(term)
            result = self._do_hash(data, params.get('hash'))
            ret.append(result)

        if len(ret) == 0:
            # This module has failed, generate an error
            raise AnsibleModuleError(f"Failed to generate hash, this is a module failure. Please contact the module author")

        return ret
