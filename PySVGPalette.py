import colorsys
import numpy as np
import seaborn as sns
from matplotlib import patches
import matplotlib.colors as mcl
import matplotlib.pyplot as plt
plt.switch_backend('TkAgg')


def rgb_to_mplrgb(a):
    return np.array(a) / 255.


def mplrgb_to_rgb(a):
    return np.array(a) * 255.


def mplhls_to_hls(a):
    return (a[0] * 360, a[1] * 100, a[2] * 100)


def display_palette(p):
    a = []
    print 'RGB\t HLS'
    for p in palette:
        print mcl.rgb2hex(p),
        print ['{:.2f}'.format(cc) for cc in mplrgb_to_rgb(p)],
        print ['{:.2f}'.format(cc) for cc in mplhls_to_hls(colorsys.rgb_to_hls(*p))]
        # print ['{:1.2f}'.format(cc * hls_scale[i])
        #        for i, cc in enumerate(mcl.rgb_to_hsv(p))]
        a.append(
            mplhls_to_hls(colorsys.rgb_to_hls(*p)))
    sns.palplot(palette)
    return a

# ======================================================================
# COLOR SCHEMER
# ======================================================================
# BEIGETONE
RGB = [
    (176, 102, 96),
    (202, 143, 66),
    (171, 156, 115),
    (94, 119, 3),
    (106, 125, 142),
    mplrgb_to_rgb(
        colorsys.hls_to_rgb(90./360, 0.85, 0.15))
]
palette = rgb_to_mplrgb(RGB)
print np.array(palette) * 255.

# HSL
n_colors = 24.
print "Angle step: {:g}".format(360/n_colors)
palette_base = sns.hls_palette(n_colors, h=0, l=.5, s=1)


fig, (ax) = plt.subplots(1, figsize=(1920/120., 1080/120.), tight_layout=True)
print (fig.get_figwidth(), fig.get_figheight())
# fig.patch.set_facecolor(palette[-1])

ax.set_axis_bgcolor(palette[-1])
ax.set_aspect('equal')
ax.set_xlim(0, n_colors)
ax.set_ylim(0, n_colors)
ax.get_xaxis().set_visible(False)
ax.get_yaxis().set_visible(False)
# ax.set_axis_off()

for i, cc in enumerate(palette):
    ax.add_patch(
        patches.Rectangle((i*4, 0), 4, 4, color=cc))

for i, cc in enumerate(palette_base):
    ax.add_patch(
        patches.Rectangle((i*1, 22), 1, 2, color=cc, ec=palette[-1], lw=1))
    ax.text(i*1 + .1, 23, '{:g}'.format(i*360/n_colors), color=palette[-1])

plt.show()


wurstel

# palette = sns.hls_palette(12, l=.5, s=.5)
# palette = sns.husl_palette(5, h=.05)
# a = display_palette(palette)

palette = [
    colorsys.hls_to_rgb(i*15/360., 0.5, 1)
    for i in range(24)]
print palette
sns.palplot(palette)

palette = sns.hls_palette(24, h=0, l=.5, s=1)
print palette
sns.palplot(palette)

palette = rgb_to_mplrgb(RGB)
b = display_palette(palette)


# fig, (ax1) = plt.subplots(1, figsize=(16, 9))
# ax1.plot(a, '-o')
# ax1.plot(b, '--o')
# ax1.legend(['h', 'l', 's', 'h', 'l', 's'])

plt.show()


wurstel
# ======================================================================
# ======================================================================
n = 300
theta = np.linspace(0, 2 * np.pi, n)

x = np.cos(theta)
y = np.sin(theta)

f = plt.figure(figsize=(10, 5))
with sns.color_palette("husl", n):
    ax = f.add_subplot(121)
    ax.plot([np.zeros_like(x), x], [np.zeros_like(y), y], lw=3)
    ax.set_axis_off()
    ax.set_title("HUSL space")

with sns.color_palette("hls", n):
    ax = f.add_subplot(122)
    ax.plot([np.zeros_like(x), x], [np.zeros_like(y), y], lw=3)
    ax.set_axis_off()
    ax.set_title("HLS space")

f.tight_layout()


cblue = (0/255., 83/255., 161/255.)
rgb_scale = (255, 255, 255)
hls_scale = (360, 100, 100)

print '\n--> HLS'
palette = sns.color_palette("hls", 12) + [cblue]
palette = sns.hls_palette(12, l=.5, s=.5)
print 'RGB\t HLS'
for p in palette:
    print mcl.rgb2hex(p),
    print ['{:03.2f}'.format(cc * rgb_scale[i])
           for i, cc in enumerate(p)],
    print ['{:03.2f}'.format(cc * hls_scale[i])
           for i, cc in enumerate(colorsys.rgb_to_hls(*p))]
    # print ['{:1.2f}'.format(cc * hls_scale[i])
    #        for i, cc in enumerate(mcl.rgb_to_hsv(p))]
sns.palplot(palette)


# In[3]:
print '\n\n--> HUSL'
palette = sns.color_palette("husl", 12) + [cblue]
palette = sns.husl_palette(12, s=.5, l=.5)
print 'RGB\t HLS'
for p in palette:
    print mcl.rgb2hex(p),
    print ['{:03.2f}'.format(cc * rgb_scale[i])
           for i, cc in enumerate(p)],
    print ['{:03.2f}'.format(cc * hls_scale[i])
           for i, cc in enumerate(colorsys.rgb_to_hls(*p))]
    # print ['{:1.2f}'.format(cc * hls_scale[i])
    #        for i, cc in enumerate(mcl.rgb_to_hsv(p))]
sns.palplot(palette)

sns.husl_palette

plt.show()


wurstel


# In[4]:

sns.color_palette("hls", 8)
sns.palplot(sns.color_palette("hls", 8))


# In[5]:

sns.set(rc={"figure.figsize": (6, 6)})
np.random.seed(sum(map(ord, "palettes")))

plt.show()
