import matplotlib.pyplot as plt
import matplotlib as mpl
from mytools import colormap_utils as mycolors
import importlib
import numpy as np
import matplotlib.colors as colors

def plotcolorbar(fig, ci, cmin, cmax, titlestr, x1, x2, y1, y2,
   cmap='blue2red', orient='horizontal', posneg='both', ticks=None, fsize=14, nowhite=False,
   contourlines=False, contourlinescale=1, posonly=False):
    """plot a color bar
       Input:
           fig = the figure identified
           ci = the contour interval for the color map
           cmin = the minimum extent of the contour range
           cmax = the maximum extent of the contour range
           titlestr = the label for the color bar
           x1 = the location of the left edge of the color bar
           x2 = the location of the right edge of the color bar
           y1 = the location of the bottom edge of the color bar
           y2 = the location of the top edge of the color bar
           cmap = the color map to be used (only set up for blue2red at the moment)
           orient = the orientation (horizontal or vertical)
           posneg = if "both", both positive and negative sides are plotted
                    if "pos", only the positive side is plotted
                    if "net", only the negative side is plotted
           ticks = user specified ticklabels
           fsize = user specified font size
           contourlines = used to overplot contour lines
           contourlinescale = scale factor for contour lines to be overplotted
    """

    # set up contour levels and color map
    nlevs = (cmax-cmin)/ci + 1
    clevs = ci * np.arange(cmin/ci, (cmax+ci)/ci, 1)

    if (cmap == "blue2red"):
        mymap = mycolors.blue2red_cmap(nlevs, nowhite, posonly=posonly)
        #mymap = blue2red_cmap(nlevs, nowhite, posonly=posonly)


    if (cmap == "precip"):
        mymap = mycolors.precip_cmap(nlevs, nowhite)
        #mymap = precip_cmap(nlevs, nowhite)


    if (cmap == "precip_nowhite"):
        mymap = mycolors.precip_cmap_nowhite(nlevs)
        #mymap = precip_cmap_nowhite(nlevs)

    if (cmap == 'red2blue'):
        mymap = mycolors.red2blue_cmap(nlevs, nowhite)
        #mymap = red2blue_cmap(nlevs, nowhite)



    clevplot=clevs
    if (posneg == "pos"):
        clevplot = clevs[clevs >= 0]
    if (posneg == "neg"):
        clevplot = clevs[clevs <= 0]

    norm = mpl.colors.Normalize(vmin=cmin, vmax=cmax)

    ax = fig.add_axes([x1, y1, x2-x1, y2-y1])

    if (ticks):
        clb = mpl.colorbar.ColorbarBase(ax, cmap=mymap,
           orientation=orient, norm=norm, values=clevplot, ticks=ticks)
    else:
        clb = mpl.colorbar.ColorbarBase(ax, cmap=mymap,
           orientation=orient, norm=norm, values=clevplot)

    clb.ax.tick_params(labelsize=fsize)
    clb.set_label(titlestr, fontsize=fsize+2)

    if (contourlines):
        #clevlines = (clevs+ci/2.)*contourlinescale
        #clevlines = clevs - ci/2.
       # clevlines = clevs[np.abs(clevlines) > ci/2.]
       # clevlines = clevlines - ci
       # clevlines = clevlines[np.abs(clevlines) > ci/2.]
       # clevlines = clevs - ci/2.
       # test = (np.arange(0,len(clevs),1) / contourlinescale).astype(int)*contourlinescale == np.arange(0,len(clevs),1)
       # clevs = clevs[test]
       # clevlines = clevs

       # clevlines = clevlines[ test ]
       # clevlines = clevs
        clevlines = clevs*contourlinescale
        #clevlines = clevs*contourlinescale
        #clevlines = clevlines - ci/2.
        #clevlines = clevs*contourlinescale
        #clevlines = clevlines - (ci/2.*contourlinescale)
        clevlines = clevlines[np.abs(clevlines) > ci/2.]
        #clevlines = clevlines - ci/2.
#        clevlines = clevlines[np.abs(clevlines) > ci/10.]
        if (orient=='horizontal'):
            ax.vlines(clevlines[clevlines > 0]-ci/2.,-5,5, colors='black', linestyle='solid')
            ax.vlines(clevlines[clevlines < 0]+ci/2.,-5,5, colors='black', linestyle='dashed')
        if (orient=='vertical'):
            ax.hlines(clevlines[clevlines > 0]-ci/2.,-10,15, colors='black', linestyle='solid')
            ax.hlines(clevlines[clevlines < 0]+ci/2.,-10,15, colors='black', linestyle='dashed')


    return ax


