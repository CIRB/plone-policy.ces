from Products.CMFCore.utils import getToolByName
import logging

logger = logging.getLogger('CES policy')

def clean_up_splashpage(portal_setup):
	portal = getToolByName(portal_setup, 'portal_url').getPortalObject()
	portal.manage_delObjects(['index_html', 'copy_of_index_html', 
		'index_html_test', 'index_test2'])
	logger.info('splash pages cleaned up')

def language_setup_folders(portal_setup):
	portal = getToolByName(portal_setup, 'portal_url').getPortalObject()
	view = portal.restrictedTraverse('@@language-setup-folders')
	view()
	logger.info('language folders set up')
	view = portal.restrictedTraverse('@@language-move-folders')
	view()
	logger.info('Content move in language folders')



# esrbhg/agenda/agenda
# Members/pvandenabeele/calendarxfolder.2010-09-09.5898499746
# zone-membres/ccm/assemblee-pleniere-ccm/calendrier-des-reunions/agenda-chambre-des-classes-moyennes