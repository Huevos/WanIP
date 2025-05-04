DESCRIPTION = "tool to look up your Wan IP at whatsmyip.com"
MAINTAINER = "Huevos"

inherit gitpkgv allarch python3native

require conf/license/license-gplv2.inc

PV = "1.0+git"
PKGV = "1.0+git${GITPKGV}"

SRCREV = "${AUTOREV}"

SRC_URI = "git://github.com/Huevos/WanIP.git;protocol=https;branch=master"



S = "${WORKDIR}/git"

pluginpath = "/usr/lib/enigma2/python/Plugins/SystemPlugins/WanIP"

do_install:append() {
	install -d ${D}${pluginpath}
	cp -r ${S}/src/* ${D}${pluginpath}/
	python3 -m compileall -o2 -b ${D}
}

FILES:${PN} = "${pluginpath}/"
