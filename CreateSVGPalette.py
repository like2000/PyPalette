import colorsys
import numpy as np
import seaborn as sns
from matplotlib import colors


width = 1440
height = 1080
n_colors = 24.


# HLS SPECTRUM
# ============
print "Angle step: {:g}".format(360/n_colors)
spectrum_array = sns.hls_palette(n_colors, h=0, l=.5, s=1)

# BEIGETONE
# =========
bgcolor = (90/360., 0.85, 0.15)
RGB = [
    map(lambda x: x*255, colorsys.hls_to_rgb(*bgcolor)),
    (176, 102, 96),
    (202, 143, 66),
    (171, 156, 115),
    (94, 119, 3),
    (106, 125, 142),
]
print np.array(colors.hex2color('#c2ccd6'))*255
print colorsys.rgb_to_hls(*colors.hex2color('#c2ccd6'))
print colorsys.rgb_to_hls(236/255., 236/255., 240/255.)
print np.array(colorsys.rgb_to_hls(*bgcolor))*255
palette_array = np.array(RGB) / 255.

# SVG RECTANGLE
# =============
def rectangle(c='#000000', w=100, h=100, x=0, y=0, id=1):
    lines = ('    <rect\n'
             '       style="opacity:1;fill:{:s};fill-opacity:1;stroke:none;stroke-width:0.125;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"\n'.format(c),
             '       id="rectangle-{:d}"\n'.format(id),
             '       width="{:f}"\n'.format(w),
             '       height="{:f}"\n'.format(h),
             '       x="{:f}"\n'.format(x),
             '       y="{:f}" />\n'.format(y))

    return lines


# with open('Palette.svg') as file:
#     lines = file.readlines()
# print lines[0]


header = ('<?xml version="1.0" encoding="UTF-8" standalone="no"?>\n'
          '<!-- Created with Inkscape (http://www.inkscape.org/) -->\n'
          '\n')

base = ('   xmlns:dc="http://purl.org/dc/elements/1.1/"\n'
        '   xmlns:cc="http://creativecommons.org/ns#"\n'
        '   xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#"\n'
        '   xmlns:svg="http://www.w3.org/2000/svg"\n'
        '   xmlns="http://www.w3.org/2000/svg"\n'
        '   xmlns:sodipodi="http://sodipodi.sourceforge.net/DTD/sodipodi-0.dtd"\n'
        '   xmlns:inkscape="http://www.inkscape.org/namespaces/inkscape"\n'
        '   id="HB2016"\n'
        '   width="{:d}"\n'.format(width),
        '   height="{:d}"\n'.format(height),
        '   viewBox="0 0 {:d} {:d}"\n'.format(width, height),
        '   version="1.1"\n'
        '   inkscape:version="0.91 r13725"\n'
        '   sodipodi:docname="Palette.svg">\n'
        '  <defs\n'
        '     id="defs4" />\n'
        '  <sodipodi:namedview\n'
        '     id="base"\n'
        '     showgrid="false"\n'
        '     inkscape:zoom="1"\n'
        '     inkscape:cx="720"\n'
        '     inkscape:cy="540"\n'
        '     inkscape:window-width="1440"\n'
        '     inkscape:window-height="1080"\n'
        '     inkscape:window-x="0"\n'
        '     inkscape:window-y="0"\n'
        '     inkscape:window-maximized="1"\n'
        '     inkscape:current-layer="layer1" />\n'
        '  <metadata\n'
        '     id="metadata7">\n'
        '    <rdf:RDF>\n'
        '      <cc:Work\n'
        '         rdf:about="">\n'
        '        <dc:format>image/svg+xml</dc:format>\n'
        '        <dc:type\n'
        '           rdf:resource="http://purl.org/dc/dcmitype/StillImage" />\n'
        '        <dc:title></dc:title>\n'
        '      </cc:Work>\n'
        '    </rdf:RDF>\n'
        '  </metadata>\n'
        '  <g\n'
        '     id="layer1"\n'
        '     inkscape:label="Base"\n'
        '     inkscape:groupmode="layer">\n'
        '    <rect\n'
        '       style="opacity:1;fill:{:s};fill-opacity:1;stroke:none;stroke-width:0.125;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"\n'.format(colors.rgb2hex(colorsys.hls_to_rgb(*bgcolor))),
        '       id="rectangle base"\n'
        '       width="{:d}"\n'.format(width),
        '       height="{:d}"\n'.format(height),
        '       x="0"\n'
        '       y="0" />\n'
        '  </g>\n')

spectrum = ('  <g\n'
            '     id="layer2"\n'
            '     inkscape:label="Spectrum"\n'
            '     inkscape:groupmode="layer">\n' + ''.join(sum(
                [rectangle(
                    c=colors.rgb2hex(spectrum_array[i]),
                    w=width/24, h=width/24,
                    x=(i % 24)*width/24, y=2*(i/24)*width/24)
                 for i in range(int(n_colors))], ())) +
            '  </g>\n')

palette = ('  <g\n'
           '     id="layer3"\n'
           '     inkscape:label="Palette"\n'
           '     inkscape:groupmode="layer">\n' + ''.join(sum(
               [rectangle(
                   c=colors.rgb2hex(cc),
                   w=100, h=100, x=i*100, y=height-100)
                for i, cc in enumerate(palette_array)], ())) +
           '  </g>\n')

logo = ('  <g\n'
        '     id="layer10"\n'
        '     inkscape:label="Logo"\n'
        '     inkscape:groupmode="layer">\n'
        '    <g\n'
        '       id="logo"\n'
        '       transform="matrix(0.7598277,0,0,0.7598277,10.000226,9.2402816)">\n'
        '      <path\n'
        '         id="cern-1"\n'
        '         d="m 38.544,76.536 c -0.921,0.7 -4.123,2.692 -8.941,2.692 -8.718,0 -14.658,-5.495 -14.658,-13.872 0,-8.328 6.298,-13.87 14.862,-13.87 3.332,0 7.147,1.026 9.275,1.939 -0.445,0.985 -0.811,2.286 -0.965,3.1 l -0.233,0.077 C 36.237,54.779 33.589,53.2 29.671,53.2 c -4.972,0 -10.696,4.027 -10.696,12.056 0,7.819 5.832,11.974 11.046,11.974 4.684,0 6.927,-2.186 8.939,-3.885 l 0.154,0.154 -0.57,3.037 z"\n'
        '         inkscape:connector-curvature="0"\n'
        '         style="fill:#0053a1" />\n'
        '      <path\n'
        '         id="cern-2"\n'
        '         d="m 60.139,77.312 c 0,-0.588 0.05,-1.193 0.092,-1.487 -2.644,0.243 -9.903,0.463 -12.734,0.504 -0.048,-0.707 -0.11,-9.091 -0.04,-10.387 1.132,0 7.114,0.078 9.787,0.35 -0.077,-0.388 -0.116,-0.962 -0.116,-1.35 0,-0.387 0.039,-1.082 0.116,-1.469 -2.286,0.193 -5.214,0.387 -9.787,0.387 0,-0.969 0.079,-8.037 0.118,-9.701 5.036,0 9.596,0.313 12.148,0.504 -0.042,-0.264 -0.092,-0.807 -0.092,-1.337 0,-0.528 0.035,-0.958 0.092,-1.322 -1.342,0.09 -5.678,0.195 -8.003,0.195 -2.324,0 -5.913,-0.078 -8.237,-0.195 0.154,3.294 0.311,6.664 0.311,9.997 l 0,6.664 c 0,3.333 -0.156,6.704 -0.311,10.075 2.363,-0.117 5.99,-0.194 8.354,-0.194 0.111,0 0.227,0 0.343,0 0.81,0.003 1.835,0.014 2.893,0.033 1.833,0.034 3.767,0.089 5.159,0.161 l 0,0 0,0 c -0.059,-0.409 -0.093,-0.841 -0.093,-1.428 z"\n'
        '         inkscape:connector-curvature="0"\n'
        '         style="fill:#0053a1" />\n'
        '      <path\n'
        '         id="cern-3"\n'
        '         d="m 68.815,65.622 0,3.082 c 0,3.332 0.154,6.701 0.311,10.034 -0.66,-0.117 -1.852,-0.128 -2.096,-0.128 -0.243,0 -1.435,0.012 -2.094,0.128 0.155,-3.333 0.31,-6.703 0.31,-10.034 l 0,-6.666 c 0,-3.332 -0.155,-6.703 -0.31,-10.035 1.473,0.117 3.336,0.195 4.809,0.195 1.473,0 2.945,-0.195 4.417,-0.195 4.379,0 8.39,1.293 8.39,6.169 0,5.161 -5.14,7.013 -8.085,7.401 1.899,2.363 8.7,10.646 10.947,13.165 -0.774,-0.117 -2.073,-0.128 -2.427,-0.128 -0.354,0 -1.691,0.012 -2.427,0.128 -1.531,-2.335 -6.437,-9.686 -9.77,-13.117 -0.102,0 -1.975,0.001 -1.975,0.001 z m 2.596,-1.418 c 3.199,-0.065 7.4,-1.081 7.4,-5.502 0,-3.852 -3.371,-5.076 -6.005,-5.076 -1.782,0 -2.945,0.116 -3.758,0.193 -0.117,2.829 -0.232,5.428 -0.232,8.218 0,0 0,1.851 0,2.131 0.384,0.053 2.2,0.042 2.595,0.036 z"\n'
        '         inkscape:connector-curvature="0"\n'
        '         style="fill:#0053a1" />\n'
        '      <path\n'
        '         id="cern-4"\n'
        '         d="m 112.594,51.99 c -0.453,0.078 -1.013,0.142 -1.699,0.142 -0.676,0 -1.257,-0.073 -1.651,-0.142 0.17,3.174 0.462,9.047 0.462,12.899 0,2.898 0,5.428 -0.04,6.862 C 108.257,70.252 92.09,53.521 90.447,51.735 l -1.269,-0.013 c 0.057,2.465 0.129,5.141 0.129,10.022 0,6.249 -0.087,12.896 -0.406,16.994 0.453,-0.079 1.012,-0.142 1.698,-0.142 0.677,0 1.257,0.071 1.65,0.142 -0.169,-3.173 -0.461,-9.048 -0.461,-12.898 0,-2.899 0.002,-5.882 0.041,-7.314 1.409,1.5 17.667,18.458 19.218,20.561 l 1.269,0.012 c -0.058,-2.465 -0.129,-5.234 -0.129,-10.116 0,-6.249 0.088,-12.898 0.407,-16.993 z"\n'
        '         inkscape:connector-curvature="0"\n'
        '         style="fill:#0053a1" />\n'
        '      <path\n'
        '         id="cern-5"\n'
        '         d="M 42.069,121.789 C 34.455,109.741 32.288,98.11 31.985,89.209 c -1.173,0 -2.346,0 -3.519,0 0.295,9.71 2.65,19.893 7.919,29.872 1.242,1.002 4.159,2.277 5.684,2.708 z"\n'
        '         inkscape:connector-curvature="0"\n'
        '         style="fill:#0053a1" />\n'
        '      <path\n'
        '         id="cern-6"\n'
        '         d="M 184.25,1.679 C 184.25,1.679 96.696,0.985 68.78,1 64.411,1.003 61.478,1.311 60.532,1.371 26.048,3.605 0.115,33.842 0,66.817 c -0.032,9.586 2.522,20.39 6.667,34.973 5.476,19.267 11.891,41.367 11.891,41.367 l 3.499,0 L 9.128,99.539 9.225,99.474 c 9.497,18.347 31.392,33.086 56.237,33.086 13.407,0 25.841,-3.753 35.638,-10.666 l 0.085,0.08 -57.516,61.204 4.492,0 c 0,0 40.387,-42.968 54.125,-57.556 10.527,-11.178 15.996,-18.381 18.285,-22.119 2.625,-4.287 10.964,-16.645 10.652,-34.847 l 0.112,-0.008 25.203,114.529 3.618,0 c 0,0 -21.146,-93.744 -25.25,-113.349 -4.038,-19.292 -8.809,-31.258 -13.957,-38.083 -1.769,-0.985 -4.527,-2.107 -5.828,-2.411 7.472,9.428 13.055,23.454 13.055,37.489 0,34.355 -27.95,62.304 -62.306,62.304 -34.354,0 -62.304,-27.949 -62.304,-62.304 0,-34.356 28.05,-62.306 62.324,-62.306 15.235,0 29.356,5.588 40.209,14.79 2.098,0.29 4.91,0.945 6.589,1.551 l 0.013,-0.035 C 104.902,13.046 95.163,7.265 84.33,4.225 c 0,-0.084 0,-0.089 0,-0.089 l 99.922,0.623 -0.002,-3.08 z"\n'
        '         inkscape:connector-curvature="0"\n'
        '         style="fill:#0053a1" />\n'
        '      <path\n'
        '         id="cern-7"\n'
        '         d="m 50.808,132.873 c -2.228,-0.329 -5.011,-1.118 -6.685,-1.836 7.5,8.536 17.82,15.366 27.953,19.198 l 2.659,-2.821 C 63.744,143.702 55.756,137.737 50.808,132.873"\n'
        '         inkscape:connector-curvature="0"\n'
        '         style="fill:#0053a1" />\n'
        '      <path\n'
        '         id="cern-8"\n'
        '         d="m 142.469,127.885 c -11.121,13.615 -28.388,22.783 -48.226,22.771 -4.259,-0.001 -8.391,-0.478 -11.836,-1.179 l -2.847,3.022 c 5.445,1.258 10.271,1.731 14.885,1.731 20.405,0 37.861,-9.523 48.972,-22.057 l -0.948,-4.288"\n'
        '         inkscape:connector-curvature="0"\n'
        '         style="fill:#0053a1" />\n'
        '      <path\n'
        '         id="cern-9"\n'
        '         d="m 165.644,17.304 -6.001,61.965 -0.113,0 C 158.679,67.573 152.848,53.603 145.647,44.771 133.147,29.442 114.805,20.186 94.203,20.186 c -19.647,0 -37.15,8.717 -49.192,22.381 l 2.758,2.186 C 59.145,31.888 75.442,23.643 94.2,23.643 c 22.836,0 41.439,11.704 51.845,27.615 9.286,14.197 12.365,32.39 10.213,45.719 -0.727,4.502 -2.36,13.257 -8.359,23.176 l 1.05,4.614 c 7.358,-11.405 11.091,-21.556 14.005,-47.503 2.234,-19.906 6.073,-59.962 6.073,-59.962 l -3.383,0.002 z"\n'
        '         inkscape:connector-curvature="0"\n'
        '         style="fill:#0053a1" />\n'
        '    </g>\n'
        '  </g>\n')

with open("Output.svg", 'w') as file:
    file.writelines(header)
    file.writelines('<svg\n')
    file.writelines(base)
    file.writelines(spectrum)
    file.writelines(palette)
    file.writelines('</svg>')
