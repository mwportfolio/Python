from diagrams import Diagram, Cluster
from diagrams.custom import Custom
from diagrams.generic.network import Subnet
from diagrams.onprem.network import Internet
from diagrams.generic.os import Windows, LinuxGeneral
from diagrams.generic.blank import Blank
from diagrams.generic.virtualization import Virtualbox
from urllib.request import urlretrieve

with Diagram("Malware Lab", show=False, direction="TB"):
	vbox = Virtualbox("VirtualBox")
	subnet = Subnet("172.30.20.0/24")

	with Cluster("Traffic Gateway 172.30.20.1"):
		linux_server = LinuxGeneral("Debian VM")

		with Cluster("Apps"):
			polarproxy_url = "https://www.netresec.com/images/PolarProxy_313x313.png"
			urlretrieve(polarproxy_url, "polarproxy.png")
			polarproxy = Custom("PolarProxy", "polarproxy.png")

			tshark_url = "https://assets.labs.ine.com/web/badges/low/tshark.png"
			urlretrieve(tshark_url, "tshark.png")
			tshark = Custom("tshark", "tshark.png")

	with Cluster("Client Workstation 172.30.20.2"):
		windows_client = Windows("MSEdge VM")

		with Cluster("Content"):
			vx_underground_url = "https://pbs.twimg.com/profile_images/1284217861318344706/m__Wj5eV_400x400.jpg"
			urlretrieve(vx_underground_url, "vx_underground.jpg")
			malware = Custom("Malware Samples", "vx_underground.jpg")

	vbox - subnet 
	subnet - linux_server
	subnet - windows_client


