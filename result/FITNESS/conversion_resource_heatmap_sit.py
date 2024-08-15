# Author: Sam Champer

import cmath
from argparse import ArgumentParser
from PIL import Image
from numpy import linspace
from numpy import vstack
from matplotlib import pyplot as plt
from matplotlib.colors import ListedColormap
import matplotlib.gridspec as gridspec
import matplotlib.font_manager as font_manager
import matplotlib as mpl
import numpy as np
# I keep some fonts in a folder other than my standard windows fonts
#  If you want to use custom fonts, point the next line to a folder with your fonts.
#font_dirs = ["C:\Python38\plex"]
#font_files = font_manager.findSystemFonts(fontpaths=font_dirs)
#for ff in font_files:
 #   font_manager.fontManager.addfont(ff)  #字体26
plt.style.use('ggplot')
plt.rcParams.update({'font.size': 40,
                     'font.family': "Times New Roman",
                     #'font.sans-serif': "IBM Plex Sans",       # This is my prefered font. It's open source and available on github if you'd like to use it too.
                     #"figure.titlesize": 18,
                     "axes.titlesize": 40,     #fig title
                     "axes.labelsize": 40,
                     "savefig.pad_inches": 0,
                     "legend.fontsize": 2,
                     "axes.labelpad": 0.1,
                     "axes.linewidth":1.2,
                     "text.color": "black",
                     "axes.labelcolor": "black",
                     "xtick.color": "black",
                     "ytick.color": "black",
                     "xtick.major.size": 5.0,
                     "xtick.major.width":1.5,
                     "xtick.major.pad":0.1,
                     "ytick.major.size": 5.0,
                     "ytick.major.width":1.5,
                     "ytick.major.pad":0.1,
                     "legend.framealpha": 0.2,
                     ""
                    # "figure.dpi": 400,
                     #"savefig.dpi": 400,
                     "patch.facecolor": "white"})

plt.subplots_adjust(left=0.45)
plt.subplots_adjust(right=0.5)

def save_and_display(fig, image_name):
    # Save and display a figure.
    fig.savefig(image_name)
    im = Image.open(image_name)
    im.show()


def transform_range(val, prev_min, prev_max, new_min, new_max):
    # Transform a value from one range to another.
    return (((val - prev_min) * (new_max - new_min)) / (prev_max - prev_min)) + new_min

def heatmap(src, xcol, ycol, zcol, xlabel, ylabel, title, cbarlabel, colormap, colormap_display):
    """
    Plots a heatmap.
    """
    with open(src, 'r') as f:
        data = f.read().splitlines()
        data = [line for line in data if line]
    data = data[883:1324]  # This trims off the header.
    print(data)
    for i in range(len(data)):
        data[i] = data[i].split(',')
        data[i] = data[i][0:2] + data[i][5:6]
    drivename = data[0][0]
    # data = [list(map(float, line)) for line in data]
    all_x = [float(entry[xcol]) for entry in data]
    all_y = [float(entry[ycol]) for entry in data]
    all_z1 = [float(entry[zcol]) for entry in data]
    all_z = [float(-50) if np.isnan(value) else value for value in all_z1]
    print(all_z)
    x_dim = len(set(all_x))
    x_min = min(all_x)
    x_max = max(all_x)
    print(x_min)
    print(x_max)
    y_dim = len(set(all_y))
    y_min = min(all_y)
    y_max = max(all_y)
    z_min = min(all_z)
    z_max = max(all_z)
    plot_data = [[0.0 for i in range(x_dim)] for i in range(y_dim)]

    for entry in data:
        x = float(entry[xcol])
        y = float(entry[ycol])
        z = float(entry[zcol])
        if (np.isnan(z)):
            z = -50.0
        x_coord = int(transform_range(x, x_min, x_max, 0, x_dim - 1) + 0.5)
        y_coord = int(transform_range(y, y_min, y_max, 0, y_dim - 1) + 0.5)
        plot_data[y_coord][x_coord] = z

    fig = plt.figure(figsize=(8.7,8.5))  # Confure the desired figure size.
    spec = gridspec.GridSpec(ncols=1, nrows=1, figure=fig) #place
    ax = fig.add_subplot(spec[0, 0])

    # Adjust the next line if the figure or legends are not well aligned with the edge of the image.
    fig.set_tight_layout({"pad":0.4, "w_pad":0.0, "h_pad":0.0})
    ax.set_title(f"{title}")   #, {drivename}")
    ax.set_xlabel(f"{xlabel}")
    ax.set_ylabel(f"{ylabel}")
    #ax.set_xticks([0.1,0.2,0.3,0.4,0.5,0.6]])
    #ax.set_yticks(np.arrange(data.shape[]))
    ax.set_xticks([i+0.5 for i in linspace(0, x_dim-1, 6)])  # This line creates six ticks on the x axis which are centered on the column they correspond to.
    ax.set_yticks([i+0.5 for i in linspace(0, y_dim-1, 7)])  # This line creates six ticks on the y axis which are centered on the row they correspond to.
    #ax.set_xticklabels([2.0,4.0,6.0,8.0,10.0,12.0])
    # ax.set_xticklabels([0,0.4,0.8,1.2,1.6,2.0])
    # ax.set_yticklabels([0.8,0.84,0.88,0.92,0.96,1])
    ax.set_xticklabels([0.5,0.6,0.7,0.8,0.9,1.0])
    ax.set_yticklabels([0,2,4,6,8,10,12])
    #ax.set_yticklabels([0.01,0.02,0.03,0.04,0.05,0.06])
    #ax.set_yticklabels([f"{i:.0f}" for i in linspace(x_min, x_max, 6)])
    #ax.set_yticklabels([f"{i:.1f}" for i in linspace(y_min, y_max, 6)])
    ax.set_aspect('equal')  #set the aspect of the axis scaling
    # You might want to change z_min and z_max to the actual min and max values for your data.
    # E.g. if your most extreme possible values are [0, 1], but your dataset only has values in [0.02, 0.95],
    # then you should probably override the next line to explicitly set vmin and vmax to 0 and 1.
    hm1 = ax.pcolormesh(plot_data, cmap = colormap_display, rasterized=True, vmin=0, vmax=300)
    #hm2 = ax.pcolormesh(plot_data, cmap = colormap, rasterized=True, vmin=0, vmax=100)
    #hm1 = mpl.colors.Normalize(0, 500)
    #fig.colorbar(hm, ax = ax, fraction=0.045)
    

    # The next block of code is for creating the colorbar for the heatmap.
    cbfig = plt.figure(figsize=(8.5,1.2))# 8.5,1.2
    cbfig.subplots_adjust(right=0.15)
    cbfig.set_tight_layout({"pad":0.4, "w_pad":0.0, "h_pad":0.0})
    cbspec = gridspec.GridSpec(ncols=1, nrows=1, figure=cbfig)
    cbax = cbfig.add_subplot(cbspec[0, 0])
    colorbar = cbfig.colorbar(hm1, cax=cbax, orientation='horizontal')#horizontal vertical
    # plt.clim(0, 100) 
    #colorbar.set_label(f"{cbarlabel}")

    hm = ax.pcolormesh(plot_data, cmap = colormap, rasterized=True, vmin=-50, vmax=300)

    #save_and_display(fig, f"{src[:-4]}.png")
    save_and_display(fig, f"{src}_heatmap_sit.png")
    #save_and_display(cbfig, f"colorbar.png")
    save_and_display(cbfig, f"{src}_colorbar_glf_sit.png")
    plt.show()


def main():
    # Get args from arg parser:
    parser = ArgumentParser()
    parser.add_argument('-src', '--source', default="generation_to_suppression.csv", type=str, help="CSV file to make heatmap from.")
    parser.add_argument('-x','--X_COL', default=0, type=int, help="The column of the entries in X.")
    parser.add_argument('-y','--Y_COL', default=1, type=int, help="The column of the entries in Y.")
    parser.add_argument('-z','--Z_COL', default=2, type=int, help="The column of the entries in Z [i.e. the color].")
    parser.add_argument('-x_label', '--X_LABEL', default="SIT fitness", type=str, help="Label for the x axis.")#Low density growth rate
    parser.add_argument('-y_label', '--Y_LABEL', default="Drop ratio", type=str, help="Label for the Y axis.")#Migration rate
    parser.add_argument('-title', '--TITLE', default="", type=str, help="Title of the graph.")
    parser.add_argument('-cbar', '--CBARLABEL', default="COLOR BAR LABEL", type=str, help="Label for the colorbar.")
    arg = vars(parser.parse_args())

    # Here are some nice color schemes to choose from:
    seismic = plt.get_cmap("seismic")
    magma = plt.get_cmap("magma")
    Reds = plt.get_cmap('Reds')
    Greens = plt.get_cmap('Greens')
    Purples = plt.get_cmap('Purples')
    copper = plt.get_cmap("copper")
    brg = plt.get_cmap("brg")
    hsv = plt.get_cmap('hsv')
    Greys = plt.get_cmap('Greys')
    #RdGy = plt.get_cmap("RdGy")
    #Accent = plt.get_cmap("Accent")
    twilight_shifted = plt.get_cmap("twilight_shifted")
    seismic = plt.get_cmap("seismic")
    # Choose a color scheme by specifying it on the next line:
    # color_range = Reds(linspace(0, 1, 1000))
    # color_range = copper(linspace(1, 0, 1000))
    color_range_1 = magma(linspace(1, 0, 3000))
    color_range_2 = Greys(linspace(0.5, 0.5, 500))
    color_range = vstack((color_range_2, color_range_1))

    # A color scheme can also be an explicit list of hex codes for each color:
    # color_range = ["#ca0020", "#f4a582", "#C4C4C4", "#92c5de", "#0060b0"]
    #color_range = ["#ca0020", "#f4a582"]
    colormap = ListedColormap(color_range)
    colormap_display = ListedColormap(color_range_1)
    print(colormap)
    heatmap(arg["source"], arg["X_COL"], arg["Y_COL"], arg["Z_COL"], arg["X_LABEL"], arg["Y_LABEL"], arg["TITLE"], arg["CBARLABEL"], colormap, colormap_display)


if __name__ == "__main__":
    main()
