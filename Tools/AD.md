# Active Directory
- An Active Directory forest is a collection of parent/child domains and is used to share authentication between domains, while keeping those domain objects (computers, users, etc.) isolated.
- If an organization called Corp has a Chicago and San Diego office, they may choose to create a forest made up of a parent domain, and two child domains.
```
                corp.local
               /          \
              /            \
sandiego.corp.local    chicago.corp.local
```
## Common Active Directory Object Types
**Computer:** Represents a workstation or server in a domain.
**User:** Represent users or individuals in a domain.
**Organizational Unit (OU):** This type of object is a "container" that can include other objects. This can be useful if a company wants to further containerize objects such as putting all accounting users and computers into an OU called "accounting".

---

## Active Directory Exploitation Checklist
- Windows hashes are NOT salted. Password re-use is very common for users that have multiple user accounts in different domains.
- Domain Service accounts passwords may not be changed often.
- Certain “Enterprise Admin” accounts may be used to traverse forest domains.  Domains should utilize separation of privilege. Workstation Admins administer workstations, SQL Admins administer SQL Servers, etc.
