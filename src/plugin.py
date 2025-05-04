from . import _
import requests

from Plugins.Plugin import PluginDescriptor
from Screens.TextBox import TextBox


class WanIP(TextBox):
	def __init__(self, session):
		TextBox.__init__(self, session, label="AboutScrollLabel")
		self.title = _("Wan IP")
		self.skinName = ["AboutOE", "About"]
		self.onShow.append(self.fetch)

	def fetch(self):
		ip = "Unknown"
		try:
			r = requests.get("http://whatsmyip.com")
			r.raise_for_status()
			i = r.content.find(b"copyToClipboard('")
			if i > -1:
				ip = r.content[i + 17:].split(b"'", 1)[0].decode()
		except Exception:
			pass
		self["AboutScrollLabel"].setText(f"Public IP: {ip}")


def PluginMain(session, **kwargs):
	session.open(WanIP)


def PluginStart(menuid, **kwargs):
	return menuid == "network" and [(_("Wan IP"), PluginMain, "PluginMain", 100)] or []


def Plugins(**kwargs):
	return [
		PluginDescriptor(
			name=_("Wan IP"), 
			description=_("Look up your Wan IP at whatsmyip.com"), 
			where=PluginDescriptor.WHERE_MENU, 
			fnc=PluginStart,)]