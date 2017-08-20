# Microservice Starter
## What is this?
This project is a starting point for building microservices with the Spring Cloud suite and to orchestrate them with Docker. It employs three basic
concepts all projects, designed to use microservices, should be using.

### Discovery Service
This project uses Eureka to support client-server discovery. Every microservice should be conidered a "client" while the microservice
designed to be the "server" keeps track of all these clients. This allows for a registry to be maintained, where the status of each microservice
is monitored (is it still running? how many instances are running? what is the IP or port?). Other pieces of the application utilize this
Eureka server to communicate with the various other microservices.

### Config Server
This project has a config server microservice designed for providing the other microservices a way to read application properties stored
in a remote repository. In a distributed system, it is a common challenge to keep track of every property file, or to support dynamic property changes.
The config server makes this easy, and could be setup to read properties from either the file system or from a remote repository (such as git).

### Edge Server
This project uses an edge server microservice to operate both as a reverse proxy and load balancer. The edge server performs it's reverse proxy
work using Zuul, while it's load-balancing is done using Ribbon. It's the gatekeeper between the outside world and the entirety of the application,
making it so we only need a single IP and port to access any REST APIs hosted on our other microservices. Zuul only needs to be given the path
pattern mapping to redirect accordingly to the other microservices. Zuul utilizes the discovery service (Eureka) to know where each service lives,
while Ribbon will also use the discovery service to load-balance across all replicated instances. By default, this project utilizes round-robin
order when load-balancing server requests to a microservice.

Another purpose of the edge server is to perform any authentication and authorization needed to filter requests to all other microservices.
This project doesn't have any basic authentication/authorization setup, but it's very easy to integrate. See [How to create Zuul filters](https://github.com/Netflix/zuul/wiki/Writing-Filters)
for more on how this can be done. Typically, some level of OAuth is performed (beit OAuth 1 or two-legged OAuth) so microservices can only
be accessed by other microservices, and the only entry into the application would be through the edge server and it's Zuul filters.
