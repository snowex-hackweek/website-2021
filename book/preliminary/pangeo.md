# Pangeo

## What is Pangeo?

[Pangeo](https://pangeo.io) is a community of researchers building open, reproducible
and scalable scientific software tools. Several of the UW eScience Hackweek organizers
are involved in [projects with NASA and NSF](https://earthdata.nasa.gov/esds/competitive-programs/access/eos-data-cloud)
to build prototype systems to enable data discovery in the era of expanding data
volume and complexity.

### What is JupyterHub?

We use {term}`JupyterHub` in an educational setting because it enables us to quickly begin working with code
without spending time to get the necessary libraries and dependencies set up on
everyone's individual computers. [These slides](https://www.slideshare.net/willingc/jupyterhub-a-thing-explainer-overview)
give a nice overview of what JupyterHub is all about.

![jupyterhub-connectivity](../img/jupyterhub-connectivity.png)

### Why use AWS?

JupyterHub can run on a laptop, supercomputers, or any Cloud provider! For this
{{ hackweek }}, we have created virtual computing instances on
[Amazon Web Services](https://aws.amazon.com/) that can be deployed on demand in
a parallel computing environment. We're running in the AWS us-west-2 datacenter
because [NASA is starting to store data there](https://earthdata.nasa.gov/eosdis/cloud-evolution)!
There are huge advantages to be gained in moving algorithms to data, rather than
downloading.

If you're new to the Cloud see these [NASA resources](https://earthdata.nasa.gov/learn/user-resources/webinars-and-tutorials/cloud-primer). Also note that Cloud computing is effectively renting hardware and
software, so there is a cost involved. Fortunately for scientists there are straightforward
[research credit programs](https://aws.amazon.com/earth/research-credits/) to help get started without worrying about costs.
