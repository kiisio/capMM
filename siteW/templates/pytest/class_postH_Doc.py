# coding=utf-8

class PostH_Doc:

#format 'adresse nom' (split)
        

        def __init__(self):
                self.nom = ''
                self.adresse = ''
                self.logo = ''

		
        def get_row_col_sm_6_col_md_4(self):
                RcS6_md4 = """<div class="col-sm-6 col-md-4"><div class="thumbnail"><div class="caption"><h3>%s</h3><img src="logos/%s.jpg" alt="%s" href="%s"><div class="caption"><a href="%s" class="btn btn-primary" role="button">%s</a> <a href="%s" class="btn btn-default" role="button">Button</a></div></div></div>
			""" % (self.nom, self.nom, self.nom, self.adresse, self.adresse, self.nom, self.adresse)

                return RcS6_md4


listeadresse =[
        'http://apache.ariens.com/cgibin/ctrg0005?SESSIONID=0.7645641020634929&Site=ARIENSS  Ariens', 'https://partsradar.arinet.com/scripts/EmpartISAPI.dll?MF&app=ariens&lang=EN&TF=Empartweb&loginID=ariensc&loginpwd=consumer Gravely', 'https://www.powertools-aftersalesservice.com/public/bosch-pt/service?lgRedirect=true&p_p_id=BoschWSRP&p_p_lifecycle=0&p_p_state=normal&p_p_mode=view&p_p_col_id=column-1&p_p_col_count=1&_BoschWSRP_wsrp-navigationalState=%2FWFS%2FPTASA-PT-SIS-Site%2Ffr_FR%2F-%2FEUR%2FViewSearch-StartSimple%3Bpgid%3D4f6c5036edb663d5e70ec6175495j6GAX8nG%3Bsid%3DA8yrRbWjp8ZOc_42HGInuboooi_DrxRAayY%3D&_BoschWSRP_proxyportlet-remoteInvocation=true  Bosch Dremel, Skil', 'https://www.briggsandstratton.com/na/en_us/home.html  Briggs and stratton', 'https://www.echo-usa.com/documentation.asp  Echo', 'http://www.gardif.fr/index.php?page=famille&id=7  Gardif', 'https://www.honda-engines-eu.com/fr/web/eec-public-site/spare-parts  Honda ', 'http://www.outdoordistributors.com/hydrogear/hydrogear_search.html  Hydro-Gear', 'https://www.ggpfrance.net/index.php/documents/catalogue-pieces-de-rechanges  GGP / Castelgarden', 'https://jdpc.deere.com/jdpc/servlet/com.deere.u90490.partscatalog.view.servlets.HomePageServlet_Alt  John-Deere', 'https://www.jonsered.com/fr/support/doumentation-technique/  Jonsered', 'https://kmcb2c.econnect.partsandwarranty.com/kmcb2c/main.jsp  Kawasaki', 'https://www.mcculloch.com/fr/aide-support-mcculloch/documentation-technique-mcculloch/  McCulloch', 'https://www.pilote88.com/eclates-produits.html  Pilote-88', 'https://euc.robin-fhi.co.jp/parts_catalog/model.aspx?lang=e&slang=e  Subaru / Robin ', 'https://www.snapper.com/na/en_us/support/manuals.html  Snapper', 'https://lookup3.toro.com/partdex/index.cfm?xCaller=Toro  Toro', 'http://cyclovap.fr/eclates-moteurs  Vap', 'https://www.zenoah.co.jp/int/downloads/  Zenoah', 'https://www.shoplawnboy.com/Comergent/en/US/adirect/Toro?cmd=ToroLBOnlineModelLookup  Lawn Boy', 'http://www.mtdparts.com/equipment/mtdparts  Bolens MTD Yard man Yard machine' 'http://www.servitech.fr/  Karcher Black Decker Dewalt Vaporetto Vaporella Polti Kew Alto Elu Sanivap Ducati']      

for mark in listeadresse:
	tmp = mark.split()
	name = tmp[1]
	adresse = tmp[0]
	name = PostH_Doc()
	name.nom = tmp[1]
	name.adresse = adresse
	name.logo = tmp[1]
	f = open('test.html','a')
	f.write(name.get_row_col_sm_6_col_md_4())
	f.close()