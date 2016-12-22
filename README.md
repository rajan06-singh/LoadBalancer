# LoadBalancer

Overview :- 
Designed a loadbalancing feature which will forward the client requests in round robin fashion to down stream connected servers. 

Lanaguage :- 
Python 

Resources:- 
Python IDLE 3.5, Ubuntu 16.04 Server, Cent OS 7 Server, Kali Linux Server. 

Summary:- 
In the project, three files are created using pyhton code and code libraries (Socket Library). Firstly, a server file was created which listens on specific tcp port 5555 to process the incoming request. Secondly, a client file was created which resides at client machine and initiate or sends the request. Lastly, a file consisting of loadbalancing code was created. It has two functions. First, it will listen on port (5555) and second, forward the incoming request on port (5555) to downstream connected servers in round robin fashion. Eventually, downstream servers will process those incoming requests. 

Working:- 
Please refer the attached png file to understand the network connectivity, architecture and working of the project. As per the architecture, we have two downstream servers, one client machine and one loadbalancer server. At first, client machine sends the request to destination server (Loadbalancer) on port 5555 (for sake of project, we can define any port here). As soon as the first client request arrives at loadbalancer, it will forward the request to first downstream server. Subsequent request arriving on the loadbalancer will be forwarded to another downstream connected server i.e. second server. Now, when the third request arrives, loadbalancer will send that request to first down stream server and so on.    

References:- 
Socket libraries introduction (https://docs.python.org/3/library/socket.html#module-socket)



