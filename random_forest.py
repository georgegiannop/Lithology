import numpy as np
import raster_configs as rc
from sklearn.ensemble import RandomForestClassifier
import pandas as pd
import pickle

if __name__ == '__main__':
    colors = dict((
        (-100, (0, 0, 0, 255)),  # Nodata
        (0, (0, 150, 0, 255)),  # green
        (1, (0, 0, 255, 255)),  # blue--
        (2, (0, 255, 0, 255)),  # light green---
        (4, (160, 82, 45, 255)),  # kafe
        (13, (255, 0, 0, 255))  # red-
    ))
    # load the raster and show its shape
    img_raster = rc.read_raster("EGU_Dataset/Exarchos_cube.tif", 25)
    print(img_raster.shape)
    # separate the raster to roi and the rest of the image
    sep_img_raster, roi_img = rc.separate_roi_from_raster(img_raster, 25)
    print("raster shap" + str(sep_img_raster.shape))
    print("roi" + str(roi_img.shape))
    # plot the images
    rc.plot_images(sep_img_raster, roi_img,colors)
    # Find how many non-zero entries we have -- i.e. how many training data samples?
    n_samples = (roi_img >= 0).sum()
    print('We have {n} samples'.format(n=n_samples))
    # What are our classification labels?
    labels = np.unique(roi_img[roi_img >= 0])
    print('The training data include {n} classes: {classes}'.format(n=labels.size,
                                                                    classes=labels))

    # We will need a "X" matrix containing our features, and a "y" array containing our labels
    #     These will have n_samples rows
    #     In other languages we would need to allocate these and them loop to fill them, but NumPy can be faster

    X = sep_img_raster[roi_img >= 0, :]
    y = roi_img[roi_img >= 0]
    print('After masking, our X matrix is sized: {sz}'.format(sz=X.shape))
    print('After masking, our y array is sized: {sz}'.format(sz=y.shape))
    """
    # Initialize our model with 500 trees
    rf = RandomForestClassifier(n_estimators=500, oob_score=True)
    
    # Fit our model to training data
    rf = rf.fit(X, y)

    with open('./rf', 'wb') as f:
        pickle.dump(rf, f)

    # in your prediction file
    """
    with open('./rf', 'rb') as f:
        rf = pickle.load(f)

    print('Our OOB prediction of accuracy is: {oob}%'.format(oob=rf.oob_score_ * 100))

    # Print the bands in order of importance
    bands = [band for band in range(1, 24)]
    rc.band_importance(rf, bands)

    # Setup a dataframe -- just like R
    df = pd.DataFrame()
    df['truth'] = y
    df['predict'] = rf.predict(X)

    # Cross-tabulate predictions
    print(pd.crosstab(df['truth'], df['predict'], margins=True))

    # Now let's predict the whole image
    new_shape = (sep_img_raster.shape[0] * sep_img_raster.shape[1], sep_img_raster.shape[2])

    img_as_array = sep_img_raster[:, :, :].reshape(new_shape)
    print('Reshaped from {o} to {n}'.format(o=sep_img_raster.shape,
                                            n=img_as_array.shape))

    # Now predict for each pixel
    class_prediction = rf.predict(img_as_array)

    # Reshape our classification map
    class_prediction = class_prediction.reshape(sep_img_raster[:, :, 0].shape)
    img543 = rc.color_stretch(sep_img_raster, [4, 3, 2], (0, 8000))



    rc.visualize_predictions(class_prediction, colors, img543)
