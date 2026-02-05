# aap-shadow-customized

Customer repo that overrides the vendor flow (operate_v1 multiplies instead of adds).

## Pattern (no flow duplication)

The customer **imports** the vendor playbook and passes overrides via vars. The flow (step 1 → step 2) is defined once in the vendor; the customer only overrides the steps it needs.

```yaml
# site.yml
- name: Customer deployment
  ansible.builtin.import_playbook: osac.demo.site
  vars:
    add_role_override:
      name: override_operate
      tasks_from: operate_v1.yml
```

Optional: **output_role_override** to replace step 2 as well.

## Vendor collection (osac.demo)

- **Option A (Galaxy):** Use `collections/requirements.yml` so AAP installs the collection on sync (no submodule).
- **Option B (submodule):** `collections/ansible_collections/osac/demo` as a git submodule; clone with `--recurse-submodules` and in AAP enable “Update submodules”.

**ansible.cfg** sets `collections_path = ./collections` and `roles_path = ./roles` so the collection and project roles (e.g. override_operate) are found.

## Run

```bash
ansible-playbook site.yml
ansible-playbook site.yml -e number_a=3 -e number_b=4   # output_v1: 12
```
