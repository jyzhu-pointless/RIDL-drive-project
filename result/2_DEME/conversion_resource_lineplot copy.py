# Author: Sam Champer

from argparse import ArgumentParser
from PIL import Image
from numpy import linspace
from matplotlib import pyplot as plt
from matplotlib.colors import ListedColormap
import matplotlib.gridspec as gridspec
import matplotlib.font_manager as font_manager
import matplotlib as mpl
import numpy as np
# I keep some fonts in a folder other than my standard windows fonts
# If you want to use custom fonts, point the next line to a folder with your fonts.
# font_dirs = ["C:\Python38\plex"]
# font_files = font_manager.findSystemFonts(fontpaths=font_dirs)
# for ff in font_files:
#    font_manager.fontManager.addfont(ff)  #字体26
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
                     "legend.framealpha": 0.8,
                     "legend.fontsize": 24,
                     "legend.title_fontsize": 24,
                     "legend.facecolor": "white",
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


def lineplot(src, xcol, ycol, xlabel, ylabel, title, cbarlabel, trimmer):
    """
    Plots a lineplot.
    """
    with open(src, 'r') as f:
        data = f.read().splitlines()
        data = [line for line in data if line]
    data = data[1:]  # This trims off the header.

    

    #print(data)
    for i in range(len(data)):
        data[i] = data[i].split(',')
    drivename = data[0][0]
    # data = [list(map(float, line)) for line in data]
    # print(data)

    data = [entry for entry in data if entry[12] == "1"]

    subdata_1 = [entry for entry in data if entry[15] == "0.02" and float(entry[0]) <= 150]
    subdata_2 = [entry for entry in data if entry[15] == "0.04" and float(entry[0]) <= 150]
    subdata_3 = [entry for entry in data if entry[15] == "0.06" and float(entry[0]) <= 150]
    subdata_4 = [entry for entry in data if entry[15] == "0.08" and float(entry[0]) <= 150]
    subdata_5 = [entry for entry in data if entry[15] == "0.1" and float(entry[0]) <= 150]
    print("subdata_1:\n", subdata_5)

    all_x1 = [float(entry[xcol]) for entry in subdata_1]
    all_x2 = [float(entry[xcol]) for entry in subdata_2]
    all_x3 = [float(entry[xcol]) for entry in subdata_3]
    all_x4 = [float(entry[xcol]) for entry in subdata_4]
    all_x5 = [float(entry[xcol]) for entry in subdata_5]

    all_y1 = [float(entry[ycol]) for entry in subdata_1]
    all_y2 = [float(entry[ycol]) for entry in subdata_2]
    all_y3 = [float(entry[ycol]) for entry in subdata_3]
    all_y4 = [float(entry[ycol]) for entry in subdata_4]
    all_y5 = [float(entry[ycol]) for entry in subdata_5]

    # all_z = [float(entry[zcol]) for entry in data]
    x1_dim = len(set(all_x1))
    x2_dim = len(set(all_x2))
    x3_dim = len(set(all_x3))
    x4_dim = len(set(all_x4))
    x5_dim = len(set(all_x5))

    x_min = 1
    x_max = 100

    y1_dim = len(set(all_y1))
    y2_dim = len(set(all_y2))
    y3_dim = len(set(all_y3))
    y4_dim = len(set(all_y4))
    y5_dim = len(set(all_y5))

    y_min = 0
    y_max = 0.2
    # z_min = min(all_z)
    # z_max = max(all_z)
    plot_data_1 = [0.0 for i in range(x1_dim)]
    plot_data_1x = [0.0 for i in range(x1_dim)]
    plot_data_2 = [0.0 for i in range(x2_dim)]
    plot_data_2x = [0.0 for i in range(x2_dim)]
    plot_data_3 = [0.0 for i in range(x3_dim)]
    plot_data_3x = [0.0 for i in range(x3_dim)]
    plot_data_4 = [0.0 for i in range(x4_dim)]
    plot_data_4x = [0.0 for i in range(x4_dim)]
    plot_data_5 = [0.0 for i in range(x5_dim)]
    plot_data_5x = [0.0 for i in range(x5_dim)]

    for entry in subdata_1:
       x = float(entry[xcol])
       y = float(entry[ycol])
       # z = float(entry[zcol])
       x_coord = int(transform_range(x, x_min, x_max, 0, x1_dim - 1) + 0.5)
       if not np.isnan(y):
           y_coord = int(transform_range(y, y_min, y_max, 0, y5_dim - 1) + 0.5)
       else:
           y_coord = y
       plot_data_1x[x_coord] = x_coord + 0.5
       plot_data_1[x_coord] = y_coord + 0.5

    for entry in subdata_2:
       x = float(entry[xcol])
       y = float(entry[ycol])
       # z = float(entry[zcol])
       x_coord = int(transform_range(x, x_min, x_max, 0, x2_dim - 1) + 0.5)
       if not np.isnan(y):
           y_coord = int(transform_range(y, y_min, y_max, 0, y5_dim - 1) + 0.5)
       else:
           y_coord = y
       plot_data_2x[x_coord] = x_coord + 0.5
       plot_data_2[x_coord] = y_coord + 0.5
    
    for entry in subdata_3:
       x = float(entry[xcol])
       y = float(entry[ycol])
       # z = float(entry[zcol])
       x_coord = int(transform_range(x, x_min, x_max, 0, x3_dim - 1) + 0.5)
       if not np.isnan(y):
           y_coord = int(transform_range(y, y_min, y_max, 0, y5_dim - 1) + 0.5)
       else:
           y_coord = y
       plot_data_3x[x_coord] = x_coord + 0.5
       plot_data_3[x_coord] = y_coord + 0.5

    for entry in subdata_4:
       x = float(entry[xcol])
       y = float(entry[ycol])
       # z = float(entry[zcol])
       x_coord = int(transform_range(x, x_min, x_max, 0, x4_dim - 1) + 0.5)
       if not np.isnan(y):
           y_coord = int(transform_range(y, y_min, y_max, 0, y5_dim - 1) + 0.5)
       else:
           y_coord = y
       plot_data_4x[x_coord] = x_coord + 0.5
       plot_data_4[x_coord] = y_coord + 0.5
    
    for entry in subdata_5:
       x = float(entry[xcol])
       y = float(entry[ycol])
       # z = float(entry[zcol])
       x_coord = int(transform_range(x, x_min, x_max, 0, x5_dim - 1) + 0.5)
       if not np.isnan(y):
           y_coord = int(transform_range(y, y_min, y_max, 0, y5_dim - 1) + 0.5)
       else:
           y_coord = y
       plot_data_5x[x_coord] = x_coord + 0.5
       plot_data_5[x_coord] = y_coord + 0.5

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
    ax.set_xticks([i+0.5 for i in linspace(0, x5_dim-1, 5)])  # This line creates six ticks on the x axis which are centered on the column they correspond to.
    ax.set_yticks([i+0.5 for i in linspace(0, y5_dim-1, 5)])  # This line creates six ticks on the y axis which are centered on the row they correspond to.
    #ax.set_xticklabels([2.0,4.0,6.0,8.0,10.0,12.0])
    # ax.set_xticklabels([0,0.4,0.8,1.2,1.6,2.0])
    # ax.set_yticklabels([0.8,0.84,0.88,0.92,0.96,1])
    ax.set_xticklabels([0,25,50,75,100])
    ax.set_yticklabels([0,0.05,0.1,0.15,0.2])
    ax.set_xlim((0,x5_dim))
    ax.set_ylim((0,y5_dim))
    #ax.set_yticklabels([0.01,0.02,0.03,0.04,0.05,0.06])
    #ax.set_yticklabels([f"{i:.0f}" for i in linspace(x_min, x_max, 6)])
    #ax.set_yticklabels([f"{i:.1f}" for i in linspace(y_min, y_max, 6)])
    ax.set_aspect('equal')  #set the aspect of the axis scaling
    
    # You might want to change z_min and z_max to the actual min and max values for your data.
    # E.g. if your most extreme possible values are [0, 1], but your dataset only has values in [0.02, 0.95],
    # then you should probably override the next line to explicitly set vmin and vmax to 0 and 1.
    hm1 = ax.plot(plot_data_1x, plot_data_1, '-')
    hm2 = ax.plot(plot_data_2x, plot_data_2, '-')
    hm3 = ax.plot(plot_data_3x, plot_data_3, '-')
    hm4 = ax.plot(plot_data_4x, plot_data_4, '-')
    hm5 = ax.plot(plot_data_5x, plot_data_5, '-')
    # ax.legend(["0.02","0.04","0.06","0.08","0.10"],loc="upper right",title="Migration rate",ncol=2)
    #hm1 = mpl.colors.Normalize(0, 500)
    #fig.colorbar(hm, ax = ax, fraction=0.045)
    

    # The next block of code is for creating the colorbar for the heatmap.
    #cbfig = plt.figure(figsize=(1.5,8.5))# 8.5,1.2
    #cbfig.subplots_adjust(right=0.15)
    #cbfig.set_tight_layout({"pad":0.4, "w_pad":0.0, "h_pad":0.0})
    #cbspec = gridspec.GridSpec(ncols=1, nrows=1, figure=cbfig)
    #cbax = cbfig.add_subplot(cbspec[0, 0])
    #colorbar = cbfig.colorbar(hm, cax=cbax, orientation='vertical')#horizontal vertical
    #colorbar.set_label(f"{cbarlabel}")

    #save_and_display(fig, f"{src[:-4]}.png")
    save_and_display(fig, f"{src}_min_freq_100_lineplot.png")
    #save_and_display(cbfig, f"colorbar.png")
    plt.show()

def main():
    # Get args from arg parser:
    parser = ArgumentParser()
    parser.add_argument('-src', '--source', default="average_data.csv", type=str, help="CSV file to make heatmap from.")
    parser.add_argument('-x','--X_COL', default=0, type=int, help="The column of the entries in X.")
    parser.add_argument('-y','--Y_COL', default=10, type=int, help="The column of the entries in Y.")
    # parser.add_argument('-z','--Z_COL', default=3, type=int, help="The column of the entries in Z [i.e. the color].")
    parser.add_argument('-x_label', '--X_LABEL', default="Weeks", type=str, help="Label for the x axis.")#Low density growth rate
    parser.add_argument('-y_label', '--Y_LABEL', default="Juvenile drive frequency", type=str, help="Label for the Y axis.")#Migration rate
    parser.add_argument('-title', '--TITLE', default="", type=str, help="Title of the graph.")
    parser.add_argument('-cbar', '--CBARLABEL', default="COLOR BAR LABEL", type=str, help="Label for the colorbar.")
    parser.add_argument('-t', '--TRIMMER', default=1, type=int, help="Data trimmer.")
    arg = vars(parser.parse_args())

    # Here are some nice color schemes to choose from:
    seismic = plt.get_cmap("seismic")
    # magma = plt.get_cmap("magma")
    Reds = plt.get_cmap('Reds')
    greens = plt.get_cmap('Greens')
    Purples = plt.get_cmap('Purples')
    copper = plt.get_cmap("copper")
    brg = plt.get_cmap("brg")
    hsv = plt.get_cmap('hsv')
    # RdGy = plt.get_cmap("RdGy")
    # Accent = plt.get_cmap("Accent")
    twilight_shifted = plt.get_cmap("twilight_shifted")
    seismic = plt.get_cmap("seismic")
    # Choose a color scheme by specifying it on the next line:
    # color_range = Reds(linspace(0, 1, 1000))
    # color_range = copper(linspace(1, 0, 1000))
    color_range = Reds(linspace(1, 0, 1000))

    # A color scheme can also be an explicit list of hex codes for each color:
    # color_range = ["#ca0020", "#f4a582", "#C4C4C4", "#92c5de", "#0060b0"]
    # color_range = ["#ca0020", "#f4a582"]
    # colormap = ListedColormap(color_range)
    # print(colormap)
    lineplot(arg["source"], arg["X_COL"], arg["Y_COL"], arg["X_LABEL"], arg["Y_LABEL"], arg["TITLE"], arg["CBARLABEL"], arg["TRIMMER"])


if __name__ == "__main__":
    main()
