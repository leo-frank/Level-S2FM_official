# from hloc import extract_features, match_features, reconstruction, pairs_from_exhaustive, visualization
from hloc.visualization import plot_images, read_image
from hloc.utils.viz_3d import init_figure, plot_points, plot_reconstruction, plot_camera_colmap
import pycolmap
reconstruction = pycolmap.Reconstruction("levels2fm-opendata/DTU/scan65/sparse")
print(reconstruction.summary())
fig = init_figure()
plot_reconstruction(fig, reconstruction)
fig.show()