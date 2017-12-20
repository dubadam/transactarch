# transactarch
Archival system with transactions in it's heart

The basic goal is to implement a storage without the actual 
DELETE operator. This is to make two things possible:
1. No change is irreversible.
2. Modification history is builtin.

The storage engine will be supplemented by Storable prototypes 
and some simple Active Query wannabe.

Architecture as follows:
* A table with list of transactions (id, date, author_id);
* A table with list of Storables (id, guid, classname);
* A history log (transaction_id, storable_id).