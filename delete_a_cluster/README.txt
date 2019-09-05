Delete a cluster


WARNING
Datastores on the ESXi hosts in the cluster that will be deleted are destroyed.
NOTE
You cannot delete the last cluster in a domain. Instead, the domain can be deleted.

Prerequisites:

The following data is required

	ID of the cluster to be deleted

	Ensure that a cluster with the given ID exists.

The cluster has been marked for deletion.

Migrate or backup the VMs and data on the data store associated with the cluster to another location.


Usage:
    python delete_clusterpy <hostname> <username> <password> <domain_id>


