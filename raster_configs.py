import rasterio as rio
from rasterio.plot import show
from sklearn import cluster
import matplotlib.pyplot as plt
import matplotlib.colors as mc
import numpy as np
from numpy import inf
from osgeo import gdal, gdal_array

# Tell GDAL to throw Python exceptions, and register all drivers
gdal.UseExceptions()
gdal.AllRegister()

"""
Function to read the raster image and return it as a 3d array
"""


def read_raster(study_area_path, bands):
    raster = rio.open(study_area_path)
    print(raster.meta)
    # Read, enhance and show the image
    raster_arr = raster.read()  # read the opened image
    vmin, vmax = np.nanpercentile(raster_arr, (5, 95))  # 5-95% contrast stretch
    # print(raster_arr.shape)

    # change the order of the image to (height, width, bands) instead of (bands, height, width)
    # create an empty array with same dimension and data type
    imgxyb = np.empty((raster.height, raster.width, bands), raster.meta['dtype'])
    # loop through the raster's bands to fill the empty array
    for band in range(bands):
        imgxyb[:, :, band] = raster.read(band + 1)

    imgxyb[np.isnan(imgxyb)] = -9999
    imgxyb = imgxyb.astype(np.int16)
    print(imgxyb.shape)
    # print(imgxyb)
    return imgxyb


def get_from_raster_array(raster, band):
    return raster[:, :, band]


def set_band_to_raster_array(raster, band_id, band_array):
    raster[:, :, band_id] = band_array


"""
Function to write the raster image into a file
"""


def write_raster(raster, out_path):
    with rio.open(out_path, 'w') as dst:
        dst.write(raster)


# def random_forest_from_raster_data():

"""
Function to plot the image and the roi
"""


def plot_images(img_cube, roi_img,colors):

    n = 13
    n=roi_img.max()
    print(np.unique(roi_img))
    for k in colors:
        v = colors[k]
        _v = [_v / 255.0 for _v in v]
        colors[k] = _v

    index_colors = [colors[key] if key in colors else
                    (255, 255, 255, 0) for key in range(-100, n + 1)]
    cmap = plt.matplotlib.colors.ListedColormap(index_colors, 'Classification', len(index_colors))
    print(index_colors)
    # Plot the image and the roi
    plt.figure(figsize=[10, 10])
    plt.subplot(121)
    plt.imshow(img_cube[:, :, 0], cmap='gray')
    plt.title('Original image')
    plt.subplot(122)
    plt.imshow(roi_img, cmap=cmap, interpolation='none')
    plt.title('Classified image')
    plt.show()


"""
Function to separate the roi from the raster image
"""


def separate_roi_from_raster(raster, band_id_roi):
    new_raster = np.empty((raster.shape[0], raster.shape[1], raster.shape[2] - 1), raster.dtype)
    # get the bands except the roi band
    for band in range(raster.shape[2] - 2):
        new_raster[:, :, band] = raster[:, :, band]
    # Get the ROI image
    roi_img = raster[:, :, band_id_roi - 1]

    return new_raster, roi_img


"""
Function to get the important bands from the random forest
"""


def band_importance(rf, bands):
    for b, imp in zip(bands, rf.feature_importances_):
        print('Band {b} importance: {imp}'.format(b=b, imp=imp))


def color_stretch(image, index, minmax=(0, 10000)):
    colors = image[:, :, index].astype(np.float64)

    max_val = minmax[1]
    min_val = minmax[0]

    # Enforce maximum and minimum values
    colors[colors[:, :, :] > max_val] = max_val
    colors[colors[:, :, :] < min_val] = min_val

    for b in range(colors.shape[2]):
        colors[:, :, b] = colors[:, :, b] * 1 / (max_val - min_val)

    return colors


"""
Visualize the predictions
"""


def visualize_predictions( predict, colors, img543):
    n = predict.max()
    print(n)
    for k in colors:
        v = colors[k]
        _v = [_v / 255.0 for _v in v]
        colors[k] = _v

    index_colors = [colors[key] if key in colors else
                    (255, 255, 255, 0) for key in range(-100, n + 1)]
    cmap = plt.matplotlib.colors.ListedColormap(index_colors, 'Classification',len(index_colors))
    print(index_colors)
    # Now show the classmap next to the image
    plt.subplot(121)
    plt.imshow(img543)

    plt.subplot(122)
    plt.imshow(predict, cmap=cmap, interpolation='none')

    plt.show()
