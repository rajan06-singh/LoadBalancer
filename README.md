# LoadBalancer

Overview :- 
Developed a loadbalancing feature which will forward the client requests in round robin fashion to down stream connected servers. 

Lanaguage :- 
Python 

Resources:- 
Python IDLE 3.5, Ubuntu 16.04 Server, Cent OS 7 Server, Kali Linux Server. 

Summary:- 
In this project, I have created a server that is listening on specific port (5555) using socket library. Secondly, created a client which will send the message to load balancer on specific IP address and port (5555). Lastly, I have created a loadbalancer which will provide the functionality of client as well as server. It will listen on port (5555) and forward the request connecting on port (5555) to server. Server will process these requests. Processing part of server is to save the message in new file called as storage.dat.

Working:- 
When a first client request arrives at loadbalancer, it will forward the request in round robin fashion i.e. forward that request to first downstream server. When another request arrives, it will forwards that request to second downstream server. Subsequent packet will be sent to first downstream server and vice versa. For more logical view, please refer the attached png file. 

References:- 
Socket libraries introduction (https://docs.python.org/3/library/socket.html#module-socket)



