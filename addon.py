import xmbcaddon
import xmbcgui

addon=xmbcaddon.Addon()
addonname=addon.getAddonInfo("name")

line1 Movies
line2 Family Favorites

xmbcgui.Dialog().ok(addonname, line1,line2)

