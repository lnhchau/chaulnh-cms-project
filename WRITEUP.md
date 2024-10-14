# Write-up Template

### Analyze, choose, and justify the appropriate resource option for deploying the app.

When deploying a lightweight CMS app, it's essential to consider the key factors of  **cost** ,  **scalability** ,  **availability** , and  **workflow** . Below is a comparison of these factors between Azure App Service and Virtual Machines:

#### 1. **Costs**

* **App Service** : Azure App Service operates on a pay-as-you-go pricing model with a range of service plans, including Free and Shared (for smaller apps), as well as Standard and Premium (for larger workloads). For a lightweight CMS, the cost is low, especially because the compute needs are minimal. However, one downside is that the app incurs charges continuously, even during idle times.
* **VM** : Virtual Machines can also offer a cost-effective solution, but the costs can increase quickly if more resources (e.g., CPU, memory) are required. Unlike App Service, VMs allow users to **stop** the machine and avoid costs when the app is not running, providing some flexibility. However, managing costs for scaling (adding more VMs) can become complex and costly.

#### 2. **Scalability**

* **App Service** : App Service offers built-in autoscaling based on demand. This is a major benefit as the service can automatically adjust the number of resources allocated, ensuring consistent performance without manual intervention. The CMS app's compute requirements are low, so scaling up or down is seamless and efficient, without significant changes to the deployment process.
* **VM** : While VMs can scale, the process is more manual and requires creating and managing additional VMs (horizontal scaling) or resizing the VM (vertical scaling). This adds complexity for developers or system administrators, especially for a small CMS that doesn't require extensive compute resources.

#### 3. **Availability**

* **App Service** : Azure App Service provides built-in high availability with automatic failover and load balancing, ensuring minimal downtime. It also supports geographic redundancy, which is useful for apps requiring global accessibility. For a CMS app, this ensures uptime with minimal configuration.
* **VM** : VMs can also achieve high availability, but it requires more configuration, such as setting up Azure Load Balancer, managing availability sets, or configuring failover solutions. For a small app, this is often overkill and adds operational overhead.

#### 4. **Workflow and Ease of Deployment**

* **App Service** : App Service provides a very simple and streamlined deployment process. Continuous deployment (CI/CD) can be easily configured through GitHub, Azure DevOps, or Bitbucket, with minimal setup. For a CMS app, this is a major advantage because it allows rapid updates and patches, without worrying about the underlying infrastructure.
* **VM** : VMs offer full control over the server environment and software stack, allowing for custom setups that are not possible with App Service. However, the deployment process can be more complex, requiring developers to manually manage the environment, patching, security, and application updates. It’s ideal for applications requiring specific configurations or dependencies, but not necessary for a simple CMS app.

### My Choice: **Azure App Service**

I chose **Azure App Service** for deploying the CMS app because of the following reasons:

* **Lightweight nature of the app** : The CMS app is a simple, lightweight application that does not require significant compute resources. App Service offers an efficient, low-maintenance, and scalable environment, which is perfect for this type of application.
* **Ease of deployment** : App Service integrates seamlessly with GitHub for continuous deployment. This means any updates or patches to the CMS app can be pushed quickly, with minimal downtime. It also eliminates the need to manage or configure infrastructure like virtual machines, which reduces operational complexity.
* **Cost efficiency** : Given the minimal compute requirements of the CMS app, App Service is cost-effective. While App Service incurs charges even when idle, the overall cost remains low for an app with these performance characteristics. The ability to autoscale also means there are no unexpected cost spikes during periods of higher traffic.
* **Built-in security and management** : App Service comes with built-in security features such as automatic patching, SSL certificates, and access to Azure's broader security ecosystem, which reduces the burden of manually managing security configurations.

### Assess app changes that would change your decision.

If the CMS app's requirements were to evolve, certain factors might lead me to reconsider using a Virtual Machine (VM):

#### App Service Limitations:

* **More compute-intensive operations** : If the CMS app were to expand to include heavier workloads, such as real-time media processing (e.g., video streaming or image editing), machine learning integration, or handling large data sets (e.g., Jupyter Notebooks or AI workloads), the compute limitations of App Service might no longer be sufficient. At this point, a Virtual Machine would provide greater flexibility in scaling hardware resources.
* **Custom configurations** : If the app required specific software configurations, programming environments, or operating system-level customizations that are not supported by App Service, a VM would offer more flexibility and control over the entire environment.

#### Virtual Machine Considerations:

* **Complexity and maintenance** : While a VM provides more control, it comes with additional complexity. For a large team with skilled developers or system administrators, the flexibility might be worth the trade-off. However, the team would need to manage the VM, handle security updates, and ensure scalability through load balancers or manual resizing.
* **Costs** : As the CMS app scales in terms of user traffic and computational needs, running multiple VMs or a powerful single VM can lead to higher costs. These costs would need to be carefully monitored and balanced against the flexibility provided by a VM.
