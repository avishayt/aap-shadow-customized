# aap-shadow-customized

Customer repo that overrides the vendor flow (operate_v1 multiplies instead of adds).

## Vendor collection (osac.demo)

The vendor collection is included as a **git submodule** at `collections/ansible_collections/osac/demo`, so the role `osac.demo.shadow_test` is found when the playbook runs (no dependency on AAP’s Galaxy install).

- **Clone with submodules:** `git clone --recurse-submodules <repo-url>`
- **Or after clone:** `git submodule update --init --recursive`
- **Upgrade vendor:** `git submodule update --remote collections/ansible_collections/osac/demo`

In AAP, enable **“Update submodules”** (or equivalent) on the project so the submodule is checked out when the project is synced.

## Run

```bash
ansible-playbook site.yml
ansible-playbook site.yml -e number_a=3 -e number_b=4   # output_v1: 12
```
