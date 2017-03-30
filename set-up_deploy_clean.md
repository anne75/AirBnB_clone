## Set-up, Deploy the static website, and clean up

This file aims at presenting what was done to deploy the static website done here (/web_static) on our servers ([image](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/288/aribnb_diagram_0.jpg?cache=off)).  

Tasks: 

0. Prepare the servers by creating folders, managing the conf files to prepare for the data.(bash)
1. Prepare the data, archive the files.(fabric)
2. Deploy the archive.(fabric)
3. Combine 1 and 2 to automate the task.
4. Clean the archives, and the older websites versions to keep only `n`.(fabric)

_____
**Readings**    
- [How to use Fabric](https://www.digitalocean.com/community/tutorials/how-to-use-fabric-to-automate-administration-tasks-and-deployments)
- [How to use Fabric in python](http://www.pythonforbeginners.com/systems-programming/how-to-use-fabric-in-python)  
- [Fabric and command line options](http://docs.fabfile.org/en/1.13/usage/fab.html#command-line-options)  
- [Nginx configuration for beginners](http://nginx.org/en/docs/beginners_guide.html)
- [Difference between root and alias in nginx](https://blog.heitorsilva.com/en/nginx/diferenca-entre-root-e-alias-do-nginx/)  
- [Fabric for python3](https://github.com/mathiasertl/fabric)
- [Fabric documentation](http://www.fabfile.org/)  
_____
**Install**  
Beware it is not always successfull.  
```
pip3 uninstall Fabric
sudo apt-get install libffi-dev
sudo apt-get install libssl-dev
sudo apt-get install python3.4-dev
sudo apt-get install libpython3-dev
pip3 install pyparsing
pip3 install appdirs
pip3 install Fabric3
```
