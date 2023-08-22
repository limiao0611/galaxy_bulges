import matplotlib
# Force matplotlib to not use any Xwindows backend.
matplotlib.use('Agg')
import yt
yt.enable_parallelism()
import matplotlib.pyplot as plt
from mpl_toolkits.axes_grid1 import AxesGrid

def get_fn(i):
    a0=''
    if (i<10):
      a0='000'
    if (10<=i<100):
      a0='00'
    if (100<=i<999):
      a0='0'
    filen='DD'+a0+str(i)+'/sb_'+a0+str(i)
    return filen

def _z_den_flux(field,data):
    return abs(data['density']*data['z-velocity'])

def _CR_Energy_Density(field,data):
    return data['CREnergyDensity']* data.ds.mass_unit/data.ds.length_unit/data.ds.time_unit**2

def see(i):
  fn = get_fn(i)
  ds = yt.load(fn)
  fig = plt.figure()
  grid = AxesGrid(fig, (0.075,0.075,0.70,0.90), 
                nrows_ncols = (2,2),
                axes_pad = 1,
                label_mode = "1",
                share_all = True,
                cbar_location="right",
                cbar_mode="each",
                cbar_size="40%",
                cbar_pad="0%")
#  fields = ['number_density','temperature','SN_Colour','z-velocity']
#  fields = ['number_density','temperature','pressure','z-velocity']#,'CR_Energy_Density','z_den_flux']
  fields = ['number_density','temperature','pressure','radial_velocity']#,'CR_Energy_Density','z_den_flux']
#  fields = ['density','temperature','pressure','SN_Colour']#,'CR_Energy_Density','z_den_flux']
#  fields = ['density','temperature','entropy','SN_Colour']#,'CR_Energy_Density','z_den_flux']
  c1 = [0.0,0.0,0.0]
  p=yt.SlicePlot(ds,'x',fields,center=c1,axes_unit='kpc',fontsize=12) #, width=(2,'kpc'))
  p.set_unit('radial_velocity','km/s')
#  p.set_unit('z-velocity','km/s')
#  p.set_zlim('number_density',1e-3, 1e3)
#  p.set_zlim('temperature',1e4,1e9)
#  p.set_zlim('pressure',1e-13,1e-9)
#  p.set_zlim('pressure',1e-11,1e-9)
#  p.set_zlim('z-velocity',-6e3,6e3)
#  p.set_zlim('entropy',5,200)
#  p.set_zlim('SN_Colour',1e2,1e6)
  p.annotate_timestamp(corner='upper_left',time_unit='Myr',text_args={'color':'black'})
  for j, field in enumerate(fields):
    plot = p.plots[field]
    plot.figure = fig
    plot.axes = grid[j].axes
    plot.cax = grid.cbar_axes[j]
  p._setup_plots()
  p.annotate_timestamp(corner='upper_left',time_unit='Myr',text_args={'color':'black'})
  if yt.is_root():
     plt.savefig('multi_x_slice_'+str(i)+'_2.png')

yt.add_field('z_den_flux',function=_z_den_flux, units  = 'Msun/yr/kpc**2')
num=[0,1,2,3,4,5]
num=range(0,132,5)
for i in num:
   see(i)


